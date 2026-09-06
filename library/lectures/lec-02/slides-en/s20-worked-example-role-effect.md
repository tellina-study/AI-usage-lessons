---
id: s20
type: case_study
section: "Section 3. Attention Mechanism"
duration_min: 3
assertion: "A role works through attention weight: role tokens shift the distribution but don't raise actual answer quality"
learning_goal: "Worked example + the full mechanism of the role effect; contrastive example with/without a role + a research caveat on the limits of the effect"
learning_outcomes: [LO7]
chapter_ref: "§3.2 (chapter-part2.md) [for-slide-s20] [FACT-CHECK: Zheng et al., EMNLP 2024 Findings, \"When \\\"A Helpful Assistant\\\" Is Not Really Helpful\"]"
visual_brief: "Top half — Ocean rounded box: the sentence 'The cat ate the mouse because it was hungry,' arrows from 'it' of varying thickness to 'cat' (thick, gold), 'was,' 'hungry,' consistent with s18/s19. Small disclaimer. Bottom half — contrastive example: two Ocean rounded boxes side by side, left 'No role' (prompt 'Explain the GIL' — neutral, generic answer), right 'With a role' (prompt 'You are an experienced Python developer. Explain the GIL' — role tokens highlighted teal, answer more specific, in an expert register). Between them an arrow 'role tokens get weight → shift the distribution of subsequent tokens.' Below — a research callout in 2 lines: (1) exact quote with numbers — 'Zheng et al. (2024, EMNLP Findings; 2410 questions, 162 personas): a persona/role in the prompt does not raise factual accuracy — the effect of any specific role is unpredictable'; (2) a separate line, not tied to Zheng — 'from course observations: a role noticeably changes the tone, style, and content selection of the answer.' Bottom gold callout: 'a role is a tool for controlling style/focus, not an intelligence booster.'"
interaction: retrieval_think_pause
---

# Visible content

## Title bar
"A role works through attention weight — but doesn't raise factual quality"

## Body

### Worked example: where does "it" look?
[Ocean rounded box, top half]

"The cat ate the mouse because **it** was hungry"

[Arrows from the token "it" with varying thickness]
- `it` ⟶ `cat` (thick, gold) — main weight
- `it` ⟶ `was` (medium)
- `it` ⟶ `hungry` (thin)

*Simplification: an aggregate of hundreds of connections across dozens of layers. The model isn't doing grammatical parsing — it's reproducing correlations of usage.*

**Think for 30 seconds:** where will the weight from "it" go in "The server crashed because it ran out of memory"?

### Contrastive example: role present vs. role absent
[2 Ocean rounded boxes side by side]

**No role**
"Explain the GIL" → a neutral, generic answer

**With a role**
"You are an experienced Python developer. Explain the GIL" → role tokens get weight during the generation of every answer token → more specific, more confident, in an expert register

[Research callout]
**Zheng et al. (2024, EMNLP Findings; 2410 questions, 162 personas): a persona/role in the prompt does not raise factual accuracy — the effect of any specific role is unpredictable.**

*Separately from that study — from course observations: a role noticeably changes the tone, style, and content selection of the answer.*

[Gold callout]
**A role is a tool for controlling style and focus, not an "intelligence booster." If you need an answer grounded in your data, give it the data — not a third adjective attached to the word "expert."**

## Speaker notes

Warm-up: "The cat ate the mouse because it was hungry." Reaching the token "it," the model has to resolve what it refers to — and in the attention map the weight is distributed in favor of "cat." The three arrows are a simplification: an aggregate of hundreds of connections across dozens of layers; the model isn't doing grammatical parsing, it's reproducing correlations of usage. Test your intuition: "The server crashed because it ran out of memory." On most models the weight will go to the nearest plausible entity given the semantic context — if your intuition gave a similar answer, you're already thinking in terms of corpus statistics rather than grammar. Note the shift from the previous example: there, the cue was thematic-role plausibility (who is the likely bearer of "hungry"); here, there's no animate-subject cue at all — "it" plausibly refers back to "server," the only entity that can "run out of memory," which is itself a giveaway of the same underlying mechanism: attention resolves pronouns via learned plausibility of who-does-what, not via a fixed grammatical rule.

Now — the reason you already know all this. Let's compare two prompts that are essentially the same. "Explain the GIL" with no role — the model answers neutrally, generically. "You are an experienced Python developer. Explain the GIL" — you've surely noticed that a prompt like this works differently. The mechanism: the tokens "experienced," "Python developer" receive weight in the attention distribution during the generation of every answer token, and the choice shifts toward whatever is consistent with them — the answer becomes more specific and more confident, in an expert register. A role isn't a request to "trust me" — it's an input signal that physically participates in the weighting.

And the boundary of the effect, important to know before you start overusing roles in your prompts: Zheng et al. (2024, EMNLP Findings) tested 2410 questions and 162 personas — a persona/role in the prompt does not raise factual accuracy, and the effect of any specific role is unpredictable. Separately from that study: from course observations, a role noticeably changes the tone, style, and content selection of the answer — a distinct effect, not the same thing as accuracy. A role shifts the distribution, it doesn't add knowledge. If the model doesn't know the answer, the role "expert" won't make it know — it will make it sound more confident without being more correct. Practical takeaway: a role is a legitimate, useful tool for controlling the style and focus of the answer, but don't confuse it with raising accuracy. If you need a precise answer grounded in your data, give the model the data — not a third adjective attached to the word "expert."
