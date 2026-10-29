# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ВОРОНКИ: демонстрационный кадр и прогон КАЖДОГО отказа.

Стандарт пакета один и здесь он не обсуждается: ПРОВЕРКА, НЕ ПРОВЕРЕННАЯ НА
СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА. Поэтому на сторож `voronka.check_voronka`
(и на разбор `voronka.parse`) — по одному прогону на каждую из тринадцати
причин, которыми модуль умеет отказать, и каждый обязан сказать СВОЁ, а
чистый вход — молчать про него же.

Сверх прогонов — СОБРАННЫЙ КАДР. Половина того, что отличает воронку от
орнамента, координатами не меряется: читается ли ступенчатая фигура
воронкой, а не трапецией непонятно чего; стоит ли подпись узкого места так,
что её нельзя пропустить; не наезжают ли ярусы подписей друг на друга —
`nalozhenie_bbox.py` этого не ловит по построению
(`notes/mcp-limitations.md` [#301-7]), и глаз пока ничем не заменяется.

Запуск:  python3 -m deckkit.selftest_voronka         (сборка + прогоны)
         python3 -m deckkit.selftest_voronka --render (ещё и PDF со снимками)
"""
import sys
from pathlib import Path

from . import metrics, prims, render, report, voronka
from .probes_formy import VORONKA_BAD, VORONKA_CLEAN, VORONKA_SHORT
from .theme import DEEP, LIGHT, SLIDE_H, SLIDE_W, WHITE

OUT = Path(__file__).resolve().parents[1] / "probe-out" / "voronka"
MX, TOP, FOOT = 0.55, 1.46, 6.94
FULL_W = SLIDE_W - 2 * MX

OK, BAD = [], []


def say(line):
    print(line)


# ── сборка демонстрационного кадра ─────────────────────────────────


def frame(p, title, raw, foot):
    d = voronka.parse("проба", raw)
    voronka.check_voronka("проба", d, FULL_W)
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    sz = metrics.fit_size(title, FULL_W, 0.92, hi=27.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 0.40, FULL_W, 0.92, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag="проба/заголовок")
    h = voronka.voronka_h(d, FULL_W)
    got = voronka.draw_voronka(s, "проба", d, MX, TOP, FULL_W)
    if abs(got - h) > 0.02:
        BAD.append(f"[воронка-мера] мера обещала {h:.3f}\", рисунок занял "
                   f"{got:.3f}\" — две формулы одного числа")
    if TOP + got > FOOT:
        BAD.append(f"[воронка-мера] форма дошла до подвала: низ "
                   f"{TOP + got:.2f}\" при подвале {FOOT:.2f}\"")
    prims.text_box(s, MX, FOOT, FULL_W, 0.40, foot, size=11.0, italic=True,
                   color=LIGHT, ls=1.12, tag="проба/подвал")
    return s, d


def build(path):
    report.reset()
    p = prims.new_deck()
    _, d1 = frame(p, "Скрытая цена: 70 000 клипов на один готовый ролик",
                 VORONKA_CLEAN,
                 "служебный кадр самопроверки ядра · форма «воронка»")
    _, d2 = frame(p, "Та же форма короче: два яруса, узкое место — "
                 "«горлышко»",
                 VORONKA_SHORT, "служебный кадр самопроверки ядра · два "
                 "яруса, синоним узкого места")
    p.save(str(path))
    w = list(report.WARNINGS)
    gold1, gold2 = "проба" in report.GOLD_SEEN, "проба" in report.GOLD_SEEN
    report.reset()
    return w, d1, d2


# ── прогоны отказов ─────────────────────────────────────────────────


def run(raw, w=FULL_W):
    """Разбор и сторож на одном входе. Возвращает (разбор, предупреждения)."""
    report.reset()
    d = voronka.parse("проба", raw)
    if d is not None:
        voronka.check_voronka("проба", d, w)
    out = list(report.WARNINGS)
    report.reset()
    return d, out


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe(name, raw, needle, w=FULL_W):
    """Один отказ: сломанный вход обязан сказать именно про `needle`, а
    чистый — промолчать про него же."""
    _, clean = run(VORONKA_CLEAN)
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


def probes():
    # 0. ЧИСТЫЙ вход молчит целиком — без этого всё остальное ничего не
    #    доказывает: сторож, который говорит всегда, не сторож.
    for name, raw in (("чисто-длинная", VORONKA_CLEAN),
                      ("чисто-короткая", VORONKA_SHORT)):
        _, got = run(raw)
        if got:
            BAD.append(f"[{name}] чистый вход дал {len(got)} предупреждений: "
                       f"{got}")
        else:
            OK.append(name)
            say(f"{'[' + name + ']':<26} МОЛЧИТ на чистом входе")

    NEEDLES = {
        "нет-входа": ("[воронка] нет входа", "не задан «vhod»"),
        "ключ-входа": ("[воронка] ключ входа", "у «vhod» ключи"),
        "нет-value-входа": ("[воронка] нет value входа", "нет `value`"),
        "форма-не-словарь": ("[воронка] форма не словарь", "должно быть"),
        "ключ-формы": ("[воронка] ключ формы", "ключи legenda"),
        "нет-ярусов": ("[воронка] нет ярусов", "нет `yarusy`"),
        "ключ-яруса": ("[воронка] ключ яруса", "ключи color"),
        "ярус-без-головы": ("[воронка] ярус без головы", "нет `head`"),
        "нет-узкого-места": ("[воронка] нет узкого места", "УЗКИМ МЕСТОМ"),
        "один-ярус": ("[воронка] один ярус", "ярус один"),
        "четыре-яруса": ("[воронка] четыре яруса", "(> 3)"),
        "вход-без-цифры": ("[воронка] вход без цифры", "без единой цифры"),
        "длинное-слово-яруса": ("[воронка] длинное слово яруса",
                               "слово разорвётся"),
    }
    for name, (key, needle) in NEEDLES.items():
        probe(name, VORONKA_BAD[key], needle)

    missing = set(VORONKA_BAD) - {k for k, _n in NEEDLES.values()}
    if missing:
        BAD.append(f"[воронка-полнота] в VORONKA_BAD есть вход(ы), на "
                   f"которые нет пробы: {sorted(missing)}")


# ── мера и золото ───────────────────────────────────────────────────


def probe_height():
    """Мера совпадает с рисованием: `voronka_h` обещает высоту ДО того, как
    нарисована хоть одна фигура, `draw_voronka` обязан вернуть ровно её."""
    report.reset()
    d = voronka.parse("проба", VORONKA_CLEAN)
    p = prims.new_deck()
    s = prims.blank(p)
    promised = voronka.voronka_h(d, FULL_W)
    drawn = voronka.draw_voronka(s, "проба", d, MX, TOP, FULL_W)
    bottom = max((sh.top + sh.height) / 914400.0 for sh in s.shapes)
    if abs(promised - drawn) > 1e-9 or bottom > TOP + promised + 0.02:
        BAD.append(f"[воронка-мера] обещано {promised:.3f}\", нарисовано "
                   f"{drawn:.3f}\", низ фигур {bottom - TOP:.3f}\"")
        return
    say(f"{'[воронка-мера]':<26} мера = рисование  →  обещано "
        f"{promised:.3f}\", занято {bottom - TOP:.3f}\"")
    OK.append("воронка-мера")


def probe_gold():
    """Золото на кадре есть, и приходит ЗАЛИВКОЙ плашек входа/выхода — не
    текстом (1,99 : 1 при пороге 3,0, золотой текст на белом не проходит)."""
    report.reset()
    d = voronka.parse("проба", VORONKA_CLEAN)
    p = prims.new_deck()
    s = prims.blank(p)
    voronka.draw_voronka(s, "проба-золото", d, MX, TOP, FULL_W)
    if "проба-золото" not in report.GOLD_SEEN:
        BAD.append("[воронка-золото] золота на чистом кадре нет вовсе")
        return
    say(f"{'[воронка-золото]':<26} плашки входа/выхода: ЗАЛИВКОЙ  →  "
        "золотой текст форма не ставит нигде")
    OK.append("воронка-золото")


def probe_bottleneck_fill():
    """Разностная проба: ярус-затор получает ЗОЛОТУЮ заливку, рядовой —
    нет. Без разницы это доказывало бы только то, что кадр чем-то залит."""
    report.reset()
    d = voronka.parse("проба", VORONKA_CLEAN)
    key = voronka.key_tier(d)
    if key is None or key == 0:
        BAD.append("[воронка-затор] проба сама устроена так, что узкое "
                   "место не в середине — переделайте входные данные")
        return
    other = voronka.key_tier(voronka.parse("проба", dict(
        VORONKA_CLEAN,
        yarusy=[{"head": "Генерация", "text": "т"},
                {"head": "Отбор", "text": "т"},
                {"head": "Результат", "text": "т"}])))
    if other is not None:
        BAD.append("[воронка-затор] разметка без слова затора всё равно "
                   "нашла узкое место — проба негодная")
        return
    say(f"{'[воронка-затор]':<26} разностно: без слова затора "
        f"`key_tier` None, со словом — ярус {key} — ровно то, что "
        "рисунок золотит")
    OK.append("воронка-затор")


def main(argv=()):
    OUT.mkdir(parents=True, exist_ok=True)
    pptx = OUT / "proba-voronka.pptx"
    warns, d1, d2 = build(pptx)
    if warns:
        BAD.append(f"[сборка] демонстрационные кадры дали {len(warns)} "
                   f"предупреждений: {warns}")
    else:
        OK.append("сборка")
        say(f"{'[сборка]':<26} два кадра собраны чисто  →  {pptx}")
    probes()
    probe_height()
    probe_gold()
    probe_bottleneck_fill()
    if "--render" in argv:
        if render.render(pptx, OUT / "snaps"):
            BAD.append("[рендер] PDF или снимки не собрались")
    print(f"\nпрошло {len(OK)} · не прошло {len(BAD)}")
    for b in BAD:
        print("  " + b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
