---
id: s-rag-cases
type: assertion_visual
section: "Section 2. RAG"
assertion: "«RAG» doesn't exist in a vacuum — there is RAG for support, for code, for contracts; retrieval design follows from the nature of the data"
learning_goal: "Typical RAG archetypes (owner #9): 5 real tasks with a retrieval design, a failure, and a baseline"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.12 [for-slide-rag-cases-intro] · [for-slide-rag-case-support] · [for-slide-rag-case-docs] · [for-slide-rag-case-code] · [for-slide-rag-case-legal] · [for-slide-rag-case-enterprise]"
interaction: none
---

# Visible content

## Title bar
«RAG doesn't exist in a vacuum — there is RAG for a task»

## Body
[5 archetypes]
1. Support / internal knowledge base (kapa.ai, Stripe) — hybrid + rerank + delta updates; failure: «backoff» ≈ «dead-letter» → wrong policy.
2. Q&A over documentation (Vercel AI SDK) — sections + cite-or-refuse + eval in CI; failure: a stale API version.
3. Code search (Cursor, Sourcegraph Cody) — chunk per function; Cody REMOVED embeddings, went back to lexical search.
4. Legal (LexisNexis, Westlaw) — hybrid + filters; 17–33% hallucinations despite «0%».
5. Enterprise: docs + tables (Glean, eSapiens) — router numeric→Text-to-SQL.

[Gold]
Two cases are direct «RAG was the wrong tool». Retrieval design follows from the nature of the data.

## Speaker notes

Up to this point we've treated RAG as a mechanism: the principle, when it fits, how it breaks, what a correct build is made of. Now let's unfold that into five real archetypes, because «RAG» doesn't exist in a vacuum — there's «RAG for support», «RAG for code», «RAG for contracts», and their retrieval design is different. One shared quantitative anchor for all of them: according to practitioners, naive dense RAG misses retrieval[1] on the order of forty percent of the time, and three techniques — context attached to the chunk, hybrid search, reranking — close most of that gap.

The support and internal-knowledge-base case: kapa.ai runs documentation assistants for Docker, Reddit, and OpenAI; Stripe has an assistant built on top of its documentation. A typical failure: the embeddings decide that «exponential backoff» and «dead-letter queue» are semantically close, and the assistant confidently states the wrong retry policy — hybrid search saves it because BM25 catches the exact term that dense search blurred. The documentation case: the Vercel AI SDK docs-copilot builds an «answer with sources or refuse» contract and keeps an eval set right in CI, so a retrieval regression after a docs update doesn't slip into production unnoticed.

The code case is the most instructive. Cursor indexes the codebase with embeddings, but Sourcegraph Cody did the opposite on Enterprise: it removed embeddings and went back to classic lexical[3] and structural search. The reasons — code was leaving the perimeter into a third-party API (a security risk), vectors have to be stored and kept up to date, and at a hundred thousand repositories vector search is expensive and doesn't scale. Classic search gave equal or better quality, cheaper and safer. This is a direct example of «RAG-as-dense-vectors was the wrong tool»: for code and exact identifiers, classic search often beats dense RAG.

The legal case shows the high-stakes boundary: a preregistered Stanford study of commercial legal-AI tools (LexisNexis, Westlaw — all built on RAG) found seventeen to thirty-three percent hallucinations[2], despite «hallucination-free» marketing. RAG reduces but doesn't zero out hallucinations — you can't deploy it without citation verification and a human in the loop. And the enterprise case with mixed data: the question «total Q3 expenses» can't be closed with vector search over a table — that's SQL aggregation, so you need a «structured vs. text» router. The general takeaway: retrieval design follows from the nature of the data, it isn't copied from someone else's blog post.

Sources:
[1] Barnett et al. 2024 — Seven Failure Points (RAG archetypes) — «returned something ≠ returned the right thing»: failure points across typical RAG tasks. https://arxiv.org/abs/2401.05856
[2] Stanford HAI/RegLab — Legal-AI hallucinates 17–33% (Lexis/Westlaw) — commercial legal-AI tools built on RAG hallucinate on 1 in 6 or more queries, despite «0%» marketing. https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries [VFY-day-of]
[3] Sourcegraph Cody — context without embeddings (classic search) — Cody on Enterprise removed embeddings → lexical/structural search is cheaper, safer, more scalable. https://sourcegraph.com/docs/cody/core-concepts/context [VFY-day-of]
