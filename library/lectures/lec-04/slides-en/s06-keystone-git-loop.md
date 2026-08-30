---
id: s05
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 3
keystone: true
assertion: "AI development as a discipline is a cycle of human-owned artifacts spec→ADR→plan→PR→incident, each owned by a human; on this skeleton the methods of different players converge"
learning_goal: "KEYSTONE — the discipline git loop (a chain-diagram of artifacts) + definition of a phase (input/output/artifact) + uneven phase maturity (sub-line); convergence of methods = 1 caption"
learning_outcomes: [LO1, LO7]
chapter_ref: "§0.6 [for-slide-s05]"
visual_brief: >
  A CHAIN-DIAGRAM (NOT a text list; keystone mandate). A horizontal chain of 5 artifact-nodes,
  each human-owned (a "human owns" icon on every node): [specification] → [ADR] → [plan] →
  [pull request] → [incident record], forward arrows along the chain; an EXPLICIT return arrow
  incident → specification (closes the cycle). Each node color-coded Primary mid; nodes in Ocean rounded boxes.
  Under each node — 1 micro-caption "input→output" of the phase. As a sub-line (not competing with the chain) —
  uneven phase maturity: strong (implementation/review/requirements/testing) Primary mid · thin
  (architecture/delivery/operations) light muted · a bright spot (documentation) gold dot.
  ONE caption line at the bottom: "on this Anthropic / OpenAI / DORA / Thoughtworks converge" (details — in the synthesis).
  Cap ≤3 load-bearing: (1) the chain of artifacts, (2) phase = input/output/artifact, (3) uneven maturity as a sub-line.
  Gold — the return arrow (the cycle closes) + the bright spot of documentation. Node font ≥16pt, captions ≥12pt.
  5-sec readability: the main idea — "discipline = a chain of versioned artifacts, each owned by a human".
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Discipline is a chain of versioned artifacts, each owned by a human

## Body
[A chain-diagram of human-owned artifacts — the main visual, each node in an Ocean rounded box]

**specification → ADR → plan → pull request → incident record → (back to specification)**

This is the **discipline git loop**: all artifacts live under version control, are versioned and reviewed like code. AI participates **inside** the nodes (drafts the spec, proposes the ADR, writes code in the PR), but each node is **owned** by a human — who reads, edits, accepts, is responsible. The return arrow closes the cycle: an incident gives rise to a new requirement.

**An SDLC phase** — a stage with its own **input / output / artifact**. The question about AI becomes concrete: not "does AI help development", but "which practice makes reliable this transformation — from spec to ADR, from ADR to plan, from plan to PR".

[Sub-line — uneven phase maturity]
Practices are unevenly mature: strong phases (implementation, review, requirements, testing) · thin ones (architecture, delivery, operations — the human practice leads) · one **bright spot** — documentation (the only measured clean plus). The reason is durable: where essential complexity (Brooks) dominates, the human leads.

[Caption, gold]
On this skeleton of practices, **Anthropic, OpenAI, DORA, Thoughtworks converged independently** — which means we have a method, not a fad.

## Speaker notes

This is the key slide of the lecture, and everything that follows depends on it. Software development, if done as an engineering discipline, is not "we write code with an assistant" but a cycle of human-owned artifacts. A specification turns into an architecture decision, that into a plan, the plan into a pull request, and operations give rise to an incident record that comes back as a new requirement into the specification. Let's call this the discipline git loop — "git" because all these artifacts live in the version control system, are versioned and reviewed like code [1].

Read this chain like so: each node is a human-owned artifact produced by its phase; an arrow is the handoff of that artifact to the next phase as context; the return arrow from the incident to the specification closes the cycle. AI participates inside the nodes — it drafts the spec, proposes the architecture decision, writes code in the pull request — but each node is owned by a human: they read, edit, accept, and are responsible for the consequences [1]. Worth naming separately is the role of the specification: in the Model Spec approach it is a contract, versioned next to the code, not a fleeting prompt [2]. This is the very skeleton on which the lecture strings everything else: not "a tool for every phase", but the discipline of producing versioned artifacts that feed AI and keep responsibility with the human [4].

The key property of a node is the definition of a phase through input, output, and artifact: a phase takes the artifact of the previous node, transforms it, and yields its own. That is why we ask the question about AI concretely: not "does AI help", but "which practice makes this transformation reliable". And finally — convergence: Anthropic [1], OpenAI [2], the DORA program [3], and Thoughtworks with their harness engineering, where the assistant suggests and the human owns, independently arrived at this same phase skeleton [4]. Different players with different interests reproduced one and the same skeleton — which means we have a method, not a fad.
