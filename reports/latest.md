# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-10T01:05:58.852780+00:00
- Latest market date: 2026-07-09
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R0 — High-rate absorption / 高利率吸收**
- Ensemble probability: **73.4%**
- Previous regime: R0
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.560% | 12.0 bp | 0.0 bp | 25.0 bp | Long-end rate pressure |
| US 30Y yield | 5.060% | 15.0 bp | 3.0 bp | 15.0 bp | Term premium / fiscal supply pressure |
| DXY | 100.82 | -0.56% | 0.91% | 2.49% | Dollar pressure |
| SPY | 751.71 | 0.80% | 2.25% | 9.85% | Broad risk asset |
| QQQ | 723.28 | -0.26% | 2.30% | 17.28% | High-duration growth |
| IWM | 297.24 | -0.69% | 4.54% | 12.40% | Small-cap financing sensitivity |
| TLT | 84.49 | -1.20% | -0.37% | -1.88% | Long-duration bond stress |
| EEM | 66.78 | 0.45% | 1.99% | 9.92% | EM dollar/rate transmission |
| HYG | 79.75 | 0.20% | 0.63% | 0.35% | Credit market proxy |
| LQD | 107.71 | -0.69% | -0.30% | -1.01% | Investment-grade bond ETF |
| HY OAS | 2.70% | -4.0 bp | -10.0 bp | -16.0 bp | Credit spread stress |
| IG OAS | 0.76% | 0.0 bp | 1.0 bp | -5.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 2.28 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.27 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 73.4% | High-rate absorption | 高利率吸收 |
| R1 | 14.3% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 4.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 7.4% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 66.2% | High-rate absorption | 高利率吸收 |
| R1 | 18.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 6.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.2% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1270
- Available feature count: 13
- Top statistical regime: R0
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 99.9% | High-rate absorption | 高利率吸收 |
| R1 | 0.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 0.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **5.3%**
- Robust distance: 0.68
- Stress votes: 0/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; equity resilience with stable credit; DXY is stable
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

