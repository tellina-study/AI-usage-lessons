import json, time
from harness2 import embed_batch, cosine
from case1_measure import tokenize, STOPWORDS  # reuse tokenizer (classical keyword method)

existing = json.load(open('corpus_case1_embedded.json'))
corpus_200 = existing['corpus_200']
q3 = json.load(open('case3_questions.json'))['questions']

q_texts = [q['question'] for q in q3]
t0 = time.time()
qvecs, meta = embed_batch(q_texts)
print(f"embedded {len(q_texts)} queries: wall={meta['wall_s']}s cost={meta['cost']}")
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
    """Reciprocal Rank Fusion — классическое, не-ИИ слияние двух ранжирований."""
    scores = {}
    for rank_list in (rank_a, rank_b):
        for i, doc_id in enumerate(rank_list):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + i + 1)
    return sorted(scores.keys(), key=lambda d: -scores[d])


def recall_at_k(ranked_ids, gold_id, k):
    return 1 if gold_id in ranked_ids[:k] else 0


results = []
for q in q3:
    kw_rank = keyword_rank(q['question'])
    vec_rank = vector_rank(q['embedding'])
    hybrid_rank = rrf_fuse(kw_rank, vec_rank)
    gold = q['gold_doc_id']
    results.append({
        'qid': q['qid'], 'question': q['question'], 'gold_doc_id': gold,
        'keyword_rank_of_gold': kw_rank.index(gold) + 1 if gold in kw_rank else None,
        'vector_rank_of_gold': vec_rank.index(gold) + 1 if gold in vec_rank else None,
        'hybrid_rank_of_gold': hybrid_rank.index(gold) + 1 if gold in hybrid_rank else None,
        'keyword_recall@1': recall_at_k(kw_rank, gold, 1),
        'keyword_recall@3': recall_at_k(kw_rank, gold, 3),
        'vector_recall@1': recall_at_k(vec_rank, gold, 1),
        'vector_recall@3': recall_at_k(vec_rank, gold, 3),
        'hybrid_recall@1': recall_at_k(hybrid_rank, gold, 1),
        'hybrid_recall@3': recall_at_k(hybrid_rank, gold, 3),
    })

n = len(results)
summary = {'n_questions': n, 'corpus_size': len(corpus_200)}
for method in ['keyword', 'vector', 'hybrid']:
    summary[method] = {
        'recall@1': round(sum(r[f'{method}_recall@1'] for r in results) / n, 3),
        'recall@3': round(sum(r[f'{method}_recall@3'] for r in results) / n, 3),
        'avg_rank_of_gold': round(sum(r[f'{method}_rank_of_gold'] or 201 for r in results) / n, 1),
    }

elapsed = time.time() - t0
out = {'summary': summary, 'details': results, 'embed_wall_s': elapsed, 'embed_cost_usd': meta['cost'],
       'corpus_size': len(corpus_200), 'fusion_method': 'RRF (k=60)',
       'note': 'keyword = пересечение токенов (та же классическая функция, что в Кейсе 1); '
               'vector = openai/text-embedding-3-small через OpenRouter/стенд; '
               'hybrid = Reciprocal Rank Fusion двух ранжирований, без ИИ-переранжирования.'}
json.dump(out, open('case3-results.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(json.dumps(summary, ensure_ascii=False, indent=2))
