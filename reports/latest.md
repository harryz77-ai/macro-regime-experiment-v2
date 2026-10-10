# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-10T02:29:26.656473+00:00
- Latest market date: 2026-10-09
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **77.9%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.220% | -2.0 bp | 27.0 bp | 67.0 bp | Long-end rate pressure |
| US 30Y yield | 5.600% | -1.0 bp | 23.0 bp | 52.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.23 | 0.30% | 3.14% | 1.49% | Dollar pressure |
| SPY | 778.57 | 1.16% | 2.12% | 3.97% | Broad risk asset |
| QQQ | 751.27 | 0.23% | 5.20% | 6.53% | High-duration growth |
| IWM | 278.94 | -0.92% | -3.19% | -5.39% | Small-cap financing sensitivity |
| TLT | 77.98 | 0.65% | -3.19% | -6.29% | Long-duration bond stress |
| EEM | 66.80 | -1.29% | -1.53% | 4.07% | EM dollar/rate transmission |
| HYG | 77.23 | 0.42% | -1.31% | -1.78% | Credit market proxy |
| LQD | 102.41 | 0.57% | -1.41% | -3.51% | Investment-grade bond ETF |
| HY OAS | 3.15% | -9.0 bp | 45.0 bp | 44.0 bp | Credit spread stress |
| IG OAS | 0.82% | -4.0 bp | 2.0 bp | 4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -5.31 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.65 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 8.8% | High-rate absorption | 高利率吸收 |
| R1 | 77.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 9.3% | High-rate absorption | 高利率吸收 |
| R1 | 78.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 92.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **30.2%**
- Robust distance: 1.79
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

