---
id: s14
type: schema_matrix
section: "Section 2. Architecture — before code, and it must be managed"
duration_min: 3
assertion: "Architecture can be managed with AI through four practices: ADR (durable context), fitness functions (oversight on every commit), C4/architecture-as-code (machine-readable), evolutionary architecture — tools are secondary"
learning_goal: "Approaches to managing architecture (ADR/fitness functions/C4/evolutionary); vendors secondary"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.2 [for-slide-s14]"
references: [nygard-adr, ford-fitness-functions, brown-c4]
verify_day_of: false
visual_brief: >
  schema_matrix 4 columns (one per practice), each with an ANCHOR ICON on top (Lucide): ADR (decision document) ·
  fitness function (shield-check) · C4/architecture-as-code (file-diagram) · evolutionary architecture (increment arrows).
  Rows: "What it is" · "Who prescribes" · "AI's role (secondary)" · "Where the human". Fill ≥75% (all cells filled,
  ≤2 lines of text per cell, font ≥14pt cell / ≥12pt header). One language (EN). Color-coding by semantics:
  durable context / deterministic gate / machine-readability / mutability. Bottom — a judgment plate:
  durable — automatic architectural governance every commit; hype — "our product will ensure the architecture by itself".
  Gold — "the human owns the 'why', AI encodes and checks".
interaction: none
---

# Visible content

## Title bar
Four practices for managing architecture with AI (tools are secondary)

## Body
[schema_matrix — 4 practice columns with anchor icons, rows: what / who / AI's role / where the human]

**ADR** (Architecture Decision Record)
- What: a short (half-page) immutable record per decision — title · context · decision · status · consequences. Stores the "why" that is in neither the code nor git.
- Who: Nygard (2011); Radar — ADOPT ring (keep it in version control)
- AI's role (secondary): edits, cross-checks — but **the human decides and justifies** (otherwise the ADR is invented after the fact)
- Where the human: the author of the fork = the author of the ADR

**Fitness function**
- What: an automatic objective check of an architectural characteristic on **every commit** ("payment does not depend on the UI"; "response < 200 ms")
- Who: Thoughtworks; Rebecca Parsons
- AI's role (secondary): convenient to **write** fitness functions; they in turn **validate** the generated code
- Where the human: decides which invariant is critical

**C4 / architecture-as-code**
- What: architecture machine-readable and versioned (C4: Context/Container/Component/Code; DSL — PlantUML/Mermaid/Structurizr); AI does **drift-detection**
- Who: Simon Brown (C4); Structurizr
- AI's role (secondary): reads as context, generates diagrams, catches drift
- Where the human: owns the text model

**Evolutionary architecture**
- What: ADR + fitness functions + architecture-as-code together = incrementality + managed change
- Who: Ford, Parsons, Kua
- AI's role (secondary): executes inside each of the three practices
- Where the human: holds the direction of the evolution

[Judgment plate, gold]
Durable pattern: **automatic architectural governance on every commit**. Vendor hype: "our product will ensure the architecture by itself". The human owns the "why," AI encodes and checks.

## Speaker notes

Architecture must not only not be neglected — it can and should be managed with AI through four mature practices, and tools here are secondary. The first is architecture decision records, ADRs. This is a short, about half-page, immutable record per significant decision in Nygard's format: context, decision, status, consequences, kept in version control next to the code [1]. Why this is critical in AI-native: the code stores what was done, git stores when and who, but "why this particular decision was made" is stored by nothing except the ADR — and the "why" is precisely the human-written context that a stateless agent lacks and that outlives its sessions [1]. An important failure: writing ADRs cannot be entrusted to the model — from the diff it reconstructs a plausible explanation after the fact, often inventing a justification, and such an empty ADR then poisons the next agent. The author of the fork is the author of the ADR; AI edits and cross-checks, the human decides and justifies.

The second practice is architectural fitness functions: an automatic objective check of an architectural characteristic on every commit, for example "the payment module does not depend on the interface," "the response fits within two hundred milliseconds," "contract coverage does not drop" [2]. The key property is objectivity: as Rebecca Parsons, co-author of "Building Evolutionary Architectures," puts it, "you and I will never argue about whether it passed or not" [2]. In essence this is a deterministic gate enforcing the "why" from the ADR; and the link to AI is twofold — it's convenient for AI to write the fitness functions themselves, and they conveniently validate the code it generated [2].

The third practice is keeping architecture machine-readable and versioned. The description language is Simon Brown's C4 with four zoom levels: context, container, component, code [3]. Architecture-as-code means describing structure with text that is versioned and diffed, rather than drawing pictures; then AI reads the architecture as context, generates valid diagrams, and, most importantly, performs drift-detection — comparing the described model with the actual code and catching the divergence [3]. The fourth practice unites the first three — the evolutionary architecture of Ford, Parsons, and Kua. The section's judgment: the durable pattern is automatic architectural governance on every commit [4]; the vendor hype is the promise that some product will ensure your architecture by itself. The human owns the "why," AI encodes and checks.
