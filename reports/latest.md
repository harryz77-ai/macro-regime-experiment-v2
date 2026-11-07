# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-07T02:57:42.725732+00:00
- Latest market date: 2026-11-06
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **37.5%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.840% | -14.0 bp | -44.0 bp | 14.0 bp | Long-end rate pressure |
| US 30Y yield | 5.250% | -7.0 bp | -42.0 bp | 1.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.28 | 0.39% | 0.07% | 2.32% | Dollar pressure |
| SPY | 735.29 | -2.70% | -5.56% | -5.24% | Broad risk asset |
| QQQ | 656.10 | -4.98% | -12.67% | -10.28% | High-duration growth |
| IWM | 273.67 | -2.03% | -1.89% | -9.59% | Small-cap financing sensitivity |
| TLT | 81.92 | 0.10% | 5.05% | -0.43% | Long-duration bond stress |
| EEM | 59.33 | -2.80% | -11.18% | -11.02% | EM dollar/rate transmission |
| HYG | 77.23 | -0.26% | 0.00% | -2.68% | Credit market proxy |
| LQD | 104.53 | 0.25% | 2.07% | -1.48% | Investment-grade bond ETF |
| HY OAS | 3.48% | 22.0 bp | 33.0 bp | 77.0 bp | Credit spread stress |
| IG OAS | 0.93% | 4.0 bp | 11.0 bp | 14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.67 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -5.62 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 11.7% | High-rate absorption | 高利率吸收 |
| R1 | 27.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 37.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 23.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 14.5% | High-rate absorption | 高利率吸收 |
| R1 | 30.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 36.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1270
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 19.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 80.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **medium**
- Risk score: **42.7%**
- Robust distance: 2.31
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D; TLT rallied over 20D

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
- R2 transition risk: **medium**
- R3 policy-repair signal: **ON**

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

