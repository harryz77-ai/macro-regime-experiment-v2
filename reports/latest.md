# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-24T01:45:00.497933+00:00
- Latest market date: 2026-10-23
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **33.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.960% | -14.0 bp | -15.0 bp | 35.0 bp | Long-end rate pressure |
| US 30Y yield | 5.290% | -14.0 bp | -11.0 bp | 20.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.75 | -0.09% | 0.77% | 1.74% | Dollar pressure |
| SPY | 759.97 | -0.43% | -1.48% | 2.72% | Broad risk asset |
| QQQ | 704.40 | -0.76% | -5.39% | 3.16% | High-duration growth |
| IWM | 275.75 | 1.96% | -2.21% | -5.51% | Small-cap financing sensitivity |
| TLT | 81.34 | 1.61% | 2.96% | -0.59% | Long-duration bond stress |
| EEM | 62.01 | -1.34% | -8.78% | -2.48% | EM dollar/rate transmission |
| HYG | 77.05 | 0.25% | -0.60% | -1.60% | Credit market proxy |
| LQD | 103.85 | 0.44% | 1.05% | -1.15% | Investment-grade bond ETF |
| HY OAS | 3.40% | 17.0 bp | 60.0 bp | 56.0 bp | Credit spread stress |
| IG OAS | 0.89% | 5.0 bp | 10.0 bp | 9.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.73 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.31 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 29.3% | High-rate absorption | 高利率吸收 |
| R1 | 33.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 28.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 8.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 43.8% | High-rate absorption | 高利率吸收 |
| R1 | 30.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R1 | 40.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 59.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **medium**
- Risk score: **43.3%**
- Robust distance: 2.33
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D
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
- R2 upgrade warning: **ON**
- R2 transition risk: **medium**
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

