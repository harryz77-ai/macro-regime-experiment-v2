# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-09-22T01:40:22.281365+00:00
- Latest market date: 2026-09-21
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **66.9%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.010% | 5.0 bp | 32.0 bp | 60.0 bp | Long-end rate pressure |
| US 30Y yield | 5.340% | -1.0 bp | 11.0 bp | 48.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.42 | 0.96% | 1.64% | -1.00% | Dollar pressure |
| SPY | 773.50 | 1.91% | 1.27% | 5.60% | Broad risk asset |
| QQQ | 741.47 | 4.66% | 4.04% | 3.61% | High-duration growth |
| IWM | 285.58 | -0.55% | -4.55% | -4.21% | Small-cap financing sensitivity |
| TLT | 81.80 | 1.08% | 0.08% | -5.27% | Long-duration bond stress |
| EEM | 68.83 | 4.30% | 2.55% | 1.28% | EM dollar/rate transmission |
| HYG | 78.68 | 0.19% | -0.63% | -0.02% | Credit market proxy |
| LQD | 105.09 | 0.76% | -0.37% | -2.87% | Investment-grade bond ETF |
| HY OAS | 2.68% | 3.0 bp | -2.0 bp | -15.0 bp | Credit spread stress |
| IG OAS | 0.77% | -3.0 bp | -4.0 bp | 0.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -5.81 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.28 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 14.8% | High-rate absorption | 高利率吸收 |
| R1 | 66.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 12.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.8% | High-rate absorption | 高利率吸收 |
| R1 | 70.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 10.2% | High-rate absorption | 高利率吸收 |
| R1 | 71.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **19.6%**
- Robust distance: 1.48
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

