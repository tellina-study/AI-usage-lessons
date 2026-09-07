---
id: s16
type: assertion_visual
section: "Section 3. Credit scoring"
duration_min: 3
assertion: "Scoring — tabular ML (logreg/GBM+SHAP/scorecard), deliberately NOT a neural network/LLM: explainability = a regulatory requirement, not a wish — 4 arguments"
learning_goal: "Unfolded criterion «why NOT a neural network/LLM» (≥4 arguments) + reason codes inspector analogy"
chapter_ref: "§3.1, §3.3"
visual_brief: "Left — 4 compact argument cards. Right — VISUAL d16 (anchor analogy «credit inspector»: the interpretable model shows reason codes line by line vs the black box refusing). Gold — «explainability = a condition of lawfulness»."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
A black box in scoring is inapplicable in principle — not "less convenient".

## Body
[Ocean rounded box — 4 argument cards 2×2]

**1. Explainability = the law**
A customer who is refused is by law owed an understandable explanation (**reason codes**: "high debt burden"). "The algorithm decided so" is inadmissible.

**2. The data is tabular**
A structured table of features. Deep networks are strong on text/audio/image; on tabular data boosting is competitive at incomparably greater interpretability.

**3. Audit > +1% accuracy**
The regulator must reproduce the decision, verify the absence of discrimination. A stable explainable model matters more than an opaque, slightly more accurate one.

**4. What breaks with a black box**
Cannot explain → a violation · cannot audit for bias → a crisis (Apple Card) · unstable → cannot defend before the regulator.

[Analogy card]
An interpretable model is a credit inspector showing the calculation line by line (reason codes from logreg / GBM + SHAP). A black box is an inspector who says "no" and refuses to explain. In a regulated industry the second is inadmissible **by law**.

[Gold callout, bottom]
"New = a neural network, therefore better" in scoring is a structural error: explainability here is not a bonus, but a **condition of lawfulness**.

## Speaker notes

Credit scoring is the assessment of a borrower's creditworthiness: from data about the customer the system produces a default-risk score, and on its basis a decision about issuance, limit, and rate is made. The type of AI for this task in the industry is classical tabular ML: gradient boosting, logistic regression, scorecards. This is deliberately not a deep neural network and not a language model, and the reason is not that neural networks compute worse, but the requirements of the task itself. Let's unfold this as a full criterion of four arguments.

First: explainability is a regulatory requirement, not a wish. A credit decision is regulated. A customer who has been refused is by law owed an understandable explanation of the reason — so-called reason codes: high debt burden, short credit history. The answer "the algorithm decided so" is legally and reputationally inadmissible. A model from which the reason cannot be extracted is inapplicable in principle in this task — not less convenient, but inapplicable. Second: the data is tabular, not text and not image; deep networks give an advantage on unstructured data, but on tabular data gradient boosting is steadily competitive at incomparably greater interpretability. Third: audit and stability matter more than one percent of accuracy; the regulator must be able to reproduce the decision and verify the absence of discrimination. Fourth: what breaks with the wrong choice — an opaque network cannot be explained to the customer, cannot be audited for bias, cannot be stably reproduced and defended before the regulator.

So that this does not remain a label, an analogy. An interpretable scoring model is like a credit inspector who does not just say "no", but shows their calculation line by line: which feature shifted the decision by how much — these are exactly the reason codes, and from gradient boosting they are extracted by the standard SHAP method. A black box is like an inspector who says "no" and refuses to explain. In a regulated industry the second is inadmissible by law. The reflex "new means a neural network, means better" here is a direct structural error: the correct type of AI is determined by the structure of the data and the hard constraints of the task, and explainability here is a condition of lawfulness, not a bonus.
