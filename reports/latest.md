# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-31T02:33:29.323454+00:00
- Latest market date: 2026-10-30
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **29.1%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.980% | 2.0 bp | -31.0 bp | 35.0 bp | Long-end rate pressure |
| US 30Y yield | 5.320% | 3.0 bp | -32.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.96 | 0.15% | 0.03% | 1.99% | Dollar pressure |
| SPY | 755.72 | -0.56% | -1.81% | -1.43% | Broad risk asset |
| QQQ | 690.49 | -1.97% | -7.88% | -3.28% | High-duration growth |
| IWM | 279.33 | 1.30% | -0.78% | -6.10% | Small-cap financing sensitivity |
| TLT | 81.84 | 0.61% | 5.63% | -0.04% | Long-duration bond stress |
| EEM | 61.04 | -1.56% | -9.80% | -6.12% | EM dollar/rate transmission |
| HYG | 77.43 | 0.49% | 0.68% | -1.58% | Credit market proxy |
| LQD | 104.27 | 0.40% | 2.40% | -1.13% | Investment-grade bond ETF |
| HY OAS | 3.26% | -14.0 bp | 2.0 bp | 55.0 bp | Credit spread stress |
| IG OAS | 0.89% | 0.0 bp | 3.0 bp | 11.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.03 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.99 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 22.8% | High-rate absorption | 高利率吸收 |
| R1 | 29.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 28.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 19.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 30.3% | High-rate absorption | 高利率吸收 |
| R1 | 33.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 29.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 4.2% | High-rate absorption | 高利率吸收 |
| R1 | 19.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 75.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **26.5%**
- Robust distance: 1.82
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
| R0 | 55.0% | High-rate absorption | 高利率吸收 |
| R1 | 25.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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

