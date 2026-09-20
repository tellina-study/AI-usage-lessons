---
id: s-rag-chunk3
type: assertion_visual
section: "Section 2. RAG"
assertion: "The silent chunking failure: naive splitting flattens a table into a «bare row of numbers» with no headers — the system doesn't crash, it just quietly answers wrong"
learning_goal: "Deepening chunking (owner #7): a worked example with a table (failure → fix), anaphora, pipeline interactions"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.10 [for-slide-rag-chunk-worked] · [for-slide-rag-chunk-fail]"
interaction: none
---

# Visible content

## Title bar
«Silent chunking failure: a bare row of numbers»

## Body
[Worked example — before]
300 PDF manuals with spec tables. A naive RecursiveCharacter splitter, 512 tokens, flattens the table and cuts on a raw byte → chunk «12 / 480 / 8.5 / 34» with no «Model / Voltage / Current / Torque» headers. The system doesn't crash — the answer is just wrong.

[Worked example — after]
Table-aware: the table becomes its own chunk; over the limit → split by row with repeated headers → «Model X-500 | Voltage 480 | Current 8.5 | Torque 34». Each row is self-contained. The win came not from a "smart" split but from respecting structure.

[Two more failures + the pipeline]
Anaphora ("it", "this policy") loses its antecedent; changing embedders means re-chunking the whole corpus; evaluating chunking is sensitive to k.

## Speaker notes

The previous slide said: don't cargo-cult someone else's recipe, measure on your own data. This slide shows exactly how chunking breaks — and why it's the most treacherous kind of RAG failure: it's silent. Take a specific corpus: three hundred PDF manuals for industrial equipment — explanatory text plus spec tables ("Model / Voltage / Current / Tightening torque") plus safety warnings. A typical question: "what's the tightening torque for model X-500?" — and the answer lives in a table cell.

What would a naive engineer pick: RecursiveCharacterTextSplitter, five hundred twelve tokens, overlap fifty — that works for prose. But the parser detects the table and flattens it into a stream, and the character splitter cuts it at an arbitrary byte on the five-hundred-twelve-token boundary. The result: the first piece has the column headers and the first rows, and every piece after that is rows of numbers with no headers: "twelve, four hundred eighty, eight point five, thirty-four" with no labels. Why this is a silent failure: the system doesn't crash — the embedding gets computed, retrieval finds the chunk with the number thirty-four, an answer gets generated. It's just wrong: the model has no way to know that thirty-four is the tightening torque for X-500, not the current for X-700. The dashboard says "retrieval is working"; in production, it's a workplace injury.

The right fix isn't a "smart" semantic split, it's the mundane act of respecting structure[1]: table-aware splitting, where the table becomes its own chunk, and if it's over the limit, it's split by row with the headers repeated in every piece so each row is self-contained. Add parent-document for the text so warnings don't get separated from the procedure, plus metadata for filtering by model and version.

And three things you can't afford to forget. Anaphora: "it", "this city", "this policy" lose their antecedent when a cut lands between them — fixed with parent-document or contextual prepending. Changing the embedding model means re-chunking the entire corpus[2], not editing a line in a config file. And evaluating chunking itself is sensitive to k: recall@k can lie (ninety-two percent recall at fifty-four percent correct answers), which is why teams measure end-to-end too. The check for a silent failure is simple: generate twenty to thirty questions whose answers live in tables and manually confirm that the top-k results bring back a chunk with headers, not a bare row of numbers.

Sources:
[1] Anthropic — Contextual Retrieval (tables are a silent retrieval failure) — flattening a table breaks row/column relationships without an error — fix with table-aware splitting. https://www.anthropic.com/engineering/contextual-retrieval
[2] firecrawl — Chunking Strategies (re-chunk when changing embedders, k-sensitivity) — chunk size is tied to the model's context window; evaluate chunking through recall@k AND end-to-end. https://www.firecrawl.dev/blog/best-chunking-strategies-rag [VFY-day-of]
