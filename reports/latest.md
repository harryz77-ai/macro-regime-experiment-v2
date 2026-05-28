# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-05-28T12:47:56.515274+00:00
- Latest market date: 2026-05-28
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **69.9%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.500% | -11.0 bp | 15.0 bp | 45.0 bp | Long-end rate pressure |
| US 30Y yield | 5.030% | -11.0 bp | 9.0 bp | 33.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.19 | 0.08% | 0.27% | 0.14% | Dollar pressure |
| SPY | 750.46 | 2.28% | 5.45% | 9.63% | Broad risk asset |
| QQQ | 729.45 | 3.98% | 10.93% | 20.11% | High-duration growth |
| IWM | 290.37 | 6.36% | 6.01% | 10.26% | Small-cap financing sensitivity |
| TLT | 85.30 | 2.75% | -0.87% | -4.08% | Long-duration bond stress |
| EEM | 68.39 | 6.43% | 8.57% | 11.20% | EM dollar/rate transmission |
| HYG | 80.13 | 0.98% | 0.19% | 0.82% | Credit market proxy |
| LQD | 108.93 | 1.69% | 0.02% | -1.00% | Investment-grade bond ETF |
| HY OAS | 2.72% | -14.0 bp | -13.0 bp | -36.0 bp | Credit spread stress |
| IG OAS | 0.74% | -2.0 bp | -7.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.56 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 3.13 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 69.9% | High-rate absorption | 高利率吸收 |
| R1 | 14.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 5.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 62.7% | High-rate absorption | 高利率吸收 |
| R1 | 17.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 13.7% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1271
- Available feature count: 13
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 95.3% | High-rate absorption | 高利率吸收 |
| R1 | 1.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 3.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **9.0%**
- Robust distance: 1.06
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
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

