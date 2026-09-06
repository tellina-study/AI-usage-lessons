---
id: s28
type: case_study
section: "Section 4. Sampling and Generation"
duration_min: 3.5
assertion: "T=0 does not give determinism: on stock vLLM — 80 unique answers out of 1000 identical requests"
learning_goal: "The mechanism of non-determinism at T=0 (batch invariance, not 'floating point in general'); the cost of the fix and consequences for testing"
learning_outcomes: [LO4, LO6]
chapter_ref: "§4.3 (chapter-part2.md) [for-slide-s28]"
visual_brief: "Left 45% — a large exhibit number in an Ocean rounded box: '80 / 1000' (gold, 96pt) with the caption 'unique answers at T=0, stock vLLM (Thinking Machines Lab, 2025)'. Right 55% — a diagram of the cause: three request tiles from different users merge into a 'server batch' of variable size → tile 'different summation order' → 'the least significant bit decides the token choice' → autoregression spreads the divergence. Bottom, two tiles: 'A fix exists: 1000/1000 bit-for-bit' and 'Cost: ~35% of throughput → off by default'. Gold callout about testing."
---

# Visible content

## Title bar
"T=0 does not give determinism: 80 unique answers out of 1000"

## Body
[Left — exhibit, Ocean rounded box]

**80 / 1000**
unique response variants to an identical request at T=0 — stock vLLM (an open inference server; Thinking Machines Lab, September 2025)

[Right — mechanism, chain of tiles]

**The cause isn't "floating point in general" — it's a lack of batch invariance in the kernels:**
1. The server groups concurrent requests from **different users** into batches
2. Batch size depends on other users' load in that exact millisecond
3. Different batch size → **different summation order** → different least-significant bits
4. Two close candidates for argmax → the least-significant bit decides the token choice → autoregression spreads the divergence through the whole answer

[Two tiles at the bottom]
- **A fix exists:** batch-invariant kernels — 1000/1000 bit-for-bit identical
- **Cost:** ~35% of throughput → providers don't turn it on; OpenAI's `seed` is officially "mostly deterministic," not fully

[Gold callout]
**You cannot get a guaranteed-deterministic answer from a cloud LLM today — build your processes accounting for that. Consequence: don't compare answers bit-for-bit, compare them semantically or structurally.**

## Speaker notes

This is the trickiest of the six claims, because it's almost true, and tests and pipelines get built on it. You set temperature to zero, expecting: same request, same answer. A check on real infrastructure: stock vLLM, a thousand runs of an identical request — eighty unique answer variants. Zero really does make the argmax choice deterministic — but the distribution itself, the one argmax is taken from, turns out to be slightly different from run to run.

The cause runs deeper than the common "floating point on the GPU" explanation. The main culprit is a lack of batch invariance in the compute kernels. A provider's server dynamically groups concurrent requests from different users into batches; batch size depends on the load at that exact millisecond; and many kernels use a different summation order depending on batch size. Floating-point addition is non-associative — order changes the least-significant bits — and when two argmax candidates are close, the least-significant bit decides the token choice; from there, autoregression spreads the divergence through the entire answer. Your "deterministic" request is non-deterministic because you're sharing the server with other users, and their traffic changes your batch size.

The most instructive part: the problem is solvable — and the fix has been rejected on economic grounds. The same authors wrote batch-invariant kernels: a thousand out of a thousand runs, bit-for-bit identical. The cost is roughly 35 percent of throughput, which is why providers don't turn this mode on by default; hence the status of OpenAI's seed parameter — officially "mostly deterministic," with no guarantees.

The main takeaway is worded this way, and the order matters here: getting a guaranteed-deterministic answer from a cloud LLM is not possible today — this isn't a temporary bug, it's a consequence of providers' economic choice, and you need to design your processes with that fact in mind, not in the hope that "the next version will fix it." From this, as a consequence rather than the main thesis: don't build tests on bit-for-bit comparison of answers — compare them semantically or structurally; pin down reproducibility with a dataset and a metric. And if strict determinism is genuinely required — for an audit, for regulatory reasons — that's a separate infrastructure requirement with a price tag of a third of your throughput, budgeted for from the start.
