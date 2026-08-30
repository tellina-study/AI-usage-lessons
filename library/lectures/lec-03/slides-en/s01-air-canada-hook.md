---
id: s01
type: case_study
section: "Section 0. Opening"
duration_min: 3
assertion: "Air Canada paid for its chatbot's invention — because it chose a generative architecture for a task that required a deterministic lookup"
learning_goal: "Hook: the wrong architecture choice = a real consequence; framing the lecture's thesis"
learning_outcomes: [LO7]
chapter_ref: "§Introduction [for-slide-s01]"
visual_brief: "Left — assertion + a brief chronology of the case (question → invented answer → tribunal 14.02.2024 → the company pays). Right — a contrast block: «what was chosen (a generative chat) vs what was needed (a deterministic policy lookup)». Gold highlight — the tribunal decision date / «the company is liable for the bot's invention»."
interaction: open_question
verify_day_of: false
---

# Visible content

## Title bar
"The chatbot invented a policy — the company pays"

## Body
[Left — the case chronology in an Ocean rounded box]

**Case *Moffatt v. Air Canada*, tribunal, 14.02.2024**
- A passenger asked the chatbot about the bereavement fare
- The bot answered: buy at full price, claim the difference back within 90 days
- The real policy **did not allow** this — and it was on the very page the bot linked to
- Tribunal: "the bot is not a separate legal entity" → **the company reimburses the difference**

[Right — the contrast of architectures, 2 blocks]

**What was chosen**
A generative chat — an architecture that by its very nature **composes plausible text**

**What was needed**
A deterministic lookup of a fixed policy — a static page or a rules table

[Gold callout, bottom]
This is **not a model failure. It is the wrong architecture choice for the task.** This entire lecture is about this class of errors.

[Open question, smaller below]
What architecture do you need just to "look up the fare rule"?

## Speaker notes

On February 14, 2024, the Civil Resolution Tribunal of British Columbia issued its decision in *Moffatt v. Air Canada*. The story is simple. Passenger Jake Moffatt visited the airline's website after his grandmother's death, asked the chatbot about the bereavement fare, and got the answer: you can buy the ticket at the regular price and then, within 90 days, file a claim to get the difference back. That was untrue — Air Canada's real policy did not allow a retroactive refund under such a fare, and this was written on the very page the chatbot even linked to. Moffatt bought the tickets, filed the claim, was refused, and the case reached the tribunal. The airline defended itself with the argument that the chatbot is "a separate legal entity responsible for its own actions."[1,2] The tribunal rejected this argument and ordered Air Canada to reimburse the passenger for the difference.

What interests us in this story is not the legal side but the engineering one. The task was elementary: show the user a fixed, known-in-advance fare policy. For such a task there exists an architecture that works perfectly and costs almost nothing: a static page or a deterministic lookup in a rules table. Air Canada chose instead a generative chatbot — an architecture that is fundamentally capable of composing a nonexistent policy, because its job is to generate plausible text, not to retrieve a verified fact.

This was not a model failure. It was the wrong architecture choice for the task. And it is exactly this class of errors — the architecture choice — that this entire lecture is about. Before going further, ask yourself: if the task is merely "look up the fare rule," what architecture closes it — and is AI even needed here at all? We will return to this answer in the section on RAG.

Sources:
[1] McCarthy Tétrault — Moffatt v. Air Canada (BC CRT, 14.02.2024) — the bot invented a refund policy; tribunal: the company is liable for the bot's answer. https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot
[2] ABA Business Law Today — companies are liable for an AI chatbot — "the bot is not a separate legal entity": the wrong architecture choice for a lookup task. https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/
