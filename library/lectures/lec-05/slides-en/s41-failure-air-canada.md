---
id: s41
type: case_study
section: "Section 5. Support / Operate"
duration_min: 2
assertion: "The tribunal rejected the \"bot is a separate legal entity\" defense: the company is responsible for the bot's answer exactly as for a static page"
learning_goal: "On-point failure #10: Air Canada — the principle of accountability for every bot answer (LO3/LO6)"
learning_outcomes: [LO3, LO6]
chapter_ref: "§5.5 [for-slide-s41]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a "scales of justice" icon with a bot on one pan and a static web page on the
  other — the scales in BALANCE (a metaphor for "you're equally accountable for both"). A
  crossed-out "bot = separate legal entity" icon (the rejected defense).
source: "Moffatt v. Air Canada, 2024 BCCRT 149 (14 Feb 2024)"
---

# Visible content

## Title bar
"The bot is a separate legal entity" — the tribunal rejected this argument in one sentence

## Body
[Scales in balance: bot = static page]

**Air Canada, website chatbot**
- Incorrectly stated a retroactive bereavement-fare discount
- Tribunal: **CAD $812.02** — the company is responsible for the bot's answer **as it would be for a static page**

[Gold callout]
You own every answer the bot gives — no more, but not one gram less accountability than for any other content on the site

## Speaker notes

In November 2022, Air Canada's website chatbot incorrectly told a customer that a bereavement fare could be requested retroactively within ninety days — the actual policy did not allow this. The customer bought full-price tickets and was denied the discount. In February 2024, the tribunal awarded $812.02. Air Canada's defense: the chatbot is a separate legal entity, responsible for its own actions. The tribunal called this a remarkable submission and rejected it: the company is responsible for all the information on its website, whether it comes from a static page or from a chatbot.

The mechanism, tied to the Support/Operate phase: there was no process to synchronize the chatbot's knowledge base with the company's actual policy — support content was managed separately from a single source of truth. Why the small amount isn't a sign of insignificance, but reinforces the lesson: $812.02 is the price of two tickets, but it's exactly the modesty of the sum that makes the precedent clean. The tribunal wasn't settling a complex dispute over large sums, it was issuing a principled ruling on accountability.

The lesson, stated as a principle: you own every answer the bot gives — as you would a static page on your site. Legal accountability for an AI agent's answers rests entirely with the company; "the chatbot made a mistake" is not a defense. The criterion: deploying a chatbot that answers questions with legal consequences, without automatic synchronization to a single source of truth, is a support process not ready for automation. The alternative: a RAG architecture with a single source of truth, mandatory citation-linking to the exact policy clause in every answer, and periodic audits of bot answers against current policy.
