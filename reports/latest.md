# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-11T02:52:50.248031+00:00
- Latest market date: 2026-11-10
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **38.5%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.880% | -3.0 bp | -36.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.260% | -2.0 bp | -34.0 bp | 5.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.26 | 0.38% | 0.07% | 2.63% | Dollar pressure |
| SPY | 749.92 | -0.59% | -3.61% | -2.70% | Broad risk asset |
| QQQ | 674.76 | -1.54% | -9.25% | -7.45% | High-duration growth |
| IWM | 280.58 | 0.28% | 1.40% | -7.48% | Small-cap financing sensitivity |
| TLT | 80.88 | -0.28% | 3.20% | 0.21% | Long-duration bond stress |
| EEM | 60.57 | -0.87% | -7.86% | -10.03% | EM dollar/rate transmission |
| HYG | 77.18 | 0.26% | 0.12% | -2.09% | Credit market proxy |
| LQD | 103.88 | 0.15% | 1.30% | -0.88% | Investment-grade bond ETF |
| HY OAS | 3.34% | -9.0 bp | 23.0 bp | 64.0 bp | Credit spread stress |
| IG OAS | 0.91% | -3.0 bp | 8.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.01 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.25 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.8% | High-rate absorption | 高利率吸收 |
| R1 | 30.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 38.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 17.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 17.4% | High-rate absorption | 高利率吸收 |
| R1 | 37.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 19.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 25.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R1 | 16.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 83.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **26.3%**
- Robust distance: 1.81
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D

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

