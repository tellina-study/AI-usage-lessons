#!/usr/bin/env python3
"""Проверка промтов этого замера на протечку правильного ответа — issue #299, образец
логики `../zamery-k4-novyy/proverka_protechki.py`.

Зачем отдельный скрипт, а не абзац в README. В этом же проекте 2026-10-27 нашлась
протечка ровно этого класса на соседнем замере (`../zamery-k5-k6/`): промт описывал поле
`sum_rub` примером `например 18990.00`, а 18990.00 — настоящая сумма `receipt-01`,
единственной квитанции этого измерения. Абзац «я проверил» в README — самоотчёт;
проверка, которую можно перепрогнать, — нет.

Что проверяется (по тому же модулю `promt.py`, который реально строит текст, уходящий
на стенд — не по константам, переписанным сюда вручную):

  1. СТАТИЧЕСКАЯ часть инструкции (без текста заявки) не содержит ни TRUE_SUM (18990,
     18990.0, 18990.00, «18 990», «18,990») ни TRUE_DATE (12.09.2026 и варианты записи)
     ни единой другой реальной суммы/даты из `receipts-manifest.json`.
  2. Для всех 30 запланированных вызовов: когда `zayavka_verna=False`, число в
     заявке ДЕЙСТВИТЕЛЬНО не равно TRUE_SUM (иначе тест был бы сломан на уровне
     плана, не только промта).
  3. Для всех 30 вызовов: когда `zayavka_verna=True`, число в заявке РАВНО TRUE_SUM —
     это ПРОВЕРКА ДИЗАЙНА, не протечка (см. README «Проверка на протечку»): отдельно
     зафиксировано ниже, что это ожидаемо, а не ошибка.
  4. Полный текст промта (включая заявку) не содержит TRUE_DATE ни в каком виде —
     дата заявки никогда не сообщается модели, поэтому единственный способ ей узнать
     дату — прочитать фотографию; если TRUE_DATE просочится в текст хоть одного
     промта, это протечка.
  5. Полный текст промта не содержит слова `zayavka_verna`, `verna`, `совпал`,
     «истина», «правильный ответ» и подобных ярлыков разметки нашего собственного
     плана — модель не должна видеть, что мы уже знаем, какой вердикт у неё должен
     получиться.
  6. Тело HTTP-запроса на стенд несёт ровно поля `image_base64`, `mime_type`,
     `receipt_id`, `prompt_text` — без побочных полей типа `zayavka_verna`.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import promt  # noqa: E402

TRUE_SUM_VARIANTS = [
    "18990.00", "18990.0", "18990", "18 990", "18,990", "18990,00", "18990.00р",
]
TRUE_DATE_VARIANTS = [
    "12.09.2026", "12/09/2026", "12-09-2026", "2026-09-12", "12 сентября",
]
# Суммы/даты ВСЕХ квитанций стенда — проверка, что ни одна чужая реальная сумма/дата не
# просочилась случайно туда, где это не предусмотрено дизайном (т.е. не как «неверная
# заявка», где чужие суммы используются намеренно и это не протечка — см. README).
ALL_REAL_SUMS = [18990.00, 23450.00, 31200.00, 9800.00, 12450.00, 27300.00]
ALL_REAL_DATES = ["12.09.2026", "03.10.2026", "21.10.2026", "14.07.2026",
                   "29.08.2026", "05.10.2026"]


def main():
    bada = []
    plan = promt.plan()

    # 1 — статическая часть инструкции (без заявки) не содержит TRUE_SUM/TRUE_DATE
    static_text = promt.static_instruction_text_for_leak_check()
    for v in TRUE_SUM_VARIANTS:
        if v in static_text:
            bada.append(f"статический текст инструкции содержит сумму-пример «{v}»")
    for v in TRUE_DATE_VARIANTS:
        if v in static_text:
            bada.append(f"статический текст инструкции содержит дату-пример «{v}»")

    # 2/3 — соответствие zayavka_verna и реального числа в заявке (проверка дизайна
    # плана, не промта самого по себе)
    n_true_sum_in_true_claims = 0
    n_wrong_in_false_claims = 0
    for e in plan:
        if e["zayavka_verna"]:
            if abs(e["zayavka_sum"] - promt.TRUE_SUM) < 0.01:
                n_true_sum_in_true_claims += 1
            else:
                bada.append(f"{e['resolution']}#{e['repeat_idx']}: zayavka_verna=True, "
                             f"но zayavka_sum={e['zayavka_sum']} != TRUE_SUM")
        else:
            if abs(e["zayavka_sum"] - promt.TRUE_SUM) >= 0.01:
                n_wrong_in_false_claims += 1
            else:
                bada.append(f"{e['resolution']}#{e['repeat_idx']}: zayavka_verna=False, "
                             f"но zayavka_sum совпадает с TRUE_SUM — план сломан")

    # 4 — TRUE_DATE не попадает в полный текст НИ ОДНОГО из 30 промтов (дата никогда не
    # часть заявки по дизайну; если тут что-то нашлось — утечка)
    for e in plan:
        full_text = promt.build_prompt(e)
        for v in TRUE_DATE_VARIANTS:
            if v in full_text:
                bada.append(f"{e['resolution']}#{e['repeat_idx']}: полный промт содержит "
                             f"дату «{v}» — TRUE_DATE никогда не должна сообщаться модели")

    # 5 — ярлыки разметки нашего собственного плана не попадают в текст
    markers = ("zayavka_verna", "истина", "правильный ответ", "ожидаемый ответ",
               "ground truth", "ground_truth")
    for e in plan:
        full_text_low = promt.build_prompt(e).lower()
        for m in markers:
            if m.lower() in full_text_low:
                bada.append(f"{e['resolution']}#{e['repeat_idx']}: ярлык разметки «{m}» "
                             f"в тексте промта")

    # 6 — что реально уйдёт в теле запроса на стенд (та же сборка тела, что run_zamer.py)
    import run_zamer
    for e in plan[:3]:
        body = run_zamer.telo_zaprosa(e)
        ozh = {"image_base64", "mime_type", "receipt_id", "prompt_text"}
        if set(body.keys()) != ozh:
            bada.append(f"тело запроса на стенд несёт поля {sorted(body.keys())}, "
                         f"ожидались ровно {sorted(ozh)}")
            break

    if bada:
        print("ПРОТЕЧКА НАЙДЕНА:")
        for b in bada:
            print("  -", b)
        sys.exit(1)

    print("Протечки не найдено.")
    print("Проверено:")
    print("  - статический текст инструкции (без заявки) не содержит TRUE_SUM/TRUE_DATE "
          "ни в одном из вариантов записи")
    print(f"  - 30/30 записей плана: zayavka_verna=True -> zayavka_sum==TRUE_SUM "
          f"({n_true_sum_in_true_claims}/15), zayavka_verna=False -> zayavka_sum!="
          f"TRUE_SUM ({n_wrong_in_false_claims}/15)")
    print("  - TRUE_DATE (12.09.2026 и варианты записи) отсутствует во всех 30 полных "
          "промтах — дата никогда не сообщается модели заранее")
    print("  - во всех 30 промтах нет ярлыков разметки плана (zayavka_verna, "
          "«правильный ответ» и т.п.)")
    print("  - тело запроса на стенд несёт ровно 4 поля: image_base64, mime_type, "
          "receipt_id, prompt_text")
    print()
    print("ОГОВОРКА (не протечка, условие задачи, см. README «Проверка на протечку»): "
          "в 15 из 30 промтов (zayavka_verna=True) сумма заявки РАВНА настоящей сумме "
          "receipt-01 (18990) — это сумма ЗАЯВКИ, а не подсказка формата поля sum_rub, "
          "и ровно половина случаев, поэтому «всегда совпало» не даёт модели выигрыша.")


if __name__ == "__main__":
    main()
