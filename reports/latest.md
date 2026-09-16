# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-09-16T01:29:39.006995+00:00
- Latest market date: 2026-09-15
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **64.0%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.970% | 19.0 bp | 29.0 bp | 48.0 bp | Long-end rate pressure |
| US 30Y yield | 5.340% | 10.0 bp | 9.0 bp | 41.0 bp | Term premium / fiscal supply pressure |
| DXY | 99.71 | 0.88% | 0.07% | -1.13% | Dollar pressure |
| SPY | 760.88 | -1.21% | -1.99% | 2.95% | Broad risk asset |
| QQQ | 709.18 | -1.36% | -2.99% | -1.74% | High-duration growth |
| IWM | 287.91 | -2.74% | -5.63% | -0.68% | Small-cap financing sensitivity |
| TLT | 80.93 | -1.56% | -0.97% | -5.17% | Long-duration bond stress |
| EEM | 65.99 | -3.94% | -0.93% | -3.75% | EM dollar/rate transmission |
| HYG | 78.53 | -0.80% | -0.94% | -0.02% | Credit market proxy |
| LQD | 104.30 | -1.12% | -1.30% | -2.95% | Investment-grade bond ETF |
| HY OAS | 2.71% | 3.0 bp | 1.0 bp | 6.0 bp | Credit spread stress |
| IG OAS | 0.80% | -1.0 bp | -1.0 bp | 6.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -3.64 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.06 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 16.5% | High-rate absorption | 高利率吸收 |
| R1 | 64.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 12.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.3% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 7.0% | High-rate absorption | 高利率吸收 |
| R1 | 78.6% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 14.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **16.6%**
- Robust distance: 1.30
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: 10Y yield rose meaningfully over 20D; IWM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

