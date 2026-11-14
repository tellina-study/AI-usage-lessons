#!/usr/bin/env python3
"""Семинар 11, Кейс 3 — основной замер.

Шаг 1 (сверка воспроизведения): пересобрать keyword_rank/vector_rank/hybrid_rank
(фикс. равный вес RRF, k=60) из `raw/case3-embedded-reproduced.json` ТОЙ ЖЕ функцией,
что `sem-10/stend/measure/case3_measure.py`, и свериться с опубликованным
`sem-10/stend/raw/case3-results.json` (keyword 0.74/0.80, vector 0.86/0.92,
hybrid 0.84/0.94) — если не совпадает, воспроизведение не честное и дальше считать
нельзя.

Шаг 2: классифицировать каждый из 50 вопросов Кейса 3 С10 через `typesafe/jev-1.13`
(OpenRouter `/api/alpha/decisions`, подтверждён прямым вызовом — см.
`case3_jev_classify.py` и `raw/case3-jev-calls.json`) на «точный факт» vs «смысловой
вопрос» — уже сделано отдельным скриптом, результат читается из
`raw/case3-jev-calls.json`.

Шаг 3: пересчитать RRF-скор с весом, подогнанным по классификации jev
(`w_keyword = 0.75` если jev сказал exact_fact, `0.25` если semantic — симметричная
пара, не точечная подгонка под веса, которые дали бы лучший результат постфактум)
против фиксированного равного веса (`w=0.5`, число С10 переиспользуется как baseline,
не пересчитывается).

ВАЖНО про k. RRF С10 использует k=60. Хочет же: веса w/(1-w) применяются
МУЛЬТИПЛИКАТИВНО к каждому терму RRF-суммы (стандартная форма weighted RRF —
`w * 1/(k+rank_kw) + (1-w) * 1/(k+rank_vec)`), без изменения самого k.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
SEM10_MEASURE = HERE.parent.parent.parent / "sem-10" / "stend" / "measure"

# Та же токенизация, что sem-10/stend/measure/case1_measure.py (скопирована буквально,
# не импортирована — исходный модуль при импорте выполняет top-level код, читающий
# несохранённый локальный артефакт замера С10, которого в этом worktree нет).
STOPWORDS = set("и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
                 "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли "
                 "если уже или ни быть был него до вас нибудь опять уж вам сказал ведь там потом "
                 "себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб "
                 "без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой "
                 "совсем ним здесь этом один почти мой тем чтобы нее сейчас были куда зачем всех "
                 "никогда можно при наконец два об другой хоть после над больше тот через эти нас "
                 "про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда "
                 "лучше чуть том нельзя такой им более всегда конечно всю между".split())
TOKEN_RE = re.compile(r"[а-яёa-z0-9]+", re.IGNORECASE)


def tokenize(text):
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS and len(t) > 2]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def keyword_rank(question, corpus):
    q_tokens = set(tokenize(question))
    scored = []
    for doc in corpus:
        d_tokens = set(tokenize(doc["text"]))
        overlap = len(q_tokens & d_tokens)
        scored.append((overlap, doc["id"]))
    scored.sort(key=lambda x: -x[0])
    return [doc_id for _, doc_id in scored]


def vector_rank(qvec, corpus):
    scored = [(cosine(qvec, d["embedding"]), d["id"]) for d in corpus]
    scored.sort(key=lambda x: -x[0])
    return [doc_id for _, doc_id in scored]


def rrf_fuse_weighted(rank_kw, rank_vec, w_kw, k=60):
    """Weighted RRF — стандартная форма (vstash / WRRF-литература, см. research brief
    §2.2): вклад каждого списка умножается на вес до суммирования, k не меняется."""
    scores = {}
    for doc_id, i in zip(rank_kw, range(len(rank_kw))):
        scores[doc_id] = scores.get(doc_id, 0.0) + w_kw * (1.0 / (k + i + 1))
    for doc_id, i in zip(rank_vec, range(len(rank_vec))):
        scores[doc_id] = scores.get(doc_id, 0.0) + (1 - w_kw) * (1.0 / (k + i + 1))
    return sorted(scores.keys(), key=lambda d: -scores[d])


def recall_at_k(ranked_ids, gold_id, k):
    return 1 if gold_id in ranked_ids[:k] else 0


def rank_of(ranked_ids, gold_id):
    return ranked_ids.index(gold_id) + 1 if gold_id in ranked_ids else None


def main():
    data = json.load(open(HERE.parent / "raw" / "case3-embedded-reproduced.json", encoding="utf-8"))
    corpus = data["corpus_500"]
    questions = data["questions"]

    jev_calls = json.load(open(HERE.parent / "raw" / "case3-jev-calls.json", encoding="utf-8"))
    jev_by_qid = {c["qid"]: c for c in jev_calls["calls"]}

    orig = json.load(open(SEM10_MEASURE.parent / "raw" / "case3-results.json", encoding="utf-8"))
    orig_by_qid = {d["qid"]: d for d in orig["details"]}

    W_EXACT = 0.75   # jev сказал "exact_fact" -> keyword получает вес 0.75
    W_SEMANTIC = 0.25  # jev сказал "semantic" -> keyword получает вес 0.25 (vector 0.75)

    results = []
    for q in questions:
        qid = q["qid"]
        gold = q["gold_doc_id"]
        kw_rank = keyword_rank(q["question"], corpus)
        vec_rank = vector_rank(q["embedding"], corpus)

        # сверка воспроизведения против опубликованных С10-рангов
        repro_kw_rank_of_gold = rank_of(kw_rank, gold)
        repro_vec_rank_of_gold = rank_of(vec_rank, gold)
        orig_d = orig_by_qid[qid]

        fixed_hybrid = rrf_fuse_weighted(kw_rank, vec_rank, 0.5)

        jev_call = jev_by_qid.get(qid)
        jev_choice = jev_call["choice"] if jev_call else None
        jev_confidence = jev_call["confidence"] if jev_call else None
        w_kw = W_EXACT if jev_choice == "exact_fact" else (W_SEMANTIC if jev_choice == "semantic" else 0.5)
        dynamic_hybrid = rrf_fuse_weighted(kw_rank, vec_rank, w_kw)

        # "кто реально выиграл" на этом вопросе (операционально, по recall@1 фиксированных keyword/vector)
        kw_win = recall_at_k(kw_rank, gold, 1) == 1
        vec_win = recall_at_k(vec_rank, gold, 1) == 1
        if kw_win and vec_win:
            actual_winner = "both"
        elif kw_win:
            actual_winner = "keyword"
        elif vec_win:
            actual_winner = "vector"
        else:
            actual_winner = "neither"

        jev_predicted_winner = "keyword" if jev_choice == "exact_fact" else ("vector" if jev_choice == "semantic" else None)
        jev_agrees = (
            jev_predicted_winner in ("keyword", "vector")
            and (actual_winner in ("both",) or actual_winner == jev_predicted_winner)
        )

        results.append({
            "qid": qid,
            "question": q["question"],
            "gold_doc_id": gold,
            "lexical_class_heuristic": q.get("lexical_class"),
            "repro_check": {
                "keyword_rank_of_gold_repro": repro_kw_rank_of_gold,
                "keyword_rank_of_gold_orig": orig_d["keyword_rank_of_gold"],
                "vector_rank_of_gold_repro": repro_vec_rank_of_gold,
                "vector_rank_of_gold_orig": orig_d["vector_rank_of_gold"],
                "match": (repro_kw_rank_of_gold == orig_d["keyword_rank_of_gold"]
                           and repro_vec_rank_of_gold == orig_d["vector_rank_of_gold"]),
            },
            "jev": {
                "choice": jev_choice,
                "confidence": jev_confidence,
                "predicted_winner": jev_predicted_winner,
            },
            "actual_winner_at_1": actual_winner,
            "jev_agrees_with_actual_winner": jev_agrees,
            "fixed_w0.5": {
                "rank_of_gold": rank_of(fixed_hybrid, gold),
                "recall@1": recall_at_k(fixed_hybrid, gold, 1),
                "recall@3": recall_at_k(fixed_hybrid, gold, 3),
            },
            "dynamic_jev_weighted": {
                "w_keyword_used": w_kw,
                "rank_of_gold": rank_of(dynamic_hybrid, gold),
                "recall@1": recall_at_k(dynamic_hybrid, gold, 1),
                "recall@3": recall_at_k(dynamic_hybrid, gold, 3),
            },
        })

    n = len(results)
    n_mismatch = sum(1 for r in results if not r["repro_check"]["match"])

    summary = {
        "n_questions": n,
        "corpus_size": len(corpus),
        "reproduction_check": {
            "mismatches_vs_sem10_published": n_mismatch,
            "note": "0 = воспроизведённые keyword_rank_of_gold/vector_rank_of_gold идентичны "
                    "опубликованным sem-10/stend/raw/case3-results.json на всех 50 вопросах",
        },
        "fixed_w0.5_recomputed": {
            "recall@1": round(sum(r["fixed_w0.5"]["recall@1"] for r in results) / n, 3),
            "recall@3": round(sum(r["fixed_w0.5"]["recall@3"] for r in results) / n, 3),
        },
        "fixed_w0.5_sem10_published_baseline": {
            "recall@1": orig["summary"]["hybrid"]["recall@1"],
            "recall@3": orig["summary"]["hybrid"]["recall@3"],
        },
        "dynamic_jev_weighted": {
            "recall@1": round(sum(r["dynamic_jev_weighted"]["recall@1"] for r in results) / n, 3),
            "recall@3": round(sum(r["dynamic_jev_weighted"]["recall@3"] for r in results) / n, 3),
        },
        "jev_classification_vs_lexical_class_heuristic": {
            "agree": sum(1 for r in results if
                         (r["jev"]["choice"] == "exact_fact" and r["lexical_class_heuristic"] == "exact_match") or
                         (r["jev"]["choice"] == "semantic" and r["lexical_class_heuristic"] == "lexical_gap")),
            "n_exact_match_or_lexical_gap": sum(1 for r in results if r["lexical_class_heuristic"] in ("exact_match", "lexical_gap")),
        },
        "jev_agrees_with_actual_winner_at_1": {
            "n_agree": sum(1 for r in results if r["jev_agrees_with_actual_winner"]),
            "n_total_with_clear_winner": sum(1 for r in results if r["actual_winner_at_1"] in ("keyword", "vector", "both")),
        },
        "questions_where_dynamic_worse_than_fixed": [
            r["qid"] for r in results
            if r["dynamic_jev_weighted"]["recall@1"] < r["fixed_w0.5"]["recall@1"]
        ],
        "questions_where_dynamic_better_than_fixed": [
            r["qid"] for r in results
            if r["dynamic_jev_weighted"]["recall@1"] > r["fixed_w0.5"]["recall@1"]
        ],
    }

    out = {"summary": summary, "details": results,
           "weights_used": {"w_keyword_if_jev_exact_fact": W_EXACT, "w_keyword_if_jev_semantic": W_SEMANTIC,
                             "w_keyword_fixed_baseline": 0.5, "rrf_k": 60}}
    out_path = HERE.parent / "case3-results.json"
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"\nsaved {out_path}")


if __name__ == "__main__":
    main()
