# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-18T04:36:27.231587+00:00
- Latest market date: 2026-11-17
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **41.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.120% | 26.0 bp | 3.0 bp | 47.0 bp | Long-end rate pressure |
| US 30Y yield | 5.460% | 20.0 bp | 3.0 bp | 27.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.65 | 1.39% | 1.89% | 4.70% | Dollar pressure |
| SPY | 732.44 | -2.33% | -4.76% | -3.83% | Broad risk asset |
| QQQ | 656.95 | -2.64% | -8.46% | -6.89% | High-duration growth |
| IWM | 269.05 | -4.11% | -2.44% | -9.47% | Small-cap financing sensitivity |
| TLT | 79.55 | -1.64% | -0.31% | -2.48% | Long-duration bond stress |
| EEM | 58.27 | -3.80% | -7.98% | -11.86% | EM dollar/rate transmission |
| HYG | 76.63 | -0.71% | 0.26% | -2.39% | Credit market proxy |
| LQD | 102.74 | -1.10% | -0.08% | -2.04% | Investment-grade bond ETF |
| HY OAS | 3.34% | 0.0 bp | 5.0 bp | 65.0 bp | Credit spread stress |
| IG OAS | 0.90% | -1.0 bp | 3.0 bp | 9.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.32 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.21 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 15.2% | High-rate absorption | 高利率吸收 |
| R1 | 41.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 35.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 18.2% | High-rate absorption | 高利率吸收 |
| R1 | 62.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 10.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 1.9% | High-rate absorption | 高利率吸收 |
| R1 | 3.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 94.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **8.2%**
- Robust distance: 1.00
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

