#!/usr/bin/env python3
"""Замер №4 (ARCHITECTURE.md §8, SETKA-KEYSOV.md Кейс 2) — согласие моделей между собой.

Вопрос: на одном наборе запросов (сами 30 сканов) — для каждого скана ищем, какой
ДРУГОЙ скан (не дубль, часть (C) case4_full_retrieval_30.py) модель считает ближайшим,
и в какой доле случаев две модели называют разного первого соседа.

Лёгкий случай: nvidia/nemotron-3.5-embed-1b:free vs nvidia/nemotron-3.5-embed-8b:free —
та же архитектурная линия ("nemotron-3.5-embed"), разный размер. 8b нестабильна на
free-tier (C10: 2 случая HTTP 500) — отказы считаются отдельно, не смешиваются с
содержательным несогласием.

Трудный случай: nvidia/nemotron-3.5-embed-1b:free, google/gemini-embedding-2,
cohere/embed-5-fast, mongodb/voyage-multimodal-3.5 — четыре поставщика, разная длина
вектора, попарная таблица несогласия по ВСЕМ C(4,2)=6 парам. Три из четырёх
(gemini/cohere-fast/voyage) имели margin≈0 на C10 (case4_working_mm_results.json) —
ожидаемая находка: они не просто расходятся с рабочими моделями, а почти не совпадают
МЕЖДУ СОБОЙ тоже.

Не делает новых вызовов эмбеддинга — использует кэш raw/originals_<model>.json,
который пишет fetch_originals.py (те же 6 моделей там уже посчитаны для всех 30 сканов).
"""
import itertools
import json
import time

from common_k2 import cosine, load_corpus, load_or_fetch_originals

EASY_PAIR = ["nvidia/nemotron-3.5-embed-1b:free", "nvidia/nemotron-3.5-embed-8b:free"]
HARD_SET = [
    "nvidia/nemotron-3.5-embed-1b:free",
    "google/gemini-embedding-2",
    "cohere/embed-5-fast",
    "mongodb/voyage-multimodal-3.5",
]
ALL_MODELS = list(dict.fromkeys(EASY_PAIR + HARD_SET))  # уникальные, порядок сохранён


def nearest_other(sid, ids, vectors):
    """Ближайший ИНОЙ скан (не сам sid) по cosine среди остальных 29."""
    best, best_score = None, -2.0
    v_sid = vectors.get(sid)
    if v_sid is None:
        return None, None
    for other in ids:
        if other == sid:
            continue
        v_other = vectors.get(other)
        if v_other is None:
            continue
        s = cosine(v_sid, v_other)
        if s > best_score:
            best_score, best = s, other
    return best, best_score


def nn_table(model, ids, vectors):
    """{sid: (nearest_other_id, score)} для одной модели по всем 30 сканам."""
    table = {}
    for sid in ids:
        nn, score = nearest_other(sid, ids, vectors)
        table[sid] = (nn, score)
    return table


def disagreement_rate(table_a, table_b, ids):
    """Доля сканов, где NN-другой у модели A != NN-другой у модели B.
    Скан исключается из знаменателя, если у любой из двух моделей NN не определён
    (отказ эмбеддинга на самом sid или на ВСЕХ остальных 29 — считаем отдельно)."""
    rows = []
    n_comparable = 0
    n_disagree = 0
    for sid in ids:
        nn_a, score_a = table_a[sid]
        nn_b, score_b = table_b[sid]
        comparable = (nn_a is not None and nn_b is not None)
        disagree = comparable and (nn_a != nn_b)
        if comparable:
            n_comparable += 1
            if disagree:
                n_disagree += 1
        rows.append({
            "id": sid,
            "nn_a": nn_a, "score_a": round(score_a, 4) if score_a is not None else None,
            "nn_b": nn_b, "score_b": round(score_b, 4) if score_b is not None else None,
            "comparable": comparable,
            "disagree": disagree if comparable else None,
        })
    rate = round(n_disagree / n_comparable, 4) if n_comparable else None
    return {
        "n_comparable": n_comparable,
        "n_disagree": n_disagree,
        "disagreement_rate": rate,
        "chance_level_disagreement_rate": round(28 / 29, 4),  # 1 - 1/29, см. case4_full_retrieval_30.py part C
        "rows": rows,
    }


def main():
    samples, ids, paths = load_corpus()
    t0 = time.time()

    print("=== загрузка кэша оригиналов (без новых вызовов API) ===")
    vectors_by_model = {}
    fail_by_model = {}
    for model in ALL_MODELS:
        vecs, fails, cost = load_or_fetch_originals(model, ids, paths)
        vectors_by_model[model] = vecs
        fail_by_model[model] = fails
        n_ok = sum(1 for v in vecs.values() if v is not None)
        print(f"  {model}: {n_ok}/{len(ids)} ok, {len(fails)} fail (кэш)")

    print("\n=== строим NN-таблицы (другой скан, не дубль) по каждой модели ===")
    tables = {m: nn_table(m, ids, vectors_by_model[m]) for m in ALL_MODELS}

    # --- лёгкий случай: одна пара, одна архитектурная линия ---
    print(f"\n=== ЛЁГКИЙ СЛУЧАЙ: {EASY_PAIR[0]} vs {EASY_PAIR[1]} ===")
    easy_result = disagreement_rate(tables[EASY_PAIR[0]], tables[EASY_PAIR[1]], ids)
    print(json.dumps({k: v for k, v in easy_result.items() if k != "rows"}, ensure_ascii=False, indent=2))

    # --- трудный случай: все пары из HARD_SET ---
    print(f"\n=== ТРУДНЫЙ СЛУЧАЙ: {HARD_SET} ===")
    hard_pairs = {}
    for a, b in itertools.combinations(HARD_SET, 2):
        key = f"{a} x {b}"
        res = disagreement_rate(tables[a], tables[b], ids)
        hard_pairs[key] = res
        print(f"  {key}: disagreement_rate={res['disagreement_rate']} "
              f"({res['n_disagree']}/{res['n_comparable']})")

    out = {
        "method": "Для каждого из 30 сканов ищем ближайший ДРУГОЙ скан (не сам себя, не "
                   "дубль) среди остальных 29 по cosine оригинального эмбеддинга — часть (C) "
                   "case4_full_retrieval_30.py, перенесённая на пару моделей вместо "
                   "модель-vs-золотой-текстовый-ответ. Доля несогласия = доля сканов, где "
                   "две модели называют РАЗНОГО ближайшего. chance-level при 29 кандидатах "
                   "≈ 28/29 = 0.9655 (вероятность НЕ совпасть при случайном выборе).",
        "easy_case": {"pair": EASY_PAIR, "result": easy_result},
        "hard_case": {"models": HARD_SET, "pairs": hard_pairs},
        "originals_fail_log_by_model": fail_by_model,
        "elapsed_s": round(time.time() - t0, 1),
    }
    json.dump(out, open("raw/agreement_results.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\n=== ЗАМЕР №4 ЗАВЕРШЁН, сохранён в raw/agreement_results.json ===")


if __name__ == "__main__":
    main()
