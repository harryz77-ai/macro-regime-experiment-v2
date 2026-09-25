# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-09-25T01:39:56.626497+00:00
- Latest market date: 2026-09-24
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **77.2%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.110% | 10.0 bp | 47.0 bp | 73.0 bp | Long-end rate pressure |
| US 30Y yield | 5.400% | 5.0 bp | 23.0 bp | 54.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.25 | 0.93% | 2.35% | 0.14% | Dollar pressure |
| SPY | 767.18 | 0.85% | 0.39% | 2.99% | Broad risk asset |
| QQQ | 741.10 | 3.48% | 4.29% | 0.74% | High-duration growth |
| IWM | 281.66 | -1.32% | -5.53% | -6.01% | Small-cap financing sensitivity |
| TLT | 79.42 | -2.89% | -4.29% | -7.03% | Long-duration bond stress |
| EEM | 67.25 | 2.33% | 0.00% | -0.27% | EM dollar/rate transmission |
| HYG | 77.89 | -0.68% | -2.01% | -1.18% | Credit market proxy |
| LQD | 103.15 | -1.24% | -3.07% | -4.83% | Investment-grade bond ETF |
| HY OAS | 2.73% | 3.0 bp | 6.0 bp | -1.0 bp | Credit spread stress |
| IG OAS | 0.77% | -1.0 bp | -3.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -5.92 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.39 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 9.8% | High-rate absorption | 高利率吸收 |
| R1 | 77.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 11.2% | High-rate absorption | 高利率吸收 |
| R1 | 75.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1270
- Available feature count: 13
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 96.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 3.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **38.1%**
- Robust distance: 2.12
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

