#!/usr/bin/env python3
"""Семинар 11, Кейс 1 — трансформация и размножение запроса перед поиском.

Переиспользует корпус Кейса 1/3 Семинара 10 (500 документов SberQuAD, confusable-кластеры
+ дистракторы, построены `sem-10/stend/measure/build_corpus_v2.py`) и уже стратифицированные
по `lexical_class` (exact_match/lexical_gap/neutral) 50 вопросов Кейса 3 того же семинара —
ровно то разделение, которое нужно, чтобы показать «трансформация помогает на расплывчатом
вопросе, портит на точном» на РЕАЛЬНОМ, не придуманном для этого измерении, корпусе.

Три варианта на одном наборе вопросов (ARCHITECTURE.md/SETKA-KEYSOV.md, Кейс 1):
  (а) baseline      — RRF(keyword(original), vector(original))            — рецепт С10, без трансформации
  (б) multi-query    — RRF(keyword(original), vector(reform_1..3))        — LLM генерирует 3 переформулировки,
                        поиск по каждой embedding'ом, фьюжн всех векторных ранжирований + keyword-якорь
  (в) HyDE            — RRF(keyword(original), vector(hyde_doc))          — LLM сочиняет гипотетический ответ,
                        поиск по его эмбеддингу вместо эмбеддинга вопроса

Во всех трёх вариантах keyword-ранжирование ОРИГИНАЛЬНОГО вопроса остаётся константой — это
изолирует эффект именно трансформации на векторном плече гибрида, при этом variant остаётся
тем же РЕЦЕПТОМ С10 (RRF гибрида), не новой архитектурой поиска.

Все LLM/embedding-вызовы — через вебхук `s10-raw-openrouter` (общий харнесс-прокси OpenRouter,
переиспользован как есть, без публикации нового сценария — задача явно это разрешает). Ключ
OpenRouter не читается и не печатается этим файлом.
"""
import concurrent.futures
import json
import os
import re
import time

from harness2 import cosine, embed_batch

CHAT_MODEL = "openai/gpt-4o-mini"
EMBED_MODEL = "openai/text-embedding-3-small"
N_REFORM = 3
MAX_WORKERS = 8
EMBED_BATCH = 25

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


def rrf_fuse(*rank_lists, k=60):
    scores = {}
    for rank_list in rank_lists:
        for i, doc_id in enumerate(rank_list):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + i + 1)
    return sorted(scores.keys(), key=lambda d: -scores[d])


def recall_at_k(ranked_ids, gold_id, k):
    return 1 if gold_id in ranked_ids[:k] else 0


REFORM_PROMPT = (
    "Ты помогаешь системе поиска. Дан вопрос пользователя на русском. Сгенерируй РОВНО 3 "
    "альтернативные переформулировки этого же вопроса — разными словами, но с тем же смыслом "
    "(как если бы три разных человека задали один и тот же вопрос). Ответь СТРОГО JSON-массивом "
    "из 3 строк, без пояснений, без markdown, например: [\"...\", \"...\", \"...\"]\n\nВопрос: {q}"
)

HYDE_PROMPT = (
    "Представь, что ты пишешь короткий (2-3 предложения) энциклопедический фрагмент текста, "
    "который мог бы содержать ответ на следующий вопрос — связный абзац в стиле статьи, "
    "а не прямой ответ одним словом. Если точных деталей не знаешь — всё равно сочини "
    "правдоподобный по стилю фрагмент (это гипотетический документ для поиска, не факт). "
    "Ответь ТОЛЬКО текстом фрагмента, без пояснений.\n\nВопрос: {q}"
)


def call_llm_raw(prompt, timeout=90):
    from harness_call import call_raw
    body = {
        "model": CHAT_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "usage": {"include": True},
    }
    r = call_raw("https://openrouter.ai/api/v1/chat/completions", body, timeout=timeout)
    resp = r["response"] or {}
    try:
        text = resp["choices"][0]["message"]["content"]
    except Exception:
        text = None
    usage = resp.get("usage", {})
    return {"exec_id": r["exec_id"], "wall_s": r["wall_s"], "text": text,
            "cost": usage.get("cost"), "raw_error": resp.get("error")}


def parse_json_list(text, n=N_REFORM):
    if not text:
        return []
    m = re.search(r"\[.*\]", text, re.DOTALL)
    if not m:
        return []
    try:
        arr = json.loads(m.group(0))
        return [str(x) for x in arr][:n]
    except Exception:
        return []


def main():
    print("Загрузка корпуса и вопросов...")
    corpus_data = json.load(open("../corpus/corpus_case1_s10.json"))
    corpus = corpus_data["corpus_500"]
    questions = json.load(open("../corpus/case3_questions_s10.json"))["questions"]
    n_sample = os.environ.get("CASE1_TRANSFORM_SAMPLE")
    if n_sample:
        questions = questions[: int(n_sample)]
    outfile = os.environ.get("CASE1_TRANSFORM_OUTFILE", "case1-transform-results.json")
    print(f"corpus={len(corpus)} questions={len(questions)}")

    t0 = time.time()

    # 1. Embed corpus (batched) + original questions ----------------------
    print("Эмбеддинг корпуса (500 документов, batch=25)...")
    texts = [d["text"] for d in corpus]
    all_vecs = []
    embed_cost = 0.0
    for i in range(0, len(texts), EMBED_BATCH):
        batch = texts[i:i + EMBED_BATCH]
        vecs, meta = embed_batch(batch, model=EMBED_MODEL)
        all_vecs.extend(vecs)
        embed_cost += (meta["cost"] or 0)
        print(f"  corpus batch {i}-{i+len(batch)} wall={meta['wall_s']}s")
    for d, v in zip(corpus, all_vecs):
        d["embedding"] = v

    print("Эмбеддинг оригинальных вопросов...")
    q_texts = [q["question"] for q in questions]
    qvecs, qmeta = embed_batch(q_texts, model=EMBED_MODEL)
    embed_cost += (qmeta["cost"] or 0)
    for q, v in zip(questions, qvecs):
        q["orig_embedding"] = v

    # Precompute keyword rank for original question (constant across all 3 variants)
    for q in questions:
        q["kw_rank_orig"] = keyword_rank(q["question"], corpus)
        q["vec_rank_orig"] = vector_rank(q["orig_embedding"], corpus)

    # 2. LLM calls: generate reformulations + HyDE docs, concurrently -----
    print(f"Генерация 3 переформулировок + HyDE-документа на {len(questions)} вопросов "
          f"(concurrency={MAX_WORKERS})...")

    def gen_for_question(q):
        reform_r = call_llm_raw(REFORM_PROMPT.format(q=q["question"]))
        hyde_r = call_llm_raw(HYDE_PROMPT.format(q=q["question"]))
        return q["qid"], reform_r, hyde_r

    gen_results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = [ex.submit(gen_for_question, q) for q in questions]
        for fut in concurrent.futures.as_completed(futs):
            qid, reform_r, hyde_r = fut.result()
            gen_results[qid] = {"reform": reform_r, "hyde": hyde_r}
            print(f"  gen done qid={qid} reform_exec={reform_r['exec_id']} hyde_exec={hyde_r['exec_id']}")

    gen_cost = sum((v["reform"]["cost"] or 0) + (v["hyde"]["cost"] or 0) for v in gen_results.values())

    # 3. Parse reformulations, batch-embed all reformulations + hyde docs -
    reform_texts_flat = []  # (qid, idx, text)
    hyde_texts_flat = []  # (qid, text)
    for q in questions:
        gr = gen_results[q["qid"]]
        reforms = parse_json_list(gr["reform"]["text"])
        q["reformulations"] = reforms
        q["reform_exec_id"] = gr["reform"]["exec_id"]
        q["reform_parse_ok"] = len(reforms) == N_REFORM
        for i, rt in enumerate(reforms):
            reform_texts_flat.append((q["qid"], i, rt))
        hyde_doc = gr["hyde"]["text"] or ""
        q["hyde_doc"] = hyde_doc
        q["hyde_exec_id"] = gr["hyde"]["exec_id"]
        hyde_texts_flat.append((q["qid"], hyde_doc))

    print(f"Переформулировок распаршено: {len(reform_texts_flat)} / ожидалось {len(questions)*N_REFORM}")

    print("Эмбеддинг переформулировок...")
    reform_vecs_by_qid = {q["qid"]: [] for q in questions}
    all_reform_texts = [t for _, _, t in reform_texts_flat]
    for i in range(0, len(all_reform_texts), EMBED_BATCH):
        batch = all_reform_texts[i:i + EMBED_BATCH]
        if not batch:
            continue
        vecs, meta = embed_batch(batch, model=EMBED_MODEL)
        embed_cost += (meta["cost"] or 0)
        for (qid, idx, _), v in zip(reform_texts_flat[i:i + EMBED_BATCH], vecs):
            reform_vecs_by_qid[qid].append(v)

    print("Эмбеддинг HyDE-документов...")
    hyde_vecs_by_qid = {}
    all_hyde_texts = [t if t else " " for _, t in hyde_texts_flat]
    for i in range(0, len(all_hyde_texts), EMBED_BATCH):
        batch = all_hyde_texts[i:i + EMBED_BATCH]
        vecs, meta = embed_batch(batch, model=EMBED_MODEL)
        embed_cost += (meta["cost"] or 0)
        for (qid, _), v in zip(hyde_texts_flat[i:i + EMBED_BATCH], vecs):
            hyde_vecs_by_qid[qid] = v

    # 4. Compute 3 variant rankings per question ---------------------------
    results = []
    for q in questions:
        qid = q["qid"]
        gold = q["gold_doc_id"]
        kw_rank = q["kw_rank_orig"]
        vec_rank_orig = q["vec_rank_orig"]

        baseline_rank = rrf_fuse(kw_rank, vec_rank_orig)

        reform_vec_ranks = [vector_rank(v, corpus) for v in reform_vecs_by_qid.get(qid, [])]
        multiquery_rank = rrf_fuse(kw_rank, *reform_vec_ranks) if reform_vec_ranks else baseline_rank

        hyde_vec = hyde_vecs_by_qid.get(qid)
        hyde_rank = rrf_fuse(kw_rank, vector_rank(hyde_vec, corpus)) if hyde_vec else baseline_rank

        results.append({
            "qid": qid, "question": q["question"], "gold_doc_id": gold,
            "lexical_class": q["lexical_class"], "overlap_ratio": q.get("overlap_ratio"),
            "reformulations": q["reformulations"], "reform_parse_ok": q["reform_parse_ok"],
            "hyde_doc": q["hyde_doc"],
            "reform_exec_id": q["reform_exec_id"], "hyde_exec_id": q["hyde_exec_id"],
            "baseline_rank_of_gold": baseline_rank.index(gold) + 1 if gold in baseline_rank else None,
            "multiquery_rank_of_gold": multiquery_rank.index(gold) + 1 if gold in multiquery_rank else None,
            "hyde_rank_of_gold": hyde_rank.index(gold) + 1 if gold in hyde_rank else None,
            "baseline_recall@1": recall_at_k(baseline_rank, gold, 1),
            "multiquery_recall@1": recall_at_k(multiquery_rank, gold, 1),
            "hyde_recall@1": recall_at_k(hyde_rank, gold, 1),
            "baseline_recall@3": recall_at_k(baseline_rank, gold, 3),
            "multiquery_recall@3": recall_at_k(multiquery_rank, gold, 3),
            "hyde_recall@3": recall_at_k(hyde_rank, gold, 3),
        })

    # 5. Summaries: overall + per lexical_class -----------------------------
    def summarize(subset):
        n = len(subset)
        if n == 0:
            return None
        out = {"n_questions": n}
        for method in ["baseline", "multiquery", "hyde"]:
            out[method] = {
                "recall@1": round(sum(r[f"{method}_recall@1"] for r in subset) / n, 3),
                "recall@3": round(sum(r[f"{method}_recall@3"] for r in subset) / n, 3),
                "avg_rank_of_gold": round(
                    sum(r[f"{method}_rank_of_gold"] or 501 for r in subset) / n, 1),
            }
        return out

    summary = {
        "overall": summarize(results),
        "by_lexical_class": {
            cls: summarize([r for r in results if r["lexical_class"] == cls])
            for cls in ["exact_match", "lexical_gap", "neutral"]
        },
    }

    elapsed = time.time() - t0
    out = {
        "summary": summary,
        "details": results,
        "corpus_size": len(corpus),
        "n_questions": len(questions),
        "n_reformulations_per_question": N_REFORM,
        "fusion_method": "RRF (k=60), keyword(original) held constant across all 3 variants",
        "models": {"chat": CHAT_MODEL, "embed": EMBED_MODEL},
        "total_wall_s": round(elapsed, 1),
        "total_cost_usd_estimate": round(embed_cost + gen_cost, 6),
        "note": (
            "baseline = RRF(keyword(вопрос), vector(вопрос)) — рецепт С10 без трансформации; "
            "multiquery = RRF(keyword(вопрос), vector(reform_1), vector(reform_2), vector(reform_3)) "
            "— 3 LLM-переформулировки, фьюжн векторных ранжирований + keyword-якорь оригинала; "
            "hyde = RRF(keyword(вопрос), vector(hyde_doc)) — LLM сочиняет гипотетический ответ, "
            "поиск по его эмбеддингу вместо эмбеддинга вопроса. Вопросы и корпус — Кейс 1/3 "
            "Семинара 10 (500 SberQuAD-документов, lexical_class exact_match/lexical_gap/neutral)."
        ),
    }
    json.dump(out, open(outfile, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"TOTAL wall={elapsed:.1f}s cost≈${embed_cost+gen_cost:.6f}")


if __name__ == "__main__":
    main()
