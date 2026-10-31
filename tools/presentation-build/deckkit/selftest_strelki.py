# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «СТРЕЛКИ»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Снимок нужен затем, что ни одна проверка пакета не знает, КАКОГО цвета
остриё стрелки и читается ли оно на острой грани
(`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_strelki [--render]
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import prims, render, report
from . import strelki as S
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "strelki"


def say(line):
    SAID.append(line)
    print(line)


def _sl(st, sid="проба"):
    return types.SimpleNamespace(sid=sid, meta={"strelki": st})


DEMO = {
    "vpravo": {"head": "Генерация", "text": "текст → шум → изображение"},
    "vlevo": {"head": "Распознавание",
             "text": "изображение → блоки внимания → оценка"},
    "itog": "та же архитектура внимания, развёрнутая в другую сторону",
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=24.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    S.check_strelki("проба", d, w)
    S.draw_strelki(s, "проба", d, mx, top, w)
    return s


def _run(meta, w=12.23):
    report.reset()
    d = S.strelki_of(_sl(meta))
    if d:
        S.check_strelki("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[стрелки-чистая] {len(warns)} предупреждений на "
                   f"здоровом кадре: {warns[:2]}")
    else:
        say(f"{'[стрелки-чистая]':<26} здоровый кадр: МОЛЧИТ  →  "
            f"«{d['vpravo']['head']}» / «{d['vlevo']['head']}»")
        ok.append("[стрелки-чистая]")


def _copy(src):
    return {"vpravo": dict(src["vpravo"]), "vlevo": dict(src["vlevo"]),
            "itog": src["itog"]}


_PARSE_CASES = (
    ("нет vlevo", "форма держит ровно две стрелки",
     lambda m: m.pop("vlevo")),
    ("vpravo не словарь", "а должно быть head/text",
     lambda m: m.__setitem__("vpravo", "просто строка")),
    ("чужой ключ стороны", "ядро не читает",
     lambda m: m["vpravo"].__setitem__("цвет", "gold")),
    ("vpravo без head", "нет `head`",
     lambda m: m["vpravo"].__setitem__("head", "")),
    ("vlevo без text", "нет `text`",
     lambda m: m["vlevo"].__setitem__("text", "")),
    ("чужой ключ формы", "ядро не читает",
     lambda m: m.__setitem__("most", "дальше")),
)


def probe_parse(ok, bad, say):
    report.reset()
    d0 = S.strelki_of(types.SimpleNamespace(sid="проба",
                                            meta={"strelki": ["строка"]}))
    hit0 = _hits(list(report.WARNINGS), "а должно быть vpravo/vlevo/itog")
    if d0 is not None or not hit0:
        bad.append(f"[стрелки/поле не словарь] не сработало; вышло: "
                   f"{report.WARNINGS}")
    else:
        say(f"{'[стрелки]':<12} {'поле не словарь':<22} ЛОВИТ  →  "
            f"{hit0[0].split(': ', 1)[-1][:78]}…")
        ok.append("[стрелки/поле не словарь]")

    for name, needle, mutate in _PARSE_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        d, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[стрелки/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[стрелки]':<12} {name:<22} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[стрелки/{name}]")


# Три пробы ниже требуют ТЕСНОЙ ширины (2.5"): при полной ширине кадра
# (12.23") текста внутри стрелки хватает места даже на нарочито длинный
# ввод — форма рисуется «во всю ширину кадра», и большинство реальных
# переполнений ловятся именно на тесном макете, не на полном.
_CHECK_CASES = (
    ("длинное слово", "не хватает ширины",
     lambda m: m["vpravo"].__setitem__(
         "head", "Сверхдлинноесловобезпробеловкотороенепоместитсявстрелку")),
    ("текст-абзац", "«vlevo» занимает",
     lambda m: m["vlevo"].__setitem__(
         "text", "это очень длинный текст хода стрелки, который растянется "
                 "на три строки и больше, потому что предел формы — две "
                 "строки, а не абзац целиком, и это видно сразу")),
    ("итог-абзац", "итог занимает",
     lambda m: m.__setitem__(
         "itog", "первая строка итога тянется вниз и вторая строка итога "
                 "тоже тянется вниз и третья строка итога добивает предел "
                 "в две строки и четвёртая строка точно переполняет его "
                 "совсем наверняка потому что текст очень длинный")),
)


def probe_broken(ok, bad, say):
    for name, needle, mutate in _CHECK_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta, w=2.5)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[стрелки/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[стрелки]':<12} {name:<22} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[стрелки/{name}]")


def probe_tight(ok, bad, say):
    """Тесная ширина — РАЗНОСТНАЯ проба: обычная ширина молчит, узкая —
    называет."""
    _, wide = _run(DEMO, w=12.23)
    _, nar = _run(DEMO, w=2.0)
    w_hit = _hits(wide, "ширина")
    n_hit = _hits(nar, "ширина")
    if w_hit or not n_hit:
        bad.append(f"[стрелки-тесная] широкая {len(w_hit)}, узкая "
                   f"{len(n_hit)} — проба ловит не ширину")
        return
    say(f"{'[стрелки-тесная]':<26} узкая стрелка: ЛОВИТ  →  {n_hit[0][:100]}")
    ok.append("[стрелки-тесная]")


def probe_gold(ok, bad, say):
    """Золото — ВСЕГДА на стрелке вправо, НИКОГДА на стрелке влево: форма
    держит ровно одну золотую фигуру на кадр."""
    report.reset()
    d = S.strelki_of(_sl(DEMO))
    p = prims.new_deck()
    demo_slide(p, d, "проба золота")
    if "проба" not in report.GOLD_SEEN:
        bad.append("[стрелки-золото] золота на кадре нет, а стрелка вправо "
                   "обязана быть золотой заливкой")
        return
    say(f"{'[стрелки-золото]':<26} стрелка вправо: ЗАЛИВКОЙ  →  золото на "
        "кадре отмечено (стрелка влево заливки не несёт)")
    ok.append("[стрелки-золото]")


def probe_height(ok, bad, say):
    report.reset()
    d = S.strelki_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    w = SLIDE_W - 2 * 0.55
    promised = S.strelki_h(d, w)
    drawn = S.draw_strelki(s, "проба", d, 0.55, 1.46, w)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[стрелки-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - 1.46:.3f}\"")
        return
    say(f"{'[стрелки-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\"")
    ok.append("[стрелки-мера]")


def build_demo(out=OUT):
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = S.strelki_of(_sl(DEMO))
    demo_slide(p, d, "Две встречные стрелки: генерация и распознавание")
    no_itog = _copy(DEMO)
    no_itog["itog"] = ""
    demo_slide(p, S.strelki_of(_sl(no_itog)), "Без итога — только две стрелки")
    pptx = out / "strelki.pptx"
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
