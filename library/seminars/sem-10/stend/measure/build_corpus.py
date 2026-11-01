#!/usr/bin/env python3
"""Строит корпус для Кейсов 1 и 3 из SberQuAD (validation split, уникальные контексты).

- `needle` — 10 документов с вопросами (одним вопросом на документ, тестовый набор).
- `distractors` — ещё 190 документов без прямого вопроса, добавляются поверх needle,
  чтобы расти 10 -> 50 -> 200 без смены "правильных" документов.
"""
import json
import random

import pandas as pd

random.seed(42)

df = pd.read_parquet("sberquad_val.parquet")

by_ctx = {}
for _, r in df.iterrows():
    ans = r["answers"]
    if len(ans["text"]) == 0:
        continue
    by_ctx.setdefault(r["context"], []).append({
        "question": r["question"],
        "answer": ans["text"][0],
        "answer_start": int(ans["answer_start"][0]),
    })

contexts = list(by_ctx.keys())
# документы разумной длины (не крошечные, не огромные) — обычный абзац статьи
mid = [c for c in contexts if 400 <= len(c) <= 900]
random.shuffle(mid)

needle_contexts = mid[:10]
pool_rest = [c for c in contexts if c not in needle_contexts]
random.shuffle(pool_rest)
distractors_190 = pool_rest[:190]

corpus_200 = []
for i, c in enumerate(needle_contexts):
    corpus_200.append({"id": f"needle-{i+1}", "text": c, "is_needle": True})
for i, c in enumerate(distractors_190):
    corpus_200.append({"id": f"distractor-{i+1}", "text": c, "is_needle": False})

random.shuffle(corpus_200)  # порядок в корпусе не должен совпадать с порядком добавления needle

questions = []
for i, c in enumerate(needle_contexts):
    q = by_ctx[c][0]  # первый вопрос к этому контексту
    doc_id = next(d["id"] for d in corpus_200 if d["text"] == c)
    questions.append({
        "qid": f"q{i+1}",
        "question": q["question"],
        "answer": q["answer"],
        "gold_doc_id": doc_id,
    })

out = {"corpus_200": corpus_200, "questions": questions}
json.dump(out, open("corpus_case1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("corpus size", len(corpus_200), "questions", len(questions))
for q in questions:
    print(" -", q["qid"], q["question"], "->", q["gold_doc_id"], "| answer:", q["answer"])
