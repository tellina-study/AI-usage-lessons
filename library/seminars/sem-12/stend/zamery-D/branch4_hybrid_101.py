#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — ветка 4: гибрид, слияние рангов формулой RRF (k=60),
зафиксированной до прогона (план §4.1). Основной вариант — ветки 1+3 (слова
+ картинка, план называет именно эту пару); второй вариант — 1+2+3, тем же
проходом бесплатно (не новый прогон модели — только пересчёт по уже
посчитанным рангам трёх веток).

RRF(doc) = Σ 1/(k + rank(doc)), ранг с 1. Отсутствие документа в top-N ветки
(здесь — top3 каждой ветки, то, что сохранено в raw/*) не даёт этой ветке
вклада для документа — честная, а не придуманная трактовка «не попал в
голову списка»."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
K = 60


def load_branch_ranks(path, key="top3", lang=None):
    doc = json.loads(path.read_text(encoding="utf-8"))
    details = doc[lang]["details"] if lang else doc["details"]
    ranks = {}
    for row in details:
        ids = [t[0] if isinstance(t, (list, tuple)) else t for t in row[key]]
        ranks[row["num"]] = ids
    return ranks


def rrf_merge(rank_lists):
    """rank_lists: список словарей {num: [doc_id,...]} — один на ветку.
    Возвращает {num: [(doc_id, rrf_score), ...]} отсортированный по убыванию."""
    nums = set()
    for rl in rank_lists:
        nums |= set(rl.keys())
    merged = {}
    for num in nums:
        scores = {}
        for rl in rank_lists:
            ids = rl.get(num, [])
            for rank_pos, doc_id in enumerate(ids, start=1):
                scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (K + rank_pos)
        merged[num] = sorted(scores.items(), key=lambda x: -x[1])
    return merged


def score_against_queries(merged, queries):
    rows = []
    for q in queries:
        pairs = merged.get(q["num"], [])
        top_ids = [p[0] for p in pairs[:3]]
        rows.append({
            "num": q["num"], "class": q["class"], "answer": q["answer"],
            "top3": pairs[:3],
            "correct_at_1": bool(top_ids) and top_ids[0] == q["answer"],
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
    return rows, by_class


def run():
    queries = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))["queries"]

    b1_ranks = load_branch_ranks(HERE / "raw" / "branch1_results_101.json", key="top3")
    b2_ranks = load_branch_ranks(HERE / "raw" / "branch2_results_101.json", key="top3")
    b3_ranks = load_branch_ranks(HERE / "raw" / "branch3_results_101.json", key="top3", lang="EN")

    merged_13 = rrf_merge([b1_ranks, b3_ranks])
    merged_123 = rrf_merge([b1_ranks, b2_ranks, b3_ranks])

    rows_13, by_class_13 = score_against_queries(merged_13, queries)
    rows_123, by_class_123 = score_against_queries(merged_123, queries)

    out = {
        "branch": "4_hybrid_rrf",
        "k": K,
        "вариант_1_слова_плюс_картинка": {
            "ветки": ["1_lexical", "3_siglip_local(EN)"],
            "by_class": by_class_13,
            "overall_recall@1": sum(r["correct_at_1"] for r in rows_13) / len(rows_13),
            "overall_recall@3": sum(r["correct_at_3"] for r in rows_13) / len(rows_13),
            "details": rows_13,
        },
        "вариант_2_слова_смысл_картинка": {
            "ветки": ["1_lexical", "2_semantic_webhook", "3_siglip_local(EN)"],
            "by_class": by_class_123,
            "overall_recall@1": sum(r["correct_at_1"] for r in rows_123) / len(rows_123),
            "overall_recall@3": sum(r["correct_at_3"] for r in rows_123) / len(rows_123),
            "details": rows_123,
        },
    }
    (HERE / "raw" / "branch4_results_101.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "вариант_1_(1+3)": {"by_class": by_class_13, "overall": out["вариант_1_слова_плюс_картинка"]["overall_recall@1"]},
        "вариант_2_(1+2+3)": {"by_class": by_class_123, "overall": out["вариант_2_слова_смысл_картинка"]["overall_recall@1"]},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
