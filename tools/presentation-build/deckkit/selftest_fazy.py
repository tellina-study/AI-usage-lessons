# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «ФАЗЫ»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Два рода прогонов:

1. ЧИСТЫЙ кадр — собирается, рендерится в PNG и ОБЯЗАН молчать. Золотую
   клетку, скобку и связку с итогом видит только глаз
   (`notes/mcp-limitations.md` [#301-7]).
2. СЛОМАННЫЕ входы — по одному на КАЖДУЮ причину отказа `check_fazy` и
   `fazy_of`. Каждый обязан дать своё предупреждение и обязан НЕ давать
   чужих.

Запуск:  python3 -m deckkit.selftest_fazy [--render]
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import fazy as F
from . import prims, render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "fazy"


def say(line):
    SAID.append(line)
    print(line)


def _sl(fz, sid="проба"):
    return types.SimpleNamespace(sid=sid, meta={"fazy": fz})


# Содержание — служебное, в деку лекции не идёт (цепочка 3D-продакшна —
# тот же пример, что в `PERENOS-PRIYOMOV.md` §2.7, слова укорочены, чтобы
# клетка на этой ширине держала перенос — демонстрация формы, не кадр).
DEMO = {
    "groups": [
        {"head": "Поиск облика", "steps": ["Блокинг", "Набросок текстур"],
         "model_in": [0]},
        {"head": "Подготовка", "steps": ["Ретопология", "Риггинг"]},
        {"head": "Использование", "steps": ["Анимация", "Рендер"]},
    ],
    "itog": "людям остаются самые дорогие инженерные стадии",
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=24.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    F.check_fazy("проба", d, w)
    F.draw_fazy(s, "проба", d, mx, top, w)
    return s


def _run(meta, w=12.23):
    report.reset()
    d = F.fazy_of(_sl(meta))
    if d:
        F.check_fazy("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[фазы-чистая] {len(warns)} предупреждений на здоровом "
                   f"кадре: {warns[:2]}")
    else:
        say(f"{'[фазы-чистая]':<26} здоровый кадр: МОЛЧИТ  →  фаз "
            f"{len(d['groups'])}, шагов "
            f"{sum(len(g['steps']) for g in d['groups'])}")
        ok.append("[фазы-чистая]")


def _copy(src):
    """Копия НЕРАЗОБРАННОГО поля — `model_in` остаётся списком, каким его
    пишут во фронтматтере, а не множеством, в которое его превращает
    `fazy_of`: копия идёт обратно В `fazy_of`, и set на входе сам по себе
    уже отказ («а должен быть список»), который замаскировал бы пробу."""
    return {"groups": [dict(g, steps=list(g["steps"]),
                            model_in=list(g.get("model_in") or []))
                       for g in src["groups"]],
            "itog": src["itog"]}


_PARSE_CASES = (
    ("нет groups", "в `fazy` нет `groups`",
     lambda m: m.__setitem__("groups", [])),
    ("фаза не словарь", "не head/steps/model_in",
     lambda m: m["groups"].insert(0, "фаза строкой")),
    ("чужой ключ фазы", "ядро не читает",
     lambda m: m["groups"][0].__setitem__("цвет", "gold")),
    ("фаза без head", "нет `head`",
     lambda m: m["groups"][0].__setitem__("head", "")),
    ("фаза без steps", "нет `steps`",
     lambda m: m["groups"][0].__setitem__("steps", [])),
    ("model_in не список", "а должен быть список",
     lambda m: m["groups"][0].__setitem__("model_in", "0")),
    ("model_in не число", "не целое число шага",
     lambda m: m["groups"][0].__setitem__("model_in", ["первый"])),
    ("model_in мимо клетки", "уйдёт мимо клетки",
     lambda m: m["groups"][0].__setitem__("model_in", [9])),
)


def probe_parse(ok, bad, say):
    # Поле целиком не словарь — отдельно: мутация таблицы ниже работает
    # над КОПИЕЙ словаря DEMO, а это тот случай, где словаря нет вовсе.
    report.reset()
    d0 = F.fazy_of(types.SimpleNamespace(sid="проба",
                                         meta={"fazy": ["строка"]}))
    hit0 = _hits(list(report.WARNINGS), "а должно быть groups/itog")
    if d0 is not None or not hit0:
        bad.append(f"[фазы/поле не словарь] не сработало; "
                   f"вышло: {report.WARNINGS}")
    else:
        say(f"{'[фазы]':<10} {'поле не словарь':<24} ЛОВИТ  →  "
            f"{hit0[0].split(': ', 1)[-1][:78]}…")
        ok.append("[фазы/поле не словарь]")

    for name, needle, mutate in _PARSE_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        d2, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[фазы/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[фазы]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[фазы/{name}]")


_CHECK_CASES = (
    ("пятая фаза", "фаз 5 (>",
     lambda m: m["groups"].extend([
         {"head": "Четвёртая", "steps": ["А", "Б"], "model_in": set()},
         {"head": "Пятая", "steps": ["В", "Г"], "model_in": set()}])),
    ("одна фаза", "фаза одна",
     lambda m: m.__setitem__("groups", m["groups"][:1])),
    ("пятый шаг фазы", "шагов 5 (>",
     lambda m: m["groups"][1].__setitem__(
         "steps", ["Ретопология", "Развёртка", "Риггинг",
                  "Текстурирование", "Шейдинг"])),
    ("один шаг фазы", "шаг один",
     lambda m: m["groups"][1].__setitem__("steps", ["Ретопология"])),
    ("длинное слово в клетке", "будет разорвано переносом",
     lambda m: m["groups"][0].__setitem__(
         "steps", ["Сверхдлинноесловобезпробеловкотороешире клетки",
                   "Набросок текстур"])),
    ("строка не влезает", "не влезает и на",
     lambda m: m["groups"][0].__setitem__(
         "steps", ["Очень длинная строка разбора которая не влезает в "
                   "клетку ни при каком разумном кегле точно совсем",
                   "Набросок текстур"])),
    ("длинная подпись фазы", "не влезает в ширину скобки",
     lambda m: m["groups"][0].__setitem__(
         "head", "Очень длинная подпись фазы, которая не влезает в "
                 "скобку этой ширины ни при каком разумном кегле")),
    ("итог-абзац", "итог занимает",
     lambda m: m.__setitem__(
         "itog", "первая строка итога тянется вниз и вторая строка итога "
                 "тоже тянется вниз и третья строка итога добивает предел "
                 "в две строки совсем наверняка")),
)


def probe_broken(ok, bad, say):
    for name, needle, mutate in _CHECK_CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[фазы/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[фазы]':<10} {name:<24} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:78]}…")
        ok.append(f"[фазы/{name}]")


def probe_tight(ok, bad, say):
    """Тесная клетка — РАЗНОСТНАЯ проба: тот же кадр на обычной ширине
    молчит про клетку, на узкой — называет."""
    _, wide = _run(DEMO, w=12.23)
    _, nar = _run(DEMO, w=3.0)
    w_hit = _hits(wide, "клетка вышла")
    n_hit = _hits(nar, "клетка вышла")
    if w_hit or not n_hit:
        bad.append(f"[фазы-тесная] широкая {len(w_hit)}, узкая {len(n_hit)} "
                   "— проба ловит не ширину")
        return
    say(f"{'[фазы-тесная]':<26} тесная клетка: ЛОВИТ  →  {n_hit[0][:100]}")
    ok.append("[фазы-тесная]")


def probe_gold(ok, bad, say):
    """Золото — ЗАЛИВКОЙ клетки `model_in`, и только её. Разностно: та же
    фаза без `model_in` золота не даёт."""
    for has, want in ((True, True), (False, False)):
        meta = _copy(DEMO)
        if not has:
            meta["groups"][0]["model_in"] = set()
        report.reset()
        d = F.fazy_of(_sl(meta))
        p = prims.new_deck()
        demo_slide(p, d, "проба золота")
        got = "проба" in report.GOLD_SEEN
        if got is not want:
            bad.append(f"[фазы-золото] model_in={has}: золото "
                       f"{'есть' if got else 'нет'}, ждали обратного")
            return
    say(f"{'[фазы-золото]':<26} клетка `model_in`: ЗАЛИВКОЙ  →  с "
        "`model_in` золото на кадре есть, без него — нет")
    ok.append("[фазы-золото]")


def probe_height(ok, bad, say):
    """Мера совпадает с рисованием: `fazy_h` обещает высоту ДО того, как
    нарисована хоть одна фигура, `draw_fazy` обязан вернуть ровно её."""
    report.reset()
    d = F.fazy_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    w = SLIDE_W - 2 * 0.55
    promised = F.fazy_h(d, w)
    drawn = F.draw_fazy(s, "проба", d, 0.55, 1.46, w)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[фазы-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - 1.46:.3f}\"")
        return
    say(f"{'[фазы-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\"")
    ok.append("[фазы-мера]")


def build_demo(out=OUT):
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = F.fazy_of(_sl(DEMO))
    demo_slide(p, d, "Конвейер со скобками фаз: где вошла модель")
    two = _copy(DEMO)
    two["groups"] = two["groups"][:2]
    demo_slide(p, F.fazy_of(_sl(two)), "Две фазы, без третьей")
    no_itog = _copy(DEMO)
    no_itog["itog"] = ""
    demo_slide(p, F.fazy_of(_sl(no_itog)), "Без итога — конвейер без связки")
    pptx = out / "fazy.pptx"
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
