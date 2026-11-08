# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ТАЙМЛАЙНА: демонстрационные кадры ОБЕИХ разновидностей и
прогон КАЖДОГО отказа, какой `timeline.py` умеет заявить.

Стандарт пакета один: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ
ПРОВЕРКА. На сторож `check_timeline` (и на разбор `timeline_of`) — по
прогону на каждую причину, и каждый обязан сказать СВОЁ, а чистый вход —
молчать про него же. Сломанные входы и демонстрационная разметка взяты из
`probes_formy.py` (TL_STADII / TL_STADII_TIERS / TL_SROKI / TL_SROKI_4 /
TL_BAD) — они собирались вместе с тремя другими формами этой же нити.

Сверх прогонов — СОБРАННЫЕ КАДРЫ, четыре: стадии · стадии с двумя
привязками на одной точке (ярусы) · сроки о двух полосах · сроки о
четырёх. Половина того, что отличает «все стоят в разных местах» от
«перечня текстом», координатами не меряется: сошлись ли подписи стадий,
разведены ли коробки одного яруса, названа ли единица — глаз пока ничем не
заменяется (`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_timeline          (сборка + прогоны)
         python3 -m deckkit.selftest_timeline --render  (ещё и снимки PNG)
"""
import sys
from pathlib import Path

from . import metrics, prims, probes_formy as PF, render, report, timeline
from .theme import DEEP, LIGHT, SLIDE_H, SLIDE_W, WHITE

OUT = Path(__file__).resolve().parents[1] / "probe-out" / "timeline"
MX, TOP, FOOT = 0.55, 1.46, 6.94
FULL_W = SLIDE_W - 2 * MX

OK, BAD = [], []


def say(line):
    print(line)


def frame(p, title, raw, foot):
    """Один демонстрационный кадр. `foot=""` — у кадра нет строки подвала
    (четырёхрядные сроки сами занимают почти всю высоту тела, и подвал
    под ними либо не ставится, либо наезжает на форму — тот же дефект,
    какой ловит `[высота]` у любой другой формы пакета)."""
    d = timeline.timeline_of("проба", raw)
    timeline.check_timeline("проба", d, FULL_W)
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    sz = metrics.fit_size(title, FULL_W, 0.92, hi=27.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 0.40, FULL_W, 0.92, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag="проба/заголовок")
    h = timeline.timeline_h(d, FULL_W)
    got = timeline.draw_timeline(s, "проба", d, MX, TOP, FULL_W)
    if abs(got - h) > 0.02:
        BAD.append(f"[таймлайн-мера] мера обещала {h:.3f}\", рисунок "
                   f"занял {got:.3f}\" — две формулы одного числа")
    bottom_limit = FOOT if foot else SLIDE_H - 0.12
    if TOP + got > bottom_limit:
        BAD.append(f"[таймлайн-мера] форма дошла до подвала: низ "
                   f"{TOP + got:.2f}\" при пределе {bottom_limit:.2f}\"")
    if foot:
        prims.text_box(s, MX, FOOT, FULL_W, 0.40, foot, size=11.0,
                       italic=True, color=LIGHT, ls=1.12,
                       tag="проба/подвал")
    return d


def build(path):
    report.reset()
    p = prims.new_deck()
    frame(p, "Правовой контур: один путь, разные страны стоят по-разному",
          PF.TL_STADII, "служебный кадр самопроверки ядра · стадии")
    frame(p, "Две привязки на одной стадии разводятся ярусом вниз",
          PF.TL_STADII_TIERS, "служебный кадр самопроверки ядра · стадии, "
          "ярусы привязок")
    frame(p, "Во сколько раз быстрее: две полосы одной шкалы",
          PF.TL_SROKI, "служебный кадр самопроверки ядра · сроки, две "
          "строки")
    frame(p, "Четыре перехода подряд на одной шкале месяцев",
          PF.TL_SROKI_4, "")
    p.save(str(path))
    w = list(report.WARNINGS)
    report.reset()
    return w


# ── прогоны отказов ─────────────────────────────────────────────────


def run(raw, w=FULL_W):
    report.reset()
    d = timeline.timeline_of("проба", raw)
    if d is not None:
        timeline.check_timeline("проба", d, w)
    out = list(report.WARNINGS)
    report.reset()
    return d, out


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe(name, raw, needle, w=FULL_W, clean=PF.TL_STADII):
    """Один отказ: сломанный вход обязан сказать именно про `needle`, а
    чистый — промолчать про него же."""
    _, cw = run(clean)
    d, got = run(raw, w)
    hit = _hits(got, needle)
    if _hits(cw, needle):
        BAD.append(f"[{name}] чистый вход тоже говорит «{needle}» — "
                   "проба ловит не этот сторож")
        return
    if not hit:
        BAD.append(f"[{name}] сломанный вход молчит про «{needle}»; "
                   f"сказано: {got or 'ничего'}")
        return
    OK.append(name)
    say(f"{'[' + name + ']':<26} ЛОВИТ  →  {hit[0][:118]}")


# Имя пробы → (ключ в `TL_BAD`, нужное слово, чистая разметка для сравнения)
NEEDLES = {
    "разновидность": ("[таймлайн] разновидность", "не та", PF.TL_STADII),
    "не-словарь": ("[таймлайн] не словарь", "должно быть", PF.TL_STADII),
    "ключ": ("[таймлайн] ключ", "форма не читает", PF.TL_STADII),
    "ключ-привязки": ("[таймлайн] ключ привязки", "форма не читает",
                      PF.TL_STADII),
    "нет-стадий": ("[таймлайн] нет стадий", "нет `stages`", PF.TL_STADII),
    "стадия-без-имени": ("[таймлайн] стадия без имени", "без названия",
                        PF.TL_STADII),
    "at-не-номер": ("[таймлайн] at не номер", "НОМЕР стадии", PF.TL_STADII),
    "at-вне-ряда": ("[таймлайн] at вне ряда", "привязывать не к чему",
                   PF.TL_STADII),
    "единица": ("[таймлайн] единица", "не названа ЕДИНИЦА", PF.TL_STADII),
    "мало-стадий": ("[таймлайн] мало стадий", "путь из двух точек",
                   PF.TL_STADII),
    "много-стадий": ("[таймлайн] много стадий", "таблица стадий",
                    PF.TL_STADII),
    "мало-привязок": ("[таймлайн] мало привязок", "расходиться не с кем",
                      PF.TL_STADII),
    "много-привязок": ("[таймлайн] много привязок", "выноски перепутаются",
                       PF.TL_STADII),
    "привязка-без-ярлыка": ("[таймлайн] привязка без ярлыка", "нет `head`",
                           PF.TL_STADII),
    "привязка-без-разбора": ("[таймлайн] привязка без разбора",
                            "нет `text`", PF.TL_STADII),
    "подписи-сошлись": ("[таймлайн] подписи сошлись", "разорвёт посреди "
                       "корня", PF.TL_STADII),
    "коробки-наложились": ("[таймлайн] коробки наложились", "друг от "
                          "друга при коробке", PF.TL_STADII),
    "нет-сроков": ("[таймлайн] нет сроков", "сравнивать длиной нечего",
                  PF.TL_SROKI),
    "срок-не-число": ("[таймлайн] срок не число", "не число", PF.TL_SROKI),
    "срок-ноль": ("[таймлайн] срок ноль", "полосы нулевой", PF.TL_SROKI),
    "один-срок": ("[таймлайн] один срок", "второй длины", PF.TL_SROKI),
    "много-сроков": ("[таймлайн] много сроков", "попарно", PF.TL_SROKI),
    "срок-без-имени": ("[таймлайн] срок без имени", "нет `label`",
                      PF.TL_SROKI),
    "полосы-не-видно": ("[таймлайн] полосы не видно", "на экране её нет",
                       PF.TL_SROKI),
    "ключ-срока": ("[таймлайн] ключ срока", "форма не читает", PF.TL_SROKI),
}


def probes():
    for name, raw in (("чисто-стадии", PF.TL_STADII),
                      ("чисто-стадии-ярусы", PF.TL_STADII_TIERS),
                      ("чисто-сроки", PF.TL_SROKI),
                      ("чисто-сроки-4", PF.TL_SROKI_4)):
        _, got = run(raw)
        if got:
            BAD.append(f"[{name}] чистый вход дал {len(got)} "
                       f"предупреждений: {got}")
        else:
            OK.append(name)
            say(f"{'[' + name + ']':<26} МОЛЧИТ на чистом входе")

    for name, (key, needle, clean) in NEEDLES.items():
        probe(name, PF.TL_BAD[key], needle, clean=clean)

    missing = set(PF.TL_BAD) - {k for k, _n, _c in NEEDLES.values()}
    if missing:
        BAD.append(f"[таймлайн-полнота] в TL_BAD есть вход(ы), на которые "
                   f"нет пробы: {sorted(missing)}")

    # Отдельно: привязка/срок, которые не словарь, — разбор снимает ЭТУ
    # запись, а не форму целиком, и это другой путь кода, чем «ключ».
    d, got = run({"unit": "стадия", "stages": ["а", "б", "в"],
                 "marks": ["не словарь", {"at": 2, "head": "B",
                                          "text": "т"}]})
    if d is None or not _hits(got, "не at/head/text"):
        BAD.append(f"[привязка-не-словарь] не сработало: {got}")
    else:
        OK.append("привязка-не-словарь")
        say(f"{'[привязка-не-словарь]':<26} ЛОВИТ  →  "
            f"{_hits(got, 'не at/head/text')[0][:100]}")

    d, got = run({"mode": "sroki", "unit": "месяцы",
                 "rows": ["не словарь",
                         {"label": "B", "value": 18, "text": "т"}]})
    if d is None or not _hits(got, "не label/value/text"):
        BAD.append(f"[срок-не-словарь] не сработало: {got}")
    else:
        OK.append("срок-не-словарь")
        say(f"{'[срок-не-словарь]':<26} ЛОВИТ  →  "
            f"{_hits(got, 'не label/value/text')[0][:100]}")


# ── мера, золото, разностная видимость ──────────────────────────────


def probe_heights():
    """Мера совпадает с рисованием для всех четырёх демонстрационных
    разметок — у обеих разновидностей своя формула высоты."""
    for name, raw in (("стадии", PF.TL_STADII),
                      ("стадии-ярусы", PF.TL_STADII_TIERS),
                      ("сроки", PF.TL_SROKI), ("сроки-4", PF.TL_SROKI_4)):
        report.reset()
        d = timeline.timeline_of("проба", raw)
        p = prims.new_deck()
        s = prims.blank(p)
        promised = timeline.timeline_h(d, FULL_W)
        drawn = timeline.draw_timeline(s, "проба", d, MX, TOP, FULL_W)
        bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
        if abs(promised - drawn) > 1e-9 or bottom > TOP + promised + 0.02:
            BAD.append(f"[таймлайн-мера/{name}] обещано {promised:.3f}\", "
                       f"нарисовано {drawn:.3f}\", низ фигур "
                       f"{bottom - TOP:.3f}\"")
            continue
        say(f"{'[таймлайн-мера/' + name + ']':<26} мера = рисование  →  "
            f"{promised:.3f}\"")
        OK.append(f"таймлайн-мера/{name}")


def probe_gold():
    """Золото есть на обеих разновидностях, и приходит ЗАЛИВКОЙ — ярлыка
    привязки у стадий, плашки значения у сроков, — не цветом текста."""
    for name, raw in (("стадии", PF.TL_STADII), ("сроки", PF.TL_SROKI)):
        report.reset()
        d = timeline.timeline_of("проба", raw)
        p = prims.new_deck()
        s = prims.blank(p)
        sid = f"проба-золото-{name}"
        timeline.draw_timeline(s, sid, d, MX, TOP, FULL_W)
        if sid not in report.GOLD_SEEN:
            BAD.append(f"[таймлайн-золото/{name}] золота на кадре нет")
            continue
        say(f"{'[таймлайн-золото/' + name + ']':<26} ЗАЛИВКОЙ  →  золотой "
            "текст форма не ставит нигде")
        OK.append(f"таймлайн-золото/{name}")


def probe_scale_log_vs_linear():
    """Разностная проба, разъясняющая §2.5 переноса: у сроков длина полосы
    несёт отношение «во сколько раз быстрее» — не подпись и не порядок
    строк. Перевёрнутый порядок строк (медленный первой) не меняет ДЛИНУ
    полосы самого длинного срока, только её позицию в списке."""
    report.reset()
    d = timeline.timeline_of("проба", PF.TL_SROKI)
    bw_slow = timeline.bar_w(d["rows"][0], d, FULL_W)
    bw_fast = timeline.bar_w(d["rows"][1], d, FULL_W)
    report.reset()
    if bw_slow <= bw_fast:
        BAD.append(f"[таймлайн-длина] историческая полоса {bw_slow:.2f}\" "
                   f"не длиннее новой {bw_fast:.2f}\" — а срок у неё в "
                   f"{d['rows'][0]['v'] / d['rows'][1]['v']:.0f} раз больше")
        return
    say(f"{'[таймлайн-длина]':<26} разностно: ЛОВИТ  →  14 лет "
        f"{bw_slow:.2f}\", 18 месяцев {bw_fast:.2f}\" — отношение несёт "
        "ДЛИНА, а не подпись")
    OK.append("таймлайн-длина")


def main(argv=()):
    OUT.mkdir(parents=True, exist_ok=True)
    pptx = OUT / "proba-timeline.pptx"
    warns = build(pptx)
    if warns:
        BAD.append(f"[сборка] демонстрационные кадры дали {len(warns)} "
                   f"предупреждений: {warns}")
    else:
        OK.append("сборка")
        say(f"{'[сборка]':<26} четыре кадра собраны чисто  →  {pptx}")
    probes()
    probe_heights()
    probe_gold()
    probe_scale_log_vs_linear()
    if "--render" in argv:
        if render.render(pptx, OUT / "snaps"):
            BAD.append("[рендер] PDF или снимки не собрались")
    print(f"\nпрошло {len(OK)} · не прошло {len(BAD)}")
    for b in BAD:
        print("  " + b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
