# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-04T11:29:21.021627+00:00
- Latest market date: 2026-06-04
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **48.6%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.22 | 0.21% | 1.23% | 0.40% | Dollar pressure |
| SPY | 754.24 | 0.50% | 4.21% | 11.50% | Broad risk asset |
| QQQ | 744.21 | 2.02% | 9.18% | 22.61% | High-duration growth |
| IWM | 287.67 | -0.93% | 1.81% | 13.63% | Small-cap financing sensitivity |
| TLT | 85.31 | 0.41% | 0.25% | -3.28% | Long-duration bond stress |
| EEM | 69.92 | 2.24% | 6.91% | 19.62% | EM dollar/rate transmission |
| HYG | 79.68 | -0.05% | 0.21% | 0.91% | Credit market proxy |
| LQD | 108.62 | 0.09% | 0.35% | -0.82% | Investment-grade bond ETF |
| HY OAS | 2.71% | 0.0 bp | -4.0 bp | -38.0 bp | Credit spread stress |
| IG OAS | 0.74% | 0.0 bp | -4.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 2.70 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 48.6% | High-rate absorption | 高利率吸收 |
| R1 | 35.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 5.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 28.0% | High-rate absorption | 高利率吸收 |
| R1 | 52.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 13.7% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 93.6% | High-rate absorption | 高利率吸收 |
| R1 | 4.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 2.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **6.6%**
- Robust distance: 0.83
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 55.0% | High-rate absorption | 高利率吸收 |
| R1 | 25.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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

