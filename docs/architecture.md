# Architecture

AutoAgentAI is organized into **five pillars**. Four are capabilities arranged as a
pipeline; the fifth — the AutoAgent — is the orchestrator that drives them, holds
goals and guardrails, and closes the loop with feedback.

```mermaid
flowchart TB
    subgraph P1[1 · Customer Integration Layer]
        direction LR
        ING[Ingest] --> RES[Resolve identity] --> ENR[Enrich] --> UP[(Unified<br/>profiles)]
    end

    subgraph P2[2 · Insights Engine]
        DISC[Discover patterns] --> GEN[Generate insights] --> RANK[Rank by value]
    end

    subgraph P3[3 · Behaviour Models]
        PUR[Purchase models] 
        OVR[Overall-behaviour models]
        JRN[Journey / lifecycle]
    end

    subgraph P4[4 · Decision Intelligence]
        NBA[Next-best-action] --> SIM[Simulate / score] --> ACT[Recommend or act]
    end

    P1 --> P3
    P3 --> P2
    P2 --> P4
    P4 --> OUT[/"Insights · recommendations · actions"/]

    AGENT(["5 · The AutoAgent<br/>goals · planning · tools · memory · guardrails"])
    AGENT -.orchestrates.-> P1
    AGENT -.orchestrates.-> P2
    AGENT -.orchestrates.-> P3
    AGENT -.orchestrates.-> P4
    OUT -.outcomes / feedback.-> AGENT
```

## The pillars at a glance

| Pillar | Input | Output | Detailed page |
|---|---|---|---|
| **1 · Customer Integration Layer** | Raw data from business sources | Unified, enriched customer profiles + event history | [Customer Integration](customer-integration.md) |
| **2 · Insights Engine** | Profiles + model outputs | Ranked, grounded custom insights | [Insights Engine](insights-engine.md) |
| **3 · Behaviour Models** | Unified profiles + events | Segments, propensities, journeys | [Behaviour Models](behaviour-models.md) |
| **4 · Decision Intelligence** | Insights + model outputs | Recommendations and actions | [Decision Making](decision-making.md) |
| **5 · The AutoAgent** | Goals + everything above | Orchestration, autonomy, memory, audit | [The AutoAgent Loop](agent-loop.md) |

## Logical layers

A different cut of the same system — by layer rather than by pillar — useful when
thinking about where a given responsibility lives:

```mermaid
flowchart TB
    L5["Experience layer<br/><small>console, approvals, chat, alerts, API</small>"]
    L4["Agent layer<br/><small>AutoAgent: planning, tools, memory, guardrails</small>"]
    L3["Intelligence layer<br/><small>insights engine · behaviour models · decision intelligence</small>"]
    L2["Data layer<br/><small>customer integration: ingest, resolve, enrich, store</small>"]
    L1["Source layer<br/><small>business systems: commerce, CRM, analytics, support, marketing</small>"]

    L1 --> L2 --> L3 --> L4 --> L5
    L5 -.actions / feedback.-> L1
```

## Data flow (end to end)

```mermaid
sequenceDiagram
    participant Src as Business sources
    participant CIL as Customer Integration
    participant BM as Behaviour Models
    participant IE as Insights Engine
    participant DI as Decision Intelligence
    participant AG as AutoAgent
    participant U as Operator / System

    Src->>CIL: events, records
    CIL->>CIL: resolve identity, enrich
    AG->>BM: "model current behaviour"
    CIL-->>BM: unified profiles + events
    BM-->>IE: segments, propensities, journeys
    AG->>IE: "find what matters"
    IE-->>DI: ranked insights
    AG->>DI: "frame as decisions"
    DI-->>AG: recommendations / candidate actions
    AG->>U: surface insight + proposed action
    U-->>AG: approve / reject (or auto within guardrails)
    AG->>Src: execute action (e.g. trigger campaign)
    Src-->>CIL: outcome signal
    CIL-->>AG: measured result (feedback)
```

## Cross-cutting concerns

These apply to every pillar and must be designed in, not bolted on:

- **Trust & provenance** — every insight and action carries a trace from raw data
  through reasoning to output, enabling explanation and audit.
- **Privacy & consent** — identity resolution and action-taking respect consent,
  data-minimization, and regional rules (e.g. GDPR/CCPA). Covered further in
  [Customer Integration](customer-integration.md#privacy-consent-and-trust).
- **Guardrails & autonomy level** — what the agent may do without approval is
  explicit and configurable. See [The AutoAgent Loop](agent-loop.md#guardrails-and-autonomy-levels).
- **Observability** — the system's own behaviour (what it looked at, decided, and
  did) is logged and measurable.
- **Extensibility** — new data sources, models, and action types plug in without
  reworking the core.

## Design stance (intentionally not yet decided)

This document describes the **logical** architecture. The **physical** choices —
languages, model providers, datastores, deployment — are deliberately deferred to
the [specifications](specs/index.md) so the concept isn't prematurely locked to a
stack. Where a choice is load-bearing, it will be recorded as a decision with
trade-offs when specs begin.
