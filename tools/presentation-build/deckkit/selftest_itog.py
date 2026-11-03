# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА НИЖНЕЙ ПЛАШКИ-ВЫВОДА: демонстрационный кадр и прогон КАЖДОГО
отказа, какой `itog.py` умеет заявить (их семь, и это весь список).

Стандарт пакета один: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ
ПРОВЕРКА. Сломанные входы (`ITOG_BAD`) и демонстрационная разметка
(`ITOG_CLEAN`, `ITOG_TWO`) взяты из `probes_formy.py` — они собирались
вместе с таймлайном и пиктограммами в той же нити.

Сверх прогонов — СОБРАННЫЙ КАДР. Половина того, что отличает вывод от
абзаца, глазами мерится, а не координатами: золотой ли ЗАЛИВКОЙ ярлык (а не
текстом — 1,99 : 1 при пороге 3,0 золотым текстом на белом), крупнее ли
строка вывода, чем тело рядом с ней (`notes/mcp-limitations.md` [#301-7]).

Запуск:  python3 -m deckkit.selftest_itog          (сборка + прогоны)
         python3 -m deckkit.selftest_itog --render  (ещё и снимки PNG)
"""
import sys
from pathlib import Path

from . import itog, metrics, prims, probes_formy as PF, render, report
from .theme import DEEP, SLIDE_H, SLIDE_W, WHITE

OUT = Path(__file__).resolve().parents[1] / "probe-out" / "itog"
MX, TOP, FOOT = 0.55, 1.46, 6.94
FULL_W = SLIDE_W - 2 * MX
BODY_PT = 15.0           # номинал тела этой пробы — тот же, что у Лекции 7

OK, BAD = [], []


def say(line):
    print(line)


def frame(p, title, raw, note):
    """Кадр с полосой-телом (несколько строк на номинале BODY_PT) и
    плашкой-выводом внизу. Тело нужно, чтобы проверить «крупнее тела» не
    на голой цифре, а на настоящем соседнем кегле."""
    d = itog.itog_of("проба", raw)
    itog.check_itog("проба", d, FULL_W)
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    sz = metrics.fit_size(title, FULL_W, 0.92, hi=27.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 0.40, FULL_W, 0.92, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 1.50, FULL_W, 3.8, note, size=BODY_PT,
                   color=DEEP, ls=1.30, tag="проба/тело")
    st = itog.style_for(BODY_PT)
    h = itog.itog_h(d, FULL_W, st)
    y = itog.itog_y(FOOT, d, FULL_W, st)
    got = itog.draw_itog(s, "проба", d, MX, y, FULL_W, st)
    if abs(got - h) > 0.02:
        BAD.append(f"[итог-мера] мера обещала {h:.3f}\", рисунок занял "
                   f"{got:.3f}\" — две формулы одного числа")
    if abs((y + got) - FOOT) > 0.02:
        BAD.append(f"[итог-мера] полоса прижата к подвалу неверно: низ "
                   f"{y + got:.3f}\" при подвале {FOOT:.3f}\"")
    return d, st


def build(path):
    report.reset()
    p = prims.new_deck()
    frame(p, "Что переехало: от стены прозы к одной строке",
          PF.ITOG_CLEAN,
          "Служебное тело пробы: три-четыре строки разбора на номинале "
          "деки, под которыми стоит полоса вывода. Форма заведена забрать "
          "у кадра именно такую стену — \"Итог: …\", \"Вывод: …\" — и "
          "оставить одну фразу крупнее тела.")
    frame(p, "Вторая проба: более длинный вывод, тот же номинал тела",
          PF.ITOG_TWO,
          "Второе служебное тело той же пробы, короче первого — чтобы "
          "видно было, что форма не зависит от объёма тела над ней.")
    p.save(str(path))
    w = list(report.WARNINGS)
    report.reset()
    return w


# ── прогоны отказов ─────────────────────────────────────────────────


def run(raw, w=FULL_W):
    report.reset()
    d = itog.itog_of("проба", raw)
    if d is not None:
        itog.check_itog("проба", d, w)
    out = list(report.WARNINGS)
    report.reset()
    return d, out


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe(name, raw, needle, w=FULL_W):
    _, clean = run(PF.ITOG_CLEAN)
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
    "не-словарь": ("[итог] не словарь", "должно быть"),
    "нет-текста": ("[итог] нет текста", "нечего вывести"),
    "ключ": ("[итог] ключ", "форма не читает"),
    "нет-ярлыка": ("[итог] нет ярлыка", "ЯРЛЫК"),
    "длинный-ярлык": ("[итог] длинный ярлык", "знаков"),
    "ярлык-фраза": ("[итог] ярлык-фраза", "слова"),
    "третья-строка": ("[итог] третья строка", "строки (>"),
}


def probes():
    _, got = run(PF.ITOG_CLEAN)
    if got:
        BAD.append(f"[чисто-1] чистый вход дал {len(got)} "
                   f"предупреждений: {got}")
    else:
        OK.append("чисто-1")
        say(f"{'[чисто-1]':<26} МОЛЧИТ на чистом входе")
    _, got = run(PF.ITOG_TWO)
    if got:
        BAD.append(f"[чисто-2] чистый вход дал {len(got)} "
                   f"предупреждений: {got}")
    else:
        OK.append("чисто-2")
        say(f"{'[чисто-2]':<26} МОЛЧИТ на чистом входе")

    for name, (key, needle) in NEEDLES.items():
        probe(name, PF.ITOG_BAD[key], needle)

    missing = set(PF.ITOG_BAD) - {k for k, _n in NEEDLES.values()}
    if missing:
        BAD.append(f"[итог-полнота] в ITOG_BAD есть вход(ы), на которые "
                   f"нет пробы: {sorted(missing)}")


# ── мера, золото-как-заливка, кегль крупнее тела ────────────────────


def probe_gold_is_fill_not_text():
    """Золото стоит на ярлыке ЗАЛИВКОЙ фигуры, а не цветом букв. Проверка
    идёт по самому XML: у прогона текста ярлыка цвет обязан быть DEEP, а
    не GOLD — иначе это и была бы та самая 1,99 : 1 ошибка, из-за которой
    форма переведена."""
    report.reset()
    d = itog.itog_of("проба", PF.ITOG_CLEAN)
    p = prims.new_deck()
    s = prims.blank(p)
    itog.draw_itog(s, "проба-золото", d, MX, TOP, FULL_W)
    if "проба-золото" not in report.GOLD_SEEN:
        BAD.append("[итог-золото] золота на кадре нет вовсе")
        return
    chip_shapes = [sh for sh in s.shapes
                  if sh.has_text_frame and sh.text_frame.text == d["yarlyk"]]
    if not chip_shapes:
        BAD.append("[итог-золото] ярлык не найден как фигура на кадре")
        return
    shp = chip_shapes[0]
    fill_rgb = shp.fill.fore_color.rgb
    run_color = shp.text_frame.paragraphs[0].runs[0].font.color.rgb
    from .theme import DEEP as _DEEP, GOLD as _GOLD
    if fill_rgb != _GOLD or run_color == _GOLD or run_color != _DEEP:
        BAD.append(f"[итог-золото] заливка {fill_rgb}, текст {run_color} "
                   "— ожидали заливку GOLD и текст DEEP")
        return
    say(f"{'[итог-золото]':<26} ЗАЛИВКОЙ  →  заливка {fill_rgb}, текст "
        f"{run_color} — золотого текста нет")
    OK.append("итог-золото")


def probe_size_bigger_than_body():
    """Кегль вывода обязан быть крупнее номинала тела — ступенью, а не
    волей случая. Проверяется на ДВУХ номиналах (15 и 13 пт), чтобы
    убедиться, что ступень считается от номинала деки, а не зашита
    числом 17."""
    for base in (15.0, 13.0):
        st = itog.style_for(base)
        if not (st.text_pt > base):
            BAD.append(f"[итог-кегль/{base}] вывод {st.text_pt} пт не "
                       f"крупнее тела {base} пт")
            continue
        say(f"{'[итог-кегль/' + str(base) + ']':<26} вывод {st.text_pt} "
            f"пт > тело {base} пт")
        OK.append(f"итог-кегль/{base}")


def probe_pinned_to_bottom():
    """`itog_y` прижимает полосу НИЗОМ к заданной границе — верх
    вычисляется из высоты, а не наоборот. Два вывода разной длины на
    одной нижней границе обязаны давать РАЗНЫЙ верх и ОДИН и тот же низ."""
    d1 = itog.itog_of("проба", PF.ITOG_CLEAN)
    d2 = itog.itog_of("проба", PF.ITOG_TWO)
    y1 = itog.itog_y(FOOT, d1, FULL_W)
    y2 = itog.itog_y(FOOT, d2, FULL_W)
    h1 = itog.itog_h(d1, FULL_W)
    h2 = itog.itog_h(d2, FULL_W)
    if abs((y1 + h1) - FOOT) > 1e-6 or abs((y2 + h2) - FOOT) > 1e-6:
        BAD.append(f"[итог-низ] низ не совпал с границей: "
                   f"{y1 + h1:.3f}\" / {y2 + h2:.3f}\" при {FOOT:.3f}\"")
        return
    if abs(y1 - y2) < 1e-6:
        BAD.append("[итог-низ] разные по длине выводы дали один и тот же "
                   "верх — проба ничего не доказывает")
        return
    say(f"{'[итог-низ]':<26} разностно: ЛОВИТ  →  верх {y1:.3f}\" vs "
        f"{y2:.3f}\", низ у обеих {FOOT:.3f}\"")
    OK.append("итог-низ")


def main(argv=()):
    OUT.mkdir(parents=True, exist_ok=True)
    pptx = OUT / "proba-itog.pptx"
    warns = build(pptx)
    if warns:
        BAD.append(f"[сборка] демонстрационные кадры дали {len(warns)} "
                   f"предупреждений: {warns}")
    else:
        OK.append("сборка")
        say(f"{'[сборка]':<26} два кадра собраны чисто  →  {pptx}")
    probes()
    probe_gold_is_fill_not_text()
    probe_size_bigger_than_body()
    probe_pinned_to_bottom()
    if "--render" in argv:
        if render.render(pptx, OUT / "snaps"):
            BAD.append("[рендер] PDF или снимки не собрались")
    print(f"\nпрошло {len(OK)} · не прошло {len(BAD)}")
    for b in BAD:
        print("  " + b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
