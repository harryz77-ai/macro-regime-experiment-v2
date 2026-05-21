# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-05-21T11:51:50.230745+00:00
- Latest market date: 2026-05-21
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **61.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | 21.0 bp | 37.0 bp | 63.0 bp | Long-end rate pressure |
| US 30Y yield | 5.180% | 15.0 bp | 29.0 bp | 48.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.25 | 0.37% | 0.45% | 1.58% | Dollar pressure |
| SPY | 741.25 | -0.14% | 4.22% | 8.14% | Broad risk asset |
| QQQ | 713.15 | -0.22% | 8.86% | 17.47% | High-duration growth |
| IWM | 279.87 | -0.99% | 1.23% | 6.47% | Small-cap financing sensitivity |
| TLT | 83.91 | -1.05% | -2.91% | -5.63% | Long-duration bond stress |
| EEM | 65.46 | -2.60% | 3.28% | 4.54% | EM dollar/rate transmission |
| HYG | 79.86 | -0.06% | -0.28% | 0.31% | Credit market proxy |
| LQD | 107.95 | -0.62% | -1.32% | -2.23% | Investment-grade bond ETF |
| HY OAS | 2.86% | 4.0 bp | 1.0 bp | -8.0 bp | Credit spread stress |
| IG OAS | 0.76% | -1.0 bp | -4.0 bp | -4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.00 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.94 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 16.6% | High-rate absorption | 高利率吸收 |
| R1 | 61.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 14.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 18.6% | High-rate absorption | 高利率吸收 |
| R1 | 63.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1271
- Available feature count: 13
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 6.7% | High-rate absorption | 高利率吸收 |
| R1 | 66.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 26.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **18.5%**
- Robust distance: 1.65
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

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

