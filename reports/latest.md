# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-20T04:05:47.528600+00:00
- Latest market date: 2026-11-19
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **39.4%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.070% | 9.0 bp | -5.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.410% | 6.0 bp | -1.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.83 | 0.64% | 2.18% | 4.70% | Dollar pressure |
| SPY | 715.87 | -5.45% | -6.29% | -6.32% | Broad risk asset |
| QQQ | 645.04 | -6.27% | -8.44% | -9.23% | High-duration growth |
| IWM | 264.22 | -5.11% | -4.50% | -11.38% | Small-cap financing sensitivity |
| TLT | 80.35 | 0.79% | -1.29% | -2.37% | Long-duration bond stress |
| EEM | 56.75 | -7.18% | -8.05% | -15.51% | EM dollar/rate transmission |
| HYG | 76.53 | -0.58% | -0.22% | -2.76% | Credit market proxy |
| LQD | 103.08 | 0.03% | -0.77% | -2.27% | Investment-grade bond ETF |
| HY OAS | 3.47% | 17.0 bp | 20.0 bp | 80.0 bp | Credit spread stress |
| IG OAS | 0.93% | 3.0 bp | 5.0 bp | 13.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.79 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.76 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 18.2% | High-rate absorption | 高利率吸收 |
| R1 | 33.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 39.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 24.5% | High-rate absorption | 高利率吸收 |
| R1 | 50.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R1 | 0.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 99.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **15.5%**
- Robust distance: 1.23
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

