#!/usr/bin/env python3
"""Кейс 1 — рост базы (10/50/200 документов) × 3 варианта (промт-стаффинг,
keyword, vector-RAG), точность + стоимость/латентность. Все LLM/embedding-вызовы —
через вебхук стенда s10-raw-openrouter (харнесс sborka.py), ключ не читается этим файлом.
"""
import json
import re
import time

from harness2 import llm_answer, cosine, contains_answer

data = json.load(open("corpus_case1_embedded.json"))
corpus_all = data["corpus_500"]
questions = data["questions"]

needle = [d for d in corpus_all if d["is_needle"]]
distractors = [d for d in corpus_all if not d["is_needle"]]
assert len(needle) == 10

SIZES = {
    10: needle,
    50: needle + distractors[:40],
    200: needle + distractors[:190],
    500: needle + distractors,
}

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


def keyword_search_top1(corpus_subset, question):
    """Полнотекстовый поиск по ключевым словам: пересечение токенов вопроса и
    документа, нормированное на длину документа (простая TF-эвристика без внешних
    библиотек — ровно тот уровень, на котором многие продакшен-FAQ реально сделаны)."""
    q_tokens = set(tokenize(question))
    best, best_score = None, -1.0
    for doc in corpus_subset:
        d_tokens = tokenize(doc["text"])
        d_set = set(d_tokens)
        overlap = len(q_tokens & d_set)
        score = overlap  # число совпавших уникальных ключевых слов
        if score > best_score:
            best_score = score
            best = doc
    return best, best_score


def vector_search_top1(corpus_subset, qvec):
    best, best_score = None, -1.0
    for doc in corpus_subset:
        s = cosine(qvec, doc["embedding"])
        if s > best_score:
            best_score = s
            best = doc
    return best, best_score


def run():
    results = []
    t_start = time.time()
    for size, subset in SIZES.items():
        full_text = "\n\n---\n\n".join(f"[{d['id']}] {d['text']}" for d in subset)
        print(f"=== corpus size {size} (full-text chars={len(full_text)}) ===")
        for q in questions:
            qid, question, answer, gold = q["qid"], q["question"], q["answer"], q["gold_doc_id"]
            qvec = q["embedding"]

            # (a) промт-стаффинг — вся база в промте
            r_a = llm_answer(question, full_text)
            ok_a = contains_answer(r_a["answer"], answer)
            print(f"  [{size}] (a) {qid} stuffing: ok={ok_a} tok={r_a['prompt_tokens']} "
                  f"cost={r_a['cost']} wall={r_a['wall_s']}s")

            # (b) keyword
            doc_b, score_b = keyword_search_top1(subset, question)
            retrieved_correct_b = (doc_b["id"] == gold)
            r_b = llm_answer(question, doc_b["text"])
            ok_b = contains_answer(r_b["answer"], answer)
            print(f"  [{size}] (b) {qid} keyword: retrieved_correct={retrieved_correct_b} "
                  f"ok={ok_b} tok={r_b['prompt_tokens']} cost={r_b['cost']} wall={r_b['wall_s']}s")

            # (c) vector
            doc_c, score_c = vector_search_top1(subset, qvec)
            retrieved_correct_c = (doc_c["id"] == gold)
            r_c = llm_answer(question, doc_c["text"])
            ok_c = contains_answer(r_c["answer"], answer)
            print(f"  [{size}] (c) {qid} vector: retrieved_correct={retrieved_correct_c} "
                  f"ok={ok_c} tok={r_c['prompt_tokens']} cost={r_c['cost']} wall={r_c['wall_s']}s")

            results.append({
                "corpus_size": size, "qid": qid, "question": question, "reference_answer": answer,
                "gold_doc_id": gold,
                "stuffing": {"model_answer": r_a["answer"], "correct": ok_a,
                             "prompt_tokens": r_a["prompt_tokens"], "completion_tokens": r_a["completion_tokens"],
                             "cost_usd": r_a["cost"], "wall_s": r_a["wall_s"], "exec_id": r_a["exec_id"]},
                "keyword": {"retrieved_doc_id": doc_b["id"], "retrieved_correct": retrieved_correct_b,
                            "keyword_score": score_b, "model_answer": r_b["answer"], "correct": ok_b,
                            "prompt_tokens": r_b["prompt_tokens"], "completion_tokens": r_b["completion_tokens"],
                            "cost_usd": r_b["cost"], "wall_s": r_b["wall_s"], "exec_id": r_b["exec_id"]},
                "vector": {"retrieved_doc_id": doc_c["id"], "retrieved_correct": retrieved_correct_c,
                           "cosine_score": score_c, "model_answer": r_c["answer"], "correct": ok_c,
                           "prompt_tokens": r_c["prompt_tokens"], "completion_tokens": r_c["completion_tokens"],
                           "cost_usd": r_c["cost"], "wall_s": r_c["wall_s"], "exec_id": r_c["exec_id"]},
            })

    # свод по размеру/варианту
    summary = {}
    for size in SIZES:
        rows = [r for r in results if r["corpus_size"] == size]
        n = len(rows)
        summary[str(size)] = {
            "n_questions": n,
            "stuffing": {
                "accuracy": sum(r["stuffing"]["correct"] for r in rows) / n,
                "avg_prompt_tokens": sum(r["stuffing"]["prompt_tokens"] or 0 for r in rows) / n,
                "avg_cost_usd": sum(r["stuffing"]["cost_usd"] or 0 for r in rows) / n,
                "avg_wall_s": sum(r["stuffing"]["wall_s"] or 0 for r in rows) / n,
            },
            "keyword": {
                "accuracy": sum(r["keyword"]["correct"] for r in rows) / n,
                "retrieval_recall@1": sum(r["keyword"]["retrieved_correct"] for r in rows) / n,
                "avg_prompt_tokens": sum(r["keyword"]["prompt_tokens"] or 0 for r in rows) / n,
                "avg_cost_usd": sum(r["keyword"]["cost_usd"] or 0 for r in rows) / n,
                "avg_wall_s": sum(r["keyword"]["wall_s"] or 0 for r in rows) / n,
            },
            "vector": {
                "accuracy": sum(r["vector"]["correct"] for r in rows) / n,
                "retrieval_recall@1": sum(r["vector"]["retrieved_correct"] for r in rows) / n,
                "avg_prompt_tokens": sum(r["vector"]["prompt_tokens"] or 0 for r in rows) / n,
                "avg_cost_usd": sum(r["vector"]["cost_usd"] or 0 for r in rows) / n,
                "avg_wall_s": sum(r["vector"]["wall_s"] or 0 for r in rows) / n,
            },
        }
    elapsed = time.time() - t_start
    out = {"summary": summary, "details": results, "total_wall_s": elapsed,
           "embed_meta": data["embed_meta"], "model": "openai/gpt-4o-mini",
           "embed_model": "openai/text-embedding-3-small"}
    json.dump(out, open("case1-results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"TOTAL wall={elapsed:.1f}s")


if __name__ == "__main__":
    run()
