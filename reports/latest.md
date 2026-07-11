# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-11T00:15:20.751570+00:00
- Latest market date: 2026-07-10
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **59.9%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.540% | 6.0 bp | 1.0 bp | 24.0 bp | Long-end rate pressure |
| US 30Y yield | 5.050% | 8.0 bp | 4.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.96 | 0.10% | 1.02% | 2.90% | Dollar pressure |
| SPY | 754.95 | 1.37% | 4.34% | 8.99% | Broad risk asset |
| QQQ | 725.51 | 1.81% | 4.70% | 15.54% | High-duration growth |
| IWM | 295.99 | -0.53% | 5.19% | 10.41% | Small-cap financing sensitivity |
| TLT | 84.47 | -1.22% | -0.12% | -2.04% | Long-duration bond stress |
| EEM | 66.90 | 1.83% | 4.00% | 8.05% | EM dollar/rate transmission |
| HYG | 79.71 | 0.00% | 0.77% | 0.51% | Credit market proxy |
| LQD | 107.46 | -1.09% | -0.30% | -1.19% | Investment-grade bond ETF |
| HY OAS | 2.70% | -5.0 bp | -8.0 bp | -13.0 bp | Credit spread stress |
| IG OAS | 0.76% | 1.0 bp | 1.0 bp | -4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.34 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 59.9% | High-rate absorption | 高利率吸收 |
| R1 | 23.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 5.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 11.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 43.8% | High-rate absorption | 高利率吸收 |
| R1 | 33.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 15.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 99.8% | High-rate absorption | 高利率吸收 |
| R1 | 0.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 0.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **5.7%**
- Robust distance: 0.72
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

