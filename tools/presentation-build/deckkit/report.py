# -*- coding: utf-8 -*-
"""Предупреждения, счётчики и отчёт сборки — одно место на весь пакет.

Почему список, а не исключение. Сборка обязана дойти до конца и выдать ВСЕ
места, где раскладка не держится: сессия раздела правит кадры пачкой, и
отчёт из одной строки за прогон превращает правку в двадцать прогонов.

Почему БЛОКИРУЮЩИЕ отдельным перечнем. Предупреждения деки неравноценны:
«заметок нет» — работа, которую кто-то не доделал, а «не укладывается даже
при 8,5 пт» — кадр, который на экране наедет сам на себя. Второе обязано
выходить из `main` кодом возврата, первое — нет. Перечень тегов поэтому
закреплён, а не выводится из текста.

Оба сборщика держали этот список в себе — `build_lec07.WARNINGS` и
`build_lec06_p1.WARNINGS` — и каждый свой. Здесь он один; `snapshot` /
`restore` нужны пробной сборке (`fit_media` в lec-07), которая меряет кадр
и обязана НЕ попасть в отчёт.
"""
from collections import Counter

WARNINGS = []

# Теги, по которым виден физический предел кадра.
#   [высота]  текст не укладывается в свою рамку и наедет сам на себя
#   [ширина]  слово шире рамки — LibreOffice рвёт его посреди корня
#   [кегль]   блок набран на дне лестницы кеглей
#   [ссылка]  URL в видимом теле кадра (место ссылки — подвал)
#   [шрифт]   начертания нет на машине, мера шла по подменённому
#   [столбец] столбец таблицы уже своего самого длинного слова (lec-06)
BLOCKING = ("[высота]", "[ширина]", "[кегль]", "[ссылка]", "[шрифт]",
            "[столбец]")

# Тег, которого в этом перечне НЕТ нарочно.
#   [запас]   блок влезает по мере, но тоньше, чем мера способна
#             разрешить (`metrics.check_thin_margin`). Это НЕ «кадр
#             сломан» — это «сборка здесь не знает» и просьба посмотреть
#             кадр глазами. Блокировать неразрешимость нельзя: правка
#             может и не быть нужна, а предупреждение, под которое нечего
#             сделать, перестают читать на второй день. Поэтому — прочее.

LINKS = Counter()        # сколько настоящих гиперссылок поставлено
PRIM = Counter()         # сколько примитивов нарисовано
GOLD_SEEN = set()        # кадры, на которых золотой акцент виден
PLACEHOLDERS = Counter()
HERO_AREA = {}           # sid → доля площади слайда под обязательным hero
MISSING_MEDIA = []       # заявленные кадры, файла которых нет на диске


def warn(text):
    WARNINGS.append(text)
    return text


def blocking():
    return [w for w in WARNINGS if w.startswith(BLOCKING)]


def other():
    return [w for w in WARNINGS if not w.startswith(BLOCKING)]


def reset():
    """Полный сброс состояния отчёта. Нужен самопроверке: каждая проба —
    отдельный прогон, и предупреждения прошлой пробы в него попадать не
    вправе."""
    WARNINGS[:] = []
    LINKS.clear()
    PRIM.clear()
    GOLD_SEEN.clear()
    PLACEHOLDERS.clear()
    HERO_AREA.clear()
    MISSING_MEDIA[:] = []


def snapshot():
    """Снять состояние, чтобы вернуть его после ПРОБНОЙ сборки.

    Проба (`fit_media`: самая широкая колонка кадра, при которой кадр ещё
    собирается чисто) гоняет настоящую раскладку в отдельную презентацию.
    Её предупреждения — не предупреждения деки, и счётчики примитивов тоже
    её: без возврата состояния отчёт считал бы примитивы вчетверо."""
    return (list(WARNINGS), Counter(LINKS), Counter(PRIM), set(GOLD_SEEN),
            Counter(PLACEHOLDERS), dict(HERO_AREA), list(MISSING_MEDIA))


def restore(state):
    w, li, pr, gs, ph, ha, mm = state
    WARNINGS[:] = w
    LINKS.clear(); LINKS.update(li)
    PRIM.clear(); PRIM.update(pr)
    GOLD_SEEN.clear(); GOLD_SEEN.update(gs)
    PLACEHOLDERS.clear(); PLACEHOLDERS.update(ph)
    HERO_AREA.clear(); HERO_AREA.update(ha)
    MISSING_MEDIA[:] = mm


def report(n, out_name="", hero_threshold=0.40):
    """Отчёт сборки. Возвращает число БЛОКИРУЮЩИХ предупреждений — его и
    отдаёт `main` кодом возврата.

    Доля площади обязательных hero печатается КАЖДУЮ сборку, а не только
    когда порог провален: молчание о 40,5% неотличимо от молчания о том,
    что hero вообще нет — ровно этим `s01` lec-07 и прожил до issue #229."""
    print(f"\nсобрано кадров: {n}" + (f"  →  {out_name}" if out_name else ""))
    if PRIM:
        print("примитивы: "
              + " · ".join(f"{k} {v}" for k, v in sorted(PRIM.items())))
    print("ссылки: " + (" · ".join(f"{k} {v}" for k, v in sorted(LINKS.items()))
                        or "ни одной"))
    if HERO_AREA:
        print(f"обязательный hero (§5.9, порог {100 * hero_threshold:.0f}%): "
              + " · ".join(f"{k} {100 * v:.1f}%"
                           for k, v in sorted(HERO_AREA.items())))
    if PLACEHOLDERS:
        tot = sum(PLACEHOLDERS.values())
        with_ph = sum(1 for v in PLACEHOLDERS.values() if v)
        print(f"заглушки чисел: {tot} на {with_ph} кадрах из {n}")
    if MISSING_MEDIA:
        print(f"\nкадры, которых нет на диске ({len(MISSING_MEDIA)}):")
        for m in MISSING_MEDIA:
            print("  " + m)
    blk, oth = blocking(), other()
    if blk:
        print(f"\nБЛОКИРУЮЩИЕ предупреждения ({len(blk)}):")
        for w in blk:
            print("  " + w)
    if oth:
        print(f"\nпрочие предупреждения ({len(oth)}):")
        for w in oth:
            print("  " + w)
    if not WARNINGS:
        print("\nпредупреждений нет")
    return len(blk)
