#!/usr/bin/env python3
"""Перемер той же пятиправильной проверки, терпимой к русской морфологии — issue #299,
Кейс 3 Семинара 9.

Находка, которая породила этот файл (см. README «Терпимая проверка»): ручная сверка
«решатель выбрал неверный ответ» на замере смеси экспертов (`analyze.py` + `raw/mix-20.json`)
показала, что ВСЕ 6 случаев отказа — артефакт двух хрупких к морфологии правил нашей
собственной проверки, не ошибки модели:

  1. деталь (`kb_keyword`) сверяется ТОЧНОЙ подстрокой в цифровой записи («24 час»,
     «10 рабочих дней», «5 рабочих дней») — модель, написавшая число СЛОВАМИ («двадцать
     четыре часа», «десяти рабочих дней»), проходит смыслово, но не проходит подстрокой;
  2. контакт сверяется точными подстроками `['администратор', 'личный кабинет',
     'преподавател', 'сотрудник', 'руководител']` — «администрацию» не содержит
     «администратор», «личного кабинета» не содержит «личный кабинет» (другая словоформа);
     склонение роняет правило оба раза.

Это НОВАЯ проверка, не правка существующей — `analyze.py` / `code_check_node()` /
`judge_criteria_text()` НЕ меняются (они уже измерены и опубликованы на деке как
«буквальная проверка»). Этот файл — вторая, параллельная проверка той же модели ответов,
результат которой встаёт рядом, а не взамен.

Ни одного нового вызова модели не делает — читает уже сохранённые тексты ответов из
`raw/mix-20.json` и `../zamery-k1-k3/raw/zamer3-judgecheck-20.json`.

Usage: python3 peregreyd_terpimyy.py [--selftest] [--json raw/peregreyd.json]
"""
import importlib.util as _ilu
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
_spec = _ilu.spec_from_file_location(
    "sem09_mix_sborka_zamer3_peregreyd", str(HERE.parent / "zamery-k1-k3" / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

Q_BY_TEXT = {q["question"]: q for q in z3.TEST_QUESTIONS}

# ---------------------------------------------------------------------------------------
# Правило 2 (деталь) — терпимая версия
# ---------------------------------------------------------------------------------------
#
# Словесные формы чисел корпуса (kb2=24, kb3=18, kb4=10 и 3000, kb7=5) — ВСЕ падежи,
# встречающиеся в естественном ответе на эти конкретные вопросы (именительный/винительный,
# родительный/дательный/предложный, инструментальный на случай «двадцатью четырьмя» и т.п.),
# не только падеж, который попался в замере — задание явно требует «для всех деталей
# корпуса, не только попавшихся». Каждый паттерн заякорен с обеих сторон (`\b`), чтобы не
# поймать число внутри другого слова (напр. «пять» не должно сработать на «пятнадцать»,
# см. notes/decisions.md про ложные совпадения без якоря).
NUMBER_WORDS = {
    "5": r"\bпят(?:ь|и|ью)\b",
    "10": r"\bдесят(?:ь|и|ью)\b",
    "18": r"\bвосемнадцат(?:ь|и|ью)\b",
    "24": r"\bдвадцат(?:ь|и|ью)\s+четыр(?:е|ёх|ьмя)\b",
    "3000": r"(?:\bтри\s+тысячи\b|\bтр[ёе]х\s+тысяч(?:ах)?\b|\bтр[ёе]м\s+тысячам\b|"
            r"\bтремя\s+тысячами\b)",
}

# Деталь вида "<цифра> <остаток>" — ровно три вопроса корпуса (kb2 оба, kb4 первый,
# kb7 первый): "24 час", "10 рабочих дней", "5 рабочих дней". Остаток ПОСЛЕ числа
# («час», «рабочих дней») не меняется между цифровой и словесной записью — числительные
# 5/10/24 управляют тем же падежом существительного что цифрой, что словом («10 рабочих
# дней» и «десять рабочих дней» — оба родительный падеж множественного числа), так что
# менять в остатке ничего не нужно; хрупкость была только в самой цифре.
_DIGIT_KEYWORD_RE = re.compile(r"^(\d+)\s+(.+)$")


def has_keyword_tolerant(answer, q):
    """Деталь считается найденной, если видна её цифровая запись, её словесная запись
    (любой падеж из NUMBER_WORDS), либо — для деталей без числа вовсе — уже существующий
    regex (`keyword_pattern`, заведён Починкой 2026-10-26 для kb5) или стем-подстрока
    (`keyword`, уже нечувствителен к окончанию у всех нечисловых деталей корпуса — см.
    комментарий в `sborka_zamer3.py` про выбор стемов). Та часть правила, что НЕ про числа,
    не трогается — она морфологически не хрупкая и уже терпима к склонению."""
    if q.get("keyword_pattern"):
        return re.search(q["keyword_pattern"], answer, re.IGNORECASE) is not None

    kw = q["keyword"]
    m = _DIGIT_KEYWORD_RE.match(kw)
    if not m:
        return kw.lower() in answer.lower()

    digit, rest = m.group(1), m.group(2)
    rest_ok = rest.lower() in answer.lower()
    digit_ok = digit in answer
    word_pattern = NUMBER_WORDS.get(digit)
    word_ok = bool(word_pattern) and re.search(word_pattern, answer, re.IGNORECASE) is not None
    return rest_ok and (digit_ok or word_ok)


# ---------------------------------------------------------------------------------------
# Правило 3 (контакт) — терпимая версия: корень вместо точной словоформы.
# ---------------------------------------------------------------------------------------
# «администратор» → «администра» (ловит и «администрация»/«администрацию» — находка
# руководителя: владелец явно признал «обратитесь в администрацию центра» верным ответом,
# хотя это другое слово, не падеж того же слова — решение закладывается здесь явно, не
# тихо). «личный кабинет» (словосочетание, первое слово склоняется — «личного кабинета»,
# «личном кабинете») → «кабинет» (только второе слово, которое не меняет корень при
# склонении в этом контексте). Три оставшихся стема не менялись — они уже были стемами без
# окончания и уже терпимы к падежу.
CONTACT_STEMS_TOLERANT = ["администра", "кабинет", "преподавател", "сотрудник", "руководител"]


def has_contact_tolerant(answer):
    low = answer.lower()
    return any(stem in low for stem in CONTACT_STEMS_TOLERANT)


# ---------------------------------------------------------------------------------------
# Правила 1, 4, 5 — БЕЗ ИЗМЕНЕНИЙ (не хрупки к морфологии, задание прямо требует их не
# трогать). Скопированы из `analyze.py::passes_rules()` один в один.
# ---------------------------------------------------------------------------------------

def passes_rules_literal(answer, q):
    """Буквальная проверка — копия `analyze.py::passes_rules()`, для сравнения рядом
    (не импортируется напрямую, чтобы этот файл не тянул зависимость на другой каталог
    сверх уже импортированного корпуса вопросов; логика продублирована один в один и ничем
    не отличается от уже опубликованной)."""
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
    if not any(c in answer.lower() for c in z3.CONTACT_PHRASES):
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


def passes_rules_tolerant(answer, q):
    """Та же пятёрка правил, в том же порядке — правила 2 и 3 терпимы к морфологии, 1/4/5
    не изменены.

    Честная оговорка про правило 4 (числа не из базы), требуемая заданием явно: если
    деталь-число написана словами, в тексте МОЖЕТ не быть ни одной цифры вовсе — тогда
    `re.findall(r"\\d+", answer)` возвращает пустой список, и правило 4 проходит
    ВПУСТУЮ (нет цифр — нет нарушения), а не потому что что-то проверено и подтверждено.
    Это не дырка: случай, где модель пишет ЧУЖОЕ число словами (не являющееся числом из
    базы), этим правилом в любом случае не пойман — ни буквальной, ни терпимой версией,
    потому что оно ищет только цифры. Эта граница была и раньше (правило всегда искало
    цифры, не числительные), терпимая проверка её не расширяет и не сужает — только
    называет явно, как и требует задание."""
    if answer is None:
        return False, ["нет ответа"]
    reasons = []
    if len(answer) > 280:
        reasons.append("длиннее 280 символов")
    if not has_keyword_tolerant(answer, q):
        reasons.append(f"нет детали «{q['keyword']}» (ни цифрой, ни словом)")
    if not has_contact_tolerant(answer):
        reasons.append("не указано, куда обращаться дальше (терпимая проверка)")
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


# ---------------------------------------------------------------------------------------
# Самопроверка на нарочно испорченном входе (канон: «чужой сторож проверять поломкой
# своего кадра, не доверием к фикстурам» — здесь это сторож СВОЙ, применяется тот же
# принцип: проверить на входе, который ОБЯЗАН быть отвергнут, прежде чем доверять проверке
# на реальных данных).
# ---------------------------------------------------------------------------------------

def selftest():
    q2 = Q_BY_TEXT["Можно ли перенести занятие, если я заболел?"]  # kb2, keyword "24 час"
    q4b = Q_BY_TEXT["Когда мне вернут деньги за отменённый курс?"]  # kb4, "10 рабочих дней"

    cases = []

    # 1. Верное число словами — ОБЯЗАНО пройти (это и есть предмет находки).
    good_word = ("Занятие можно перенести не позднее чем за двадцать четыре часа до начала "
                 "— обратитесь к администратору.")
    ok, reasons = has_keyword_tolerant(good_word, q2), None
    cases.append(("24 словами, верно → деталь найдена", ok, True))

    # 2. ИСПОРЧЕННЫЙ вход — то же самое предложение, но «двадцать пять» вместо «двадцать
    #    четыре» (задание прямо требует этот тест). ОБЯЗАНО быть отвергнуто.
    bad_word = ("Занятие можно перенести не позднее чем за двадцать пять часов до начала "
                "— обратитесь к администратору.")
    ok_bad = has_keyword_tolerant(bad_word, q2)
    cases.append(("25 словами вместо 24 → деталь НЕ найдена (не поддавок)", not ok_bad, True))

    # 3. Цифрой, как раньше — ОБЯЗАНО продолжать проходить (не регрессия буквальной формы).
    good_digit = "Перенос возможен не позднее чем за 24 часа. Обратитесь к администратору."
    cases.append(("24 цифрой, как раньше → деталь найдена", has_keyword_tolerant(good_digit, q2), True))

    # 4. Другое число цифрой, неверное — ОБЯЗАНО быть отвергнуто.
    bad_digit = "Перенос возможен не позднее чем за 25 часов. Обратитесь к администратору."
    cases.append(("25 цифрой вместо 24 → деталь НЕ найдена", not has_keyword_tolerant(bad_digit, q2), True))

    # 5. «10 рабочих дней» словами, верно.
    good_10 = "Возврат оформляется в течение десяти рабочих дней. Обратитесь к руководителю."
    cases.append(("10 словами, верно → деталь найдена", has_keyword_tolerant(good_10, q4b), True))

    # 6. «10 рабочих дней» словами, но испорченное число (одиннадцать вместо десяти).
    bad_10 = "Возврат оформляется в течение одиннадцати рабочих дней. Обратитесь к руководителю."
    cases.append(("11 словами вместо 10 → деталь НЕ найдена", not has_keyword_tolerant(bad_10, q4b), True))

    # 7. Контакт: «администрацию» (другое слово, не словоформа) — ОБЯЗАНО пройти (решение
    #    владельца, явно заложенное в CONTACT_STEMS_TOLERANT).
    cases.append(("контакт «администрацию» → найден", has_contact_tolerant("Обратитесь в администрацию."), True))

    # 8. Контакт: «личного кабинета» (другой падеж) — ОБЯЗАНО пройти.
    cases.append(("контакт «личного кабинета» → найден",
                   has_contact_tolerant("См. объявление личного кабинета."), True))

    # 9. Контакт: вообще никакого упоминания — ОБЯЗАНО быть отвергнуто (терпимость не
    #    должна означать «любой текст проходит»).
    cases.append(("контакт отсутствует вовсе → НЕ найден",
                   not has_contact_tolerant("Занятие переносится автоматически."), True))

    print("=== Самопроверка терпимой проверки на нарочно испорченном входе ===")
    all_ok = True
    for name, got, expect in cases:
        status = "OK" if got == expect else "FAIL"
        if got != expect:
            all_ok = False
        print(f"  [{status}] {name}")
    if not all_ok:
        print("\nСАМОПРОВЕРКА ПРОВАЛЕНА — терпимая проверка НЕ применяется к реальным данным.")
        sys.exit(1)
    print("Все 9 случаев прошли как ожидалось — терпимая проверка не поддавок.\n")


# ---------------------------------------------------------------------------------------
# Перегрейд mix-20.json (смесь экспертов)
# ---------------------------------------------------------------------------------------

LETTER_TO_KEY = {"A": "qwen", "B": "llama", "C": "ministral"}


def regrade_mix(mix_path):
    data = json.loads(mix_path.read_text(encoding="utf-8"))
    results = data["results"]
    assert len(results) == 20

    rows = []
    for idx, r in enumerate(results, start=1):
        q = Q_BY_TEXT[r["question"]]
        per_expert = {}
        for key_, info in r["experts"].items():
            text = info.get("text")
            lit_ok, lit_reasons = passes_rules_literal(text, q)
            tol_ok, tol_reasons = passes_rules_tolerant(text, q)
            per_expert[key_] = {
                "text": text, "literal_ok": lit_ok, "literal_reasons": lit_reasons,
                "tolerant_ok": tol_ok, "tolerant_reasons": tol_reasons,
            }
        chosen_letter = r["resolver"]["choice"]
        chosen_key = LETTER_TO_KEY.get(chosen_letter)
        rows.append({
            "idx": idx, "question": r["question"], "kb_id": q["kb_id"],
            "per_expert": per_expert, "chosen_letter": chosen_letter, "chosen_key": chosen_key,
            "llm_calls": r["llm_calls"], "total_cost_usd": r["total_cost_usd"],
            "total_tokens_in": r["total_tokens_in"], "total_tokens_out": r["total_tokens_out"],
        })
    return rows


def five_numbers(rows, column):
    """column: 'literal_ok' или 'tolerant_ok'."""
    n_resolver_correct = 0
    n_any_expert_correct = 0
    n_chose_wrong_when_correct_available = 0
    for row in rows:
        per_expert_ok = {k: v[column] for k, v in row["per_expert"].items()}
        any_correct = any(per_expert_ok.values())
        chosen_ok = per_expert_ok.get(row["chosen_key"], False) if row["chosen_key"] else False
        if chosen_ok:
            n_resolver_correct += 1
        if any_correct:
            n_any_expert_correct += 1
        if any_correct and not chosen_ok:
            n_chose_wrong_when_correct_available += 1
    return {
        "resolver_correct": n_resolver_correct,
        "any_expert_correct": n_any_expert_correct,
        "chose_wrong_when_available": n_chose_wrong_when_correct_available,
    }


def per_expert_accuracy(rows, column):
    out = {}
    for key_ in ("qwen", "llama", "ministral"):
        n_ok = sum(1 for row in rows if row["per_expert"][key_][column])
        out[key_] = n_ok
    return out


def diff_report(rows):
    """Построчный разбор: что именно перешло из неверных в верные и по какому правилу."""
    flips = []
    for row in rows:
        for key_, info in row["per_expert"].items():
            if (not info["literal_ok"]) and info["tolerant_ok"]:
                flips.append({
                    "idx": row["idx"], "kb_id": row["kb_id"], "expert": key_,
                    "was_chosen": row["chosen_key"] == key_,
                    "literal_reasons": info["literal_reasons"],
                    "text": info["text"],
                })
            elif info["literal_ok"] and (not info["tolerant_ok"]):
                # ОБЯЗАНО не встречаться — терпимая проверка только добавляет случаи,
                # никогда не отбирает уже пройденные литерально.
                flips.append({
                    "idx": row["idx"], "kb_id": row["kb_id"], "expert": key_,
                    "REGRESSION": True, "tolerant_reasons": info["tolerant_reasons"],
                    "text": info["text"],
                })
    return flips


# ---------------------------------------------------------------------------------------
# Перегрейд zamer3-judgecheck-20.json (вариант «судья»)
# ---------------------------------------------------------------------------------------

def regrade_judgecheck(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for r in data["results"]:
        q = Q_BY_TEXT[r["question"]]
        answer = r["answer"]
        lit_ok, lit_reasons = passes_rules_literal(answer, q)
        tol_ok, tol_reasons = passes_rules_tolerant(answer, q)
        rows.append({
            "question": r["question"], "kb_id": q["kb_id"], "answer": answer,
            "orig_code_ok": r["code_ok"], "orig_code_reason": r["code_reason"],
            "judge_ok": r["judge_ok"],
            "literal_ok": lit_ok, "literal_reasons": lit_reasons,
            "tolerant_ok": tol_ok, "tolerant_reasons": tol_reasons,
        })
    return rows


def main():
    args = sys.argv[1:]
    out_path = Path("raw/peregreyd.json")
    if "--json" in args:
        out_path = Path(args[args.index("--json") + 1])

    selftest()

    mix_path = HERE / "raw" / "mix-20.json"
    perm_path = HERE / "raw" / "permutatsiya-8.json"
    judgecheck_path = HERE.parent / "zamery-k1-k3" / "raw" / "zamer3-judgecheck-20.json"

    rows = regrade_mix(mix_path)

    lit5 = five_numbers(rows, "literal_ok")
    tol5 = five_numbers(rows, "tolerant_ok")
    lit_per = per_expert_accuracy(rows, "literal_ok")
    tol_per = per_expert_accuracy(rows, "tolerant_ok")
    flips = diff_report(rows)
    regressions = [f for f in flips if f.get("REGRESSION")]

    print("=== Смесь экспертов — буквальная против терпимой (raw/mix-20.json) ===")
    print(f"1. Верных после смеси (выбор решателя прошёл правила):"
          f" буквальная {lit5['resolver_correct']}/20, терпимая {tol5['resolver_correct']}/20")
    print(f"2. Верный ответ среди трёх экспертов (потолок приёма):"
          f" буквальная {lit5['any_expert_correct']}/20, терпимая {tol5['any_expert_correct']}/20")
    print(f"3. Решатель выбрал неверный при наличии верного:"
          f" буквальная {lit5['chose_wrong_when_available']}/20,"
          f" терпимая {tol5['chose_wrong_when_available']}/20")
    print("4. Цена — не меняется (нет новых вызовов модели)")
    if perm_path.exists():
        perm = json.loads(perm_path.read_text(encoding="utf-8"))
        held = sum(1 for it in perm["items"] if it["held"])
        total = len(perm["items"])
        print(f"5. Устойчивость к порядку: {held}/{total} ({held/total:.0%}) — грейдинг "
              f"на это число НЕ влияет (held считается по идентичности выбора, не по "
              f"формальной верности), число то же в обеих колонках")

    print("\n=== По экспертам — доля формально верных (независимо, 20 вопросов) ===")
    for key_ in ("qwen", "llama", "ministral"):
        print(f"  {key_:10s}: буквальная {lit_per[key_]}/20 ({lit_per[key_]/20:.0%}), "
              f"терпимая {tol_per[key_]}/20 ({tol_per[key_]/20:.0%})")

    print(f"\n=== Переходы «неверно → верно» под терпимой проверкой: {len(flips) - len(regressions)} ===")
    for f in flips:
        if f.get("REGRESSION"):
            continue
        tag = " (ВЫБРАН РЕШАТЕЛЕМ)" if f["was_chosen"] else ""
        print(f"  Q{f['idx']:>2} ({f['kb_id']}) {f['expert']}{tag}: было «{'; '.join(f['literal_reasons'])}»")

    print(f"\n=== Регрессий (было верно буквально, стало неверно терпимо): {len(regressions)} ===")
    for f in regressions:
        print(f"  !!! Q{f['idx']} ({f['kb_id']}) {f['expert']}: {f['tolerant_reasons']}")

    jc_rows = []
    if judgecheck_path.exists():
        jc_rows = regrade_judgecheck(judgecheck_path)
        jc_lit_ok = sum(1 for r in jc_rows if r["literal_ok"])
        jc_tol_ok = sum(1 for r in jc_rows if r["tolerant_ok"])
        jc_orig_ok = sum(1 for r in jc_rows if r["orig_code_ok"])
        jc_flips = [r for r in jc_rows if (not r["literal_ok"]) and r["tolerant_ok"]]
        jc_regressions = [r for r in jc_rows if r["literal_ok"] and not r["tolerant_ok"]]
        print(f"\n=== Вариант «судья» (zamer3-judgecheck-20.json, перегрейд поля answer) ===")
        print(f"  Исходный code_ok (JS-проверка на стенде, литеральная): {jc_orig_ok}/20")
        print(f"  Наша литеральная копия (Python, та же логика): {jc_lit_ok}/20")
        print(f"  Терпимая: {jc_tol_ok}/20")
        print(f"  Переходов неверно→верно: {len(jc_flips)}, регрессий: {len(jc_regressions)}")
        if not jc_flips and not jc_regressions:
            print("  Терпимая проверка НИЧЕГО не меняет на этом наборе (ожидаемо — см. README: "
                  "это попытки-1 кодового варианта, они уже проходили литеральную проверку по "
                  "построению; расхождение code_ok vs judge_ok тут — самопротиворечие "
                  "модели-судьи, не морфология)")

    out = {
        "mix": {
            "literal_five": lit5, "tolerant_five": tol5,
            "literal_per_expert": lit_per, "tolerant_per_expert": tol_per,
            "flips": [f for f in flips if not f.get("REGRESSION")],
            "regressions": regressions,
            "rows": rows,
        },
        "judgecheck": jc_rows,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nЗаписано: {out_path}")


if __name__ == "__main__":
    main()
