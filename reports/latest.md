# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-20T01:57:06.555593+00:00
- Latest market date: 2026-10-19
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **68.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.090% | -13.0 bp | 15.0 bp | 42.0 bp | Long-end rate pressure |
| US 30Y yield | 5.430% | -17.0 bp | 14.0 bp | 28.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.92 | -0.64% | 1.49% | 0.45% | Dollar pressure |
| SPY | 766.48 | -1.49% | -0.91% | 3.99% | Broad risk asset |
| QQQ | 718.36 | -3.71% | -3.12% | 5.10% | High-duration growth |
| IWM | 271.28 | -2.38% | -5.01% | -6.59% | Small-cap financing sensitivity |
| TLT | 79.46 | 1.81% | -2.47% | -3.41% | Long-duration bond stress |
| EEM | 63.31 | -4.29% | -8.02% | -0.03% | EM dollar/rate transmission |
| HYG | 76.83 | -0.60% | -1.92% | -1.59% | Credit market proxy |
| LQD | 102.88 | 0.29% | -1.68% | -1.90% | Investment-grade bond ETF |
| HY OAS | 3.31% | 20.0 bp | 63.0 bp | 52.0 bp | Credit spread stress |
| IG OAS | 0.85% | 2.0 bp | 8.0 bp | 5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -4.10 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.11 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 13.9% | High-rate absorption | 高利率吸收 |
| R1 | 68.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 10.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 93.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **medium**
- Risk score: **47.1%**
- Robust distance: 2.31
- Stress votes: 3/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; IWM underperformed SPY over 20D; EEM underperformed SPY over 20D
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

