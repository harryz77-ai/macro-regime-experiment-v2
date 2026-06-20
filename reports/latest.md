# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-20T01:34:37.955448+00:00
- Latest market date: 2026-06-19
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **60.9%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.490% | -6.0 bp | -18.0 bp | 10.0 bp | Long-end rate pressure |
| US 30Y yield | 4.930% | -10.0 bp | -25.0 bp | -1.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.85 | 0.99% | 1.75% | 1.43% | Dollar pressure |
| SPY | 746.74 | 1.48% | 1.00% | 14.62% | Broad risk asset |
| QQQ | 740.62 | 3.28% | 3.85% | 26.82% | High-duration growth |
| IWM | 295.59 | 2.03% | 5.87% | 19.10% | Small-cap financing sensitivity |
| TLT | 86.75 | 0.90% | 3.79% | 2.04% | Long-duration bond stress |
| EEM | 70.79 | 5.42% | 8.70% | 25.90% | EM dollar/rate transmission |
| HYG | 80.01 | 0.09% | 0.70% | 2.61% | Credit market proxy |
| LQD | 108.77 | 0.56% | 1.93% | 1.38% | Investment-grade bond ETF |
| HY OAS | 2.63% | -17.0 bp | -15.0 bp | -58.0 bp | Credit spread stress |
| IG OAS | 0.74% | -1.0 bp | -1.0 bp | -14.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 4.87 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 7.70 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 60.9% | High-rate absorption | 高利率吸收 |
| R1 | 24.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.3% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 8.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 46.3% | High-rate absorption | 高利率吸收 |
| R1 | 35.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 7.6% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 10.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1272
- Available feature count: 13
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 98.9% | High-rate absorption | 高利率吸收 |
| R1 | 0.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 0.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **18.0%**
- Robust distance: 1.62
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit
- **R1**: DXY strengthened over 20D; credit spread pressure is not yet disorderly
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

