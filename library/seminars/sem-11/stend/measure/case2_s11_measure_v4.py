#!/usr/bin/env python3
"""Семинар 11, Кейс 2 — продвинутый чанкинг. ЧЕТВЁРТАЯ версия (v4), добавленная ПОСЛЕ
v1/v2/v3 (`case2_s11_measure.py`, уже прогнан и записан в `case2-s11-results.json`), на
ТОЧНО ТОМ ЖЕ корпусе и тех же 72 вопросах — вопрос владельца курса: «где чанкинг, который
сам подстраивается, как резать по абзацу, нескольким предложениям или словам?».

Это настоящая **рекурсивная/самоподстраивающаяся резка по сепараторам** — каноническая
техника `RecursiveCharacterTextSplitter` (LangChain): пробует разделители по убыванию
размера (абзац -> строка -> предложение -> слово -> символ) и переходит к БОЛЕЕ МЕЛКОМУ
разделителю ТОЛЬКО если кусок после разделения текущим уровнем всё ещё превышает целевой
размер. Библиотека `langchain-text-splitters` недоступна в этом окружении (pip install
отказал — externally-managed-environment, без доступа на системную установку в общем
стенде нескольких параллельных сессий) — алгоритм реализован самостоятельно, порт той же
логики (расщепление уровня -> жадная упаковка "хороших" кусочков -> рекурсия в более
мелкий уровень ТОЛЬКО для кусочков, которые сами превысили target), не её описание.

ОТДЕЛЬНАЯ ось от v2 (иерархическая/parent-document) и v3 (семантическая по порогу разрыва
эмбеддингов) — v4 ничего не знает про родителей и не вызывает эмбеддинг для самой резки
(эмбеддинг вызывается один раз, как и для v1, только чтобы найти top-1 кусок в поиске).

Честная методическая оговорка, обязательная к переносу в главу: документы SberQuAD в этом
корпусе — однопараграфные выдержки Википедии, **без единого `\\n\\n` или `\\n`** (проверено
по всем 60 документам выборки). Значит первые два уровня рекурсии (абзац, строка) на этом
корпусе НИКОГДА не применяются — рекурсия реально работает только на уровне
предложение -> слово (-> символ, если слово само длиннее target, что для русского текста
не встретилось). Это не брешь в реализации, а честное свойство ДАННЫХ: настоящий эффект
"абзац -> предложения -> слова" раскроется на документах с реальной параграфной
структурой (регламенты, многостраничные инструкции), не на коротких энциклопедических
абзацах — тот же класс ограничения, что уже назван для v2 ("родитель = документ целиком,
естественного третьего уровня иерархии здесь нет").

Цель размера (target=180) взята РОВНО ТОЙ ЖЕ, что CHUNK_SIZE_V1 — единственная переменная,
которая меняется между v1 и v4, это САМ АЛГОРИТМ резки (копит предложения до target, не
трогая кусок, который сам превысил target VS копит предложения до target, а если
отдельное предложение само больше target — рекурсивно дробит его на слова), не размер.
Это самое честное прямое сравнение "флэт резка по предложениям" vs "рекурсивная резка" на
одном стенде.

Инфраструктура и метрика — переиспользованы без изменений из `case2_s11_measure.py`:
корпус (seed=7, offset-фильтр, 60 документов/72 вопроса), вебхук `s10-raw-openrouter`,
`harness2.embed_batch/llm_answer/contains_answer`, K=1, accuracy_strict/
answer_intact_rate/gold_doc_retrieved_rate. v4 — версия "direct" (как v1/v3), не
"parent" (как v2): найденный top-1 кусок отдаётся модели как есть, без подстановки
родителя.
"""
import concurrent.futures
import json
import random
import re
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd

_SEM10_MEASURE = Path(__file__).resolve().parent.parent.parent.parent / "sem-10" / "stend" / "measure"
if str(_SEM10_MEASURE) not in sys.path:
    sys.path.insert(0, str(_SEM10_MEASURE))

from harness2 import contains_answer, embed_batch, llm_answer

CHUNK_SIZE_V1 = 180  # буквально та же константа, что case2_s11_measure.py — единственная
                      # общая ось сравнения v1 vs v4 — РАЗМЕР, не алгоритм
MAX_WORKERS_EMBED = 6
MAX_WORKERS_LLM = 12
OUTFILE = "case2-s11-results-v4.json"  # отдельный файл v4; слияние в основной
                                        # case2-s11-results.json — отдельным скриптом ниже

# ---------------------------------------------------------------------------
# 1. Корпус — буквально та же подготовка, что case2_s11_measure.py (seed=7, offset-фильтр,
#    SberQuAD >=500 символов). Проверка 60/72 перед тратой реальных API-вызовов.
# ---------------------------------------------------------------------------
df = pd.read_parquet("sberquad_val.parquet")
by_ctx = {}
for _, r in df.iterrows():
    ans = r["answers"]
    if len(ans["text"]) == 0:
        continue
    a_start = int(ans["answer_start"][0])
    a_text = ans["text"][0]
    ctx = r["context"]
    if ctx[a_start:a_start + len(a_text)] != a_text:
        continue
    by_ctx.setdefault(ctx, []).append({
        "question": r["question"],
        "answer": a_text,
        "answer_start": a_start,
    })

candidates = [(c, qs) for c, qs in by_ctx.items() if len(c) >= 500]
random.seed(7)
random.shuffle(candidates)
sample = candidates[:60]

all_questions = []
for doc_idx, (ctx, qs) in enumerate(sample):
    for q in qs:
        a_start = q["answer_start"]
        a_end = a_start + len(q["answer"])
        if a_end > len(ctx):
            continue
        all_questions.append((doc_idx, {**q, "answer_start": a_start, "answer_end": a_end}))

print(f"[корпус] n_documents={len(sample)} n_questions={len(all_questions)} "
      f"(контроль верности воспроизведения v1-v3: ожидается 60/72)")
assert len(sample) == 60, "корпус не совпадает с v1-v3 — проверить seed/фильтр"
assert len(all_questions) == 72, "вопросы не совпадают с v1-v3 — проверить фильтр офсетов"

# честная проверка методической оговорки docstring'а — считается РЕАЛЬНО, не заявляется
n_docs_with_para = sum(1 for ctx, _ in sample if "\n\n" in ctx)
n_docs_with_line = sum(1 for ctx, _ in sample if "\n" in ctx)
print(f"[оговорка] документов с '\\n\\n': {n_docs_with_para}/60, с '\\n': {n_docs_with_line}/60 "
      f"(0/60 ожидается — однопараграфные выдержки; первые 2 уровня рекурсии на этом корпусе "
      f"не применяются ни разу)")

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")

# ---------------------------------------------------------------------------
# 2. v4 — настоящая рекурсивная/самоподстраивающаяся резка по сепараторам.
#    Уровни по убыванию размера: 0=абзац(\n\n) -> 1=строка(\n) -> 2=предложение(SENT_SPLIT,
#    та же регулярка, что v1/v2/v3 — граница предложения одинакова во ВСЕХ версиях,
#    различие изолировано к самой СТРАТЕГИИ резки) -> 3=слово(' ') -> 4=символ (гарантия
#    терминации: кусок из 1 символа всегда <= target, если target>=1).
# ---------------------------------------------------------------------------
LEVEL_NAME = {0: "абзац", 1: "строка", 2: "предложение", 3: "слово", 4: "символ"}
LEVEL_JOINER = {0: "\n\n", 1: "\n", 2: " ", 3: " ", 4: ""}
N_LEVELS = 5
recursion_level_hits = {k: 0 for k in range(N_LEVELS)}  # на каком уровне разделитель
                                                          # реально встретился в тексте (не
                                                          # заявлено — посчитано)
recursion_level_used_for_oversized = {k: 0 for k in range(N_LEVELS)}  # на каком уровне
    # кусок САМ превысил target и пришлось рекурсивно дробить его мельче — это и есть
    # механика, которой v1 не имеет вовсе


def _split_level(text, level):
    if level == 0:
        parts = re.split(r"\n\n+", text)
    elif level == 1:
        parts = text.split("\n")
    elif level == 2:
        parts = SENT_SPLIT.split(text)
    elif level == 3:
        parts = text.split(" ")
    else:
        parts = list(text)
    return [p for p in parts if p != ""]


def _pack_greedy(pieces, target, joiner):
    """Жадная упаковка кусочков уровня в чанки <= target, без overlap — тот же приём, что
    chunk_structural (v1) использует для предложений, обобщённый на любой уровень."""
    chunks = []
    cur = []
    cur_len = 0
    for p in pieces:
        extra = len(p) + (len(joiner) if cur else 0)
        if cur and cur_len + extra > target:
            chunks.append(joiner.join(cur))
            cur = [p]
            cur_len = len(p)
        else:
            cur.append(p)
            cur_len += extra
    if cur:
        chunks.append(joiner.join(cur))
    return chunks


def recursive_split(text, target, level=0):
    if level >= N_LEVELS:
        return [text]
    pieces = _split_level(text, level)
    if len(pieces) <= 1:
        # разделитель этого уровня не встретился в тексте вовсе (например, нет "\n\n" в
        # документе SberQuAD) — пробуем следующий, более мелкий уровень
        return recursive_split(text, target, level + 1)
    recursion_level_hits[level] += 1
    good, out = [], []
    joiner = LEVEL_JOINER[level]
    for p in pieces:
        if len(p) <= target:
            good.append(p)
        else:
            recursion_level_used_for_oversized[level] += 1
            if good:
                out.extend(_pack_greedy(good, target, joiner))
                good = []
            out.extend(recursive_split(p, target, level + 1))
    if good:
        out.extend(_pack_greedy(good, target, joiner))
    return out


def chunk_recursive_with_spans(text, target):
    """Превращает плоский список текстов кусков (в порядке документа) в (start, end, text)
    тем же приёмом, что split_sentences_with_spans/chunk_structural уже использует в
    case2_s11_measure.py: find() от текущей позиции вперёд, с откатом на полный поиск."""
    texts = [t for t in recursive_split(text, target, level=0) if t != ""]
    out = []
    pos = 0
    n_fallback = 0
    for t in texts:
        idx = text.find(t, pos)
        if idx == -1:
            idx = text.find(t)
            n_fallback += 1
        if idx == -1:
            idx = pos
        s_start, s_end = idx, idx + len(t)
        out.append((s_start, s_end, t))
        pos = max(pos, s_end)
    return out, n_fallback


print(f"\n[v4] рекурсивная/самоподстраивающаяся резка по сепараторам (target={CHUNK_SIZE_V1}, "
      f"уровни: абзац->строка->предложение->слово->символ)")
v4_pool = []
n_fallback_total = 0
for doc_idx, (ctx, _qs) in enumerate(sample):
    chunks, n_fb = chunk_recursive_with_spans(ctx, CHUNK_SIZE_V1)
    n_fallback_total += n_fb
    for (s, e, t) in chunks:
        v4_pool.append({"doc_idx": doc_idx, "start": s, "end": e, "text": t})
chunk_lens = [len(c["text"]) for c in v4_pool]
print(f"  кусков: {len(v4_pool)} (из {len(sample)} документов), "
      f"средний размер {np.mean(chunk_lens):.1f} символов, max={max(chunk_lens)}")
print(f"  уровень реально встретился в тексте (hits): "
      f"{ {LEVEL_NAME[k]: v for k, v in recursion_level_hits.items()} }")
print(f"  уровень реально использован для ДРОБЛЕНИЯ куска, превысившего target (не просто "
      f"присутствовал, а потребовался): "
      f"{ {LEVEL_NAME[k]: v for k, v in recursion_level_used_for_oversized.items()} }")
print(f"  find() не нашёл кусок от текущей позиции (откат на полный поиск): "
      f"{n_fallback_total} раз из {len(v4_pool)} кусков")

# ---------------------------------------------------------------------------
# 3. Эмбеддинг вопросов + пула v4 (та же механика, что v1/v3 в case2_s11_measure.py —
#    реальные HTTP-вызовы через вебхук s10-raw-openrouter, не моки).
# ---------------------------------------------------------------------------
question_texts = [q["question"] for _, q in all_questions]
print(f"\n[эмбеддинг] вопросы: {len(question_texts)} текстов")
q_vecs, q_meta = embed_batch(question_texts)
Q = np.array(q_vecs, dtype=np.float64)
Q = Q / np.linalg.norm(Q, axis=1, keepdims=True)
print(f"  вопросы готовы: shape={Q.shape}, cost={q_meta['cost']}, wall={q_meta['wall_s']}s")

BATCH = 80
texts = [c["text"] for c in v4_pool]
batches = [texts[i:i + BATCH] for i in range(0, len(texts), BATCH)]
embeds_by_batch = [None] * len(batches)
n_embed_calls = 1  # вопросы


def embed_one_batch(i_batch):
    b = batches[i_batch]
    vecs, meta = embed_batch(b)
    return i_batch, vecs, meta


total_cost = 0.0
t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_EMBED) as ex:
    futs = [ex.submit(embed_one_batch, i) for i in range(len(batches))]
    for fut in concurrent.futures.as_completed(futs):
        i_batch, vecs, meta = fut.result()
        embeds_by_batch[i_batch] = vecs
        total_cost += (meta.get("cost") or 0.0)
n_embed_calls += len(batches)
all_vecs = [v for batch in embeds_by_batch for v in batch]
assert len(all_vecs) == len(v4_pool)
C = np.array(all_vecs, dtype=np.float64)
C = C / np.linalg.norm(C, axis=1, keepdims=True)
sims = Q @ C.T
top1_idx = np.argsort(-sims, axis=1)[:, 0]
print(f"  пул v4 эмбеддирован: {len(batches)} запросов, cost=${total_cost:.6f}, "
      f"elapsed={time.time()-t0:.1f}s")

pool_embed_cost_total = total_cost + (q_meta.get("cost") or 0.0)


# ---------------------------------------------------------------------------
# 4. Структурная метрика + честный LLM-вызов (K=1), версия "direct" (как v1/v3).
# ---------------------------------------------------------------------------
def covers_span(start, end, a_start, a_end):
    return start <= a_start and a_end <= end


tasks = []
for qi, (doc_idx, q) in enumerate(all_questions):
    chosen = v4_pool[int(top1_idx[qi])]
    gold_doc_retrieved = (chosen["doc_idx"] == doc_idx)
    context_text = chosen["text"]
    intact = gold_doc_retrieved and covers_span(
        chosen["start"], chosen["end"], q["answer_start"], q["answer_end"])
    tasks.append((qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact))


def run_one(task):
    qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact = task
    r = llm_answer(q["question"], context_text)
    return qi, doc_idx, q, chosen, gold_doc_retrieved, intact, r


print(f"\n[v4] LLM-вызовы (K=1, gpt-4o-mini через s10-raw-openrouter): {len(tasks)}")
t_llm_start = time.time()
results_q = [None] * len(tasks)
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_LLM) as ex:
    futs = [ex.submit(run_one, t) for t in tasks]
    for fut in concurrent.futures.as_completed(futs):
        qi, doc_idx, q, chosen, gold_doc_retrieved, intact, r = fut.result()
        results_q[qi] = (doc_idx, q, chosen, gold_doc_retrieved, intact, r)
elapsed_llm = time.time() - t_llm_start

details = []
n_correct = n_intact = n_gold_doc_retrieved = 0
total_cost = total_wall = 0.0
for qi, (doc_idx, q, chosen, gold_doc_retrieved, intact, r) in enumerate(results_q):
    ok = contains_answer(r["answer"], q["answer"])
    n_correct += ok
    n_intact += intact
    n_gold_doc_retrieved += gold_doc_retrieved
    total_cost += (r["cost"] or 0.0)
    total_wall += (r["wall_s"] or 0.0)
    details.append({
        "version": "v4", "k": 1, "doc_idx": doc_idx,
        "question": q["question"], "reference_answer": q["answer"],
        "model_answer": r["answer"], "correct_strict": ok,
        "answer_intact": intact, "gold_doc_retrieved": gold_doc_retrieved,
        "retrieved_chunk": {"doc_idx": chosen["doc_idx"], "start": chosen["start"],
                             "end": chosen["end"]},
        "cost_usd": r["cost"], "wall_s": r["wall_s"], "exec_id": r["exec_id"],
        "raw_error": r["raw_error"],
    })

n = len(tasks)
row = {
    "version": "v4",
    "label": "рекурсивная/самоподстраивающаяся резка по сепараторам "
              "(абзац->строка->предложение->слово, target=180, как у v1)",
    "k": 1, "n_questions": n,
    "accuracy_strict": round(n_correct / n, 4),
    "answer_intact_rate": round(n_intact / n, 4),
    "gold_doc_retrieved_rate": round(n_gold_doc_retrieved / n, 4),
    "avg_cost_usd": round(total_cost / n, 8),
    "avg_wall_s": round(total_wall / n, 3),
}
print(f"\n[итог v4] accuracy_strict={row['accuracy_strict']} intact={row['answer_intact_rate']} "
      f"gold_doc_retrieved={row['gold_doc_retrieved_rate']}")
print(f"LLM-вызовов={n}, elapsed={elapsed_llm:.1f}s")

out = {
    "method": {
        "corpus": "SberQuAD validation, те же 60 документов/72 вопроса, что v1-v3 "
                  "(case2_s11_measure.py), seed=7",
        "algorithm": "RecursiveCharacterTextSplitter-логика (LangChain), реализована "
                      "самостоятельно (библиотека недоступна в среде — pip install "
                      "отказал как externally-managed-environment): уровни разделителей "
                      "по убыванию размера абзац(\\n\\n) -> строка(\\n) -> "
                      "предложение(SENT_SPLIT, та же регулярка, что v1/v2/v3) -> "
                      "слово(' ') -> символ; переход на уровень мельче ТОЛЬКО если кусок "
                      "этого уровня сам превысил target после разделения; соседние "
                      "кусочки, уложившиеся в target, жадно упаковываются без overlap "
                      "(тот же приём, что chunk_structural v1, обобщённый на все уровни)",
        "target_chars": CHUNK_SIZE_V1,
        "corpus_caveat": "документы SberQuAD в этой выборке — однопараграфные (0/60 "
                          "содержат '\\n\\n' или '\\n'), поэтому уровни «абзац» и «строка» "
                          "на этом корпусе реально НЕ СРАБАТЫВАЮТ ни разу (hits=0) — "
                          "рекурсия работает только на предложение->слово. Эффект "
                          "«абзац -> предложения -> слова» в полном виде раскрывается на "
                          "документах с реальной параграфной структурой, не на коротких "
                          "энциклопедических абзацах (то же ограничение данных, что уже "
                          "названо для v2 — 'родитель = документ целиком')",
        "recursion_level_hits": {LEVEL_NAME[k]: v for k, v in recursion_level_hits.items()},
        "recursion_level_used_for_oversized": {
            LEVEL_NAME[k]: v for k, v in recursion_level_used_for_oversized.items()},
        "n_chunks": len(v4_pool),
        "mean_chunk_chars": round(float(np.mean(chunk_lens)), 1),
        "max_chunk_chars": int(max(chunk_lens)),
        "n_span_find_fallback": n_fallback_total,
        "embed_model": "openai/text-embedding-3-small",
        "llm_model": "openai/gpt-4o-mini",
        "webhook": "s10-raw-openrouter",
        "k": 1,
        "correctness_criterion": "accuracy_strict — harness2.contains_answer, идентично v1-v3",
        "intact_definition": "верный документ был top-1 И найденный кусок целиком содержит "
                              "эталонный спан (версия 'direct', как v1/v3 — без подстановки "
                              "родителя)",
        "n_llm_calls": n, "n_embedding_calls": n_embed_calls,
        "n_embedding_texts": len(question_texts) + len(texts),
        "elapsed_llm_s": round(elapsed_llm, 1),
        "pool_embed_cost_usd": round(pool_embed_cost_total, 6),
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    },
    "summary": [row],
    "details": details,
}

json.dump(out, open(OUTFILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"\nсохранено: {OUTFILE}")
