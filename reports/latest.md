# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-12T03:57:34.817284+00:00
- Latest market date: 2026-11-11
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **40.8%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.880% | -3.0 bp | -36.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.260% | -2.0 bp | -34.0 bp | 5.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.01 | 1.48% | 0.45% | 3.37% | Dollar pressure |
| SPY | 759.81 | -0.91% | -1.27% | -0.75% | Broad risk asset |
| QQQ | 690.38 | -0.23% | -5.29% | -3.68% | High-duration growth |
| IWM | 283.09 | -0.33% | 4.32% | -5.46% | Small-cap financing sensitivity |
| TLT | 80.92 | -1.03% | 3.00% | 0.29% | Long-duration bond stress |
| EEM | 62.04 | 0.68% | -3.65% | -5.05% | EM dollar/rate transmission |
| HYG | 77.35 | -0.22% | 1.23% | -1.26% | Credit market proxy |
| LQD | 103.96 | -0.52% | 1.66% | -0.56% | Investment-grade bond ETF |
| HY OAS | 3.34% | -9.0 bp | 23.0 bp | 64.0 bp | Credit spread stress |
| IG OAS | 0.91% | -3.0 bp | 8.0 bp | 10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.59 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.38 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.9% | High-rate absorption | 高利率吸收 |
| R1 | 28.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 40.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 17.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.2% | High-rate absorption | 高利率吸收 |
| R1 | 8.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 91.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **20.2%**
- Robust distance: 1.73
- Stress votes: 0/8
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

