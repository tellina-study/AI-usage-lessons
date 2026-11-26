#!/usr/bin/env python3
"""Разбор четвёртого метода («картинка и распознанный текст вместе») против прежних
трёх — два вопроса задания владельца 2026-11-25:

  (1) ИСПРАВЛЯЕТ ли подсказка ошибку? Поля, где гибрид (метод 2) ДОСЛОВНО скопировал
      ошибку распознавания — что на них дал метод 4.
  (2) УТАСКИВАЕТ ли подсказка? Поля, где метод 1 (одна картинка) ответил ВЕРНО, а
      метод 4 (картинка + подсказка) ошибся, И ошибка совпадает с распознанным
      текстом. Это и есть «новый класс ошибки», если он есть.
  (+) обратный счёт: поля, где метод 1 ошибся, а метод 4 ответил верно.

Операциональное определение «ответ взят из распознанного текста» — одно для обоих
вопросов, названо здесь, а не подобрано под результат: нормализованный ответ модели
непуст и является ПОДСТРОКОЙ нормализованного OCR-текста той же формы, при этом
нормализованный эталон подстрокой того же текста НЕ является. Второе условие
обязательно: без него всякий верный ответ, который OCR тоже прочёл верно, попал бы
в «скопировано из подсказки». Нормализация — та же `score.py::normalize` (снятие
всего, кроме букв и цифр), не своя.

Запуск: .venv/bin/python3 analiz_metod_4.py
"""
import json
from collections import defaultdict
from pathlib import Path

from score import normalize

HERE = Path(__file__).resolve().parent
LABELS = {"vision": "метод 1 (картинка)", "hybrid": "метод 2 (гибрид, текст)",
          "ocr_rules": "метод 3 (правила)", "vision_ocr": "метод 4 (картинка+текст)"}
CAT_RU = {"name": "имя", "date": "дата", "phone": "телефон/факс", "count": "число"}


def load():
    rows = json.load(open(HERE / "raw" / "scored_all.json"))
    ocr = json.load(open(HERE / "raw" / "ocr_results.json"))["per_form"]
    ocr_norm = {fid: normalize(v["text_joined"]) for fid, v in ocr.items()}
    by = defaultdict(dict)
    # Ключ ОБЯЗАН содержать номер вхождения: после правки эталона (issue #351)
    # на форме 11508234 два поля «Date:» несут один и тот же эталон «3/ 3/ 95»
    # (у второго он был «3433/ 3/ 95»), и ключ без номера схлопнул бы их в одну
    # запись, молча потеряв поле. Порядок строк одинаков у всех четырёх методов
    # (score.py обходит корпус одним и тем же циклом), поэтому n-е вхождение у
    # одного метода отвечает n-му у другого.
    seen = defaultdict(int)
    for r in rows:
        base = (r["form_id"], r["q_text"], r["gt"])
        seen[(r["method"], base)] += 1
        by[r["method"]][base + (seen[(r["method"], base)],)] = r
    return by, ocr_norm, rows


def from_hint(row, ocr_norm):
    """Ответ модели взят из распознанного текста (а эталона там нет) — см. докстринг."""
    p, g = normalize(row["pred"]), normalize(row["gt"])
    t = ocr_norm.get(row["form_id"], "")
    return bool(p) and p in t and g not in t


def pct(a, b):
    return f"{a}/{b} = {a/b:.1%}" if b else f"{a}/0 = —"


def main():
    by, ocr_norm, rows = load()
    keys = list(by["vision"].keys())

    print("=" * 78)
    print("СВОД: четыре метода на одном корпусе (363 целевых поля, 100 форм)")
    print("=" * 78)
    for m in ["vision", "hybrid", "ocr_rules", "vision_ocr"]:
        rs = list(by[m].values())
        e = sum(r["exact"] for r in rs)
        n_all = len(rs)
        line = [f"{LABELS[m]:28s} {e:3d}/{n_all} = {e/n_all:.1%}"]
        for c in ["name", "date", "phone", "count"]:
            cr = [r for r in rs if r["cat"] == c]
            ce = sum(r["exact"] for r in cr)
            line.append(f"{CAT_RU[c]} {ce}/{len(cr)}={ce/len(cr):.0%}")
        print("  " + "  ·  ".join(line))

    # --- Вопрос 1 -----------------------------------------------------------
    print()
    print("=" * 78)
    print("ВОПРОС 1. Исправляет ли подсказка скопированную ошибку распознавания?")
    print("=" * 78)
    copied = [k for k in keys
              if not by["hybrid"][k]["exact"] and from_hint(by["hybrid"][k], ocr_norm)]
    fixed = [k for k in copied if by["vision_ocr"][k]["exact"]]
    still = [k for k in copied if not by["vision_ocr"][k]["exact"]]
    still_same = [k for k in still if from_hint(by["vision_ocr"][k], ocr_norm)]
    print(f"полей, где метод 2 дословно скопировал ошибку распознавания: {len(copied)}")
    print(f"  из них метод 4 ИСПРАВИЛ: {pct(len(fixed), len(copied))}")
    print(f"  из них метод 4 НЕ исправил: {pct(len(still), len(copied))}")
    print(f"     ⤷ и повторил ту же ошибку распознавания: {pct(len(still_same), len(copied))}")
    v1_on_copied = sum(by["vision"][k]["exact"] for k in copied)
    print(f"  (для базы: метод 1 на этих же {len(copied)} полях верен "
          f"{pct(v1_on_copied, len(copied))})")
    print("\n  — все случаи, где метод 4 НЕ исправил скопированную ошибку:")
    for k in still:
        r4, r2, r1 = by["vision_ocr"][k], by["hybrid"][k], by["vision"][k]
        print(f"    {k[0]:20s} {CAT_RU[r4['cat']]:12s} «{k[1]}»")
        print(f"       эталон={r4['gt']!r}  м2={r2['pred']!r}  м4={r4['pred']!r}  "
              f"м1={r1['pred']!r} ({'верно' if r1['exact'] else 'неверно'})")

    # --- Вопрос 2 -----------------------------------------------------------
    print()
    print("=" * 78)
    print("ВОПРОС 2. Утаскивает ли подсказка модель от верного чтения картинки?")
    print("=" * 78)
    lost = [k for k in keys if by["vision"][k]["exact"] and not by["vision_ocr"][k]["exact"]]
    lost_hint = [k for k in lost if from_hint(by["vision_ocr"][k], ocr_norm)]
    lost_null = [k for k in lost if by["vision_ocr"][k]["pred"] is None]
    lost_other = [k for k in lost if k not in lost_hint and k not in lost_null]
    gained = [k for k in keys if not by["vision"][k]["exact"] and by["vision_ocr"][k]["exact"]]
    print(f"метод 1 верно -> метод 4 неверно (потеряно):  {len(lost)}")
    print(f"   ⤷ ошибка СОВПАДАЕТ с распознанным текстом (новый класс): {len(lost_hint)}")
    print(f"   ⤷ метод 4 вернул пусто/форма не разобралась:             {len(lost_null)}")
    print(f"   ⤷ прочее (своя ошибка модели, не из подсказки):          {len(lost_other)}")
    print(f"метод 1 неверно -> метод 4 верно (приобретено): {len(gained)}")
    gained_hint = [k for k in gained if from_hint(by["hybrid"][k], ocr_norm)
                   or normalize(by["hybrid"][k]["pred"]) == normalize(by["hybrid"][k]["gt"])]
    print(f"   ⤷ из них распознавание читало это поле верно (подсказка помогла по делу): "
          f"{len(gained_hint)}")
    print(f"ИТОГО сальдо метод 4 − метод 1: {len(gained) - len(lost):+d} полей")

    print("\n  — ВСЕ поля нового класса (подсказка утащила от верного чтения):")
    for k in lost_hint:
        r4, r2 = by["vision_ocr"][k], by["hybrid"][k]
        print(f"    {k[0]:20s} {CAT_RU[r4['cat']]:12s} «{k[1]}»")
        print(f"       эталон={r4['gt']!r}")
        print(f"       м1 (картинка)      = {by['vision'][k]['pred']!r}  ВЕРНО")
        print(f"       м4 (картинка+текст)= {r4['pred']!r}  неверно — это и есть OCR")
        print(f"       м2 (только текст)  = {r2['pred']!r}")

    print("\n  — поля, приобретённые методом 4 (метод 1 ошибался):")
    for k in gained:
        r4 = by["vision_ocr"][k]
        print(f"    {k[0]:20s} {CAT_RU[r4['cat']]:12s} «{k[1]}»  эталон={r4['gt']!r}  "
              f"м1={by['vision'][k]['pred']!r}  м4={r4['pred']!r}")

    # --- Разбивка потерь/приобретений по категориям -------------------------
    print()
    print("=" * 78)
    print("Где метод 4 выигрывает и где проигрывает методу 1 — по категориям")
    print("=" * 78)
    for c in ["name", "date", "phone", "count"]:
        L = [k for k in lost if by["vision_ocr"][k]["cat"] == c]
        Lh = [k for k in L if k in lost_hint]
        G = [k for k in gained if by["vision_ocr"][k]["cat"] == c]
        print(f"  {CAT_RU[c]:12s} потеряно {len(L):2d} (из них из-за подсказки {len(Lh):2d})"
              f" · приобретено {len(G):2d} · сальдо {len(G)-len(L):+d}")

    # --- Природа промахов метода 4 (та же развилка, что считали гибриду) ----
    print()
    print("=" * 78)
    print("Природа промахов метода 4 (та же развилка, что считали гибриду)")
    print("=" * 78)
    vo_raw = json.load(open(HERE / "raw" / "vision_ocr_results.json"))["per_form"]
    broken = {fid for fid, v in vo_raw.items() if v.get("parsed") is None}
    misses = [k for k in keys if not by["vision_ocr"][k]["exact"]]
    bm = [k for k in misses if k[0] in broken]
    cm = [k for k in misses if k[0] not in broken]
    nulls = [k for k in cm if by["vision_ocr"][k]["pred"] is None]
    print(f"всего промахов: {len(misses)}")
    print(f"  сломанный формат ответа (вся форма разом, форм: {len(broken)}): "
          f"{len(bm)} ({len(bm)/len(misses):.1%})  формы: {sorted(broken)}")
    print(f"  содержательная потеря: {len(cm)} ({len(cm)/len(misses):.1%})")
    print(f"    ⤷ пусто (честное «не нашла»): {len(nulls)}")
    print(f"    ⤷ неверное значение уверенно: {len(cm)-len(nulls)}")
    cm_hint = [k for k in cm if from_hint(by["vision_ocr"][k], ocr_norm)]
    print(f"  из всех содержательных промахов взяты из подсказки: "
          f"{pct(len(cm_hint), len(cm))}")

    # --- Счёт без формы, у которой сломался JSON (честное отделение) --------
    print()
    print("=" * 78)
    print("Контроль: тот же счёт БЕЗ формы 83594639 (её JSON у метода 4 сломался)")
    print("=" * 78)
    ks = [k for k in keys if k[0] != "83594639"]
    for m in ["vision", "hybrid", "vision_ocr"]:
        e = sum(by[m][k]["exact"] for k in ks)
        print(f"  {LABELS[m]:28s} {e}/{len(ks)} = {e/len(ks):.1%}")


if __name__ == "__main__":
    main()
