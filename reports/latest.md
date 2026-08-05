# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-08-05T00:52:30.742375+00:00
- Latest market date: 2026-08-04
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **40.6%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.700% | 5.0 bp | 22.0 bp | 34.0 bp | Long-end rate pressure |
| US 30Y yield | 5.230% | 11.0 bp | 24.0 bp | 29.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.84 | -1.52% | -1.29% | 1.62% | Dollar pressure |
| SPY | 771.33 | 4.11% | 3.16% | 5.71% | Broad risk asset |
| QQQ | 723.85 | 7.16% | 2.03% | 4.27% | High-duration growth |
| IWM | 301.71 | 2.84% | 1.86% | 7.14% | Small-cap financing sensitivity |
| TLT | 82.82 | -1.29% | -1.65% | -2.17% | Long-duration bond stress |
| EEM | 66.00 | 5.84% | 0.43% | -0.37% | EM dollar/rate transmission |
| HYG | 79.55 | 0.65% | 0.22% | 1.07% | Credit market proxy |
| LQD | 106.76 | 0.37% | -0.61% | -0.67% | Investment-grade bond ETF |
| HY OAS | 2.78% | -3.0 bp | 6.0 bp | -4.0 bp | Credit spread stress |
| IG OAS | 0.78% | -3.0 bp | 3.0 bp | 1.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.30 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -2.73 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 20.6% | High-rate absorption | 高利率吸收 |
| R1 | 40.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 31.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
- Usable rows: 1270
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 19.8% | High-rate absorption | 高利率吸收 |
| R1 | 0.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 80.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **6.0%**
- Robust distance: 0.76
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: equity resilience with stable credit
- **R1**: 10Y yield rose meaningfully over 20D; EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

