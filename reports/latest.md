# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-05-17T13:21:54.992171+00:00
- Latest market date: 2026-05-15
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **65.5%**
- Previous regime: unknown
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.470% | 6.0 bp | 15.0 bp | 39.0 bp | Long-end rate pressure |
| US 30Y yield | 5.020% | 5.0 bp | 9.0 bp | 32.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.27 | 1.46% | 1.19% | 1.37% | Dollar pressure |
| SPY | 739.17 | 0.21% | 4.09% | 8.28% | Broad risk asset |
| QQQ | 708.93 | -0.32% | 9.26% | 17.62% | High-duration growth |
| IWM | 277.60 | -2.31% | 0.66% | 5.10% | Small-cap financing sensitivity |
| TLT | 83.66 | -2.81% | -3.56% | -5.62% | Long-duration bond stress |
| EEM | 65.07 | -4.22% | 2.25% | 6.60% | EM dollar/rate transmission |
| HYG | 79.46 | -0.85% | -0.96% | -0.35% | Credit market proxy |
| LQD | 107.86 | -1.23% | -1.60% | -2.31% | Investment-grade bond ETF |
| HY OAS | 2.76% | -3.0 bp | -10.0 bp | -10.0 bp | Credit spread stress |
| IG OAS | 0.76% | -3.0 bp | -5.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.43 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.84 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 20.8% | High-rate absorption | 高利率吸收 |
| R1 | 65.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 15.1% | High-rate absorption | 高利率吸收 |
| R1 | 75.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 3.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 27.7% | High-rate absorption | 高利率吸收 |
| R1 | 57.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 14.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **20.1%**
- Robust distance: 1.51
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: SPY and QQQ rallied over 20D

## 8. Markov Prior

No Markov prior used because previous regime is unknown or invalid.

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

