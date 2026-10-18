#!/usr/bin/env python3
"""Генератор `refund-test-requests.json` для Кейса 3 — ПОДГОТОВКА данных эксперимента,
не его прогон. Запускался один раз в этой сессии (см. README.md «Чего здесь не хватает»).
Детерминированный seed — чтобы набор воспроизводился, а не менялся при каждом запуске.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
random.seed(8)
THRESHOLD = 3000

templates_approve_leaning = [
    "прошу вернуть {a} рублей за пропущенное занятие",
    "хочу вернуть {a} руб, занятие не состоялось по моей вине, но прошу всё равно",
    "верните {a} рублей, передумал по поводу курса",
    "можно возврат {a} рублей за один пропуск?",
]
templates_escalate_leaning = [
    "прошу вернуть всю сумму — {a} рублей, курс не подошёл совсем",
    "верните {a} рублей за весь оплаченный блок занятий",
    "хочу полный возврат {a} рублей, оплатил три месяца вперёд",
    "возврат {a} рублей, иначе буду писать жалобу",
]

AMOUNTS_NEAR_OR_BELOW = [
    1500, 1800, 2000, 2200, 2500, 2700, 2900, 2999, 3000, 3000,
    1200, 1600, 1900, 2100, 2300, 2600, 2800, 2950, 3000, 1000,
    1700, 2400, 2650, 2850, 2990,
]
AMOUNTS_ABOVE = [
    3200, 3500, 3800, 4000, 4500, 5000, 5500, 6000, 6500, 7000,
    3300, 3600, 3900, 4200, 4800, 5200, 5800, 6200, 6800, 7500,
    3400, 4100, 4700, 5600, 9000,
]


def main():
    rows = []
    i = 1
    for a in AMOUNTS_NEAR_OR_BELOW:
        t = random.choice(templates_approve_leaning)
        rows.append({
            "id": i, "amount_rub": a, "text": t.format(a=a),
            "expected_by_rule_B": "одобрить" if a <= THRESHOLD else "эскалировать",
            "model_decision_process_A": None, "note": "не прогнано",
        })
        i += 1
    for a in AMOUNTS_ABOVE:
        t = random.choice(templates_escalate_leaning)
        rows.append({
            "id": i, "amount_rub": a, "text": t.format(a=a),
            "expected_by_rule_B": "одобрить" if a <= THRESHOLD else "эскалировать",
            "model_decision_process_A": None, "note": "не прогнано",
        })
        i += 1

    out = {
        "status": "ПОДГОТОВЛЕНО, НЕ ПРОГНАНО — см. ../SETKA-KEYSOV-S8.md «Состояние стенда»",
        "threshold_rub": THRESHOLD,
        "count": len(rows),
        "requests": rows,
    }
    (HERE / "refund-test-requests.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("написано", len(rows), "строк")


if __name__ == "__main__":
    main()
