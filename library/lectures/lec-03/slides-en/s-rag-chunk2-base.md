---
id: s-rag-chunk2
type: case_study
section: "Section 2. RAG"
duration_min: 2.5
assertion: "Studies on the effect of chunking openly disagree: recursive-512 69% versus semantic 54%; don't cargo-cult semantic; the silent retrieval failure is tables"
learning_goal: "How to choose a chunking strategy + the silent failure of tables (§2.10)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.10 [for-slide-rag-chunk-studies]"
subtype: meme_forward
new_in_v4: "#196 WAVE 2 — RAG deepening (failure)"
---

# Visible content

## Title
«Don't cargo-cult semantic chunking.»

## Speaker notes

Here is the most instructive slide for judgment: studies on the effect of chunking openly disagree, and that disagreement is itself a lesson. Take three measurements, each with a baseline. A February 2026 benchmark compared seven strategies on fifty scientific papers: recursive chunking at 512 tokens came out first at 69 percent accuracy, while semantic chunking gave only 54 — and produced tiny fragments of about forty-three tokens each. In an MDPI clinical study from November 2025, adaptive and topic-boundary chunking gave 87 percent against 13 for fixed-size — a huge gap, but that's a narrow clinical domain. And NAACL 2025 Findings states outright that the computational cost of semantic chunking isn't justified by a stable gain: fixed chunks of two hundred words matched or beat semantic.

Read it this way: claims that "smart chunking wins" are domain-specific and inconsistent. On many corpora, plain recursive fixed-size is a strong baseline, and semantic chunking loses on both quality and cost. The engineering takeaway, verbatim: don't cargo-cult semantic chunking. Recursive fixed-size is cheap and strong as a starting point; add complexity only for a gap you've measured on your own corpus.

And this subsection's named failure, right on point for our failure thread: tables. They are the single most common cause of silent retrieval failures. Flattening a table into text destroys the row-column relationships — the model can't recover them, and this doesn't fail with an error, it silently corrupts the answer. The fix is to treat tables as structured objects rather than flattening them into a string. The meta-lesson from the strongest teams: the ones who went from months stuck on a RAG use case to a reliable deployment stopped fiddling with chunk size and started managing the knowledge layer — document quality, table handling, freshness, and metadata.

Sources:
[1] firecrawl — chunking benchmark (recursive-512 69% vs semantic 54%) — 7 strategies on 50 papers; semantic produced ~43-token fragments. https://www.firecrawl.dev/blog/best-chunking-strategies-rag [VFY-day-of]
[2] firecrawl — chunking eval (recall@k in isolation can mislead) — recall@k 91.9% at 54% end-to-end accuracy — evaluate chunking through end-to-end too. https://www.firecrawl.dev/blog/best-chunking-strategies-rag [VFY-day-of]
