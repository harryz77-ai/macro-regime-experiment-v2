# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-24T00:53:56.180078+00:00
- Latest market date: 2026-07-23
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **65.7%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.670% | 12.0 bp | 17.0 bp | 36.0 bp | Long-end rate pressure |
| US 30Y yield | 5.150% | 7.0 bp | 21.0 bp | 24.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.44 | 0.71% | -0.16% | 3.01% | Dollar pressure |
| SPY | 738.18 | -1.67% | 0.67% | 3.48% | Broad risk asset |
| QQQ | 691.96 | -1.98% | -2.63% | 4.29% | High-duration growth |
| IWM | 292.09 | -1.18% | -1.55% | 5.65% | Small-cap financing sensitivity |
| TLT | 83.17 | -1.24% | -4.47% | -2.51% | Long-duration bond stress |
| EEM | 64.60 | 0.64% | -3.94% | 2.04% | EM dollar/rate transmission |
| HYG | 79.23 | -0.71% | -0.32% | -0.11% | Credit market proxy |
| LQD | 106.26 | -1.15% | -2.54% | -1.68% | Investment-grade bond ETF |
| HY OAS | 2.68% | -3.0 bp | -8.0 bp | -15.0 bp | Credit spread stress |
| IG OAS | 0.78% | -1.0 bp | 3.0 bp | -3.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.22 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -4.61 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 20.3% | High-rate absorption | 高利率吸收 |
| R1 | 65.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 27.8% | High-rate absorption | 高利率吸收 |
| R1 | 57.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.6% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.5% | High-rate absorption | 高利率吸收 |
| R1 | 93.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **17.6%**
- Robust distance: 1.05
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

