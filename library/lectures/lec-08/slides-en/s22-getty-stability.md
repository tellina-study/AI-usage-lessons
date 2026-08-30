---
id: s22
type: assertion_visual
duration_min: 2
assertion: "Getty v. Stability AI: UK High Court 04.11.2025 — Stability won the primary claims (weights ≠ copy under CDPA). US case MTD 10.02.2026."
learning_goal: "Case 2: cross-jurisdiction split (UK win vs US pending)"
learning_outcomes: [LO4]
chapter_ref: "§3.3 — Getty v. Stability AI"
references: [bird-bird-ruling, getty-stability-uk]
visual:
  pattern: assertion_visual
  primary: "Bird & Bird ruling screenshot + UK vs US split visual + «Lesson: check both jurisdictions»"
  backup: assets/backup/s22-getty-uk-ruling.png
---

# Getty v. Stability — UK win vs US pending (Case 2)

## Assertion

Getty v. Stability AI: UK High Court 04.11.2025 — Stability won the primary claims (weights ≠ copy under CDPA). US case MTD 10.02.2026.

## Visual

On top, the assertion 24pt. Center — a split visual: the left half "UK High Court" (Union Jack subtle background tint) with a green marker "Stability won primary claims (CDPA — weights ≠ copy)" + date 04.11.2025; the right half "US case" (subtle US flag tint) with an amber marker "MTD 10.02.2026 — pending" + date 10.02.2026. Below the split — a Bird & Bird ruling article screenshot in an Ocean rounded box. Below — a large gold "LESSON FOR THE ENGINEER": "Jurisdictions diverge — what is legal in the UK under CDPA is not legal in the US under 'fair use.' For global deployment, check both."

## Speaker notes

The second copyright case — Getty Images v. Stability AI. This case illustrates a critically important fact for engineers: different jurisdictions issue different rulings on the same type of dispute. The UK High Court ruling of November 4, 2025: Stability AI won the primary copyright claims. The key legal logic under the UK Copyright, Designs and Patents Act 1988 — CDPA: the model's weights are not a "copy" in the sense of UK copyright law. Accordingly, training the model on Getty images is not an infringement of primary copyright under the CDPA. This is a win for the AI industry in the UK. In parallel runs the US case with motion-to-dismiss hearings on February 10, 2026. The US legal contour is fundamentally different: the "fair use" doctrine in Section 107 of the Copyright Act with a four-factor test. Here a completely opposite outcome is possible. Bird and Bird, which specializes in IP law, published a detailed analysis of the UK ruling, which we cite in the lecture materials. What this jurisdictional split means practically. Lesson for the engineer: jurisdictions diverge. What is legal in the UK under CDPA is not legal in the US under "fair use." For global deployment, check both. If you build a creative AI product for the global market, you must have a jurisdiction-aware compliance layer: the product may behave differently depending on where it is deployed. This is not a theoretical requirement — it is already an empirical fact of 2025-2026. And one more important nuance. Stability's UK win does not mean "no risk in the UK." It means only "primary copyright claims rejected." Secondary claims — for example, trademark or passing-off — may remain. And right of publicity in any jurisdiction is a separate, non-copyright class of legal regulation. The jurisdictional split is not "the UK legalized AI training," but only "a UK ruling on a specific type of claim."
