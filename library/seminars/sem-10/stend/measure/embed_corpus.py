import json, time
from harness2 import embed_batch

data = json.load(open("corpus_case1.json"))
corpus = data["corpus_500"]
questions = data["questions"]

texts = [d["text"] for d in corpus]
BATCH = 25
all_vecs = []
cost_total = 0.0
t0 = time.time()
for i in range(0, len(texts), BATCH):
    batch = texts[i:i+BATCH]
    vecs, meta = embed_batch(batch)
    all_vecs.extend(vecs)
    cost_total += (meta["cost"] or 0)
    print(f"batch {i}-{i+len(batch)}: wall={meta['wall_s']}s cost={meta['cost']}")

for d, v in zip(corpus, all_vecs):
    d["embedding"] = v

q_texts = [q["question"] for q in questions]
qvecs, qmeta = embed_batch(q_texts)
for q, v in zip(questions, qvecs):
    q["embedding"] = v
cost_total += (qmeta["cost"] or 0)

elapsed = time.time() - t0
print(f"TOTAL embed wall={elapsed:.1f}s cost=${cost_total:.6f} for {len(texts)} docs + {len(q_texts)} queries")

json.dump({"corpus_500": corpus, "questions": questions,
           "embed_meta": {"model": "openai/text-embedding-3-small", "total_cost_usd": cost_total,
                           "total_wall_s": elapsed, "n_docs": len(texts), "n_queries": len(q_texts)}},
          open("corpus_case1_embedded.json", "w", encoding="utf-8"), ensure_ascii=False)
print("saved corpus_case1_embedded.json")
