---
id: s23
type: case_study
section: "Section 4. LLM in finance"
duration_min: 3
assertion: "Air Canada: the company is liable for its chatbot's hallucination (court 2024); Klarna: full replacement of people → CSAT↓ → rollback 2025 — augmentation is durable, not replacement"
learning_goal: "Air Canada callback (NOT a duplicate of L3) + the Klarna arc 2023→2025 + criterion grounded/human exit (CQ return 4)"
chapter_ref: "§4.4"
visual_brief: "2 panels: Air Canada callback | Klarna arc. Lesson card + criterion. Gold — «augmentation, not replacement»."
interaction: think_pause
verify_day_of: false
---

# Visible content

## Title bar
The right AI type without grounding and without a human exit = Air Canada / Klarna.

## Body
[Ocean rounded box — 2 panels]

**Case E — Air Canada** *(callback, not a duplicate of L3)*
- the chatbot reported a nonexistent refund policy
- the passenger acted on the answer
- February 2024: a tribunal ruled — **the company is liable for the information its chatbot provides**, and ordered it to pay compensation
- class of error: **hallucination of a financial fact = the organization's legal liability**

**Case F — Klarna** *(arc 2023 → 2025)*
- LLM assistant: ~2/3 of inquiries, resolution time ~11 min → < 2 min, claimed savings ~$40 million/year *(Klarna, 2024)*
- 2024: presented as «AI replaces support»
- mid-2025: CSAT↓ → **returned to hiring people**
- class of error: **full replacement ≠ transformation**

[teal callout — criterion]
A fixed policy/tariff/right → deterministic retrieval/grounded, not free generation; and **in any scenario a path to a human is guaranteed**.

[Gold callout, bottom]
What is durable is not replacement but **augmentation**: AI on the mass routine + a guaranteed human escalation on the emotional/disputed/nonstandard tail.

## Speaker notes

The central question returns sharply for the fourth time — through two connected cases. The first — Air Canada, as a return to the material of Lecture 3, not its duplicate. Briefly: the airline's chatbot reported a nonexistent refund policy to a passenger; the passenger acted on the bot's answer; in February 2024 a Canadian tribunal ruled that the company is liable for the information its chatbot provides, and ordered it to pay compensation. The class of error: hallucination of a financially significant fact equals the organization's legal liability. The transfer to a bank is direct: a chatbot that named a wrong rate or condition creates exactly the same liability — this is an illustration of the previous slide in the form of a court precedent, not a hypothesis.

The second — Klarna, an arc from 2023 to 2025. The fintech deployed a language support assistant: it closed about two thirds of inquiries, cut the average resolution time from roughly eleven minutes to under two, with claimed savings of around forty million dollars a year. In 2024 this was presented as proof that AI replaces support, and many publications cited precisely this half of the story. The denouement: by mid-2025 Klarna recorded a drop in customer satisfaction and returned to hiring people. Let us analyze why this is not «AI turned out to be bad» but a subtler lesson. The assistant really did work: two thirds of inquiries were closed, time fell severalfold, the savings are real. The failure is in a categorical error: the task «answer inquiries» was confused with the system «customer service». Service is also the rare, emotionally charged, disputed cases, where trust and retention are at stake. They are few in number but disproportionately weighty. Full replacement of people optimized the average cost of a contact and collapsed quality in the hard tail.

The lesson is twofold: hallucination of a financial fact equals legal liability, therefore regulated facts must be grounded; full auto-replacement of human support is not durable, and the right role of the model is augmentation, not replacement. Think for thirty seconds: a bank's chatbot named you a rate — how do you recognize the risk of a hallucination without checking the rate itself?
