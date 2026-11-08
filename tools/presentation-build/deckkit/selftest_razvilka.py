# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «РАЗВИЛКА»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Главный сторож формы — ОДИНАКОВЫЙ набор строк в обеих ветках — проверен
отдельно; читается ли подпись ДА/НЕТ рядом с линией, а не поверх неё
(первый же снимок поймал ровно это и был исправлен), видит только глаз
(`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_razvilka [--render]
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import prims, razvilka as R, render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "razvilka"


def say(line):
    SAID.append(line)
    print(line)


def _sl(rv, sid="проба"):
    return types.SimpleNamespace(sid=sid, meta={"razvilka": rv})


DEMO = {
    "vopros": "Критерий задан физикой и проверяемыми условиями?",
    "da": {
        "head": "Бионическая перегородка",
        "rows": [
            {"label": "Инструмент",
             "text": "САПР и оптимизация, не генеративная модель"},
            {"label": "Результат", "text": "65 кг → 35 кг"},
            {"label": "Ограничения", "text": "спора об авторстве нет"},
        ],
    },
    "net": {
        "head": "Баннеры журнала",
        "rows": [
            {"label": "Инструмент", "text": "генеративная модель изображений"},
            {"label": "Результат", "text": "серия баннеров без фотосъёмки"},
            {"label": "Ограничения",
             "text": "иск об использовании образа художника"},
        ],
    },
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=24.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    R.check_razvilka("проба", d, w)
    R.draw_razvilka(s, "проба", d, mx, top, w)
    return s


def _run(meta, w=12.23):
    report.reset()
    d = R.razvilka_of(_sl(meta))
    if d:
        R.check_razvilka("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[развилка-чистая] {len(warns)} предупреждений на "
                   f"здоровом кадре: {warns[:2]}")
    else:
        say(f"{'[развилка-чистая]':<26} здоровый кадр: МОЛЧИТ  →  "
            f"«{d['da']['head']}» / «{d['net']['head']}»")
        ok.append("[развилка-чистая]")


def _copy(src):
    return {"vopros": src["vopros"],
            "da": {"head": src["da"]["head"], "image": "",
                  "rows": [dict(r) for r in src["da"]["rows"]]},
            "net": {"head": src["net"]["head"], "image": "",
                   "rows": [dict(r) for r in src["net"]["rows"]]}}


_PARSE_CASES = (
    ("нет vopros", "в `razvilka` нет `vopros`",
     lambda m: m.__setitem__("vopros", "")),
    ("нет net", "а должно быть image/head/rows",
     lambda m: m.__setitem__("net", None)),
    ("da не словарь", "а должно быть image/head/rows",
     lambda m: m.__setitem__("da", "строка")),
    ("чужой ключ ветки", "ядро не читает",
     lambda m: m["da"].__setitem__("цвет", "gold")),
    ("ветка без head", "нет `head`",
     lambda m: m["da"].__setitem__("head", "")),
    ("картинки нет на диске", "нет на диске",
     lambda m: m["da"].__setitem__("image", "assets/нет-такого-файла.png")),
    ("ветка без rows", "нет `rows`",
     lambda m: m["da"].__setitem__("rows", [])),
    ("строка не словарь", "а должна быть label/text",
     lambda m: m["da"]["rows"].insert(0, "строка")),
    ("чужой ключ строки", "ядро не читает",
     lambda m: m["da"]["rows"][0].__setitem__("цвет", "gold")),
    ("строка без label", "без `label`",
     lambda m: m["da"]["rows"][0].__setitem__("label", "")),
    ("строка без text", "без `text`",
     lambda m: m["net"]["rows"][0].__setitem__("text", "")),
    ("разный набор строк", "набор строк разный",
     lambda m: m["net"]["rows"][0].__setitem__("label", "Другое")),
    ("чужой ключ формы", "ядро не читает",
     lambda m: m.__setitem__("itog", "вывод")),
)


def probe_parse(ok, bad, say):
    report.reset()
    d0 = R.razvilka_of(types.SimpleNamespace(sid="проба",
                                             meta={"razvilka": ["строка"]}))
    hit0 = _hits(list(report.WARNINGS), "а должно быть vopros/da/net")
    if d0 is not None or not hit0:
        bad.append(f"[развилка/поле не словарь] не сработало; вышло: "
                   f"{report.WARNINGS}")
    else:
        say(f"{'[развилка]':<12} {'поле не словарь':<22} ЛОВИТ  →  "
            f"{hit0[0].split(': ', 1)[-1][:78]}…")
        ok.append("[развилка/поле не словарь]")

    for name, needle, mutate in _PARSE_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        d, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[развилка/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[развилка]':<12} {name:<22} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[развилка/{name}]")


_CHECK_CASES = (
    ("пятая строка", "строк 5 (>",
     lambda m: m["da"]["rows"].extend([
         {"label": "Четыре", "text": "текст"},
         {"label": "Пять", "text": "текст"}])),
    ("строка одна", "строка одна",
     lambda m: (m["da"].__setitem__("rows", m["da"]["rows"][:1]),
                m["net"].__setitem__("rows", m["net"]["rows"][:1]))),
    ("длинное слово", "не хватает ширины",
     lambda m: m["da"]["rows"][0].__setitem__(
         "text", "Сверхдлинноесловобезпробеловкотороенепоместитсявветку")),
)


# «Длинное слово» использует тесную ширину: на полной ширине кадра
# (12.23") каждой ветке достаётся ~6" — хватает места даже нарочито
# длинному слову, переполнение реально только на тесной ветке.
_TIGHT = {"длинное слово"}


def probe_broken(ok, bad, say):
    for name, needle, mutate in _CHECK_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta, w=3.0 if name in _TIGHT else 12.23)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[развилка/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[развилка]':<12} {name:<22} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[развилка/{name}]")


def probe_tight(ok, bad, say):
    """Тесная ветка — РАЗНОСТНАЯ проба: обычная ширина молчит, узкая —
    называет."""
    _, wide = _run(DEMO, w=12.23)
    _, nar = _run(DEMO, w=3.0)
    w_hit = _hits(wide, "ветка вышла")
    n_hit = _hits(nar, "ветка вышла")
    if w_hit or not n_hit:
        bad.append(f"[развилка-тесная] широкая {len(w_hit)}, узкая "
                   f"{len(n_hit)} — проба ловит не ширину")
        return
    say(f"{'[развилка-тесная]':<26} тесная ветка: ЛОВИТ  →  {n_hit[0][:100]}")
    ok.append("[развилка-тесная]")


def probe_height(ok, bad, say):
    report.reset()
    d = R.razvilka_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    w = SLIDE_W - 2 * 0.55
    promised = R.razvilka_h(d, w)
    drawn = R.draw_razvilka(s, "проба", d, 0.55, 1.46, w)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[развилка-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - 1.46:.3f}\"")
        return
    say(f"{'[развилка-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\"")
    ok.append("[развилка-мера]")


def build_demo(out=OUT):
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = R.razvilka_of(_sl(DEMO))
    demo_slide(p, d, "Развилка решения: два реальных случая")
    two = _copy(DEMO)
    two["da"]["rows"] = two["da"]["rows"][:2]
    two["net"]["rows"] = two["net"]["rows"][:2]
    demo_slide(p, R.razvilka_of(_sl(two)), "Две строки в каждой ветке")
    pptx = out / "razvilka.pptx"
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
