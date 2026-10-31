# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «АРХИТЕКТУРА»: демонстрационный кадр и отказы.

Стандарт пакета: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА.
Поэтому здесь два рода прогонов, и оба обязательны:

1. ЧИСТЫЙ кадр — собирается, рендерится в PNG и ОБЯЗАН молчать. Снимок
   существует не для красоты: ни одна проверка пакета не знает, ЧТО кадр
   говорит, и золотую обводку узкого места, наезд строки и читаемость
   указателя видит только глаз (`notes/mcp-limitations.md` [#301-7]).
2. СЛОМАННЫЕ входы — по одному на КАЖДУЮ причину отказа из `check_arhitektura`
   и `arhitektura_of`. Каждый обязан дать своё предупреждение и обязан НЕ
   давать чужих.

Запуск:  python3 -m deckkit.selftest_arhitektura [--render]

Без `--render` идут только пробы (быстро, без LibreOffice). С `--render`
сверх них собирается демонстрационный кадр и снимается PNG — рендер всегда
по требованию, потому что `soffice` на деках этого курса дважды вешал машину
на часы (`notes/mcp-limitations.md` [#223-6], [#229-2]).
"""
import sys
import types
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR

from . import arhitektura as A
from . import prims, render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OK, BAD, SAID = [], [], []
OUT = Path(__file__).resolve().parents[1] / "probe-out" / "arhitektura"


def say(line):
    SAID.append(line)
    print(line)


def _sl(arh, sid="проба"):
    """Кадр в памяти: форме нужны только `sid` и фронтматтер. Поле кладётся
    ВНУТРЬ `meta` под своим именем, а не подсовывается вместо него, — иначе
    проба мерила бы разбор, которого в деке не происходит."""
    return types.SimpleNamespace(sid=sid, meta={"arhitektura": arh})


# ── демонстрационное содержание ─────────────────────────────────────
# Числа взяты из `PERENOS-PRIYOMOV.md` §2.11 как ОБРАЗЕЦ РАЗМЕТКИ, а не как
# утверждение этого кадра: демонстрационный кадр служебный, в деку лекции он
# не идёт и содержания собой не вводит.
DEMO = {
    "blocks": [
        {"head": "Текстовый кодировщик", "role": "вход",
         "lines": ["переводит слова в векторы",
                   "чужая замороженная модель, своей не учат"]},
        {"head": "Сеть расшумления", "role": "работа",
         "lines": ["от 1 до 50 проходов",
                   "работает в латентном пространстве, не с пикселями"]},
        {"head": "Автокодировщик", "role": "выход · узкое место",
         "uzkoe": True,
         "lines": ["изображение 1024×1024 сжимается в латент 128×128×16",
                   "восстановление на 4 каналах даёт 25,12 дБ против "
                   "28,62 на 16"]},
    ],
    "vynoska": {
        "at": 2,
        "text": "размытое декодировщиком ДО генерации не вернётся никогда — "
                "диффузионная сеть этот потолок не перешагнёт"},
}


def demo_slide(p, d, title, *, mx=0.55, top=1.46):
    """Один кадр с формой во всю колонку. Раскладка здесь самая скромная —
    заголовок и форма, — потому что проверяется ФОРМА, а не раскладка деки."""
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    prims.text_box(s, mx, 0.40, SLIDE_W - 2 * mx, 0.92, title, size=27.0,
                   bold=True, color=DEEP, anchor=MSO_ANCHOR.MIDDLE,
                   tag="проба/заголовок")
    w = SLIDE_W - 2 * mx
    A.check_arhitektura("проба", d, w)
    A.draw_arhitektura(s, "проба", d, mx, top, w)
    return s


# ── пробы ───────────────────────────────────────────────────────────


def _run(meta, w=12.23):
    """Разобрать и проверить кадр, вернуть предупреждения этого прогона."""
    report.reset()
    d = A.arhitektura_of(_sl(meta))
    if d:
        A.check_arhitektura("проба", d, w)
    return d, list(report.WARNINGS)


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe_clean(ok, bad, say):
    """ЧИСТЫЙ вход обязан молчать. Проба, у которой нет чистого прогона,
    доказывает только то, что сторож умеет говорить, — но не то, что он
    умеет молчать."""
    d, warns = _run(DEMO)
    if d is None or warns:
        bad.append(f"[архитектура-чистая] {len(warns)} предупреждений на "
                   f"здоровом кадре: {warns[:2]}")
    else:
        say(f"{'[архитектура-чистая]':<26} здоровый кадр: МОЛЧИТ  →  блоков "
            f"{len(d['blocks'])}, узких мест 1, выноска к блоку "
            f"{d['vynoska']['at']}")
        ok.append("[архитектура-чистая]")


_CASES = (
    # Кадр-образец несёт ТРИ блока, предел — четыре. Поэтому сломанный вход
    # добавляет ДВА: один добавленный встал бы ровно на предел и обязан был
    # бы пройти молча — то есть проба доказывала бы предел не тот.
    ("пятый блок", "блоков 5",
     lambda m: m["blocks"].extend(
         [{"head": "Планировщик шага", "role": "работа",
           "lines": ["решает, насколько сильно шуметь"]},
          {"head": "Ещё часть", "role": "хвост",
           "lines": ["пятая клетка в ряду"]}])),
    ("один блок", "блок один",
     lambda m: m.__setitem__("blocks", m["blocks"][:1])),
    ("два узких места", "узких мест объявлено 2",
     lambda m: m["blocks"][0].__setitem__("uzkoe", True)),
    ("блок без разбора", "нет `lines`",
     lambda m: m["blocks"][1].__setitem__("lines", [])),
    ("пятая строка разбора", "строк разбора 5",
     lambda m: m["blocks"][0].__setitem__(
         "lines", [f"строка разбора номер {i}" for i in range(1, 6)])),
    ("строка не влезла на полу", "не влезает и на",
     lambda m: m["blocks"][0]["lines"].append(
         "эта строка разбора нарочно длинная настолько, что не "
         "укладывается в три строки переноса даже на нижнем допустимом "
         "кегле видимого слоя, и потому обязана быть названа сторожем "
         "формы, а не ужата кеглем ниже пола")),
    ("разорванное слово", "будет разорвано переносом",
     lambda m: m["blocks"][0]["lines"].append(
         "сверхдлинноесловобезпробеловкотороешире бокса")),
    ("ярлык роли фразой", "ярлык это одно-два слова",
     lambda m: m["blocks"][0].__setitem__(
         "role", "вход, он же место, где текст превращается в числа")),
    ("выноска в никуда", "указывает на блок 7",
     lambda m: m["vynoska"].__setitem__("at", 7)),
    ("ключ, который не читают", "ядро не читает",
     lambda m: m["blocks"][0].__setitem__("color", "gold")),
    ("блок без имени", "нет `head`",
     lambda m: m["blocks"][1].__setitem__("head", "")),
)


def _copy(src):
    return {"blocks": [dict(b, lines=list(b["lines"]))
                       for b in src["blocks"]],
            "vynoska": dict(src["vynoska"])}


def probe_broken(ok, bad, say):
    """По одному сломанному входу на каждую причину отказа."""
    for name, needle, mutate in _CASES:
        meta = _copy(DEMO)
        mutate(meta)
        _, warns = _run(meta)
        hit = _hits(warns, needle)
        if not hit:
            bad.append(f"[архитектура/{name}] не сработало; вышло: {warns}")
            continue
        say(f"{'[архитектура]':<26} {name:<26} ЛОВИТ  →  "
            f"{hit[0].split(': ', 1)[-1][:72]}…")
        ok.append(f"[архитектура/{name}]")


def probe_tight(ok, bad, say):
    """ТЕСНЫЙ БОКС — проба РАЗНОСТНАЯ: мало знать, что сторож сработал, надо
    знать, ОТ ЧЕГО. Тот же кадр меряется во всю колонку и в узкую: на
    широкой обязан молчать, на узкой — назвать ширину бокса."""
    report.reset()
    d = A.arhitektura_of(_sl(DEMO))
    A.check_arhitektura("проба", d, 12.23)
    wide = _hits(list(report.WARNINGS), "бокс вышел")
    report.reset()
    A.check_arhitektura("проба", d, 4.60)
    nar = _hits(list(report.WARNINGS), "бокс вышел")
    if wide or not nar:
        bad.append(f"[архитектура-тесный] широкая {len(wide)}, узкая "
                   f"{len(nar)} — проба ловит не ширину")
        return
    say(f"{'[архитектура-тесный]':<26} тесный бокс: ЛОВИТ  →  во всю колонку "
        f"{A._box_w(d, 12.23, A.DEFAULT):.2f}\" молчит, в узкой "
        f"{A._box_w(d, 4.60, A.DEFAULT):.2f}\" говорит")
    ok.append("[архитектура-тесный]")


def probe_gold(ok, bad, say):
    """Золото на кадре есть — и приходит ЗАЛИВКОЙ ярлыка, а не текстом.

    Разностно: тот же кадр без `uzkoe` обязан золота не дать. Иначе проба
    доказывала бы только то, что кадр вообще чем-то залит."""
    for flag, want in ((True, True), (False, False)):
        meta = _copy(DEMO)
        meta["blocks"][2]["uzkoe"] = flag
        report.reset()
        d = A.arhitektura_of(_sl(meta))
        p = prims.new_deck()
        demo_slide(p, d, "проба золота")
        got = "проба" in report.GOLD_SEEN
        if got is not want:
            bad.append(f"[архитектура-золото] uzkoe={flag}: золото "
                       f"{'есть' if got else 'нет'}, ждали обратного")
            return
    say(f"{'[архитектура-золото]':<26} узкое место: ЗАЛИВКОЙ  →  с `uzkoe` "
        "золото на кадре есть, без него — нет; золотого ТЕКСТА форма не "
        "ставит нигде (1,99 : 1 при пороге 3,0)")
    ok.append("[архитектура-золото]")


def probe_height(ok, bad, say):
    """Мера совпадает с рисованием: `arhitektura_h` обещает высоту ДО того,
    как нарисована хоть одна фигура, и `draw_arhitektura` обязан вернуть
    ровно её. Две формулы одного числа расходятся на первой правке."""
    report.reset()
    d = A.arhitektura_of(_sl(DEMO))
    p = prims.new_deck()
    s = prims.blank(p)
    promised = A.arhitektura_h(d, 12.23)
    drawn = A.draw_arhitektura(s, "проба", d, 0.55, 1.46, 12.23)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > 1.46 + promised + 0.02:
        bad.append(f"[архитектура-мера] обещано {promised:.3f}\", "
                   f"нарисовано {drawn:.3f}\", низ фигур "
                   f"{bottom - 1.46:.3f}\"")
        return
    say(f"{'[архитектура-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - 1.46:.3f}\" (ни одна фигура "
        "не вышла за обещанное)")
    ok.append("[архитектура-мера]")


def build_demo(out=OUT):
    """Демонстрационный кадр: чистый, сломанный по ширине и без выноски.

    Три кадра, а не один: глаз сверяет форму с собой же в других условиях —
    узкая колонка показывает, как держится разбор, кадр без выноски — что
    форма без неё не разваливается."""
    out.mkdir(parents=True, exist_ok=True)
    report.reset()
    p = prims.new_deck()
    d = A.arhitektura_of(_sl(DEMO))
    demo_slide(p, d, "Устройство модели: три части и узкое место")
    two = _copy(DEMO)
    two["blocks"] = two["blocks"][1:]
    two["vynoska"]["at"] = 1
    demo_slide(p, A.arhitektura_of(_sl(two)), "Две части, колонка та же")
    four = _copy(DEMO)
    four["blocks"].insert(2, {"head": "Планировщик шага", "role": "работа",
                              "lines": ["решает, насколько сильно шуметь",
                                        "от него зависит число проходов"]})
    four.pop("vynoska")
    demo_slide(p, A.arhitektura_of(_sl(four)),
               "Четыре части, выноски нет — предел ряда")
    pptx = out / "arhitektura.pptx"
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
