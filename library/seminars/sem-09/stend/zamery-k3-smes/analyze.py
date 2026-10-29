#!/usr/bin/env python3
"""Сводка по замеру «смесь экспертов» — issue #299, задание З4, Часть Б.

Грейдинг — ТА ЖЕ логика, что `code_check_node()` в `zamery-k1-k3/sborka_zamer3.py` (JS-узел
«Code check», уже измеренный и опубликованный в n40/n40a), переписанная на Python и
применённая к реально полученным текстам ответов (не к шаблону, не к самоотчёту модели):
не длиннее 280 символов; содержит нужную деталь (стем/`keyword_pattern`); называет, куда
обращаться дальше; не содержит чисел вне пункта базы; целиком на русском (без латиницы и
иероглифов). Пять правил — те же, что уже стоят в промте генератора и решателя, грейдер их
не придумывает заново, только воспроизводит механически.

Usage: python3 analyze.py raw/mix-20.json raw/permutatsiya-8.json
"""
import importlib.util as _ilu
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
_spec = _ilu.spec_from_file_location(
    "sem09_mix_sborka_zamer3_analyze", str(HERE.parent / "zamery-k1-k3" / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

Q_BY_TEXT = {q["question"]: q for q in z3.TEST_QUESTIONS}
CONTACT_PHRASES = z3.CONTACT_PHRASES

# Прайс OpenRouter, GET https://openrouter.ai/api/v1/models без авторизации, 2026-10-29.
PRICES = {
    "qwen/qwen-2.5-7b-instruct": (0.0000001, 0.0000002),
    "meta-llama/llama-3.1-8b-instruct": (0.00000005, 0.00000008),
    "mistralai/ministral-8b-2512": (0.00000015, 0.00000015),
}
EXPERT_MODEL = {"qwen": "qwen/qwen-2.5-7b-instruct",
                "llama": "meta-llama/llama-3.1-8b-instruct",
                "ministral": "mistralai/ministral-8b-2512"}


def passes_rules(answer, q):
    """Копия code_check_node(): пять правил, в том же порядке, та же логика regex/includes."""
    if answer is None:
        return False, ["нет ответа"]
    reasons = []
    if len(answer) > 280:
        reasons.append("длиннее 280 символов")
    kw_pattern = q.get("keyword_pattern")
    if kw_pattern:
        has_kw = re.search(kw_pattern, answer, re.IGNORECASE) is not None
    else:
        has_kw = q["keyword"].lower() in answer.lower()
    if not has_kw:
        reasons.append(f"нет детали «{q['keyword']}»")
    if not any(c in answer.lower() for c in CONTACT_PHRASES):
        reasons.append("не указано, куда обращаться дальше")
    nums = re.findall(r"\d+", answer)
    allowed = set(q["numbers"])
    bad_nums = [n for n in nums if n not in allowed]
    if bad_nums:
        reasons.append("числа не из базы: " + ",".join(bad_nums))
    if re.search(r"[A-Za-z]", answer):
        reasons.append("есть латиница")
    if re.search(r"[一-鿿]", answer):
        reasons.append("есть иероглифы")
    return len(reasons) == 0, reasons


def main():
    mix_path = Path(sys.argv[1] if len(sys.argv) > 1 else "raw/mix-20.json")
    perm_path = Path(sys.argv[2] if len(sys.argv) > 2 else "raw/permutatsiya-8.json")

    data = json.loads(mix_path.read_text(encoding="utf-8"))
    results = data["results"]
    assert len(results) == 20, f"ожидалось 20, получено {len(results)}"

    rows = []
    n_resolver_correct = 0
    n_any_expert_correct = 0
    n_chose_wrong_when_correct_available = 0
    total_calls = 0
    total_cost = 0.0
    total_tokens_in = total_tokens_out = 0

    for r in results:
        q = Q_BY_TEXT[r["question"]]
        letter_to_key = {"A": "qwen", "B": "llama", "C": "ministral"}
        per_expert_ok = {}
        for key_, info in r["experts"].items():
            ok, reasons = passes_rules(info.get("text"), q)
            per_expert_ok[key_] = ok

        any_correct = any(per_expert_ok.values())
        chosen_letter = r["resolver"]["choice"]
        chosen_key = letter_to_key.get(chosen_letter)
        chosen_ok = per_expert_ok.get(chosen_key, False) if chosen_key else False

        if chosen_ok:
            n_resolver_correct += 1
        if any_correct:
            n_any_expert_correct += 1
        if any_correct and not chosen_ok:
            n_chose_wrong_when_correct_available += 1

        total_calls += r["llm_calls"]
        total_cost += r["total_cost_usd"]
        total_tokens_in += r["total_tokens_in"]
        total_tokens_out += r["total_tokens_out"]

        rows.append({
            "question": r["question"][:60], "kb_id": q["kb_id"],
            "per_expert_ok": per_expert_ok, "any_correct": any_correct,
            "chosen": chosen_letter, "chosen_key": chosen_key, "chosen_ok": chosen_ok,
        })

    print("=== Часть Б — пять чисел ===")
    print(f"1. Верных после смеси экспертов (выбор решателя прошёл 5 правил): "
          f"{n_resolver_correct}/20 ({n_resolver_correct/20:.0%})")
    print(f"2. Верный ответ был среди трёх экспертов (потолок приёма): "
          f"{n_any_expert_correct}/20 ({n_any_expert_correct/20:.0%})")
    print(f"3. Решатель выбрал неверный при наличии верного среди трёх: "
          f"{n_chose_wrong_when_correct_available}/20 "
          f"({n_chose_wrong_when_correct_available/max(n_any_expert_correct,1):.0%} от "
          f"случаев, где верный был доступен)")
    print(f"4. Цена: {total_calls} вызовов модели на 20 вопросов "
          f"({total_calls/20:.1f} вызовов/вопрос), "
          f"{total_tokens_in} токенов вход + {total_tokens_out} токенов выход, "
          f"${total_cost:.5f} суммарно (${total_cost/20:.6f}/вопрос)")

    if perm_path.exists():
        perm = json.loads(perm_path.read_text(encoding="utf-8"))
        held = sum(1 for it in perm["items"] if it["held"])
        total = len(perm["items"])
        print(f"5. Держится ли выбор за порядок: удержался в {held}/{total} "
              f"({held/total:.0%}) случаях на подвыборке из {total} вопросов")

    print("\n=== По экспертам — доля верных ответов (независимо) ===")
    for key_ in ("qwen", "llama", "ministral"):
        n_ok = sum(1 for row in rows if row["per_expert_ok"][key_])
        print(f"  {key_:10s} ({EXPERT_MODEL[key_]:35s}): {n_ok}/20 ({n_ok/20:.0%})")

    print("\n=== Решатель — какую позицию выбирал (устройство замера: A=qwen,B=llama,C=ministral) ===")
    from collections import Counter
    cnt = Counter(row["chosen"] for row in rows)
    for letter in ("A", "B", "C"):
        print(f"  {letter} ({letter_to_key[letter]:10s}): {cnt.get(letter, 0)}/20")

    print("\n=== Построчно ===")
    for row in rows:
        print(f"  {row['kb_id']:4s} {row['question']:62s} эксперты_ок={row['per_expert_ok']} "
              f"выбор={row['chosen']}({row['chosen_key']}) выбор_верен={row['chosen_ok']}")


if __name__ == "__main__":
    main()
