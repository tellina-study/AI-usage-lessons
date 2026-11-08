#!/usr/bin/env python3
"""Кейс 2 — ЧЕСТНЫЙ END-TO-END замер (issue #311, доп. фаза по прямому указанию владельца
курса): проверяет не прокси-метрику "разорван ли эталонный спан границей куска"
(`case2_chunking.py`), а итог реального RAG-пайплайна — эмбеддинг вопроса → top-K
retrieval по косинусному сходству среди ВСЕХ кусков ВСЕХ 60 документов корпуса (не
только кусков "своего" документа — иначе тест был бы легче, чем в проде) → LLM-ответ по
top-K кускам → содержит ли финальный ответ модели правильный эталонный ответ.

Гипотеза владельца: если итоговый пайплайн тянет top-K, K>1, кусков, а не ровно один,
то даже "разорванный" на границе куска ответ может целиком дойти до модели через два
соседних извлечённых куска — и разница между версиями нарезки (видимая в прокси-метрике
на K=1) должна СОКРАЩАТЬСЯ при росте K.

Переиспользовано без изменений: 4 функции нарезки (chunk_fixed/chunk_structural/
chunk_word_boundary/chunk_fixed_overlap) и подготовка корпуса (60 документов SberQuAD,
seed=7, offset-фильтр) — буквально та же логика, что в `case2_chunking.py` (сверено
прогоном: тот же n_documents=60, n_questions=72, те же broken-counты 9/1/6/4 на
chunk_size=180). Переиспользован вызов эмбеддинга/LLM и контейнер cosine/contains_answer
из `harness2.py` (та же механика, что Кейс 1) — credential/вебхук `s10-raw-openrouter`,
ключ OpenRouter этим файлом не читается и не печатается.
"""
import concurrent.futures
import json
import os
import random
import re
import time

import numpy as np
import pandas as pd

from harness2 import contains_answer, embed_batch, llm_answer

CHUNK_SIZE = 180  # то же заголовочное значение, что headline-строка прокси-замера
# env-переопределения — ТОЛЬКО для быстрого smoke-теста перед полным прогоном
# (по умолчанию полный замер: все 4 версии x K=[1,2,3,5]); не трогать для финального прогона.
K_VALUES = [int(x) for x in os.environ.get("CASE2_E2E_K", "1,2,3,5").split(",")]
VERSION_FILTER = os.environ.get("CASE2_E2E_VERSIONS")  # например "v1,v2"
EMBED_BATCH_SIZE = 80
MAX_WORKERS_EMBED = 6
MAX_WORKERS_LLM = 12
OUTFILE = os.environ.get("CASE2_E2E_OUTFILE", "case2_e2e_results.json")

# ---------------------------------------------------------------------------
# 1. Корпус — буквально та же подготовка, что в case2_chunking.py (seed=7,
#    >=500 символов, offset-фильтр SberQuAD), сверено прогоном (n_documents=60,
#    n_questions=72, те же broken-counты 9/1/6/4 на chunk_size=180).
# ---------------------------------------------------------------------------
df = pd.read_parquet("sberquad_val.parquet")
by_ctx = {}
n_offset_mismatch = 0
n_offset_total = 0
for _, r in df.iterrows():
    ans = r["answers"]
    if len(ans["text"]) == 0:
        continue
    n_offset_total += 1
    a_start = int(ans["answer_start"][0])
    a_text = ans["text"][0]
    ctx = r["context"]
    if ctx[a_start:a_start + len(a_text)] != a_text:
        n_offset_mismatch += 1
        continue
    by_ctx.setdefault(ctx, []).append({
        "question": r["question"],
        "answer": a_text,
        "answer_start": a_start,
    })

candidates = [(c, qs) for c, qs in by_ctx.items() if len(c) >= 500]
random.seed(7)
random.shuffle(candidates)
sample = candidates[:60]  # [(context, [questions...]), ...], doc_idx = позиция в списке

# ---------------------------------------------------------------------------
# 2. Четыре функции нарезки — буквально скопированы из case2_chunking.py,
#    не переизобретены (владелец: "переиспользуй как есть").
# ---------------------------------------------------------------------------
def chunk_fixed(text, size=CHUNK_SIZE, overlap=0):
    chunks = []
    i = 0
    while i < len(text):
        end = min(i + size, len(text))
        chunks.append((i, end, text[i:end]))
        if end == len(text):
            break
        i += size - overlap
    return chunks


SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_structural(text, target=CHUNK_SIZE):
    sentences = SENT_SPLIT.split(text)
    chunks = []
    pos = 0
    cur_start = 0
    cur_text = ""
    for sent in sentences:
        idx = text.find(sent, pos)
        if idx == -1:
            idx = pos
        s_start, s_end = idx, idx + len(sent)
        if cur_text and len(cur_text) + len(sent) + 1 > target:
            chunks.append((cur_start, pos, cur_text))
            cur_text = sent
            cur_start = s_start
        else:
            if not cur_text:
                cur_start = s_start
            cur_text = (cur_text + " " + sent).strip() if cur_text else sent
        pos = s_end
    if cur_text:
        chunks.append((cur_start, len(text), cur_text))
    return chunks


WORD_SPLIT = re.compile(r"\S+")


def chunk_word_boundary(text, size=CHUNK_SIZE):
    words = list(WORD_SPLIT.finditer(text))
    if not words:
        return [(0, len(text), text)]
    chunks = []
    cur_start = words[0].start()
    cur_end = cur_start
    cur_len = 0
    for m in words:
        w = m.group()
        added = len(w) if cur_len == 0 else len(w) + 1
        if cur_len and cur_len + added > size:
            chunks.append([cur_start, cur_end])
            cur_start = m.start()
            cur_len = len(w)
        else:
            cur_len += added
        cur_end = m.end()
    chunks.append([cur_start, cur_end])
    for i in range(len(chunks) - 1):
        chunks[i][1] = chunks[i + 1][0]
    chunks[-1][1] = len(text)
    return [(s, e, text[s:e]) for s, e in chunks]


def chunk_fixed_overlap(text, size=CHUNK_SIZE, frac=0.15):
    overlap = round(size * frac)
    return chunk_fixed(text, size=size, overlap=overlap)


VERSIONS = {
    "v1": chunk_fixed,
    "v2": chunk_structural,
    "v3": chunk_word_boundary,
    "v4": chunk_fixed_overlap,
}
VERSION_LABELS = {
    "v1": "резать по счёту символов",
    "v2": "резать по границам предложений",
    "v3": "резать по границам слов",
    "v4": "резать по счёту символов с перекрытием",
}
if VERSION_FILTER:
    _keep = set(VERSION_FILTER.split(","))
    VERSIONS = {k: v for k, v in VERSIONS.items() if k in _keep}

# ---------------------------------------------------------------------------
# 3. Лёгкая эвристика по пересечению ключевых слов — запасной, не основной,
#    критерий (см. ниже в разделе проверки ответа). Скопирована из
#    case1_measure.py (тот же токенайзер/стоп-слова, что уже используется на
#    этом стенде для keyword-поиска) — не изобретена заново.
# ---------------------------------------------------------------------------
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
    return [t for t in TOKEN_RE.findall((text or "").lower()) if t not in STOPWORDS and len(t) > 2]


def _covers_span(chunks, a_start, a_end):
    """Покрывает ли СОЮЗ интервалов [start,end) данных кусков весь [a_start, a_end)?
    Куски могут идти не по порядку и перекрываться (v4) — сортируем и мёрджим."""
    if a_end <= a_start:
        return False
    ivs = sorted((c["start"], c["end"]) for c in chunks)
    merged = []
    for s, e in ivs:
        if merged and s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return any(s <= a_start and a_end <= e for s, e in merged)


def lenient_match(model_answer, reference_answer):
    """Запасной критерий: все содержательные (не-стоп) токены эталонного ответа
    присутствуют где-то в ответе модели. Терпимее к перефразированию модели, но
    не "на глаз" — воспроизводимая проверка подмножества токенов."""
    ref_tokens = set(tokenize(reference_answer))
    if not ref_tokens:
        return contains_answer(model_answer, reference_answer)
    model_tokens = set(tokenize(model_answer))
    return ref_tokens.issubset(model_tokens)


# ---------------------------------------------------------------------------
# 4. Вопросы с валидным офсетом (ответ не выходит за пределы контекста) — тот
#    же фильтр, что headline-прогон case2_chunking.py (даёт ровно 72 вопроса).
# ---------------------------------------------------------------------------
all_questions = []  # (doc_idx, q)
for doc_idx, (ctx, qs) in enumerate(sample):
    for q in qs:
        a_start = q["answer_start"]
        a_end = a_start + len(q["answer"])
        if a_end > len(ctx):
            continue
        all_questions.append((doc_idx, {**q, "answer_start": a_start, "answer_end": a_end}))

print(f"[корпус] n_documents={len(sample)} n_questions={len(all_questions)} "
      f"(ожидается 60 / 72, как в case2_chunking.py)")

n_llm_calls = 0
n_embed_calls = 0
n_embed_texts = 0
t_global_start = time.time()

# ---------------------------------------------------------------------------
# 5. Эмбеддинг всех 72 вопросов — ОДИН РАЗ (не зависит от версии нарезки/K).
# ---------------------------------------------------------------------------
question_texts = [q["question"] for _, q in all_questions]
print(f"[эмбеддинг] вопросы: {len(question_texts)} текстов, 1 запрос")
q_vecs, q_meta = embed_batch(question_texts)
n_embed_calls += 1
n_embed_texts += len(question_texts)
Q = np.array(q_vecs, dtype=np.float64)
Q = Q / np.linalg.norm(Q, axis=1, keepdims=True)
print(f"[эмбеддинг] вопросы готовы: shape={Q.shape}, cost={q_meta['cost']}, wall={q_meta['wall_s']}s")

version_results = {}

for vname, chunk_fn in VERSIONS.items():
    print(f"\n=== версия {vname} ({VERSION_LABELS[vname]}) ===")
    # 5а. нарезаем все 60 документов этой версией
    pool = []  # список чанков: {doc_idx, start, end, text}
    for doc_idx, (ctx, _qs) in enumerate(sample):
        for (s, e, t) in chunk_fn(ctx):
            pool.append({"doc_idx": doc_idx, "start": s, "end": e, "text": t})
    print(f"  куски: {len(pool)} (из {len(sample)} документов)")

    # 5б. эмбеддинг всех кусков пачками, параллельно
    texts = [c["text"] for c in pool]
    batches = [texts[i:i + EMBED_BATCH_SIZE] for i in range(0, len(texts), EMBED_BATCH_SIZE)]
    embeds_by_batch = [None] * len(batches)

    def embed_one_batch(i_batch):
        b = batches[i_batch]
        vecs, meta = embed_batch(b)
        return i_batch, vecs, meta

    total_embed_cost = 0.0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_EMBED) as ex:
        futs = [ex.submit(embed_one_batch, i) for i in range(len(batches))]
        for fut in concurrent.futures.as_completed(futs):
            i_batch, vecs, meta = fut.result()
            embeds_by_batch[i_batch] = vecs
            total_embed_cost += (meta.get("cost") or 0.0)
    n_embed_calls += len(batches)
    n_embed_texts += len(texts)
    all_vecs = [v for batch in embeds_by_batch for v in batch]
    assert len(all_vecs) == len(pool), (len(all_vecs), len(pool))
    C = np.array(all_vecs, dtype=np.float64)
    C = C / np.linalg.norm(C, axis=1, keepdims=True)
    print(f"  эмбеддинг кусков: {len(batches)} запросов, cost=${total_embed_cost:.6f}, shape={C.shape}")

    # 5в. cosine sim вопрос x кусок — матрично (локально, без внешнего индекса)
    sims = Q @ C.T  # shape (n_questions, n_chunks)
    topk_idx_all = np.argsort(-sims, axis=1)[:, :max(K_VALUES)]  # top-max(K) на запас

    version_results[vname] = {"pool": pool, "sims": sims, "topk_idx_all": topk_idx_all}

print(f"\n[итог эмбеддингов] запросов={n_embed_calls}, текстов={n_embed_texts}, "
      f"elapsed={time.time()-t_global_start:.1f}s")

# ---------------------------------------------------------------------------
# 6. Для каждой версии x K — собрать top-K контекст, вызвать LLM, проверить
#    финальный ответ. Плюс структурная метрика (без LLM): покрывает ли СОЮЗ
#    top-K извлечённых кусков эталонный спан ответа (мост к прокси-метрике,
#    но на честном retrieval по всему корпусу — не только "своему" документу).
# ---------------------------------------------------------------------------
details = []
summary_rows = []

for vname in VERSIONS:
    pool = version_results[vname]["pool"]
    topk_idx_all = version_results[vname]["topk_idx_all"]

    for K in K_VALUES:
        print(f"\n--- {vname} / K={K} ---")
        tasks = []
        for qi, (doc_idx, q) in enumerate(all_questions):
            idxs = topk_idx_all[qi, :K].tolist()
            retrieved = [pool[j] for j in idxs]
            # контекст для LLM — top-K кусков в порядке ранга, с разделителем,
            # формат как в стаффинге Кейса 1 ("[id] текст" через "---")
            context_text = "\n\n---\n\n".join(
                f"[фрагмент {rank+1}] {c['text']}" for rank, c in enumerate(retrieved)
            )
            # структурная метрика: покрыт ли эталонный спан СОЮЗОМ top-K кусков
            # ИЗ ПРАВИЛЬНОГО документа (кусков из чужих документов быть не может
            # внутри одного документа, поэтому просто берём все куски retrieved,
            # принадлежащие doc_idx, и проверяем покрытие [answer_start, answer_end))
            own_doc_chunks = [c for c in retrieved if c["doc_idx"] == doc_idx]
            covered = _covers_span(own_doc_chunks, q["answer_start"], q["answer_end"]) if own_doc_chunks else False
            gold_doc_retrieved = any(c["doc_idx"] == doc_idx for c in retrieved)
            tasks.append((qi, doc_idx, q, context_text, retrieved, covered, gold_doc_retrieved))

        def run_one(task):
            qi, doc_idx, q, context_text, retrieved, covered, gold_doc_retrieved = task
            r = llm_answer(q["question"], context_text)
            return qi, doc_idx, q, retrieved, covered, gold_doc_retrieved, r

        results_k = [None] * len(tasks)
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_LLM) as ex:
            futs = [ex.submit(run_one, t) for t in tasks]
            for fut in concurrent.futures.as_completed(futs):
                qi, doc_idx, q, retrieved, covered, gold_doc_retrieved, r = fut.result()
                results_k[qi] = (doc_idx, q, retrieved, covered, gold_doc_retrieved, r)
        n_llm_calls += len(tasks)

        n_correct_strict = 0
        n_correct_lenient = 0
        n_covered = 0
        n_gold_doc_retrieved = 0
        total_cost = 0.0
        total_wall = 0.0
        for qi, (doc_idx, q, retrieved, covered, gold_doc_retrieved, r) in enumerate(results_k):
            ok_strict = contains_answer(r["answer"], q["answer"])
            ok_lenient = lenient_match(r["answer"], q["answer"])
            n_correct_strict += ok_strict
            n_correct_lenient += ok_lenient
            n_covered += covered
            n_gold_doc_retrieved += gold_doc_retrieved
            total_cost += (r["cost"] or 0.0)
            total_wall += (r["wall_s"] or 0.0)
            details.append({
                "version": vname, "k": K, "doc_idx": doc_idx,
                "question": q["question"], "reference_answer": q["answer"],
                "model_answer": r["answer"],
                "correct_strict": ok_strict, "correct_lenient": ok_lenient,
                "span_covered_by_topk": covered,
                "gold_doc_in_topk": gold_doc_retrieved,
                "retrieved": [{"doc_idx": c["doc_idx"], "start": c["start"], "end": c["end"]}
                              for c in retrieved],
                "prompt_tokens": r["prompt_tokens"], "cost_usd": r["cost"], "wall_s": r["wall_s"],
                "exec_id": r["exec_id"], "raw_error": r["raw_error"],
            })
        n = len(tasks)
        row = {
            "version": vname, "label": VERSION_LABELS[vname], "k": K, "n_questions": n,
            "accuracy_strict": round(n_correct_strict / n, 4),
            "accuracy_lenient": round(n_correct_lenient / n, 4),
            "span_coverage_rate": round(n_covered / n, 4),
            "gold_doc_retrieved_rate": round(n_gold_doc_retrieved / n, 4),
            "avg_cost_usd": round(total_cost / n, 8),
            "avg_wall_s": round(total_wall / n, 3),
        }
        summary_rows.append(row)
        print(f"  accuracy_strict={row['accuracy_strict']} accuracy_lenient={row['accuracy_lenient']} "
              f"span_coverage={row['span_coverage_rate']} gold_doc_retrieved={row['gold_doc_retrieved_rate']}")

elapsed_total = time.time() - t_global_start
print(f"\n[итог] LLM-вызовов={n_llm_calls}, embedding-вызовов={n_embed_calls} "
      f"(текстов={n_embed_texts}), elapsed={elapsed_total:.1f}s")

out = {
    "method": {
        "corpus": "SberQuAD validation, 60 документов >=500 символов, seed=7, offset-фильтр "
                  "— буквально та же подготовка, что case2_chunking.py (сверено: n_documents=60, "
                  "n_questions=72)",
        "chunk_size_chars": CHUNK_SIZE,
        "k_values": K_VALUES,
        "retrieval": "top-K косинусного сходства ПО ВСЕМУ пулу кусков всех 60 документов "
                     "(не только кусков 'своего' документа) — честный корпус-wide retrieval, "
                     "как в Кейсе 1/3 этого стенда, а не облегчённый тест 'ищем только в своём документе'",
        "embed_model": "openai/text-embedding-3-small (тот же, что Кейс 1)",
        "llm_model": "openai/gpt-4o-mini (тот же, что Кейс 1/3)",
        "correctness_criterion_primary": "accuracy_strict — строгое вхождение эталонного ответа "
                                          "подстрокой в ответ модели (lower+strip), ТА ЖЕ функция "
                                          "harness2.contains_answer, что использует Кейс 1 — для "
                                          "прямой сравнимости чисел на одном стенде",
        "correctness_criterion_secondary": "accuracy_lenient — запасной критерий: все содержательные "
                                            "(не-стоп) токены эталонного ответа — подмножество токенов "
                                            "ответа модели (тот же токенайзер/стоп-слова, что keyword-поиск "
                                            "Кейса 1); логируется для прозрачности, headline-числа — strict",
        "span_coverage_metric": "структурная (без LLM) метрика-мост к прокси-замеру: покрывает ли "
                                 "СОЮЗ top-K извлечённых кусков ИЗ ПРАВИЛЬНОГО документа эталонный "
                                 "символьный спан ответа — 0, если верный документ вообще не попал в top-K",
        "n_llm_calls": n_llm_calls,
        "n_embedding_calls": n_embed_calls,
        "n_embedding_texts": n_embed_texts,
        "elapsed_s": round(elapsed_total, 1),
    },
    "summary": summary_rows,
    "details": details,
}

json.dump(out, open(OUTFILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("\nСводная таблица:")
print(json.dumps(summary_rows, ensure_ascii=False, indent=2))
