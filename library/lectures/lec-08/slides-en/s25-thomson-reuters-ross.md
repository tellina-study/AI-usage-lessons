---
id: s25
type: assertion_visual
duration_min: 2
assertion: "Thomson Reuters v. Ross (Feb 2025): first US ruling REJECTING «fair use» in AI training. 2200/3000 headnotes infringed. Caveat: Ross — non-generative."
learning_goal: "Case 5: «fair use» rejected (with caveat)"
learning_outcomes: [LO4, LO5]
chapter_ref: "§3.6 — Thomson Reuters v. Ross"
references: [reed-smith-tr-ross, judge-bibas-feb-2025]
visual:
  pattern: assertion_visual
  primary: "Reed Smith analysis screenshot + Warhol v. Goldsmith 4-factor chip + «Lesson: 'fair use' is not the default»"
  backup: assets/backup/s25-thomson-ross.png
---

# Thomson Reuters v. Ross — first US refusal of «fair use» (Case 5)

## Assertion

Thomson Reuters v. Ross (Feb 2025): first US ruling REJECTING "fair use" in AI training. 2200/3000 headnotes infringed. Caveat: Ross — non-generative.

## Visual

On top, the assertion 22pt. On the left — a Reed Smith analysis article screenshot mock-up in an Ocean rounded box. On the right — a large fact card: "Judge Bibas, Feb 2025 · 2200/3000 headnotes infringed · 4-factor 'fair use' rejected." Below the fact card — a Warhol v. Goldsmith chip (4-factor reference). Below this — a large amber caveat box: "⚠ Caveat: Ross — non-generative AI (legal search). LLM/diffusion test cases pending (NYT, Andersen, Getty US)." Below — a gold "LESSON FOR THE ENGINEER": "'Fair use' is not the default. LLM/diffusion test cases are ahead. Do not build a product roadmap on the assumption of 'fair use' as a defense."

## Speaker notes

The fifth case — Thomson Reuters v. Ross Intelligence. This is the first ruling in the US that rejected "fair use" as a defense for AI training. The ruling was issued by Judge Bibas in February 2025. The specifics. Ross Intelligence — a company developing an AI-based legal search engine. To train the model, Ross used Westlaw headnotes — short summary annotations of court decisions that are copyright-protected content of Thomson Reuters. Of the three thousand headnotes used, two thousand two hundred were found infringed. The judge applied the Warhol v. Goldsmith four-factor test for "fair use" and concluded that Ross does not pass this test. An important caveat. Ross — non-generative AI. It is a legal search engine that used headnotes for indexing and matching, not for generating new content. The applicability of this ruling to LLMs and diffusion models is an open question. The test cases in that direction — NYT v. OpenAI, Andersen, Getty US — are still ahead. Reed Smith published a detailed analysis of the ruling, which we cite in the lecture materials. What this ruling has already changed for the industry. Before February 2025, a significant part of the AI industry operated on the assumption that training on copyright-protected content is transformative "fair use," and therefore defensible. The Bibas ruling signals that this assumption is not self-evident. The concrete outcome for generative AI is not yet determined, but the baseline has shifted: "fair use" must be proven, not assumed. Lesson for the engineer: "fair use" is not the default. LLM and diffusion test cases are ahead — NYT, Andersen, Getty US. Do not build a product roadmap on the assumption of "fair use" as a defense. If your business model is tied to using copyright-protected content without licensing — that is a business model on a legally unstable foundation. The alternative — a licensed-corpus model, like Adobe Firefly: training data is a core business asset, not a free externality. This now looks like a structural shift of the industry in 2025-2026: licensed data becomes more expensive, and this cost passes into product pricing.
