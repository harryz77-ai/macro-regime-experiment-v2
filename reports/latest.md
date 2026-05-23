# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-05-23T07:57:36.258802+00:00
- Latest market date: 2026-05-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **44.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.570% | 10.0 bp | 23.0 bp | 55.0 bp | Long-end rate pressure |
| US 30Y yield | 5.100% | 8.0 bp | 18.0 bp | 43.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.32 | 0.05% | 0.82% | 1.56% | Dollar pressure |
| SPY | 745.64 | 0.88% | 4.44% | 8.47% | Broad risk asset |
| QQQ | 717.54 | 1.21% | 8.08% | 17.92% | High-duration growth |
| IWM | 285.12 | 2.71% | 3.06% | 7.38% | Small-cap financing sensitivity |
| TLT | 84.68 | 1.22% | -1.98% | -5.16% | Long-duration bond stress |
| EEM | 65.88 | 1.24% | 3.36% | 5.06% | EM dollar/rate transmission |
| HYG | 79.91 | 0.57% | -0.19% | 0.33% | Credit market proxy |
| LQD | 108.37 | 0.47% | -0.73% | -1.88% | Investment-grade bond ETF |
| HY OAS | 2.78% | 2.0 bp | -8.0 bp | -32.0 bp | Credit spread stress |
| IG OAS | 0.75% | -1.0 bp | -5.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.38 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.08 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 44.6% | High-rate absorption | 高利率吸收 |
| R1 | 32.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 11.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 11.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
- Usable rows: 1271
- Available feature count: 13
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 70.3% | High-rate absorption | 高利率吸收 |
| R1 | 16.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **10.9%**
- Robust distance: 1.21
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 9. Risk Alerts

- R1 continuation: **ON**
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

