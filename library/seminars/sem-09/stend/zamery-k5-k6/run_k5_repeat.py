#!/usr/bin/env python3
"""Замер 3.1 — Кейс 5: 25 повторов ОДНОГО вопроса на `С9 · замер K5 — повторы T=0`
(вебхук `s9-m5-repeat`), температура 0. Мерит: сколько РАЗНЫХ ответов получилось и
расходятся ли они только формулировкой или ещё и по существу (проверяемая деталь — срок
в рабочих/часах, пороговая сумма).

Вопрос намеренно ВНУТРИ базы знаний (kb4, «Возврат денег») — он несёт две проверяемые
детали: срок (10 рабочих дней) и порог (3000 рублей, решение через руководителя). Первый
вызов этого вопроса в этой сессии уже сделан при проверке монтажа воркфлоу (execution 650,
до правки скрипта запуска никакого исправления не вносилось — вопрос и воркфлоу те же,
что и в последующих 24) — он учитывается как повтор №1, не выбрасывается и не повторяется
вхолостую.

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k5_repeat.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import common

QUESTION = "Когда вернут деньги за отменённый курс?"
FIRST_EXEC_ID = "650"  # уже отправлен при проверке монтажа — переиспользуется, не теряется
N_TOTAL = 25


def run_one(api_url, api_key):
    resp = common.post_form("s9-m5-repeat", QUESTION)
    exec_id = common.exec_id_from_waiting_url(resp)
    run_data = common.wait_for_node(api_url, api_key, exec_id, "Answer (free, T=0)")
    out = common.node_output(run_data, "Answer (free, T=0)")
    text = (out or {}).get("text", "")
    return {"execution_id": exec_id, "answer": text}


def main():
    api_url, api_key = common.env_or_die()
    results = []

    # повтор №1 — уже выполненный execution 650 (проверка монтажа), читаем заново
    ex = common.get_execution(api_url, api_key, FIRST_EXEC_ID)
    run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
    out = common.node_output(run_data, "Answer (free, T=0)")
    results.append({"execution_id": FIRST_EXEC_ID, "answer": (out or {}).get("text", "")})
    print(f"#1 execution={FIRST_EXEC_ID} (переиспользован) -> {results[0]['answer'][:70]}...")

    for i in range(2, N_TOTAL + 1):
        r = run_one(api_url, api_key)
        results.append(r)
        print(f"#{i} execution={r['execution_id']} -> {r['answer'][:70]}...")

    unique_texts = sorted(set(r["answer"] for r in results))
    out = {
        "question": QUESTION, "n_calls": len(results),
        "n_unique_texts": len(unique_texts), "results": results,
    }
    out_path = Path(__file__).parent / "results-k5-repeat.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nИТОГО: {len(results)} вызовов, {len(unique_texts)} РАЗНЫХ по тексту ответов "
          f"-> {out_path}")


if __name__ == "__main__":
    main()
