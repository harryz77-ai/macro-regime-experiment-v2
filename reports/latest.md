# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-10-22T01:39:16.245643+00:00
- Latest market date: 2026-10-21
- Overall data freshness: Fresh
- Missing fields: us2y, us10y, us30y, hy_oas, ig_oas
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **56.8%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | missing | missing | missing | missing | Long-end rate pressure |
| US 30Y yield | missing | missing | missing | missing | Term premium / fiscal supply pressure |
| DXY | 101.70 | -0.83% | 0.59% | 0.32% | Dollar pressure |
| SPY | 773.09 | 0.45% | 0.69% | 4.61% | Broad risk asset |
| QQQ | 725.20 | -0.51% | -2.16% | 7.47% | High-duration growth |
| IWM | 276.48 | 1.88% | -1.93% | -5.51% | Small-cap financing sensitivity |
| TLT | 80.24 | 1.71% | 0.13% | -3.61% | Long-duration bond stress |
| EEM | 63.57 | -1.27% | -6.11% | 1.94% | EM dollar/rate transmission |
| HYG | 76.98 | 0.22% | -1.00% | -1.63% | Credit market proxy |
| LQD | 103.21 | 0.54% | -0.23% | -2.14% | Investment-grade bond ETF |
| HY OAS | missing | missing | missing | missing | Credit spread stress |
| IG OAS | missing | missing | missing | missing | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | -2.62 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | -6.80 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 20.7% | High-rate absorption | 高利率吸收 |
| R1 | 56.8% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.4% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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
- Usable rows: 1236
- Available feature count: 7
- Top statistical regime: R1
- Warnings: State R2 has only 0 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 8.1% | High-rate absorption | 高利率吸收 |
| R1 | 78.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 13.7% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **12.3%**
- Robust distance: 0.97
- Stress votes: 1/8
- Warnings: none

## 7. Signal Evidence

- **R0**: DXY is stable
- **R1**: IWM underperformed SPY over 20D; EEM underperformed SPY over 20D
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

