#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — не потолок, а ПЯТАЯ, диагностическая ветка: поиск по
РУКОПИСНОЙ РАЗМЕТКЕ (`what_is_visible`, человек) вместо caption модели.

Названо неверно в первой версии этого файла («потолок класса 1») — поправка
по разбору оркестратора: величина, которую реальная ветка 1 (1,000 на
классе 1) ПРЕВОСХОДИТ, не может называться потолком — потолок не превышают.
Это результат альтернативного индекса (человеческая разметка вместо
caption), тем же алгоритмом (лемма-поиск ветки 1), и он НИЖЕ ветки 1 на
классе 1 (0,583 против 1,000) — не выше и не ограничивает её.

Почему он ниже: запросы класса 1 намеренно переписаны правкой кейса B под
СЛОВО МОДЕЛИ («флипчарт»), а человек тот же предмет на той же фотографии
называет иначе («доска», `zamery-B/zaprosy-klass1-finalizirovano.md` §2.1).
Индекс и запрос обязаны говорить на одном языке; эта ветка говорит на языке
человека, а запрос — на языке модели, и теряет на несовпадении. Находка, не
поломка счёта.

Классы 2-3 здесь не ветка поиска (словесный поиск по разметке для них не
осмыслен — класс 2 намеренно использует другие слова, класс 3 — деталь, не
записанную ни в чьём описании): для них — только машинная перепроверка
единственности ответа через группы `razmetka.json` (обязанность замера,
zaprosy-B.md строка 6), не пятая ветка.
"""
import json
from pathlib import Path

from corpus_b101 import load_razmetka, corpus_ids
from branch1_lexical import lemmatize, build_index, rank

HERE = Path(__file__).resolve().parent


def ground_truth_text(entry):
    return " ".join(entry["what_is_visible"])


def branch5_class1(queries, rz, ids):
    gt_texts = {i: ground_truth_text(rz[i]) for i in ids}
    doc_lemma_sets, df = build_index(gt_texts)
    rows = []
    for q in queries:
        if q["class"] != 1:
            continue
        scored, _ = rank(q["ru"], doc_lemma_sets, df, len(ids))
        top_score = scored[0][1]
        tied = [s for s in scored if s[1] == top_score]
        correct = scored[0][0] == q["answer"] and len(tied) == 1
        rows.append({"num": q["num"], "top1_by_gt": scored[0][0], "answer": q["answer"],
                      "n_tied_at_top": len(tied), "correct_at_1": correct})
    return rows


def group_consistency_check(queries, rz):
    """Для классов 2-3: ответ и трудные негативы — одна группа? Есть ли В ТОЙ
    ЖЕ группе документы, не названные трудными негативами (значит планировщик
    либо не нашёл их, либо не счёл похожими — проверяется глазами, не правится
    этим скриптом)."""
    group_members = {}
    for doc_id, e in rz.items():
        group_members.setdefault(e["group"], []).append(doc_id)

    rows = []
    for q in queries:
        if q["class"] == 1:
            continue
        ans_group = rz[q["answer"]]["group"]
        same_group = set(group_members.get(ans_group, [])) - {q["answer"]}
        # Запросы добора (круг 3) не объявляют трудные негативы ПОШТУЧНО: они
        # объявлены на уровне ГРУППЫ в `zamery-B/otbor-dobora.json`. Сверка
        # «объявленные против фактических» применима только к кругу 1.
        if "hard_negatives" not in q:
            continue
        declared = set(q["hard_negatives"])
        unnamed_in_group = same_group - declared
        rows.append({
            "num": q["num"], "answer": q["answer"], "group": ans_group,
            "hard_negatives_in_same_group": sorted(declared & same_group),
            "hard_negatives_other_group": sorted(declared - same_group),
            "group_members_not_declared_as_hard_negative": sorted(unnamed_in_group),
        })
    return rows


def run():
    rz = load_razmetka()
    ids = corpus_ids()
    queries = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))["queries"]

    c1_rows = branch5_class1(queries, rz, ids)
    c1_recall = sum(r["correct_at_1"] for r in c1_rows) / len(c1_rows)

    gc_rows = group_consistency_check(queries, rz)
    n_clean = sum(1 for r in gc_rows if not r["group_members_not_declared_as_hard_negative"]
                  and not r["hard_negatives_other_group"])

    out = {
        "описание": "Ветка 5 (диагностическая): поиск по рукописной разметке, не по caption. "
                     "НЕ потолок — результат альтернативного индекса тем же алгоритмом ветки 1. "
                     "Ниже ветки 1 на классе 1 (0,583 против 1,000): запрос переписан под слово "
                     "модели, разметка говорит словом человека — несовпадение языка индекса и запроса.",
        "класс_1_ветка5_recall@1_по_рукописной_разметке": c1_recall,
        "класс_1_детали": c1_rows,
        "классы_2_3_группы_без_расхождения_из": f"{n_clean}/{len(gc_rows)}",
        "классы_2_3_детали": gc_rows,
    }
    (HERE / "raw" / "branch5_results_101.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"ветка 5 (поиск по разметке), класс 1 recall@1: {c1_recall:.3f} "
          f"({sum(r['correct_at_1'] for r in c1_rows)}/{len(c1_rows)}) — "
          f"НИЖЕ ветки 1 по caption (1,000), не потолок")
    print(f"классы 2-3, группы без расхождения: {n_clean}/{len(gc_rows)}")
    for r in gc_rows:
        if r["hard_negatives_other_group"] or r["group_members_not_declared_as_hard_negative"]:
            print("  расхождение:", r["num"], r)
    wrong_c1 = [r for r in c1_rows if not r["correct_at_1"]]
    if wrong_c1:
        print("\nкласс 1, ветка 5 промахи (читать глазами, канон §8.12):")
        for r in wrong_c1:
            print(" ", r["num"], "top1_by_gt=", r["top1_by_gt"], "answer=", r["answer"], "tied=", r["n_tied_at_top"])


if __name__ == "__main__":
    run()
