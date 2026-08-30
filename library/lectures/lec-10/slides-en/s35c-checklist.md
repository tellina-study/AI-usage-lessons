---
id: s35c
type: schema_checklist
duration_min: 1.5
assertion: "10 questions in 5 blocks (Classification / Production status / Liability / Lock-in / Connectivity). 8-10 green = buy / pilot; 5-7 = conditional; ≤4 = reject. A minimal audit check, answered not by the vendor's words but by external sources."
learning_goal: "LO2 operationally — an application artifact for due diligence"
learning_outcomes: [LO2]
chapter_ref: "§6.1a Part 3 — Pre-purchase verification checklist"
references: []
visual:
  pattern: schema_checklist_5blocks
  primary: "Vertical schema 5 blocks × 2 items + scoring rubric (8-10 / 5-7 / ≤4)"
---

# Pre-purchase verification checklist for an AI solution

## Assertion

10 questions in 5 blocks (Classification / Production status / Liability / Lock-in / Connectivity). 8-10 green = buy / pilot; 5-7 = conditional; ≤4 = reject. A minimal audit check, answered not by the vendor's words but by external sources.

## Visual

Below the 28pt bold assertion — a vertical schema of 5 blocks, each block in an Ocean rounded box with a Lucide icon 32px Primary mid + 2 nested items.

**Block 1 — Solution classification** (icon `list-checks`):
1. **Ladder rung (L1-L5)** — an unambiguous answer from the vendor?
2. **AI operating mode** — rule-based / ML / CV / sensor-fusion / RAG-grounded / agentic? **Brand ≠ mode**

**Block 2 — Production status** (icon `factory`):
3. **Number of production deployments** — not «sold», not «pilot», not «partner announcement»; verifiable via customer references
4. **Accuracy on edge cases** — a bench-test from an **independent** extension service; documented failure modes

**Block 3 — Liability and regulation** (icon `gavel`):
5. **Liability terms in the EULA** — if «autonomous», who is liable for a collision/damage? Marketing ≠ contract
6. **Regulatory status** — EU AI Act high-risk; FCC compliance; local certifications; request compliance documentation

**Block 4 — Lock-in and exit route** (icon `unlock`):
7. **Data exit route** — access to the processing history, satellite imagery, herd metrics upon termination?
8. **Multi-vendor compatibility** — exclusive or works in a mixed fleet?

**Block 5 — Connectivity and resilience** (icon `wifi-off`):
9. **Minimal connectivity** — always cloud / periodic / offline? What share of functions when the channel fails?
10. **Mechanical fallback** — degradation into an «ordinary tractor / milking machine» when AI is switched off?

To the right of the schema (or below) — a **scoring rubric** in a Teal-tint box:

- **8-10 green** ✓ → buy / pilot ready
- **5-7 green** ◐ → conditional pilot (1-2 sites + exit criteria)
- **≤4 green** ✗ → reject or escalate to expert audit

Bottom callout 14pt italic in a gold-tint box: «**Each item is verified NOT by the vendor's words**, but by **external sources**: independent reports, public registers, customer references, regulatory filings. This is a concrete practical tool for critically evaluating a vendor claim — the skill by which an engineer protects the company from vendor maskirovka».

Footer 12pt italic: «Source: Chapter v3.1 §6.1a Part 3».

## Speaker notes

Before moving to the consolidation of the five criteria, let's give a concrete applicable artifact — a pre-purchase verification checklist for an AgTech solution. This is an operational application of LO-two: critically evaluating a vendor claim — ten questions grouped into five blocks of two items.

Block one — solution classification. The first question: on which rung of the ladder is the solution located? L1, L2, L3, L4 or L5? If the vendor can't answer unambiguously — that's a sign the product mixes levels. The typical "universal platform for the whole agriculture cycle" pattern almost always means the L1 functions aren't worked out. The second question: exactly what operating mode does the AI component use? Rule-based, classical ML, CV, sensor-fusion, RAG-grounded LLM, agentic AI? Brand is not the same as mode. Having gotten the answer, you can predict which class of failures the solution is more vulnerable to.

Block two — production status. The third question: how many production deployments? Not "sold", not "pilot", not "partner announcement". How many of them are verified independently via customer references? The fourth question: what is the model's accuracy on the edge cases of the specific deployment environment — soil type, climate zone, livestock breed? Cross-check: request a bench-test from an independent agricultural extension service, not from the vendor. Additionally — which failure modes are already documented and how does the vendor address them?

Block three — liability and regulation. The fifth question: if the product is sold as "autonomous", who is liable for a collision or damage? If the answer is "the farmer" — that's vendor maskirovka. The marketing says "autonomous", the contract says "you are liable". The sixth question: the regulatory status in the specific jurisdiction? EU AI Act high-risk classification, FCC compliance, locally required certifications? Cross-check: request the compliance documentation; if the vendor refuses — that's a red flag.

Block four — lock-in and exit route. The seventh question: what is the exit route upon terminating the relationship? Who will have access to the processing history, satellite imagery, herd metrics? Cross-check: the wording in the contract. The eighth question: does the solution require an exclusive tie-in or work in a mixed fleet?

Block five — connectivity and resilience. The ninth question: always cloud, periodic synchronization, or fully offline? What share of the functionality is available when the channel fails? The tenth question: what will happen if the AI function is switched off or becomes unavailable — political factors, subscription expiry, a vendor decision? Is degradation into an "ordinary tractor" possible without losing basic functions?

Scoring rubric: eight-to-ten green — buy / pilot ready, the solution passes due diligence for a commercial deployment. Five-to-seven green — conditional pilot, limited piloting on one or two sites with explicit exit criteria. Four or fewer green — reject or escalate to expert audit.

This is a minimal audit check to which a student — or the CTO of any company evaluating an AgTech investment — should have a direct and measurable answer. Each of the ten items is verified not by the vendor's words but by external sources: independent reports, public registers, customer references, regulatory filings. This is a concrete practical tool for critically evaluating a vendor claim — the skill by which an engineer protects the company from vendor maskirovka.

## Sources

- Chapter v3.1 §6.1a Part 3.
