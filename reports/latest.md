# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-04T03:03:47.215164+00:00
- Latest market date: 2026-11-03
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **38.4%**
- Previous regime: R2
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.910% | -9.0 bp | -37.0 bp | 22.0 bp | Long-end rate pressure |
| US 30Y yield | 5.280% | -3.0 bp | -35.0 bp | 6.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.29 | -1.01% | -0.53% | 1.48% | Dollar pressure |
| SPY | 754.35 | -1.99% | -3.18% | -2.17% | Broad risk asset |
| QQQ | 685.28 | -4.99% | -9.79% | -4.84% | High-duration growth |
| IWM | 279.79 | -0.14% | -0.55% | -6.49% | Small-cap financing sensitivity |
| TLT | 81.11 | -0.64% | 4.96% | -0.78% | Long-duration bond stress |
| EEM | 61.10 | -2.27% | -10.50% | -6.25% | EM dollar/rate transmission |
| HYG | 76.98 | -0.80% | -0.38% | -2.61% | Credit market proxy |
| LQD | 103.72 | -0.56% | 1.55% | -1.70% | Investment-grade bond ETF |
| HY OAS | 3.43% | 13.0 bp | 31.0 bp | 73.0 bp | Credit spread stress |
| IG OAS | 0.94% | 4.0 bp | 10.0 bp | 16.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.62 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.33 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 11.9% | High-rate absorption | 高利率吸收 |
| R1 | 26.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 38.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 23.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 14.5% | High-rate absorption | 高利率吸收 |
| R1 | 30.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 36.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 15.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 84.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **33.3%**
- Robust distance: 2.11
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: 10Y and 30Y yields fell materially over 20D; TLT rallied over 20D

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 10.0% | High-rate absorption | 高利率吸收 |
| R1 | 18.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 38.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 34.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 9. Risk Alerts

- R1 continuation: **ON**
- R2 upgrade warning: **ON**
- R2 transition risk: **low**
- R3 policy-repair signal: **ON**

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

