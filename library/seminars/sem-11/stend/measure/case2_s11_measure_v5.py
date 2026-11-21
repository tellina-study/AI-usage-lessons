#!/usr/bin/env python3
"""Семинар 11, Кейс 2 — продвинутый чанкинг. ПЯТАЯ версия (v5), добавленная ПОСЛЕ
v1/v2/v3 (`case2_s11_measure.py`) и v4 (`case2_s11_measure_v4.py`), на ТОЧНО ТОМ ЖЕ корпусе
и тех же 72 вопросах — вопрос владельца курса: «добавь вариант, когда показывается не
только найденный чанк, но и соседние, как будто в этом случае он вообще всех порвёт».

Это "sentence window retrieval" (соседние чанки): поиск (top-1) — ТОТ ЖЕ, что версия 1
(резка по предложениям, `chunk_structural`, target=180) — ни эмбеддинги, ни индекс не
меняются относительно v1. Меняется только то, что отдаётся модели для ответа: не сам
найденный кусок, а он + его N=1 соседних кусков ТОЙ ЖЕ нарезки, слева и справа по порядку в
документе (если они существуют — кусок на границе документа получает меньше соседей, это
честно считается, не скрывается).

Отличие от v2 (иерархическая/parent-document, Кейс 2 С11): v2 подставляет РОДИТЕЛЯ — весь
документ целиком, независимо от размера. v5 — локальное расширение окна вокруг top-1, не
весь документ: три кусочка приблизительно по 180 символов (≈540 символов) против целого
документа (≥500 символов, обычно больше). Проверяет гипотезу владельца курса прямым
измерением, а не предположением: даёт ли локальное расширение окна выигрыш, сравнимый с
подстановкой целого родителя — или это другая, более дешёвая, но и менее полная починка.

N=1 выбран как самый просто реализуемый вариант окна (владелец: «можешь попробовать
несколько и выбрать то, что физически реализуемо проще») — ровно по одному соседу с каждой
стороны, конкатенация текстом подряд в порядке документа (сосед слева → top-1 → сосед
справа), без перекрытия. У кусков на границе документа одного из соседей нет — счётчики
такого усечения считаются честно (`n_left_missing`/`n_right_missing`), не прячутся под
средним.

Инфраструктура и метрика — переиспользованы без изменений из `case2_s11_measure.py`/
`case2_s11_measure_v4.py`: корпус (seed=7, offset-фильтр, 60 документов/72 вопроса), вебхук
`s10-raw-openrouter`, `harness2.embed_batch/llm_answer/contains_answer`, K=1,
accuracy_strict/answer_intact_rate/gold_doc_retrieved_rate/avg_cost_usd. v5 — версия
"direct", расширенная окном: `gold_doc_retrieved` считается ТОЧНО как в v1 (top-1 кусок из
нужного документа) — поиск идентичен; `intact` считается по ОБЪЕДИНЁННОМУ окну (левая
граница соседа слева или top-1, если соседа нет; правая граница — аналогично справа).
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

CHUNK_SIZE_V1 = 180  # буквально та же константа, что v1/v4 — окно строится ВОКРУГ той же
                      # нарезки, не новой
WINDOW_RADIUS = 1     # N соседей с каждой стороны — простейший физически реализуемый вариант
MAX_WORKERS_EMBED = 6
MAX_WORKERS_LLM = 12
OUTFILE = "case2-s11-results-v5.json"  # отдельный файл v5; слияние в основной
                                        # case2-results.json — отдельным шагом после прогона

# ---------------------------------------------------------------------------
# 1. Корпус — буквально та же подготовка, что case2_s11_measure.py/case2_s11_measure_v4.py
#    (seed=7, offset-фильтр, SberQuAD >=500 символов). Проверка 60/72 перед тратой реальных
#    API-вызовов.
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
      f"(контроль верности воспроизведения v1-v4: ожидается 60/72)")
assert len(sample) == 60, "корпус не совпадает с v1-v4 — проверить seed/фильтр"
assert len(all_questions) == 72, "вопросы не совпадают с v1-v4 — проверить фильтр офсетов"

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_structural(text, target):
    """Буквально та же функция, что case2_s11_measure.py — v1 baseline, не переизобретена."""
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


# ---------------------------------------------------------------------------
# 2. v5 — та же нарезка, что v1 (по предложениям, target=180). Поиск top-1 идентичен v1:
#    отдельная ось измерения — не в индексе, а в том, что отдаётся модели после поиска.
# ---------------------------------------------------------------------------
print("\n[v5] нарезка по границам предложений (target=180) — ТА ЖЕ, что v1 baseline")
v1_pool = []
for doc_idx, (ctx, _qs) in enumerate(sample):
    for (s, e, t) in chunk_structural(ctx, CHUNK_SIZE_V1):
        v1_pool.append({"doc_idx": doc_idx, "start": s, "end": e, "text": t})
print(f"  куски: {len(v1_pool)} (из {len(sample)} документов) — должно совпасть с v1 (269)")

# индекс соседства: для каждого doc_idx — список глобальных индексов пула в порядке
# документа (пул уже строится по документам последовательно с возрастающим start; сортировка
# ниже — защитная, не меняет порядок при верной конструкции).
doc_chunk_order = {}
for gi, c in enumerate(v1_pool):
    doc_chunk_order.setdefault(c["doc_idx"], []).append(gi)
for d in doc_chunk_order:
    doc_chunk_order[d].sort(key=lambda gi: v1_pool[gi]["start"])
local_pos = {}  # gi -> позиция внутри своего документа
for d, order in doc_chunk_order.items():
    for pos, gi in enumerate(order):
        local_pos[gi] = pos

# ---------------------------------------------------------------------------
# 3. Эмбеддинг вопросов + пула v1 (идентично поиску v1 — реальные вызовы, не кэш из
#    предыдущего прогона, чтобы файл был самодостаточным и воспроизводимым отдельно).
# ---------------------------------------------------------------------------
question_texts = [q["question"] for _, q in all_questions]
print(f"\n[эмбеддинг] вопросы: {len(question_texts)} текстов")
q_vecs, q_meta = embed_batch(question_texts)
Q = np.array(q_vecs, dtype=np.float64)
Q = Q / np.linalg.norm(Q, axis=1, keepdims=True)
print(f"  вопросы готовы: shape={Q.shape}, cost={q_meta['cost']}, wall={q_meta['wall_s']}s")

BATCH = 80
texts = [c["text"] for c in v1_pool]
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
assert len(all_vecs) == len(v1_pool)
C = np.array(all_vecs, dtype=np.float64)
C = C / np.linalg.norm(C, axis=1, keepdims=True)
sims = Q @ C.T
top1_idx = np.argsort(-sims, axis=1)[:, 0]
print(f"  пул v1 эмбеддирован: {len(batches)} запросов, cost=${total_cost:.6f}, "
      f"elapsed={time.time()-t0:.1f}s")

pool_embed_cost_total = total_cost + (q_meta.get("cost") or 0.0)


# ---------------------------------------------------------------------------
# 4. Окно соседей вокруг top-1 (WINDOW_RADIUS=1 с каждой стороны) + структурная метрика +
#    честный LLM-вызов (K=1).
# ---------------------------------------------------------------------------
def covers_span(start, end, a_start, a_end):
    return start <= a_start and a_end <= end


n_left_missing = 0
n_right_missing = 0
tasks = []
for qi, (doc_idx, q) in enumerate(all_questions):
    gi0 = int(top1_idx[qi])
    chosen = v1_pool[gi0]
    gold_doc_retrieved = (chosen["doc_idx"] == doc_idx)  # идентично v1 — поиск не менялся

    order = doc_chunk_order[chosen["doc_idx"]]
    pos = local_pos[gi0]
    left = v1_pool[order[pos - 1]] if pos > 0 else None
    right = v1_pool[order[pos + 1]] if pos < len(order) - 1 else None
    if left is None:
        n_left_missing += 1
    if right is None:
        n_right_missing += 1

    parts = [c["text"] for c in (left, chosen, right) if c is not None]
    context_text = " ".join(parts)
    win_start = left["start"] if left is not None else chosen["start"]
    win_end = right["end"] if right is not None else chosen["end"]
    intact = gold_doc_retrieved and covers_span(
        win_start, win_end, q["answer_start"], q["answer_end"])

    tasks.append((qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact,
                   left is not None, right is not None))

print(f"\n[окно] радиус={WINDOW_RADIUS}: соседа слева нет у {n_left_missing}/72 вопросов "
      f"(top-1 — первый кусок документа), соседа справа нет у {n_right_missing}/72 "
      f"(top-1 — последний кусок документа)")


def run_one(task):
    qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact, has_left, has_right = task
    r = llm_answer(q["question"], context_text)
    return qi, doc_idx, q, chosen, gold_doc_retrieved, intact, has_left, has_right, r


print(f"\n[v5] LLM-вызовы (K=1, gpt-4o-mini через s10-raw-openrouter): {len(tasks)}")
t_llm_start = time.time()
results_q = [None] * len(tasks)
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_LLM) as ex:
    futs = [ex.submit(run_one, t) for t in tasks]
    for fut in concurrent.futures.as_completed(futs):
        qi, doc_idx, q, chosen, gold_doc_retrieved, intact, has_left, has_right, r = fut.result()
        results_q[qi] = (doc_idx, q, chosen, gold_doc_retrieved, intact, has_left, has_right, r)
elapsed_llm = time.time() - t_llm_start

details = []
n_correct = n_intact = n_gold_doc_retrieved = 0
total_cost = total_wall = 0.0
for qi, (doc_idx, q, chosen, gold_doc_retrieved, intact, has_left, has_right, r) in enumerate(results_q):
    ok = contains_answer(r["answer"], q["answer"])
    n_correct += ok
    n_intact += intact
    n_gold_doc_retrieved += gold_doc_retrieved
    total_cost += (r["cost"] or 0.0)
    total_wall += (r["wall_s"] or 0.0)
    details.append({
        "version": "v5", "k": 1, "doc_idx": doc_idx,
        "question": q["question"], "reference_answer": q["answer"],
        "model_answer": r["answer"], "correct_strict": ok,
        "answer_intact": intact, "gold_doc_retrieved": gold_doc_retrieved,
        "has_left_neighbor": has_left, "has_right_neighbor": has_right,
        "retrieved_chunk": {"doc_idx": chosen["doc_idx"], "start": chosen["start"],
                             "end": chosen["end"]},
        "cost_usd": r["cost"], "wall_s": r["wall_s"], "exec_id": r["exec_id"],
        "raw_error": r["raw_error"],
    })

n = len(tasks)
row = {
    "version": "v5",
    "label": f"соседние чанки / sentence window retrieval (радиус={WINDOW_RADIUS}, "
              f"та же нарезка по предложениям, что v1, target=180)",
    "k": 1, "n_questions": n,
    "accuracy_strict": round(n_correct / n, 4),
    "answer_intact_rate": round(n_intact / n, 4),
    "gold_doc_retrieved_rate": round(n_gold_doc_retrieved / n, 4),
    "avg_cost_usd": round(total_cost / n, 8),
    "avg_wall_s": round(total_wall / n, 3),
}
print(f"\n[итог v5] accuracy_strict={row['accuracy_strict']} intact={row['answer_intact_rate']} "
      f"gold_doc_retrieved={row['gold_doc_retrieved_rate']}")
print(f"LLM-вызовов={n}, elapsed={elapsed_llm:.1f}s")

out = {
    "method": {
        "corpus": "SberQuAD validation, те же 60 документов/72 вопроса, что v1-v4 "
                  "(case2_s11_measure.py/case2_s11_measure_v4.py), seed=7",
        "algorithm": "Sentence window retrieval (соседние чанки): поиск top-1 — ИДЕНТИЧЕН v1 "
                      "(та же нарезка по предложениям chunk_structural, target=180, тот же "
                      "индекс, те же эмбеддинги). Модели отдаётся не сам top-1 кусок, а "
                      "конкатенация [сосед слева (если есть) + top-1 + сосед справа (если "
                      "есть)] в порядке документа, без перекрытия, радиус=1 с каждой стороны.",
        "window_radius": WINDOW_RADIUS,
        "target_chars": CHUNK_SIZE_V1,
        "n_left_missing": n_left_missing,
        "n_right_missing": n_right_missing,
        "boundary_caveat": f"{n_left_missing}/72 вопросов — top-1 кусок был первым в своём "
                            f"документе (нет соседа слева), {n_right_missing}/72 — последним "
                            f"(нет соседа справа); эти вопросы получили окно из двух кусков, "
                            f"не трёх — считано честно, не усреднено молча",
        "embed_model": "openai/text-embedding-3-small",
        "llm_model": "openai/gpt-4o-mini",
        "webhook": "s10-raw-openrouter",
        "k": 1,
        "correctness_criterion": "accuracy_strict — harness2.contains_answer, идентично v1-v4",
        "intact_definition": "верный документ был top-1 (идентично v1) И объединённое окно "
                              "(левая граница соседа слева или top-1, правая — соседа справа "
                              "или top-1) целиком содержит эталонный спан",
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
