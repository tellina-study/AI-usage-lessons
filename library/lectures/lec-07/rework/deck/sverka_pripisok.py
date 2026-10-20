#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""СЧЁТ СКВОЗНОЙ ЛИНИИ СОБИРАЕТСЯ, А НЕ ВПИСЫВАЕТСЯ (канон §5 и §6).

ЗАЧЕМ. `stroenie-i-povestvovanie.md` §6 требует, чтобы сквозная линия получила
на закрытии число, а §5 — чтобы число «пересчитывалось при каждой сборке по
файлу, а не переписывалось из прошлой редакции». Цена пропуска измерена самой
главой: её счёт красной линии «читался „десять", потом „двенадцать", потом
снова „десять"», и вписанное заранее число соврало бы трижды.

ЧТО ПРОВЕРЯЕТСЯ. Каждая строка `REESTR-PRIPISOK-DEKI.md` называет адрес кадра и
опорную фразу. Прогон открывает кадр, берёт ТОЛЬКО видимый слой (между
«## Видимый текст слайда» и «## Заметки лектора») и требует, чтобы фраза там
стояла. Фраза, уехавшая в заметки, засчитана НЕ БУДЕТ — это то же правило, по
которому нюанс в заметках не закрывает кадр (`obzor-stran-i-glubina-razbora.md`
§2.3), и ровно оно даёт счёту смысл: он мерит, сколько линии доехало до экрана.

ЗНАМЕНАТЕЛЬ СЧИТАЕТСЯ НЕЗАВИСИМО — по дивайдерам, а не по этому реестру.
Разборы берутся из видимого тела дивайдеров («Пример N: …»), как их берёт
`sverka_reestra.py`. Если числитель посчитать по реестру, а знаменатель по
реестру же, прогон докажет только непротиворечивость реестра с самим собой
(`notes/decisions.md`, правило 7 от 2026-10-15). Поэтому источники у двух чисел
разные.

ПОЧЕМУ `grep` ЗДЕСЬ НЕ ГОДИТСЯ: `grep -P` по кириллице даёт ложный ноль
(`seminar-production/README.md` §8.6). Счёт идёт Python `re` по тексту файла.

    python3 sverka_pripisok.py              # счёт и расхождения
    python3 sverka_pripisok.py --samoproverka   # контрольный прогон
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDES = HERE / "slides"
REESTR = HERE.parent / "REESTR-PRIPISOK-DEKI.md"

# Опорная фраза каждой приписки: адрес кадра -> что обязано стоять в ВИДИМОМ слое.
# Берётся из последней графы реестра; держится здесь, потому что фраза — это то,
# что прогон умеет проверить, а графа «чему принадлежит» — суждение, которое
# проверяет человек чтением.
OPORY = [
    ("1",  "s15a",  "56,7",                              3),
    ("2",  "s16a",  "не было вовсе",                     1),
    ("3",  "s27b",  "Выигрыш не в том",                   2),
    ("4",  "s28",   "Провалилось развёртывание",          2),
    ("5",  "s30",   "в этом дело",                        2),
    ("6",  "s31",   "предсказывать будущие расходы",      2),
    ("7",  "s41",   "обратный знак",                      2),
    ("8",  "s44",   "Эффекта нет",                        3),
    ("9",  "s49e",  "глубокой сети нет",                  2),
    ("9а", "s49f",  "считано от разного",                 3),
    ("10", "s61",   "принадлежит реализации",             2),
    ("11", "s63ab", "ТАК СЧИТАЮТ",                        3),
    ("12", "s73g",  "заявленным числам",                  3),
    ("13", "s73ga", "бывает и без модели",                1),
]
# Приписка на УПОМИНАНИИ: считается отдельно, в знаменатель разборов не входит.
NA_UPOMINANII = [("сигнал прибора", "s33", "модели нет", 1)]
# Разбор 9 несёт две приписки (строки 9 и 9а) — один разбор, два номера.
ODIN_RAZBOR = {"9", "9а"}


def vidimyy_sloy(path):
    t = path.read_text(encoding="utf-8")
    if "## Видимый текст слайда" not in t:
        return ""
    return t.split("## Видимый текст слайда")[1].split("## Заметки")[0]


def kadr(sid):
    hits = [p for p in SLIDES.glob("*.md") if re.match(rf"^{sid}-", p.name)]
    return hits[0] if len(hits) == 1 else None


def razborov_po_divayderam():
    """Знаменатель — независимо от реестра: «Пример N» в телах дивайдеров."""
    vsego, po_razdelam = 0, {}
    for p in sorted(SLIDES.glob("*.md")):
        t = p.read_text(encoding="utf-8")
        fm = t.split("---")[1] if t.startswith("---") else ""
        if not re.search(r"^type:\s*divider", fm, re.M):
            continue
        sec = re.search(r'^section:\s*"(.*?)"', fm, re.M)
        sec = sec.group(1) if sec else p.name
        nomera = set(re.findall(r"Пример (\d+)", vidimyy_sloy(p)))
        if nomera:
            po_razdelam[sec] = len(nomera)
            vsego += len(nomera)
    return vsego, po_razdelam


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--samoproverka", action="store_true",
                    help="контрольный прогон: заведомо отсутствующая опора обязана найтись")
    args = ap.parse_args()

    if args.samoproverka:
        # Ноль, полученный без контрольного прогона, не означает ничего
        # (`proverka_nalozheniy.py`, та же причина).
        p = kadr("s97")
        assert p is not None, "самопроверка: кадра s97 нет — проверять нечем"
        vis = vidimyy_sloy(p)
        assert "форма" in vis.lower(), "самопроверка: видимый слой не читается"
        fake = "ЗАВЕДОМО ОТСУТСТВУЮЩАЯ ОПОРА"
        assert fake not in vis, "самопроверка сломана: подложная опора нашлась"
        # и обратное: опора, стоящая только в заметках, зачёта не даёт
        t = p.read_text(encoding="utf-8")
        zam = t.split("## Заметки")[-1]
        tolko_v_zametkah = [w for w in ("Вопрос залу стоит задать",) if w in zam and w not in vis]
        assert tolko_v_zametkah, "самопроверка: не нашлось фразы, живущей только в заметках"
        print("самопроверка пройдена: видимый слой отделён от заметок, "
              "подложная опора не засчитана")
        return 0

    bad = []
    po_grafam = {1: set(), 2: set(), 3: set()}
    for nom, sid, opora, grafa in OPORY:
        p = kadr(sid)
        if p is None:
            bad.append(f"строка {nom}: кадра {sid} в деке нет")
            continue
        vis = vidimyy_sloy(p)
        if opora not in vis:
            gde = "в заметках" if opora in p.read_text(encoding="utf-8") else "нигде"
            bad.append(f"строка {nom} ({sid}): опоры «{opora}» в видимом слое нет — {gde}")
            continue
        po_grafam[grafa].add("9" if nom in ODIN_RAZBOR else nom)

    upom = []
    for name, sid, opora, grafa in NA_UPOMINANII:
        p = kadr(sid)
        if p is not None and opora in vidimyy_sloy(p):
            upom.append(f"{name} ({sid}, графа {grafa})")
        else:
            bad.append(f"упоминание {name}: опоры «{opora}» в видимом слое {sid} нет")

    vsego, po_razdelam = razborov_po_divayderam()
    vse_razbory = set().union(*po_grafam.values())
    s_pripiskoy = len(vse_razbory)

    # ДВА ЧИСЛА, И ПУТАТЬ ИХ НЕЛЬЗЯ (`forma.md` §11.8 — два похожих числа в
    # разных смысловых ролях это тот же дефект, даже если они не в одной фразе).
    # Номинаций больше, чем разборов: разбор 9 несёт две приписки разных граф.
    # Разбор зачитывается графе, в которой он встретился ВПЕРВЫЕ по порядку
    # реестра, иначе сумма по графам разойдётся со счётом разборов.
    nominaciy = {g: len(po_grafam[g]) for g in (1, 2, 3)}
    razborov_grafy, vidano = {}, set()
    for _nom, _sid, _op, g in OPORY:
        kto = "9" if _nom in ODIN_RAZBOR else _nom
        if kto in vse_razbory and kto not in vidano:
            vidano.add(kto)
            razborov_grafy[g] = razborov_grafy.get(g, 0) + 1

    print("РАЗБОРЫ (знаменатель, по дивайдерам — независимо от реестра)")
    for sec in sorted(po_razdelam):
        print(f"   {sec}: {po_razdelam[sec]}")
    print(f"   всего: {vsego}\n")
    print("ПРИПИСКИ (числитель, по реестру, зачёт только по видимому слою)")
    for g in (1, 2, 3):
        print(f"   графа {g}: разборов {razborov_grafy.get(g, 0)}, "
              f"номинаций {nominaciy[g]}")
    print(f"   РАЗБОРОВ С ПРИПИСКОЙ: {s_pripiskoy} из {vsego} "
          f"(сумма по графам {'+'.join(str(razborov_grafy.get(g, 0)) for g in (1,2,3))})")
    print(f"   номинаций на разборах: {sum(nominaciy.values())} — "
          f"больше разборов на {sum(nominaciy.values()) - s_pripiskoy}: "
          f"разбор 9 несёт две приписки")
    print(f"   на упоминании, в знаменатель не входит: {', '.join(upom) or '—'}\n")
    if sum(razborov_grafy.values()) != s_pripiskoy:
        bad.append("сумма по графам не сходится со счётом разборов")

    if bad:
        print("РАСХОЖДЕНИЯ:")
        for b in bad:
            print("   ✗ " + b)
        return 1
    print("расхождений нет: каждая строка реестра стоит на своём кадре в видимом слое")
    return 0


if __name__ == "__main__":
    sys.exit(main())
