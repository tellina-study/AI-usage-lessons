#!/usr/bin/env python3
"""Семинар 11, Кейс 2 — продвинутый чанкинг. Последовательная итерация v1 -> v2 -> v3
на РАСШИРЕНИИ корпуса Кейса 2 Семинара 10 (та же 60-документная выборка SberQuAD,
seed=7, тот же offset-фильтр, те же 72 вопроса) — буквально та же подготовка данных, что
`sem-10/stend/measure/case2_chunking.py`/`case2_e2e_measure.py`, не переизобретена.

Версии (в порядке, который требует ARCHITECTURE.md §6 — последовательная итерация, не
параллельный A/B):

- v1 — baseline С10: нарезка по границам предложений (`chunk_structural`, target=180
  символов) = версия 2 из Семинара 10. Это входной рецепт, который С11 проверяет на
  изломе, не изобретённая заново версия 1 Семинара 10 (символьная нарезка) — она уже
  была закрыта как проигравшая на С10.
- v2 — иерархический / parent-document retrieval: маленькие "дети" (`chunk_structural`,
  target=90, половина размера v1) идут в индекс и участвуют в поиске; при совпадении
  модели отдаётся не найденный ребёнок, а ВЕСЬ родительский документ целиком (докстор
  "родителей" в этом корпусе — просто исходный `context` SberQuAD, так как документы
  здесь короче полноценного многостраничного регламента и естественного третьего уровня
  иерархии у них нет; упрощение названо прямо, не скрыто).
- v3a/v3b — семантический чанкинг по порогу разрыва эмбеддингов соседних предложений:
  v3a — порог = 90-й процентиль распределения разрывов по всему корпусу (консервативный,
  режет только на самых резких сменах темы); v3b — порог = 40-й процентиль (агрессивный,
  режет почти на каждом заметном перепаде) — воспроизводит на СВОИХ данных механику
  Vectara/arXiv 2410.13070 ("на неподходящем пороге резка идёт почти по каждому
  предложению"), не копирует её число.

Метрика — как в С10: структурная ("intact" / "gold_doc_retrieved" на top-1, без LLM) +
честная accuracy_strict ответа модели (`gpt-4o-mini`, через тот же вебхук
`s10-raw-openrouter`, та же функция `harness2.contains_answer`, что Кейс 1/2 Семинара 10
— для прямой сравнимости чисел на одном стенде). K=1 для всех версий (один найденный
кусок -> один ответ) — это ровно та точка, где С10 (`case2_e2e_results.json`) показал
самый широкий разрыв между версиями нарезки; без этого K=1-фокуса бюджет замера (288
LLM-вызовов + ~45 embedding-вызовов) было бы нечестно расширять на полный K-sweep ещё
раз — это открытый пункт для будущего прохода, не скрытое урезание.

Инфраструктура — переиспользована, не заведена новая: вебхук `s10-raw-openrouter`
(credential остаётся на стороне n8n, этим файлом не читается и не печатается). Импорт
`harness2`/`harness_call` идёт НЕ из локальной `sem-11/stend/measure/` (этот каталог общий
для нескольких параллельных сессий Кейсов С11, и локальная копия `harness2.py` уже была
переписана соседней сессией Кейса 4 под её узкую задачу, без `llm_answer`/
`contains_answer` — см. `notes/decisions.md`), а напрямую из стабильной, не редактируемой
параллельно `sem-10/stend/measure/` — тем же приёмом, которым `case3_embed_reproduce.py`
(сосед этого файла, Кейс 3 С11) уже обошёл тот же риск.
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

CHUNK_SIZE_V1 = 180
CHUNK_SIZE_V2_CHILD = 90
MAX_WORKERS_EMBED = 6
MAX_WORKERS_LLM = 12
OUTFILE = "case2-s11-results.json"  # рабочая копия (имя с дефисом — только так совпадает с
                                     # паттерном .gitignore `case*-results.json`, тот же приём,
                                     # что уже используют case2_e2e_measure.py С10 и case1/case4
                                     # этого занятия); канонический выход — ../case2-results.json,
                                     # копируется вручную ниже

# ---------------------------------------------------------------------------
# 1. Корпус — буквально та же подготовка, что case2_chunking.py/case2_e2e_measure.py
#    Семинара 10 (seed=7, >=500 символов, offset-фильтр SberQuAD). Сверяем счётчики
#    (60 документов, 72 вопроса) как проверку верности воспроизведения перед тем, как
#    тратить реальные API-вызовы.
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
sample = candidates[:60]

all_questions = []  # (doc_idx, q)
for doc_idx, (ctx, qs) in enumerate(sample):
    for q in qs:
        a_start = q["answer_start"]
        a_end = a_start + len(q["answer"])
        if a_end > len(ctx):
            continue
        all_questions.append((doc_idx, {**q, "answer_start": a_start, "answer_end": a_end}))

print(f"[корпус] n_documents={len(sample)} n_questions={len(all_questions)} "
      f"(контроль верности воспроизведения С10: ожидается 60/72)")
assert len(sample) == 60, "корпус не совпадает с Семинаром 10 — проверить seed/фильтр"
assert len(all_questions) == 72, "вопросы не совпадают с Семинаром 10 — проверить фильтр офсетов"


# ---------------------------------------------------------------------------
# 2. v1 — baseline С10 (= версия 2 Семинара 10): нарезка по границам предложений.
#    Буквально скопирована функция chunk_structural из case2_chunking.py, не
#    переизобретена.
# ---------------------------------------------------------------------------
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")


def chunk_structural(text, target):
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


def split_sentences_with_spans(text):
    """Как chunk_structural, но без накопления в куски — отдельное предложение с его
    [start,end) в исходном тексте. Нужно для семантического чанкинга (v3) и для
    "детей" иерархии (v2), где граница должна совпадать с границей предложения, а не
    произвольного окна символов."""
    sentences = SENT_SPLIT.split(text)
    out = []
    pos = 0
    for sent in sentences:
        if not sent.strip():
            continue
        idx = text.find(sent, pos)
        if idx == -1:
            idx = pos
        s_start, s_end = idx, idx + len(sent)
        out.append((s_start, s_end, sent))
        pos = s_end
    return out


print("\n[v1] нарезка по границам предложений (target=180) — baseline С10")
v1_pool = []
for doc_idx, (ctx, _qs) in enumerate(sample):
    for (s, e, t) in chunk_structural(ctx, CHUNK_SIZE_V1):
        v1_pool.append({"doc_idx": doc_idx, "start": s, "end": e, "text": t})
print(f"  куски: {len(v1_pool)} (из {len(sample)} документов)")

# ---------------------------------------------------------------------------
# 3. v2 — иерархический / parent-document retrieval: дети = chunk_structural(target=90),
#    родитель = весь документ целиком.
# ---------------------------------------------------------------------------
print("\n[v2] иерархический/parent-document: дети target=90, родитель = весь документ")
v2_children_pool = []
for doc_idx, (ctx, _qs) in enumerate(sample):
    for (s, e, t) in chunk_structural(ctx, CHUNK_SIZE_V2_CHILD):
        v2_children_pool.append({"doc_idx": doc_idx, "start": s, "end": e, "text": t})
print(f"  детей: {len(v2_children_pool)} (из {len(sample)} документов, "
      f"родителей = документов целиком = {len(sample)})")

# ---------------------------------------------------------------------------
# 4. v3a/v3b — семантический чанкинг по порогу разрыва эмбеддингов соседних предложений.
#    Шаг 1: эмбеддинг каждого предложения каждого документа (реальный вызов).
#    Шаг 2: разрыв = 1 - cosine(e_i, e_i+1) для соседних предложений ОДНОГО документа.
#    Шаг 3: порог = процентиль распределения разрывов ПО ВСЕМУ КОРПУСУ (не по одному
#    документу — так считает и LangChain SemanticChunker, и так интерпретируется порог
#    у Vectara/FloTorch: "один параметр метода на весь корпус", см. бриф §2/§4).
# ---------------------------------------------------------------------------
print("\n[v3] семантический чанкинг — эмбеддинг предложений для вычисления разрывов")
doc_sentences = [split_sentences_with_spans(ctx) for ctx, _qs in sample]
flat_sentences = []  # (doc_idx, sent_idx_in_doc, start, end, text)
for doc_idx, sents in enumerate(doc_sentences):
    for sent_idx, (s, e, t) in enumerate(sents):
        flat_sentences.append((doc_idx, sent_idx, s, e, t))
print(f"  предложений всего: {len(flat_sentences)} (из {len(sample)} документов)")

sent_texts = [t for (_, _, _, _, t) in flat_sentences]
BATCH = 80
sent_vecs = [None] * len(sent_texts)
n_embed_calls = 0
n_embed_texts = 0
t_embed_start = time.time()
sent_embed_cost = 0.0


def embed_one_batch_sent(i_batch, batch):
    vecs, meta = embed_batch(batch)
    return i_batch, vecs, meta


batches = [sent_texts[i:i + BATCH] for i in range(0, len(sent_texts), BATCH)]
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_EMBED) as ex:
    futs = [ex.submit(embed_one_batch_sent, i, b) for i, b in enumerate(batches)]
    for fut in concurrent.futures.as_completed(futs):
        i_batch, vecs, meta = fut.result()
        start = i_batch * BATCH
        for j, v in enumerate(vecs):
            sent_vecs[start + j] = v
        sent_embed_cost += (meta.get("cost") or 0.0)
n_embed_calls += len(batches)
n_embed_texts += len(sent_texts)
print(f"  эмбеддинг предложений: {len(batches)} запросов, cost=${sent_embed_cost:.6f}, "
      f"elapsed={time.time()-t_embed_start:.1f}s")

S = np.array(sent_vecs, dtype=np.float64)
S = S / np.linalg.norm(S, axis=1, keepdims=True)

# разрывы только между соседними предложениями ОДНОГО документа
gaps = []  # (doc_idx, sent_idx, gap_value) — gap между sent_idx и sent_idx+1
idx_by_doc = {}
for flat_i, (doc_idx, sent_idx, s, e, t) in enumerate(flat_sentences):
    idx_by_doc.setdefault(doc_idx, []).append(flat_i)

for doc_idx, flat_idxs in idx_by_doc.items():
    for k in range(len(flat_idxs) - 1):
        i1, i2 = flat_idxs[k], flat_idxs[k + 1]
        cos = float(np.dot(S[i1], S[i2]))
        gap = 1.0 - cos
        gaps.append((doc_idx, k, gap))

gap_values = np.array([g for (_, _, g) in gaps])
pct90 = float(np.percentile(gap_values, 90))
pct40 = float(np.percentile(gap_values, 40))
pct10 = float(np.percentile(gap_values, 10))
print(f"  разрывов: {len(gap_values)}, распределение: "
      f"min={gap_values.min():.4f} p10={pct10:.4f} p40={pct40:.4f} "
      f"median={np.median(gap_values):.4f} p90={pct90:.4f} max={gap_values.max():.4f}")

gap_by_doc_k = {(d, k): g for (d, k, g) in gaps}


def build_semantic_chunks(threshold):
    """Режет по предложениям документа, начинает новый кусок, когда разрыв со следующим
    предложением превышает threshold. Возвращает пул кусков с [start,end) во всём тексте
    документа (объединение спанов входящих предложений)."""
    pool = []
    for doc_idx, flat_idxs in idx_by_doc.items():
        cur_start = None
        cur_end = None
        cur_sent_count = 0
        for k, flat_i in enumerate(flat_idxs):
            _, _, s, e, _t = flat_sentences[flat_i]
            if cur_start is None:
                cur_start = s
            cur_end = e
            cur_sent_count += 1
            is_last = (k == len(flat_idxs) - 1)
            gap_to_next = gap_by_doc_k.get((doc_idx, k)) if not is_last else None
            if is_last or (gap_to_next is not None and gap_to_next > threshold):
                ctx_text = sample[doc_idx][0][cur_start:cur_end]
                pool.append({"doc_idx": doc_idx, "start": cur_start, "end": cur_end,
                             "text": ctx_text, "n_sentences": cur_sent_count})
                cur_start = None
                cur_sent_count = 0
    return pool


v3a_pool = build_semantic_chunks(pct90)
v3b_pool = build_semantic_chunks(pct40)
v3c_pool = build_semantic_chunks(pct10)
# v3d — вырожденный предел той же оси (не новая ось, а её конец): порог ниже минимального
# разрыва корпуса (min=см. выше) режет на КАЖДОЙ границе предложения без исключения — тот же
# механизм, что дал Vectara/FloTorch 922 куска по 33,9 токена на пороге 0.45 (почти-по-
# предложению резка). Проверяет, пересекает ли семантический чанкинг на предельно агрессивном
# пороге baseline v1, не только v2 (ARCHITECTURE.md §5, Кейс 2: "самая умная техника
# документированно проигрывает самой простой").
v3d_pool = build_semantic_chunks(-1.0)
for _name, _pool, _thr in [("v3a (p90, консервативный)", v3a_pool, pct90),
                            ("v3b (p40, умеренно агрессивный)", v3b_pool, pct40),
                            ("v3c (p10, сверхагрессивный)", v3c_pool, pct10),
                            ("v3d (режет на каждом предложении, вырожденный предел)", v3d_pool, -1.0)]:
    print(f"  {_name}: {len(_pool)} кусков, "
          f"средний размер {np.mean([len(c['text']) for c in _pool]):.1f} символов, "
          f"средне предложений/кусок {np.mean([c['n_sentences'] for c in _pool]):.2f}")

# ---------------------------------------------------------------------------
# 5. Эмбеддинг вопросов (1 раз) + эмбеддинг пулов v1/v2-дети/v3a/v3b (батчами).
# ---------------------------------------------------------------------------
question_texts = [q["question"] for _, q in all_questions]
print(f"\n[эмбеддинг] вопросы: {len(question_texts)} текстов, 1 запрос")
q_vecs, q_meta = embed_batch(question_texts)
n_embed_calls += 1
n_embed_texts += len(question_texts)
Q = np.array(q_vecs, dtype=np.float64)
Q = Q / np.linalg.norm(Q, axis=1, keepdims=True)
print(f"  вопросы готовы: shape={Q.shape}, cost={q_meta['cost']}, wall={q_meta['wall_s']}s")

pools = {
    "v1": v1_pool,
    "v2_children": v2_children_pool,
    "v3a": v3a_pool,
    "v3b": v3b_pool,
    "v3c": v3c_pool,
    "v3d": v3d_pool,
}
pool_embed_cost_total = 0.0

version_state = {}
for pname, pool in pools.items():
    print(f"\n[эмбеддинг пула] {pname}: {len(pool)} кусков")
    texts = [c["text"] for c in pool]
    batches = [texts[i:i + BATCH] for i in range(0, len(texts), BATCH)]
    embeds_by_batch = [None] * len(batches)

    def embed_one_batch(i_batch):
        b = batches[i_batch]
        vecs, meta = embed_batch(b)
        return i_batch, vecs, meta

    total_cost = 0.0
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_EMBED) as ex:
        futs = [ex.submit(embed_one_batch, i) for i in range(len(batches))]
        for fut in concurrent.futures.as_completed(futs):
            i_batch, vecs, meta = fut.result()
            embeds_by_batch[i_batch] = vecs
            total_cost += (meta.get("cost") or 0.0)
    n_embed_calls += len(batches)
    n_embed_texts += len(texts)
    pool_embed_cost_total += total_cost
    all_vecs = [v for batch in embeds_by_batch for v in batch]
    assert len(all_vecs) == len(pool)
    C = np.array(all_vecs, dtype=np.float64)
    C = C / np.linalg.norm(C, axis=1, keepdims=True)
    sims = Q @ C.T  # (n_questions, n_chunks)
    top1_idx = np.argsort(-sims, axis=1)[:, 0]
    version_state[pname] = {"pool": pool, "top1_idx": top1_idx}
    print(f"  готово: {len(batches)} запросов, cost=${total_cost:.6f}")

print(f"\n[итог эмбеддингов] запросов={n_embed_calls}, текстов={n_embed_texts}, "
      f"стоимость пулов=${pool_embed_cost_total:.6f} + предложения=${sent_embed_cost:.6f} "
      f"+ вопросы=${q_meta['cost']}")


# ---------------------------------------------------------------------------
# 6. Структурная метрика (без LLM) + честный LLM-вызов (K=1) по каждой из 4 версий.
#    v1, v3a, v3b: top-1 кусок -> и есть контекст, отдаваемый модели (та же логика, что
#    К=1 Кейса 2 Семинара 10). v2: top-1 РЕБЁНОК -> контекст модели = РОДИТЕЛЬ (весь
#    документ ребёнка), не сам ребёнок — это и есть механика parent-document retrieval.
# ---------------------------------------------------------------------------
def covers_span(start, end, a_start, a_end):
    return start <= a_start and a_end <= end


VERSIONS_FOR_LLM = {
    "v1": {"label": "по предложениям (baseline С10)", "kind": "direct"},
    "v2": {"label": "иерархический / parent-document (ребёнок target=90 -> родитель = документ)",
           "kind": "parent"},
    "v3a": {"label": "семантический чанкинг, порог=p90 корпуса (консервативный)", "kind": "direct"},
    "v3b": {"label": "семантический чанкинг, порог=p40 корпуса (умеренно агрессивный)", "kind": "direct"},
    "v3c": {"label": "семантический чанкинг, порог=p10 корпуса (сверхагрессивный)", "kind": "direct"},
    "v3d": {"label": "семантический чанкинг, порог ниже минимума (каждое предложение — свой кусок)", "kind": "direct"},
}

details = []
summary_rows = []
n_llm_calls = 0
t_llm_start = time.time()

for vname, vinfo in VERSIONS_FOR_LLM.items():
    print(f"\n--- {vname} ({vinfo['label']}) ---")
    if vinfo["kind"] == "parent":
        pool = version_state["v2_children"]["pool"]
        top1_idx = version_state["v2_children"]["top1_idx"]
    else:
        pool = version_state[vname]["pool"]
        top1_idx = version_state[vname]["top1_idx"]

    tasks = []
    for qi, (doc_idx, q) in enumerate(all_questions):
        chosen = pool[int(top1_idx[qi])]
        gold_doc_retrieved = (chosen["doc_idx"] == doc_idx)
        if vinfo["kind"] == "parent":
            # контекст модели — родитель (весь документ ребёнка), не сам ребёнок
            parent_doc_idx = chosen["doc_idx"]
            context_text = sample[parent_doc_idx][0]
            intact = gold_doc_retrieved  # родитель = весь документ -> если это тот
            # документ, ответ в нём заведомо целиком (структура самого определения
            # parent-document retrieval, не отдельное измерение)
        else:
            context_text = chosen["text"]
            intact = gold_doc_retrieved and covers_span(
                chosen["start"], chosen["end"], q["answer_start"], q["answer_end"])
        tasks.append((qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact))

    def run_one(task):
        qi, doc_idx, q, context_text, chosen, gold_doc_retrieved, intact = task
        r = llm_answer(q["question"], context_text)
        return qi, doc_idx, q, chosen, gold_doc_retrieved, intact, r

    results_q = [None] * len(tasks)
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS_LLM) as ex:
        futs = [ex.submit(run_one, t) for t in tasks]
        for fut in concurrent.futures.as_completed(futs):
            qi, doc_idx, q, chosen, gold_doc_retrieved, intact, r = fut.result()
            results_q[qi] = (doc_idx, q, chosen, gold_doc_retrieved, intact, r)
    n_llm_calls += len(tasks)

    n_correct = 0
    n_intact = 0
    n_gold_doc_retrieved = 0
    total_cost = 0.0
    total_wall = 0.0
    for qi, (doc_idx, q, chosen, gold_doc_retrieved, intact, r) in enumerate(results_q):
        ok = contains_answer(r["answer"], q["answer"])
        n_correct += ok
        n_intact += intact
        n_gold_doc_retrieved += gold_doc_retrieved
        total_cost += (r["cost"] or 0.0)
        total_wall += (r["wall_s"] or 0.0)
        details.append({
            "version": vname, "k": 1, "doc_idx": doc_idx,
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
        "version": vname, "label": vinfo["label"], "k": 1, "n_questions": n,
        "accuracy_strict": round(n_correct / n, 4),
        "answer_intact_rate": round(n_intact / n, 4),
        "gold_doc_retrieved_rate": round(n_gold_doc_retrieved / n, 4),
        "avg_cost_usd": round(total_cost / n, 8),
        "avg_wall_s": round(total_wall / n, 3),
    }
    summary_rows.append(row)
    print(f"  accuracy_strict={row['accuracy_strict']} intact={row['answer_intact_rate']} "
          f"gold_doc_retrieved={row['gold_doc_retrieved_rate']}")

elapsed_llm = time.time() - t_llm_start
print(f"\n[итог] LLM-вызовов={n_llm_calls}, elapsed={elapsed_llm:.1f}s")

out = {
    "method": {
        "corpus": "SberQuAD validation, 60 документов >=500 символов, seed=7, offset-фильтр — "
                  "буквально та же подготовка, что case2_chunking.py/case2_e2e_measure.py "
                  "Семинара 10 (сверено: n_documents=60, n_questions=72)",
        "sequential_iteration": "v1 (baseline С10, по предложениям, target=180) -> "
                                 "v2 (иерархический/parent-document, дети target=90, "
                                 "родитель=документ) -> v3a/v3b (семантический чанкинг, "
                                 "порог=p90/p40 распределения разрывов соседних предложений "
                                 "по всему корпусу) — последовательная итерация, не "
                                 "параллельный A/B (ARCHITECTURE.md §6)",
        "k": 1,
        "embed_model": "openai/text-embedding-3-small (тот же, что Кейс 1/2 С10)",
        "llm_model": "openai/gpt-4o-mini (тот же, что Кейс 1/2 С10)",
        "webhook": "s10-raw-openrouter (переиспользован общий, не завели новый сценарий)",
        "correctness_criterion": "accuracy_strict — строгое вхождение эталонного ответа "
                                  "подстрокой в ответ модели — ТА ЖЕ функция "
                                  "harness2.contains_answer, что уже использует Кейс 1/2 С10",
        "intact_definition": "v1/v3a/v3b: верный документ был top-1 И найденный кусок целиком "
                              "содержит эталонный спан. v2: верный документ был top-1 среди "
                              "детей (тогда родитель = весь документ = заведомо содержит "
                              "ответ целиком, это свойство самой механики parent-document, "
                              "не отдельное измерение)",
        "semantic_threshold_percentiles": {"v3a_p90": pct90, "v3b_p40": pct40, "v3c_p10": pct10},
        "gap_distribution": {"min": float(gap_values.min()), "p10": pct10, "p40": pct40,
                              "median": float(np.median(gap_values)), "p90": pct90,
                              "max": float(gap_values.max()), "n_gaps": len(gap_values)},
        "n_llm_calls": n_llm_calls,
        "n_embedding_calls": n_embed_calls,
        "n_embedding_texts": n_embed_texts,
        "n_sentences_embedded": len(sent_texts),
        "elapsed_llm_s": round(elapsed_llm, 1),
        "sent_embed_cost_usd": round(sent_embed_cost, 6),
        "pool_embed_cost_usd": round(pool_embed_cost_total, 6),
        "run_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    },
    "summary": summary_rows,
    "details": details,
}

json.dump(out, open(OUTFILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"\nсохранено: {OUTFILE}")
print("\nСводная таблица:")
print(json.dumps(summary_rows, ensure_ascii=False, indent=2))
