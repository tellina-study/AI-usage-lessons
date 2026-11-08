# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «ЭПОХИ»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Лесенку отступа, разную обводку карточек и золотую плашку вывода видит
только глаз (`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_epohi [--render]
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import epohi as E
from . import prims, render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "epohi"


def say(line):
    SAID.append(line)
    print(line)


def _sl(ep, sid="проба"):
    return types.SimpleNamespace(sid=sid, meta={"epohi": ep})


DEMO = {
    "left": {
        "head": "2006 — сработало",
        "steps": [
            {"label": "Событие", "text": "цена фото падает"},
            {"label": "Реакция", "text": "покупают разрушителя цены"},
            {"label": "Итог", "text": "рынок разделился, игрок уцелел"},
        ],
        "vyvod": "микросток был новым каналом продажи той же вещи",
    },
    "right": {
        "head": "2026 — не прошло",
        "steps": [
            {"label": "Событие", "text": "генератор обесценивает исполнение"},
            {"label": "Реакция", "text": "покупают генератор, не фото"},
            {"label": "Итог",
             "text": "покупать нечего: у вещи не стало владельца"},
        ],
        "vyvod": "покупать нечего: у вещи не стало владельца",
    },
    "obshchiy_vyvod": (
        "когда дешевеет канал — выживает тот, кто его купит; когда "
        "обесценивается сама единица — покупать нечего"),
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=24.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    E.check_epohi("проба", d, w)
    E.draw_epohi(s, "проба", d, mx, top, w)
    return s


def _run(meta, w=12.23):
    report.reset()
    d = E.epohi_of(_sl(meta))
    if d:
        E.check_epohi("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[эпохи-чистая] {len(warns)} предупреждений на "
                   f"здоровом кадре: {warns[:2]}")
    else:
        say(f"{'[эпохи-чистая]':<26} здоровый кадр: МОЛЧИТ  →  "
            f"«{d['left']['head']}» / «{d['right']['head']}»")
        ok.append("[эпохи-чистая]")


def _copy(src):
    return {"left": {"head": src["left"]["head"],
                     "steps": [dict(s2) for s2 in src["left"]["steps"]],
                     "vyvod": src["left"]["vyvod"]},
            "right": {"head": src["right"]["head"],
                      "steps": [dict(s2) for s2 in src["right"]["steps"]],
                      "vyvod": src["right"]["vyvod"]},
            "obshchiy_vyvod": src["obshchiy_vyvod"]}


_PARSE_CASES = (
    ("нет right", "а должно быть head/steps/vyvod",
     lambda m: m.__setitem__("right", None)),
    ("left не словарь", "а должно быть head/steps/vyvod",
     lambda m: m.__setitem__("left", "строка")),
    ("чужой ключ карточки", "ядро не читает",
     lambda m: m["left"].__setitem__("цвет", "gold")),
    ("карточка без head", "нет `head`",
     lambda m: m["left"].__setitem__("head", "")),
    ("карточка без steps", "нет `steps`",
     lambda m: m["left"].__setitem__("steps", [])),
    ("ступень не словарь", "а должна быть label/text",
     lambda m: m["left"]["steps"].insert(0, "строка")),
    ("чужой ключ ступени", "ядро не читает",
     lambda m: m["left"]["steps"][0].__setitem__("цвет", "gold")),
    ("ступень без label", "без `label`",
     lambda m: m["left"]["steps"][0].__setitem__("label", "")),
    ("ступень без text", "без `text`",
     lambda m: m["right"]["steps"][0].__setitem__("text", "")),
    ("карточка без vyvod", "нет `vyvod`",
     lambda m: m["left"].__setitem__("vyvod", "")),
    ("разное число ступеней", "ступеней слева",
     lambda m: m["right"]["steps"].pop()),
    ("чужой ключ формы", "ядро не читает",
     lambda m: m.__setitem__("most", "мост")),
)


def probe_parse(ok, bad, say):
    report.reset()
    d0 = E.epohi_of(types.SimpleNamespace(sid="проба",
                                          meta={"epohi": ["строка"]}))
    hit0 = _hits(list(report.WARNINGS),
                "а должно быть left/right/obshchiy_vyvod")
    if d0 is not None or not hit0:
        bad.append(f"[эпохи/поле не словарь] не сработало; вышло: "
                   f"{report.WARNINGS}")
    else:
        say(f"{'[эпохи]':<10} {'поле не словарь':<24} ЛОВИТ  →  "
            f"{hit0[0].split(': ', 1)[-1][:78]}…")
        ok.append("[эпохи/поле не словарь]")

    for name, needle, mutate in _PARSE_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        d, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[эпохи/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[эпохи]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[эпохи/{name}]")


_CHECK_CASES = (
    ("шестая ступень", "ступеней 6 (>",
     lambda m: m["left"]["steps"].extend([
         {"label": "Четыре", "text": "текст"},
         {"label": "Пять", "text": "текст"},
         {"label": "Шесть", "text": "текст"}])),
    ("ступень одна", "ступень одна",
     lambda m: (m["left"].__setitem__("steps", m["left"]["steps"][:1]),
                m["right"].__setitem__("steps", m["right"]["steps"][:1]))),
    ("длинное слово ступени", "не хватает ширины",
     lambda m: m["left"]["steps"][0].__setitem__(
         "text", "Сверхдлинноесловобезпробеловкотороенепоместитсявкарточку")),
)


def probe_broken(ok, bad, say):
    for name, needle, mutate in _CHECK_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[эпохи/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[эпохи]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[эпохи/{name}]")


def probe_tight(ok, bad, say):
    """Тесная карточка — РАЗНОСТНАЯ проба: обычная ширина молчит, узкая —
    называет."""
    _, wide = _run(DEMO, w=12.23)
    _, nar = _run(DEMO, w=3.0)
    w_hit = _hits(wide, "карточка вышла")
    n_hit = _hits(nar, "карточка вышла")
    if w_hit or not n_hit:
        bad.append(f"[эпохи-тесная] широкая {len(w_hit)}, узкая "
                   f"{len(n_hit)} — проба ловит не ширину")
        return
    say(f"{'[эпохи-тесная]':<26} тесная карточка: ЛОВИТ  →  {n_hit[0][:100]}")
    ok.append("[эпохи-тесная]")


def probe_gold(ok, bad, say):
    """Золото — ЗАЛИВКОЙ строки-вывода внутри карточки. Разностно: та же
    карточка без `vyvod` золота не даёт."""
    for has, want in ((True, True), (False, False)):
        meta = _copy(DEMO)
        if not has:
            meta["left"]["vyvod"] = ""
            meta["right"]["vyvod"] = ""
            meta["obshchiy_vyvod"] = ""
        report.reset()
        d = E.epohi_of(_sl(meta))
        p = prims.new_deck()
        demo_slide(p, d, "проба золота")
        got = "проба" in report.GOLD_SEEN
        if got is not want:
            bad.append(f"[эпохи-золото] vyvod={has}: золото "
                       f"{'есть' if got else 'нет'}, ждали обратного")
            return
    say(f"{'[эпохи-золото]':<26} вывод карточки: ЗАЛИВКОЙ  →  с `vyvod` "
        "золото на кадре есть, без него — нет")
    ok.append("[эпохи-золото]")


def probe_height(ok, bad, say):
    report.reset()
    d = E.epohi_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    w = SLIDE_W - 2 * 0.55
    promised = E.epohi_h(d, w)
    drawn = E.draw_epohi(s, "проба", d, 0.55, 1.46, w)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[эпохи-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - 1.46:.3f}\"")
        return
    say(f"{'[эпохи-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\"")
    ok.append("[эпохи-мера]")


def build_demo(out=OUT):
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = E.epohi_of(_sl(DEMO))
    demo_slide(p, d, "Карточки двух эпох: 2006 против 2026")
    no_obshchiy = _copy(DEMO)
    no_obshchiy["obshchiy_vyvod"] = ""
    demo_slide(p, E.epohi_of(_sl(no_obshchiy)),
              "Без общего вывода — только карточки")
    pptx = out / "epohi.pptx"
    p.save(str(pptx))
    print(f"\nсобрано: {pptx}")
    for wline in report.WARNINGS:
        print("  " + wline)
    if not report.WARNINGS:
        print("  предупреждений нет")
    return render.render(pptx, out, dpi=110)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    probe_clean(OK, BAD, say)
    probe_parse(OK, BAD, say)
    probe_broken(OK, BAD, say)
    probe_tight(OK, BAD, say)
    probe_gold(OK, BAD, say)
    probe_height(OK, BAD, say)
    print(f"\nпроб пройдено {len(OK)}, провалено {len(BAD)}")
    for b in BAD:
        print("  ПРОВАЛ " + b)
    rc = 1 if BAD else 0
    if "--render" in argv:
        rc = build_demo() or rc
    return rc


if __name__ == "__main__":
    sys.exit(main())
