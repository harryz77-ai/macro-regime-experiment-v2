# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-26T05:14:53.578464+00:00
- Latest market date: 2026-11-26
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **44.4%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.910% | -19.0 bp | -9.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.300% | -16.0 bp | -1.0 bp | 11.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.82 | -0.08% | 1.74% | 4.28% | Dollar pressure |
| SPY | 716.70 | -1.85% | -7.20% | -5.68% | Broad risk asset |
| QQQ | 633.93 | -3.88% | -12.63% | -10.32% | High-duration growth |
| IWM | 268.87 | -0.46% | -4.42% | -7.23% | Small-cap financing sensitivity |
| TLT | 82.24 | 2.52% | 1.97% | 1.28% | Long-duration bond stress |
| EEM | 56.40 | -2.56% | -11.21% | -15.53% | EM dollar/rate transmission |
| HYG | 76.52 | -0.17% | -0.87% | -2.33% | Credit market proxy |
| LQD | 104.29 | 1.11% | 0.60% | -0.07% | Investment-grade bond ETF |
| HY OAS | 3.72% | 29.0 bp | 54.0 bp | 107.0 bp | Credit spread stress |
| IG OAS | 0.98% | 6.0 bp | 10.0 bp | 17.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.79 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.01 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 14.7% | High-rate absorption | 高利率吸收 |
| R1 | 27.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 44.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 13.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 19.3% | High-rate absorption | 高利率吸收 |
| R1 | 41.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 20.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 19.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R1 | 0.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 100.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **36.9%**
- Robust distance: 1.89
- Stress votes: 3/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D
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

