# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-17T05:08:51.338602+00:00
- Latest market date: 2026-11-16
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **44.4%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.150% | 31.0 bp | 5.0 bp | 44.0 bp | Long-end rate pressure |
| US 30Y yield | 5.470% | 22.0 bp | 4.0 bp | 19.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.55 | 1.87% | 1.54% | 4.81% | Dollar pressure |
| SPY | 739.95 | -1.69% | -3.46% | -3.13% | Broad risk asset |
| QQQ | 661.75 | -2.59% | -7.88% | -7.15% | High-duration growth |
| IWM | 272.94 | -3.39% | 0.61% | -8.77% | Small-cap financing sensitivity |
| TLT | 79.38 | -3.15% | 0.32% | -2.08% | Long-duration bond stress |
| EEM | 58.89 | -3.51% | -6.98% | -12.26% | EM dollar/rate transmission |
| HYG | 76.73 | -1.01% | 0.39% | -2.15% | Credit market proxy |
| LQD | 102.80 | -1.79% | 0.31% | -1.74% | Investment-grade bond ETF |
| HY OAS | 3.23% | -19.0 bp | -8.0 bp | 53.0 bp | Credit spread stress |
| IG OAS | 0.89% | -4.0 bp | 4.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.07 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.52 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 19.4% | High-rate absorption | 高利率吸收 |
| R1 | 44.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 28.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 18.2% | High-rate absorption | 高利率吸收 |
| R1 | 62.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 10.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 16.1% | High-rate absorption | 高利率吸收 |
| R1 | 12.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 71.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **8.7%**
- Robust distance: 1.04
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

