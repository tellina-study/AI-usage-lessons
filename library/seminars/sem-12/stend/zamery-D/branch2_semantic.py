#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — ветка 2: поиск по смыслу описаний.

`openai/text-embedding-3-small` через вебхук стенда `s10-raw-openrouter`
(`harness2.embed_batch`, ключ OpenRouter остаётся на стороне n8n). Забор
результата исполнения вебхука требует `X-N8N-API-KEY` из управляющего API
n8n (`[#351-5]`) — у ЭТОЙ сессии доступ к файлу с ключом есть (в этом
окружении файл называется `~/.n8n-lab.env`, не `~/.n8n-lab-credentials`, но
несёт те же `N8N_API_URL`/`N8N_API_KEY`), поэтому прогон исполняется и
забирается этой же сессией без передачи другой.

Корпус — caption кейса B (как и в ветке 1: вопрос — что находит поиск по
тому, что ЗАПИСАНО). Запросы — RU (модель `text-embedding-3-small`
многоязычна, перевод запроса здесь не нужен — цена языка измеряется только
в ветке 3/SigLIP, чья текстовая башня англоязычна).
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEM10_MEASURE = HERE.parent.parent.parent / "sem-10" / "stend" / "measure"
sys.path.insert(0, str(SEM10_MEASURE))

from harness2 import embed_batch, cosine  # noqa: E402
from corpus_b import load_opisaniya, corpus_ids  # noqa: E402

TEXT_MODEL = "openai/text-embedding-3-small"


def run():
    assert os.environ.get("N8N_API_KEY"), (
        "N8N_API_KEY не задан — перед запуском: `source ~/.n8n-lab.env`")

    op, _ = load_opisaniya()
    ids = corpus_ids()
    captions = [op[i]["caption"] for i in ids]

    queries = json.loads((HERE / "zaprosy_full.json").read_text(encoding="utf-8"))["queries"]
    query_texts = [q["ru"] for q in queries]

    print(f"=== embedding {len(captions)} caption корпуса B ({TEXT_MODEL}, вебхук) ===")
    corpus_vecs_list, corpus_meta = embed_batch(captions, model=TEXT_MODEL)
    corpus_vecs = dict(zip(ids, corpus_vecs_list))
    print(f"  done, wall_s={corpus_meta['wall_s']}, cost={corpus_meta['cost']}")

    print(f"=== embedding {len(query_texts)} запросов (RU, один батч) ===")
    query_vecs_list, query_meta = embed_batch(query_texts, model=TEXT_MODEL)
    print(f"  done, wall_s={query_meta['wall_s']}, cost={query_meta['cost']}")

    n_nonempty_corpus = sum(1 for v in corpus_vecs_list if v)
    n_nonempty_query = sum(1 for v in query_vecs_list if v)
    print(f"=== обязательная часть обхода [#351-5]: корпус {n_nonempty_corpus}/{len(corpus_vecs_list)} "
          f"непустых, запросы {n_nonempty_query}/{len(query_vecs_list)} непустых ===")
    assert n_nonempty_corpus == len(corpus_vecs_list), "пустые векторы корпуса — см. [#351-5] обязательную часть обхода"
    assert n_nonempty_query == len(query_vecs_list), "пустые векторы запросов — см. [#351-5] обязательную часть обхода"

    def nearest(qvec):
        best_id, best_score = None, -2.0
        for cid, cvec in corpus_vecs.items():
            s = cosine(qvec, cvec)
            if s > best_score:
                best_score, best_id = s, cid
        return best_id, best_score

    def top3(qvec):
        scored = [(cid, cosine(qvec, cvec)) for cid, cvec in corpus_vecs.items()]
        scored.sort(key=lambda x: -x[1])
        return scored[:3]

    rows = []
    for q, qvec in zip(queries, query_vecs_list):
        t3 = top3(qvec)
        top_ids = [c for c, _ in t3]
        rows.append({
            "num": q["num"], "class": q["class"], "answer": q["answer"],
            "top3": [(c, round(s, 4)) for c, s in t3],
            "correct_at_1": top_ids[0] == q["answer"],
            "correct_at_3": q["answer"] in top_ids,
        })

    by_class = {}
    for cls in (1, 2, 3):
        cls_rows = [r for r in rows if r["class"] == cls]
        by_class[cls] = {
            "n": len(cls_rows),
            "recall@1": sum(r["correct_at_1"] for r in cls_rows) / len(cls_rows),
            "recall@3": sum(r["correct_at_3"] for r in cls_rows) / len(cls_rows),
        }

    out = {
        "branch": "2_semantic_webhook",
        "model": TEXT_MODEL,
        "call_path": "harness2.embed_batch -> harness_call.call_raw -> вебхук s10-raw-openrouter",
        "n351_5_compliance": {
            "corpus_vectors_total": len(corpus_vecs_list), "corpus_vectors_nonempty": n_nonempty_corpus,
            "query_vectors_total": len(query_vecs_list), "query_vectors_nonempty": n_nonempty_query,
        },
        "timing": {"corpus_embed_wall_s": corpus_meta["wall_s"], "query_embed_wall_s": query_meta["wall_s"]},
        "cost_usd": {
            "corpus_embed_cost": corpus_meta["cost"], "query_embed_cost": query_meta["cost"],
            "total_cost": (corpus_meta["cost"] or 0) + (query_meta["cost"] or 0),
        },
        "n_queries": len(rows),
        "by_class": by_class,
        "overall_recall@1": sum(r["correct_at_1"] for r in rows) / len(rows),
        "overall_recall@3": sum(r["correct_at_3"] for r in rows) / len(rows),
        "details": rows,
    }
    (HERE / "raw" / "branch2_results.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"by_class": by_class, "overall": out["overall_recall@1"],
                       "cost_usd": out["cost_usd"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
