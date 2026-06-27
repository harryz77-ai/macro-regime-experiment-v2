# Macro Regime Update v2

## 1. Timestamp

- Fetch time UTC: 2026-06-27T01:26:59.678571+00:00
- Latest market date: 2026-06-26
- Overall data freshness: Fresh
- Missing fields: none
- Stale fields: none

## 2. Current Regime Conclusion

- Most likely regime: **R1 — Bear steepening + dollar pressure / 熊市陡峭化 + 美元压力**
- Ensemble probability: **41.2%**
- Previous regime: R1
- Model type: deterministic feature scoring + Markov prior + robust Student-t filter + change-point risk score

## 3. Evidence Table

| Indicator | Latest | 5D | 20D | 60D | Regime Signal |
|---|---:|---:|---:|---:|---|
| US 10Y yield | 4.400% | -9.0 bp | -8.0 bp | 10.0 bp | Long-end rate pressure |
| US 30Y yield | 4.860% | -7.0 bp | -15.0 bp | -2.0 bp | Term premium / fiscal supply pressure |
| DXY | 101.37 | 0.51% | 2.37% | 1.41% | Dollar pressure |
| SPY | 728.99 | -2.38% | -3.14% | 12.38% | Broad risk asset |
| QQQ | 706.52 | -4.50% | -3.85% | 22.54% | High-duration growth |
| IWM | 299.83 | 1.43% | 2.92% | 21.19% | Small-cap financing sensitivity |
| TLT | 87.36 | 0.70% | 2.29% | 1.95% | Long-duration bond stress |
| EEM | 67.19 | -5.09% | -1.56% | 18.93% | EM dollar/rate transmission |
| HYG | 79.83 | -0.22% | 0.01% | 1.87% | Credit market proxy |
| LQD | 109.50 | 0.39% | 0.60% | 1.66% | Investment-grade bond ETF |
| HY OAS | 2.78% | 12.0 bp | 6.0 bp | -35.0 bp | Credit spread stress |
| IG OAS | 0.76% | 2.0 bp | 3.0 bp | -10.0 bp | Investment-grade credit stress |
| IWM - SPY relative | n/a | n/a | 6.06 pp | n/a | Small-cap relative stress |
| EEM - SPY relative | n/a | n/a | 1.58 pp | n/a | EM relative stress |

## 4. Ensemble Regime Probability

| Regime | Ensemble Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 18.7% | High-rate absorption | 高利率吸收 |
| R1 | 41.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 31.0% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
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
- Usable rows: 1271
- Available feature count: 13
- Top statistical regime: R2
- Warnings: State R2 has only 5 pseudo-labeled rows; using global robust scale.

| Regime | Student-t Filter Probability | Interpretation | 中文解释 |
|---|---:|---|---|
| R0 | 1.4% | High-rate absorption | 高利率吸收 |
| R1 | 26.2% | Bear steepening + dollar pressure | 熊市陡峭化 + 美元压力 |
| R2 | 72.5% | Credit / sovereign stress spillover | 信用 / 主权压力外溢 |
| R3 | 0.0% | Rate decline / policy repair | 利率下行 / 政策修复 |

### Robust Change-Point / Transition Risk

- Used: **True**
- Risk level: **low**
- Risk score: **12.5%**
- Robust distance: 1.32
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

