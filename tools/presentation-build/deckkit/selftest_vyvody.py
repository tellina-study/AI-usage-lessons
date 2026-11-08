# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «ВЫВОДЫ»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Единственное место пакета, где текст ставится ЗОЛОТОМ (цифра на тёмном
квадрате, см. шапку `vyvody.py`) — проверено отдельной разностной пробой,
а читается ли оно глазами на кадре — видит только глаз
(`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_vyvody [--render]
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import prims, render, report
from . import vyvody as V
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "vyvody"


def say(line):
    SAID.append(line)
    print(line)


def _sl(vv, sid="проба"):
    return types.SimpleNamespace(sid=sid, meta={"vyvody": vv})


DEMO = {
    "items": [
        {"head": "Платят за выбор, а не за исполнение",
         "text": "исполнение обесценилось, выбор — не бесплатен"},
        {"head": "Права переехали в отбор",
         "text": "лицензирование сместилось к моменту отбора результата"},
    ],
    "most": ("дальше по курсу: класс угроз, возникающий когда "
             "подтверждение подлинности перестаёт быть бесплатным"),
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=24.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    V.check_vyvody("проба", d, w)
    V.draw_vyvody(s, "проба", d, mx, top, w)
    return s


def _run(meta, w=12.23):
    report.reset()
    d = V.vyvody_of(_sl(meta))
    if d:
        V.check_vyvody("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[выводы-чистая] {len(warns)} предупреждений на "
                   f"здоровом кадре: {warns[:2]}")
    else:
        say(f"{'[выводы-чистая]':<26} здоровый кадр: МОЛЧИТ  →  выводов "
            f"{len(d['items'])}")
        ok.append("[выводы-чистая]")


def _copy(src):
    return {"items": [dict(it) for it in src["items"]], "most": src["most"]}


_PARSE_CASES = (
    ("нет items", "в `vyvody` нет `items`",
     lambda m: m.__setitem__("items", [])),
    ("вывод не словарь", "а должен быть head/text",
     lambda m: m["items"].insert(0, "строка")),
    ("чужой ключ вывода", "ядро не читает",
     lambda m: m["items"][0].__setitem__("цвет", "gold")),
    ("вывод без head", "нет `head`",
     lambda m: m["items"][0].__setitem__("head", "")),
    ("чужой ключ формы", "ядро не читает",
     lambda m: m.__setitem__("yarlyk", "итог")),
)


def probe_parse(ok, bad, say):
    report.reset()
    d0 = V.vyvody_of(types.SimpleNamespace(sid="проба",
                                           meta={"vyvody": ["строка"]}))
    hit0 = _hits(list(report.WARNINGS), "а должно быть items/most")
    if d0 is not None or not hit0:
        bad.append(f"[выводы/поле не словарь] не сработало; вышло: "
                   f"{report.WARNINGS}")
    else:
        say(f"{'[выводы]':<10} {'поле не словарь':<24} ЛОВИТ  →  "
            f"{hit0[0].split(': ', 1)[-1][:78]}…")
        ok.append("[выводы/поле не словарь]")

    for name, needle, mutate in _PARSE_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        d, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[выводы/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[выводы]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[выводы/{name}]")


_CHECK_CASES = (
    ("пятый вывод", "выводов 5 (>",
     lambda m: m["items"].extend([
         {"head": "Третий", "text": "текст"},
         {"head": "Четвёртый", "text": "текст"},
         {"head": "Пятый", "text": "текст"}])),
    ("вывод один", "вывод один",
     lambda m: m.__setitem__("items", m["items"][:1])),
    ("длинное слово", "не хватает ширины",
     lambda m: m["items"][0].__setitem__(
         "head", "Сверхдлинноесловобезпробеловкотороенепоместитсявкарточку")),
    ("пояснение-абзац", "пояснение занимает",
     lambda m: m["items"][0].__setitem__(
         "text", "это очень длинное пояснение растягивается на три строки "
                 "и больше, потому что предел пояснения — две строки, а не "
                 "абзац целиком, и это видно сразу любому читателю кадра")),
    ("мост-абзац", "мост к следующей лекции занимает",
     lambda m: m.__setitem__(
         "most", "первая строка моста тянется вниз и вторая строка моста "
                 "тоже тянется вниз и третья строка моста добивает предел "
                 "в две строки совсем наверняка и переполняет его дальше")),
)


# "Длинное слово" / "пояснение-абзац" / "мост-абзац" используют тесную
# ширину (2.2"): на полной ширине кадра (12.23") даже нарочито длинному
# вводу хватает места — форма держит мало текста и рисуется во всю колонку.
_TIGHT = {"длинное слово", "пояснение-абзац", "мост-абзац"}


def probe_broken(ok, bad, say):
    for name, needle, mutate in _CHECK_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta, w=2.2 if name in _TIGHT else 12.23)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[выводы/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[выводы]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[выводы/{name}]")


def probe_tight(ok, bad, say):
    _, wide = _run(DEMO, w=12.23)
    _, nar = _run(DEMO, w=2.0)
    w_hit = _hits(wide, "ширина")
    n_hit = _hits(nar, "ширина")
    if w_hit or not n_hit:
        bad.append(f"[выводы-тесная] широкая {len(w_hit)}, узкая "
                   f"{len(n_hit)} — проба ловит не ширину")
        return
    say(f"{'[выводы-тесная]':<26} узкая ширина: ЛОВИТ  →  {n_hit[0][:100]}")
    ok.append("[выводы-тесная]")


def probe_gold(ok, bad, say):
    """Золото — ВСЕГДА: цифра на каждой карточке и линия над мостом. Это
    единственная форма пакета, где нет условия «золота может не быть» —
    цифра рисуется для любого непустого `items`."""
    report.reset()
    d = V.vyvody_of(_sl(DEMO))
    p = prims.new_deck()
    demo_slide(p, d, "проба золота")
    if "проба" not in report.GOLD_SEEN:
        bad.append("[выводы-золото] золота на кадре нет, а цифра обязана "
                   "быть золотым текстом на тёмном квадрате")
        return
    say(f"{'[выводы-золото]':<26} цифра на тёмном: ТЕКСТОМ  →  единственное "
        "разрешённое место пакета (6,85 : 1, фон глубокий `#21295C`)")
    ok.append("[выводы-золото]")


def probe_height(ok, bad, say):
    report.reset()
    d = V.vyvody_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    w = SLIDE_W - 2 * 0.55
    promised = V.vyvody_h(d, w)
    drawn = V.draw_vyvody(s, "проба", d, 0.55, 1.46, w)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[выводы-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - 1.46:.3f}\"")
        return
    say(f"{'[выводы-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\"")
    ok.append("[выводы-мера]")


def build_demo(out=OUT):
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = V.vyvody_of(_sl(DEMO))
    demo_slide(p, d, "Нумерованные карточки закрытия")
    three = _copy(DEMO)
    three["items"].append({"head": "Узнавание стало спором о личности",
                           "text": "подтверждение подлинности — новая цена"})
    demo_slide(p, V.vyvody_of(_sl(three)), "Три вывода, без пояснений")
    pptx = out / "vyvody.pptx"
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
