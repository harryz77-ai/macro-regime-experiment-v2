# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-11-03T03:57:50.271919+00:00
- Latest market date: 2026-11-02
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R2 — Credit / sovereign stress spillover / 信用 / 主权压力外溢**
- Ensemble probability: **34.1%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.940% | -6.0 bp | -30.0 bp | 31.0 bp | Long-end rate pressure |
| US 30Y yield | 5.310% | -2.0 bp | -30.0 bp | 14.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.80 | -0.16% | -0.36% | 2.21% | Dollar pressure |
| SPY | 752.10 | -1.73% | -2.93% | -2.49% | Broad risk asset |
| QQQ | 681.09 | -4.37% | -9.93% | -5.70% | High-duration growth |
| IWM | 279.14 | 0.78% | -1.50% | -7.19% | Small-cap financing sensitivity |
| TLT | 81.73 | 0.06% | 5.99% | -0.47% | Long-duration bond stress |
| EEM | 61.11 | -1.15% | -11.09% | -6.90% | EM dollar/rate transmission |
| HYG | 76.89 | -0.40% | -0.12% | -2.46% | Credit market proxy |
| LQD | 103.71 | -0.30% | 1.85% | -1.84% | Investment-grade bond ETF |
| HY OAS | 3.44% | 6.0 bp | 34.0 bp | 74.0 bp | Credit spread stress |
| IG OAS | 0.94% | 3.0 bp | 9.0 bp | 16.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 1.44 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -8.15 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 15.0% | High-rate absorption | 高利率吸收 |
| R1 | 31.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 34.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 19.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 19.8% | High-rate absorption | 高利率吸收 |
| R1 | 39.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 11.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 29.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R1 | 15.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 84.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **34.9%**
- Robust distance: 2.17
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
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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

