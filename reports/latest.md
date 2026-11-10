# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-10T04:41:50.062218+00:00
- Latest market date: 2026-11-09
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **39.6%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.860% | -8.0 bp | -36.0 bp | 18.0 bp | Long-end rate pressure |
| US 30Y yield | 5.260% | -5.0 bp | -34.0 bp | 2.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.68 | -0.07% | -0.88% | 2.01% | Dollar pressure |
| SPY | 752.69 | 0.08% | -3.27% | -2.81% | Broad risk asset |
| QQQ | 679.35 | -0.26% | -8.94% | -6.98% | High-duration growth |
| IWM | 282.51 | 1.21% | 1.66% | -7.16% | Small-cap financing sensitivity |
| TLT | 81.96 | 0.28% | 5.01% | 0.69% | Long-duration bond stress |
| EEM | 61.03 | -0.13% | -7.74% | -8.38% | EM dollar/rate transmission |
| HYG | 77.51 | 0.81% | 0.28% | -1.79% | Credit market proxy |
| LQD | 104.67 | 0.93% | 2.04% | -0.52% | Investment-grade bond ETF |
| HY OAS | 3.42% | -2.0 bp | 31.0 bp | 75.0 bp | Credit spread stress |
| IG OAS | 0.93% | -1.0 bp | 10.0 bp | 13.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.92 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.47 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 12.0% | High-rate absorption | 高利率吸收 |
| R1 | 24.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 39.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 23.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 11.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 88.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **30.6%**
- Robust distance: 2.00
- Stress votes: 1/8
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

