---
id: s09
type: assertion_visual
section: "Section 1. Requirements — the first artifact"
duration_min: 3
assertion: "Requirements — the first artifact, before any code: the spec-driven practice places a human-reviewed spec between intent and code; three voices of the industry converge that the spec is the central artifact"
learning_goal: "The spec-driven practice as a discipline; the visual of the git tree with spec files; Grove's \"~10-20%\" as rhetoric, not a measurement"
learning_outcomes: [LO1, LO7]
chapter_ref: "§1.1 [for-slide-s08]"
references: [openai-model-spec, grove-new-code, fowler-intent]
verify_day_of: true
visual_brief: >
  MAIN VISUAL (#257) — a repository git tree with spec files first: show
  the directory/commit tree structure, where spec/ (spec.md, design.md, tasks.md) appears
  BEFORE src/ — the spec is versioned next to the code (a git-branch icon, .md files with a human-owner icon).
  On the right — three voices of the industry in an Ocean rounded box: OpenAI Model Spec (living versioned Markdown on GitHub) ·
  Grove "the spec is the valuable artifact, code ~10-20% of the value" · Fowler "intent is the bottleneck".
  IMPORTANT: present "~10-20%" as Grove's rhetoric, NOT a measured fact (a light caveat plate).
  Gold — "the first artifact is the spec, not code". Lucide icons. Source references — inline right against the material itself (definition/claim/recommendation), NOT in a bottom footer; small and muted: Grove/Model Spec/Fowler.
interaction: none
---

# Visible content

## Title bar
The first artifact of development is the specification, not code

## Body
[Main visual — the repository git tree: spec files versioned next to the code]

**spec/spec.md · spec/design.md · spec/tasks.md → src/…**

The specification is a human-owned artifact: what the system must do, with which constraints, in what order; the human **read and accepted** it; it is versioned and feeds all subsequent phases. The most expensive mistakes are the mistakes of this phase: a misunderstood requirement propagates through all stages and surfaces in production.

[Three voices of the industry — Ocean rounded box]

**OpenAI Model Spec** — living, versioned Markdown on GitHub: the spec is a durable, reviewable, diffable artifact, not fleeting prompts.

**Sean Grove (OpenAI)** — "the source specification — that is the valuable artifact"; code is "structured communication".

**Martin Fowler** — the bottleneck of AI development is **intent**: the model writes code better and better, while expressing what to build is still hard.

[Caveat, light]
Grove estimates the share of code at "~10–20% of the value" — this is a **rhetorical provocation, not an empirical measurement**: its purpose is to shift the focus to the spec.

[Gold callout]
AI is strong at the **structuring and completeness** of intent; on the **intent itself** — what the system needs — the human decides.

## Speaker notes

The first phase of the lifecycle and the first node of the git loop. Its leading practice is spec-driven development: the primary, versioned, and reviewable artifact is not code but the specification from which code is generated [3]. The specification here is not a bureaucratic document for the record, but that very human-owned artifact: what the system must do, with which constraints, in what order; what the human read and accepted; what is versioned as living Markdown next to the code, not as a fleeting prompt [2]. A classic engineering truth, known long before AI: the most expensive mistakes are the mistakes of this phase, because a misunderstood requirement propagates through all stages and surfaces in production. A requirement mistake at the requirements phase is worth rewording a paragraph; at implementation — rewriting code; in production — it costs an incident plus lost trust. This curve is what makes the "spec before code" discipline pay off: it catches misunderstanding where it is cheapest.

Why precisely a discipline, and not "AI can write requirements"? Because AI is strong at the structuring and completeness of expressing intent — turning free text into a spec, asking clarifying questions, surfacing missed cases — but the intent itself, what the system needs, stays with the human [1]. Surfacing a missed case is structural work where AI is strong; deciding what the behavior should be is essential complexity where the human decides. This is exactly why the bottleneck of development is not to write code but to precisely express intent [4]. The spec-driven practice is the way to put AI in the first role and the human in the second, observing the order "requirements → design → tasks" with small verifiable units [3].

Three voices of the industry converge that the spec is the central artifact. OpenAI formulates this through its Model Spec — living versioned Markdown, openly published on GitHub: the spec here is a durable, reviewable, diffable artifact, not fleeting prompts [2]. Sean Grove takes the thesis to a provocation: the source specification — that is the valuable artifact, and code is structured communication [5]; and let's caveat right away, so this isn't carried off as a fact: his estimate of the share of code at ten to twenty percent of the value is a rhetorical provocation, not a measurement. Martin Fowler says the same from the other side: the bottleneck is intent, expressing precisely what to build is hard [4]. Three independent sources, one conclusion: the center of gravity has shifted from writing code to the discipline of expressing intent into a versioned artifact.
