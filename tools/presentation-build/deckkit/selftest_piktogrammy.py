# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ПИКТОГРАММНОЙ СЕТКИ: демонстрационный кадр и прогон КАЖДОГО
отказа, какой `piktogrammy.py` умеет заявить.

Стандарт пакета один: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ
ПРОВЕРКА. Демонстрационная разметка (`PIK_CLEAN`, `PIK_30`, `PIK_50`) и
бо́льшая часть сломанных входов (`PIK_BAD`) взяты из `probes_formy.py` —
они собирались вместе с таймлайном и плашкой-выводом в той же нити.
Сверх них здесь одна проба, которой не было в исходном словаре: узкая
колонка, которой не хватает места под подписи (`check_pikto`'s `need > w`).

Сверх прогонов — СОБРАННЫЙ КАДР. Половина того, что отличает «долю как
площадь» от узора, глазами мерится, а не координатами: различимы ли золотые
фигурки среди контурных НА РАССТОЯНИИ (уменьшенный снимок), не слиплась ли
сетка в сплошное пятно, напечатан ли знаменатель
(`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_piktogrammy          (сборка + прогоны)
         python3 -m deckkit.selftest_piktogrammy --render  (ещё и снимки PNG)
"""
import sys
from pathlib import Path

from . import metrics, piktogrammy as pikto, prims, probes_formy as PF
from . import render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OUT = Path(__file__).resolve().parents[1] / "probe-out" / "piktogrammy"
MX, TOP, FOOT = 0.55, 1.46, 6.94
FULL_W = SLIDE_W - 2 * MX

OK, BAD = [], []


def say(line):
    print(line)


def frame(p, title, raw, foot):
    d = pikto.pikto_of("проба", raw)
    pikto.check_pikto("проба", d, FULL_W)
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    sz = metrics.fit_size(title, FULL_W, 0.92, hi=27.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 0.40, FULL_W, 0.92, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag="проба/заголовок")
    h = pikto.pikto_h(d, FULL_W)
    got = pikto.draw_pikto(s, "проба", d, MX, TOP, FULL_W)
    if abs(got - h) > 0.02:
        BAD.append(f"[пиктограммы-мера] мера обещала {h:.3f}\", рисунок "
                   f"занял {got:.3f}\" — две формулы одного числа")
    if TOP + got > FOOT:
        BAD.append(f"[пиктограммы-мера] форма дошла до подвала: низ "
                   f"{TOP + got:.2f}\" при подвале {FOOT:.2f}\"")
    prims.text_box(s, MX, FOOT, FULL_W, 0.40, foot, size=11.0, italic=True,
                   color=DEEP, ls=1.12, tag="проба/подвал", quiet=True)
    return d


def build(path):
    report.reset()
    p = prims.new_deck()
    frame(p, "Пять человек сделали то, что отбирали девяносто пять",
          PF.PIK_CLEAN,
          "служебный кадр самопроверки ядра · 100 фигурок, доля 5")
    frame(p, "Почти треть рабочего дня иллюстратора уходит до правок",
          PF.PIK_30,
          "служебный кадр самопроверки ядра · 100 фигурок, доля 30")
    frame(p, "Меньше пятой части суточной загрузки — целиком модель",
          PF.PIK_50,
          "служебный кадр самопроверки ядра · 50 фигурок, доля 9")
    p.save(str(path))
    w = list(report.WARNINGS)
    report.reset()
    return w


# ── прогоны отказов ─────────────────────────────────────────────────


def run(raw, w=FULL_W):
    report.reset()
    d = pikto.pikto_of("проба", raw)
    if d is not None:
        pikto.check_pikto("проба", d, w)
    out = list(report.WARNINGS)
    report.reset()
    return d, out


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe(name, raw, needle, w=FULL_W):
    _, clean = run(PF.PIK_CLEAN)
    d, got = run(raw, w)
    hit = _hits(got, needle)
    if _hits(clean, needle):
        BAD.append(f"[{name}] чистый вход тоже говорит «{needle}» — "
                   "проба ловит не этот сторож")
        return
    if not hit:
        BAD.append(f"[{name}] сломанный вход молчит про «{needle}»; "
                   f"сказано: {got or 'ничего'}")
        return
    OK.append(name)
    say(f"{'[' + name + ']':<26} ЛОВИТ  →  {hit[0][:118]}")


NEEDLES = {
    "не-словарь": ("[пиктограммы] не словарь", "должно быть"),
    "целое-не-число": ("[пиктограммы] целое не число", "не целое число"),
    "доля-не-число": ("[пиктограммы] доля не число", "не целое число"),
    "ключ": ("[пиктограммы] ключ", "форма не читает"),
    "нет-знаменателя": ("[пиктограммы] нет знаменателя", "ЗНАМЕНАТЕЛЬ"),
    "доля-больше-целого": ("[пиктограммы] доля больше целого",
                          "больше целого"),
    "доля-ноль": ("[пиктограммы] доля ноль", "доля 0"),
    "доля-отрицательна": ("[пиктограммы] доля отрицательна",
                         "отрицательна"),
    "целое-велико": ("[пиктограммы] целое велико", "сольются в заливку"),
    "целое-мало": ("[пиктограммы] целое мало", "читается перечислением"),
    "нет-подписи-доли": ("[пиктограммы] нет подписи доли",
                        "у доли нет подписи"),
    "нет-подписи-остатка": ("[пиктограммы] нет подписи остатка",
                           "у остатка нет подписи"),
}


def probes():
    for name, raw in (("чисто-5-из-100", PF.PIK_CLEAN),
                      ("чисто-30-из-100", PF.PIK_30),
                      ("чисто-9-из-50", PF.PIK_50)):
        _, got = run(raw)
        if got:
            BAD.append(f"[{name}] чистый вход дал {len(got)} "
                       f"предупреждений: {got}")
        else:
            OK.append(name)
            say(f"{'[' + name + ']':<26} МОЛЧИТ на чистом входе")

    for name, (key, needle) in NEEDLES.items():
        probe(name, PF.PIK_BAD[key], needle)

    missing = set(PF.PIK_BAD) - {k for k, _n in NEEDLES.values()}
    if missing:
        BAD.append(f"[пиктограммы-полнота] в PIK_BAD есть вход(ы), на "
                   f"которые нет пробы: {sorted(missing)}")

    # Тринадцатая причина отказа — та, которой не было в исходном словаре:
    # узкая колонка, которой не хватает места под подписи рядом с сеткой.
    # Проба НАРОЧНО разностная: на обычной колонке (FULL_W) `check_pikto`
    # обязан молчать про ширину, на узкой — назвать её числом.
    _, wide = run(PF.PIK_CLEAN, w=FULL_W)
    _, nar = run(PF.PIK_CLEAN, w=3.0)
    if _hits(wide, "сядут на фигурки"):
        BAD.append(f"[узкая-колонка] широкая колонка тоже жалуется: {wide}")
    elif not _hits(nar, "сядут на фигурки"):
        BAD.append(f"[узкая-колонка] узкая колонка молчит: {nar}")
    else:
        OK.append("узкая-колонка")
        say(f"{'[узкая-колонка]':<26} ЛОВИТ  →  "
            f"{_hits(nar, 'сядут на фигурки')[0][:118]}")


# ── мера, золото, читаемость доли на расстоянии ─────────────────────


def probe_gold_is_fill():
    """Золото — заливка ДОЛИ фигурок, остаток контурный без заливки.
    Разностно: доля 0 не даёт золота вовсе (`check_pikto` отдельно
    предупреждает про это как про содержательный дефект, но и рисунок
    обязан вести себя соответственно)."""
    report.reset()
    d = pikto.pikto_of("проба", PF.PIK_CLEAN)
    p = prims.new_deck()
    s = prims.blank(p)
    pikto.draw_pikto(s, "проба-золото", d, MX, TOP, FULL_W)
    if "проба-золото" not in report.GOLD_SEEN:
        BAD.append("[пиктограммы-золото] золота на кадре с долей 5 нет")
        return
    say(f"{'[пиктограммы-золото]':<26} ЗАЛИВКОЙ  →  {d['dolya']} из "
        f"{d['vsego']} фигурок залиты, остаток контурный")
    OK.append("пиктограммы-золото")


def probe_height():
    report.reset()
    d = pikto.pikto_of("проба", PF.PIK_CLEAN)
    p = prims.new_deck()
    s = prims.blank(p)
    promised = pikto.pikto_h(d, FULL_W)
    drawn = pikto.draw_pikto(s, "проба", d, MX, TOP, FULL_W)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > TOP + promised + 0.02:
        BAD.append(f"[пиктограммы-мера] обещано {promised:.3f}\", "
                   f"нарисовано {drawn:.3f}\", низ фигур "
                   f"{bottom - TOP:.3f}\"")
        return
    say(f"{'[пиктограммы-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - TOP:.3f}\"")
    OK.append("пиктограммы-мера")


def probe_grid_is_square_ish():
    """Сто фигурок обязаны лечь квадратом 10×10, а не лентой в один ряд —
    `grid_cols` и есть сторож этого выбора. Разностная проба: число, не
    делящееся на десять (50), берёт СВОЙ делитель, не растягиваясь в один
    ряд из пятидесяти."""
    c100 = pikto.grid_cols(100)
    c50 = pikto.grid_cols(50)
    if c100 != 10:
        BAD.append(f"[пиктограммы-сетка] 100 фигурок дали {c100} столбцов, "
                   "а не 10 — квадрат развалился")
        return
    if c50 >= 50 or c50 < 2:
        BAD.append(f"[пиктограммы-сетка] 50 фигурок дали {c50} столбцов — "
                   "это лента, а не сетка")
        return
    say(f"{'[пиктограммы-сетка]':<26} разностно: ЛОВИТ  →  100 фигурок "
        f"→ {c100} столбцов (квадрат), 50 → {c50} столбцов")
    OK.append("пиктограммы-сетка")


def main(argv=()):
    OUT.mkdir(parents=True, exist_ok=True)
    pptx = OUT / "proba-piktogrammy.pptx"
    warns = build(pptx)
    if warns:
        BAD.append(f"[сборка] демонстрационные кадры дали {len(warns)} "
                   f"предупреждений: {warns}")
    else:
        OK.append("сборка")
        say(f"{'[сборка]':<26} три кадра собраны чисто  →  {pptx}")
    probes()
    probe_gold_is_fill()
    probe_height()
    probe_grid_is_square_ish()
    if "--render" in argv:
        if render.render(pptx, OUT / "snaps"):
            BAD.append("[рендер] PDF или снимки не собрались")
    print(f"\nпрошло {len(OK)} · не прошло {len(BAD)}")
    for b in BAD:
        print("  " + b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
