# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-26T01:34:52.583923+00:00
- Latest market date: 2026-06-25
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **35.9%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.410% | -2.0 bp | -9.0 bp | 6.0 bp | Long-end rate pressure |
| US 30Y yield | 4.860% | -7.0 bp | -17.0 bp | -5.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.48 | 1.39% | 2.29% | 0.97% | Dollar pressure |
| SPY | 734.30 | -0.64% | -1.90% | 16.49% | Broad risk asset |
| QQQ | 716.38 | -0.74% | -1.68% | 28.46% | High-duration growth |
| IWM | 298.91 | 3.12% | 3.19% | 25.05% | Small-cap financing sensitivity |
| TLT | 87.35 | 1.18% | 2.81% | 1.83% | Long-duration bond stress |
| EEM | 67.96 | -0.88% | -0.11% | 24.77% | EM dollar/rate transmission |
| HYG | 79.88 | 0.19% | 0.20% | 2.91% | Credit market proxy |
| LQD | 109.50 | 0.67% | 0.90% | 2.30% | Investment-grade bond ETF |
| HY OAS | 2.76% | 13.0 bp | 4.0 bp | -41.0 bp | Credit spread stress |
| IG OAS | 0.75% | 1.0 bp | 2.0 bp | -11.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.09 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.79 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 31.6% | High-rate absorption | 高利率吸收 |
| R1 | 35.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 23.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 35.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 9.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 23.4% | High-rate absorption | 高利率吸收 |
| R1 | 20.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 55.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **12.8%**
- Robust distance: 1.34
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating
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

