#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Семинар 12, Кейс D — ветка 1: поиск по словам описаний (без модели).

Леммы pymorphy3 обеих сторон (запрос и caption-рассказ кейса B), обратный
индекс. Счёт — число совпавших ЛЕММ запроса в документе; при равенстве —
выше документ, у которого совпавшие леммы реже встречаются в корпусе
(больше суммы IDF). Без вызова модели — канон §3.1 С5: модели нет, и это
само написано.

Корпус поиска — caption кейса B (`opisaniya.json`, метод «рассказ»,
`openai/gpt-4o-mini`), НЕ человеческая разметка: вопрос кейса D — что
находит поиск по тому, что ЗАПИСАНО, а разметка — истина для сверки, не
индекс.
"""
import json
import re
from pathlib import Path
from collections import Counter

import pymorphy3

from corpus_b101 import load_opisaniya, corpus_ids

HERE = Path(__file__).resolve().parent
morph = pymorphy3.MorphAnalyzer()

_token_re = re.compile(r"[а-яёa-z]+", re.IGNORECASE)
_lemma_cache = {}

# Служебные части речи (предлоги, союзы, частицы, местоимения) и несколько
# глаголов-связок, которые есть почти в каждом описании («виден», «находиться»)
# — без фильтра они забивают совпадения лемм ложными тай-брейками и портят
# счёт (проверено: без фильтра класс 1 ветки 5 давал 0,417 — ниже честного
# числа 0,583 — из-за лишних документов, деливших верхний счёт на предлогах).
STOPWORD_LEMMAS = {
    "и", "а", "но", "или", "же", "бы", "ли", "да", "то", "это", "этот", "тот",
    "как", "что", "кто", "который", "весь", "один", "два", "некоторый",
    "в", "на", "с", "со", "у", "к", "от", "до", "по", "за", "под", "над",
    "при", "для", "из", "о", "об", "про", "без", "через", "между", "перед",
    "не", "ни", "его", "её", "их", "свой", "наш", "ваш", "себя", "сам",
    "я", "ты", "он", "она", "они", "мы", "вы",
    "быть", "являться", "находиться", "виден", "видный", "видно",
}


def lemmatize(text):
    toks = _token_re.findall(text.lower())
    lemmas = []
    for t in toks:
        if t not in _lemma_cache:
            _lemma_cache[t] = morph.parse(t)[0].normal_form
        lemma = _lemma_cache[t]
        if lemma in STOPWORD_LEMMAS:
            continue
        lemmas.append(lemma)
    return lemmas


def build_index(doc_texts):
    """doc_texts: {id: text}. Возвращает (doc_lemma_sets, df) — df — частота
    леммы по документам (document frequency) для IDF-подобного тай-брейка."""
    doc_lemma_sets = {}
    df = Counter()
    for doc_id, text in doc_texts.items():
        lemmas = set(lemmatize(text))
        doc_lemma_sets[doc_id] = lemmas
        for l in lemmas:
            df[l] += 1
    return doc_lemma_sets, df


def rank(query_text, doc_lemma_sets, df, n_docs):
    q_lemmas = set(lemmatize(query_text))
    scored = []
    for doc_id, d_lemmas in doc_lemma_sets.items():
        matched = q_lemmas & d_lemmas
        n_match = len(matched)
        # тай-брейк: сумма редкости совпавших лемм (выше — у более редких)
        rarity = sum(1.0 / df[l] for l in matched) if matched else 0.0
        scored.append((doc_id, n_match, rarity))
    scored.sort(key=lambda x: (-x[1], -x[2]))
    return scored, sorted(q_lemmas)


def run():
    op, _ = load_opisaniya()
    ids = corpus_ids()
    captions = {i: op[i]["caption"] for i in ids}
    doc_lemma_sets, df = build_index(captions)

    queries = json.loads((HERE / "zaprosy_101.json").read_text(encoding="utf-8"))["queries"]

    rows = []
    for q in queries:
        scored, q_lemmas = rank(q["ru"], doc_lemma_sets, df, len(ids))
        top_ids = [s[0] for s in scored[:3]]
        rows.append({
            "num": q["num"], "class": q["class"], "answer": q["answer"],
            "query_lemmas": q_lemmas,
            "n_matched_top1": scored[0][1],
            "top3": top_ids,
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
        "branch": "1_lexical",
        "описание": "pymorphy3-леммы, обратный индекс, без модели; индекс строится по caption (рассказ) кейса B",
        "n_queries": len(rows),
        "by_class": by_class,
        "overall_recall@1": sum(r["correct_at_1"] for r in rows) / len(rows),
        "overall_recall@3": sum(r["correct_at_3"] for r in rows) / len(rows),
        "details": rows,
    }
    (HERE / "raw" / "branch1_results_101.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"by_class": by_class, "overall": out["overall_recall@1"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
