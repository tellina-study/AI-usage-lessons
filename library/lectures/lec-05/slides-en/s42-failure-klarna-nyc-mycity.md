---
id: s42
type: case_study
section: "Section 5. Support and operations"
duration_min: 2
assertion: "New York City's chatbot advised business owners to break the law, and all 10 of 10 journalists who asked got the same wrong answer: reproducibility moves an event from \"an error\" to \"a property of the system\", and the answer to it is a circuit breaker, not the next iteration"
learning_goal: "An operations failure: reproducibility of a fault as the criterion for stopping immediately"
learning_outcomes: [LO2, LO6]
chapter_ref: "§5.6"
in_bucket: true
interaction: none
protected: true
verify_day_of: false
note: >
  issue #212: the chronicle of Klarna's support headcount (automation growing to the
  equivalent of 853 full-time positions, the staffing curve) was dropped — that is a
  business story about staffing, not a lesson about application. Klarna itself moved to
  s39 as a single line of evidence, in exactly the part that is the lesson: the rollback
  of the "no access to a human" policy. This slide is now purely the New York case. The
  file name is kept deliberately: notes are loaded by the `s42-` prefix, a rename
  improves nothing and risks breaking references in the plan and the speech.
revision: >
  issue #212, EN parity. (1) The EN builder still drew the PRE-Stage-6 composition — a
  Klarna chart, the 853-FTE-equivalent inset, the "not an isolated glitch" headline —
  which the source no longer contains. The visible layer is brought to this file. (2)
  Rule R9: "what happened" first, with the circumstances, the date and the content of
  the advice; the analysis second. (3) The slide's reference registry was reduced to the
  single New York source, mirroring RU.
meme_or_visual: >
  case_study: a "what happened" bar at the top. Below left, a real source image (the
  seal of the City of New York, Wikimedia, public domain) and ten identical silhouette
  icons with the same cross — reproducibility reads as SHAPE and is CAPTIONED. On the
  right, a captioned analysis block: a circuit breaker against the next iteration. A
  gold callout with the criterion at the bottom.
source: "The Markup (29 March 2024) — an investigation of the New York City chatbot"
---

# Visible content

## Title bar
New York: city bot advised breaking the law 10 times out of 10

## Body
[A "what happened" bar; below it ten identical crosses and an analysis block]

**WHAT HAPPENED**

New York City shipped a chatbot for small business owners — to answer questions about city rules. In March 2024 an investigation found the bot advising employers to take their staff's tips and to fire people for reporting harassment, and landlords to turn away tenants with housing vouchers. All of that goes against the law in force, and the advice came confidently, as instruction. All **10 of 10** journalists who asked got the same wrong answer. The mayor acknowledged the errors and did not pull the bot, though switching it off was technically possible.

**ANALYSIS**

Repeatability changes the class of the event. A single error is grounds for a fix. Ten identical answers to ten identical questions are a system property, reproducible on demand, and it can no longer be discussed as an unlucky run.

The decision to keep iterating came after reproducibility had been shown in public. That is the error under review: the data was there, the response stayed the same.

[Gold callout]
Criterion: a reproducible harmful answer calls for a circuit breaker. Next iteration waits. The threshold is named as a number in advance — else, when it has to be applied, it is argued over again and loses to the wish to "polish it".

## Speaker notes

The circumstances first. New York City shipped a chatbot for small business owners — to answer questions about city rules, permits, an employer's obligations. In March twenty twenty-four an investigation found that the bot was advising employers to take their staff's tips and to fire people for reporting harassment, and landlords to turn away tenants with housing vouchers. Everything on that list goes directly against the law in force. And it came confidently, in the form of instruction.

Now the thing that decides this case — repeatability: all ten of ten journalists who asked got the same wrong answer. This is where the class of the event changes. A single error is grounds for a fix; that is the normal life of any system. Ten identical answers to ten identical questions are a property of the system, reproducible on demand. You can no longer discuss that as an unlucky run.

So the criterion is stated as a number: a feeling of "it seems rare" does not work here. The fault reproduces — the response is a circuit breaker, and the next iteration waits. And look at what happened next. The mayor acknowledged the errors and did not pull the bot from public use, although switching it off was technically possible. Which means the decision to keep iterating was taken after reproducibility had been shown in public. That is the error under review: the data was there, the response stayed the same.

Why the threshold has to be agreed in advance. At the moment it has to be applied there is always the argument "we have almost fixed it, let's not switch it off". If there is no threshold set beforehand, that argument wins. Not by force — simply because the other side has nothing to put on the table. A threshold named as a number before the incident is exactly what gets put on the table.

And connect this case with the previous one. Air Canada answers the question of who owns the bot's answer. New York answers a different question: what to do once it is already known that the answer is bad and that it reproduces. Two halves of one accountability.
