# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-28T02:27:54.717339+00:00
- Latest market date: 2026-10-27
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **42.9%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.000% | -15.0 bp | -17.0 bp | 32.0 bp | Long-end rate pressure |
| US 30Y yield | 5.310% | -17.0 bp | -18.0 bp | 10.0 bp | Term premium / fiscal supply pressure |
| DXY | 102.41 | 0.67% | 1.02% | 2.45% | Dollar pressure |
| SPY | 769.66 | 0.08% | 0.71% | 1.83% | Broad risk asset |
| QQQ | 721.25 | 0.50% | -2.26% | 3.13% | High-duration growth |
| IWM | 280.18 | 1.60% | 0.42% | -5.17% | Small-cap financing sensitivity |
| TLT | 81.63 | 1.87% | 4.77% | 0.10% | Long-duration bond stress |
| EEM | 62.52 | -1.26% | -7.24% | -2.80% | EM dollar/rate transmission |
| HYG | 77.60 | 1.00% | 0.76% | -1.18% | Credit market proxy |
| LQD | 104.30 | 1.05% | 2.28% | -0.87% | Investment-grade bond ETF |
| HY OAS | 3.30% | 1.0 bp | 28.0 bp | 52.0 bp | Credit spread stress |
| IG OAS | 0.90% | 3.0 bp | 7.0 bp | 12.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -0.30 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.95 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 14.0% | High-rate absorption | 高利率吸收 |
| R1 | 42.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 33.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 17.5% | High-rate absorption | 高利率吸收 |
| R1 | 58.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 10.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 13.7% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 0.5% | High-rate absorption | 高利率吸收 |
| R1 | 15.4% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 84.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **27.5%**
- Robust distance: 1.86
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
- **R1**: DXY strengthened over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: TLT rallied over 20D

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

