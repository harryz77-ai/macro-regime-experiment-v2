# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-05T11:48:11.449298+00:00
- Latest market date: 2026-06-05
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **62.2%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.21 | 0.31% | 0.98% | -0.02% | Dollar pressure |
| SPY | 757.09 | 0.33% | 3.17% | 12.11% | Broad risk asset |
| QQQ | 740.61 | 0.68% | 6.44% | 22.01% | High-duration growth |
| IWM | 292.01 | -0.01% | 1.82% | 15.46% | Small-cap financing sensitivity |
| TLT | 85.50 | 0.11% | -0.28% | -2.02% | Long-duration bond stress |
| EEM | 69.10 | 0.71% | 2.39% | 17.76% | EM dollar/rate transmission |
| HYG | 79.83 | 0.01% | 0.10% | 1.26% | Credit market proxy |
| LQD | 108.85 | 0.00% | 0.07% | 0.07% | Investment-grade bond ETF |
| HY OAS | 2.75% | 3.0 bp | -4.0 bp | -42.0 bp | Credit spread stress |
| IG OAS | 0.74% | 1.0 bp | -5.0 bp | -17.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.78 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 62.2% | High-rate absorption | 高利率吸收 |
| R1 | 18.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 13.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 50.2% | High-rate absorption | 高利率吸收 |
| R1 | 22.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 18.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 94.5% | High-rate absorption | 高利率吸收 |
| R1 | 3.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 2.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **4.9%**
- Robust distance: 0.62
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: credit spread pressure is not yet disorderly
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

