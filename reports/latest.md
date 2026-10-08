# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-08T02:47:13.993769+00:00
- Latest market date: 2026-10-07
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **79.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.270% | 1.0 bp | 47.0 bp | 65.0 bp | Long-end rate pressure |
| US 30Y yield | 5.640% | 5.0 bp | 39.0 bp | 54.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.20 | 0.74% | 3.47% | 1.25% | Dollar pressure |
| SPY | 777.22 | 1.91% | 2.20% | 3.63% | Broad risk asset |
| QQQ | 757.73 | 2.43% | 5.89% | 5.40% | High-duration growth |
| IWM | 277.70 | -0.07% | -4.20% | -5.46% | Small-cap financing sensitivity |
| TLT | 77.15 | -0.41% | -5.22% | -7.15% | Long-duration bond stress |
| EEM | 67.37 | 0.87% | -1.62% | 2.59% | EM dollar/rate transmission |
| HYG | 77.18 | 0.41% | -1.84% | -1.70% | Credit market proxy |
| LQD | 102.10 | 0.35% | -2.63% | -3.54% | Investment-grade bond ETF |
| HY OAS | 3.03% | -5.0 bp | 36.0 bp | 31.0 bp | Credit spread stress |
| IG OAS | 0.83% | -1.0 bp | 2.0 bp | 4.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -6.40 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -3.82 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 8.4% | High-rate absorption | 高利率吸收 |
| R1 | 79.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 4.7% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 9.0% | High-rate absorption | 高利率吸收 |
| R1 | 79.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 5.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 97.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 2.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **medium**
- Risk score: **42.8%**
- Robust distance: 2.14
- Stress votes: 3/8
- Warnings: none

## 7. Signal Evidence

- **R0**: no strong evidence
- **R1**: 10Y yield rose meaningfully over 20D; 30Y yield rose meaningfully over 20D; DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D; TLT sold off over 20D; credit spread pressure is not yet disorderly
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
- R2 transition risk: **medium**
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

