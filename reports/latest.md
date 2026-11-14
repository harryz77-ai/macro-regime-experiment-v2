# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-14T03:24:47.768285+00:00
- Latest market date: 2026-11-13
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **39.9%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.100% | 20.0 bp | -9.0 bp | 38.0 bp | Long-end rate pressure |
| US 30Y yield | 5.430% | 15.0 bp | -9.0 bp | 12.0 bp | Term premium / fiscal supply pressure |
| DXY | 103.41 | 1.09% | 1.54% | 4.56% | Dollar pressure |
| SPY | 754.37 | 2.59% | -1.16% | -0.83% | Broad risk asset |
| QQQ | 679.89 | 3.63% | -4.21% | -4.27% | High-duration growth |
| IWM | 277.54 | 1.41% | 2.63% | -6.52% | Small-cap financing sensitivity |
| TLT | 79.38 | -3.10% | -0.42% | -2.43% | Long-duration bond stress |
| EEM | 60.92 | 2.68% | -3.07% | -8.56% | EM dollar/rate transmission |
| HYG | 76.94 | -0.38% | 0.63% | -1.82% | Credit market proxy |
| LQD | 102.81 | -1.65% | -0.19% | -1.86% | Investment-grade bond ETF |
| HY OAS | 3.20% | -12.0 bp | -5.0 bp | 47.0 bp | Credit spread stress |
| IG OAS | 0.89% | -2.0 bp | 5.0 bp | 8.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.79 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.91 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 27.0% | High-rate absorption | 高利率吸收 |
| R1 | 39.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 24.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 24.5% | High-rate absorption | 高利率吸收 |
| R1 | 50.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 28.7% | High-rate absorption | 高利率吸收 |
| R1 | 21.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 49.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **8.4%**
- Robust distance: 1.01
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

