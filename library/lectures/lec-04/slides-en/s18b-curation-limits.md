---
id: s18b
type: assertion_visual
section: "Section 3. Implementation — discipline and harness"
assertion: "Each of the four context levels has its own limit: stale instructions are worse than none, compaction loses decisions silently and JIT will not ask about the unknown, operational history ages more quietly than instructions, memory entrenches a wrong conclusion — the risk does not disappear, it is traded for another"
duration_min: 3
learning_goal: "The honest limit of EVERY context level, in parallel with the previous slide — not an optional caveat but a condition of applying the practice correctly"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.2 [for-slide-s17], §3.3d (entrenchment)"
references: [anthropic-context-engineering, agents-md]
in_bucket: true
verify_day_of: false
visual_brief: >
  assertion_visual: 4 equal cards in a row (Ocean rounded box), strictly parallel to the four levels of the
  previous slide — same order, same colors (mid/teal alternating), each headed "LEVEL N · <name>".
  (1) icon shield-alert — a stale instruction file is worse than none: it prescribes a build command replaced
  long ago. (2) icon layers — compaction loses silently + JIT symmetrically will not ask about the unknown.
  (3) icon clock — an archive of write-ups ages more quietly than a single instruction file: the agent finds
  them by relevance, not by currency. (4) icon lock — memory entrenches a wrong belief when only the agent
  reads it. Below — a single conclusion line "curation trades one risk for another". Gold callout — the
  allocation rule: what cannot be lost silently is recorded at level 1.
interaction: none
---

# Visible content

## Title bar
Every level has its own limit — the risk changes, it does not disappear

## Body

[Card 1 — LEVEL 1 · INSTRUCTIONS] **A stale file is worse than no file**
A missing file the agent makes up for by asking; a stale one it trusts literally.
It prescribes a build command that was replaced long ago — the agent keeps running it and burns turns for nothing.

[Card 2 — LEVEL 2 · SESSION] **Compaction loses, JIT will not ask**
Summarization is lossy: "do not use library X" may not survive into the summary, and the agent will propose exactly that. No error is raised.
JIT is symmetric: what the agent does not know exists, it will never request.

[Card 3 — LEVEL 3 · HISTORY] **Ages more quietly than instructions**
There is one instruction file — it gets re-read along with the project. An archive of write-ups is dozens of documents.
The agent finds them by **relevance**, not by **currency**, and proposes a workaround for a problem closed long ago.

[Card 4 — LEVEL 4 · MEMORY] **Entrenches a wrong conclusion**
Memory accumulates on its own, so it cannot be proofread line by line like a file.
A wrong belief, once retained and read only by the agent itself, keeps being reproduced — it needs periodic checking from outside, not editing.

[Conclusion line]
No curation technique removes the risk — each one **trades one risk for another**. That is a limit of the technique itself, not a consequence of applying it carelessly.

[Gold callout]
Hence the allocation rule: a decision you cannot afford to lose silently is not trusted to level 2 — it is recorded at level 1, the only one that is not compressed between turns.

## Speaker notes

The previous slide broke the agent's context into four levels; each of them has its own honest limit, and those limits are different — which is why we walk through them in the same order.

Level one, the persistent instructions. The failure mode here is worse than simply not having a file: both the agent and the human trust an artifact that has stopped describing the real project. A missing file the agent compensates for by asking a question or scouting the repository; a stale one it follows literally. Concretely: the file prescribes a build command that was replaced long ago, the agent stubbornly runs it, gets an opaque environment error, and spends turns diagnosing a problem that does not exist — while it would have found the current command by searching in seconds.

Level two, the context of a single session. Compaction is summarization, and summarization is lossy by definition: if the conversation explicitly decided not to use library X because of a licensing conflict, and the model judged that detail secondary while compressing, the decision disappears silently. No error is raised — the agent simply proposes, a few turns later, exactly what was just rejected. JIT retrieval suffers symmetrically from the other side of the same trade-off: the agent pulls in what it thought to ask for, and what it does not know exists it will never request.

Level three, the operational history. There is one instruction file, and it gets re-read together with the project at every review; an archive of write-ups is dozens of separate documents, and it ages unnoticed. The agent finds a document by relevance to the query rather than by currency, and proposes a workaround for a problem that was closed six months ago.

Level four, memory. It accumulates on its own, so it cannot be proofread line by line. A wrong belief, once retained and read only by the agent itself, is reproduced in every following session — what it needs is periodic checking from outside, not line-by-line editing. Hence the allocation rule: what cannot be lost silently is recorded at level one.
