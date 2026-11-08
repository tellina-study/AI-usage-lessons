---
id: s26
type: assertion_visual
duration_min: 3.8
assertion: "The higher the determinism of a problem and the cost of error, the less room there is for probabilistic AI — for every criterion there is a more correct tool."
learning_goal: "Criteria of non-applicability + the right tool (the judgment core, a table)"
learning_outcomes: [LO2, LO7]
chapter_ref: "§5.1 — Criteria of non-applicability and the right tool"
references: [vonmises-1913, gost-eskd]
visual:
  pattern: schema_matrix
  primary: "An 8-row-criteria × 2-column table (Why probabilistic AI doesn't fit · The more correct tool); fill ≥75%, single line, icons per row"
  illustration:
    type: schematic
    sources:
      - "Self-generated table via PowerPoint add_table + format_table_cell (Ocean palette)"
      - "Lucide icons https://lucide.dev — `file-check`, `shield`, `ruler`, `scale`, `function-square`, `heart-pulse`, `ruler-dimension-line`, `git-pull-request`, 24px badge per row, recolored to Primary mid `#065A82`"
    caption: "Criteria of non-applicability + the right tool"
interaction: none
---

# The higher the cost of error — the less room for probabilistic AI

## Assertion

The higher the determinism of a problem and the cost of error, the less room there is for probabilistic AI — for every criterion there is a more correct tool.

## Visual

A table in an Ocean rounded box: 8 criterion rows × 2 columns. Column A, "Why probabilistic AI doesn't fit"; column B, "The more correct tool." Rows (icon per row, single-line cells, ≥14pt): "Certification calculation" — reproducibility and traceability are needed / a certified deterministic solver + independent verification. "Safety factor" — set by the code, not optimized by a model / a normative value + engineering justification. "Normative inspection (GOST/ASTM/ISO)" — an LLM hallucinates numbers and tolerances / the normative base + a code-compliance inspector. "Legal responsibility" — AI is not a subject of responsibility / a qualified engineer's signature. "An exact solver exists" — an approximation is worse than the exact one / a direct numerical calculation. "Safety of life" — the cost of error is lives / a normative calculation + independent check + NDT with POD. "Units at a seam between systems" — AI confidently confuses units / a machine dimensional check + a single SI system. "A change to the force scheme" — 'in a chat,' with no recalculation = Hyatt / a formal change-request with an independent recalculation. At the bottom, a gold plate (`#F0AB00` bold, 16pt): "AI is a tool for expanding variety and drafting, not an arbiter of truth and not a bearer of responsibility." Fill ≥75%.

## Speaker notes

There is one decisive rule: the higher the determinism of the problem and the cost of error, the less room there is for probabilistic AI. Let's unfold it into a table. A certification calculation needs reproducibility and traceability, and an LLM or a surrogate gives scatter and is not certifiable — the right tool is a certified deterministic solver with a convergence check, plus independent verification. A safety factor is set by the code and the responsible engineer, not "optimized" by a model — the right thing is to take the normative value from the standard with engineering justification. Normative inspection against GOST, ASTM, ISO: an LLM hallucinates standard numbers, grades, tolerances — a normative base and a code-compliance inspector, cross-checking against the primary source, are needed.

Legal responsibility: AI is not a subject of responsibility, the signature and the accountability rest with the engineer — AI is, at most, a draft subject to review. If an exact deterministic solver is available, an approximation is worse and is not needed — a direct calculation, with a surrogate as only a preliminary filter. Safety of life — load-bearing structures, aviation, pressure vessels: the cost of error is lives, and a probabilistic model gives no guarantees — a normative calculation plus an independent check plus physical testing. Units at a seam between systems: AI confidently confuses units, as in Mars and Gimli — a machine dimensional check and a single system of units are needed. A change to the force scheme "in a chat," with no recalculation, is Hyatt; a formal change-request with an independent recalculation is needed.

The summary of the table is the operational form of the course's mission: AI in engineering is a tool for expanding variety and drafting, not an arbiter of truth and not a bearer of responsibility. Notice: this is not a ban on AI, but a designation of its place. Deterministic topology optimization is nowhere banned in this table — the bans concern the probabilistic classes where a guarantee is required.
