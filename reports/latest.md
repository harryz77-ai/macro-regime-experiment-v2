# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-07T01:13:06.028572+00:00
- Latest market date: 2026-07-06
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **48.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.490% | 9.0 bp | 0.0 bp | 16.0 bp | Long-end rate pressure |
| US 30Y yield | 4.980% | 12.0 bp | -1.0 bp | 8.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.90 | -0.46% | 1.50% | 1.78% | Dollar pressure |
| SPY | 751.28 | 3.06% | -0.51% | 11.42% | Broad risk asset |
| QQQ | 722.82 | 2.31% | -2.29% | 19.39% | High-duration growth |
| IWM | 298.90 | -0.31% | 2.60% | 15.03% | Small-cap financing sensitivity |
| TLT | 85.45 | -1.83% | 0.31% | -0.96% | Long-duration bond stress |
| EEM | 67.57 | 0.57% | -1.71% | 12.38% | EM dollar/rate transmission |
| HYG | 79.87 | 0.51% | 0.51% | 0.59% | Credit market proxy |
| LQD | 108.67 | -0.41% | 0.19% | -0.01% | Investment-grade bond ETF |
| HY OAS | 2.74% | -9.0 bp | -2.0 bp | -21.0 bp | Credit spread stress |
| IG OAS | 0.75% | -2.0 bp | 1.0 bp | -7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.11 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -1.19 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 48.0% | High-rate absorption | 高利率吸收 |
| R1 | 33.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 9.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 98.7% | High-rate absorption | 高利率吸收 |
| R1 | 0.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 0.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **6.3%**
- Robust distance: 0.80
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

- R1 continuation: **not confirmed**
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

