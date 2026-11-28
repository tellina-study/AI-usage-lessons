#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Семинар 12, Кейс 3 — КОНТРОЛЬНАЯ ветка «распознать текст + текстовый эмбеддинг».

Зачем: оркестратор указал на методологический изъян в замере «весь кадр против
плиток» (`case3_tiles_vs_whole.py` / `raw/case3_tiles_vs_whole_results.json`) — без
третьей ветки непонятно, провалилась ли сама идея поиска детали или просто инструмент
(картиночная модель CLIP) не читает печатный текст в принципе. Эта ветка — контроль:
те же 60 запросов (30 лёгких + 30 трудных из того же JSON), тот же корпус 30 чеков
CORD, но вместо CLIP-вектора на картинку — текстовый эмбеддинг на РАСПОЗНАННОМ тексте.

Что считается "распознанным текстом":
- для корпуса (30 чеков) — `ocr_text` из `sem-10/stend/corpus/cord_sample_meta.json`
  (полный эталонный OCR чека, уже готов, не гоняем OCR повторно);
- для запроса — `line_text` из `case3_tiles_vs_whole_results.json` (точный текст
  строки-запроса, уже "распознанный" — в этом замере это ground truth OCR-строка,
  именно то, что обычно получает OCR-слой).

Модель: `openai/text-embedding-3-small`, та же, что в Кейсе 1/3 Семинара 10, вызов —
`embed_batch` из `sem-10/stend/measure/harness2.py` через вебхук стенда
`s10-raw-openrouter` (ключ OpenRouter остаётся на стороне n8n).

Алгоритм:
1. embed_batch(30 ocr_text) -> 30 текстовых векторов корпуса (ключ = receipt_id).
2. embed_batch(60 line_text запросов: 30 easy + 30 hard) -> 60 векторов запросов.
3. Для каждого запроса — cosine до всех 30 векторов корпуса, top-1 = предсказанный
   источник, сравнить с source_id -> recall@1, отдельно easy/hard.
4. Сохранить raw/case3_text_control_results.json.
"""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent.resolve()
SEM10_MEASURE = HERE.parent.parent.parent / "sem-10" / "stend" / "measure"
sys.path.insert(0, str(SEM10_MEASURE))

from harness2 import embed_batch, cosine  # noqa: E402

TILES_RESULTS_PATH = HERE / "raw" / "case3_tiles_vs_whole_results.json"
CORD_META_PATH = (HERE.parent.parent.parent / "sem-10" / "stend" / "corpus" / "cord_sample_meta.json")
OUT_PATH = HERE / "raw" / "case3_text_control_results.json"

TEXT_MODEL = "openai/text-embedding-3-small"


def run():
    t0 = time.time()

    tiles_data = json.load(open(TILES_RESULTS_PATH, encoding="utf-8"))
    easy_rows_src = tiles_data["details_easy"]
    hard_rows_src = tiles_data["details_hard"]
    print(f"=== loaded {len(easy_rows_src)} easy + {len(hard_rows_src)} hard queries "
          f"from {TILES_RESULTS_PATH.name} ===")

    meta = json.load(open(CORD_META_PATH, encoding="utf-8"))
    corpus_ids = [m["id"] for m in meta]
    corpus_ocr_texts = [m["ocr_text"] for m in meta]
    print(f"=== loaded {len(corpus_ids)} corpus OCR texts from {CORD_META_PATH.name} ===")

    # ---- Step 1: embed corpus OCR texts (batch) ----
    print(f"=== embedding {len(corpus_ocr_texts)} corpus OCR texts ({TEXT_MODEL}, via webhook) ===")
    corpus_vecs_list, corpus_meta = embed_batch(corpus_ocr_texts, model=TEXT_MODEL)
    corpus_vecs = dict(zip(corpus_ids, corpus_vecs_list))
    print(f"  done, wall_s={corpus_meta['wall_s']}, cost={corpus_meta['cost']}")
    n_calls = 1

    # ---- Step 2: embed 60 query line_texts (batch) ----
    query_texts = [r["line_text"] for r in easy_rows_src] + [r["line_text"] for r in hard_rows_src]
    print(f"=== embedding {len(query_texts)} query line_texts (30 easy + 30 hard, one batch) ===")
    query_vecs_list, query_meta = embed_batch(query_texts, model=TEXT_MODEL)
    print(f"  done, wall_s={query_meta['wall_s']}, cost={query_meta['cost']}")
    n_calls += 1

    n_easy = len(easy_rows_src)
    easy_query_vecs = query_vecs_list[:n_easy]
    hard_query_vecs = query_vecs_list[n_easy:]

    # ---- Step 3: nearest neighbor among 30 corpus text vectors ----
    def nearest(qvec):
        best_id, best_score = None, -2.0
        for cid, cvec in corpus_vecs.items():
            s = cosine(qvec, cvec)
            if s > best_score:
                best_score, best_id = s, cid
        return best_id, best_score

    def score_rows(src_rows, qvecs, label):
        rows = []
        for r, qvec in zip(src_rows, qvecs):
            pred_id, score = nearest(qvec)
            rows.append({
                "source_id": r["source_id"],
                "line_text": r["line_text"],
                "predicted_source": pred_id,
                "cosine": round(score, 4),
                "correct": pred_id == r["source_id"],
            })
        recall = sum(row["correct"] for row in rows) / len(rows)
        print(f"  [{label}] recall@1 = {recall:.4f} ({sum(row['correct'] for row in rows)}/{len(rows)})")
        return rows, recall

    print("=== Part: easy queries (text control) ===")
    easy_rows, recall_easy = score_rows(easy_rows_src, easy_query_vecs, "easy")
    print("=== Part: hard queries (text control) ===")
    hard_rows, recall_hard = score_rows(hard_rows_src, hard_query_vecs, "hard")

    elapsed = time.time() - t0

    out = {
        "purpose": "Семинар 12, Кейс 3 — КОНТРОЛЬНАЯ ветка: распознать текст (OCR, уже готов "
                   "как ground truth) + текстовый эмбеддинг, на ТЕХ ЖЕ 60 запросах (30 "
                   "лёгких + 30 трудных) и том же корпусе 30 чеков CORD, что в "
                   "case3_tiles_vs_whole_results.json. Проверяет: провалилась ли сама идея "
                   "поиска детали, или просто инструмент (CLIP) не читает печатный текст.",
        "date": "2026-11-21",
        "model": TEXT_MODEL,
        "call_path": "harness2.embed_batch -> harness_call.call_raw -> вебхук "
                      "s10-raw-openrouter (ключ OpenRouter на стороне n8n), "
                      "sem-10/stend/measure/harness2.py (импортирован через sys.path, "
                      "файл не копировался и не менялся).",
        "data_sources": {
            "corpus_ocr": "sem-10/stend/corpus/cord_sample_meta.json : ocr_text (эталонный OCR "
                          "всего чека, 30 штук, уже готов)",
            "queries": "zamery-k3/raw/case3_tiles_vs_whole_results.json : details_easy + "
                       "details_hard : line_text (точный текст строки-запроса, уже "
                       "'распознан' — ground truth OCR строки, тот же набор 60 запросов, "
                       "что в замере весь-кадр/плитки, без изменений)",
        },
        "n_calls": {
            "corpus_embed_batch_calls": 1,
            "query_embed_batch_calls": 1,
            "total_webhook_calls": n_calls,
            "n_corpus_texts_embedded": len(corpus_ocr_texts),
            "n_query_texts_embedded": len(query_texts),
        },
        "timing": {
            "total_wall_s": round(elapsed, 1),
            "corpus_embed_wall_s": corpus_meta["wall_s"],
            "query_embed_wall_s": query_meta["wall_s"],
        },
        "cost_usd": {
            "corpus_embed_cost": corpus_meta["cost"],
            "query_embed_cost": query_meta["cost"],
            "total_cost": (corpus_meta["cost"] or 0) + (query_meta["cost"] or 0),
        },
        "summary_recall_at_1": {
            "text_control_recall_at_1_easy": recall_easy,
            "text_control_recall_at_1_hard": recall_hard,
        },
        "details_easy": easy_rows,
        "details_hard": hard_rows,
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\n=== saved to {OUT_PATH} ===")
    print(json.dumps({"summary_recall_at_1": out["summary_recall_at_1"],
                       "timing": out["timing"], "cost_usd": out["cost_usd"]},
                      ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
