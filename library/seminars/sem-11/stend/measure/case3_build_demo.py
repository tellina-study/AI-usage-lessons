#!/usr/bin/env python3
"""Семинар 11, Кейс 3 — построение МАЛОГО демо-набора для живого n8n-канваса (Фаза 4,
слайды n41-n60). НЕ повторяет основной замер (50 вопросов/500 документов,
`case3_dynamic_rrf.py`) — тот уже посчитан и опубликован в `case3-results.json`.
Этот скрипт готовит компактный (10 документов), но РЕАЛЬНЫЙ набор: настоящие тексты
из того же 500-документного корпуса (`corpus/corpus_case1_s10.json`), настоящие
эмбеддинги через OpenRouter `text-embedding-3-small` (тот же вебхук-прокси
`s10-raw-openrouter`, что everywhere на этом стенде) — чтобы на канвасе n8n был
настоящий узел «Embed query» и настоящий узел «Cosine ranking», не захардкоженные
числа.

Два демо-вопроса — c3q17 и c3q42 из основного замера (их реальный разбор — в
rework/section-3-klassifikatsiya-dinamicheskiy-rrf.md, раздел «Нюансы»):
  - c3q17 «К какому сроку прирост в промышленности Германии сравнялся со
    странами-противниками?» — gold distractor-149, jev классифицировал exact_fact
    (confidence 0.92), хотя реально выигрывает vector.
  - c3q42 «Чем был обмен по бартеру в торговле?» — gold distractor-107, jev
    классифицировал semantic (confidence 0.84), хотя реально выигрывает keyword.

Сохраняет `raw/case3-n8n-demo-payloads.json` — два готовых payload для формы n8n
(вопрос + 10 документов с текстом и настоящим эмбеддингом каждого).
"""
import json
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent.parent.parent / "sem-10" / "stend" / "measure"))
from harness_call import call_raw  # noqa: E402

EMBED_MODEL = "openai/text-embedding-3-small"
DEMO_DOC_IDS = [
    "distractor-149",  # gold c3q17 — прирост промышленности СССР/Британии к ВВП Германии
    "distractor-107",  # gold c3q42 — бартерный обмен (модель Золотаса, 1944)
    "distractor-379",  # keyword-decoy c3q17 — буквально «Германии», 1918, оккупационные войска
    "distractor-463",  # keyword-decoy c3q17 — буквально «промышленный», промышленный переворот РИ
    "distractor-30",   # keyword-decoy c3q42 — буквально «обмен» (Никсон отменил обмен доллара на золото)
    "distractor-200",  # topически смежный decoy — банковские кредиты промышленникам, 1894
    "distractor-99", "distractor-38", "distractor-58", "distractor-20",
]
DEMO_QUESTIONS = [
    {"qid": "c3q17", "question": "К какому сроку прирост в промышленности Германии сравнялся со странами-противниками?",
     "gold_doc_id": "distractor-149"},
    {"qid": "c3q42", "question": "Чем был обмен по бартеру в торговле?",
     "gold_doc_id": "distractor-107"},
]


def embed_batch(texts, timeout=120):
    body = {"model": EMBED_MODEL, "input": texts}
    r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=timeout)
    resp = r["response"] or {}
    if "data" not in resp:
        raise RuntimeError(f"embed_batch failed: {json.dumps(resp, ensure_ascii=False)[:500]}")
    vecs = [d["embedding"] for d in resp["data"]]
    usage = resp.get("usage", {})
    return vecs, {"wall_s": r["wall_s"], "cost": usage.get("cost"), "exec_id": r["exec_id"]}


STOPWORDS = set("и в во не что он на я с со как а то все она так его но да ты к у же вы за бы по "
                 "только ее мне было вот от меня еще нет о из ему теперь когда даже ну вдруг ли "
                 "если уже или ни быть был него до вас нибудь опять уж вам сказал ведь там потом "
                 "себя ничего ей может они тут где есть надо ней для мы тебя их чем была сам чтоб "
                 "без будто чего раз тоже себе под будет ж тогда кто этот того потому этого какой".split())
TOKEN_RE = re.compile(r"[а-яёa-z0-9]+", re.IGNORECASE)


def tokenize(text):
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS and len(t) > 2]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    return dot / (na * nb) if na and nb else 0.0


def main():
    corpus = json.load(open(HERE.parent / "corpus" / "corpus_case1_s10.json", encoding="utf-8"))["corpus_500"]
    byid = {d["id"]: d for d in corpus}
    docs = [byid[i] for i in DEMO_DOC_IDS]
    texts = [d["text"] for d in docs]

    vecs, meta = embed_batch(texts)
    print(f"docs embedded: wall={meta['wall_s']}s cost=${meta['cost']} exec={meta['exec_id']}")
    for d, v in zip(docs, vecs):
        d["embedding"] = v

    q_texts = [q["question"] for q in DEMO_QUESTIONS]
    qvecs, qmeta = embed_batch(q_texts)
    print(f"questions embedded: wall={qmeta['wall_s']}s cost=${qmeta['cost']} exec={qmeta['exec_id']}")

    payloads = []
    for q, qvec in zip(DEMO_QUESTIONS, qvecs):
        q_tokens = set(tokenize(q["question"]))
        kw_scored = []
        for d in docs:
            overlap = len(q_tokens & set(tokenize(d["text"])))
            kw_scored.append((overlap, d["id"]))
        kw_scored.sort(key=lambda x: -x[0])
        keyword_rank = [i for _, i in kw_scored]

        vec_scored = [(cosine(qvec, d["embedding"]), d["id"]) for d in docs]
        vec_scored.sort(key=lambda x: -x[0])
        vector_rank = [i for _, i in vec_scored]

        payloads.append({
            "qid": q["qid"],
            "question": q["question"],
            "gold_doc_id": q["gold_doc_id"],
            # Текст НЕ обрезан: узел «Keyword overlap» на холсте считает пересечение токенов
            # по этому самому тексту, и обрезка увела бы живой keyword_rank_live от того,
            # что посчитан здесь офлайн тем же tokenize (замерено 2026-11-14 — c3q42 на 220
            # символах давал другой keyword_rank, чем на полном тексте).
            "docs": [{"id": d["id"], "text": d["text"], "embedding": d["embedding"]} for d in docs],
            "keyword_rank": keyword_rank,
            "vector_rank": vector_rank,
            "keyword_rank_of_gold": keyword_rank.index(q["gold_doc_id"]) + 1,
            "vector_rank_of_gold": vector_rank.index(q["gold_doc_id"]) + 1,
        })
        print(f"{q['qid']}: keyword_rank_of_gold={payloads[-1]['keyword_rank_of_gold']} "
              f"vector_rank_of_gold={payloads[-1]['vector_rank_of_gold']}")

    total_cost = (meta["cost"] or 0) + (qmeta["cost"] or 0)
    out = {"model": EMBED_MODEL, "n_docs": len(docs), "total_cost_usd": total_cost,
           "payloads": payloads}
    out_path = HERE.parent / "raw" / "case3-n8n-demo-payloads.json"
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"TOTAL cost=${total_cost:.6f}, saved {out_path}")


if __name__ == "__main__":
    main()
