#!/usr/bin/env python3
"""Расширенный корпус для Кейсов 1 и 3 (issue #311, доп. запрос владельца —
"текущий замер слишком лёгкий"). Та же SberQuAD (validation split), тот же
источник, что исходный `build_corpus.py` — не выдумываем вопросы и тексты,
только иначе их отбираем и добавляем топическую путаницу через реальные,
заранее не подогнанные данные:

1. Пул документов растёт до 500 (было 200) — Кейс 1 получает 4-й размер (500).
2. Среди документов — несколько "confusable clusters": реальные контексты
   SberQuAD, которые делят друг с другом редкую именованную сущность (имя,
   место), найденную эвристикой "заглавное слово не в начале предложения,
   встречается в 2-6 документах пула" — это настоящая топическая близость,
   не сконструированная вручную.
3. Вопросы Кейса 3 — классифицированы (не придуманы) на "лексический разрыв"
   (вопрос и текст почти не делят токенов — выигрышная зона для vector) и
   "точное совпадение" (вопрос несёт число/дату, которое буквально встречается
   в тексте — выигрышная зона для keyword); обе группы представлены заметно.

Запускать из measure/ (читает /tmp/sem10-data/sberquad_val.parquet)."""
import json
import random
import re

import pandas as pd

random.seed(42)

SBERQUAD_PATH = "/tmp/sem10-data/sberquad_val.parquet"
TOTAL_CORPUS_SIZE = 500
CASE1_NEEDLES = 10          # как в v1 — для непрерывности тиров 10/50/200/500
N_CLUSTERS = 8              # confusable-кластеры
CLUSTER_SIZE = 5            # документов на кластер (включая сам gold-документ)
N_CASE3_QUESTIONS = 50

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


CAP_WORD_RE = re.compile(r"[А-ЯЁ][а-яё]{3,}")


def mid_sentence_proper_nouns(text):
    """Заглавные слова, не стоящие в начале текста/предложения — грубый, но
    честный proxy именованной сущности (имя/место), без внешних NER-моделей."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    found = set()
    for sent in sentences:
        words = sent.split()
        for w in words[1:]:  # пропускаем первое слово предложения
            m = CAP_WORD_RE.match(w.strip(",;:()«»\""))
            if m and m.group(0) == w.strip(",;:()«»\"")[:len(m.group(0))]:
                found.add(m.group(0))
    return found


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
print(f"unique contexts={len(contexts)}, mid-length candidates={len(mid)}")

# --- индекс именованных сущностей по всему mid-пулу (для поиска confusable) ---
print("extracting mid-sentence proper nouns (entity proxy) over candidate pool...")
entity_to_ctx = {}
ctx_entities = {}
for c in mid[:2000]:  # ограничиваем пул индексации — достаточно для поиска кластеров
    ents = mid_sentence_proper_nouns(c)
    ctx_entities[c] = ents
    for e in ents:
        entity_to_ctx.setdefault(e, []).append(c)

rare_entities = {e: ctxs for e, ctxs in entity_to_ctx.items() if 2 <= len(ctxs) <= 6}
print(f"rare shared entities found: {len(rare_entities)}")

# --- выбор needle-контекстов Кейса 1 (как в v1, для непрерывности) ---
needle_contexts = mid[:CASE1_NEEDLES]
used = set(needle_contexts)

# --- выбор gold-контекстов для кластеров (не needles, разные сущности) ---
cluster_seed_candidates = [c for c in mid[CASE1_NEEDLES:] if ctx_entities.get(c)]
random.shuffle(cluster_seed_candidates)

clusters = []  # list of {"gold": ctx, "members": [ctx, ...], "entity": e}
tried_entities = set()
for c in cluster_seed_candidates:
    if len(clusters) >= N_CLUSTERS:
        break
    if c in used:
        continue
    cand_entities = [e for e in ctx_entities[c] if e in rare_entities and e not in tried_entities]
    if not cand_entities:
        continue
    e = cand_entities[0]
    siblings = [sc for sc in rare_entities[e] if sc != c and sc not in used]
    if len(siblings) < 1:
        continue
    members = [c] + siblings[: CLUSTER_SIZE - 1]
    clusters.append({"gold": c, "members": members, "entity": e})
    used.update(members)
    tried_entities.add(e)

print(f"confusable clusters built: {len(clusters)} (target {N_CLUSTERS})")
for cl in clusters:
    print(f"  entity={cl['entity']!r} gold+siblings={len(cl['members'])}")

# --- сборка корпуса: needles + cluster members + случайные дистракторы до TOTAL ---
corpus = []
for i, c in enumerate(needle_contexts):
    corpus.append({"id": f"needle-{i+1}", "text": c, "is_needle": True, "topic_cluster": None})

cluster_doc_ids = {}  # ctx text -> doc id (для questions gold_doc_id)
for ci, cl in enumerate(clusters):
    for mi, m in enumerate(cl["members"]):
        doc_id = f"cluster{ci+1}-{mi+1}"
        corpus.append({"id": doc_id, "text": m, "is_needle": False,
                       "topic_cluster": f"cluster{ci+1} (сущность: {cl['entity']})"})
        cluster_doc_ids[m] = doc_id

remaining_pool = [c for c in mid if c not in used]
random.shuffle(remaining_pool)
n_fill = TOTAL_CORPUS_SIZE - len(corpus)
fill = remaining_pool[:n_fill]
for i, c in enumerate(fill):
    corpus.append({"id": f"distractor-{i+1}", "text": c, "is_needle": False, "topic_cluster": None})
    used.add(c)

random.shuffle(corpus)
print(f"TOTAL corpus size: {len(corpus)} (needles={CASE1_NEEDLES}, "
      f"cluster_members={sum(len(cl['members']) for cl in clusters)}, "
      f"random_distractors={len(fill)})")

ctx_to_id = {d["text"]: d["id"] for d in corpus}

# --- вопросы Кейса 1 (как в v1 — по needle-контекстам) ---
case1_questions = []
for i, c in enumerate(needle_contexts):
    q = by_ctx[c][0]
    case1_questions.append({"qid": f"q{i+1}", "question": q["question"], "answer": q["answer"],
                             "gold_doc_id": ctx_to_id[c]})

# --- классификация и выбор вопросов Кейса 3 ---
# Кандидаты: любой документ корпуса (needle, cluster-member, distractor), у которого
# есть хотя бы один реальный вопрос в by_ctx.
candidates = []
for d in corpus:
    qas = by_ctx.get(d["text"])
    if not qas:
        continue
    q = qas[0]
    q_tokens = set(tokenize(q["question"]))
    ctx_tokens = set(tokenize(d["text"]))
    overlap_ratio = len(q_tokens & ctx_tokens) / max(1, len(q_tokens))
    has_number_in_q = bool(re.search(r"\d", q["question"]))
    number_shared = False
    for num in re.findall(r"\d+", q["question"]):
        if num in d["text"]:
            number_shared = True
            break
    # заглавная сущность вопроса, буквально встречающаяся в тексте
    q_caps = set(re.findall(r"[А-ЯЁ][а-яё]{3,}", q["question"]))
    entity_shared = bool(q_caps & (q_caps & set(d["text"].split())))
    lexical_gap = overlap_ratio <= 0.3
    exact_match_favorable = number_shared or (has_number_in_q and overlap_ratio > 0.3)
    cls = "lexical_gap" if lexical_gap else ("exact_match" if exact_match_favorable else "neutral")
    candidates.append({"doc": d, "q": q, "overlap_ratio": round(overlap_ratio, 3), "cls": cls})

lexical_gap_c = [c for c in candidates if c["cls"] == "lexical_gap"]
exact_match_c = [c for c in candidates if c["cls"] == "exact_match"]
neutral_c = [c for c in candidates if c["cls"] == "neutral"]
random.shuffle(lexical_gap_c)
random.shuffle(exact_match_c)
random.shuffle(neutral_c)
print(f"question classes available: lexical_gap={len(lexical_gap_c)}, "
      f"exact_match={len(exact_match_c)}, neutral={len(neutral_c)}")

N_PER_CLASS = N_CASE3_QUESTIONS // 3
picked = lexical_gap_c[:max(N_PER_CLASS, 15)] + exact_match_c[:max(N_PER_CLASS, 15)]
remaining_slots = N_CASE3_QUESTIONS - len(picked)
picked += neutral_c[:max(remaining_slots, 0)]
random.shuffle(picked)
picked = picked[:N_CASE3_QUESTIONS]

case3_questions = []
for i, c in enumerate(picked):
    case3_questions.append({
        "qid": f"c3q{i+1}", "question": c["q"]["question"], "answer": c["q"]["answer"],
        "gold_doc_id": c["doc"]["id"], "lexical_class": c["cls"], "overlap_ratio": c["overlap_ratio"],
    })

cls_counts = {}
for q in case3_questions:
    cls_counts[q["lexical_class"]] = cls_counts.get(q["lexical_class"], 0) + 1
print(f"Кейс 3 вопросы отобраны: {len(case3_questions)}, классы: {cls_counts}")

json.dump({"corpus_500": corpus, "questions": case1_questions,
           "clusters_meta": [{"entity": cl["entity"], "gold": ctx_to_id[cl["gold"]],
                               "members": [ctx_to_id[m] for m in cl["members"]]} for cl in clusters]},
          open("../corpus/corpus_case1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
json.dump({"questions": case3_questions},
          open("../corpus/case3_questions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("saved corpus/corpus_case1.json (corpus_500) and corpus/case3_questions.json")
