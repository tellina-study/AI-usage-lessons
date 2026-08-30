---
id: s12
type: failure_case
duration_min: 1.5
assertion: "Tzachor et al. (Reichman University, Nature Food, November 2023, press coverage 2024-05): 184 questions about pesticide application; GPT-3.5/GPT-4/Bard answer confident-wrong in tens of percent of cases. AP4 — a generic LLM in advisory — is a categorical anti-pattern."
learning_goal: "AP4 categorical anti-pattern + RAG-grounded alternative"
learning_outcomes: [LO2, LO5]
chapter_ref: "§1.5 Part 1 — Strict-in F2 generic LLM hallucinations"
references: [tzachor-2024-nature-food, phys-org-2024-may]
visual:
  pattern: question_answer_2col
  primary: "Left — Q/A example from the Tzachor 2024 paper (cassava farmer + ChatGPT confident wrong); right — AP4 callout + RAG-grounded architecture"
---

# ChatGPT/Bard as an agronomist — «confidently wrong»

## Assertion

Tzachor et al. (Reichman University, Nature Food, November 2023, press coverage 2024-05): 184 questions about pesticide application; GPT-3.5/GPT-4/Bard answer confident-wrong in tens of percent of cases. AP4 — a generic LLM in advisory — is a categorical anti-pattern.

## Visual

A two-column layout.

**Left column (55%) — an example from the study:**

An Ocean rounded box reproducing a Q/A:

**Farmer's question** (a typical one of the 184): «When should glyphosate be applied against fall armyworm in a cassava field at the 4-leaf stage in Kenya?»

**GPT-4's answer (schematically):** "*Upon detecting a fall armyworm infestation in cassava — apply glyphosate at a concentration of X% Y days before harvest*" — specific numbers, a confident tone.

**The problem:** glyphosate is a herbicide, **not an insecticide**. Against fall armyworm you need a Bt spray or a contact insecticide. A generic LLM doesn't know the context and answers confident-wrong.

Below this — a small caption 12pt italic: «Tzachor et al., Nature Food, November 2023 (press coverage 2024-05). 184 questions, GPT-3.5 / GPT-4 / Bard. Co-authors: USA, UK, Kenya, Nigeria, Colombia».

**Right column (45%) — AP4 + alternative:**

A callout with a **gold accent** in an Ocean rounded box:
- **AP4. A generic LLM in advisory mode for high-stakes decisions = a categorical anti-pattern.**

Below it — the alternative architecture (compact diagram):
1. **Database of approved products** (USDA-EPA / EU-EFSA / Rosselkhoznadzor) → retrieval
2. **Farmer's query** → structured query
3. **LLM generation** **only within the retrieved documents** (RAG-grounded)
4. **Under low confidence** → explicit abstention «contact an extension agent»
5. **Logging** for audit

Bottom callout 14pt italic: «**Confident-wrong is more dangerous than admitted-don't-know.** RAG-grounded turns one class of risk into another, fundamentally less dangerous one».

Footer 12pt italic: «Source: Tzachor et al., Nature Food, November 2023 (press coverage Phys.org 2024-05)».

## Speaker notes

The second failure block concerns a popular hope of the last three years: can a consulting agronomist be replaced by an LLM chatbot? This is especially tempting for developing regions, where the density of qualified agronomists is low but most farmers have smartphones with internet.

The Tzachor et al. study from Reichman University in Israel, published in Nature Food in November 2023 (with wide resonance in May 2024 thanks to a Phys.org review), is a controlled experiment on one hundred eighty-four questions about applying pesticides and herbicides to specific crops. GPT-3.5, GPT-4, and Google Bard were tested. The co-authors — research groups from the USA, the UK, Kenya, Nigeria, Colombia; the object — potential use scenarios for ChatGPT-like models by African farmers: cassava, fall armyworm, fertilizer timing. The result: the models confidently recommended the wrong application window for a significant share of questions. On average — tens of percent of confident-wrong answers. This is not "sometimes wrong"; it's a confidently wrong answer with no explicit expression of uncertainty.

An important caveat: this is a study, a controlled experiment, not a documented real-world catastrophe. But the significance is the same. Confident-wrong is more dangerous than admitted-don't-know. A farmer who hears "not sure — consult an expert" consults an expert. A farmer who hears a specific recommendation with a number carries it out. Had a farmer carried out the recommendation from such answers — significant crop damage depending on the crop and the regulator.

The failure mechanism. Generic LLMs are trained on an enormous volume of internet text, including old forums, contradictory sources, marketing materials. They have no grounding in local regulation — neither USDA-EPA, nor EU-EFSA, nor Rosselkhoznadzor — and no mechanism for explicit abstention under low confidence. When asked about a specific herbicide at a specific stage for a specific crop in a specific region, the model generates the most probable text resembling an agronomic recommendation — but without checking whether the product is approved, whether the recommendation is current today, whether the stage matches.

This is our second anti-AI criterion — AP-four. A generic LLM in advisor mode for high-stakes decisions is a categorical anti-pattern. The alternative on the right: a RAG-grounded architecture. Retrieval-Augmented Generation tied to the local regulator. The local regulator's database of approved products as the retrieval source; the farmer's query is turned into a structured query; the LLM generates a recommendation only within the retrieved documents; under low confidence — explicit abstention; logging of all recommendations for audit. This architecture doesn't eliminate errors entirely — but it turns a confidently wrong answer into an honestly uncertain one, which for critical decisions is a fundamentally different class of risk.

## Sources

- Tzachor et al., Nature Food (November 2023; press coverage Phys.org 2024-05) — Reichman University.
- Phys.org coverage (May 2024).
