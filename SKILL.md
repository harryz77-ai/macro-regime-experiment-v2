# Macro Regime Monitoring Skill v2

## Purpose

This skill defines a repeatable macro-regime monitoring method. It fetches fresh macro-market data, builds a multi-asset observation vector, maps the vector into a 4-state macro regime framework, and outputs a concise monitoring report.

It is designed for:

- macro regime identification;
- Markov transition matrix monitoring;
- robust Student-t observation filtering;
- change-point / transition risk detection;
- R1-to-R2 upgrade alerts;
- scenario tree updates;
- risk monitoring.

It is not an automatic trading system and must not be presented as a buy/sell signal.

## Regime Framework

| Regime | Name | Core Features |
|---|---|---|
| R0 | High-rate absorption | Treasury yields high but no longer rising aggressively; equities resilient; dollar stable |
| R1 | Bear steepening + dollar pressure | Long-end yields rising; USD stronger; small caps and EM weak |
| R2 | Credit / sovereign stress spillover | Credit spreads widen; sovereign spreads widen; risk assets deleverage together |
| R3 | Rate decline / policy repair | Yields fall; driven by growth shock or policy/liquidity support |

Always separate:

1. verified market data;
2. computed indicators;
3. deterministic rule inference;
4. robust statistical diagnostics;
5. judgment calls;
6. monitoring suggestions.

## Data Sources

- FRED: US Treasury yields and credit OAS.
- Yahoo Finance: DXY, ETF/index proxies.

## Statistical Layer

The Markov chain is not used as the sole model. It is only used as a transition-smoothing prior.

The upgraded statistical layer includes:

1. deterministic rule posterior;
2. Student-t observation filter with Markov transition smoothing;
3. robust trailing-window change-point risk;
4. ensemble probability.

## R2 Discipline

Do not upgrade to R2 from rates and equity weakness alone. R2 requires credit-spread stress, sovereign-spread stress, or synchronized deleveraging across equities, EM, credit, and high-duration assets.
