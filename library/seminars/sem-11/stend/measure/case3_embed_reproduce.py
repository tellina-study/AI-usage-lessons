#!/usr/bin/env python3
"""Семинар 11, Кейс 3 — шаг 0: воспроизвести эмбеддинги корпуса Кейса 3 Семинара 10
(500 документов + 50 вопросов), потому что промежуточный файл с готовыми эмбеддингами
(`corpus_case1_embedded.json`) — локальный несохранённый артефакт замера С10, в
worktree/репозитории его нет (корпус с текстами есть, эмбеддингов при текстах нет).
Без полных векторов невозможно пересчитать RRF-скор с другим весом — скаляр
`vector_rank_of_gold` в `case3-results.json` говорит, на каком месте эталон, но не
говорит, где относительно эталона стоят остальные 499 документов, а это нужно для
honest recall@1 под новым весом.

Переиспользует corpus/corpus_case1.json ИЗ С10 (тот же корпус, 500 документов, тот же
набор вопросов Кейса 3 — файл не правится, только читается) и тот же вебхук
`s10-raw-openrouter` (харнесс С10, `sem-10/stend/sborka.py`), с тем же
`openai/text-embedding-3-small` — ПЕРЕИСПОЛЬЗУЕМ существующий прокси, не создаём новый
сценарий на стенде (своего эмбеддинга этот шаг не требует, только новый вызов через уже
опубликованный вебхук).

Сохраняет `library/seminars/sem-11/stend/raw/case3-embedded-reproduced.json` — большой
файл с векторами, НЕ коммитится (см. .gitignore правило `case*-results.json`, этот файл
называется иначе и будет явно добавлен в .gitignore sem-11, если нужно).
"""
import json
import time
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent.parent.parent / "sem-10" / "stend" / "measure"))
from harness_call import call_raw  # noqa: E402

SEM10 = HERE.parent.parent.parent / "sem-10" / "stend"
EMBED_MODEL = "openai/text-embedding-3-small"


def embed_batch(texts, timeout=120):
    body = {"model": EMBED_MODEL, "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    if "data" not in resp:
        raise RuntimeError(f"embed_batch failed: {json.dumps(resp, ensure_ascii=False)[:500]}")
    vecs = [d["embedding"] for d in resp["data"]]
    usage = resp.get("usage", {})
    return vecs, {"wall_s": r["wall_s"], "cost": usage.get("cost"), "exec_id": r["exec_id"]}


def main():
    data = json.load(open(SEM10 / "corpus" / "corpus_case1.json", encoding="utf-8"))
    corpus = data["corpus_500"]
    q3 = json.load(open(SEM10 / "corpus" / "case3_questions.json", encoding="utf-8"))["questions"]

    texts = [d["text"] for d in corpus]
    BATCH = 25
    all_vecs = []
    cost_total = 0.0
    t0 = time.time()
    exec_ids = []
    for i in range(0, len(texts), BATCH):
        batch = texts[i:i + BATCH]
        vecs, meta = embed_batch(batch)
        all_vecs.extend(vecs)
        cost_total += (meta["cost"] or 0)
        exec_ids.append(meta["exec_id"])
        print(f"batch {i}-{i + len(batch)}: wall={meta['wall_s']}s cost={meta['cost']} exec={meta['exec_id']}")

    for d, v in zip(corpus, all_vecs):
        d["embedding"] = v

    q_texts = [q["question"] for q in q3]
    qvecs, qmeta = embed_batch(q_texts)
    for q, v in zip(q3, qvecs):
        q["embedding"] = v
    cost_total += (qmeta["cost"] or 0)
    exec_ids.append(qmeta["exec_id"])

    elapsed = time.time() - t0
    print(f"TOTAL embed wall={elapsed:.1f}s cost=${cost_total:.6f} "
          f"for {len(texts)} docs + {len(q_texts)} queries, exec_ids={exec_ids}")

    out_path = HERE.parent / "raw" / "case3-embedded-reproduced.json"
    json.dump({"corpus_500": corpus, "questions": q3,
               "embed_meta": {"model": EMBED_MODEL, "total_cost_usd": cost_total,
                               "total_wall_s": elapsed, "n_docs": len(texts),
                               "n_queries": len(q_texts), "exec_ids": exec_ids}},
              open(out_path, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()
