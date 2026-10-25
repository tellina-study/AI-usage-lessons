#!/usr/bin/env python3
"""Повторный Замер Кейса 5 Семинара 9 (трудный случай) — issue #299.

Три сценария (`sborka.py`), по 10 повторов каждый, температура 0, один и тот же текст
вопроса на всех повторах своего сценария — 30 вызовов всего. Первый вызов каждого сценария
одновременно служит проверкой монтажа (тот же приём, что `zamery-k5-k6/run_k5_repeat.py`
сделал с execution 650) — НЕ лишний вызов сверх 10, засчитывается как повтор №1.

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k5p.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import common

SCENARIOS = [
    {
        "key": "arith",
        "webhook": "s9-m5p-arith",
        "node_name": "Answer (arith, T=0)",
        "question": (
            "Я оплатил курс из 10 занятий на сумму 24000 рублей. Прошло 3 занятия, "
            "дальше ходить не смогу — хочу вернуть деньги за оставшиеся занятия. "
            "Сколько мне должны вернуть?"),
    },
    {
        "key": "boundary",
        "webhook": "s9-m5p-boundary",
        "node_name": "Answer (boundary, T=0)",
        "question": (
            "Я заплатил за курс 3000 рублей и хочу оформить возврат. Решение по моему "
            "возврату будет принимать руководитель, или это пройдёт по обычному порядку?"),
    },
    {
        "key": "combo",
        "webhook": "s9-m5p-combo",
        "node_name": "Answer (combo, T=0)",
        "question": (
            "Я пропустил занятие без предупреждения. Когда будет следующая пересдача, "
            "чтобы я мог на неё попасть?"),
    },
]

N_PER_SCENARIO = 10


def run_one(api_url, api_key, webhook, question, node_name):
    resp = common.post_form(webhook, question)
    exec_id = common.exec_id_from_waiting_url(resp)
    run_data = common.wait_for_node(api_url, api_key, exec_id, node_name)
    out = common.node_output(run_data, node_name)
    text = (out or {}).get("text", "")
    return {"execution_id": exec_id, "answer": text}


def main():
    api_url, api_key = common.env_or_die()
    all_results = {}
    total_calls = 0

    for sc in SCENARIOS:
        print(f"\n=== {sc['key']} ({sc['webhook']}) ===")
        print(f"Вопрос: {sc['question']}")
        results = []
        for i in range(1, N_PER_SCENARIO + 1):
            r = run_one(api_url, api_key, sc["webhook"], sc["question"], sc["node_name"])
            results.append(r)
            total_calls += 1
            tag = " (= проверка монтажа)" if i == 1 else ""
            print(f"#{i} execution={r['execution_id']}{tag} -> {r['answer'][:90]}...")
        unique_texts = sorted(set(r["answer"] for r in results))
        all_results[sc["key"]] = {
            "question": sc["question"], "webhook": sc["webhook"],
            "n_calls": len(results), "n_unique_texts": len(unique_texts),
            "results": results,
        }
        print(f"-- {sc['key']}: {len(results)} вызовов, {len(unique_texts)} "
              f"РАЗНЫХ дословных текстов")

    out_path = Path(__file__).parent / "results-k5p.json"
    out_path.write_text(
        json.dumps({"total_calls": total_calls, "scenarios": all_results},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nИТОГО: {total_calls} вызовов -> {out_path}")


if __name__ == "__main__":
    main()
