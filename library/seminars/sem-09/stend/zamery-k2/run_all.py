#!/usr/bin/env python3
"""Кейс 2 — пять серий замеров по структурированию базы в промте, issue #299.

Правка владельца 2026-10-27. Пять направлений, каждое ≥10 вызовов на живом стенде через
`harness.py` (webhook `s9-k2-experiment`):
    A — неизменный префикс в начале промта (важность для кэша): латентность стабильного
        префикса против перемешиваемого.
    B — структурирование/форматирование: обычный список против markdown-заголовков против
        списка с краткими описаниями.
    C — расположение данных: нужный пункт в начале/середине/конце списка (lost-in-the-middle
        на своей короткой FAQ-базе — замер, которого не было: `research/05`, раздел «Что
        проверить своим замером», пункт 4, был спроектирован, но не прогнан).
    D — формулировка правил: обычная проза против строгой условной формы «ЕСЛИ…ТО…» — на тех
        же вопросах про сравнение чисел, что уже дали ошибки в Кейсе 1 (n13, n13a).
    E — вопрос клиента повторён и до, и после списка базы против вопроса только после.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_all.py --dims ABCDE --output raw/zamer_k2.json
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from harness import call, grade  # noqa: E402

KB_ITEMS = [
    ("kb1", "Оплата", "Курс оплачивается на сайте по ссылке в личном кабинете (карта, "
     "Робокасса) или наличными на ресепшене при личном визите. Рассрочка не предусмотрена."),
    ("kb2", "Перенос занятия", "Перенести конкретное занятие можно не позднее чем за 24 "
     "часа до его начала — через личный кабинет (кнопка «Перенести») или сообщением "
     "администратору. Позже 24 часов занятие считается использованным."),
    ("kb3", "Документы при поступлении", "Нужен паспорт (копия разворота) и СНИЛС; если "
     "студенту не исполнилось 18 лет — согласие одного из родителей, бланк в личном "
     "кабинете."),
    ("kb4", "Возврат денег", "Возврат оформляется в течение 10 рабочих дней на карту, с "
     "которой была оплата. Для сумм выше 3000 рублей решение проходит через руководителя, "
     "это дольше стандартного срока."),
    ("kb5", "Пересдача пропущенного занятия", "Пересдачи идут каждую вторую субботу "
     "месяца, расписание публикуется в объявлениях личного кабинета за неделю."),
    ("kb6", "Пропуск без предупреждения", "Занятие считается проведённым, бесплатного "
     "повтора не предусмотрено — действует то же правило, что и перенос позже 24 часов."),
    ("kb7", "Сертификат", "Электронный сертификат формируется автоматически и появляется "
     "в личном кабинете в течение 5 рабочих дней после последнего занятия курса."),
    ("kb8", "Перевод на другой курс", "Перевод возможен при наличии мест на новом курсе; "
     "разница в стоимости пересчитывается администратором индивидуально."),
    ("kb9", "Работа в праздники", "Центр не работает в государственные праздники РФ, "
     "занятия на эти даты переносятся автоматически, уведомление приходит в личный "
     "кабинет."),
    ("kb10", "Связь с преподавателем", "Написать конкретному преподавателю можно через "
     "раздел «Сообщения» личного кабинета, ответ приходит в течение одного рабочего дня."),
]
KB_BY_ID = {k: (t, b) for k, t, b in KB_ITEMS}

SYS_INSTRUCTION = ("Ты — ассистент поддержки учебного центра. Ниже база знаний, которой "
                    "можно пользоваться для ответа.\n\n")
TAIL_INSTRUCTION = ("\n\nОтветь по существу и по-русски, коротко (2-4 предложения). Если "
                     "ответа в базе знаний нет и ты не уверена — честно напиши, что не "
                     "знаешь. Если уверена — отвечай прямо, без оговорок.")


def kb_plain(items):
    return "База знаний учебного центра:\n" + "\n".join(
        f"{k} · {t}: {b}" for k, t, b in items)


def kb_headers(items):
    return "\n".join(f"### {k} — {t}\n{b}" for k, t, b in items)


def kb_with_desc(items):
    lines = []
    for k, t, b in items:
        desc = {
            "kb1": "про оплату и рассрочку", "kb2": "про перенос занятия",
            "kb3": "про документы при поступлении", "kb4": "про возврат денег",
            "kb5": "про пересдачу пропущенного", "kb6": "про пропуск без предупреждения",
            "kb7": "про сертификат", "kb8": "про перевод на другой курс",
            "kb9": "про праздники", "kb10": "про связь с преподавателем",
        }.get(k, "")
        lines.append(f"{k} ({desc}) · {t}: {b}")
    return "База знаний учебного центра:\n" + "\n".join(lines)


# ---- вопросы (подмножество трудных вопросов Кейса 1, для прямой сравнимости) ----
QUESTIONS = [
    {"kb_id": "kb1", "q": "А можно оплатить курс в рассрочку на 3 месяца?",
     "must": [r"не предусмотрен|нельзя|нет\b"]},
    {"kb_id": "kb2", "q": "Если до начала занятия осталось всего 2 часа — ещё можно его "
     "перенести?", "must": [r"нельзя|невозможн|не\s+полож|не\s+удастся|не\s+может"]},
    {"kb_id": "kb4", "q": "Я оплатил 2500 рублей — моё возвращение пройдёт через "
     "руководителя?", "must": [r"нет\b|не\s+(будет|пройдёт|через)|обычн"]},
    {"kb_id": "kb5", "q": "Можно договориться о пересдаче в будний день, если субботой не "
     "получается?", "must": [r"нет\b|нельзя|только.{0,20}суббот"]},
    {"kb_id": "kb7", "q": "Можно получить сертификат сразу после оплаты, ещё до начала "
     "занятий?", "must": [r"нет\b|после.{0,20}последн|только.{0,20}после"]},
    {"kb_id": "kb9", "q": "А летние каникулы у учебного центра есть — занятия "
     "останавливаются на месяц?", "must": [r"нет\b|не\s+знаю|база.{0,20}(не\s+сказ|молч|нет)"]},
    {"kb_id": "kb2/kb6", "q": "Если я предупредил о пропуске заранее, за двое суток — будет "
     "бесплатный перенос?", "must": [r"да\b|полож|доступ|можно"]},
]


def run_group(label, prompt_builder, questions, n=None):
    qs = questions if n is None else questions[:n]
    results = []
    for q in qs:
        prompt = prompt_builder(q)
        r = call(prompt)
        ok, reason = grade(r["text"], q["must"])
        r.update({"label": label, "kb_id": q["kb_id"], "question": q["q"],
                  "ok": ok, "reason": reason})
        results.append(r)
        print(f"  [{label}] {q['kb_id']:8s} ok={ok!s:5s} ({reason}) "
              f"exec={r['exec_id']} lat={r['node_latency_ms']}ms")
    return results


def dim_a_cache(out):
    """A — неизменный префикс: латентность стабильного vs перемешиваемого порядка."""
    import random
    stable_items = list(KB_ITEMS)
    stable_prefix = kb_plain(stable_items)

    def stable_prompt(q):
        return (SYS_INSTRUCTION + stable_prefix +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    def shuffled_prompt(q):
        items = list(KB_ITEMS)
        random.Random(hash(q["q"])).shuffle(items)
        return (SYS_INSTRUCTION + kb_plain(items) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    qs10 = (QUESTIONS * 2)[:10]
    out["A_stable"] = run_group("A-stable", stable_prompt, qs10)
    out["A_shuffled"] = run_group("A-shuffled", shuffled_prompt, qs10)


def dim_b_structure(out):
    """B — форматирование: plain / markdown-заголовки / с краткими описаниями."""
    qs5 = QUESTIONS[:5]

    def plain_prompt(q):
        return (SYS_INSTRUCTION + kb_plain(KB_ITEMS) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    def headers_prompt(q):
        return (SYS_INSTRUCTION + kb_headers(KB_ITEMS) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    def desc_prompt(q):
        return (SYS_INSTRUCTION + kb_with_desc(KB_ITEMS) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    out["B_plain"] = run_group("B-plain", plain_prompt, qs5)
    out["B_headers"] = run_group("B-headers", headers_prompt, qs5)
    out["B_desc"] = run_group("B-desc", desc_prompt, qs5)


def dim_c_position(out):
    """C — позиция нужного пункта: начало / середина / конец списка из 10."""
    others = [it for it in KB_ITEMS if it[0] not in
              {"kb1", "kb2", "kb4", "kb5", "kb7"}]  # 5 нейтральных пунктов-заполнителей

    def make_prompt(target_item, position):
        items = list(others)
        if position == "start":
            items = [target_item] + items
        elif position == "end":
            items = items + [target_item]
        else:
            items = items[:2] + [target_item] + items[2:]
        return items

    qs5 = QUESTIONS[:5]
    for pos in ("start", "middle", "end"):
        def prompt_fn(q, pos=pos):
            target = next(it for it in KB_ITEMS if it[0] == q["kb_id"].split("/")[0])
            items = make_prompt(target, pos)
            return (SYS_INSTRUCTION + kb_plain(items) +
                    f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)
        out[f"C_{pos}"] = run_group(f"C-{pos}", prompt_fn, qs5)


def dim_d_rules(out):
    """D — формулировка правил: проза vs строгая условная форма. На вопросах сравнения
    чисел — тех же, что дали ошибки в Кейсе 1."""
    COND_RULES = {
        "kb2": "ЕСЛИ до начала занятия ≥24 часов → перенос РАЗРЕШЁН. ЕСЛИ <24 часов → "
               "перенос ЗАПРЕЩЁН.",
        "kb4": "ЕСЛИ сумма возврата ≤3000 рублей → решает сотрудник, срок 10 рабочих дней. "
               "ЕСЛИ сумма >3000 рублей → решает руководитель, дольше 10 рабочих дней.",
    }

    def prose_prompt(q):
        return (SYS_INSTRUCTION + kb_plain(KB_ITEMS) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    def cond_prompt(q):
        items = []
        for k, t, b in KB_ITEMS:
            items.append((k, t, COND_RULES.get(k, b)))
        return (SYS_INSTRUCTION + kb_plain(items) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    number_qs = [q for q in QUESTIONS if q["kb_id"] in ("kb2", "kb4", "kb2/kb6")] * 4
    number_qs = number_qs[:12]
    out["D_prose"] = run_group("D-prose", prose_prompt, number_qs)
    out["D_conditional"] = run_group("D-cond", cond_prompt, number_qs)


def dim_e_repeat(out):
    """E — вопрос клиента повторён до и после списка vs только после."""
    def after_only(q):
        return (SYS_INSTRUCTION + kb_plain(KB_ITEMS) +
                f"\n\nВопрос клиента: {q['q']}" + TAIL_INSTRUCTION)

    def before_and_after(q):
        return (SYS_INSTRUCTION + f"Вопрос клиента (держи в уме, читая базу ниже): {q['q']}"
                "\n\n" + kb_plain(KB_ITEMS) +
                f"\n\nВопрос клиента ещё раз: {q['q']}" + TAIL_INSTRUCTION)

    qs5 = QUESTIONS[:5]
    out["E_after"] = run_group("E-after", after_only, qs5)
    out["E_both"] = run_group("E-both", before_and_after, qs5)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dims", default="ABCDE")
    ap.add_argument("--output", default="raw/zamer_k2.json")
    args = ap.parse_args()

    out = {}
    if "A" in args.dims:
        dim_a_cache(out)
    if "B" in args.dims:
        dim_b_structure(out)
    if "C" in args.dims:
        dim_c_position(out)
    if "D" in args.dims:
        dim_d_rules(out)
    if "E" in args.dims:
        dim_e_repeat(out)

    Path(args.output).write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    total = sum(len(v) for v in out.values())
    print(f"\n{total} вызовов записано в {args.output}")
