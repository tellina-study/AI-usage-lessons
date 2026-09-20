# -*- coding: utf-8 -*-
"""Spec for Seminar 3 — three model mechanisms in system design (English track).

English counterpart of spec_sem03.py, slide for slide: same 43 entries, same
order, same `kind` per entry, same renderer (build_cases_deck.py). It is kept as
a separate file rather than a language switch inside spec_sem03.py because the
Russian spec is the source of truth and stays untouched by translation work;
a bilingual spec would double every dict and make a RU-side edit silently
partial. `lang: "en"` on SEMINAR routes the output to deck.en.yaml / slides-en/
/ rendered/sem-03-en.pptx, per publish/publication-config.yaml naming.

The deck is derived from the six case files in library/seminars/sem-03/cases/,
and carries the fact-check corrections recorded in
library/seminars/sem-03/roast-findings.md — a translation must never revert one.

Structure of each case (mirrors the Russian spec):
  context      — the brief and its requirements only (case file section 1);
  concept      — how to compare / by what method (sections 2-3), not the options;
  variants     — the axes of choice as column headings (1.1, 3.1);
  complication — the twist or trap (section 5), kept out of the brief;
  scheme       — the solution pipeline (section 6.1);
  breakdown    — implementation logic, key components and commentary (6.2-6.4);
  resolution   — a real success/failure example (section 5) plus a short lesson.

Issue: #204 (EN track for seminars 1-3), part of bilingual production #172.
"""

S = []

# ===== Cover / map / section 1 =============================================
S += [
    {"kind": "cover", "kicker": "Seminar 3 · builds on Lecture 2",
     "title": "Three model mechanisms in system design",
     "sub": "Embeddings · attention · sampling and tokenization — six working tasks: build, fix, improve"},
    {"kind": "map", "title": "Three blocks, six tasks",
     "blocks": [
         ("Block 1 · Embeddings", "Choosing an embedding model for your corpus · deduplicating support tickets"),
         ("Block 2 · Attention", "Extracting \"who pays whom\" from contracts · a legal-team assistant and how to measure quality"),
         ("Block 3 · Sampling and tokenization", "Product card generator (description + specs) · tokenization breaks counting and validation"),
     ]},
    {"kind": "divider", "number": "1", "block": "Block 1", "title": "Embeddings: comparing and grouping by meaning",
     "tag": "Building embedding search · improving support"},
]

# ==========================================================================
# Case 1.1 — Choosing an embedding model for your corpus
# Source: cases/case-1.1.md
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 1.1 · Building embedding search",
     "title": "Which embedding model to use for your corpus",
     "lead": "We're building semantic search over an internal knowledge base: an employee asks in plain words, the system finds the document by meaning. The first decision: which model encodes text into vectors.",
     "inputs": [
         ("Corpus", "in-house, Russian-language, with domain-specific terms"),
         ("Output", "return relevant documents for a query"),
         ("Latency", "results within ~300 milliseconds"),
         ("Switching models is costly", "change model → reindex the whole corpus"),
         ("No labeled data", "no table of \"for query X, Y and Z are relevant\" exists"),
         ("Out of scope", "the selection criterion, model list, dimensionality — these are decisions, not givens"),
     ],
     "question": "What criterion should we use to choose a model — and how do we test candidates on OUR OWN data?",
     "notes": "The slide only sets up the problem: your own Russian domain, a latency budget of ~300ms, expensive model switching (vectors from different models aren't comparable, so switching means reindexing the whole corpus), and no ready-made relevance labels. The selection criterion and the model list are deliberately left out of scope — students propose those themselves. This is a class of task where the component is expensive to change later. Two obvious moves come to mind here: pick the MTEB benchmark leader and stop thinking (fast, but the leader averages across dozens of languages), or build a mini-eval on your own query-to-document pairs and measure the candidates (an hour of work, but numbers about your own corpus). The beginner's trap is picking the top of the leaderboard and discovering poor recall on your own queries a month later. Likely question: \"can't we just take the biggest model?\" — higher dimensionality costs more in storage and latency, and there may be no quality gain on your domain; that's exactly what the mini-eval shows. The following slides cover how to build the eval, the comparison axes, and the candidate table."},
    {"kind": "concept", "kicker": "Method · Mini-eval on your own data",
     "title": "How to choose: eval first, everything else second",
     "definition": "Search quality is a property of the pair \"model + your corpus + your queries,\" not of the model alone. It can only be measured on your own data: how well the model's vectors bring YOUR queries close to YOUR relevant documents.",
     "steps": [
         "Pick 3-4 candidates from different classes via MTEB/ruMTEB (the embedding-model leaderboard; ru- is the Russian version) — as a shortlist, not as an answer",
         "Build a mini-eval: 50-100 \"query → relevant document\" pairs from your corpus, plus traps",
         "Run each candidate on the SAME set → recall@k and MRR under identical conditions",
         "Weigh quality against vector dimensionality: 384 vs 1024 → storage and search latency",
         "Choose along the \"quality on my data / cost\" axis, and pin the model version in the config",
     ],
     "scheme": ["Candidates (from leaderboard)", "Mini-eval (your pairs)", "recall@k · MRR", "Choice: quality / cost"],
     "note": "recall@k is the share of queries where the right document lands in the top-k. MRR (mean reciprocal rank) shows how high it ranks. Eval set size is a function of the task (query diversity, cost of error), not a round \"200\" — even 30 honest pairs beat choosing blind.",
     "notes": "This is the comparison method, not the variants themselves yet. Two metrics cover the choice: recall@k (did the right document show up among the first k) and MRR (how high it ranks — first place 1.0, second 0.5, third 0.33). You need both together: recall@10=1.0 for two models can hide that one puts the right answer first and the other ninth. k comes from the product's architecture: users scan a first page of 10 links → recall@10; RAG puts 5 chunks into context → recall@5. Measuring recall@100 is self-deception — a user will never see a document ranked 87th. Two silent bugs in eval pseudocode: query/document modes (e5/bge-m3 use different prefixes for query vs. document — encode everything the same way and you lose quality) and a mismatch between the distance metric/normalization and how the model was trained. Likely question: \"is 30 pairs enough eval data?\" — yes, 30 honest pairs give a signal; the sign that it's too few is results jumping around as you add more pairs."},
    {"kind": "variants", "kicker": "Case 1.1 · Candidate comparison axes",
     "title": "Three axes of choice — each checked by the same eval",
     "lead": "The axes don't reduce to one number: quality on your data, vector dimensionality, cost, and latency. Different model classes offer different trade-offs on each axis.",
     "cols": [
         {"head": "Multilingual / monolingual", "sample": "Multilingual — broad coverage; Russian-centric — richer Russian, narrower coverage.",
          "use": ["Multilingual: e5, bge-m3 — average quality across dozens of languages", "Russian-centric: RoSBERTa, GigaEmbeddings — candidates for a Russian domain", "Tested by: recall@k on a Russian eval"]},
         {"head": "Domain-specific / general", "sample": "Domain-specific/fine-tuned for legal/med/fintech vs. a solid general model out of the box.",
          "use": ["Domain-specific may score higher on its own domain", "General is sometimes good enough and cheaper", "Tested by: eval; \"domain-specific = better\" is a hypothesis"]},
         {"head": "Dimensionality", "sample": "Compact 384-768 vs. large 1536-3072 (MTEB flag, bigger vector).",
          "use": ["Large: higher average score, costlier storage and search", "Compact: cheaper, closer to the 300ms budget", "Tested by: equal recall → pick the smaller one"]},
     ],
     "note": "Don't compare models by description — compare them by numbers on your own corpus. Larger dimensionality linearly increases vector-DB size and search time across the WHOLE index: if a 768-dim model gets the same recall@10, there's no reason to pay for 1536. Vector truncation (Matryoshka/MRL) is checked with the same measurement.",
     "notes": "The three variant axes from the case breakdown are laid out as column headers. \"Multilingual/monolingual\" axis: a multilingual model is trained on dozens of languages and its Russian quality is an average; a Russian-centric model has seen more Russian and often wins on the domain — but that's checked by recall@k on a Russian eval, not by description. \"Domain-specific/general\" axis: domain-specific may be more precise but needs labeled data and fine-tuning; there are documented cases where a general model beat a specialized one, so \"domain-specific = better\" is just as untested a hypothesis as \"leaderboard = better.\" \"Dimensionality\" axis is a direct quality-vs-cost trade-off: a 1536 vector takes twice the space of a 768 one and is linearly slower to search across the whole index. How to lock in the choice: a table of model × recall@k × MRR × dimensionality × latency, with the decision made on the \"quality on my data / cost\" column. Question: \"is an embedding model from the same vendor as the LLM more compatible?\" — \"compatibility\" isn't a real category here: the LLM never sees the search embeddings at all, so pick the best search model for your language regardless of the generator."},
    {"kind": "complication", "kicker": "Case 1.1 · In practice",
     "title": "The benchmark leader slips exactly on the Russian domain",
     "body": "In a documented production system for searching legal contracts, the top-3 MTEB leaderboard models placed 5th, 7th, and 2nd on the in-domain eval set: the model ranked first on the general benchmark came in fifth on the real corpus — beaten by less \"decorated\" ones.",
     "effect": "The benchmark's average score is averaged across dozens of languages and domains. \"Best on MTEB\" and \"best on your data\" are different models — quality isn't a single axis.",
     "notes": "This isn't \"the benchmark lies,\" it's a property of the aggregate: MTEB averages retrieval, classification, and clustering across many languages, and a high average score can rest on languages you don't have. A separate axis is robustness to dimensionality truncation (Matryoshka/MRL): the leader on full-size retrieval can end up last after vector truncation, and vice versa; a 2026 paper showed embeddings stay robust to truncation even without dedicated MRL training, as long as the reduction doesn't exceed ~70-80%. There's also a reverse nuance (the chemistry domain, ChEmbed): a domain-specific model WINS on retrieval (nDCG@10 0.82→0.91), but the general model stays competitive on non-retrieval tasks — hence the rule \"measure against your main function,\" not \"domain-specific always wins.\" How to detect a mismatch with the leaderboard: you already have the mini-eval — compare candidates' recall@k on your own pairs, the gap shows up immediately. Hence the rule: the leaderboard supplies the candidate list, the eval makes the decision. Likely question: \"what if there's no good off-the-shelf model for my domain at all?\" — then fine-tuning an embedder on your own pairs, or a hybrid with full-text BM25, becomes a candidate, but that's the next step after the eval has shown the ceiling of the ready-made options."},
    {"kind": "scheme", "kicker": "Case 1.1 · Solution",
     "title": "Selection pipeline: leaderboard → eval → metrics → choice",
     "lead": "The leaderboard shortlists candidates; from there, measurement on your own data makes the decision.",
     "nodes": ["3-4 candidate classes", "Mini-eval + traps", "recall@k · MRR + dimensionality/latency", "Choice + version pinning"],
     "bullets": [
         "MTEB/ruMTEB leaderboard is only a source of candidates, not the answer",
         "Every candidate is run on the SAME set under identical conditions",
         "Choice is made on the \"quality on my data / cost\" axis; the winner's version is pinned — switching means reindexing",
     ],
     "caption": "An hour of eval versus weeks of living with a bad, expensively-reindexed index.",
     "notes": "The diagram is from section 6.1 of the case file. The logic runs in three steps. The leaderboard is used only to shortlist 3-4 candidate models from different classes — after that it plays no further role in the decision. A small, honest eval set is built from real \"query → needed document\" pairs, with deliberate traps (antonym pairs like \"on/off,\" different product versions — these expose the method's limits). Every candidate is run on the same set under identical conditions, producing comparable recall@k, MRR, dimensionality, and latency. Latency is measured at real index size and by percentile (p95/p99), not by average — users feel the worst cases. The choice is made on the \"quality on my own data vs. cost\" axis, and the winner's version is pinned in the config, because a silent vendor update to the model changes its vectors, and those aren't comparable to the old index. Likely question: \"we switched the chat model in RAG — do we need to reindex?\" — no, the index lives in the embedding model's coordinate space and doesn't depend on the generator; reindexing is only needed when the embedding model itself changes."},
    {"kind": "breakdown", "kicker": "Case 1.1 · Breakdown",
     "logic": "The leaderboard shortlists 3-4 candidates from different classes, then steps aside. On one shared mini-eval of real pairs with traps, every candidate is measured on recall@k, MRR, dimensionality, and latency under identical conditions. The choice is made on the \"quality on my data / cost\" axis; the winner's version is pinned in the config, because switching models means reindexing the whole corpus.",
     "components": [
         ("Candidate list", "3-4 models from different classes via MTEB/ruMTEB, used as a shortlist; BM25 can be added as a non-AI baseline."),
         ("Mini-eval set", "A table of \"query | document id | type (regular/trap),\" 50-100 rows. The sole arbiter of quality."),
         ("Encoder", "The text-to-vector model; query/document modes and metric/normalization matching the model's training both matter."),
         ("Nearest-neighbor index", "pgvector / Qdrant / FAISS — stores the corpus vectors, quickly returns the top-k."),
         ("Pinned config", "A locked model version + metric + dimensionality — protection against a silent update."),
     ],
     "comments": [
         "The vector reflects the statistics of what the model saw during training → \"search quality\" is inseparable from the pair \"model + your data.\"",
         "similarity ≠ relevance: high similarity for pairs like \"turn on/turn off\" is a limit of the method itself; a reranker/hybrid removes it, not a model swap.",
         "Pitfalls: metric/normalization mismatched with training; encoding query/document the same way; choosing by leaderboard without an eval; \"I'll just take a bigger one to be safe.\"",
     ],
     "notes": "The breakdown comes from sections 6.2-6.4 of the case file. Central takeaway: a vector is a statistical reflection of what the model saw during training, so search quality is inseparable from the pair \"model + your data.\" A model that has seen a lot of your language and domain will separate documents in the space better than one that has seen little of them — regardless of leaderboard rank. Separately, spell out a limit of the embedding method itself that no model choice removes: high cosine similarity means \"about the same thing,\" not \"with the same meaning\" — the pair \"how to enable SSL\" / \"how to disable SSL\" gets very high similarity because negation barely shifts the vector. What fixes this isn't \"a better model\" but a reranker, a hybrid with full-text search, or metadata filters; traps in the eval exist so you see the limit before your users do. Main pitfalls: a mismatch between the distance metric and how the model was trained (a silent quality drop with a perfectly fine model), encoding the query and document the same way, choosing by leaderboard without an eval, paying for dimensionality with no quality gain. Likely question: \"can we skip embeddings and use old-school full-text search?\" — for Russian full-document search, BM25 remains a strong baseline; add it as a candidate in the eval, and if it keeps up, you save on vector infrastructure."},
    {"kind": "resolution", "kicker": "Case 1.1",
     "solution": "Choosing an embedding model = a mini-eval on your own pairs plus a deliberate dimensionality trade-off; the leaderboard only supplies candidates, and the version gets pinned in the config.",
     "howto": [
         "Gather 50-100 \"query → relevant document\" pairs from your corpus, plus \"on/off\" traps — that's your eval",
         "Run candidates (multilingual, Russian-centric, large, BM25) on the SAME set → recall@k and MRR",
         "Weigh quality against dimensionality: if 768 gives the same recall as 1536, pick 768",
         "Check that the metric (cosine/dot) and normalization match how the model was trained; pin the version",
     ],
     "example": {"kind": "pos", "title": "An hour of eval versus weeks with a bad index",
                 "text": "Run the final check on a sample of your own documents and queries: an hour of work versus weeks with a bad index. The MTEB leader ≠ the leader on your domain."},
     "notes": "A step-by-step how-to from the breakdown and Q&A in the case file. (1) Eval set: write down real queries and, for each, the document that must be found; 50-100 pairs give a signal, and be sure to add traps (antonyms, different versions). (2) Run: encode the corpus and queries with each candidate, compute recall@k and MRR under identical conditions. (3) Dimensionality: OpenAI has a dimensions parameter, and Matryoshka models let you truncate the vector in a controlled way — check whether you lose recall on truncation. (4) Pitfalls: the distance metric and normalization must match how the model was trained — if the model was trained on cosine with L2 normalization and you search with dot product without it, quality drops with no \"bad model\" involved. A simple metric-consistency test: encode two synonymous texts and two unrelated ones — if the synonyms are noticeably closer, the metric is fine; if \"everything is close to everything,\" that's a mismatch. Likely question: \"how often should we revisit the model choice?\" — rarely, given the cost of reindexing, but keep the eval set alive: it catches degradation and tells you when a new model is actually worth rebuilding the index for."},
]

# ==========================================================================
# Case 1.2 — Deduplicating support tickets
# Source: cases/case-1.2.md
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 1.2 · Improving support",
     "title": "Collapsing duplicates in a stream of support tickets",
     "lead": "A payment service's support team receives a stream of tickets; the same problem arrives over and over, phrased dozens of different ways. We want to merge similar ones automatically.",
     "inputs": [
         ("Stream", "on the order of hundreds of tickets a day, continuous"),
         ("Duplicates", "one problem, different wording, often with no shared words"),
         ("Structure available", "card type, error code, service id"),
         ("Almost no labels", "no ready \"duplicate / not duplicate\" set for our stream exists"),
         ("Asymmetric cost of error", "merging different tickets hides and loses an incident"),
         ("Decision on arrival", "at intake, not batched once a day — otherwise an agent handles the duplicate by hand"),
     ],
     "question": "How do we find and merge duplicates — and where do we put a safeguard against false merges?",
     "notes": "The slide is a clean setup, WITHOUT the trap (that's in the complication). The key constraint is the asymmetric cost of error: missing a duplicate is reversible (an agent loses a few extra minutes), while merging different tickets is costly and often irreversible — one incident hides inside another ticket's card and drops out of triage. A lost incident is the task's main risk. This is a class of task: semantic clustering with a safeguard against false merges. Two obvious moves come to mind: a cosine-similarity threshold over embeddings (simple, but merges different incidents with similar text), or similarity plus a hard structural gate on distinguishing fields (more reliable). The beginner's trap is cranking the similarity threshold trying to separate close-but-different tickets, breaking recall on real duplicates in the process. Likely question: \"where does the threshold τ come from?\" — not \"by eye,\" but from labeled pairs via precision-recall, a separate step in the method. One more nuance: the stream is continuous, so dedup runs incrementally (a new ticket against recent clusters via a nearest-neighbor index), not by recomputing the whole similarity matrix — otherwise the cost grows quadratically."},
    {"kind": "concept", "kicker": "Method · Similarity + structural gate",
     "title": "How the dedup works — and why a structural gate",
     "definition": "Embedding-based dedup: we encode ticket text into a vector; cosine-close ones become candidates for the same cluster past a threshold τ. A structural gate is a set of hard fields that must match for a merge to be allowed.",
     "steps": [
         "Vectorize the ticket text → similar wording yields similar vectors, even with no shared words",
         "Cosine threshold τ: pairs with similarity > τ are merge candidates (\"does it look similar?\")",
         "Structural gate: merge ONLY if the keys match — card type, error code, service (\"is it the same thing?\")",
         "Keys don't match despite high similarity → don't merge, flag for manual review",
     ],
     "scheme": ["Ticket → vector", "Similarity > τ?", "Structural keys match?", "Merge / keep separate"],
     "note": "The threshold τ isn't a constant from an example — it's a separate tuning step: it's set from labeled pairs via a precision-recall curve. The size of the labeled set is a function of the task (stream frequency, cost of error, wording diversity), not a round \"200.\"",
     "notes": "This is the method, not yet the trap. The pipeline separates two questions: \"does it look similar?\" is answered by similarity (cheap, broad, error-prone on near-duplicates), and \"is it the same thing?\" is answered by a deterministic structural key (precise, safe). The order \"similarity → gate\" isn't arbitrary: start with structural keys and you'll lump together tickets that share an error code for different reasons; decide everything by similarity and you'll get false merges. The threshold τ is set from a precision-recall curve on labeled pairs: precision (share of correct merges) takes priority because of the asymmetric cost of error, recall (share of caught duplicates) is secondary. Because of measure concentration in high-dimensional space, the absolute cosine value is not very informative — τ is local: your model, your domain, your language, your τ; someone else's 0.90 doesn't transfer. The set size isn't set by a round number but by the number of trap pairs: if only 8 of 200 pairs are near-duplicates, the precision estimate rests on eight observations. Likely question: \"why not compare whole tickets with an LLM?\" — at hundreds of tickets a day that's thousands of calls, expensive and slow; embedding+gate delivers the same for pennies, leaving the LLM for rare disputed pairs."},
    {"kind": "complication", "kicker": "Case 1.2 · In practice",
     "title": "\"Visa\" and \"Mastercard\": close by vector, not the same thing",
     "body": "\"Payment fails with a Visa card\" and \"payment fails with a Mastercard card\" are near-identical by vector (cosine 0.95+): one word out of six differs. But these are different incidents — different acquiring, different gateways, different causes. A plain similarity threshold merges them and hides one incident inside the other.",
     "effect": "The embedding encodes the TOPIC and systematically loses the distinguishing detail. Raising τ doesn't help: any τ that separates Visa/Mastercard will also throw out a mass of real duplicates.",
     "notes": "This is exactly the trap we kept out of the setup. Why the similarity is high rather than \"the model being bad\": one word out of ten differs, almost the whole surrounding context is shared, so the vector barely shifts — a property of embeddings (they encode WHAT a text is about, not the distinguishing detail). The same mechanism makes the pair \"how to enable certificate checking\" / \"how to disable it\" almost indistinguishable. The same class of failure is documented by practitioners under the diagnosis \"pure text similarity produces confident false merges\"; under a merge-only semantics, such errors are irreversible — silent data corruption. How to detect it: keep trap pairs in your eval set (Visa/Mastercard, different amounts, different codes with identical text) and check whether the current τ merges them. The fix isn't cranking τ indefinitely (you'll break recall on real duplicates), it's adding a hard gate on the distinguishing field. There's a matching pitfall on the other side: an overly generic structural key (an oversimplified dedup_key) merges just as harmfully as a naive threshold — gate fields need the same domain-specific care as τ. Likely question: \"why not just raise τ instead of building a gate?\" — a high τ throws out real duplicates; the gate removes that trade-off, letting you keep τ lower with no false merges."},
    {"kind": "scheme", "kicker": "Case 1.2 · Solution",
     "title": "Hybrid \"similarity + structural keys\"",
     "lead": "Text decides \"does it look similar,\" deterministic fields decide \"is it the same thing.\" ANN is approximate nearest-neighbor search (quickly finds similar vectors).",
     "nodes": ["Ticket: text + fields", "Vector → ANN index", "Similarity > τ?", "Structural gate", "Merge / keep separate"],
     "bullets": [
         "Similarity gathers candidates cheaply and broadly (incrementally, via an ANN nearest-neighbor index)",
         "A structural gate on required fields filters out false merges precisely and safely",
         "High similarity + mismatched keys → don't merge, send to manual review, not silently into a new cluster",
     ],
     "caption": "Neither mechanism works alone: similarity merges near-duplicates, and keys without similarity miss duplicates.",
     "notes": "The diagram is from section 6.1 of the case file. A new ticket goes through normalization: structural fields (card type, error code, service) and cleaned text are extracted. The text is encoded into a vector, and an ANN index (approximate nearest neighbors) retrieves neighbors among recent tickets and cluster centroids. Neighbors with similarity above τ become candidates. A candidate goes through to a merge only if all required structural keys match; otherwise the ticket stays separate and, if similarity was high (a near-duplicate with a disputed key), it's flagged for manual review instead of silently disappearing. Trace it through the tickets: A and B describe the same problem in different words, both have error_code=51 → similarity 0.93, gate passes → merge. C is textually identical to B, but error_code=05 → similarity 0.97, gate fails → new cluster plus manual review; on similarity alone, C would have been merged and the incident with code 05 would have dissolved. Disputed pairs are also a source of new trap pairs to feed back into the set. Likely question: \"do we recompute everything for each ticket?\" — no, only against recent ones via the ANN index; a full recompute only happens when the model changes."},
    {"kind": "breakdown", "kicker": "Case 1.2 · Breakdown",
     "logic": "A new ticket is normalized into \"text + structural fields.\" The text is encoded into a vector, and an ANN index retrieves the nearest neighbors among recent tickets and cluster centroids; neighbors with similarity > τ are candidates. A candidate is merged only if all required keys match; otherwise it stays separate and, if similarity was high, goes to manual review. The threshold τ and the model version are pinned; at release, the false-merge rate and the missed-duplicate rate are measured.",
     "components": [
         ("Normalizer / field extractor", "A ticket from any channel → clean text + structural fields (regex/parser). The gate's reliability depends on it."),
         ("Embedding model", "Text → vector (chosen in Case 1.1); the metric and normalization must match its training."),
         ("ANN index", "FAISS / Qdrant / pgvector — incremental neighbors, no quadratic recompute."),
         ("Similarity threshold τ", "The only \"soft\" parameter; set from a precision-recall curve for a fixed target precision."),
         ("Structural gate", "A deterministic \"all keys match\" — carries the distinguishing detail that the vector loses."),
         ("Manual review queue", "Disputed near-duplicates go to a human — a safeguard against losing an incident and a source of new traps."),
     ],
     "comments": [
         "The embedding encodes \"what a text is about\" and loses the distinguishing detail when the lexical difference is small — cosine gives candidates, not identity.",
         "The main pitfall is trying to separate near-duplicates by raising τ: any τ high enough to do that will throw out real duplicates. Structure is what catches the distinguishing detail.",
         "Asymmetric cost of error → priority goes to precision, not balance; missed recall is recovered via the hybrid and manual review.",
     ],
     "notes": "The breakdown is from sections 6.2-6.4 of the case file. What the case illustrates about the mechanism: an embedding encodes WHAT a text is about, and systematically loses the distinguishing detail when the lexical difference is small — dedup is the cleanest demonstration of this, the \"Visa/Mastercard\" near-duplicates are indistinguishable by vector because the mechanism averages out context. Cosine similarity is a candidate signal, not an identity signal. The main pitfall is trying to separate near-duplicates by raising τ: any τ high enough to split near-identical but different incidents will also throw out a mass of real duplicates — you pay in recall for a problem the threshold can't solve in principle. Structure, not the threshold, is what catches the distinguishing detail. Where the limit sits: the structural gate is only as reliable as how reliably the fields were extracted and populated — empty or wrong fields make the gate useless; too generic a gate merges harmfully, too narrow a gate fails to collapse duplicates. Because of the asymmetric cost of error, the priority metric is precision on merges, not balance; the threshold is chosen for an acceptable level of false merges. Likely question: \"what happens when the embedding model changes?\" — new geometry, the old τ is void, the set must be remeasured, the corpus reindexed; keep the model version explicit in the config, since a silent update shifts the similarity distribution and quietly breaks the dedup."},
    {"kind": "resolution", "kicker": "Case 1.2",
     "solution": "Dedup = vector similarity plus required structural keys: text decides \"does it look similar,\" keys decide \"is it the same thing.\" Disputed cases go to manual review, not silently through.",
     "howto": [
         "Extract structural fields (card type, error code, service) — regex/parser from machine-readable sources",
         "Set τ as a separate step: label duplicate/not-duplicate pairs (with plenty of traps), build precision-recall, pick τ for the target precision",
         "Merge candidate = similarity > τ AND all required keys match",
         "Disputed cases (high similarity, mismatched keys) aren't merged — they go to manual review; at release we measure the false-merge rate",
     ],
     "example": {"kind": "neg", "title": "Confident false merges (near-duplicates)",
                 "text": "\"Pure text similarity produces confident false merges\": semantic similarity doesn't guarantee identity — the distinguishing detail is caught by the structural gate, not the threshold."},
     "notes": "In the example card: one team shipped a pure vector-clustering approach and got worse precision on the most important merges, so they rolled out a strict, deterministic gate instead. A step-by-step how-to from the breakdown and Q&A in the case file. A two-step pipeline: step 1, similarity gathers candidates (cheap, broad); step 2, deterministic key checking makes the final call (precise, safe). How to set τ by hand: label pairs as duplicate/not-duplicate with a high share of trap pairs; compute precision and recall across a grid of τ values; pick the τ where precision is sufficient for the cost of error. Set size is a function of the task: start with 30-50 honest pairs with traps, add more until the precision estimate for the chosen τ stops jumping around as pairs are added. Disputed pairs sent to manual review are almost ready-made labels: close the loop and let the verdicts feed back into the set. How to choose gate fields: candidates are fields that distinguish incidents (card type, error code, service), not ones that describe them (channel, app version); check on trap pairs that the field differs for traps and matches for real duplicates. Pitfalls: one τ for a heterogeneous stream is a poor compromise — compute τ per class. Likely question: \"can we get by with structural keys alone, no embeddings?\" — only if all distinguishing fields are populated and reliable; for user-submitted tickets the structure is partial, and \"one problem, different words\" is precisely about text."},
]

S += [{"kind": "divider", "number": "2", "block": "Block 2",
       "title": "Attention: what the model understands in text",
       "tag": "Building extraction · improving an assistant"}]

# ==========================================================================
# Case 2.1 -- Extracting "who pays whom" from contracts
# Source: cases/case-2.1.md
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 2.1 · Building extraction from contracts",
     "title": "Extract \"who pays whom, how much, and when\"",
     "lead": "The legal department has accumulated hundreds of contracts. As long as payment obligations live only in text, you can't use them as data. The task: turn free text into structured payment records.",
     "inputs": [
         ("Input", "contracts in different formats: docx, native PDF, scans"),
         ("Extracting", "payer, payee, amount, due date, condition"),
         ("Money fields are critical", "an error in the amount or direction = a wrong posting"),
         ("All by hand -- no", "hundreds of contracts, thousands of fields you can't check manually"),
         ("Auditability", "for every value, see exactly where in the text it came from"),
         ("Out of scope", "sufficiency criteria; where the real difficulty lies is the subject of the breakdown"),
     ],
     "question": "What should the pipeline look like -- and where should you place verification for critical fields?",
     "notes": "The slide is just the setup, WITHOUT mentioning the difficulty (coreference is saved for the complication slide). The key point: money fields are critical (an error in the amount, currency, or \"who pays whom\" direction = a wrong posting, potentially a payment to the wrong party), you can't check everything by hand, and you need auditability -- for every value, you should be able to see where in the text it came from (\"the model said so\" is not an argument for the accounting department). The temptation is to run everything through the model in a single call; that's exactly why it matters to understand in advance why the straightforward path is dangerous on money fields. The task class is structured-data extraction (information extraction) with verification. Two obvious moves: hand everything to the LLM with \"extract the fields\" (fast on typical cases, systematically wrong on ambiguous ones), or LLM extraction + span evidence + deterministic checks + a confidence gate (more reliable on money). The right engineering reflex isn't \"which model to use\" but \"which fields are critical, what can I verify programmatically, where do I have to leave a human in the loop.\" Another input trap: scans and mangled PDFs -- you need a text normalizer before extraction, otherwise the model confidently \"extracts\" nonsense from bad OCR; check input quality before blaming the model for its output."},
    {"kind": "concept", "kicker": "Method · Extraction with verification",
     "title": "Value + span evidence + confidence gate",
     "definition": "Attention reliably resolves \"who to whom\" as long as the text carries an unambiguous signal, and errs systematically when there is no unambiguous answer. So: bulk extraction goes to the model, critical fields go under non-model verification.",
     "steps": [
         "For EVERY field, the model returns a triple: value + evidence_span (a verbatim quote) + a confidence flag",
         "the span is checked as a substring of the source: not found → a signal of fabrication, the field is disputed",
         "Structured output fixes the form: the model must return the answer per a JSON schema; strict = it won't return a field outside the schema (the response_format parameter) -- it guarantees form, NOT truth",
         "Deterministic cross-checks in code: the amount in words matches the amount in figures, dates are valid, the parties are unambiguous",
         "Gate: no span / low confidence / failed check / a pronoun as the evidence → to a human",
     ],
     "scheme": ["Contract", "LLM extraction + span", "Cross-checks (code)", "Confidence gate", "Human review on disputed items"],
     "note": "Take confidence from objective signals (presence of a span, cross-checks, log-probabilities), not from asking the model \"are you sure?\" -- verbal self-assessment measures how well the model was trained to sound confident, not its actual reliability.",
     "notes": "This is the method, not the difficulty itself yet. The naive approach -- \"extract JSON\" -- works on typical cases and quietly breaks on ambiguous ones. The improvement that gives you something to check: for every field, a triple of value + evidence_span + confidence. The point of the span isn't to \"explain\" the decision (the model would make up an explanation too) -- it's that you can check it deterministically, by searching for it as a substring in the text; not found → a hallucination signal, a cheap non-model detector. Structured output (response_format with a json_schema, strict) fixes the form -- the model must return JSON in the given shape; the important caveat: the schema guarantees form, not truth (payer will be a string, but that doesn't mean it's the correct party). Order stable-content-first (the system prompt + schema are cached across hundreds of contracts via prompt caching), variable content last (the contract text). The cross-checks are ordinary code: num2words / a spelled-out-number parser for amounts, dateutil/workalendar for dates, currency reference tables, a party dictionary from the header. A practical trick for the parties: first extract the parties' details from the header, then require payer/payee to resolve to a known entity; \"the Party,\" \"he\" won't match -- an ambiguity that was invisible becomes detectable. Likely question: \"how do you get confidence if self-assessment can't be trusted?\" -- the presence of a span, token log-probabilities, and a verbal flag only as an additional signal."},
    {"kind": "complication", "kicker": "Case 2.1 · In practice",
     "title": "\"...if it provides the guarantee\" -- who is \"it\"?",
     "body": "\"The Customer pays the Contractor an advance if it provides a guarantee.\" Who is required to provide the guarantee? Grammatically, both nouns are neutral -- agreement doesn't narrow it down. WinoBias (a coreference benchmark, 3160 sentences): changing a single word flips the referent, and systems link pronouns to pro-stereotypical entities 21.1 F1 points more accurately (an accuracy metric, 0-100).",
     "effect": "The attention mechanism relies on statistical correlation between words, not on cause and effect. On ambiguous coreference, it errs systematically, in a predictable direction -- and in a confident tone.",
     "notes": "The difficulty has been moved here out of the setup slide. This isn't \"a bad model\" -- it's a property of the mechanism: attention computes a weight between the pronoun's position (the Query -- \"looking for who could have done this\") and the Key of each candidate; on an unambiguous signal (grammar and meaning point to one candidate), it's a hit; on an ambiguous one, the weight shifts to the statistically more frequent option, not to \"the one that's correct given the meaning of the contract,\" and the tone of the answer doesn't change. Distinguish two sources of difficulty: resolvable ambiguity (the answer is in the text but requires understanding meaning -- a good model handles it, and eval measures it) and genuine ambiguity (the answer can't be derived from the document; only the author knows it) -- the second case isn't solved by the model or by a checker, only by asking the author. Conflating them is a common mistake: a team \"improves the model's quality\" where there's nothing to improve. WinoBias is a direct illustration: the mechanism picks up correlations (statistics on \"who usually does what job\"), not causation, and wherever the correlation diverges from the truth, it errs systematically. In contracts, the role of the stereotype is played by the frequency of certain constructions. The system's job in the second case isn't to guess but to reliably catch the fact of ambiguity and escalate it. Likely question: \"fine-tune the model on coreference?\" -- that would raise the resolvable cases, but part of the ambiguity is unresolvable in principle; the final line of defense is the gate plus a human."},
    {"kind": "scheme", "kicker": "Case 2.1 · Solution",
     "title": "LLM extraction with verification of critical fields",
     "lead": "The model is a fast first pass; verification goes where the cost of error is high.",
     "nodes": ["Input normalization", "LLM extraction + span", "Cross-checks (code)", "Confidence gate", "Publish / human review"],
     "bullets": [
         "Garbage input (bad OCR) doesn't get through -- a text-quality threshold sits before extraction",
         "Deterministic checks catch mismatched sums and invalid dates without the model",
         "No span / low confidence / pronoun as evidence → to a human; money never reaches production past the gate",
     ],
     "caption": "Automate the bulk, insure the critical -- not \"all or nothing.\"",
     "notes": "The diagram is from section 6.1 of the case file. A contract of any format is first converted to clean text, and the text passes a quality threshold -- garbage input doesn't get through. Clean text goes to the LLM, which uses structured output to return, for every field, a value + a verbatim quote as evidence + a confidence flag. Candidates go through a deterministic layer of checks (the amount in words against the amount in figures, date validity and consistency, currency from a reference table, unambiguous parties), then a gate that lets only fields with a found span, sufficient confidence, and passed checks through to the final output; everything disputed goes to a human. The deterministic layer matters because it has zero drift: a regex that checks start date ≤ end date will never \"change its mind\" or get swayed by a confident tone. A sound tactic is to maximize the share of fields covered by deterministic checks. This is an economic calculation, not a compromise: even at an optimistic 10% error rate for raw extraction, across thousands of fields that's hundreds of wrong amounts scattered invisibly among the correct ones, all delivered in the same confident tone; the gate flips that economics -- a human reads not 1000 fields but 50-150. Likely question: \"would RAG, or the whole contract in context, remove hallucinations?\" -- no: the Stanford study on RAG-based tools found 17-33% hallucinations; our source of truth is span verification plus cross-checks, not \"the model saw the text.\""},
    {"kind": "breakdown", "kicker": "Case 2.1 · Breakdown",
     "logic": "A contract of any format is converted to clean text with a quality threshold (garbage OCR doesn't get through). Clean text → LLM with structured output: for every field, value + evidence_span + confidence. Candidates go through deterministic cross-checks, then a gate -- only fields with a found span, sufficient confidence, and passed checks make it into the final output; disputed items go to a human. This way the machine handles the bulk of typical cases, and human attention is spent only where the text has no unambiguous answer.",
     "components": [
         ("Input normalizer", "OCR (Tesseract/Yandex Vision/ABBYY) + pdfplumber/PyMuPDF + a text-quality threshold. The model gets text, not noise."),
         ("LLM extractor", "A top-tier model with structured output (json_schema, strict); the stable part of the prompt goes first (prefix caching)."),
         ("Cross-check layer", "num2words / a spelled-out-number parser, dateutil/workalendar, currency and party reference tables, pydantic. Errors caught without the model."),
         ("Confidence gate", "span found ∧ confidence ≥ threshold ∧ checks passed ∧ evidence isn't a pronoun. Splits auto vs. human."),
         ("Human review queue", "A table of disputed fields with the quote and the contract -- a focused review of 5-15% of fields."),
         ("Winograd-style eval set", "Disputed cases with ground-truth answers -- measures coreference on every release, catches regressions."),
     ],
     "comments": [
         "Attention relies on the statistical correlation of words, not on causation: on unambiguous cases it's excellent, on ambiguous ones it systematically picks the frequent option.",
         "A span, not \"are you sure\": a confident tone doesn't correlate with whether an unambiguous answer exists; the quote is either in the text or it isn't.",
         "The schema guarantees the form of the JSON, not the truth of the value -- truth comes from the cross-checks and the gate, not from a strict schema.",
     ],
     "notes": "The breakdown comes from sections 6.2-6.4 of the case file. The main thesis: attention relies on the statistical correlation of words, not on cause and effect. On unambiguous coreference (\"he\" = the only fitting candidate), it works well; on ambiguous coreference, the model systematically picks the more frequent option and delivers it confidently, because there's no unambiguous answer in the text and the model still has to output a token. The line isn't \"a bad model\" -- it's in the text itself: if there's no unambiguous referent, neither attention nor a checker will resolve it, only the contract's author can; the system's job is to catch the fact of ambiguity, not to guess the answer. Why a span, not \"are you sure\": a confident tone doesn't correlate with whether an unambiguous answer exists -- research shows models systematically overestimate their own confidence, and numeric self-assessments collapse to \"0.9/1.0\"; evidence_span gives a non-model, checkable signal. Why the schema doesn't save you from falsehood: structured output guarantees the form of the JSON, not the truth -- that comes from the cross-checks and the gate. Pitfalls: trusting a confident tone on ambiguous coreference; asking for confidence as a second question; blaming the model without checking the input (OCR garbage); trying to fine-tune the model instead of using a gate. Likely question: \"does this pipeline work for other fields -- deadlines, penalties, banking details?\" -- yes, the architecture is the same, only the validation rules change (banking details -- checksum validation for the INN taxpayer ID / bank account number, deadlines -- calendar arithmetic)."},
    {"kind": "resolution", "kicker": "Case 2.1",
     "solution": "Extraction is the model's job; resolving ambiguous coreference in money fields goes under verification and rules. The schema gives you form, code and the gate give you truth.",
     "howto": [
         "The prompt returns, for every field: value + span evidence from the text + a confidence flag",
         "Deterministic cross-checks: the amount in words matches the amount in figures, dates are valid, parties resolve to a dictionary built from the header",
         "Gate: a field with no unambiguous span, low confidence, or a pronoun as evidence → goes to manual review",
         "Keep an eval set of ambiguous contracts (Winograd-style), measure the share of correct referents and the share of escalations",
     ],
     "example": {"kind": "neg", "title": "Hallucinations even with RAG (legal/finance domain)",
                 "text": "Stanford, 2024: source-grounded tools still hallucinated -- Lexis+ AI 17%, Westlaw 33%, plain GPT-4 43%. Money fields without verification are unacceptable."},
     "notes": "[VERIFY-DAY-OF: double-check the Stanford 17/33/43% figures and the list of tools before class.] On the example card: even \"grounded\" (RAG-based) extraction in the legal/finance domain isn't hallucination-free -- that's exactly why money fields only go through verification. Step-by-step how-to from the breakdown and Q&A of the case file. (1) span evidence: in the prompt, require a quoted fragment of the source for every field; in post-verification, confirm the span actually exists in the text, otherwise it's a fabrication. (2) cross-checks: the amount in words against the amount in figures (the model extracts them from different places, and an error in one doesn't repeat verbatim in the other -- the discrepancy gets caught; this also catches typos in the contract itself), start date ≤ end date, currency recognized -- all deterministic code. (3) gate: no span or confidence below the threshold → to a human; tune the gate to the cost of error, and for money lean toward being over-cautious. (4) eval: split into resolvable cases (metric: resolution accuracy) and genuinely ambiguous ones (metric: escalation rate, with the ideal being 100% escalated, not 100% guessed). Log the reason for every escalation: if 70% are \"span not found,\" the problem is in the prompt/input, not in coreference. Pitfall: don't ask the model for a \"confidence estimate\" as a second question -- it measures how well the model was trained to answer, not actual confidence. Likely question: \"where exactly is attention here, rather than the model abstractly making mistakes?\" -- resolving \"he\"/\"the party\" is exactly what the mechanism does through Q/K/V; the error is born in the weighting itself."},
]

# ==========================================================================
# Case 2.2 -- Legal department assistant: raising quality and how to measure it
# Source: cases/case-2.2.md -- 4 slides: context -> concept -> complication -> breakdown
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 2.2 · Improving the legal department's assistant",
     "title": "\"It answers inaccurately -- make it better\"",
     "lead": "A chat assistant for the legal department has been running on a general-purpose model for a year. The client shows up with a vague \"make it answer better\": the answers sound confident, but the facts and the references to regulations are regularly inaccurate.",
     "inputs": [
         ("What exists", "a working assistant on a general-purpose model that doesn't use the regulations database"),
         ("Complaint", "confident tone, but facts and regulation citations are inaccurate"),
         ("No metric", "\"quality\" exists only as a feeling -- no number, no baseline"),
         ("Data available", "current regulations and rules in machine-readable form"),
         ("Logs available", "thousands of real questions from lawyers over the past year"),
         ("Cost of error", "a wrong citation to a regulation → legal risk"),
     ],
     "question": "How do you raise quality -- and how do you prove you raised it, rather than just made it \"sound more authoritative\"?",
     "notes": "The slide is the setup. The central constraint: there's no quality metric -- \"quality\" exists only as individual lawyers' impressions, with no number, no reproducible check, no baseline; as long as quality isn't in numbers, any change is accepted blindly. The task class is improvement without a defined metric. Two obvious moves: jump straight to \"improving the prompt\" (role, tone) -- the typical first attempt, which moves the form, not the substance; or first set up a metric and a baseline, then change one thing at a time and measure -- the only way to tell a real improvement from something that just \"sounds more authoritative.\" The beginner's trap is deciding by the impression that \"it got better\" without a number. The right engineering reflex here isn't \"what prompt should I write to sound nicer\" but \"how do I even know it got better.\" Likely question: \"what do I measure if there are no ground-truth answers?\" -- build a golden set from lawyers' real questions with reference answers and verifiable citations; 50-100 rows give you a signal. A year of logs is gold: eval on real traffic measures what people actually ask. Next: how to set up the eval, what actually moves quality, and why the first obvious idea (role) won't work."},
    {"kind": "concept", "kicker": "Method · How to measure quality",
     "title": "Metric and baseline first, changes second",
     "definition": "You can't improve what you don't measure. A generative system is deceptive: its output always looks like an answer, and to the naked eye a correct answer and a confident fabrication are indistinguishable. You need a reproducible measuring instrument -- a golden set.",
     "steps": [
         "Build a golden set: 50-100 real questions from the logs with reference answers and correct citations",
         "Three metrics: factual accuracy · citation correctness · share of answers with a verifiable source",
         "Score automatically: meaning -- LLM-as-judge (a stronger model scores the answer against a rubric, calibrated), citation -- exact string match (code, not a judge)",
         "Measure the current assistant's baseline on the set -- that's your reference point",
         "Change one thing at a time and measure on the same set; a change is accepted only if the metric improves",
     ],
     "scheme": ["Question", "Assistant's answer", "Check against reference / regulation", "3 metrics"],
     "note": "A golden set is just a table: \"question | reference answer | correct citation.\" Its size is a function of the task (traffic diversity, cost of error, number of topics), not a round \"200\"; the sufficiency criterion is that the set has stopped surfacing new types of errors.",
     "notes": "This is the measurement method, not the role trap itself yet. A classical program crashes on error; an LLM doesn't crash when it lacks knowledge -- it must pick a next token and picks the most plausible one, dressed in a confident tone. That's why the quality of a generative system can't be judged by eye: a person evaluates plausibility and fluency, not correctness, which they can't know without checking. The three metrics move independently, and it's essential to keep them separate: factual accuracy (whether it's telling the truth), citation correctness (whether it's the right regulation in its current version -- separately, because an answer can be substantively correct with a citation that's \"off target\"), and grounding rate (the share of answers with a verifiable basis -- for legal risk this is often more important than accuracy itself, since a grounded answer can be checked in seconds). How to score it: deterministic code-based matching wherever the ground truth is a string (a citation like \"Article 196 of the Civil Code of the Russian Federation\" -- a normalized string comparison, not a job for a judge); LLM-as-judge wherever the ground truth is meaning (though the judge has its own biases -- calibrate it); manual review is the gold-standard reference for calibrating the judge. Likely question: \"why not just ask the lawyers if it got better?\" -- user perception is biased by the form of the answer: a confident tone reads as \"more accurate\" even when the facts are the same; a golden set measures factual accuracy reproducibly."},
    {"kind": "complication", "kicker": "Case 2.2 · In practice",
     "title": "\"You are an experienced lawyer\" doesn't move the metric",
     "body": "A common first attempt is adding a role to the prompt: \"You are an experienced lawyer with 20 years in practice.\" Zheng et al., 2024: 162 persona roles across 2410 factual questions, four model families -- adding a role does NOT raise accuracy; the persona effect is essentially random. On the eval set, answers become more confident in form, but not more correct in substance.",
     "effect": "The role uses the same attention mechanism that resolved coreference: role tokens shift the choice toward style, but they don't add knowledge. Form and knowledge are different axes. Accuracy comes from grounding, not from a \"title\" in the prompt.",
     "notes": "The trap has been moved here from the setup slide. Why this happens, rather than \"prompting doesn't work\": a role in the system prompt is the same attention-weighting mechanism that resolved \"he\" → \"the cat\" in Case 2.1, except here the Query belongs to the positions of the generated answer, and the Key/Value belong to the role's tokens. Tokens like \"experienced,\" \"lawyer,\" \"years of practice\" get weight and shift the choice of the next tokens toward the vocabulary and confidence associated with the role -- the answer becomes more polished in form. But the weight on the role's tokens doesn't add a single fact to the model that wasn't already in its weights or context: if the needed fact isn't there, no phrasing of the role will create it -- it will only make the model state what it already \"knew\" more confidently, including confidently stated errors. Zheng et al. measured exactly this: zero gain in accuracy, the persona effect no better than random. How to detect it: run the eval with the role and without -- the numbers are the same; this makes it visible that the metric decides, not the impression. A role is useful for form (tone, structure, declining to answer outside its competence), just not for factual accuracy -- confusing these two axes is exactly the mistake the eval catches. Next: how to actually raise accuracy (grounding) and pin it down with a number."},
    {"kind": "breakdown", "kicker": "Case 2.2 · Breakdown",
     "logic": "A golden set is assembled once from real logs (clustering by embeddings for even topic coverage, 50-100 questions, a lawyer writes the reference answer + correct citation). The baseline is measured on it across three metrics: accuracy (LLM judge, calibrated against a manual sample), citation correctness (string matching in code), grounding rate (code checks the quote). Then the cycle runs: ONE change is made, the same set is run again, the metrics are compared to the baseline; the change is accepted and versioned only if the metrics improve.",
     "components": [
         ("Golden set", "A table of \"question | reference answer | correct citation\" from real logs. The only anchor that tells improvement from regression."),
         ("Set builder", "Clustering the logs by embeddings + selection for even topic coverage. Measures real traffic."),
         ("Eval runner", "Ragas / DeepEval / Promptfoo -- runs a version against the set, collects the three metrics."),
         ("LLM judge", "A stronger model, scores meaning against a rubric, T=0, calibrated against a manual sample."),
         ("Deterministic check", "Code: normalizing and comparing citations, checking that the quote exists. No hallucinations, no drift."),
         ("RAG grounding on regulations", "Retrieving fragments from the database + answering from them with a mandatory citation. The real lever on accuracy (per the metric)."),
     ],
     "comments": [
         "\"Raise quality\" is first a measurement problem, then a change problem: without a number, any edit is blind, and a confident tone and a fabrication look the same to the eye.",
         "Form and knowledge are different axes: a role moves form (the attention weight of the role's tokens), knowledge comes from data in context (grounding).",
         "grounding is a lever, not an off switch: even RAG-based tools give 17-33% errors; a change is accepted based on the metric, the judge is calibrated, citations are checked in code.",
     ],
     "notes": "The breakdown comes from sections 6.1-6.4 of the case file (for this case -- a single breakdown slide, as specified: context → concept → complication → breakdown). The main thesis: \"raise quality\" is, first, a measurement problem, and only second, a change problem. Where the limit of the role effect lies: a role in the prompt is the same attention-weighting mechanism that resolved coreference; the role's tokens get weight and shift the choice of the next tokens toward style, but they add no facts -- form and knowledge are different axes. Why grounding, not a \"magic phrase\": accuracy is moved by data in context, not by epithets in the role; but grounding isn't an off switch for hallucinations (the Stanford 17-33% even with RAG), it's a change that gets accepted based on the metric. Why the measuring instrument also needs checking: the LLM judge carries its own biases -- positional bias (favors the first/last option in order), a bias toward verbosity (a longer answer looks better -- genuinely dangerous, since the judge may rate a \"polished\" role higher), self-preference; whatever is deterministic (citations) -- check with code, whatever requires meaning -- with a judge, but a calibrated one. Pitfalls: deciding by the impression that \"it sounds more polished\" without a number; \"improving\" via role; changing several things at once; treating the judge as an oracle; mistaking grounding for a hallucination off switch and removing human review on critical documents. Likely question: \"the metric went up -- ship it and forget it?\" -- an increase is necessary but not sufficient; keep expanding the set with production failures, run the eval on every release, including silent vendor model updates."},
    {"kind": "resolution", "kicker": "Case 2.2",
     "solution": "Golden set and baseline first; what raises quality is grounding on current regulations, verified by the metric -- not the wording of a role. Change one thing at a time.",
     "howto": [
         "Build a golden set (question/reference answer/citation) from real logs, measure the current assistant's baseline",
         "Test the \"role\" hypothesis: with the role and without it -- the metric is the same (that's a success for the eval, not a failure)",
         "Add RAG on the regulations database with a mandatory citation; accuracy and grounding rate rise -- accept it",
         "Automated check: accuracy -- LLM judge (calibrated), citation -- exact string match; accept a change only if the metric improves",
     ],
     "example": {"kind": "neg", "title": "Role instead of measurable quality",
                 "text": "Zheng et al., 2024: 162 persona roles, 2410 questions -- role-in-prompt improves form, not factual accuracy. The rise in accuracy comes from grounding, and you see it on the eval, not by eye."},
     "notes": "The conclusion on the example card: whoever has a golden set will outpace, in a month, someone who spends a year \"improving by eye.\" Step-by-step how-to from the breakdown and Q&A of the case file. Turn \"raise quality\" into a cycle: measure → change one thing → measure again. (1) golden set: take real questions from the logs (you can cluster by embeddings for even topic coverage), a lawyer writes the reference answer and correct citation once; 50-100 rows, and the sufficiency criterion is that the set has stopped surfacing new types of errors. (2) baseline: run the current assistant, record the three numbers. (3) the very first hypothesis -- role -- fails on the metric: that's not a failure of the experiment but its success; a five-minute eval closed off a week of fruitless prompt rewriting. (4) the first candidate that works is grounding (RAG on the regulations database with a mandatory citation), accepted because the metric improves. Change one thing at a time -- otherwise you won't know what worked. Automated check: an LLM judge for meaning (calibrate it with a share of manual review; for pairwise comparisons, swap the order of the answers and average -- this cancels out positional bias), check citations with code. Version the bundle \"prompt/model/RAG version → set version → three numbers.\" Likely question: \"what if the LLM judge itself gets it wrong?\" -- keep a share on manual review as calibration, and check citations deterministically, not with a judge."},
]

S += [{"kind": "divider", "number": "3", "block": "Block 3",
       "title": "Sampling and tokenization: how the model generates and sees text",
       "tag": "Picking a generation mode · running into the limits of counting"}]

# ==========================================================================
# Case 3.1 — Product card generator: description + structural parameters
# Source: cases/case-3.1.md — two runs, a scheme with two branches, WITHOUT distribution
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 3.1 · Building a product card generator",
     "title": "Product cards: description and structural parameters",
     "lead": "A marketplace creates product cards by the thousands daily. Each card has two fundamentally different field groups: a marketing description (free text) and structural attributes (machine-readable fields).",
     "inputs": [
         ("Volume", "thousands of cards a day — writing them by hand isn't realistic"),
         ("Description", "natural, coherent text, one consistent brand voice, not copy-paste"),
         ("Attributes", "dimensions, weight, category from a reference list — a strictly defined form"),
         ("Regulated fields", "ingredients, shelf life, warranty — the source of truth is the GOST standard/spec sheet"),
         ("Cost of error differs", "marketing — cheap and reversible; regulated fields — liability to the regulator"),
     ],
     "question": "Which mode to set — and is it the same for every field?",
     "notes": "On the slide — the setup. The two groups of fields live under opposite laws: the marketing description values liveliness and variety (a thousand cookie-cutter cards = spam, it doesn't sell); structural attributes value repeatable, strict form (the catalog takes numbers as numbers — a category from a reference list, \"about 5 kg\" instead of 5.0 won't load). Some of the structural fields are regulated: ingredients, shelf life, warranty — their value is set not by imagination but by a source (a spec sheet, a GOST standard). The cost of error differs: low and reversible in the description, high in the structural fields (a wrong dimension breaks the shipping calculation, a wrong regulated field means liability to the regulator). The temptation is to run everything through one model in one request at one temperature; that's exactly the path that produces the most expensive mistakes, because a single sampling setting serves at best one of the two groups well. The task class is generation with two different output modes in one pipeline. Next — how to split fields across modes: tuning temperature for descriptions, structured output for attributes, substitution from the source for regulated fields."},
    {"kind": "variants", "kicker": "Case 3.1 · The temperature axis",
     "title": "One prompt, three temperatures: an axis of spread, not of \"flair\"",
     "lead": "The same factual question, three temperatures, repeated runs at each. The axis is \"predictable/repeatable ↔ random/varied and risky\".",
     "cols": [
         {"head": "T = 0 (repeatable)", "sample": "Repeated runs — identical answers. The choice is almost deterministic.",
          "use": ["Predictable and repeatable", "Classification, extraction, attributes", "No spread, by construction"]},
         {"head": "T = 0.7 (working spread)", "sample": "Phrasing drifts between runs, but the facts and coherence hold.",
          "use": ["Variety of form without losing substance", "Marketing, explanations", "The working choice for descriptions"]},
         {"head": "T = 1.3+ (risk)", "sample": "The answer falls apart: coherence breaks down, factual errors and stray insertions creep in.",
          "use": ["Idea drafts, brainstorming", "Not for facts", "Risk of incoherence and fabrication"]},
     ],
     "note": "Mini-experiment: 20-30 cards from different categories, one prompt at 0.4 / 0.7 / 1.0 / 1.3, 3 runs each, scored on \"variety of phrasing without factual errors and in the brand tone\". The working zone is usually 0.6-0.8; the chosen T is locked into the config, not the provider's default.",
     "notes": "The temperature axis is placed in the column headers; the visual experiment comes BEFORE the mechanics (concept) so the \"predictable ↔ random\" axis is visible before the mechanism is explained. Don't pick a temperature at random, and don't confuse it with \"style\". The mechanics: as T→0, the probability of the top candidate → 1, and the choice matches argmax (deterministic); as T>1, probabilities flatten out, and low-ranked tail tokens get a real chance — hence the spread and the risk of incoherence. T never changes the order of the candidates — it changes how confidently the sampling sticks to that order. What reads as \"livelier\" at a moderate T is variety of phrasing BETWEEN runs, not a change of style within one answer; at high T that same variety turns into noise. How to read a batch experiment with two rough numbers per T: the share of unique phrasings (the higher, the livelier the catalog) and the share of runs with a factual error or a slip out of tone (the lower, the safer); you move up in T and look for the point where the first number is high and the second is still close to zero — usually 0.6-0.8, but it depends on the model and the prompt, so the tuning is repeated whenever the model changes. Brand tone is set by the prompt and few-shot examples, not by temperature — \"I want a different style, let me raise T\" is a typical confusion: that's not how style changes, spread changes. Check the provider's default: if you don't set temperature explicitly, you're running on its default, chosen for you at random. Likely question: \"is high T more creative?\" — no, it's more varied and riskier; \"creativity\" without coherence is noise."},
    {"kind": "concept", "kicker": "Method · Sampling and structured output",
     "title": "Temperature sets spread; a schema sets form, not truth",
     "definition": "Temperature — one knob: how random the choice of the next word is. Low → the choice is predictable and repeatable (the model almost always takes the most probable option); high → the choice is more random and varied, but riskier. It doesn't change the order of \"what's more probable\", or the facts themselves.",
     "steps": [
         "Low T → almost always the most probable option; predictable and repeatable (at T=0 — argmax)",
         "High T → rare options get a chance; more varied, but incoherence and fabrication creep in",
         "T ≠ truncation: top-k / top-p CUT OFF unlikely options (by count / by mass), T only changes the randomness of the choice",
         "structured output (json_schema, strict) — the model must return an answer matching a JSON schema; strict = it won't return a field outside the schema (the response_format parameter)",
         "The schema guarantees FORM (numbers as numbers, a category from the reference list), but NOT the truth of the value",
     ],
     "scheme": ["Next-word choice", "Temperature: randomness", "top-k/top-p: cut the rare", "Schema: form, not truth"],
     "note": "The correct temperature axis is \"predictable/repeatable ↔ random/varied and risky\", NOT \"boring ↔ vivid\". High T doesn't make the style more flamboyant — it makes word choice more random. Brand tone is set by the prompt and examples, not by temperature.",
     "notes": "Here — the mechanics of the axis already shown. Mechanically (for Q&A, not for the slide): the model's true output at every step is a probability distribution over the whole vocabulary; temperature divides the logits (raw scores) by T before softmax (the normalization into probabilities), changing the sharpness of the distribution but not the order of the candidates. All of the model's \"creativity\" and all of its \"randomness\" don't live in the distribution — they live in the rule for choosing a token out of it — that's sampling, the one part the engineer controls with the API knobs. Dividing by a positive T does NOT change the order of the candidates — the most probable one stays the most probable; what changes is the sharpness of the distribution, i.e. how confidently the sampling sticks to that order. The arithmetic on three tokens: logits 2.0/1.0/0.0 at T=1 give probabilities 0.67/0.24/0.09; at T=0.5 (dividing by 0.5 = doubling) 0.87/0.12/0.02 — sharper; at T=2 they give 0.51/0.31/0.18 — flattened, the order never changed once. top-k truncates by the number of candidates, top-p (nucleus) — by cumulative mass; temperature scales the heights without discarding any tokens — different axes. How to see the axis — repeated runs of the same prompt, not a single answer: on one run you can't tell \"the model is confident\" from \"it got lucky\". Structured output doesn't work by persuading the prompt (\"answer in JSON\" gives valid JSON ~80% of the time), but by constrained decoding: the schema is compiled into an automaton over tokens, invalid ones are zeroed out, OpenAI's strict mode gives 100% schema compliance. Likely question: \"is top-p/top-k the same as temperature?\" — no, they cut off the tail, temperature scales the heights."},
    {"kind": "complication", "kicker": "Case 3.1 · In practice",
     "title": "Regulated fields: no temperature saves you",
     "body": "Ingredients, contraindications, warranty terms, \"complies with GOST...\" — the same cards, but variability isn't acceptable here, the text must exactly match the source. Air Canada (2024): a chatbot \"made up\" a refund policy that didn't exist, and a tribunal held the company liable — the company is responsible for a generated factual statement.",
     "effect": "Temperature controls spread, not accuracy. Even T=0 makes the output repeatable, not true — the model can consistently repeat something wrong. Regulated fields don't need the \"right T\" — they need substitution from a verifiable source.",
     "notes": "The trap goes here. Why even T=0 doesn't save you: low temperature makes the choice stable (repeatable), but doesn't guarantee the fact is correct — the model can consistently repeat something wrong. Air Canada (Moffatt v. Air Canada, February 2024) is the most-cited precedent: a chatbot on the airline's website told a passenger about a bereavement-fare policy that didn't exist, the passenger bought a ticket and was refused; the British Columbia tribunal found negligent misrepresentation, rejecting the argument that \"the bot is a separate entity\"; the amount was small ($812), the principle is large — the company is responsible for a factual statement the model generated. A regulated field on a card (ingredients, warranty, \"complies with GOST\") is exactly that kind of factual statement in front of the buyer and the regulator. How to detect a regulated field: if a field has an external normative source of truth (a GOST standard, an instruction manual, a warranty card), it's regulated — generation has no place there, it's substituted from the source by a template. A separate, well-documented failure class is \"one temperature for everything\": set it high for lively descriptions and you get fabricated attributes; set it low for stable attributes and you get boring descriptions with still no guarantee of truth. Likely question: \"can I just use T=0 and copy from the source via the prompt?\" — template substitution is more reliable: T=0 doesn't stop the model from paraphrasing or dropping a point, a template guarantees an exact match."},
    {"kind": "scheme", "kicker": "Case 3.1 · Solution",
     "title": "A three-branch pipeline: two runs + substitution",
     "lead": "Different groups of fields — different generation modes; regulated fields bypass the model.",
     "nodes": ["Field classifier", "A: desc (T≈0.7)", "B: attributes (T=0)", "Regulated: from source", "Validate + assemble"],
     "bullets": [
         "Run A — free text, temperature tuned on a batch, input is known facts only",
         "Run B — structured output (json_schema, strict) + T=0 + an evidence field for every value",
         "Regulated fields (ingredients, shelf life, warranty) — substituted from the spec sheet/GOST standard WITHOUT generation; anything suspicious goes to a human",
     ],
     "caption": "One call for everything is a false saving of one line of code, paid for with a worse result in both groups of fields.",
     "notes": "The scheme from section 6.1 of the case file — three branches, not one. The input data about the product is first sorted by field type: what can be generated freely (marketing), what structurally (non-regulated attributes), what can't be generated at all (regulated). Then two separate model runs with opposite sampling settings: run A produces live text at a moderate temperature tuned on a batch (the input is known facts only, the prompt forbids inventing specs); run B produces valid attributes via structured output at T=0 and requires a justification-source for every value (the evidence field). Regulated fields bypass the model — they're substituted from the spec sheet/template. After run B, deterministic value validation is mandatory — it's what supplies the truth the schema doesn't guarantee: ranges (weight isn't 0 or 10,000 kg), a category from the reference list, and above all — the evidence actually appears in the input data (a crude substring-match check catches the most common failure: an impeccably formatted but fabricated value). The cost of splitting into two runs is negligible: run B is short (tens of tokens), while a single call with a rigid schema for the whole card forces the model to \"spend\" its distribution on form even where live text is needed. Likely question: \"put the description in as a string field in the same schema?\" — you'd inherit the worst of both: a single T would ruin either the description or the attributes."},
    {"kind": "breakdown", "kicker": "Case 3.1 · Breakdown",
     "logic": "The input data is sorted by field type: free generation (marketing), structural generation (non-regulated attributes), can't be generated (regulated). Two separate model runs: A — live text at a T tuned on a batch; B — attributes via structured output at T=0 with an evidence field. Regulated fields bypass the model, substituted from the source. Everything generated goes through a check (a light one for text, mandatory validation for attributes); anything suspicious and anything regulated escalates to a human.",
     "components": [
         ("Field classifier", "A deterministic layer (rules/config): generate freely, generate structurally, or take from the source. Implements \"different fields — different modes\"."),
         ("Run A (description)", "Free text: a prompt with brand tone + few-shot examples, T≈0.6-0.8 from the config, input is known facts only."),
         ("Run B (attributes)", "structured output (response_format/json_schema/strict), T=0, a schema with an evidence field. Valid form."),
         ("Value validator", "Code after B: ranges, units, evidence present in the input, category from the reference list. The truth the schema doesn't provide."),
         ("Regulation substituter", "A template + source (spec sheet, GOST standard, warranty reference). Verbatim substitution, no generation."),
         ("Config", "Model version, temperatures per field type, schema version — a single point for deliberate decisions."),
     ],
     "comments": [
         "Temperature = the spread axis, not style and not accuracy: high T increases the randomness of token choice, and on facts it leads to fabrication.",
         "A schema guarantees form, not the truth of a value: weight_kg=5.0 can be fabricated → value validation and an evidence field are mandatory.",
         "T=0 ≠ truth (and not full determinism in the cloud either): no T saves regulated fields — their source of truth is the spec sheet/GOST standard, not the model.",
     ],
     "notes": "Breakdown from sections 6.2-6.4 of the case file. Temperature = the spread axis, not style and not accuracy: run A works at a moderate T for the sake of varied phrasing between cards; high T doesn't \"decorate the style\", it increases the randomness of token choice, and on facts it leads to fabrication. A beginner's trap: raising T \"to be more creative\" and getting fabricated specs; the correct framing is \"raise T so descriptions repeat less, but not so much that the facts slip\" — the threshold is found by a batch experiment. A schema guarantees form, not the truth of a value: run B always returns valid JSON of the right shape, but weight_kg=5.0 can be fabricated; the trap is believing that if the JSON is valid, the value is correct; hence the mandatory value validation and the evidence field (the schema gives form, code and the source give truth). T=0 ≠ truth, and not full determinism either: low temperature makes the output repeatable, but the model can consistently repeat something wrong, and in the cloud even T=0 doesn't give bit-for-bit determinism (the provider batches requests in variable-size groups, and the order of summation inside the kernels differs); no temperature saves regulated fields. One call for everything is a false saving that costs you neither of the two groups being served correctly. Likely question: \"100% schema compliance — why validate values on top of that?\" — the 100% is about form, not truth; plus a separate refusal path has to be caught by code."},
    {"kind": "resolution", "kicker": "Case 3.1",
     "solution": "Different fields — different modes: T≈0.7 for marketing, structured output + T=0 for attributes, substitution from the source for regulated fields. The schema gives form; code and the source give truth.",
     "howto": [
         "Split the card's fields with a classifier: marketing (generate), structural (generate structurally), regulated (substitute)",
         "Marketing: T≈0.6-0.8, tuned on a batch of 20-30 cards; brand voice via the prompt and few-shot examples, not temperature",
         "Attributes: structured output (json_schema, strict), T=0, an evidence field; then value validation by code",
         "Regulated: a template with substitution from a verified source, no free generation at any T",
     ],
     "example": {"kind": "pos", "title": "Structured output as a reliable form",
                 "text": "OpenAI: structured outputs in strict mode give 100% schema compliance versus ~86% for function calling — the model physically cannot emit a token outside the schema."},
     "notes": "On the example card, the caveat: 100% form ≠ 100% truth — structured output doesn't replace value validation or regulated-field generation; strict mode works via constrained decoding. Step-by-step how-to from the breakdown and the case file's Q&A. The decision per field: \"is this about polish, or about fact/law?\" Polish — moderate T (0.6-0.8), tuned on a batch of 20-30 cards from different categories against the criterion \"variety without lying\", 3 runs per value. Fact/law — substitution from the source: a template with placeholders, values from the source card or a verified database, generation has no place there at any T. Attributes — structured output (strict) + T=0 + an evidence field, with mandatory code validation after generation: ranges, units, checking that the evidence actually appears in the input data (a crude substring-match check catches a fabricated value — the model might return material: \"stainless steel\", evidence: \"stainless steel\", even though the word \"steel\" isn't in the source). Traps: don't rely on T=0 as \"insurance against lying\" — stability ≠ truth; start with a schema simpler than you'd like (deep nesting gets you closer to the limits of the grammar compiler); don't generate the schema dynamically on every request (cold compilation). Likely question: \"is brand tone a matter of temperature?\" — no, tone is set by the prompt and few-shot examples, temperature only controls the spread around that tone. A field is missing from the input — allow null in the schema and require null, not a guess."},
]

# ==========================================================================
# Case 3.2 — Tokenization breaks counting and validation
# Source: cases/case-3.2.md
# ==========================================================================
S += [
    {"kind": "context", "kicker": "Case 3.2 · Fixing a registration and payments web service",
     "title": "Character-level features: password, card, limit, count",
     "lead": "A web service with registration and payments. A set of small features working at the level of individual characters. At the planning meeting: \"We have a model — let's just ask it, it's smarter than regexes.\"",
     "inputs": [
         ("Feature 1 · password", "length ≥12, character classes, no 3+ identical in a row + a list of violations"),
         ("Feature 2 · card", "last 4 digits visible, the rest asterisks (a PCI DSS requirement)"),
         ("Feature 3 · truncation", "exactly to a character limit (SMS segment, DB field), without breaking a word"),
         ("Feature 4 · counting", "character count, length, an SKU of exactly 8 characters"),
         ("Precision is mandatory", "code runs on every request, no human in the loop; one wrong character = a leak or a rejected form"),
     ],
     "question": "What should implement each feature, and why — a model, code, or a combination?",
     "notes": "On the slide — the setup. All the features work at the level of individual characters, precision is mandatory, there must be no errors: the code runs on every request with no human in the loop — if the length check is off by a character, the form will accept something invalid or reject something valid; if masking drops a digit, that's a leak. Volume and latency: milliseconds, not \"go call an API and wait\". Regulation: card masking has an external requirement (PCI DSS — the set of rules for protecting bank card data); sending a full card number to someone else's cloud API just to \"mask it\" is a problem in its own right, separate from the question of whether the model can do it. The setup doesn't claim \"the model will fail\" — it just describes a set of character-level tasks and notes that someone on the team proposes doing them via an LLM; what actually implements them is for the students to decide. Contrast with case 3.1: there, generating text and attributes was the model's home turf, working with tokens is its strength; here the task is the opposite — character-level checking and counting isn't the model's niche. The same mechanism (working with tokens, not letters) that makes an LLM a good generator makes it a bad character counter. Next — why a token ≠ a character, exactly where it breaks, and how code does the same job reliably."},
    {"kind": "concept", "kicker": "Method · Token ≠ character",
     "title": "Why the model structurally can't count characters",
     "definition": "A token is an identifier from the model's vocabulary. Text is cut into tokens (frequent subsequences) and turned into numbers; from then on the model works ONLY with numbers, not letters. Token boundaries don't line up with letter boundaries.",
     "steps": [
         "\"strawberry\" is 3 tokens: [st][raw][berry], not 10 letters; \"klubnika\" (Russian for \"strawberry\") is also 3 tokens",
         "Inside the token [raw] there's NO separate representation of the letter 'r' at position 1 — just averaged statistics of contexts",
         "The vocabulary is built once, before training, by the BPE algorithm (Byte-Pair Encoding — how text gets cut into tokens), and doesn't change afterward — a trade-off made for the sake of attention's economics",
         "A character-level representation would make the input 3-5x longer, and the cost of attention grows quadratically",
         "So character counting, length, and character-level slicing are unreliable — and this is NOT something that \"gets fixed in the next version\"",
     ],
     "scheme": ["String \"strawberry\"", "BPE cuts it into tokens", "[st][raw][berry] = 3 numbers", "No letters as units"],
     "note": "Jagged intelligence: the same model solves an olympiad problem and fails to count the letters in a 9-letter word. Success on an impressive task is NOT evidence of reliability on a \"simple\" one. \"It wrote SQL — surely it can count characters\" is a mistaken extrapolation.",
     "notes": "Here — the mechanics, not yet the demonstrations themselves. A token is an identifier (an integer) from the vocabulary; text doesn't enter the model letter by letter — it's first cut into tokens (statistically frequent subsequences learned during training) and turned into numbers. Token boundaries don't line up with the boundaries of letters, syllables, or morphemes — the tokenizer cuts by the corpus's frequency statistics. Inside the token [raw] there's no breakdown into letters as separate addressable units: the token's vector is a learned representation of the contexts it appears in; asking it \"which is the third letter\" is like asking an averaged portrait of a crowd about the eye color of the third person from the left. The model can reconstruct letters by an indirect route (if the word was often spelled out letter by letter), but that's reconstruction from memory, not reading a position, and so it's unreliable. The vocabulary is built by BPE (Byte-Pair Encoding — merging frequent pairs) once before training; that's a trade-off, not a bug: a character-level representation would make the input 3-5x longer, and the cost of attention grows quadratically (4x longer input — 16x more expensive). Don't expect this to \"get fixed\": there's no vocabulary that's simultaneously \"a frequent chunk for efficiency\" and \"a separate letter for counting\" — these are mutually exclusive requirements. It's worse for Russian: about 0.5 tokens per character versus 0.25 for English. Likely question: \"does chain-of-thought solve this?\" — sometimes, if the model spells the word out or calls code, but that's more expensive and gives no guarantee; for an exact result, len/regex is more reliable."},
    {"kind": "complication", "kicker": "Case 3.2 · In practice",
     "title": "Patch != skill: strawberry fixed, cranberry breaks",
     "body": "A race of point patches: GPT-5.2 answered \"two r's\" for strawberry; GPT-5.5 fixes strawberry, but for \"how many r's in cranberry\" answers \"two\" (the correct answer is three); GPT-5.6 fixes cranberry. Every viral question eventually gets its own fix, but the task class never gets solved.",
     "effect": "Passing a viral specific example ≠ having a skill. The model passes KNOWN examples (fine-tuned in, or via a heuristic), but your SKU or password is unknown to it. Swap in a rare, non-viral word and the failure comes back.",
     "notes": "[VERIFY-DAY-OF: GPT-5.x versions and their answers on strawberry/cranberry are volatile — re-check before class; present forward-dated models as an illustration of the patch-race pattern, not as a verified fact.] The meme \"how many r's in strawberry\" became the canonical example of LLM blindness to letters; the mechanism is the same one — the word arrives as [st][raw][berry], not ten letters. What's interesting isn't the error itself but its evolution: it shows the nature of the problem — this is a race of point patches, every viral question eventually gets its fix (via fine-tuning on it or a heuristic), but the task class never gets solved, and character-level counting stays broken on words that haven't gone viral yet. A dedicated benchmark even appeared for this — StrawberryBench (847 questions, seven difficulty levels for counting an arbitrary letter). Lesson learned: passing a viral specific example ≠ having a skill — test your own rare, unknown-to-anyone cases separately; don't rely on \"the model counts letters now\" — it passes known examples, and your SKU or password is unknown to it. A related failure is arithmetic: without external tools, multiplication accuracy drops from ~59% on 3-digit numbers to 4% on 4-digit numbers and 0% on 5-digit numbers (Dziri et al., 2023, \"Faith and Fate\"); the sharpness of that drop-off is a reliable sign of a structural problem, not an \"intelligence\" one. A mini-experiment for the skeptic on your team: ask the model how many of a given letter appear in a list of words (common + rare + made-up + SKUs), compare against word.count from code — the model is right on viral words, wrong on rare ones, code gives 100% on any of them. The key to the demo is including specifically non-viral words: test only strawberry and you're measuring patch coverage, not skill."},
    {"kind": "scheme", "kicker": "Case 3.2 · Solution",
     "title": "Deterministic to code, semantic to the model",
     "lead": "Split the task by the nature of the result: an exact character-level result, or understanding of meaning.",
     "nodes": ["A task over a string", "Chars or meaning?", "Character -> CODE", "Meaning -> MODEL", "Mixed -> model + code"],
     "bullets": [
         "An exact result at the level of characters/length/format/numbers → code: len, regex, slices, count, formatters",
         "Understanding meaning (is this spam? what's the tone? paraphrase this?) → the model, it has no competition here",
         "Mixed (shorten to under 160 characters while keeping the point): the model does meaning, code does the exact length (truncate on top)",
     ],
     "caption": "Code: microseconds, free, 100% reproducible, testable. A model's API: tens to hundreds of ms, paying for tokens, a probabilistic result.",
     "notes": "The scheme from section 6.1 of the case file. Every incoming task over a string is first classified by the nature of the result: does it need an exact result at the level of characters, positions, length, or numbers — or does it need an understanding of meaning. Character-level/deterministic work goes to code (len, regex, slices, count, formatters, ordinary arithmetic) — there the result is exact, instant, free, and reproducible. Semantic work (is this spam? what's the tone? extract the gist? paraphrase?) goes to the model — it has no competition here among ordinary code. If the task is mixed (it needs both meaning and an exact form — for example \"shorten the description to 160 characters while keeping the point\"): the model handles the semantic part with no hard length requirement, code guarantees the character-level part (truncate(model_output, 160)) — a final deterministic cut on top. Never make the model the last word on an exact character-level constraint — code has the final say. The numbers make the choice obvious: a character operation in code is microseconds on a local processor, zero cost, one-hundred-percent reproducibility; the same operation through an API is tens to hundreds of ms, you pay for tokens on every call, and you depend on the service's availability with a probabilistic result. Even if the model counted characters perfectly, handing it this job would be more expensive, slower, and more fragile. Likely question: \"different models tokenize differently, maybe some model has token = character?\" — no mainstream model has token equal to character, that would defeat the purpose of tokenization; the answer is code."},
    {"kind": "breakdown", "kicker": "Case 3.2 · Breakdown",
     "logic": "Every task over a string is classified by the nature of the result: an exact result at the level of characters/positions/length/numbers, or understanding of meaning. Character-level work goes to code (len, regex, slices, count, formatters) — exact, instant, free, reproducible. Semantic work goes to the model. Mixed: the model handles meaning, but the final word on exact length/form belongs to the surrounding code. Everything character-level is covered by unit tests at the boundaries, because precision here is a requirement, not a nice-to-have.",
     "components": [
         ("Task-nature classifier", "Not code, but an engineer's decision/checklist: \"exact, character-level result → code; meaning → model\". Made before implementation."),
         ("Character code", "len (length), regex (classes, format, positions), slices (s[:n], s[-4:]), count, formatters. Microseconds, testable."),
         ("Model (LLM)", "Meaning only: classification, extracting the gist, paraphrasing, a clear error message. Never exact counting/length/masking."),
         ("Model-output wrapper", "For mixed tasks: truncate()/validate() on top of the model's answer guarantees the exact form."),
         ("Boundary unit tests", "Threshold ±1, empty string, whitespace, emoji/non-ASCII, a long string. Catch off-by-one errors."),
         ("Tokenization visualizer", "tiktokenizer.vercel.app / tiktoken — a tool for understanding and demonstration, not for runtime use."),
     ],
     "comments": [
         "Inside a token there's no reliable representation of \"which letter is at which position\" → counting, length, slicing, format validation are structurally not the model's job.",
         "The 3.1/3.2 pair is one nature of the model seen from two sides: know where the mechanism works for you (generation) and where it works against you (counting).",
         "Traps: extrapolating from hard to \"simple\" (jagged intelligence); \"it answered right on my test\" (check a rare case); sensitive data sent to an API; no boundary tests.",
     ],
     "notes": "Breakdown from sections 6.2-6.4 of the case file. What the case illustrates about the tokenization mechanism: the model works with a sequence of tokens (numbers), not letters; inside a token there's no reliable representation of \"which letter is at which position\", so character counting, length control, character-level slicing, and format validation are operations the model structurally lacks the right representation for. This isn't fixed by fine-tuning or a new version: the cause is a trade-off built into tokenization for the sake of attention's economics. The central takeaway: character-level and deterministic operations aren't the model's job — code does them. Contrast with case 3.1 (same mechanism, different niche): in 3.1 the task was generation, where the model is on its home turf and working with tokens is its strength; here the task is the opposite — exact counting and validation — and the same token mechanism makes the model unsuitable. The 3.1/3.2 pair is one nature of the model seen from two sides: know where the mechanism works for you (generation) and where it works against you (counting); knowing when to say \"an LLM isn't needed here\" is a skill this course teaches. Traps: \"the model is smart, it'll handle something this small too\" (extrapolating from hard to simple — the jagged-intelligence trap, success on SQL doesn't predict success at counting commas); \"it answered correctly on my test\" (check it on a rare, non-viral example); the model truncating text to N characters (\"about N\" is a bug for a hard limit); sending sensitive data to an API for a character-level operation (a PCI DSS violation); exotic strings in the input (risk of a glitch token — an undertrained vocabulary entry, ~4% of the vocabulary, anomalous behavior); no boundary tests. Likely question: \"where does the model actually fit into these features?\" — only in semantic add-ons: a clear explanation of why a password is weak, language detection, classifying a request by topic."},
    {"kind": "resolution", "kicker": "Case 3.2",
     "solution": "Code handles character-level and deterministic work; the model is for meaning, not counting. If you can't avoid the model, it handles meaning while wrapper code guarantees the exact form.",
     "howto": [
         "Password — len + regex over character classes; card — a string slice (d[-4:] + asterisks), locally, not a byte goes to an API",
         "Truncation to a limit — a slice + len; counting and format — count and re.fullmatch; all deterministic and in microseconds",
         "A mixed task — the model handles meaning, code guarantees form: truncate(model_output, 160) on top",
         "Set up boundary unit tests: threshold ±1, empty string, whitespace, emoji/non-ASCII, a long string",
     ],
     "example": {"kind": "pos", "title": "Code where code belongs, the model where the model belongs",
                 "text": "Production form-validation, masking, and truncation systems do NOT use an LLM for the character-level part — that's regex, len, slices, covered by tests. The LLM only comes in for meaning."},
     "notes": "The example card's takeaway: the \"boring\" solution in code isn't \"we don't use AI\" — it's engineering maturity, the tool chosen to match the nature of the task. Step-by-step how-to from the breakdown and the case file's Q&A. Each of the four features is solved with deterministic, character-level code. Password: len(pw)<12 and re.search over character classes ([A-ZА-Я], \\d, special characters), (.)\\1{3,} for repeats — len counts characters exactly and instantly, the result is reproducible. Card: strip non-digits, slice d[-4:], asterisks for the rest, grouped in 4s — a local operation, not a byte of card data goes to someone else's API (that's both a PCI DSS requirement and common sense), and the guarantee is checked by a test, not by \"trusting the model\". Truncation: len(text)<=limit, otherwise a slice with room for an ellipsis, without breaking a word — cut at the last space — len(result)<=limit is guaranteed by construction and checked by an assert. Counting/format: str.count, re.fullmatch against the pattern [0-9A-Z]{8} for the SKU, re.finditer for positions. A subtlety about length in characters: in Python, len counts Unicode code points — for emoji and composite characters use grapheme segmentation (regex \\X), but that's a subtlety of CODE, solved with code tools, not by handing it to the model. If a task is mixed, the model does the semantic part, code guarantees the character-level part on top; the model is never the final authority on a character-level constraint. Boundary unit tests (threshold ±1, empty, whitespace, emoji, a long string) catch the vast majority of errors; the model would \"wobble\" on them non-deterministically, and the failure couldn't even be pinned down with a reproducible test. Likely question: \"why use code if the LLM is smarter?\" — \"smarter\" doesn't hold on every axis; don't drive nails with a microscope."},
]

# ===== Final ===============================================================
S += [{"kind": "closing",
       "takeaways": [
           "Embeddings: which model to pick is decided by a mini-eval on your own data (recall@k/MRR), not by a benchmark ranking; \"similar\" ≠ \"the same\" → use structural keys.",
           "Attention: correlation, not causation → the model extracts and justifies a span, rules and a human verify anything critical; grounding moves quality, not role-play.",
           "Sampling and tokenization: temperature sets the spread (not style, not truth), a schema sets the form (not truth); counting characters isn't the model's niche — code does it.",
       ],
       "bridge": "One principle across all three: a mechanism isn't a \"model feature\" — it's a boundary the engineer knows from both sides, using its strength and hedging its weakness. Next — Lecture 3: how these mechanisms combine into architectures (RAG, agents)."}]

SEMINAR = {
    "dir": "sem-03", "number": 3, "lang": "en",
    "spec_file": "spec_sem03_en.py",
    "title": "Seminar 3 — Three model mechanisms in system design",
    "central": "Three mechanisms across six system-design tasks: we build, we fix, we extend.",
    "lo": "[LO1, LO4, LO6, LO7]",
    "slides": S,
}
