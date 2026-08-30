---
id: s15
type: case_study
section: "Section 2. Architecture — before code, and it must be managed"
duration_min: 3
assertion: "Poisoned context: AI copies bad examples from the codebase and amplifies them — but this happens when the architecture is not described and there is no process for managing it; the alternative is ADR + fitness functions"
learning_goal: "[SI] Poisoned context + caveat #261 \"when the architecture is not described and unmanaged\" (bridge to s14)"
learning_outcomes: [LO1, LO7, LO4]
chapter_ref: "§2.3 [for-slide-s13]"
references: [bockeler-thoughtworks]
in_bucket: true
verify_day_of: false
visual_brief: >
  schema_cycle the poisoning loop (main visual on the left, Ocean rounded box): bad design → AI copies ("to it, this is how it's done")
  → design gets worse → AI copies even more confidently. An explicit start marker (gold dot on "bad design") + a continue arrow.
  ABOVE the loop — the CONSPICUOUS caveat #261 (plate): "This happens WHEN the architecture is not described and there is no process for managing it".
  Right — the alternative, 3 bridge plates to s14: the human owns the forks · ADR (human-written context against poisoning) ·
  fitness functions + modular code (managed context). Gold — "AI does not distinguish 'this is how it turned out' from 'this is how it's right'".
  Lucide icons. Source citations — inline right next to the material itself (definition/claim/recommendation), NOT in a bottom footer; small and muted: Böckeler, Thoughtworks.
interaction: none
---

# Visible content

## Title bar
Poisoned context: AI does not distinguish "this is how it turned out" from "this is how it's right"

## Body
[Caveat on top — the conspicuous plate #261]
**This happens when the architecture is not described and there is no process for managing it.** With the practices in place — ADR, fitness functions, architecture-as-code — the loop breaks.

[Left — the poisoning loop, schema_cycle in an Ocean rounded box]

**Poisoned context** (Böckeler, Thoughtworks): AI behaves like "a developer copying from bad examples in the codebase."

bad design → **AI copies** (to it, this is "how it's done here") → design gets worse → **AI copies even more confidently**

[Gold callout]
AI sees a pattern and **continues** it — it does not distinguish a good example from a bad one. The worse the existing architecture, the more strongly AI entrenches it. Böckeler, honestly: "we don't yet have a good way to mitigate this."

[Right — the alternative, 3 plates, bridge to s14]

**The human owns the forks** — makes the architectural decisions; AI on the periphery under the human's choice.

**ADR** — human-written context "we decided X because Y, rejected Z": shared understanding against poisoning.

**Fitness functions + modular code** — deterministic invariants break the loop; clear components give managed context.

## Speaker notes

The thinness of AI in architecture has a concrete observable mechanism, not just an abstract Brooks. Birgitta Böckeler of Thoughtworks named it poisoned context: an AI assistant behaves like the developer who copies from bad examples in the codebase [1]. The mechanism is this: the model generates based on what it sees in the context — on the existing project code. If the project already has architectural problems — duplication, workarounds, outdated patterns — AI reproduces and amplifies them, because to it this is "how it's done in this project," not "what to avoid" [1]. A loop arises: bad design, AI copies, the design gets worse, AI copies even more confidently [1]. Böckeler honestly admits: there is no good way to mitigate this at the model level yet.

And here is the critical caveat for which we reworked this slide. Poisoned context is not a property of "AI in general," but a consequence of the absence of practice. It sets in precisely when the architecture is not described and there is no process for managing it: no ADRs, no fitness functions, no machine-readable model. Where the previous slide's practices are in place, the loop breaks: a shared, human-written understanding of the "why" in the ADR deprives AI of a reason to replicate "how it turned out" [2], and the deterministic invariants of fitness functions automatically catch the self-entrenchment of bad design on every commit [3]. So this is not an argument that "AI must not be let near code," but an argument that "first the practice of managing architecture, then AI inside it."

Hence a concrete human-centric alternative that directly continues the previous slide. First, the human owns the architecture and is capable of what AI by construction does not do: look at a pattern and say "this is how it turned out here, but it's wrong." Second, record decisions explicitly through ADRs — human-written context that lowers the risk of poisoning [2]. Third, fitness functions as deterministic invariants break the loop automatically [3], and modular code gives AI managed context. And note: vector search and RAG do not solve architecture — they improve the model's awareness of how the code is, but awareness of how it is is not the same as judgment about how it should be.
