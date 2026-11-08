#!/usr/bin/env python3
"""Сводка по raw/zamer3-full-20.json (и, если есть, raw/zamer3-judgecheck-20.json) — issue #299.

Печатает по каждому варианту (code/judge/combo[/judge-check]): сошлось/не сошлось,
среднее число попыток, суммарные вызовы модели, суммарную и среднюю стоимость. Не прячет
ошибки — отдельно перечисляет вопросы, где converged=False или outcome содержит error.

Usage:
    python3 analyze_full20.py raw/zamer3-full-20.json
"""
import json
import sys


def summarize(variant, items):
    n = len(items)
    ok_items = [r for r in items if not r.get("error")]
    converged = sum(1 for r in ok_items if r.get("converged"))
    errored = [r for r in items if r.get("error")]
    not_converged = [r for r in ok_items if not r.get("converged")]
    attempts = [r["attempts"] for r in ok_items if "attempts" in r]
    avg_attempts = sum(attempts) / len(attempts) if attempts else 0
    total_calls = sum(r.get("llm_calls", 0) for r in ok_items)
    total_cost = sum(r.get("cost_usd", 0) for r in ok_items)
    print(f"\n=== {variant} ({n} вопросов) ===")
    print(f"  сошлось: {converged}/{n} ({100*converged/n:.0f}%)")
    print(f"  попыток: сумма={sum(attempts)}, среднее={avg_attempts:.2f}, "
          f"разброс={attempts}")
    print(f"  вызовов модели всего: {total_calls}")
    print(f"  стоимость: ${total_cost:.4f} всего, ${total_cost/n:.5f} на вопрос")
    if not_converged:
        print(f"  НЕ сошлось ({len(not_converged)}):")
        for r in not_converged:
            print(f"    - {r['question'][:60]}  (попыток={r['attempts']})")
    if errored:
        print(f"  ОШИБКИ ({len(errored)}):")
        for r in errored:
            print(f"    - {r['question'][:60]}: {r['error']}")
    return {
        "n": n, "converged": converged, "avg_attempts": avg_attempts,
        "total_calls": total_calls, "total_cost": total_cost,
        "not_converged": [r["question"] for r in not_converged],
        "errored": [r["question"] for r in errored],
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "raw/zamer3-full-20.json"
    d = json.load(open(path, encoding="utf-8"))
    summary = {}
    for variant, items in d.get("variants", {}).items():
        summary[variant] = summarize(variant, items)
    grand_calls = sum(s["total_calls"] for s in summary.values())
    grand_cost = sum(s["total_cost"] for s in summary.values())
    print(f"\n=== ИТОГО ({path}) ===")
    print(f"  вызовов модели: {grand_calls}")
    print(f"  стоимость: ${grand_cost:.4f}")
    return summary


if __name__ == "__main__":
    main()
