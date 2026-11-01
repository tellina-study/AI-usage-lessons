#!/usr/bin/env python3
"""Кейс 3, 4-й и 5-й варианты — LLM-реранкер поверх top-10 кандидатов (а) гибрида
RRF и (б) чистого вектора. Zero new infra: тот же credential/вебхук
s10-raw-openrouter, та же модель gpt-4o-mini, что уже используется в Кейсе 1 —
реранкер здесь не отдельный rerank-эндпоинт (OpenRouter такого не даёт), а
LLM-as-reranker: модели показывают топ-10 кандидатов и просят вернуть порядок по
релевантности. Тот же пул вопросов SberQuAD / корпус документов, что в
case3_measure.py — чтобы оставаться на одной эталонной разметке.

Запускать из measure/ с corpus_case1_embedded.json и case3_questions.json рядом
(см. README «Как пересобрать»):
    python3 embed_corpus.py   # если ещё не сделано в этой сессии
    python3 case3_rerank_measure.py
"""
import json
import re
import time

from harness2 import embed_batch, cosine
from harness_call import call_raw
from case1_measure import tokenize  # классический токенизатор (keyword-метод)

RERANK_MODEL = "openai/gpt-4o-mini"
TOP_N = 10

existing = json.load(open('corpus_case1_embedded.json'))
corpus_200 = existing['corpus_500']  # имя переменной сохранено для минимального диффа; теперь 500 документов
by_id = {d['id']: d for d in corpus_200}
q3 = json.load(open('case3_questions.json'))['questions']

q_texts = [q['question'] for q in q3]
t_embed0 = time.time()
qvecs, qmeta = embed_batch(q_texts)
print(f"embedded {len(q_texts)} queries: wall={qmeta['wall_s']}s cost={qmeta['cost']}")
for q, v in zip(q3, qvecs):
    q['embedding'] = v


def keyword_rank(question):
    q_tokens = set(tokenize(question))
    scored = []
    for doc in corpus_200:
        d_tokens = set(tokenize(doc['text']))
        overlap = len(q_tokens & d_tokens)
        scored.append((overlap, doc['id']))
    scored.sort(key=lambda x: -x[0])
    return [doc_id for _, doc_id in scored]


def vector_rank(qvec):
    scored = [(cosine(qvec, d['embedding']), d['id']) for d in corpus_200]
    scored.sort(key=lambda x: -x[0])
    return [doc_id for _, doc_id in scored]


def rrf_fuse(rank_a, rank_b, k=60):
    scores = {}
    for rank_list in (rank_a, rank_b):
        for i, doc_id in enumerate(rank_list):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + i + 1)
    return sorted(scores.keys(), key=lambda d: -scores[d])


def recall_at_k(ranked_ids, gold_id, k):
    return 1 if gold_id in ranked_ids[:k] else 0


def rerank_llm(question, candidate_ids, timeout=90):
    """Один вызов gpt-4o-mini: показать top-N кандидатов, попросить порядок по
    релевантности. Возвращает (reranked_ids, meta). При сбое парсинга —
    fallback на исходный порядок, помечается parse_ok=False (честно, не скрыто)."""
    cand_texts = [by_id[cid]['text'] for cid in candidate_ids]
    numbered = "\n\n".join(f"{i+1}. {t}" for i, t in enumerate(cand_texts))
    body = {
        "model": RERANK_MODEL,
        "messages": [
            {"role": "system", "content": (
                "Ты — переранжировщик результатов поиска. Тебе дан вопрос и "
                f"{len(candidate_ids)} кандидатов-отрывков, пронумерованных 1.."
                f"{len(candidate_ids)}. Переупорядочи номера кандидатов от самого "
                "релевантного вопросу к наименее релевантному. Ответь СТРОГО JSON-"
                "массивом чисел — перестановкой всех номеров, без пояснений. "
                "Пример ответа: [3,1,4,2,5,6,7,8,9,10]"
            )},
            {"role": "user", "content": f"Вопрос: {question}\n\nКандидаты:\n{numbered}"},
        ],
        "usage": {"include": True},
    }
    r = call_raw("https://openrouter.ai/api/v1/chat/completions", body, timeout=timeout)
    resp = r["response"] or {}
    try:
        content = resp["choices"][0]["message"]["content"]
    except Exception:
        content = None
    usage = resp.get("usage", {})
    meta = {
        "exec_id": r["exec_id"], "wall_s": r["wall_s"], "node_ms": r["node_ms"],
        "prompt_tokens": usage.get("prompt_tokens"), "completion_tokens": usage.get("completion_tokens"),
        "cost": usage.get("cost"), "raw_content": content,
    }
    order = None
    if content:
        m = re.search(r"\[[\d,\s]+\]", content)
        if m:
            try:
                parsed = json.loads(m.group(0))
                if sorted(parsed) == list(range(1, len(candidate_ids) + 1)):
                    order = parsed
            except Exception:
                order = None
    if order is None:
        meta["parse_ok"] = False
        return list(candidate_ids), meta  # fallback: исходный порядок, без изменений
    meta["parse_ok"] = True
    reranked_ids = [candidate_ids[i - 1] for i in order]
    return reranked_ids, meta


def rank_after_rerank(reranked_candidates, gold, fallback_full_rank):
    """Ранг gold после реранка top-N. Если gold не входил в top-N кандидатов —
    реранкер физически не мог его поднять/опустить: ранг остаётся тем, что дал
    retrieval до реранка (fallback_full_rank), это не сентинел, а честная
    семантика «реранкер работает только над тем, что ему показали»."""
    if gold in reranked_candidates:
        return reranked_candidates.index(gold) + 1
    return fallback_full_rank


results = []
t0 = time.time()
for i, q in enumerate(q3):
    kw_rank = keyword_rank(q['question'])
    vec_rank = vector_rank(q['embedding'])
    hybrid_rank = rrf_fuse(kw_rank, vec_rank)
    gold = q['gold_doc_id']

    hybrid_full_rank = hybrid_rank.index(gold) + 1 if gold in hybrid_rank else None
    vector_full_rank = vec_rank.index(gold) + 1 if gold in vec_rank else None

    hybrid_top10 = hybrid_rank[:TOP_N]
    vector_top10 = vec_rank[:TOP_N]

    reranked_hybrid, meta_h = rerank_llm(q['question'], hybrid_top10)
    reranked_vector, meta_v = rerank_llm(q['question'], vector_top10)

    rank_hr = rank_after_rerank(reranked_hybrid, gold, hybrid_full_rank)
    rank_vr = rank_after_rerank(reranked_vector, gold, vector_full_rank)

    print(f"[{i+1}/{len(q3)}] {q['qid']}: hybrid_rank={hybrid_full_rank}->rerank={rank_hr} "
          f"(parse_ok={meta_h['parse_ok']}, cost={meta_h['cost']}, wall={meta_h['wall_s']}s) | "
          f"vector_rank={vector_full_rank}->rerank={rank_vr} "
          f"(parse_ok={meta_v['parse_ok']}, cost={meta_v['cost']}, wall={meta_v['wall_s']}s)")

    results.append({
        'qid': q['qid'], 'question': q['question'], 'gold_doc_id': gold,
        'keyword_rank_of_gold': kw_rank.index(gold) + 1 if gold in kw_rank else None,
        'vector_rank_of_gold': vector_full_rank,
        'hybrid_rank_of_gold': hybrid_full_rank,
        'hybrid_rerank_rank_of_gold': rank_hr,
        'vector_rerank_rank_of_gold': rank_vr,
        'keyword_recall@1': recall_at_k(kw_rank, gold, 1),
        'keyword_recall@3': recall_at_k(kw_rank, gold, 3),
        'vector_recall@1': recall_at_k(vec_rank, gold, 1),
        'vector_recall@3': recall_at_k(vec_rank, gold, 3),
        'hybrid_recall@1': recall_at_k(hybrid_rank, gold, 1),
        'hybrid_recall@3': recall_at_k(hybrid_rank, gold, 3),
        'hybrid_rerank_recall@1': 1 if reranked_hybrid[:1] == [gold] else 0,
        'hybrid_rerank_recall@3': 1 if gold in reranked_hybrid[:3] else 0,
        'vector_rerank_recall@1': 1 if reranked_vector[:1] == [gold] else 0,
        'vector_rerank_recall@3': 1 if gold in reranked_vector[:3] else 0,
        'hybrid_rerank_meta': {k: v for k, v in meta_h.items() if k != 'raw_content'},
        'vector_rerank_meta': {k: v for k, v in meta_v.items() if k != 'raw_content'},
    })

n = len(results)
summary = {'n_questions': n, 'corpus_size': len(corpus_200), 'rerank_top_n': TOP_N, 'rerank_model': RERANK_MODEL}
for method in ['keyword', 'vector', 'hybrid']:
    summary[method] = {
        'recall@1': round(sum(r[f'{method}_recall@1'] for r in results) / n, 3),
        'recall@3': round(sum(r[f'{method}_recall@3'] for r in results) / n, 3),
        'avg_rank_of_gold': round(sum(r[f'{method}_rank_of_gold'] or 201 for r in results) / n, 1),
    }
for method in ['hybrid_rerank', 'vector_rerank']:
    meta_key = 'hybrid_rerank_meta' if method == 'hybrid_rerank' else 'vector_rerank_meta'
    summary[method] = {
        'recall@1': round(sum(r[f'{method}_recall@1'] for r in results) / n, 3),
        'recall@3': round(sum(r[f'{method}_recall@3'] for r in results) / n, 3),
        'avg_rank_of_gold': round(sum(r[f'{method}_rank_of_gold'] for r in results) / n, 1),
        'avg_cost_usd_per_question': round(sum((r[meta_key]['cost'] or 0) for r in results) / n, 6),
        'avg_wall_s_per_question': round(sum((r[meta_key]['wall_s'] or 0) for r in results) / n, 2),
        'avg_prompt_tokens': round(sum((r[meta_key]['prompt_tokens'] or 0) for r in results) / n, 1),
        'n_parse_fallback': sum(1 for r in results if not r[meta_key]['parse_ok']),
    }

elapsed = time.time() - t0
out = {
    'summary': summary, 'details': results, 'total_wall_s': round(elapsed, 1),
    'embed_wall_s': qmeta['wall_s'], 'embed_cost_usd': qmeta['cost'],
    'note': ('hybrid_rerank = top-10 кандидатов RRF(keyword, vector) -> gpt-4o-mini '
              'переранжирует -> новый ранг (если gold не входил в top-10, ранг = '
              'rank_of_gold ДО реранка — реранкер не мог поднять то, чего не видел). '
              'vector_rerank = то же самое, но top-10 кандидатов — чистый vector-поиск, '
              'без RRF. Обе ветки — тот же вызов gpt-4o-mini через s10-raw-openrouter, '
              'без новой инфраструктуры.'),
}
json.dump(out, open('case3-rerank-results.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(json.dumps(summary, ensure_ascii=False, indent=2))
print(f"TOTAL wall={elapsed:.1f}s")
