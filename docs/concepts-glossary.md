# Concepts & Glossary

A shared vocabulary so the rest of the docs — and later the specs — mean the same
thing by the same words.

## Core concepts

### AutoAgent
The autonomous orchestrator at the heart of the system. It holds goals, decides
what to investigate, invokes the other components as tools, and chooses what to
surface or act on. Distinguished from a passive report by **initiative** (it acts
without being asked) and **continuity** (it runs on its own cadence). See
[The AutoAgent Loop](agent-loop.md).

### Customer-Integrated
The property of being wired into a business's actual customer data and systems.
Concretely: ingesting from the business's sources, resolving identities into one
view per customer, and being able to read context and (eventually) trigger actions
in those systems. See [Customer Integration](customer-integration.md).

### Custom Insight
A finding that is **tailored** (specific to this business / segment / customer),
**grounded** (traceable to the data and reasoning behind it), and
**decision-oriented** (it implies an action). Contrast with a generic benchmark or
a raw metric. See [Insights Engine](insights-engine.md).

### Purchase behaviour
Everything about how a customer buys: what, when, how often, how much, through
which channel, and in response to what. Includes conversion, basket composition,
recency/frequency/monetary (RFM) patterns, price sensitivity, and churn.

### Overall behaviour
The full relationship beyond transactions: engagement, product/feature usage,
support interactions, content consumption, sentiment, and lifecycle stage. Purchase
behaviour is a subset of overall behaviour.

### Decision Making
The discipline of turning insight into action. In AutoAgentAI every insight is
framed as a decision — a recommended next-best-action, a targeting choice, an
intervention — with expected impact and a way to measure the result. See
[Decision Making](decision-making.md).

## The five pillars

| # | Pillar | Role |
|---|---|---|
| 1 | **Customer Integration Layer** | Connect, unify, resolve, and enrich customer data |
| 2 | **Insights Engine** | Generate custom, grounded, decision-oriented insights |
| 3 | **Behaviour Models** | Model purchase and overall behaviour (segments, propensities, journeys) |
| 4 | **Decision Intelligence** | Turn insights into recommendations and actions |
| 5 | **The AutoAgent** | Orchestrate the loop; hold goals, guardrails, and memory |

## Glossary

| Term | Definition |
|---|---|
| **Action** | A concrete step the agent recommends or takes (send offer, flag account, adjust segment). |
| **Attribution** | Measuring the outcome and impact caused by an action the agent took. |
| **CDP** | Customer Data Platform — a system that unifies customer data; AutoAgentAI can sit on one or provide its own integration layer. |
| **Churn** | A customer ending or lapsing their relationship (stopping purchases, cancelling). |
| **Cohort** | A group of customers sharing a defining trait or start time, analyzed together. |
| **Customer 360 / Unified profile** | One resolved record per customer combining all sources. |
| **Entity / Identity resolution** | Deciding that records across sources refer to the same customer. |
| **Feature (model sense)** | A computed signal about a customer used as model input (e.g. days-since-last-order). |
| **Guardrail** | A rule constraining what the agent may do autonomously (budget caps, approval gates, excluded actions). |
| **Human-in-the-loop (HITL)** | A person reviews/approves agent proposals before they take effect. |
| **Insight** | See *Custom Insight*. |
| **LTV / CLV** | (Customer) Lifetime Value — total value a customer is expected to generate. |
| **Next-best-action (NBA)** | The single most valuable action to take for a given customer right now. |
| **Propensity** | A modeled probability a customer will do something (buy, churn, upgrade). |
| **RFM** | Recency, Frequency, Monetary — a classic purchase-behaviour segmentation. |
| **Segment** | A defined group of customers sharing behaviour or attributes. |
| **Signal** | Any piece of customer data that may carry meaning. |
| **Tool (agent sense)** | A capability the agent can invoke — a query, a model, an API call. |
| **Trace / Provenance** | The recorded chain from raw data → reasoning → insight → action, enabling explanation and audit. |

!!! info "Naming discipline"
    When specs are written, terms defined here should be used verbatim. If a spec
    needs a new term, add it here first.
