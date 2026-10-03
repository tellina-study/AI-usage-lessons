---
id: s38a
type: schema_matrix
section: "Section 5. Support and operations"
duration_min: 2.5
assertion: "AI enters support in two different ways: a suggester at the agent's elbow leaves the answer with a human and delivers a measured gain where there is little experience (+15% resolutions per hour on average and +30% among the least experienced, against a base of 2.1 resolutions per hour; among the most experienced the gain is almost nil), while a bot speaks on the company's behalf and invents rules that do not exist (the Cursor support bot, April 2025)"
learning_goal: "The section's practice: two modes of AI in support, the mechanism for choosing between them by the cost of an error, the measured limit of the benefit"
learning_outcomes: [LO1, LO2, LO3]
chapter_ref: "§5.2"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
revision: >
  issue #212, owner-review 2026-10-01: "slide 38 is a completely unclear and unreadable
  example; let us do AI in support instead (assistants / bots and so on) and show where they
  are good and where they are not". The slide has been remade from end to end. Its previous
  content — observability of AI answers (a trace with versions, a proxy metric, a threshold
  taken from the system's own spread) — has been taken off the slide: it is about controlling
  the model, whereas by that same owner-review the section turns towards the use of AI in
  support. The practice-card form is kept unchanged: WHAT IT IS · HOW IT WORKS (numbered steps
  + a labelled diagram) · WITH AI AND WITHOUT · WHERE IT BREAKS. The numbers are given with a
  baseline: the suggester's effect is stated in percent AND in resolutions per hour before the
  rollout. Style rule: the contrastive "not X, but Y" format is absent from the slide body and
  from the notes.
meme_or_visual: >
  schema_matrix, a single practice card. In HOW IT WORKS, on the right, a labelled measurement
  diagram: the baseline marker "2.1 resolutions per hour before the rollout" and three effect
  bars (all agents +15%, the least experienced +30%, the most experienced ≈0
  with slightly lower quality), and beneath them a counterfactual line about length of service.
source: "Brynjolfsson, Li, Raymond. Generative AI at Work — Quarterly Journal of Economics, 2025 (early version NBER w31161): 5,172 support agents at a Fortune 500 company (small-business software, most of the agents in the Philippines), staged rollout of a GPT-3-based assistant from November 2020 to May 2021; the base before the rollout — 2.1 resolutions per hour, a resolution rate of 0.82, an average handling time of 41 minutes. AI Incident Database, incident 1039 — the Cursor (Anysphere) support bot, April 2025"
note: >
  issue #212: the card form is one and the same across all twelve practices in the deck, and
  this slide may not change it. The Brynjolfsson et al. measurement is to be presented
  honestly: this is a 2020-2021 rollout on a GPT-3-generation model, published in 2025. The
  numbers carry over as an order of magnitude and as the SHAPE of the effect (the gain
  concentrates among the inexperienced), not as a forecast for a 2026 model.
---

# Visible content

## Title bar
AI in support: a suggester at the agent's elbow and a bot that answers on its own

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

AI enters the work with tickets in two ways, and confusing them is expensive. A **suggester** offers the agent an answer; a human sends it, and the same human answers for what was said. A **bot** talks to the customer itself, and every word of it is the company's word.

**HOW IT WORKS**

1. **Sort the ticket flow by the cost of an error.** Information that can be derived in full from your own knowledge base lives apart from a commitment the company pays for in money or answers for in law.
2. **On the information flow, begin with a suggester.** It pays off where there is little experience, and it leaves the answer with a human.
3. **Switch the bot on where the answer follows from a checkable source** — and show that source beside the answer, so the customer can check it.
4. **Two safeguards are compulsory:** a guaranteed path to a live human, and a threshold at which the bot falls silent and calls an agent.

[Labelled diagram on the right: the baseline marker "base before the rollout — 2.1 resolutions per hour", three effect bars: all agents +15%, the least experienced +30%, the most experienced ≈0; the caption "for the most experienced the quality of the conversation is slightly lower: the suggestion offers them the average answer" and a gold panel "an agent with two months on the job and a suggester works like an agent with six months without one"]

**WITH AI AND WITHOUT**

| WITHOUT AI — what support stands on and will go on standing on | WITH AI — what it has added |
|---|---|
| A knowledge base, answer templates, ticket routing, a mentor for the newcomer. Speed runs up against the agent's length of service: knowledge of rare cases takes months to build up and leaves with the person who resigns. | A suggestion in real time on top of that same knowledge base; a bot on the routine flow; a summary of a long thread for whoever picks it up. The knowledge base remains a precondition: where something is missing from it, AI will fill the gap itself. |

[Gold callout — WHERE IT BREAKS]
A bot confidently announces a rule that does not exist. **April 2025:** the Cursor support bot told customers about a "one login per user" limit of its own invention; people cancelled their subscriptions, the company apologised and refunded them — no such policy had ever existed.

## Speaker notes

The second half of quality is people and the tickets they bring. Here AI enters the work in two ways, and telling them apart is compulsory, because the cost of an error is not the same for each. A suggester reads the thread and offers the agent a ready answer; a human sends it, and the human answers for what was said. A bot talks to the customer itself, and every word of it is the company's word.

Let me begin with the suggester, because behind it there is a real measurement rather than a vendor's promise. Brynjolfsson, Li and Raymond published a study of five thousand one hundred and seventy-two support agents at a Fortune 500 company. The assistant was rolled out in stages, from November of two thousand twenty to May of two thousand twenty-one, and that staging is what gives us a comparison with the people who had not been given it yet. The base before the rollout was two point one tickets resolved per hour. The effect: plus fifteen percent on average. And this is where it becomes interesting. Among the least experienced the gain is thirty percent; among the most experienced there is almost none at all, and the quality of their conversations sags a little — they are being offered the average answer, and they can do better than the average. Here is what it all adds up to: an agent with two months on the job and a suggestion works like an agent with six months without one. The suggester carries over to the newcomer what the strong ones already know how to do.

Now the mechanism, in four steps. First: sort the ticket flow by the cost of an error. Information you can derive in full from your own knowledge base, and a commitment the company pays for in money or answers for in law, are two different flows. Second: on the information flow, begin with the suggester — it pays off where there is little experience, and it leaves the answer with a human. Third: switch the bot on where the answer follows from a checkable source, and show that source beside the answer. Fourth: two safeguards are compulsory — a guaranteed path to a live human, and a threshold at which the bot falls silent and calls an agent.

Where this breaks. April of two thousand twenty-five, the company Cursor: their own support bot announced to customers a limit of one login per user. There had never been such a policy; the bot invented it. People began cancelling their subscriptions, the company apologised and refunded them. And hold this in mind: the gain from AI rests on the knowledge base. Where there is no knowledge base, AI will compose whatever is missing.
