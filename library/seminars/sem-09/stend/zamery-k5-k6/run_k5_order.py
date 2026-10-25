#!/usr/bin/env python3
"""Замер 3.2 — Кейс 5: порядок полей структурированного вывода. Десять вопросов с
арифметикой внутри («заплатил X, курс стоит Y, сколько вернут») — через ОБЕ схемы:
`С9 · замер K5 — порядок полей, ответ первым` (`s9-m5-order-a`) и `...рассуждение первым`
(`s9-m5-order-b`). Мерит: доля верных ответов (точная арифметика, проверяется в Python,
не моделью) на каждой схеме, на ОДНОЙ и той же модели.

Вопрос №1 обеих схем уже отправлен при проверке монтажа (execution 651 — ответ первым,
652 — рассуждение первым); эти два вызова переиспользуются как повтор №1, не выбрасываются.

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k5_order.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import common

# (заплачено, цена курса) -> верный ответ = заплачено - цена. Числа подобраны так, чтобы
# вычитание не было круглым/угадываемым по шаблону (не кратно 1000, не "очевидная" разница).
PAIRS = [
    (15700, 12000),  # 3700 — уже прогнан на обеих схемах как проверка монтажа (651/652)
    (23450, 18000),  # 5450
    (9800, 7300),    # 2500
    (31200, 24500),  # 6700
    (5600, 4150),    # 1450
    (18990, 15990),  # 3000
    (27300, 19800),  # 7500
    (12450, 9990),   # 2460
    (42100, 35600),  # 6500
    (8700, 6250),    # 2450
]

QUESTION_TEMPLATE = ("Я заплатил за курс {paid} рублей, а сам курс стоит {price} рублей — "
                     "курс отменили до начала. Сколько мне должны вернуть?")

FIRST_PAIR_EXEC = {"s9-m5-order-a": "651", "s9-m5-order-b": "652"}


def expected(paid, price):
    return paid - price


def read_execution(api_url, api_key, exec_id, node_name):
    ex = common.get_execution(api_url, api_key, exec_id)
    run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
    return common.node_output(run_data, node_name)


def run_schema(api_url, api_key, webhook_path, node_name, label):
    results = []
    for i, (paid, price) in enumerate(PAIRS, start=1):
        q = QUESTION_TEMPLATE.format(paid=paid, price=price)
        exp = expected(paid, price)
        if i == 1:
            exec_id = FIRST_PAIR_EXEC[webhook_path]
            out = read_execution(api_url, api_key, exec_id, node_name)
            reused = True
        else:
            resp = common.post_form(webhook_path, q)
            exec_id = common.exec_id_from_waiting_url(resp)
            run_data = common.wait_for_node(api_url, api_key, exec_id, node_name)
            out = common.node_output(run_data, node_name)
            reused = False
        output = (out or {}).get("output", {})
        answer = output.get("answer")
        reasoning = output.get("reasoning")
        correct = (answer == exp)
        results.append({
            "paid": paid, "price": price, "expected": exp, "question": q,
            "execution_id": exec_id, "model_answer": answer, "reasoning": reasoning,
            "correct": correct, "reused_from_wiring_check": reused,
        })
        tag = " (переиспользован)" if reused else ""
        print(f"[{label}] #{i} exec={exec_id}{tag} expected={exp} got={answer} "
              f"correct={correct}")
    return results


def main():
    api_url, api_key = common.env_or_die()
    res_a = run_schema(api_url, api_key, "s9-m5-order-a", "Extract (answer-first)",
                        "ответ первым")
    res_b = run_schema(api_url, api_key, "s9-m5-order-b", "Extract (reasoning-first)",
                        "рассуждение первым")

    n_correct_a = sum(1 for r in res_a if r["correct"])
    n_correct_b = sum(1 for r in res_b if r["correct"])
    out = {
        "schema_answer_first": {"n": len(res_a), "n_correct": n_correct_a, "results": res_a},
        "schema_reasoning_first": {"n": len(res_b), "n_correct": n_correct_b, "results": res_b},
    }
    out_path = Path(__file__).parent / "results-k5-order.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nИТОГО: ответ-первым {n_correct_a}/{len(res_a)}, "
          f"рассуждение-первым {n_correct_b}/{len(res_b)} -> {out_path}")


if __name__ == "__main__":
    main()
