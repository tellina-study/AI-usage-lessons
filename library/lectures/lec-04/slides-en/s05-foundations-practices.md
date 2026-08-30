---
id: s05
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 2
assertion: "This lecture is a digest of practices: modern approaches from industry leaders + time-tested classics; tools change, practices are durable"
learning_goal: "Source frame: show that the phase discipline rests on two bodies — fresh practices of leading players and classics that have withstood decades; all with references"
learning_outcomes: [LO1, LO7]
chapter_ref: "§0.5 [for-slide-s05a]"
visual_brief: >
  TWO LISTS side by side (Ocean rounded box each): A "Modern practices (leaders)" ≥5 items,
  B "Time-tested classics" ≥5 items. Each item — a name (clickable hyperlink) +
  1 line of the gist. Compact numbered markers [N]; clicking the name leads to the canonical URL.
  The heading is about the lecture = a digest of practices, not a catalog of tools.
interaction: none
verify_day_of: true
---

# Visible content

## Title bar
This lecture is a digest of practices: modern approaches from leaders + time-tested classics

## Body

[Two lists side by side; each name is a clickable link to the canonical source]

**A. Modern practices (industry leaders)**
- **Anthropic — Claude Code / AI-Native SDLC** [1] — an agentic git loop: each stage commits a versioned artifact; the human is accountable at the gates.
- **OpenAI — Model Spec** [2] — spec-as-contract: versioned Markdown; each clause = an example prompt = a unit test.
- **GitHub — Spec Kit** [3] — "intent is the source of truth"; `/specify → /plan → /tasks → /implement`; small verifiable tasks.
- **Google — DORA 2025** [4] — "AI amplifies what is already there": throughput rises, stability does not; seven capabilities.
- **Thoughtworks — Böckeler "Exploring Gen AI"** [5] — the assistant suggests, the developer owns; harness engineering; Radar "Adopt/Hold".
- **Simon Willison — "Vibe engineering"** [6] — the disciplines an LLM rewards: tests, planning, documentation, version control, review.

**B. Time-tested classics**
- **Brooks — "No Silver Bullet"** [7] — essential vs accidental complexity; "the hardest part — deciding what to build" stays with the human.
- **Kent Beck — "TDD: By Example"** [8] — red-green-refactor; test-as-specification — the foundation of verification discipline.
- **Nygard — ADR** [9] — lightweight immutable records of the "why" of a decision under version control — durable context.
- **Ford/Parsons/Kua — "Building Evolutionary Architectures"** [10] — fitness functions make "fitness" objective and automatic.
- **Fowler — "Refactoring"** [11] — the discipline of small verifiable changes — what AI rewards, and without which it amplifies tech debt.
- **Simon Brown — C4** [12] — architecture-as-code (Context/Container/Component/Code): a textual, diffable model that AI consumes.

[Caption, gold]
Tools will change over quarters — these practices are durable: they rest on the nature of complexity, not on the maturity of a product.

## Speaker notes

Before diving into the phases, let's honestly show where all the recommendations of this lecture come from. These are not personal preferences and not a retelling of vendor advertising, but a digest of two bodies of practice. The first — modern approaches from those who are building tools and processes right now: Anthropic with their AI-Native SDLC, where each stage commits a versioned artifact and the human stays accountable at the gates [1]; OpenAI with Model Spec, where the specification becomes a contract and each of its clauses works as an example prompt and a test [2]; GitHub Spec Kit with the idea that "intent is the source of truth" and small verifiable tasks [3]; the DORA 2025 report with seven delivery capabilities and the key conclusion "AI amplifies what is already there" [4]; Thoughtworks and Böckeler with the Exploring Gen AI series and the notion of harness engineering, where the assistant suggests and the developer owns [5]; and Simon Willison with "vibe engineering" — a list of the disciplines an LLM rewards: tests, plans, reviews [6].

The second body — the classics that have withstood decades. Brooks with the distinction between essential and accidental complexity, where "what to build" stays with the human [7]; Kent Beck with TDD, where test-as-specification sets red-green-refactor [8]; Nygard with ADR — immutable records of the "why" under version control [9]; Ford and Parsons with evolutionary architectures and fitness functions that make "fitness" objective and automatic [10]; Fowler with refactoring and the discipline of small verifiable changes [11]; and Simon Brown with the C4 model — architecture-as-code, a textual diffable model intelligible to AI [12].

Why is it important to show this right away: tools and their "leadership" change over quarters, while these practices are durable for years — because they rest on the nature of complexity [7], not on the maturity of a particular product. It is precisely at the intersection of the leaders' fresh practices and the proven classics that we will build the discipline by phase.
