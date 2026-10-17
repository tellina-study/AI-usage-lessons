#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сторож кромки: не уехал ли текст кадра под нижний край страницы.

ЗАЧЕМ ОТДЕЛЬНО ОТ ПОЛА КЕГЛЯ. `zamer_pdf.py` отвечает на вопрос «не мелко
ли набрано» и даёт по этой деке «ноль знаков ниже 12 пт из 62 127». Число
верное, и вопрос оно закрывает — но не тот. Обложка, с которой начался
этот сторож, давала **ноль знаков ниже 12 пт И ОДНОВРЕМЕННО уезжала под
нижнюю кромку**: кегля там хватало, не хватало высоты. «Пол кегля чист»
не равно «раскладка цела», и до этого прогона второе в приёмке не мерил
никто.

ПОЧЕМУ ПО СОБРАННОМУ PDF, А НЕ ПО ОТЧЁТУ СБОРКИ. Отчёт говорит, что
раскладка ОЦЕНИЛА, а PDF показывает, что вышло на страницу; эти два
расходятся, и расходились в этом производстве не раз — отчёт однажды
назвал один кадр ниже пола там, где по PDF их было шесть. Здесь меряется
страница, которую видит зал.

ЧТО ИМЕННО МЕРИТСЯ. У каждого прогона текста PDF хранит базовую линию.
Низ прогона — не базовая линия, а она минус выносные элементы букв
(«у», «р», «д»), иначе кадр с базовой линией в двух пунктах от края
считался бы целым, когда хвосты букв уже срезаны. Берётся доля 0,22 от
кегля — мера выносного элемента для начертаний этой деки.

ПОРОГИ ЗАМЕРЕНЫ, А НЕ НАЗНАЧЕНЫ. По собранной деке (101 кадр) самый
низкий прогон лежит на 13,0 пункта над краем, медиана 26,6, ниже нуля —
ни одного. Сломанная обложка даёт **минус 168,9**. Две кучи разведены с
огромным запасом, поэтому:
    низ < 0            — ВЫХОД ЗА КРОМКУ, блокирующее;
    0 ≤ низ < 6        — у самой кромки, предупреждение: запас меньше,
                         чем у любого кадра этой деки.

ОТРИЦАТЕЛЬНЫЙ РЕЗУЛЬТАТ ЗДЕСЬ ВИДЕН. Прогон всегда печатает, сколько
страниц он открыл и сколько проверил, и говорит «выходов за кромку M»
числом, а не фразой «раскладка цела». Пустой вход — отказ с кодом 2, не
«чисто»: читать было нечего, и это другое.

    python3 storozh_kromki.py                  # по lec-07-karkas.pdf
    python3 storozh_kromki.py sec-0-1.pdf      # по названному PDF
    python3 storozh_kromki.py --samoproverka   # на заведомо сломанном входе

Код возврата: 0 — выходов нет; 1 — есть; 2 — читать было нечего.
"""
import argparse
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "tools" / "presentation-build"))

from deckkit import pdfmeasure as pm        # noqa: E402

PO_UMOLCHANIYU = HERE / "lec-07-karkas.pdf"
VYNOS = 0.22          # доля кегля на выносной элемент буквы
KROMKA = 0.0          # нижний край страницы в координатах PDF
ZAPAS = 6.0           # ближе этого к краю — предупреждение

# Сломанный вход самопроверки: та самая обложка, которая давала
# `[высота] 9,06" > 5,72"` и уезжала под кромку, наложившись на подпись к
# фото. Сторож, не доказанный на сломанном входе, ничего не стоит.
#
# HERO ЗДЕСЬ ОБЯЗАТЕЛЕН, и это выяснила сама самопроверка. Первая проба
# шла без него и НЕ ловилась: без hero колонка текста идёт во всю ширину
# кадра, и тот же текст укладывается свободно. Кадр ломала не длина
# текста сама по себе, а длина ПРИ колонке в 4,00 дюйма рядом с
# иллюстрацией. Фикстура без hero проверяла бы не тот кадр — ровно та
# подмена, из-за которой сессия ядра не смогла воспроизвести поломку.
SLOMANNAYA_OBLOZHKA = """---
id: s01
local_id: В-01
section: "0. Вход"
type: cover
title: "Проба сторожа кромки"
assertion: "—"
source: "—"
media: "rework/deck/assets/s01-hero-chtenie-mammogrammy.jpg"
media_hero: true
media_caption: "Фото: Bill Branson, Национальный институт рака США (NCI), общественное достояние"
media_needed: ""
media_note: "—"
timing_min: 0.4
in_bucket: false
method_steps: []
form: []
vfy: false
status: собран
---

## Видимый текст слайда

# Решение о человеке: кто смотрит, кто подписывает, кто платит

### AI в медицине и фармацевтике · Лекция 7

Цену ошибки в медицине удерживает процедура вокруг человека: двойное чтение, второе мнение, консилиум, информированное согласие.

Лекция идёт по пути одного случая: что модель делает с процедурой и с человеком в ней.

## Заметки лектора

Кадр существует только ради самопроверки сторожа кромки.
"""


def niz_progonov(stream):
    """Низ каждого прогона страницы: базовая линия минус выносной элемент."""
    return [(y - VYNOS * size, size, n)
            for size, n, x, y in pm.text_runs(stream)]


def proverit(pdf):
    """(находки, страниц открыто, страниц с текстом).

    Находка — страница, у которой самый низкий прогон ушёл за кромку либо
    подошёл к ней ближе запаса. Возвращается, а не печатается: своду
    приёмки нужен результат, а обёртка процессом его не даёт.
    """
    nakhodki, vsego, s_tekstom = [], 0, 0
    for n, stream, box in pm.pages(pdf):
        vsego += 1
        nizy = niz_progonov(stream)
        if not nizy:
            continue
        s_tekstom += 1
        niz, kegl, _ = min(nizy, key=lambda t: t[0])
        if niz < KROMKA:
            nakhodki.append((n, niz, kegl, "ВЫХОД ЗА КРОМКУ"))
        elif niz < ZAPAS:
            nakhodki.append((n, niz, kegl, "у самой кромки"))
    return nakhodki, vsego, s_tekstom


def proverit_pdf(pdf=None):
    """Вызываемый вход для свода приёмки: результат ВОЗВРАЩАЕТСЯ.

    Договор тот же, что у `storozh_dublej.proverit_papku`, и поле `pusto`
    здесь по той же причине: своду нужно отличить «раскладка цела» от
    «читать было нечего».
    """
    p = Path(pdf or PO_UMOLCHANIYU)
    if not p.exists():
        return {"prochitano": {"страниц": 0, "с текстом": 0},
                "pusto": True, "net_fayla": str(p), "nahodki": []}
    nakhodki, vsego, s_tekstom = proverit(p)
    return {
        "prochitano": {"страниц": vsego, "с текстом": s_tekstom,
                       "файл": p.name},
        "kromka": KROMKA, "zapas": ZAPAS,
        "pusto": vsego == 0 or s_tekstom == 0,
        "nahodki": [{"stranitsa": n, "niz_pt": round(niz, 1),
                     "kegl": kegl, "vid": vid}
                    for n, niz, kegl, vid in nakhodki],
    }


def pechat(pdf, nakhodki, vsego, s_tekstom):
    print(f"прочитано: {vsego} страниц файла {Path(pdf).name}, "
          f"с текстом {s_tekstom}, кромка y = {KROMKA:.0f}, "
          f"запас {ZAPAS:.0f} пт")
    if vsego == 0 or s_tekstom == 0:
        print("ОТКАЗ: читать было нечего. Это не «раскладка цела» — это "
              "пустой вход; проверьте путь к PDF.")
        return 2
    vyshli = [f for f in nakhodki if f[3] == "ВЫХОД ЗА КРОМКУ"]
    u_kromki = [f for f in nakhodki if f[3] == "у самой кромки"]
    print(f"выходов за кромку: {len(vyshli)} · у самой кромки: "
          f"{len(u_kromki)} · проверено страниц: {s_tekstom}")
    for n, niz, kegl, vid in nakhodki:
        znak = "" if niz < 0 else "+"
        print(f"   стр.{n:>3}  {vid:<16} низ прогона {znak}{niz:.1f} пт "
              f"(кегль {kegl:.1f})")
    if not nakhodki:
        print("   ни одна страница к краю ближе запаса не подошла")
    return 1 if vyshli else 0


def samoproverka():
    """Сторож обязан поймать тот вход, ради которого заведён.

    Кадр собирается из ВРЕМЕННОЙ папки, а не правкой `slides/s01-cover.md`:
    самопроверка, которая трогает рабочий файл, однажды не вернёт его на
    место. (В этом производстве проба обложки уже оставила в файле лишнюю
    строку — заметили по выводу, а не по диффу.)
    """
    import build_lec07 as B
    from deckkit import render as rnd, report

    tmp = Path(tempfile.mkdtemp(prefix="kromka-"))
    try:
        (tmp / "s01-proba.md").write_text(SLOMANNAYA_OBLOZHKA, encoding="utf-8")
        out = tmp / "proba.pptx"
        keep = report.snapshot()
        report.reset()
        B.build(only="s01", out=out, slides_dir=tmp)
        bl = len(report.blocking())
        report.restore(keep)
        if rnd.render(out, tmp / "snaps", timeout=300):
            print("ОТКАЗ самопроверки: кадр не отрендерился")
            return 2
        nakhodki, vsego, s_tekstom = proverit(out.with_suffix(".pdf"))
        print("самопроверка на заведомо сломанной обложке "
              f"(сборка даёт блокирующих: {bl})")
        kod = pechat(out.with_suffix(".pdf"), nakhodki, vsego, s_tekstom)
        poyman = any(f[3] == "ВЫХОД ЗА КРОМКУ" for f in nakhodki)
        print("самопроверка пройдена: выход за кромку пойман" if poyman
              else "ПРОВАЛ: сломанный вход не пойман — сторож бесполезен")
        return 0 if poyman else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf", nargs="?", default=str(PO_UMOLCHANIYU))
    ap.add_argument("--samoproverka", action="store_true")
    a = ap.parse_args()
    if a.samoproverka:
        return samoproverka()
    p = Path(a.pdf)
    if not p.exists():
        print(f"ОТКАЗ: файла {p} нет. Соберите деку, затем зовите сторож — "
              "по несобранному PDF вывод был бы ложным «чисто».")
        return 2
    return pechat(p, *proverit(p))


if __name__ == "__main__":
    sys.exit(main())
