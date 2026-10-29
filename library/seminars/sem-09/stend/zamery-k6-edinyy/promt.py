#!/usr/bin/env python3
"""Единый источник промта и плана вызовов для Замера «единый вызов» (Кейс 6, С9, issue
#299) — ОДИН модуль, который читают и `run_zamer.py` (чтобы отправить), и
`proverka_protechki.py` (чтобы проверить на протечку ДО отправки). Если бы текст промта
жил в двух местах, проверка проверяла бы не то, что реально уходит на стенд — ровно тот
класс ошибки, которого избегает `../zamery-k4-novyy/proverka_protechki.py` (читает
собранные файлы сценария, не константы в памяти).

Истинные значения `receipt-01` (НЕ подставлять никуда в статический текст промта —
только в поле заявки, где это — условие задачи, не протечка, см. README):
"""
TRUE_SUM = 18990.00
TRUE_DATE = "12.09.2026"

# Суммы ДРУГИХ квитанций стенда (receipts-manifest.json) — используются как «неверные»
# суммы заявки. Это настоящие суммы, но не суммы receipt-01, поэтому их появление в
# промте не протекает ответ ЭТОГО измерения (сумма receipt-01 остаётся неизвестной
# модели до того, как она сама прочитает фотографию).
OTHER_RECEIPT_SUMS = [23450.00, 31200.00, 9800.00, 12450.00, 27300.00]

RESOLUTIONS = ["full", "half", "quarter", "eighth", "sixteenth", "thirtysecond"]

# Балансировка true/false внутри каждого разрешения — паттерн A начинается с True,
# паттерн B начинается с False; три разрешения на каждый паттерн => 15 True / 15 False
# суммарно по всем 30 вызовам (не группой «все true потом все false» — порядок
# перемешан внутри каждого разрешения, чтобы не создавать артефакт порядка).
_PATTERN_A = [True, False, True, False, True]    # 3 True, 2 False
_PATTERN_B = [False, True, False, True, False]   # 2 True, 3 False
_PATTERN_BY_RES = {
    "full": _PATTERN_A, "quarter": _PATTERN_A, "sixteenth": _PATTERN_A,
    "half": _PATTERN_B, "eighth": _PATTERN_B, "thirtysecond": _PATTERN_B,
}

_CLAIM_TEMPLATES = [
    "Прошу подтвердить оплату курса. Я оплатил(а) {sum} рублей, прошу зачесть платёж "
    "по этой квитанции.",
    "Добрый день! Высылаю квитанцию об оплате. Сумма составила {sum} рублей, прошу "
    "подтвердить зачисление.",
    "Квитанция прикреплена. По моим данным оплата была на сумму {sum} рублей, прошу "
    "сверить и зачислить платёж.",
]


def plan():
    """30 записей плана — 6 разрешений × 5 повторов, детерминированно (без random,
    чтобы план был воспроизводим и проверяем `proverka_protechki.py` без побочных
    эффектов). Индекс `i` (0..4) внутри разрешения задаёт: (а) true/false из паттерна
    разрешения, (б) если false — какую из 5 «чужих» сумм подставить (циклически), (в)
    какой из 3 шаблонов заявки использовать (циклически, не связано с true/false)."""
    out = []
    false_cursor = 0
    for res in RESOLUTIONS:
        pattern = _PATTERN_BY_RES[res]
        for i in range(5):
            verna = pattern[i]
            if verna:
                zayavka_sum = TRUE_SUM
            else:
                zayavka_sum = OTHER_RECEIPT_SUMS[false_cursor % len(OTHER_RECEIPT_SUMS)]
                false_cursor += 1
            template = _CLAIM_TEMPLATES[(len(out)) % len(_CLAIM_TEMPLATES)]
            out.append({
                "resolution": res, "repeat_idx": i + 1,
                "receipt_id": f"receipt-01-{res}",
                "zayavka_verna": verna, "zayavka_sum": zayavka_sum,
                "claim_template_idx": (len(out)) % len(_CLAIM_TEMPLATES),
            })
    return out


def format_sum(x):
    """Печатает целые суммы без `.0` (18990, не 18990.0) — так, как их скорее всего
    написал бы человек в заявке; на протечку/сравнение не влияет (сравнение числовое)."""
    if float(x) == int(x):
        return str(int(x))
    return str(x)


def build_claim_text(entry):
    template = _CLAIM_TEMPLATES[entry["claim_template_idx"]]
    return template.format(sum=format_sum(entry["zayavka_sum"]))


# ВНИМАНИЕ (читает `proverka_protechki.py`): всё, что ниже этой строки и выше функции
# `build_prompt`, — ЕДИНСТВЕННЫЙ статический текст, уходящий модели как инструкция по
# формату. Он НЕ должен содержать ни TRUE_SUM, ни TRUE_DATE, ни их фрагментов — ни как
# «пример», ни как-либо иначе. Протечка числа-примера именно в этом месте уже случалась
# в этом же проекте 2026-10-27 (см. README «Проверка на протечку»).
_INSTRUCTION_TEMPLATE = (
    "На фотографии — квитанция об оплате курса учебного центра, снятая телефоном "
    "(возможны перекос, шум, нерезкость). Рядом — текст заявки клиента на зачисление "
    "платежа.\n\n"
    "Текст заявки клиента: «{claim_text}»\n\n"
    "Сначала прочитай с фотографии СУММУ платежа и ДАТУ. Затем сравни прочитанную с "
    "фотографии сумму с суммой, которую клиент указал в тексте заявки, и реши, "
    "совпадают ли они.\n\n"
    "Ответь СТРОГО в формате JSON без markdown-разметки и пояснений вокруг:\n"
    '{{"sum_rub": <число без пробелов и валюты — то, что написано на фотографии>, '
    '"date": "<дата в формате ДД.ММ.ГГГГ как написана на квитанции>", '
    '"zayavka_sum_rub": <число без пробелов и валюты — то, что указано в тексте '
    'заявки>, '
    '"verdict": "<ровно одно слово: sovpalo или ne_sovpalo — совпадает ли прочитанная '
    'с фотографии сумма с суммой из заявки>", '
    '"raw_text_seen": "<что именно ты прочитала в строке суммы на фотографии, '
    'дословно>"}}.\n'
    "Если строку суммы или даты невозможно разобрать уверенно — всё равно верни "
    "лучшую догадку в sum_rub/date, а в raw_text_seen честно напиши, что не уверена."
)


def build_prompt(entry):
    """Полный текст, уходящий модели. ЕДИНСТВЕННОЕ место, где в текст попадает реальное
    число — поле `{claim_text}`, и то только сумма ЗАЯВКИ (`entry['zayavka_sum']`), а не
    сумма квитанции напрямую (сумма квитаники, когда `zayavka_verna=True`, совпадает с
    суммой заявки по определению — это условие задачи, не протечка, см. README)."""
    claim_text = build_claim_text(entry)
    return _INSTRUCTION_TEMPLATE.format(claim_text=claim_text)


def static_instruction_text_for_leak_check():
    """То же, что `_INSTRUCTION_TEMPLATE`, но с заведомо безопасной (пустой по числам)
    подстановкой claim_text — для проверки СТАТИЧЕСКОЙ части текста инструкции отдельно
    от динамической суммы заявки (которая по дизайну задачи несёт реальное число в
    половине случаев)."""
    return _INSTRUCTION_TEMPLATE.format(claim_text="<здесь будет текст заявки клиента>")


if __name__ == "__main__":
    import json
    p = plan()
    n_true = sum(1 for e in p if e["zayavka_verna"])
    n_false = len(p) - n_true
    print(f"Всего записей плана: {len(p)}  true={n_true}  false={n_false}")
    for e in p:
        print(f"  {e['resolution']:12s} #{e['repeat_idx']} verna={e['zayavka_verna']!s:5s} "
              f"zayavka_sum={e['zayavka_sum']}")
    print("\n--- пример полного промта (resolution=full, repeat=1) ---")
    print(build_prompt(p[0]))
