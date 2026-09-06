---
id: s27
type: case_study
section: "Section 4. Sampling and Generation"
duration_min: 2.5
assertion: "Temperature is a divisor on the logits: it changes the sharpness of the choice, not the model's knowledge"
learning_goal: "Precise mechanics of temperature — the formula T=0⇒argmax, P^(1/T) when T>0 — and why T matters even though the token ranking doesn't change; top-p/top-k as a second tier"
learning_outcomes: [LO4, LO7]
chapter_ref: "§4.2 (chapter-part2.md) [for-slide-s27]"
visual_brief: "Top — an explicit formula in an Ocean rounded box: 'T=0 ⇒ choice = argmax P(token)'; 'T>0 ⇒ sampling from a P^(1/T)-shaped distribution (logits divided by T before softmax)'. 3 versions of the distribution from s26 side-by-side below: T→0 — a single bar 'apple' 1.0 (argmax), T=1 — the original distribution, T=1.5 — smoothed, tail raised. Below that a thin line about top-p (cut by mass) and top-k (cut by count). Separate callout 'why T matters even though token order doesn't change': the choice isn't 'top-1' but a random draw PROPORTIONAL to the probabilities; T changes the probabilities themselves (sharpens/flattens), not their ranking. Badge 'live demo: one prompt, T=0 ×10 and T=1.5 ×10'. Gold on the T=1 panel (the default)."
interaction: live_comparison
---

# Visible content

## Title bar
"Temperature is a divisor on the logits: it changes the sharpness of the choice, not the knowledge"

## Body
[Formula — top block, Ocean rounded box]

**T = 0** ⇒ choice = **argmax P(token)** — take the most likely one, no sampling
**T > 0** ⇒ sampling from a **P^(1/T)**-shaped distribution — logits are divided by T before softmax

[3 distributions side-by-side, Ocean rounded boxes]

**T → 0** (argmax)
[A single bar: apple ≈ 1.0]
Picks the most likely token. Nearly identical answers — we'll unpack that "nearly" on the next slide.

**T = 1** (default) *(gold)*
[The original distribution]
Sampling proportional to the model's probabilities. Natural variability.

**T = 1.5** (smoothing)
[Distribution flattened, tail raised]
Rare tokens get a real chance — anywhere from lucky finds to incoherence.

[Separate callout — why T matters even though the order doesn't change]
**Token ranking by probability is the same at any T. But the choice isn't "take the top-1" — it's a random draw proportional to probabilities — and T reshapes the probabilities themselves: sharpening them (T<1) or flattening them (T>1).**

[Second-tier line]
**top-p** — cuts the tail by probability mass · **top-k** — cuts by number of candidates. The main knob is temperature; these two are fine-tuning.

[Live-comparison badge]
**Live run:** the same prompt — 10 times at T=0 and 10 times at T=1.5.

[Action line]
**What to do:** set T for the task — 0–0.3 for code and classification, 0.7+ for text generation (details in the table on the next slide).

## Speaker notes

You already know these knobs — let's sharpen the mechanics into an exact formula. At T=0, the choice is argmax P(token): deterministically take the token with maximum probability, with no sampling at all. At T>0, the model samples from a distribution transformed by the rule P to the power of 1/T — technically this means the raw logits are divided by T before passing through softmax and turning into probabilities.

It's worth pausing on a point that often causes confusion: token ranking by probability doesn't change with temperature — the most probable token stays the most probable at any T. So why does temperature matter at all if the ranking is the same? The answer is that choosing a token isn't "take the top-1 off a list" — it's a random draw where the probability of picking each token is proportional to its probability in the distribution. And temperature changes those probabilities themselves, not their order: at T below one, the distribution sharpens — the leader gets even more probability mass, the outsiders lose their chances down to nearly zero; at T above one, the distribution flattens — the gap between the leader and the rest shrinks, and tokens that were previously almost impossible get a real chance of being picked. That's exactly why T=0 is the limiting case: the sharpening is taken to its extreme, and the leader's probability becomes exactly one — argmax.

Second tier: top-p cuts the tail by probability mass — we sample from the smallest set of the most probable tokens whose combined probability is at least p; top-k cuts by number of candidates. Practice hasn't changed: the main knob is temperature, these two are fine-tuning.

Now the live run: the same prompt — "come up with a name for a note-taking service" — ten times at zero and ten times at one-point-five. The first row gives nearly identical answers — "Notely," "Notely," "Notely," with maybe an ending changing here and there; the word "nearly" carries more weight here than it seems, and the next slide is devoted to it. The second row spreads from lucky finds to gibberish: "MindStream," "dawn-fog notebook," "breath-of-numbers pad" (examples are illustrative — you'll see your own spread of variety in a minute).

The value of this experiment, if you run it yourself, isn't confirming the theory — it's calibrating your hand: you'll see what the tail of the distribution looks like for your specific task and at what temperature it starts leaking into the answers. And the reverse exercise: if your prompts in production run at the provider's default temperature — find out what that default actually is; defaults differ across providers and change over time, and a deliberate choice here costs one line of code.
