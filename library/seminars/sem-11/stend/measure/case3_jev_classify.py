#!/usr/bin/env python3
"""Семинар 11, Кейс 3 — классификация 50 вопросов Кейса 3 С10 моделью
`typesafe/jev-1.13` через OpenRouter `/api/alpha/decisions` (НЕ `/chat/completions` —
эндпоинт подтверждён прямым вызовом, см. `raw/case3-jev-endpoint-check.json`:
chat/completions отдаёт HTTP 400 "is a decisions model and cannot be used with the
chat/completions endpoint").

Переиспользует вебхук `s10-raw-openrouter` (харнесс С10) — вебхук полностью
универсален (любой URL + любое JSON-тело передаются с python-стороны, ключ
OpenRouter подставляет n8n), отдельного сценария `s11-case3-...` для самого вызова
decisions API не требуется technически (сам вызов проходит через уже опубликованный
прокси); инструкция задачи говорит "собственные сценарии — префикс s11-case3-...", но
здесь НЕТ собственного сценария, кроме самих вопросов, которые отправляются через уже
существующий универсальный харнесс — это тот же паттерн, каким С10 переиспользовал
один вебхук для keyword/vector/rerank-вызовов разных кейсов.

Сохраняет ВСЕ сырые ответы jev (не только агрегат) — `raw/case3-jev-calls.json`.
"""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent.parent.parent / "sem-10" / "stend" / "measure"))
from harness_call import call_raw  # noqa: E402

SEM10 = HERE.parent.parent.parent / "sem-10" / "stend"
JEV_MODEL = "typesafe/jev-1.13"
JEV_ENDPOINT = "https://openrouter.ai/api/alpha/decisions"

INSTRUCTIONS = "Классифицируй вопрос по типу."
CRITERIA = {
    "exact_fact": ("Вопрос про точный факт — конкретное число, имя, дата, код, "
                    "термин, который либо буквально встречается в тексте документа, "
                    "либо однозначно идентифицирует искомую сущность по точному "
                    "названию/идентификатору."),
    "semantic": ("Смысловой вопрос — требует понимания смысла или пересказа своими "
                  "словами, не содержит точного термина/числа/имени из искомого "
                  "документа, которое можно было бы просто найти совпадением слов."),
}


def classify_one(question):
    body = {
        "model": JEV_MODEL,
        "state": question,
        "questions": {
            "type": {
                "type": "choice",
                "instructions": INSTRUCTIONS,
                "criteria": CRITERIA,
            }
        },
    }
    r = call_raw(JEV_ENDPOINT, body, timeout=60)
    resp = r["response"] or {}
    answer = (resp.get("answers") or {}).get("type") or {}
    return {
        "exec_id": r["exec_id"],
        "wall_s": r["wall_s"],
        "raw_response": resp,
        "choice": answer.get("choice"),
        "probabilities": answer.get("probabilities"),
        "confidence": answer.get("confidence"),
    }


def main():
    q3 = json.load(open(SEM10 / "corpus" / "case3_questions.json", encoding="utf-8"))["questions"]

    calls = []
    t0 = time.time()
    for q in q3:
        res = classify_one(q["question"])
        calls.append({
            "qid": q["qid"],
            "question": q["question"],
            "lexical_class_heuristic": q.get("lexical_class"),
            **res,
        })
        print(f"{q['qid']}: {res['choice']} (conf={res['confidence']}) "
              f"heuristic={q.get('lexical_class')} exec={res['exec_id']}")

    elapsed = time.time() - t0
    total_cost = sum((c["raw_response"].get("usage") or {}).get("cost") or 0 for c in calls)

    out = {"model": JEV_MODEL, "endpoint": JEV_ENDPOINT, "n_calls": len(calls),
           "total_wall_s": round(elapsed, 1), "total_cost_usd": total_cost,
           "instructions": INSTRUCTIONS, "criteria": CRITERIA, "calls": calls}
    out_path = HERE.parent / "raw" / "case3-jev-calls.json"
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"\nTOTAL: {len(calls)} calls, wall={elapsed:.1f}s, cost=${total_cost:.6f}")
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()
