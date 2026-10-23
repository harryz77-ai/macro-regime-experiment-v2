# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-23T01:42:06.582241+00:00
- Latest market date: 2026-10-22
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **42.2%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 5.130% | -6.0 bp | 17.0 bp | 48.0 bp | Long-end rate pressure |
| US 30Y yield | 5.420% | -10.0 bp | 13.0 bp | 30.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.56 | -0.43% | 0.27% | 0.75% | Dollar pressure |
| SPY | 763.96 | -1.01% | -0.42% | 4.99% | Broad risk asset |
| QQQ | 704.47 | -3.23% | -4.94% | 6.57% | High-duration growth |
| IWM | 276.67 | 0.58% | -1.77% | -3.87% | Small-cap financing sensitivity |
| TLT | 81.74 | 2.21% | 3.34% | -0.16% | Long-duration bond stress |
| EEM | 61.72 | -3.50% | -8.22% | 1.06% | EM dollar/rate transmission |
| HYG | 77.10 | -0.04% | -0.57% | -1.26% | Credit market proxy |
| LQD | 104.28 | 0.75% | 1.53% | -0.56% | Investment-grade bond ETF |
| HY OAS | 3.27% | 2.0 bp | 54.0 bp | 40.0 bp | Credit spread stress |
| IG OAS | 0.88% | 4.0 bp | 11.0 bp | 7.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -1.35 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -7.80 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 29.3% | High-rate absorption | 高利率吸收 |
| R1 | 42.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 19.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 8.8% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 5. Rule Engine Probability

| Regime | Rule Posterior | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 43.8% | High-rate absorption | 高利率吸收 |
| R1 | 30.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 12.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

## 6. Robust Statistical Layer

### Student-t Observation Filter

- Used: **True**
- Method: Student-t observation filter + Markov transition smoothing
- Usable rows: 1269
- Available feature count: 13
- Top statistical regime: R1
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 0.0% | High-rate absorption | 高利率吸收 |
| R1 | 68.9% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 31.1% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **medium**
- Risk score: **41.5%**
- Robust distance: 2.26
- Stress votes: 2/8
- Warnings: none

## 7. Signal Evidence

- **R0**: 10Y yield is high but not accelerating; DXY is stable
- **R1**: EEM underperformed SPY over 20D
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
- R2 transition risk: **medium**
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

