# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-16T00:54:01.306946+00:00
- Latest market date: 2026-07-15
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **38.2%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.580% | 3.0 bp | 10.0 bp | 26.0 bp | Long-end rate pressure |
| US 30Y yield | 5.080% | 3.0 bp | 11.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.48 | -0.57% | 0.85% | 2.42% | Dollar pressure |
| SPY | 754.81 | 1.26% | 0.25% | 6.56% | Broad risk asset |
| QQQ | 717.74 | 0.89% | -3.42% | 10.74% | High-duration growth |
| IWM | 295.77 | 0.78% | 0.38% | 7.50% | Small-cap financing sensitivity |
| TLT | 84.24 | -0.14% | -1.36% | -2.15% | Long-duration bond stress |
| EEM | 65.57 | -1.00% | -5.99% | 3.57% | EM dollar/rate transmission |
| HYG | 79.81 | 0.19% | 0.17% | 0.45% | Credit market proxy |
| LQD | 107.58 | -0.08% | -0.95% | -1.13% | Investment-grade bond ETF |
| HY OAS | 2.72% | 5.0 bp | 1.0 bp | -12.0 bp | Credit spread stress |
| IG OAS | 0.79% | 3.0 bp | 4.0 bp | 0.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 0.13 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.25 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 38.2% | High-rate absorption | 高利率吸收 |
| R1 | 23.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 30.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 48.6% | High-rate absorption | 高利率吸收 |
| R1 | 33.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 9.9% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 8.5% | Rate decline / policy repair | 利率下行 / 政策修复 |

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
| R0 | 18.2% | High-rate absorption | 高利率吸收 |
| R1 | 2.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 79.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **10.5%**
- Robust distance: 0.78
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
- **R1**: EEM underperformed SPY over 20D; credit spread pressure is not yet disorderly
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

