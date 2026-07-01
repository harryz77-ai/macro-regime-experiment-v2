# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-07-01T01:37:10.343169+00:00
- Latest market date: 2026-06-30
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **37.5%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.380% | -13.0 bp | -7.0 bp | 7.0 bp | Long-end rate pressure |
| US 30Y yield | 4.860% | -9.0 bp | -13.0 bp | -2.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.30 | -0.11% | 2.11% | 1.27% | Dollar pressure |
| SPY | 746.77 | 1.80% | -1.30% | 14.16% | Broad risk asset |
| QQQ | 736.40 | 3.19% | -0.74% | 26.02% | High-duration growth |
| IWM | 300.45 | 1.74% | 4.22% | 19.85% | Small-cap financing sensitivity |
| TLT | 86.42 | 0.26% | 1.11% | 0.33% | Long-duration bond stress |
| EEM | 68.41 | 1.85% | -1.88% | 21.52% | EM dollar/rate transmission |
| HYG | 79.97 | 0.13% | 0.16% | 1.56% | Credit market proxy |
| LQD | 109.07 | 0.15% | 0.13% | 0.73% | Investment-grade bond ETF |
| HY OAS | 2.80% | 15.0 bp | 8.0 bp | -32.0 bp | Credit spread stress |
| IG OAS | 0.76% | 2.0 bp | 3.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 5.51 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -0.58 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 20.3% | High-rate absorption | 高利率吸收 |
| R1 | 37.5% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 33.2% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 9.1% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 24.5% | High-rate absorption | 高利率吸收 |
| R1 | 50.1% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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
| R0 | 6.5% | High-rate absorption | 高利率吸收 |
| R1 | 13.7% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 79.8% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **10.4%**
- Robust distance: 1.17
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
| R0 | 25.0% | High-rate absorption | 高利率吸收 |
| R1 | 43.0% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 18.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 14.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 9. Risk Alerts

- R1 continuation: **not confirmed**
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

