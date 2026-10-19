#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Программная проверка НАЛОЖЕНИЙ текста по собранному PDF (§11.1 канона).

Заведена после тройной прожарки Лекции 7: наложение на `s16` пережило личный
визуальный просмотр PNG при 150 dpi и нашлось замером координат за секунды.
Вывод канона дословно — «не полагаться на то, что смотрят»: там, где правило
проверяется программой, оно проверяется программой, а просмотр остаётся
дополнительным слоем, не единственным.

ЧТО СЧИТАЕТСЯ НАЛОЖЕНИЕМ. Берутся прямоугольники СТРОК (`get_text("dict")`,
уровень `line`), а не блоков: блок — это рамка абзаца, и соседние абзацы
законно стоят вплотную, тогда как две строки, перекрывшиеся по обеим осям, —
это и есть то, что зал видит как кашу.

ПАРЫ ИЗ ОДНОГО БЛОКА ПРОВЕРЯЮТСЯ НАРАВНЕ СО ВСЕМИ, и это исправление, а не
изначальный замысел. Первая редакция пропускала их («строки одного абзаца
стоят вплотную по устройству») и на контрольном прогоне НЕ НАШЛА заведомо
подложенного наложения: PyMuPDF положил обе наложенные строки в один блок,
и проверка промолчала. Ноль на боевой деке при этом выглядел подтверждением
чистоты — ровно тот ложный ноль, о котором предупреждает §8.6 семинарского
README про `grep -P` по кириллице. Нормально сложенные строки абзаца не
перекрываются выше порога и без этого пропуска, так что ничего он не
экономил, кроме честности прогона.

КОНТРОЛЬНЫЙ ПРОГОН ОБЯЗАТЕЛЕН ПЕРЕД ТЕМ, КАК ДОКЛАДЫВАТЬ НОЛЬ. `--samoprovierka`
строит PDF с заведомым наложением и требует, чтобы проверка его нашла. Ноль,
полученный без этого прогона, не означает ничего.

ПОРОГ НЕ НОЛЬ, И ЭТО НЕ ПОСЛАБЛЕНИЕ. Рендер кладёт строки с субпиксельным
зазором, а глифы с выносными элементами законно заходят в чужой прямоугольник
на доли пункта. Поэтому пересечение считается значимым, если площадь общей
части больше `MIN_DOLYA` меньшего из двух прямоугольников. Порог назван числом
здесь, а не подобран молча: при нуле прогон даёт срабатывания на каждой второй
странице и перестаёт что-либо значить.

    python3 proverka_nalozheniy.py sec-2-3.pdf
"""
import sys
from pathlib import Path

import pymupdf

MIN_DOLYA = 0.12      # доля площади меньшего прямоугольника
MIN_H = 1.0           # строки тоньше пункта — артефакты разбора, не текст


def stroki(stranitsa):
    out = []
    for b in stranitsa.get_text("dict")["blocks"]:
        if b.get("type") != 0:
            continue
        for ln in b.get("lines", []):
            x0, y0, x1, y1 = ln["bbox"]
            if (y1 - y0) < MIN_H or (x1 - x0) < MIN_H:
                continue
            tekst = "".join(s.get("text", "") for s in ln.get("spans", []))
            if tekst.strip():
                out.append((b["number"], (x0, y0, x1, y1), tekst.strip()))
    return out


def peresechenie(a, b):
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    dx = min(ax1, bx1) - max(ax0, bx0)
    dy = min(ay1, by1) - max(ay0, by0)
    if dx <= 0 or dy <= 0:
        return 0.0
    obshchaya = dx * dy
    menshaya = min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0))
    return obshchaya / menshaya if menshaya else 0.0


def main(put):
    doc = pymupdf.open(put)
    vsego = 0
    for nomer, stranitsa in enumerate(doc, 1):
        ln = stroki(stranitsa)
        for i in range(len(ln)):
            for j in range(i + 1, len(ln)):
                _, ra, ta = ln[i]
                _, rb, tb = ln[j]
                dolya = peresechenie(ra, rb)
                if dolya > MIN_DOLYA:
                    vsego += 1
                    print(f"  стр. {nomer}: перекрытие {dolya:.0%} — "
                          f"{ta[:46]!r} и {tb[:46]!r}")
    print(f"\nстраниц {len(doc)} · наложений выше порога {MIN_DOLYA:.0%}: {vsego}")
    return 1 if vsego else 0


def samoprovierka():
    """Подложить наложение и потребовать, чтобы проверка его нашла."""
    import pymupdf as pm
    d = pm.open()
    p = d.new_page(width=720, height=405)
    p.insert_text((100, 200), "Строка, на которую сейчас наедут", fontsize=18)
    p.insert_text((104, 203), "Наехавшая на неё строка", fontsize=18)
    p.insert_text((100, 320), "Строка, которая ни на что не наложена",
                  fontsize=18)
    put = Path("/tmp/kontrol-nalozhenie.pdf")
    d.save(put)
    print("контрольный прогон (обязан найти ровно одно наложение):")
    kod = main(put)
    if kod != 1:
        print("САМОПРОВЕРКА ПРОВАЛЕНА: подложенное наложение не найдено — "
              "ноль этой проверки на настоящей деке ничего не значит")
        return 2
    print("самопроверка пройдена\n")
    return 0


if __name__ == "__main__":
    if "--samoprovierka" in sys.argv:
        kod = samoprovierka()
        sys.exit(kod if kod else main(
            [a for a in sys.argv[1:] if not a.startswith("--")][0]
            if [a for a in sys.argv[1:] if not a.startswith("--")]
            else "sec-2-3.pdf"))
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "sec-2-3.pdf"))
