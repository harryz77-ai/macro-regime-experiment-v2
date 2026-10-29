# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-29T02:34:36.744107+00:00
- Latest market date: 2026-10-28
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **32.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.990% | -13.0 bp | -25.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.300% | -12.0 bp | -26.0 bp | 3.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.08 | 0.30% | 0.62% | 2.19% | Dollar pressure |
| SPY | 772.31 | -0.10% | 1.27% | 0.38% | Broad risk asset |
| QQQ | 725.61 | 0.06% | -1.91% | 0.35% | High-duration growth |
| IWM | 281.29 | 1.74% | 1.22% | -6.52% | Small-cap financing sensitivity |
| TLT | 80.99 | 0.93% | 4.55% | -1.44% | Long-duration bond stress |
| EEM | 63.52 | -0.08% | -4.90% | -3.76% | EM dollar/rate transmission |
| HYG | 77.59 | 0.79% | 0.94% | -1.49% | Credit market proxy |
| LQD | 104.07 | 0.83% | 2.29% | -1.69% | Investment-grade bond ETF |
| HY OAS | 3.18% | -15.0 bp | 10.0 bp | 45.0 bp | Credit spread stress |
| IG OAS | 0.88% | 1.0 bp | 4.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.05 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.17 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 26.2% | High-rate absorption | 高利率吸收 |
| R1 | 29.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 32.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 11.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 9.5% | High-rate absorption | 高利率吸收 |
| R1 | 8.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 81.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.6% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **24.9%**
- Robust distance: 1.75
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
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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

