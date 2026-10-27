# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-27T02:13:02.741477+00:00
- Latest market date: 2026-10-26
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **34.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.000% | -9.0 bp | -18.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.330% | -10.0 bp | -14.0 bp | 13.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.04 | 0.06% | 0.83% | 2.25% | Dollar pressure |
| SPY | 765.37 | -0.14% | -0.03% | 2.71% | Broad risk asset |
| QQQ | 712.20 | -0.86% | -3.30% | 3.63% | High-duration growth |
| IWM | 276.99 | 2.10% | -1.08% | -4.63% | Small-cap financing sensitivity |
| TLT | 81.68 | 2.79% | 4.31% | 0.49% | Long-duration bond stress |
| EEM | 61.82 | -2.35% | -8.01% | -3.54% | EM dollar/rate transmission |
| HYG | 77.20 | 0.48% | 0.00% | -1.43% | Credit market proxy |
| LQD | 104.02 | 1.11% | 1.95% | -0.84% | Investment-grade bond ETF |
| HY OAS | 3.38% | 7.0 bp | 45.0 bp | 53.0 bp | Credit spread stress |
| IG OAS | 0.91% | 6.0 bp | 10.0 bp | 12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.05 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.97 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 23.2% | High-rate absorption | 高利率吸收 |
| R1 | 34.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 31.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 11.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 33.3% | High-rate absorption | 高利率吸收 |
| R1 | 39.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 11.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 15.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 26.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 74.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **33.4%**
- Robust distance: 2.11
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 9. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
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

