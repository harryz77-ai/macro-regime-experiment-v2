# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-21T00:56:17.604815+00:00
- Latest market date: 2026-07-20
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **42.3%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.550% | -1.0 bp | 6.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.060% | 0.0 bp | 13.0 bp | 17.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.96 | -0.31% | 0.11% | 2.41% | Dollar pressure |
| SPY | 742.09 | -0.95% | -0.62% | 4.61% | Broad risk asset |
| QQQ | 696.06 | -2.20% | -5.91% | 6.37% | High-duration growth |
| IWM | 292.31 | -0.40% | -1.11% | 5.98% | Small-cap financing sensitivity |
| TLT | 83.89 | -0.10% | -2.94% | -2.19% | Long-duration bond stress |
| EEM | 63.56 | -1.46% | -10.21% | 0.81% | EM dollar/rate transmission |
| HYG | 79.68 | 0.20% | 0.05% | 0.47% | Credit market proxy |
| LQD | 107.15 | 0.18% | -1.42% | -1.33% | Investment-grade bond ETF |
| HY OAS | 2.73% | 4.0 bp | 7.0 bp | -11.0 bp | Credit spread stress |
| IG OAS | 0.79% | 2.0 bp | 5.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.49 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -9.59 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 22.1% | High-rate absorption | 高利率吸收 |
| R1 | 23.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 42.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 30.5% | High-rate absorption | 高利率吸收 |
| R1 | 33.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 17.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.7% | High-rate absorption | 高利率吸收 |
| R1 | 0.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 99.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **13.6%**
- Robust distance: 1.08
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

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

