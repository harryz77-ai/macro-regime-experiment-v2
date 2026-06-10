# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-10T12:06:36.664965+00:00
- Latest market date: 2026-06-10
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **49.3%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 100.00 | 0.79% | 2.11% | -0.35% | Dollar pressure |
| SPY | 739.22 | -2.55% | 0.22% | 11.29% | Broad risk asset |
| QQQ | 716.07 | -3.59% | 0.68% | 20.04% | High-duration growth |
| IWM | 284.11 | -1.69% | -0.02% | 15.04% | Small-cap financing sensitivity |
| TLT | 84.62 | -0.99% | -1.31% | -1.57% | Long-duration bond stress |
| EEM | 65.75 | -6.18% | -3.22% | 15.45% | EM dollar/rate transmission |
| HYG | 79.54 | -0.38% | -0.24% | 1.77% | Credit market proxy |
| LQD | 108.06 | -0.80% | -0.67% | 0.71% | Investment-grade bond ETF |
| HY OAS | 2.75% | 3.0 bp | -7.0 bp | -47.0 bp | Credit spread stress |
| IG OAS | 0.75% | 2.0 bp | -2.0 bp | -17.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.24 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.44 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 33.9% | High-rate absorption | 高利率吸收 |
| R1 | 49.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 9.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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
- Usable rows: 1270
- Available feature count: 9
- Top statistical regime: R0
- Warnings: State R2 has only 6 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 64.2% | High-rate absorption | 高利率吸收 |
| R1 | 29.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **5.7%**
- Robust distance: 0.73
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit
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

