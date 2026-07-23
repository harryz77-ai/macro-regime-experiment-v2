# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-23T00:57:47.752853+00:00
- Latest market date: 2026-07-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **35.9%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.630% | 5.0 bp | 12.0 bp | 29.0 bp | Long-end rate pressure |
| US 30Y yield | 5.130% | 5.0 bp | 18.0 bp | 21.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.10 | 0.60% | -0.30% | 2.63% | Dollar pressure |
| SPY | 747.41 | -0.98% | 1.89% | 4.96% | Broad risk asset |
| QQQ | 705.35 | -1.73% | -1.16% | 6.36% | High-duration growth |
| IWM | 293.79 | -0.67% | -0.52% | 6.45% | Small-cap financing sensitivity |
| TLT | 83.44 | -0.95% | -2.84% | -2.68% | Long-duration bond stress |
| EEM | 64.99 | -0.88% | -3.25% | 2.49% | EM dollar/rate transmission |
| HYG | 79.52 | -0.36% | 0.02% | 0.30% | Credit market proxy |
| LQD | 106.67 | -0.85% | -1.71% | -1.58% | Investment-grade bond ETF |
| HY OAS | 2.69% | -3.0 bp | -2.0 bp | -13.0 bp | Credit spread stress |
| IG OAS | 0.78% | -1.0 bp | 4.0 bp | -3.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -5.13 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 27.1% | High-rate absorption | 高利率吸收 |
| R1 | 35.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 26.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.6% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 33.3% | High-rate absorption | 高利率吸收 |
| R1 | 36.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 16.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.6% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 11.9% | High-rate absorption | 高利率吸收 |
| R1 | 36.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 51.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **11.7%**
- Robust distance: 0.91
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

