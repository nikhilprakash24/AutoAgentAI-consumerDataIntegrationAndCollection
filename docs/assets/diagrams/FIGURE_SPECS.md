# Figure Specs

Two kinds of visuals are used in these docs:

1. **Mermaid diagrams** — written as code throughout the docs. They render
   automatically on GitHub *and* on the hosted site, and are editable as text. No
   image generation needed. The rest of this page lists where they live.
2. **Rich conceptual visuals** — polished illustrations Mermaid can't produce (hero
   images, layered concept art, marketing-grade figures). These are **specified
   below as generator-ready prompts** so you can produce them later with an image
   tool and drop the files into `docs/assets/diagrams/`.

---

## Part A — Mermaid diagrams already in the docs

| Diagram | Location | Shows |
|---|---|---|
| Five pillars | `README.md`, `index.md` | The pillar pipeline + agent |
| Product-in-one-picture | `index.md` | Sources → integration → agent → actions |
| Fragmentation problem | `problem-motivation.md` | Why data is siloed |
| Pillar pipeline (detailed) | `architecture.md` | All five pillars internally |
| Logical layers | `architecture.md` | Source → data → intelligence → agent → experience |
| End-to-end sequence | `architecture.md` | The full request/response + feedback |
| Integration flow + ERD | `customer-integration.md` | Ingest→resolve→enrich; conceptual entities |
| Insight generation | `insights-engine.md` | Methods → candidates → rank |
| Behaviour segmentation quadrant | `behaviour-models.md` | Value vs. engagement |
| Lifecycle state machine | `behaviour-models.md` | Prospect → … → churned/reactivated |
| Insight→decision→outcome | `decision-making.md` | The last-mile loop |
| Agent loop + autonomy ladder | `agent-loop.md` | Perceive→reason→act→learn; L0–L4 |
| Use-case flows | `use-cases.md` | Per-scenario arcs |
| Roadmap phases | `roadmap.md` | Phase 0→5 |

To edit any of these, find the ` ```mermaid ` block in the named file. Preview with
`mkdocs serve` or directly on GitHub.

---

## Part B — Rich visuals to generate (prompts)

Each entry gives a **suggested filename**, **where it would go**, and a
**generator prompt**. Style guidance is shared below so the set looks consistent.

### Shared style guide

> Modern, clean, professional SaaS aesthetic. Indigo-to-deep-purple accent palette
> on a light background (and a dark-mode variant where noted). Flat vector / subtle
> depth, generous whitespace, rounded shapes, thin consistent linework. No
> stock-photo people, no clutter, no fake chart numbers. Legible labels. 16:9 unless
> stated.

---

### Fig 1 — Hero / concept image
- **File:** `hero.png` · **Use:** top of `README.md` / site home.
- **Prompt:**
  > A clean, modern hero illustration for an AI product called "AutoAgentAI." Center:
  > a friendly abstract AI agent represented as a glowing node/orb made of connected
  > lines. Flowing into it from the left, several labeled data streams (transactions,
  > web events, CRM, support, reviews) merging into one. Flowing out to the right,
  > three labeled outputs: "Insights," "Decisions," "Actions." Indigo-to-purple
  > gradient accents on a light background, flat vector style, lots of whitespace,
  > subtle glow. 16:9.

### Fig 2 — The five pillars (polished)
- **File:** `pillars.png` · **Use:** `architecture.md` header (alongside the Mermaid version).
- **Prompt:**
  > A polished horizontal diagram of five connected pillars for a customer-intelligence
  > platform. Four pillars in a left-to-right pipeline labeled "Customer Integration,"
  > "Behaviour Models," "Insights Engine," "Decision Intelligence," each as a rounded
  > card with a simple icon. A fifth element, "The AutoAgent," sits above as an orb
  > connected by dotted lines to all four, labeled "orchestrates." Indigo/purple on
  > light, flat vector, clean icons, thin connectors with arrowheads. 16:9.

### Fig 3 — The autonomous agent loop (polished)
- **File:** `agent-loop.png` · **Use:** `agent-loop.md` header.
- **Prompt:**
  > A circular loop diagram with four labeled stages arranged clockwise: "Perceive,"
  > "Reason & Plan," "Act," "Learn," connected by curved arrows forming a continuous
  > cycle. In the center, a small AI agent orb. Each stage has a minimal icon (eye,
  > brain/gears, lightning/hand, upward arrow). Indigo/purple accents on light
  > background, flat vector, clean. Square (1:1).

### Fig 4 — Customer 360 / unified profile
- **File:** `customer-360.png` · **Use:** `customer-integration.md`.
- **Prompt:**
  > An illustration of identity resolution: on the left, five scattered, mismatched
  > record cards (POS receipt, CRM contact, anonymous web-device icon, support ticket,
  > email contact), each with a small question mark. Arrows converge to the right into
  > a single clean "unified customer profile" card showing combined attributes.
  > Convey "many fragments → one resolved view." Indigo/purple on light, flat vector,
  > no real personal data. 16:9.

### Fig 5 — Insight anatomy card
- **File:** `insight-anatomy.png` · **Use:** `insights-engine.md`.
- **Prompt:**
  > A single clean "insight card" UI mockup for an AI analytics product. It shows,
  > top to bottom: a plain-language Statement, an Evidence row, a Confidence meter, a
  > Scope ("applies to N customers"), an Expected impact figure, and a "Suggested
  > action" button. Minimal, modern dashboard style, indigo/purple accents, light and
  > dark variants. 4:3.

### Fig 6 — Autonomy ladder
- **File:** `autonomy-ladder.png` · **Use:** `agent-loop.md` (guardrails section).
- **Prompt:**
  > A five-step ascending staircase, each step a labeled level: "L0 Observe,"
  > "L1 Recommend," "L2 Act with approval," "L3 Act within limits," "L4 Autonomous."
  > A small agent orb climbs the steps; a dotted "trust / track record" arrow runs
  > upward alongside. Indigo/purple gradient darkening as it ascends, light
  > background, flat vector, clean labels. 16:9.

### Fig 7 — Roadmap timeline
- **File:** `roadmap.png` · **Use:** `roadmap.md` header.
- **Prompt:**
  > A clean horizontal roadmap with six milestones labeled "Phase 0 Concept & Docs,"
  > "Phase 1 Specs," "Phase 2 Integration," "Phase 3 Insights," "Phase 4 Decisions,"
  > "Phase 5 Autonomy." Phase 0 marked as current/done with a checkmark. Each milestone
  > a node on a path with a small icon. Indigo/purple on light, flat vector. 16:9.

---

## How to add a generated image to the docs

1. Generate the image from the prompt and save it into `docs/assets/diagrams/`
   (e.g. `docs/assets/diagrams/hero.png`).
2. Reference it in the relevant markdown page, for example in `index.md`:
   ```markdown
   ![AutoAgentAI concept](assets/diagrams/hero.png)
   ```
   (Paths are relative to the markdown file. From `docs/index.md`, use
   `assets/diagrams/hero.png`; from a page in `docs/specs/`, use
   `../assets/diagrams/hero.png`.)
3. Commit and push — the site rebuilds automatically.

!!! tip "You don't have to generate anything to ship"
    The Mermaid diagrams already carry every page. The Part B visuals are polish for
    when you want a more designed look — generate them on your own schedule.
