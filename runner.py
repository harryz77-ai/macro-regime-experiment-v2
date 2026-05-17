#!/usr/bin/env python3
"""
Macro Regime Runner v2

Purpose
-------
Fetch macro-market data, compute a cross-asset observation vector, classify the
current R0/R1/R2/R3 macro regime, and write Markdown + JSON outputs.

Design discipline
-----------------
- No LLM call.
- Deterministic feature engineering and rule scoring.
- Optional robust statistical layer:
  1. Student-t observation filter with Markov transition smoothing.
  2. Robust change-point / abnormality risk score.
  3. Ensemble probability with transparent fallbacks.
- Suitable for GitHub Actions or VPS cron.

This is a monitoring and research tool, not an automatic trading system.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
import pandas as pd


FRED_SERIES = {
    "us2y": "DGS2",
    "us10y": "DGS10",
    "us30y": "DGS30",
    "hy_oas": "BAMLH0A0HYM2",
    "ig_oas": "BAMLC0A0CM",
}

YAHOO_TICKERS = {
    "dxy": "DX-Y.NYB",
    "spy": "SPY",
    "qqq": "QQQ",
    "iwm": "IWM",
    "tlt": "TLT",
    "uup": "UUP",
    "eem": "EEM",
    "hyg": "HYG",
    "lqd": "LQD",
}

REGIME_NAMES = {
    "R0": "High-rate absorption",
    "R1": "Bear steepening + dollar pressure",
    "R2": "Credit / sovereign stress spillover",
    "R3": "Rate decline / policy repair",
}

REGIME_CN = {
    "R0": "高利率吸收",
    "R1": "熊市陡峭化 + 美元压力",
    "R2": "信用 / 主权压力外溢",
    "R3": "利率下行 / 政策修复",
}

# Research prior. Replace only after walk-forward calibration.
TRANSITION_MATRIX = {
    "R0": {"R0": 0.55, "R1": 0.25, "R2": 0.06, "R3": 0.14},
    "R1": {"R0": 0.25, "R1": 0.43, "R2": 0.18, "R3": 0.14},
    "R2": {"R0": 0.10, "R1": 0.18, "R2": 0.38, "R3": 0.34},
    "R3": {"R0": 0.42, "R1": 0.20, "R2": 0.08, "R3": 0.30},
}

MODEL_FEATURE_COLUMNS = [
    "us10y_20d_change_bp",
    "us30y_20d_change_bp",
    "curve_10y2y",
    "curve_30y10y",
    "dxy_20d_return",
    "spy_20d_return",
    "qqq_20d_return",
    "iwm_spy_20d_relative",
    "eem_spy_20d_relative",
    "tlt_20d_return",
    "hyg_20d_return",
    "hy_oas_20d_change_bp",
    "ig_oas_20d_change_bp",
]


@dataclass
class SeriesResult:
    name: str
    source: str
    series: Optional[pd.Series]
    error: Optional[str] = None


# ---------------------------------------------------------------------------
# Fetching and series utilities
# ---------------------------------------------------------------------------

def import_optional_modules() -> Dict[str, Any]:
    modules: Dict[str, Any] = {}
    try:
        import yfinance as yf  # type: ignore
        modules["yf"] = yf
    except Exception as exc:  # pragma: no cover - depends on environment
        modules["yf"] = None
        modules["yf_error"] = str(exc)
    return modules


def clean_series(series: pd.Series) -> pd.Series:
    s = pd.to_numeric(series, errors="coerce").dropna()
    s.index = pd.to_datetime(s.index).tz_localize(None)
    return s.sort_index()


def fetch_fred_series(name: str, series_id: str, start: str) -> SeriesResult:
    """Fetch FRED series through the public CSV endpoint."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    try:
        df = pd.read_csv(url)
        if df.empty:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No data returned for {series_id}")

        date_col = "observation_date" if "observation_date" in df.columns else "DATE" if "DATE" in df.columns else None
        if date_col is None:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No date column found for {series_id}")

        value_col = series_id if series_id in df.columns else next((c for c in df.columns if c != date_col), None)
        if value_col is None:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No value column found for {series_id}")

        dates = pd.to_datetime(df[date_col], errors="coerce")
        values = pd.to_numeric(df[value_col].replace(".", np.nan), errors="coerce")
        s = pd.Series(values.to_numpy(), index=dates).dropna().sort_index()
        if start:
            s = s[s.index >= pd.Timestamp(start)]
        if s.empty:
            return SeriesResult(name, f"FRED:{series_id}", None, f"No non-missing observations after {start}")
        return SeriesResult(name, f"FRED:{series_id}", clean_series(s), None)
    except Exception as exc:  # pragma: no cover - network dependent
        return SeriesResult(name, f"FRED:{series_id}", None, str(exc))


def fetch_yahoo_series(ticker: str, period: str, yf: Any) -> Tuple[Optional[pd.Series], Optional[str]]:
    if yf is None:
        return None, "yfinance is not installed"
    try:
        df = yf.download(ticker, period=period, auto_adjust=True, progress=False, threads=False)
        if df is None or df.empty:
            return None, f"No Yahoo data returned for {ticker}"
        if isinstance(df.columns, pd.MultiIndex):
            if ("Close", ticker) in df.columns:
                raw = df[("Close", ticker)]
            else:
                raw = df.xs("Close", axis=1, level=0).iloc[:, 0]
        else:
            raw = df["Close"]
        return clean_series(raw), None
    except Exception as exc:  # pragma: no cover - network dependent
        return None, str(exc)


def fetch_yahoo_data(tickers: Dict[str, str], period: str, yf: Any) -> Dict[str, SeriesResult]:
    results: Dict[str, SeriesResult] = {}
    for name, ticker in tickers.items():
        s, err = fetch_yahoo_series(ticker, period, yf)
        results[name] = SeriesResult(name, f"Yahoo:{ticker}", s, err)
    return results


def latest(series: Optional[pd.Series]) -> Optional[float]:
    if series is None or series.empty:
        return None
    return float(series.iloc[-1])


def latest_date(series: Optional[pd.Series]) -> Optional[str]:
    if series is None or series.empty:
        return None
    return pd.Timestamp(series.index[-1]).date().isoformat()


def pct_change(series: Optional[pd.Series], days: int) -> Optional[float]:
    if series is None or len(series) <= days:
        return None
    return float((series.iloc[-1] / series.iloc[-days - 1] - 1.0) * 100.0)


def bp_change(series: Optional[pd.Series], days: int) -> Optional[float]:
    if series is None or len(series) <= days:
        return None
    return float((series.iloc[-1] - series.iloc[-days - 1]) * 100.0)


def safe_subtract(a: Optional[float], b: Optional[float]) -> Optional[float]:
    if a is None or b is None:
        return None
    return float(a - b)


def business_days_old(date_str: Optional[str]) -> Optional[int]:
    if date_str is None:
        return None
    today = pd.Timestamp.utcnow().normalize().tz_localize(None)
    d = pd.Timestamp(date_str).normalize().tz_localize(None)
    if d > today:
        return 0
    return int(len(pd.bdate_range(d + pd.Timedelta(days=1), today)))


def freshness_from_date(date_str: Optional[str]) -> str:
    age = business_days_old(date_str)
    if age is None:
        return "Missing"
    if age <= 1:
        return "Fresh"
    if age <= 3:
        return "Acceptable"
    return "Stale"


# ---------------------------------------------------------------------------
# Feature engineering
# ---------------------------------------------------------------------------

def build_features(
    fred: Dict[str, SeriesResult],
    yahoo: Dict[str, SeriesResult],
    sovereign_spread_change_bp: Optional[float] = None,
) -> Dict[str, Optional[float]]:
    features: Dict[str, Optional[float]] = {}

    features["us2y_level"] = latest(fred.get("us2y").series if fred.get("us2y") else None)
    features["us10y_level"] = latest(fred.get("us10y").series if fred.get("us10y") else None)
    features["us30y_level"] = latest(fred.get("us30y").series if fred.get("us30y") else None)

    for tenor in ["us10y", "us30y"]:
        s = fred.get(tenor).series if fred.get(tenor) else None
        for window in [5, 20, 60]:
            features[f"{tenor}_{window}d_change_bp"] = bp_change(s, window)

    features["curve_10y2y"] = safe_subtract(features["us10y_level"], features["us2y_level"])
    features["curve_30y10y"] = safe_subtract(features["us30y_level"], features["us10y_level"])

    for name in ["hy_oas", "ig_oas"]:
        s = fred.get(name).series if fred.get(name) else None
        features[f"{name}_level"] = latest(s)
        for window in [5, 20, 60]:
            features[f"{name}_{window}d_change_bp"] = bp_change(s, window)

    for name, result in yahoo.items():
        s = result.series
        features[f"{name}_latest"] = latest(s)
        for window in [5, 20, 60]:
            features[f"{name}_{window}d_return"] = pct_change(s, window)

    features["iwm_spy_20d_relative"] = safe_subtract(features.get("iwm_20d_return"), features.get("spy_20d_return"))
    features["eem_spy_20d_relative"] = safe_subtract(features.get("eem_20d_return"), features.get("spy_20d_return"))
    features["qqq_spy_20d_relative"] = safe_subtract(features.get("qqq_20d_return"), features.get("spy_20d_return"))
    features["sovereign_spread_change_bp"] = sovereign_spread_change_bp
    return features


def _series_or_none(results: Dict[str, SeriesResult], name: str) -> Optional[pd.Series]:
    r = results.get(name)
    return r.series if r else None


def build_historical_feature_frame(
    fred: Dict[str, SeriesResult],
    yahoo: Dict[str, SeriesResult],
    sovereign_spread_change_bp: Optional[float] = None,
) -> pd.DataFrame:
    """Build a daily feature panel used by robust statistical diagnostics."""
    cols: Dict[str, pd.Series] = {}

    for name in ["us2y", "us10y", "us30y", "hy_oas", "ig_oas"]:
        s = _series_or_none(fred, name)
        if s is not None and not s.empty:
            if name in ["us2y", "us10y", "us30y"]:
                cols[f"{name}_level"] = s
            else:
                cols[f"{name}_level"] = s
            for window in [5, 20, 60]:
                suffix = "change_bp"
                cols[f"{name}_{window}d_{suffix}"] = (s - s.shift(window)) * 100.0

    if "us10y_level" in cols and "us2y_level" in cols:
        cols["curve_10y2y"] = cols["us10y_level"] - cols["us2y_level"]
    if "us30y_level" in cols and "us10y_level" in cols:
        cols["curve_30y10y"] = cols["us30y_level"] - cols["us10y_level"]

    for name, result in yahoo.items():
        s = result.series
        if s is None or s.empty:
            continue
        cols[f"{name}_latest"] = s
        for window in [5, 20, 60]:
            cols[f"{name}_{window}d_return"] = (s / s.shift(window) - 1.0) * 100.0

    df = pd.DataFrame(cols).sort_index()
    if not df.empty:
        df = df.ffill(limit=3)
        if "iwm_20d_return" in df and "spy_20d_return" in df:
            df["iwm_spy_20d_relative"] = df["iwm_20d_return"] - df["spy_20d_return"]
        if "eem_20d_return" in df and "spy_20d_return" in df:
            df["eem_spy_20d_relative"] = df["eem_20d_return"] - df["spy_20d_return"]
        if "qqq_20d_return" in df and "spy_20d_return" in df:
            df["qqq_spy_20d_relative"] = df["qqq_20d_return"] - df["spy_20d_return"]
        if sovereign_spread_change_bp is not None:
            df["sovereign_spread_change_bp"] = sovereign_spread_change_bp
    return df


# ---------------------------------------------------------------------------
# Rule engine
# ---------------------------------------------------------------------------

def softmax(scores: Dict[str, int], temperature: float = 1.25) -> Dict[str, float]:
    labels = list(scores.keys())
    values = np.array([scores[k] for k in labels], dtype=float) / float(temperature)
    exp_values = np.exp(values - np.max(values))
    probs = exp_values / exp_values.sum()
    return {k: float(v) for k, v in zip(labels, probs)}


def classify_regime(
    features: Dict[str, Optional[float]],
    previous_regime: Optional[str] = None,
    temperature: float = 1.25,
) -> Dict[str, Any]:
    scores = {"R0": 0, "R1": 0, "R2": 0, "R3": 0}
    evidence: Dict[str, List[str]] = {"R0": [], "R1": [], "R2": [], "R3": []}

    def record(regime: str, condition: bool, text: str, points: int = 1) -> None:
        if condition:
            scores[regime] += points
            evidence[regime].append(text if points == 1 else f"{text} (+{points})")

    us10y = features.get("us10y_level")
    us30y = features.get("us30y_level")
    us10y_20d = features.get("us10y_20d_change_bp")
    us30y_20d = features.get("us30y_20d_change_bp")
    dxy_20d = features.get("dxy_20d_return")
    spy_20d = features.get("spy_20d_return")
    qqq_20d = features.get("qqq_20d_return")
    iwm_spy = features.get("iwm_spy_20d_relative")
    eem_spy = features.get("eem_spy_20d_relative")
    tlt_20d = features.get("tlt_20d_return")
    hyg_20d = features.get("hyg_20d_return")
    hy_oas_20d = features.get("hy_oas_20d_change_bp")
    sov_20d = features.get("sovereign_spread_change_bp")

    # R0: high rate, absorption, no credit disorder.
    record("R0", us10y is not None and us10y >= 4.0 and us10y_20d is not None and abs(us10y_20d) < 20,
           "10Y yield is high but not accelerating")
    record("R0", spy_20d is not None and spy_20d > 0 and hy_oas_20d is not None and hy_oas_20d < 20,
           "equity resilience with stable credit")
    record("R0", dxy_20d is not None and abs(dxy_20d) < 1.0,
           "DXY is stable")

    # R1: bear steepening + dollar pressure without credit disorder.
    record("R1", us10y_20d is not None and us10y_20d > 20,
           "10Y yield rose meaningfully over 20D")
    record("R1", us30y_20d is not None and us30y_20d > 25,
           "30Y yield rose meaningfully over 20D")
    record("R1", dxy_20d is not None and dxy_20d > 1.0,
           "DXY strengthened over 20D")
    record("R1", iwm_spy is not None and iwm_spy < -2.0,
           "IWM underperformed SPY over 20D")
    record("R1", eem_spy is not None and eem_spy < -2.0,
           "EEM underperformed SPY over 20D")
    record("R1", tlt_20d is not None and tlt_20d < -3.0,
           "TLT sold off over 20D")
    record("R1", hy_oas_20d is not None and hy_oas_20d < 50,
           "credit spread pressure is not yet disorderly")

    # R2: credit / sovereign stress spillover.
    record("R2", hy_oas_20d is not None and hy_oas_20d > 75,
           "HY OAS widened sharply over 20D", 2)
    record("R2", hyg_20d is not None and hyg_20d < -3.0,
           "HYG sold off quickly over 20D")
    record("R2", spy_20d is not None and iwm_spy is not None and spy_20d < -5.0 and iwm_spy < -3.0,
           "broad equity drawdown plus small-cap underperformance")
    record("R2", dxy_20d is not None and eem_spy is not None and dxy_20d > 3.0 and eem_spy < -4.0,
           "DXY spike plus EM underperformance")
    record("R2", sov_20d is not None and sov_20d > 40,
           "sovereign spread widened sharply", 2)

    # R3: rate decline / policy repair.
    record("R3", us10y_20d is not None and us30y_20d is not None and us10y_20d < -25 and us30y_20d < -25,
           "10Y and 30Y yields fell materially over 20D")
    record("R3", tlt_20d is not None and tlt_20d > 4.0,
           "TLT rallied over 20D")
    record("R3", dxy_20d is not None and dxy_20d < -1.5,
           "DXY weakened over 20D")
    record("R3", hy_oas_20d is not None and hy_oas_20d < -25,
           "HY OAS narrowed over 20D")
    record("R3", spy_20d is not None and qqq_20d is not None and spy_20d > 3.0 and qqq_20d > 3.0,
           "SPY and QQQ rallied over 20D")

    signal_probs = softmax(scores, temperature=temperature)

    if previous_regime in TRANSITION_MATRIX:
        prior = TRANSITION_MATRIX[previous_regime]
        posterior = {k: float(0.65 * signal_probs[k] + 0.35 * prior[k]) for k in signal_probs}
    else:
        prior = None
        posterior = signal_probs.copy()

    top_regime = max(posterior, key=posterior.get)
    return {
        "scores": scores,
        "evidence": evidence,
        "signal_probability": signal_probs,
        "markov_prior": prior,
        "posterior_probability": posterior,
        "top_regime": top_regime,
    }


# ---------------------------------------------------------------------------
# Robust statistical layer
# ---------------------------------------------------------------------------

def finite_float(x: Any) -> Optional[float]:
    try:
        y = float(x)
    except Exception:
        return None
    if math.isnan(y) or math.isinf(y):
        return None
    return y


def normalize_prob_dict(probs: Dict[str, float]) -> Dict[str, float]:
    clean = {k: max(0.0, float(v)) for k, v in probs.items()}
    total = sum(clean.values())
    if total <= 0:
        return {k: 1.0 / len(clean) for k in clean}
    return {k: v / total for k, v in clean.items()}


def robust_center_scale(df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
    center = df.median(skipna=True)
    mad = (df - center).abs().median(skipna=True)
    scale = 1.4826 * mad
    std = df.std(skipna=True)
    scale = scale.where(scale > 1e-9, std)
    scale = scale.where(scale > 1e-9, 1.0)
    center = center.fillna(0.0)
    scale = scale.fillna(1.0)
    return center, scale


def student_t_logpdf_diag(x: np.ndarray, mu: np.ndarray, scale: np.ndarray, nu: float = 5.0) -> float:
    """Diagonal Student-t log density. Robust against heavy-tailed observations."""
    scale = np.maximum(scale, 1e-6)
    z = (x - mu) / scale
    c = math.lgamma((nu + 1.0) / 2.0) - math.lgamma(nu / 2.0) - 0.5 * math.log(nu * math.pi)
    return float(np.sum(c - np.log(scale) - ((nu + 1.0) / 2.0) * np.log1p((z * z) / nu)))


def row_to_feature_dict(row: pd.Series) -> Dict[str, Optional[float]]:
    out: Dict[str, Optional[float]] = {}
    for k, v in row.items():
        out[k] = finite_float(v)
    return out


def transition_array() -> Tuple[List[str], np.ndarray]:
    states = ["R0", "R1", "R2", "R3"]
    mat = np.array([[TRANSITION_MATRIX[s][t] for t in states] for s in states], dtype=float)
    mat = mat / mat.sum(axis=1, keepdims=True)
    return states, mat


def run_student_t_filter(
    panel: pd.DataFrame,
    previous_regime: Optional[str],
    temperature: float,
    min_rows: int = 80,
) -> Dict[str, Any]:
    """
    Robust HMM-like filter.

    It uses rule-derived pseudo labels to estimate Student-t observation centers
    and scales for each macro regime, then applies Markov forward filtering.
    This is intentionally transparent and dependency-light; it is not an EM-fit
    black-box HMM.
    """
    available_cols = [c for c in MODEL_FEATURE_COLUMNS if c in panel.columns]
    diagnostics: Dict[str, Any] = {
        "method": "Student-t observation filter + Markov transition smoothing",
        "available_feature_count": len(available_cols),
        "required_min_rows": min_rows,
        "used": False,
        "warnings": [],
    }
    default_probs = {"R0": 0.25, "R1": 0.25, "R2": 0.25, "R3": 0.25}

    if len(available_cols) < 6:
        diagnostics["warnings"].append("Too few statistical features available.")
        return {"probability": default_probs, "diagnostics": diagnostics}

    model_df = panel[available_cols].copy()
    model_df = model_df.dropna(thresh=max(4, int(0.55 * len(available_cols))))
    if len(model_df) < min_rows:
        diagnostics["warnings"].append(f"Only {len(model_df)} usable rows; statistical filter is not trusted.")
        return {"probability": default_probs, "diagnostics": diagnostics}

    global_center, global_scale = robust_center_scale(model_df)
    imputed = model_df.fillna(global_center)

    labels: List[str] = []
    for _, row in imputed.iterrows():
        f = row_to_feature_dict(row)
        cls = classify_regime(f, previous_regime=None, temperature=temperature)
        labels.append(cls["top_regime"])

    labeled = imputed.copy()
    labeled["_label"] = labels

    states, transition = transition_array()
    centers: Dict[str, np.ndarray] = {}
    scales: Dict[str, np.ndarray] = {}
    counts: Dict[str, int] = {}

    for state in states:
        sub = labeled[labeled["_label"] == state].drop(columns=["_label"])
        counts[state] = int(len(sub))
        if len(sub) >= 8:
            c, s = robust_center_scale(sub)
        else:
            c, s = global_center, global_scale
            diagnostics["warnings"].append(f"State {state} has only {len(sub)} pseudo-labeled rows; using global robust scale.")
        centers[state] = c.reindex(available_cols).to_numpy(dtype=float)
        scales[state] = s.reindex(available_cols).to_numpy(dtype=float)

    if previous_regime in states:
        alpha = np.array([1.0 if s == previous_regime else 0.0 for s in states], dtype=float)
    else:
        alpha = np.ones(len(states), dtype=float) / len(states)

    xs = imputed[available_cols].to_numpy(dtype=float)
    latest_loglik: Dict[str, float] = {}
    for x in xs:
        loglik = np.array([
            student_t_logpdf_diag(x, centers[s], scales[s], nu=5.0)
            for s in states
        ], dtype=float)
        pred = alpha @ transition
        emission = np.exp(loglik - np.max(loglik))
        alpha = pred * emission
        if alpha.sum() <= 0 or not np.isfinite(alpha).all():
            alpha = np.ones(len(states), dtype=float) / len(states)
        else:
            alpha = alpha / alpha.sum()
        latest_loglik = {s: float(v) for s, v in zip(states, loglik)}

    probs = {s: float(v) for s, v in zip(states, alpha)}
    diagnostics.update({
        "used": True,
        "usable_rows": int(len(imputed)),
        "available_features": available_cols,
        "pseudo_label_counts": counts,
        "latest_log_likelihood": latest_loglik,
        "top_regime": max(probs, key=probs.get),
    })
    return {"probability": normalize_prob_dict(probs), "diagnostics": diagnostics}


def sigmoid(x: float) -> float:
    try:
        return float(1.0 / (1.0 + math.exp(-x)))
    except OverflowError:
        return 0.0 if x < 0 else 1.0


def robust_change_point_score(panel: pd.DataFrame) -> Dict[str, Any]:
    """Robust abnormality score for detecting abrupt R1->R2 style transition risk."""
    available_cols = [c for c in MODEL_FEATURE_COLUMNS if c in panel.columns]
    out: Dict[str, Any] = {
        "method": "robust trailing-window abnormality score",
        "used": False,
        "risk_score": 0.0,
        "risk_level": "not_available",
        "distance": None,
        "warnings": [],
    }
    if len(available_cols) < 6 or panel.empty:
        out["warnings"].append("Too few features for change-point scoring.")
        return out

    model_df = panel[available_cols].dropna(thresh=max(4, int(0.55 * len(available_cols))))
    if len(model_df) < 60:
        out["warnings"].append(f"Only {len(model_df)} usable rows; change-point score is weak.")
        return out

    trailing = model_df.tail(126)
    latest_row = trailing.iloc[-1]
    baseline = trailing.iloc[:-1] if len(trailing) > 20 else trailing
    center, scale = robust_center_scale(baseline)
    z = ((latest_row.fillna(center) - center) / scale).replace([np.inf, -np.inf], np.nan)
    distance = float(np.sqrt(np.nanmean(np.square(z.to_numpy(dtype=float)))))

    # Credit/liquidity stress votes make the score more sensitive to R2 upgrades.
    f = row_to_feature_dict(latest_row)
    stress_votes = [
        f.get("hy_oas_20d_change_bp") is not None and f["hy_oas_20d_change_bp"] > 50,
        f.get("ig_oas_20d_change_bp") is not None and f["ig_oas_20d_change_bp"] > 20,
        f.get("hyg_20d_return") is not None and f["hyg_20d_return"] < -2.5,
        f.get("spy_20d_return") is not None and f["spy_20d_return"] < -5.0,
        f.get("iwm_spy_20d_relative") is not None and f["iwm_spy_20d_relative"] < -3.0,
        f.get("eem_spy_20d_relative") is not None and f["eem_spy_20d_relative"] < -4.0,
        f.get("dxy_20d_return") is not None and f["dxy_20d_return"] > 2.5,
        f.get("tlt_20d_return") is not None and f["tlt_20d_return"] < -4.0,
    ]
    vote_score = sum(bool(v) for v in stress_votes) / len(stress_votes)
    distance_score = sigmoid((distance - 2.25) / 0.65)
    risk_score = float(min(1.0, max(0.0, 0.65 * distance_score + 0.35 * vote_score)))
    if risk_score >= 0.66:
        level = "high"
    elif risk_score >= 0.40:
        level = "medium"
    else:
        level = "low"

    out.update({
        "used": True,
        "risk_score": risk_score,
        "risk_level": level,
        "distance": distance,
        "stress_vote_count": int(sum(bool(v) for v in stress_votes)),
        "stress_vote_total": int(len(stress_votes)),
        "available_features": available_cols,
    })
    return out


def build_ensemble_probability(
    rule_probs: Dict[str, float],
    stat_probs: Dict[str, float],
    stat_used: bool,
    change_score: Dict[str, Any],
) -> Dict[str, Any]:
    states = ["R0", "R1", "R2", "R3"]
    if stat_used:
        weights = {"rule": 0.60, "stat": 0.30, "change": 0.10}
    else:
        weights = {"rule": 0.90, "stat": 0.00, "change": 0.10}

    change_risk = float(change_score.get("risk_score") or 0.0)
    change_prior = {"R0": 0.20, "R1": 0.25, "R2": 0.45, "R3": 0.10}
    calm_prior = {"R0": 0.38, "R1": 0.34, "R2": 0.08, "R3": 0.20}
    transition_risk_prior = {
        s: change_risk * change_prior[s] + (1.0 - change_risk) * calm_prior[s]
        for s in states
    }
    raw = {
        s: weights["rule"] * rule_probs.get(s, 0.0)
        + weights["stat"] * stat_probs.get(s, 0.0)
        + weights["change"] * transition_risk_prior.get(s, 0.0)
        for s in states
    }

    # Conservative R2 boost only when abnormality is meaningful. This avoids
    # upgrading to crisis regime from rates/equity noise alone.
    if change_risk >= 0.66:
        raw["R2"] += 0.05
    probs = normalize_prob_dict(raw)
    return {
        "probability": probs,
        "top_regime": max(probs, key=probs.get),
        "weights": weights,
        "change_risk_prior": transition_risk_prior,
    }


# ---------------------------------------------------------------------------
# Metadata, alerts, and reporting
# ---------------------------------------------------------------------------

def build_metadata(fred: Dict[str, SeriesResult], yahoo: Dict[str, SeriesResult]) -> Dict[str, Any]:
    items: Dict[str, Any] = {}
    for group_name, group in [("fred", fred), ("yahoo", yahoo)]:
        for name, result in group.items():
            d = latest_date(result.series)
            items[name] = {
                "group": group_name,
                "source": result.source,
                "latest_date": d,
                "freshness": freshness_from_date(d),
                "error": result.error,
            }
    missing = [k for k, v in items.items() if v["latest_date"] is None]
    stale = [k for k, v in items.items() if v["freshness"] == "Stale"]
    latest_dates = [v["latest_date"] for v in items.values() if v["latest_date"] is not None]
    max_date = max(latest_dates) if latest_dates else None
    return {
        "items": items,
        "missing": missing,
        "stale": stale,
        "latest_market_date": max_date,
        "overall_freshness": freshness_from_date(max_date),
    }


def fmt_num(x: Optional[float], digits: int = 2, suffix: str = "") -> str:
    y = finite_float(x)
    if y is None:
        return "missing"
    return f"{y:.{digits}f}{suffix}"


def probability_table(probs: Dict[str, float], title: str = "Probability") -> str:
    rows = [f"| Regime | {title} | Interpretation | 中文解释 |", "|---|---:|---|---|"]
    for regime in ["R0", "R1", "R2", "R3"]:
        rows.append(f"| {regime} | {probs.get(regime, 0.0):.1%} | {REGIME_NAMES[regime]} | {REGIME_CN[regime]} |")
    return "\n".join(rows)


def build_evidence_table(features: Dict[str, Optional[float]]) -> str:
    rows = ["| Indicator | Latest | 5D | 20D | 60D | Regime Signal |", "|---|---:|---:|---:|---:|---|"]
    rows.append(
        f"| US 10Y yield | {fmt_num(features.get('us10y_level'), 3, '%')} | "
        f"{fmt_num(features.get('us10y_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us10y_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us10y_60d_change_bp'), 1, ' bp')} | Long-end rate pressure |"
    )
    rows.append(
        f"| US 30Y yield | {fmt_num(features.get('us30y_level'), 3, '%')} | "
        f"{fmt_num(features.get('us30y_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us30y_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('us30y_60d_change_bp'), 1, ' bp')} | Term premium / fiscal supply pressure |"
    )
    rows.append(
        f"| DXY | {fmt_num(features.get('dxy_latest'), 2)} | "
        f"{fmt_num(features.get('dxy_5d_return'), 2, '%')} | "
        f"{fmt_num(features.get('dxy_20d_return'), 2, '%')} | "
        f"{fmt_num(features.get('dxy_60d_return'), 2, '%')} | Dollar pressure |"
    )
    for name, label, signal in [
        ("spy", "SPY", "Broad risk asset"),
        ("qqq", "QQQ", "High-duration growth"),
        ("iwm", "IWM", "Small-cap financing sensitivity"),
        ("tlt", "TLT", "Long-duration bond stress"),
        ("eem", "EEM", "EM dollar/rate transmission"),
        ("hyg", "HYG", "Credit market proxy"),
        ("lqd", "LQD", "Investment-grade bond ETF"),
    ]:
        rows.append(
            f"| {label} | {fmt_num(features.get(f'{name}_latest'), 2)} | "
            f"{fmt_num(features.get(f'{name}_5d_return'), 2, '%')} | "
            f"{fmt_num(features.get(f'{name}_20d_return'), 2, '%')} | "
            f"{fmt_num(features.get(f'{name}_60d_return'), 2, '%')} | {signal} |"
        )
    rows.append(
        f"| HY OAS | {fmt_num(features.get('hy_oas_level'), 2, '%')} | "
        f"{fmt_num(features.get('hy_oas_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('hy_oas_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('hy_oas_60d_change_bp'), 1, ' bp')} | Credit spread stress |"
    )
    rows.append(
        f"| IG OAS | {fmt_num(features.get('ig_oas_level'), 2, '%')} | "
        f"{fmt_num(features.get('ig_oas_5d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('ig_oas_20d_change_bp'), 1, ' bp')} | "
        f"{fmt_num(features.get('ig_oas_60d_change_bp'), 1, ' bp')} | Investment-grade credit stress |"
    )
    rows.append(f"| IWM - SPY relative | n/a | n/a | {fmt_num(features.get('iwm_spy_20d_relative'), 2, ' pp')} | n/a | Small-cap relative stress |")
    rows.append(f"| EEM - SPY relative | n/a | n/a | {fmt_num(features.get('eem_spy_20d_relative'), 2, ' pp')} | n/a | EM relative stress |")
    return "\n".join(rows)


def build_alerts(features: Dict[str, Optional[float]], rule_classification: Dict[str, Any], ensemble: Dict[str, Any], change: Dict[str, Any]) -> Dict[str, str]:
    r2_prob = ensemble["probability"].get("R2", 0.0)
    us10y = features.get("us10y_level")
    us30y = features.get("us30y_level")
    dxy = features.get("dxy_latest")
    eem_spy = features.get("eem_spy_20d_relative")
    hy_oas_20d = features.get("hy_oas_20d_change_bp")
    hyg_20d = features.get("hyg_20d_return")
    iwm_spy = features.get("iwm_spy_20d_relative")

    r1_conditions = [
        us10y is not None and 4.5 <= us10y <= 5.0,
        us30y is not None and 5.0 <= us30y <= 5.5,
        hy_oas_20d is not None and hy_oas_20d < 50,
        iwm_spy is not None and iwm_spy < 0,
    ]
    r2_conditions = [
        us10y is not None and us10y > 5.0,
        us30y is not None and us30y > 5.5,
        dxy is not None and dxy > 101 and eem_spy is not None and eem_spy < -4,
        hy_oas_20d is not None and hy_oas_20d > 75,
        hyg_20d is not None and hyg_20d < -3.0,
        r2_prob >= 0.30,
        change.get("risk_level") == "high",
    ]
    r3_conditions = [
        features.get("us10y_20d_change_bp") is not None and features["us10y_20d_change_bp"] < -25,
        features.get("us30y_20d_change_bp") is not None and features["us30y_20d_change_bp"] < -25,
        features.get("tlt_20d_return") is not None and features["tlt_20d_return"] > 4,
        hy_oas_20d is not None and hy_oas_20d < -25,
    ]
    return {
        "R1 continuation": "ON" if sum(r1_conditions) >= 2 else "not confirmed",
        "R2 upgrade warning": "ON" if any(r2_conditions) else "not confirmed",
        "R2 transition risk": str(change.get("risk_level", "not_available")),
        "R3 policy-repair signal": "ON" if sum(r3_conditions) >= 2 else "not confirmed",
    }


def generate_markdown(report: Dict[str, Any]) -> str:
    features = report["features"]
    rule = report["rule_classification"]
    stat = report["student_t_filter"]
    change = report["change_point"]
    ensemble = report["ensemble"]
    metadata = report["metadata"]
    alerts = report["alerts"]
    top = ensemble["top_regime"]
    probs = ensemble["probability"]

    evidence_lines = []
    for regime in ["R0", "R1", "R2", "R3"]:
        ev = rule["evidence"].get(regime, [])
        if ev:
            evidence_lines.append(f"- **{regime}**: " + "; ".join(ev))
        else:
            evidence_lines.append(f"- **{regime}**: no strong evidence")

    missing = ", ".join(metadata["missing"]) if metadata["missing"] else "none"
    stale = ", ".join(metadata["stale"]) if metadata["stale"] else "none"
    prior_text = probability_table(rule["markov_prior"], "Prior") if rule.get("markov_prior") else "No Markov prior used because previous regime is unknown or invalid."

    stat_diag = stat.get("diagnostics", {})
    stat_warning_text = "; ".join(stat_diag.get("warnings", [])) if stat_diag.get("warnings") else "none"
    change_warning_text = "; ".join(change.get("warnings", [])) if change.get("warnings") else "none"

    return f"""# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: {report["fetch_time_utc"]}
- Latest market date: {metadata["latest_market_date"]}
- Overall data freshness: {metadata["overall_freshness"]}
- Missing fields: {missing}
- Stale fields: {stale}

## 2. Current Regime Conclusion

- Most likely regime: **{top} — {REGIME_NAMES[top]} / {REGIME_CN[top]}**
- Ensemble probability: **{probs[top]:.1%}**
- Previous regime: {report.get("previous_regime") or "unknown"}
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

{build_evidence_table(features)}

## 4. Ensemble Regime Probability

{probability_table(probs, "Ensemble Probability")}

## 5. Rule Engine Probability

{probability_table(rule["posterior_probability"], "Rule Posterior")}

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **{stat_diag.get("used", False)}**
- Method: {stat_diag.get("method", "not_available")}
- Usable rows: {stat_diag.get("usable_rows", "not_available")}
- Available feature count: {stat_diag.get("available_feature_count", "not_available")}
- Top statistical regime: {stat_diag.get("top_regime", "not_available")}
- Warnings: {stat_warning_text}

{probability_table(stat.get("probability", {"R0": 0.25, "R1": 0.25, "R2": 0.25, "R3": 0.25}), "Student-t Filter Probability")}

### Robust Change-Point / Transition Risk

- Used: **{change.get("used", False)}**
- Risk level: **{change.get("risk_level", "not_available")}**
- Risk score: **{float(change.get("risk_score") or 0.0):.1%}**
- Robust distance: {fmt_num(change.get("distance"), 2)}
- Stress votes: {change.get("stress_vote_count", "n/a")}/{change.get("stress_vote_total", "n/a")}
- Warnings: {change_warning_text}

## 7. Signal Evidence

{chr(10).join(evidence_lines)}

## 8. Markov Prior

{prior_text}

## 9. Risk Alerts

- R1 continuation: **{alerts["R1 continuation"]}**
- R2 upgrade warning: **{alerts["R2 upgrade warning"]}**
- R2 transition risk: **{alerts["R2 transition risk"]}**
- R3 policy-repair signal: **{alerts["R3 policy-repair signal"]}**

## 10. Interpretation

### Verified market data

The report uses FRED for US Treasury yields and credit OAS series, and Yahoo Finance for ETF/index market proxies where available.

### Computed indicators

The system computes 5D, 20D, and 60D changes. ETF/index moves are percentage returns. Yield and spread moves are basis-point changes.

### Model inference

The final state is the highest ensemble probability regime. The ensemble combines:

1. deterministic rule posterior;
2. robust Student-t observation filter with Markov transition smoothing;
3. robust change-point / transition-risk score.

### Judgment discipline

Do not upgrade to R2 from rates and equity weakness alone. R2 requires credit-spread stress, sovereign-spread stress, or synchronized deleveraging across equities, EM, credit, and high-duration assets.

## 11. Next Data to Watch

1. HY OAS 20D change
2. HYG 20D return
3. DXY level and 20D return
4. IWM/SPY and EEM/SPY relative performance
5. US 10Y and 30Y yield levels
6. Change-point risk score and Student-t filter disagreement with the rule engine

"""


def append_history(history_csv: Path, report: Dict[str, Any]) -> None:
    row: Dict[str, Any] = {
        "fetch_time_utc": report["fetch_time_utc"],
        "latest_market_date": report["metadata"]["latest_market_date"],
        "previous_regime": report.get("previous_regime"),
        "top_regime": report["ensemble"]["top_regime"],
        "rule_top_regime": report["rule_classification"]["top_regime"],
        "student_t_top_regime": report["student_t_filter"].get("diagnostics", {}).get("top_regime"),
        "change_point_risk_score": report["change_point"].get("risk_score"),
        "change_point_risk_level": report["change_point"].get("risk_level"),
    }
    for regime, prob in report["ensemble"]["probability"].items():
        row[f"ensemble_prob_{regime}"] = prob
    for regime, prob in report["rule_classification"]["posterior_probability"].items():
        row[f"rule_prob_{regime}"] = prob
    for regime, prob in report["student_t_filter"].get("probability", {}).items():
        row[f"student_t_prob_{regime}"] = prob
    for key in [
        "us10y_level", "us30y_level", "us10y_20d_change_bp", "us30y_20d_change_bp",
        "dxy_20d_return", "spy_20d_return", "qqq_20d_return", "iwm_spy_20d_relative",
        "eem_spy_20d_relative", "tlt_20d_return", "hyg_20d_return", "hy_oas_20d_change_bp",
        "ig_oas_20d_change_bp",
    ]:
        row[key] = report["features"].get(key)

    history_csv.parent.mkdir(parents=True, exist_ok=True)
    df_new = pd.DataFrame([row])
    if history_csv.exists() and history_csv.stat().st_size > 0:
        df_old = pd.read_csv(history_csv)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(history_csv, index=False)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_previous_regime(arg: Optional[str], history_csv: Path) -> Optional[str]:
    if arg != "auto":
        return arg
    if not history_csv.exists() or history_csv.stat().st_size == 0:
        return None
    try:
        df_hist = pd.read_csv(history_csv)
        if "top_regime" in df_hist.columns and not df_hist.empty:
            val = str(df_hist.iloc[-1]["top_regime"])
            return val if val in TRANSITION_MATRIX else None
    except Exception:
        return None
    return None


def run(args: argparse.Namespace) -> Dict[str, Any]:
    modules = import_optional_modules()
    history_csv = Path(args.history_csv)
    previous_regime = resolve_previous_regime(args.previous_regime, history_csv)

    fred = {name: fetch_fred_series(name, series_id, args.start) for name, series_id in FRED_SERIES.items()}
    yahoo = fetch_yahoo_data(YAHOO_TICKERS, args.period, modules.get("yf"))

    features = build_features(fred, yahoo, sovereign_spread_change_bp=None)
    panel = build_historical_feature_frame(fred, yahoo, sovereign_spread_change_bp=None)

    rule_classification = classify_regime(features, previous_regime=previous_regime, temperature=args.temperature)
    student_t_filter = run_student_t_filter(panel, previous_regime=previous_regime, temperature=args.temperature, min_rows=args.min_stat_rows)
    change_point = robust_change_point_score(panel)
    ensemble = build_ensemble_probability(
        rule_probs=rule_classification["posterior_probability"],
        stat_probs=student_t_filter.get("probability", {}),
        stat_used=bool(student_t_filter.get("diagnostics", {}).get("used")),
        change_score=change_point,
    )
    metadata = build_metadata(fred, yahoo)
    alerts = build_alerts(features, rule_classification, ensemble, change_point)

    report: Dict[str, Any] = {
        "fetch_time_utc": datetime.now(timezone.utc).isoformat(),
        "previous_regime": previous_regime,
        "features": features,
        "metadata": metadata,
        "rule_classification": rule_classification,
        "student_t_filter": student_t_filter,
        "change_point": change_point,
        "ensemble": ensemble,
        "alerts": alerts,
    }

    output = Path(args.output)
    json_output = Path(args.json_output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(generate_markdown(report), encoding="utf-8")
    write_json(json_output, report)
    append_history(history_csv, report)

    print(f"Wrote Markdown report: {output}")
    print(f"Wrote JSON report: {json_output}")
    print(f"Updated history CSV: {history_csv}")
    print(f"Top regime: {ensemble['top_regime']} ({ensemble['probability'][ensemble['top_regime']]:.1%})")
    return report


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run robust macro regime monitoring.")
    parser.add_argument("--previous-regime", default="auto", choices=["R0", "R1", "R2", "R3", "auto"], help="Previous regime for Markov prior.")
    parser.add_argument("--output", default="reports/latest.md", help="Markdown report output path.")
    parser.add_argument("--json-output", default="data/latest.json", help="JSON output path.")
    parser.add_argument("--history-csv", default="data/history.csv", help="History CSV path.")
    parser.add_argument("--start", default="2020-01-01", help="Start date for FRED data.")
    parser.add_argument("--period", default="5y", help="Yahoo Finance lookback period.")
    parser.add_argument("--temperature", type=float, default=1.25, help="Softmax temperature for rule scoring.")
    parser.add_argument("--min-stat-rows", type=int, default=80, help="Minimum rows required for the Student-t filter.")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        run(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
