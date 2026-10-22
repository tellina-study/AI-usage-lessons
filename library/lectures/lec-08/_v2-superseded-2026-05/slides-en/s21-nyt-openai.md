---
id: s21
type: assertion_visual
duration_min: 2
assertion: "NYT v. OpenAI (Dec 2023): 20M ChatGPT logs ordered to be produced. Summary judgment (SJ) deadline April 2, 2026. Verbatim-citation theory."
learning_goal: "Case 1: training + output similarity"
learning_outcomes: [LO4]
chapter_ref: "§3.2 — NYT v. OpenAI"
references: [bloomberg-law-nyt-openai, nyt-complaint-2023]
visual:
  pattern: assertion_visual
  primary: "Bloomberg Law headline screenshot + timeline (Dec 2023 → Apr 2 2026 SJ) + «Lesson for the engineer»"
  backup: assets/backup/s21-nyt-bloomberg.png
---

# NYT v. OpenAI — training + output similarity (Case 1)

## Assertion

NYT v. OpenAI (Dec 2023): 20M ChatGPT logs ordered to be produced. Summary judgment (SJ) deadline April 2, 2026. Verbatim-citation theory.

## Visual

On top, the assertion 24pt. On the left — a Bloomberg Law-style headline screenshot mock-up in an Ocean rounded box: "OpenAI Ordered to Hand Over 20M ChatGPT Logs to NYT." Top right — a horizontal timeline: Dec 2023 (NYT complaint filed) → 2024-2025 (discovery + procedural fight) → April 2, 2026 (summary judgment (SJ) deadline). Below the timeline — a chip "Verbatim-citation theory: model can verbatim reproduce the training corpus." Below — a large gold Ocean rounded box "LESSON FOR THE ENGINEER": "If the model can cite your training corpus verbatim — that is not 'fair use,' it is infringement evidence. An output-similarity check against training data is mandatory."

## Speaker notes

The first of four landmark copyright cases — the New York Times v. OpenAI. The lawsuit was filed in December 2023. NYT claims that OpenAI trained the GPT models on thousands of NYT articles without a license, and that ChatGPT reproduces protected content verbatim — this is the so-called verbatim-citation theory. During discovery, OpenAI was ordered by the court to produce twenty million ChatGPT logs — an enormous volume that will let NYT's lawyers search for specific examples of regurgitation. Bloomberg Law covers the case in the most detail. The summary judgment deadline — April 2, 2026, that is, two weeks after our lecture. This means that between the delivery of this lecture and a public ruling in the case literally a few weeks may pass. The exact outcome is an open question. What this case has already changed for the industry. Regurgitation as a theory of harm is not a theoretical dispute; it is a documented artifact of large language models, and any defendant in such cases will have to show that it has an output-similarity check. Lesson for the engineer: if the model can cite your training corpus verbatim — that is not "fair use," it is infringement evidence. An output-similarity check against training data is mandatory. What this means in practice. If you build a product on a foundation model, you must have a technical control that tracks how "too similar" the model's output is to its training data. Without such a control you bear regurgitation risk that can become your personal legal debt, not only the debt of the foundation-model vendor. This is a new class of engineering responsibility of 2025-2026 — and it does not appear in any earlier academic ML course.
