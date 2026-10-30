# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-30T02:43:59.140597+00:00
- Latest market date: 2026-10-29
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **42.8%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.050% | -8.0 bp | -21.0 bp | 35.0 bp | Long-end rate pressure |
| US 30Y yield | 5.370% | -5.0 bp | -22.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.74 | 0.12% | -0.36% | 2.05% | Dollar pressure |
| SPY | 769.36 | 0.71% | 0.70% | 0.19% | Broad risk asset |
| QQQ | 715.34 | 1.54% | -3.60% | -0.17% | High-duration growth |
| IWM | 284.01 | 2.65% | 1.79% | -5.01% | Small-cap financing sensitivity |
| TLT | 81.49 | -0.31% | 4.86% | -1.05% | Long-duration bond stress |
| EEM | 62.72 | 1.62% | -6.12% | -4.56% | EM dollar/rate transmission |
| HYG | 77.58 | 0.62% | 0.88% | -1.47% | Credit market proxy |
| LQD | 104.22 | -0.06% | 2.15% | -1.53% | Investment-grade bond ETF |
| HY OAS | 3.14% | -13.0 bp | 2.0 bp | 39.0 bp | Credit spread stress |
| IG OAS | 0.86% | -2.0 bp | 2.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.09 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.82 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 42.8% | High-rate absorption | 高利率吸收 |
| R1 | 22.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 19.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 15.6% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 28.0% | High-rate absorption | 高利率吸收 |
| R1 | 30.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 22.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 75.4% | High-rate absorption | 高利率吸收 |
| R1 | 2.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 21.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **21.3%**
- Robust distance: 1.57
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 10.0% | High-rate absorption | 高利率吸收 |
| R1 | 18.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 38.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 34.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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

