# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-29T00:14:46.169962+00:00
- Latest market date: 2026-07-28
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **45.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.650% | 5.0 bp | 27.0 bp | 23.0 bp | Long-end rate pressure |
| US 30Y yield | 5.120% | 1.0 bp | 25.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.42 | 0.43% | 0.06% | 2.53% | Dollar pressure |
| SPY | 740.86 | -0.99% | -0.02% | 3.35% | Broad risk asset |
| QQQ | 675.49 | -4.72% | -6.71% | 1.27% | High-duration growth |
| IWM | 293.37 | -1.07% | -1.87% | 5.79% | Small-cap financing sensitivity |
| TLT | 84.24 | 0.69% | -3.31% | -0.49% | Long-duration bond stress |
| EEM | 62.36 | -4.56% | -7.52% | -2.04% | EM dollar/rate transmission |
| HYG | 79.42 | -0.29% | -0.28% | 0.29% | Credit market proxy |
| LQD | 106.83 | -0.02% | -2.27% | -0.75% | Investment-grade bond ETF |
| HY OAS | 2.81% | 12.0 bp | 1.0 bp | 4.0 bp | Credit spread stress |
| IG OAS | 0.81% | 3.0 bp | 5.0 bp | 2.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.50 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 11.8% | High-rate absorption | 高利率吸收 |
| R1 | 45.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 36.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 6.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.8% | High-rate absorption | 高利率吸收 |
| R1 | 70.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 0.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 99.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **14.3%**
- Robust distance: 1.13
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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

