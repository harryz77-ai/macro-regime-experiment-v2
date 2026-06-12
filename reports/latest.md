# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-12T12:06:27.473343+00:00
- Latest market date: 2026-06-12
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **51.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.77 | -0.30% | 0.90% | -0.32% | Dollar pressure |
| SPY | 737.76 | -2.55% | -0.61% | 10.28% | Broad risk asset |
| QQQ | 717.12 | -3.17% | 0.34% | 19.01% | High-duration growth |
| IWM | 290.41 | -0.55% | 2.74% | 16.14% | Small-cap financing sensitivity |
| TLT | 85.98 | 0.56% | 1.79% | -0.53% | Long-duration bond stress |
| EEM | 67.50 | -2.32% | 0.43% | 14.89% | EM dollar/rate transmission |
| HYG | 79.94 | 0.14% | 0.55% | 1.69% | Credit market proxy |
| LQD | 109.08 | 0.21% | 0.80% | 0.98% | Investment-grade bond ETF |
| HY OAS | 2.80% | 5.0 bp | 4.0 bp | -47.0 bp | Credit spread stress |
| IG OAS | 0.75% | 1.0 bp | -1.0 bp | -15.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.04 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 51.7% | High-rate absorption | 高利率吸收 |
| R1 | 26.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 11.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 31.2% | High-rate absorption | 高利率吸收 |
| R1 | 37.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 16.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 15.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1271
- Available feature count: 9
- Top statistical regime: R0
- Warnings: State R2 has only 6 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 97.6% | High-rate absorption | 高利率吸收 |
| R1 | 1.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 1.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **4.9%**
- Robust distance: 0.63
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 9. Risk Alerts

- R1 continuation: **not confirmed**
- R2 upgrade warning: **not confirmed**
- R2 transition risk: **low**
- R3 policy-repair signal: **not confirmed**

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

