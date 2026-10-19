#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""НАЛОЖЕНИЕ ТЕКСТА — замер по координатам собранного PDF, а не глазами.

ЗАЧЕМ ЭТОТ СТОРОЖ ЗАВЕДЁН. Четвёртый круг правок раздела 1 Лекции 7 прошёл
личный визуальный просмотр оркестратора (PNG, 150 dpi, все страницы) и всё
равно вернулся с REJECT независимой прожарки: на `s16` слово «фунтов» 23 пт
лежало поверх подписи «список около 49 тысяч человек» 12 пт — обе начинались
с одного x, их прямоугольники пересекались по обеим осям. Глазами при 150 dpi
этого не видно; по координатам это секунда счёта.
Правило — `trebovaniya-k-soderzhaniyu-forma.md` §11.1: перед любым докладом о
готовности кадра или раздела прогон этого замера обязателен, и его результат
идёт в доклад, в том числе когда он отрицательный.

ЧЕМ МЕРИТ. `PyMuPDF` (`page.get_text("dict")`) даёт прямоугольник каждого
прогона текста — того самого, который LibreOffice на самом деле положил на
страницу. Между нашим сборщиком и этими числами лежит весь рендер, поэтому
расхождение меры с тем, что увидит зал, здесь видно, а не предполагается.
`pdfplumber` из докладной записки канона — такой же годный вход; взят
PyMuPDF потому, что он уже стоит в окружении сборки (`render.py`,
`render_sec.py`), а `pdfplumber` в него не входит.

ЧТО СЧИТАЕТСЯ НАЛОЖЕНИЕМ. Пересечение прямоугольников двух прогонов по обеим
осям, у которого площадь перекрытия больше `--min-area` (по умолчанию 2 кв. пт
— ниже этого лежит обычное соприкосновение рамок соседних строк) И больше
`--min-frac` доли площади меньшего из двух (по умолчанию 0,12). Две доли, а не
одна: абсолютный порог отсеивает касание крупных плашек, долевой — случай,
когда мелкая подпись целиком утонула под крупным числом, а в абсолютных
единицах это всего несколько пунктов.

ЧЕГО ЗДЕСЬ НЕТ. Разбора того, КАКОЕ наложение терпимо: ни одного терпимого
не бывает, порог отсечки — про шум измерения, а не про допуск. И проверки
«текст наехал на картинку»: рамки изображений этот модуль не читает, за ними
`deckkit/probes_layout.py` и предупреждение сборки `[высота]`.

    python3 nalozhenie_bbox.py sec-1.pdf
    python3 nalozhenie_bbox.py sec-1.pdf --imena s11,s11a,s12      # подписать страницы
    python3 nalozhenie_bbox.py sec-1.pdf --selftest                # проверить сам замер
"""
import argparse
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # окружение сборки зовёт его старым именем
    import fitz as pymupdf


def _progony(page):
    """Прогоны текста страницы: (прямоугольник, кегль, текст)."""
    out = []
    for block in page.get_text("dict").get("blocks", []):
        if block.get("type") != 0:  # 0 — текст, 1 — изображение
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                txt = span.get("text", "")
                if not txt.strip():
                    continue
                out.append((tuple(span["bbox"]), round(span.get("size", 0), 1), txt))
    return out


def _perekrytie(a, b):
    """Площадь пересечения двух прямоугольников (x0, y0, x1, y1)."""
    dx = min(a[2], b[2]) - max(a[0], b[0])
    dy = min(a[3], b[3]) - max(a[1], b[1])
    return dx * dy if dx > 0 and dy > 0 else 0.0


def _ploshchad(r):
    return max(0.0, r[2] - r[0]) * max(0.0, r[3] - r[1])


def nalozheniya(page, min_area=2.0, min_frac=0.12):
    """Пары прогонов этой страницы, чьи прямоугольники перекрылись."""
    progony = _progony(page)
    out = []
    for i in range(len(progony)):
        ra, ka, ta = progony[i]
        for j in range(i + 1, len(progony)):
            rb, kb, tb = progony[j]
            s = _perekrytie(ra, rb)
            if s <= min_area:
                continue
            menshaya = min(_ploshchad(ra), _ploshchad(rb))
            if menshaya <= 0 or s / menshaya < min_frac:
                continue
            out.append({
                "ploshchad": s,
                "dolya": s / menshaya,
                "a": (ta, ka, ra),
                "b": (tb, kb, rb),
            })
    out.sort(key=lambda d: -d["ploshchad"])
    return out


def _obrez(s, n=46):
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "…"


def proverit(pdf, imena=None, min_area=2.0, min_frac=0.12, tiho=False):
    """Прогон по всему файлу. Возвращает число найденных наложений."""
    doc = pymupdf.open(pdf)
    vsego = 0
    for nomer, page in enumerate(doc):
        podpis = imena[nomer] if imena and nomer < len(imena) else f"стр.{nomer + 1}"
        naydeno = nalozheniya(page, min_area, min_frac)
        vsego += len(naydeno)
        if naydeno and not tiho:
            print(f"\n{podpis} — наложений {len(naydeno)}")
            for n in naydeno:
                ta, ka, ra = n["a"]
                tb, kb, rb = n["b"]
                print(f"  {n['ploshchad']:7.1f} кв.пт ({n['dolya'] * 100:4.0f}% меньшей)")
                print(f"      «{_obrez(ta)}» {ka} пт  x {ra[0]:.1f}–{ra[2]:.1f} "
                      f"y {ra[1]:.1f}–{ra[3]:.1f}")
                print(f"      «{_obrez(tb)}» {kb} пт  x {rb[0]:.1f}–{rb[2]:.1f} "
                      f"y {rb[1]:.1f}–{rb[3]:.1f}")
    if not tiho:
        print(f"\nстраниц {doc.page_count} · наложений {vsego} · "
              f"порог {min_area:g} кв.пт и {min_frac * 100:g}% меньшей рамки")
        if vsego == 0:
            print("ЧИСТО. Ноль получен замером координат, не просмотром снимков.")
    doc.close()
    return vsego


def selftest():
    """Замер обязан найти наложение, которое мы сами же и построили.

    Ноль от сторожа стоит ровно столько, сколько стоит доказательство, что
    он вообще умеет говорить не ноль (`storozha-i-priyomka.md` §11,
    «`--selftest` перед тем, как верить нулю»).
    """
    doc = pymupdf.open()
    page = doc.new_page(width=400, height=200)
    # Пара, которая ДОЛЖНА найтись: крупное число поверх мелкой подписи,
    # ровно та форма дефекта, что нашлась на s16.
    page.insert_text((50, 100), "10,5 млн фунтов", fontsize=23)
    page.insert_text((50, 95), "список около 49 тысяч человек", fontsize=12)
    # Пара, которая НЕ должна найтись: та же мелкая подпись строкой ниже.
    page.insert_text((50, 160), "список около 49 тысяч человек", fontsize=12)
    naydeno = nalozheniya(page)
    doc.close()

    teksty = {_obrez(n["a"][0]) + " | " + _obrez(n["b"][0]) for n in naydeno}
    ok = len(naydeno) == 1
    print(f"selftest: построено одно наложение и одна чистая строка; "
          f"замер нашёл {len(naydeno)}")
    for t in sorted(teksty):
        print(f"  найдено: {t}")
    print("selftest ПРОШЁЛ — нулю этого замера можно верить" if ok
          else "selftest ПРОВАЛЕН — нулю этого замера верить НЕЛЬЗЯ")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pdf", nargs="?", help="собранный PDF")
    ap.add_argument("--imena", default="", help="подписи страниц через запятую")
    ap.add_argument("--min-area", type=float, default=2.0)
    ap.add_argument("--min-frac", type=float, default=0.12)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not a.pdf:
        ap.error("нужен путь к PDF либо --selftest")
    imena = [s.strip() for s in a.imena.split(",")] if a.imena else None
    return 1 if proverit(Path(a.pdf), imena, a.min_area, a.min_frac) else 0


if __name__ == "__main__":
    sys.exit(main())
