#!/usr/bin/env python3
"""issue #311 — точечная пересборка ТОЛЬКО 10 needle-вопросов Кейса 1.

Проблема (владелец курса): все 10 текущих вопросов Кейса 1 — почти дословные
пересечения с текстом золотого документа (overlap_ratio 0.29-1.00), поэтому
keyword-поиск выигрывает тривиально и recall@1=1.0 везде не показывает ничего
содержательного. Кейс 3 этого же занятия уже решил эту проблему через
классификацию вопросов по overlap_ratio (`build_corpus_v2.py`) — этот скрипт
переиспользует ТУ ЖЕ формулу/токенизацию/пороги для ВЫБОРА новых 10
needle-пар, не трогая 490 документов Кейса 3 (confusable clusters +
дистракторы) и не запуская build_corpus_v2.py заново.

Пул кандидатов: контексты SberQuAD validation длиной 350-1100 символов,
которых НЕТ среди текстов, уже присутствующих в corpus_500 (сверка по
точному тексту). Тот же random.seed(42), тот же порядок операций
(построить mid -> shuffle mid), что в build_corpus_v2.py, — пул кандидатов
другой (уже занятые 500 текстов исключены), поэтому конкретные выбранные
тексты неизбежно другие, это ожидаемо.

Пишет ../corpus/corpus_case1.json (490 документов и clusters_meta —
побайтово как было; заменяются только 10 is_needle=true записей и весь
массив questions). Каждый новый вопрос получает lexical_class/overlap_ratio
— то же поле, что уже есть у вопросов Кейса 3 (case3_questions.json)."""
import json
import random
import re

import pandas as pd

random.seed(42)

SBERQUAD_PATH = "/tmp/sem10-data/sberquad_val.parquet"
CORPUS_PATH = "../corpus/corpus_case1.json"

TOKEN_RE = re.compile(r"[а-яёa-z0-9]+", re.IGNORECASE)
STOPWORDS = set("и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
                 "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли "
                 "если уже или ни быть был него до вас нибудь опять уж вам сказал ведь там потом "
                 "себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб "
                 "без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой "
                 "совсем ним здесь этом один почти мой тем чтобы нее сейчас были куда зачем всех "
                 "никогда можно при наконец два об другой хоть после над больше тот через эти нас "
                 "про всего них какая много разве три эту моя впрочем хорошо свою этой перед иногда "
                 "лучше чуть том нельзя такой им более всегда конечно всю между".split())


def tokenize(text):
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS and len(t) > 2]


def classify(question, ctx_text):
    q_tokens = set(tokenize(question))
    ctx_tokens = set(tokenize(ctx_text))
    overlap_ratio = len(q_tokens & ctx_tokens) / max(1, len(q_tokens))
    has_number_in_q = bool(re.search(r"\d", question))
    number_shared = any(num in ctx_text for num in re.findall(r"\d+", question))
    lexical_gap = overlap_ratio <= 0.3
    exact_match_favorable = number_shared or (has_number_in_q and overlap_ratio > 0.3)
    cls = "lexical_gap" if lexical_gap else ("exact_match" if exact_match_favorable else "neutral")
    return round(overlap_ratio, 3), cls


print("loading existing corpus_case1.json (to exclude already-used texts)...")
existing = json.load(open(CORPUS_PATH, encoding="utf-8"))
existing_texts = {d["text"] for d in existing["corpus_500"]}
assert len(existing_texts) == 500, f"expected 500 existing texts, got {len(existing_texts)}"

print("loading SberQuAD validation split...")
df = pd.read_parquet(SBERQUAD_PATH)
by_ctx = {}
for _, r in df.iterrows():
    ans = r["answers"]
    if len(ans["text"]) == 0:
        continue
    by_ctx.setdefault(r["context"], []).append({
        "question": r["question"], "answer": ans["text"][0], "answer_start": int(ans["answer_start"][0]),
    })

contexts = list(by_ctx.keys())
mid = [c for c in contexts if 350 <= len(c) <= 1100]
random.shuffle(mid)
pool = [c for c in mid if c not in existing_texts]
print(f"unique contexts={len(contexts)}, mid-length={len(mid)}, pool (excl. existing 500)={len(pool)}")

candidates = []
for c in pool:
    q = by_ctx[c][0]
    overlap_ratio, cls = classify(q["question"], c)
    candidates.append({"ctx": c, "q": q, "overlap_ratio": overlap_ratio, "cls": cls})

lexical_gap_c = [c for c in candidates if c["cls"] == "lexical_gap"]
exact_match_c = [c for c in candidates if c["cls"] == "exact_match"]
neutral_c = [c for c in candidates if c["cls"] == "neutral"]
random.shuffle(lexical_gap_c)
random.shuffle(exact_match_c)
random.shuffle(neutral_c)
print(f"classes in pool: lexical_gap={len(lexical_gap_c)}, exact_match={len(exact_match_c)}, "
      f"neutral={len(neutral_c)}")

# --- ручной отбор 10 (4 lexical_gap / 3 exact_match / 3 neutral), по индексам
# в детерминированно перемешанных списках выше. Отобраны вручную из первых
# 10 каждого класса (см. measure/explore_needle_pool.py вывод) — пропущены
# вопросы с висящим анафорическим "она"/"этого" без антецедента в самой
# формулировке (например lexical_gap[0] "Что стало следствием этого?" и
# lexical_gap[4] "Кем она приходилась?" — плохие needle-вопросы сами по
# себе, по смыслу, не по классу) и exact_match[4] (вопрос содержит
# "Устава 1928 года", а контекст — "Уставе 1828 года": несовпадение цифр
# в самом датасете SberQuAD, не берём этот кандидат).
picks = [
    ("lexical_gap", lexical_gap_c[1], "Как называется круг кровообращения"),
    ("exact_match", exact_match_c[1], "Сколько длилось путешествие Моцарта"),
    ("neutral", neutral_c[3], "Какая температура летом"),
    ("lexical_gap", lexical_gap_c[2], "В каком году была возрождена дискуссия"),
    ("exact_match", exact_match_c[6], "Какому розыгрышу Кубка мира"),
    ("neutral", neutral_c[6], "В чем заключается функция митохондрий"),
    ("lexical_gap", lexical_gap_c[3], "Кровью каких животных"),
    ("exact_match", exact_match_c[8], "Какая страна в 2001 году"),
    ("neutral", neutral_c[9], "Какая структура управляет Центральным банком"),
    ("lexical_gap", lexical_gap_c[6], "Как звали ученого"),
]

for cls_expected, cand, expected_prefix in picks:
    assert cand["cls"] == cls_expected, f"class mismatch: {cand['q']['question']!r} is {cand['cls']}"
    assert cand["q"]["question"].startswith(expected_prefix), (
        f"pool drift detected: expected question starting {expected_prefix!r}, "
        f"got {cand['q']['question']!r} — re-run measure/explore_needle_pool.py and re-pick indices")

# защита от дублей внутри выбранных 10 и от пересечения с уже занятыми 500 текстами
chosen_ctxs = [p[1]["ctx"] for p in picks]
assert len(set(chosen_ctxs)) == 10, "duplicate contexts among the 10 picks"
assert not (set(chosen_ctxs) & existing_texts), "a pick collides with an already-used corpus_500 text"

# --- применяем: заменяем is_needle=true записи (id/is_needle/topic_cluster неизменны) ---
needle_ids_in_order = [d["id"] for d in existing["corpus_500"] if d["is_needle"]]
assert sorted(needle_ids_in_order, key=lambda s: int(s.split("-")[1])) == [
    f"needle-{i}" for i in range(1, 11)]
id_to_new_text = {f"needle-{i+1}": picks[i][1]["ctx"] for i in range(10)}

for d in existing["corpus_500"]:
    if d["is_needle"]:
        d["text"] = id_to_new_text[d["id"]]
        # is_needle / topic_cluster остаются как были (True / None)

# --- новые вопросы q1..q10, привязанные к needle-N по порядку picks ---
new_questions = []
for i, (cls, cand, _) in enumerate(picks):
    gold_id = f"needle-{i+1}"
    new_questions.append({
        "qid": f"q{i+1}",
        "question": cand["q"]["question"],
        "answer": cand["q"]["answer"],
        "gold_doc_id": gold_id,
        "lexical_class": cls,
        "overlap_ratio": cand["overlap_ratio"],
    })
existing["questions"] = new_questions

cls_counts = {}
for q in new_questions:
    cls_counts[q["lexical_class"]] = cls_counts.get(q["lexical_class"], 0) + 1
print(f"needle classes: {cls_counts}")
for q in new_questions:
    print(f"  {q['qid']} -> {q['gold_doc_id']} [{q['lexical_class']} overlap={q['overlap_ratio']}] "
          f"Q={q['question']!r} A={q['answer']!r}")

json.dump(existing, open(CORPUS_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"saved {CORPUS_PATH}")
