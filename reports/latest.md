# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-15T00:11:17.101804+00:00
- Latest market date: 2026-07-14
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **32.8%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.620% | 14.0 bp | 17.0 bp | 33.0 bp | Long-end rate pressure |
| US 30Y yield | 5.100% | 11.0 bp | 15.0 bp | 21.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.89 | -0.25% | 1.14% | 2.71% | Dollar pressure |
| SPY | 751.83 | 0.55% | 1.62% | 7.43% | Broad risk asset |
| QQQ | 719.71 | 1.45% | -0.12% | 12.50% | High-duration growth |
| IWM | 294.51 | -0.57% | 0.77% | 9.36% | Small-cap financing sensitivity |
| TLT | 84.08 | -0.56% | -1.61% | -1.44% | Long-duration bond stress |
| EEM | 65.67 | -0.08% | -2.75% | 5.70% | EM dollar/rate transmission |
| HYG | 79.68 | -0.10% | 0.14% | 0.66% | Credit market proxy |
| LQD | 107.21 | -0.62% | -1.31% | -0.92% | Investment-grade bond ETF |
| HY OAS | 2.69% | -3.0 bp | 3.0 bp | -16.0 bp | Credit spread stress |
| IG OAS | 0.78% | 3.0 bp | 5.0 bp | -2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.37 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 28.6% | High-rate absorption | 高利率吸收 |
| R1 | 32.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 31.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 37.2% | High-rate absorption | 高利率吸收 |
| R1 | 48.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 5.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 8.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 8.9% | High-rate absorption | 高利率吸收 |
| R1 | 1.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 90.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **11.0%**
- Robust distance: 0.84
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

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

