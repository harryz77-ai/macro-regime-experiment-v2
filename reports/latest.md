# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-13T10:12:53.845593+00:00
- Latest market date: 2026-06-12
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **58.1%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 99.75 | -0.32% | 0.88% | -0.34% | Dollar pressure |
| SPY | 741.75 | 0.57% | -0.86% | 12.45% | Broad risk asset |
| QQQ | 721.34 | 2.31% | 0.22% | 21.41% | High-duration growth |
| IWM | 292.95 | 4.01% | 2.99% | 19.08% | Small-cap financing sensitivity |
| TLT | 85.77 | 0.83% | 1.40% | -0.22% | Long-duration bond stress |
| EEM | 67.88 | 5.09% | 0.74% | 17.93% | EM dollar/rate transmission |
| HYG | 79.94 | 0.64% | 0.63% | 2.22% | Credit market proxy |
| LQD | 109.01 | 0.78% | 0.80% | 1.47% | Investment-grade bond ETF |
| HY OAS | 2.78% | 4.0 bp | -2.0 bp | -46.0 bp | Credit spread stress |
| IG OAS | 0.75% | 1.0 bp | 0.0 bp | -13.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 3.85 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.60 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 58.1% | High-rate absorption | 高利率吸收 |
| R1 | 22.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 8.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.9% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 41.7% | High-rate absorption | 高利率吸收 |
| R1 | 31.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 12.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 15.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1271
- Available feature count: 9
- Top statistical regime: R0
- Warnings: State R2 has only 6 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 97.8% | High-rate absorption | 高利率吸收 |
| R1 | 1.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 0.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **5.1%**
- Robust distance: 0.65
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: credit spread pressure is not yet disorderly
- **R2**: no strong evidence
- **R3**: no strong evidence

## 8. Markov Prior

| Regime | Prior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 55.0% | High-rate absorption | 高利率吸收 |
| R1 | 25.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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

