---
id: s18
type: case_study
section: "Section 3. Credit scoring"
duration_min: 3
assertion: "Apple Card: NYDFS did NOT find a violation of law — the failure was in opacity; proxy bias is real: removing sex/race from the input does not prove the absence of discrimination"
learning_goal: "Precise wording of the outcome + proxy-bias mechanism FROM SCRATCH + criterion (CQ return 3); forward→Obermeyer L7"
chapter_ref: "§3.4"
visual_brief: "Left — precise facts. Right — proxy bias from scratch + criterion + forward-pointer. Gold — «absence of a feature ≠ absence of bias»."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Even a formally lawful model without explainability creates a crisis.

## Body
[Left — Ocean rounded box, precise facts]

**Apple Card / Goldman Sachs, 2019–2021**
- November 2019: a viral thread — a limit ×20 higher for the husband than the wife (joint tax filing, wife's credit score higher)
- NYDFS opened an investigation (~400,000 applicants)
- **March 2021: NYDFS did NOT find a violation** of fair-lending laws
- **BUT:** clients received no explanations; «the algorithm decided so» = a regulatory-reputational crisis

*To claim «discrimination was proven» is factually incorrect.*

[Right — Ocean rounded box]

**Proxy bias «in plain terms»**
The engineer does not feed in sex/race. But features that **correlate** with them remain: ZIP code, spending history, employment. The model, optimizing accuracy, **indirectly reconstructs** the forbidden feature through proxies — with no intent whatsoever.

[teal callout — criterion]
A regulated decision requires simultaneously: reason codes + appeal path (a human on the disputed case) + a bias audit of outcomes **BEFORE production**.

[forward-pointer card, small]
*The canonical analysis of the mechanism (Obermeyer/Optum) — Lecture 7 (medicine).*

[Gold callout, bottom]
«We do not use protected features» — a **necessary but completely insufficient** condition. The only proof is a direct audit of outcomes across groups.

## Speaker notes

The central question returns sharply for the third time. The case — Apple Card and Goldman Sachs, November 2019. The precise facts must not be oversimplified. A developer published a viral thread: he was approved for a credit limit roughly twenty times higher than his wife's, despite a joint tax filing and a higher credit score for the wife; similar complaints appeared. The New York State regulator opened an investigation. And here is the critically important nuance of the outcome: in March 2021, after analyzing data on about four hundred thousand applicants, the regulator did not find a violation of fair-lending laws — the decisions were explained by credit policy and were not deemed unlawful discrimination by sex. To claim «Apple Card provably discriminated against women» is factually incorrect. But the regulator explicitly pointed to opacity: clients could not obtain an explanation of a decision, and the answer «the algorithm decided so» undermined trust. That is, the failure is not proven discrimination but a regulatory-reputational crisis due to unexplainability.

Now let us introduce, from scratch, the mechanism that makes this class of failures dangerous even without malicious intent — proxy bias. Suppose an engineer deliberately does not feed the forbidden features — sex, race — into the model. Discrimination seems ruled out. But the data still contains features that correlate with the forbidden ones: ZIP code, the structure and history of spending, employment type. The model, optimizing accuracy, indirectly reconstructs the forbidden feature through these proxy variables and begins to treat groups systematically differently while formally not seeing them. An analogy: you removed the «sex» field from the form but kept a dozen fields that together make the sex almost unambiguously guessable. Therefore «we do not use protected features» is not proof of the absence of bias; the only proof is a direct audit of the model's outcomes across protected groups. The criterion: a regulated credit decision requires simultaneously reason codes, a human appeal path, and a bias audit of outcomes before production, not after the scandal. The canonical analysis of the mechanism will come in Lecture 7 on a medical case.
