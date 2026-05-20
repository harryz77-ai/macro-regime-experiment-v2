# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-05-20T10:37:50.178688+00:00
- Latest market date: 2026-05-20
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **70.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.610% | 19.0 bp | 35.0 bp | 58.0 bp | Long-end rate pressure |
| US 30Y yield | 5.140% | 16.0 bp | 26.0 bp | 44.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.39 | 0.92% | 0.81% | 1.54% | Dollar pressure |
| SPY | 733.73 | -0.60% | 4.21% | 7.82% | Broad risk asset |
| QQQ | 701.53 | -0.81% | 8.88% | 16.79% | High-duration growth |
| IWM | 273.00 | -3.39% | -0.55% | 4.99% | Small-cap financing sensitivity |
| TLT | 83.02 | -2.32% | -3.75% | -6.47% | Long-duration bond stress |
| EEM | 64.26 | -2.37% | 3.23% | 4.23% | EM dollar/rate transmission |
| HYG | 79.35 | -0.65% | -0.75% | -0.40% | Credit market proxy |
| LQD | 107.12 | -1.33% | -1.89% | -3.00% | Investment-grade bond ETF |
| HY OAS | 2.83% | 4.0 bp | -4.0 bp | -14.0 bp | Credit spread stress |
| IG OAS | 0.75% | -3.0 bp | -6.0 bp | -6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -4.76 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.98 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 11.8% | High-rate absorption | 高利率吸收 |
| R1 | 70.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 11.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.9% | High-rate absorption | 高利率吸收 |
| R1 | 71.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.3% | High-rate absorption | 高利率吸收 |
| R1 | 81.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **24.7%**
- Robust distance: 1.74
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit; DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

