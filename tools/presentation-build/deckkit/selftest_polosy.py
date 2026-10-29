# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ПАРНЫХ ПОЛОС: демонстрационный кадр и прогон КАЖДОГО отказа.

Стандарт пакета один и здесь он тоже не обсуждается: ПРОВЕРКА, НЕ
ПРОВЕРЕННАЯ НА СЛОМАННОМ ВХОДЕ, — НЕ ПРОВЕРКА. Поэтому на каждый сторож
`polosy.check_polosy` два прогона: чистый вход (обязан молчать) и сломанный
(обязан сказать именно своё).

Сверх прогонов — СОБРАННЫЙ КАДР. Он нужен не для красоты отчёта: половина
дефектов этой формы (подпись значения, наехавшая на соседнюю полосу; полоса,
ставшая невидимой полоской; разрыв, которого не видно на логарифме) не
меряется координатами — `nalozhenie_bbox.py` их не ловит по построению
(`notes/mcp-limitations.md` [#301-7]), и глаз пока ничем не заменяется.

Запуск:  python3 -m deckkit.selftest_polosy         (сборка + прогоны)
         python3 -m deckkit.selftest_polosy --render (ещё и PDF со снимками)
"""
import sys
from pathlib import Path

from pptx.enum.text import PP_ALIGN

from . import metrics, polosy, prims, render, report
from .theme import DEEP, LIGHT, SLIDE_H, SLIDE_W, WHITE

OUT = Path(__file__).resolve().parents[1] / "out-polosy"
MX, TOP, FOOT = 0.55, 1.46, 6.94
FULL_W = SLIDE_W - 2 * MX

OK, BAD = [], []


def say(line):
    print(line)


# ── демонстрационные входы (служебные: содержания не придумываем, взяты
#    примеры разметки из наряда) ───────────────────────────────────────

LOG = {
    "unit": "доллары за одну пробу · шкала логарифмическая",
    "scale": "log",
    "caption": "Пара считана в одной единице: цена одной пробы.",
    "rows": [
        {"label": "Одно изображение 1024×1024",
         "klassika": {"value": 100, "text": "$50–150"},
         "model": {"value": 0.042, "text": "$0,034–0,05"},
         "mnozhitel": "×1 000–4 500 к заказу"},
        {"label": "Минута озвучки",
         "klassika": {"value": 30, "text": "$20–40"},
         "model": {"value": 0.41, "text": "$0,41"},
         "mnozhitel": "×73 к опту"},
        {"label": "Выпуск микродрамы",
         "klassika": {"value": 1470, "text": "$1 200–1 800"},
         "model": {"value": 0.1, "text": "$0,10"},
         "mnozhitel": "×14 700 к рознице"},
    ],
}

LIN = {
    "unit": "часы человека на один готовый ролик",
    "scale": "linear",
    "rows": [
        {"label": "Отбор кадров",
         "klassika": {"value": 18, "text": "18 ч"},
         "model": {"value": 11, "text": "11 ч"}},
        {"label": "Сборка и сведение",
         "klassika": {"value": 9, "text": "9 ч"},
         "model": {"value": 7, "text": "7 ч"}},
    ],
}


# ── сборка кадра ────────────────────────────────────────────────────


def frame(p, title, raw, foot):
    d = polosy.parse("проба", raw)
    polosy.check_polosy("проба", d, FULL_W)
    s = prims.blank(p)
    prims.rect(s, 0, 0, SLIDE_W, SLIDE_H, WHITE, count="фон")
    sz = metrics.fit_size(title, FULL_W, 0.92, hi=27.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag="проба/заголовок")
    prims.text_box(s, MX, 0.40, FULL_W, 0.92, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag="проба/заголовок")
    h = polosy.polosy_h(d, FULL_W)
    got = polosy.draw_polosy(s, "проба", d, MX, TOP, FULL_W)
    if abs(got - h) > 0.02:
        BAD.append(f"[полосы-мера] мера обещала {h:.3f}\", рисунок занял "
                   f"{got:.3f}\" — две формулы одного числа")
    if TOP + got > FOOT:
        BAD.append(f"[полосы-мера] форма дошла до подвала: низ "
                   f"{TOP + got:.2f}\" при подвале {FOOT:.2f}\"")
    prims.text_box(s, MX, FOOT, FULL_W, 0.40, foot, size=11.0, italic=True,
                   color=LIGHT, ls=1.12, tag="проба/подвал")
    return s


def build(path):
    report.reset()
    p = prims.new_deck()
    frame(p, "Цена одной пробы: классический режим против режима модели",
          LOG, "служебный кадр самопроверки ядра · форма «парные полосы»")
    frame(p, "Линейная шкала: разрыв в полтора раза, а не в тысячу",
          LIN, "служебный кадр самопроверки ядра · шкала линейная")
    p.save(str(path))
    w = list(report.WARNINGS)
    report.reset()
    return w


# ── прогоны отказов ─────────────────────────────────────────────────


def run(raw, w=FULL_W):
    """Разбор и сторож на одном входе. Возвращает (разбор, предупреждения)."""
    report.reset()
    d = polosy.parse("проба", raw)
    if d is not None:
        polosy.check_polosy("проба", d, w)
    out = list(report.WARNINGS)
    report.reset()
    return d, out


def _hits(warns, needle):
    return [x for x in warns if needle in x]


def probe(name, raw, needle, w=FULL_W, must_parse=True):
    """Один отказ: сломанный вход обязан сказать именно про `needle`, а
    чистый — промолчать про него же."""
    _, clean = run(LOG)
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
    if must_parse and d is None:
        BAD.append(f"[{name}] разбор снял форму целиком — сторож не "
                   "проверен на нарисованном кадре")
        return
    OK.append(name)
    say(f"{'[' + name + ']':<26} ЛОВИТ  →  {hit[0][:118]}")


def rows_of(n):
    return [{"label": f"строка {i}",
             "klassika": {"value": 10 * i, "text": f"{10 * i} ч"},
             "model": {"value": i, "text": f"{i} ч"}} for i in range(1, n + 1)]


def probes():
    # 0. ЧИСТЫЙ вход молчит целиком — без этого всё остальное ничего не
    #    доказывает: сторож, который говорит всегда, не сторож.
    for name, raw in (("чисто-лог", LOG), ("чисто-линейно", LIN)):
        _, got = run(raw)
        if got:
            BAD.append(f"[{name}] чистый вход дал {len(got)} предупреждений: "
                       f"{got}")
        else:
            OK.append(name)
            say(f"{'[' + name + ']':<26} МОЛЧИТ на чистом входе")

    probe("единица", dict(LOG, unit=""), "не названа ЕДИНИЦА")
    probe("логарифм-не-назван", dict(LOG, unit="доллары за одну пробу"),
          "шкала логарифмическая, а подпись")
    probe("одна-строка", dict(LOG, rows=LOG["rows"][:1]), "строка одна")
    probe("шестая-строка", {"unit": "часы", "scale": "linear",
                            "rows": rows_of(6)}, "строк 6")
    probe("значение-не-число",
          dict(LOG, rows=[dict(LOG["rows"][0],
                               model={"value": "дёшево", "text": "дёшево"})]
               + LOG["rows"][1:]),
          "не число")
    probe("ноль-на-логарифме",
          dict(LOG, rows=[dict(LOG["rows"][0],
                               model={"value": 0, "text": "$0"})]
               + LOG["rows"][1:]),
          "не больше нуля")
    probe("подписи-сойдутся",
          dict(LOG, rows=[dict(LOG["rows"][0],
                               klassika={"value": 100,
                                         "text": "$50–150 за изображение "
                                                 "в разрешении 1024×1024"})]
               + LOG["rows"][1:]),
          "сядет на соседнюю полосу")
    probe("разные-единицы-объявлены",
          dict(LOG, rows=[dict(LOG["rows"][0], unit="доллары"),
                          dict(LOG["rows"][1], unit="часы")]),
          "РАЗНЫЕ единицы")
    probe("разные-единицы-в-подписях",
          {"unit": "непонятно что", "scale": "linear",
           "rows": [{"label": "деньгами",
                     "klassika": {"value": 150, "text": "$150"},
                     "model": {"value": 40, "text": "$40"}},
                    {"label": "временем",
                     "klassika": {"value": 120, "text": "120 часов"},
                     "model": {"value": 30, "text": "30 часов"}}]},
          "Одна шкала на обе")
    probe("полоса-невидима",
          {"unit": "доллары за одну пробу", "scale": "linear",
           "rows": LOG["rows"]},
          "на экране её нет")
    probe("неполная-пара",
          dict(LOG, rows=[{"label": "одна сторона",
                           "klassika": {"value": 10, "text": "$10"}}]
               + LOG["rows"][1:]),
          "пара в ней обязана быть полной")
    probe("чужой-ключ", dict(LOG, legenda="да"), "ядро не читает")
    probe("шкале-нет-ширины", LOG, "под шкалу осталось", w=4.2)

    # Разбор снимает форму целиком — отдельно, потому что `probe` требует
    # нарисованного кадра, а здесь кадра как раз и не должно остаться.
    for name, raw, needle in (
            ("нет-строк", {"unit": "часы", "rows": []}, "нет `rows`"),
            ("поле-не-словарь", ["строка"], "поле `polosy`"),
            ("шкала-неизвестна", dict(LOG, scale="кубическая"),
             "ядру неизвестна")):
        d, got = run(raw)
        hit = _hits(got, needle)
        snatched = d is None
        if not hit or (name != "шкала-неизвестна" and not snatched):
            BAD.append(f"[{name}] разбор {d is not None} сказал {got}")
        else:
            OK.append(name)
            say(f"{'[' + name + ']':<26} ЛОВИТ  →  {hit[0][:118]}")


# ── мера ────────────────────────────────────────────────────────────


def probe_scale():
    """Логарифм делает именно то, ради чего заведён: пара, отличающаяся в
    тысячи раз, остаётся видимой ОБЕИМИ полосами.

    Разностная проба, и без неё «форма собралась» не значило бы ничего: на
    линейной шкале те же числа дают полосу в сотые доли дюйма."""
    report.reset()
    d_log = polosy.parse("проба", LOG)
    d_lin = polosy.parse("проба", dict(LOG, scale="linear"))
    report.reset()
    _, _, plot, _, _ = polosy.cols(d_log, FULL_W)
    lg = polosy._frac(0.042, d_log, polosy.DEFAULT) * plot
    lin = polosy._frac(0.042, d_lin, polosy.DEFAULT) * plot
    if lg < polosy.DEFAULT.min_bar or lin >= polosy.DEFAULT.min_bar:
        BAD.append(f"[логарифм-видимость] на логарифме {lg:.3f}\", на "
                   f"линейной {lin:.3f}\" — проба меряет не то")
    else:
        OK.append("логарифм-видимость")
        say(f"{'[логарифм-видимость]':<26} разностно: ЛОВИТ  →  полоса "
            f"$0,034–0,05 на логарифме {lg:.2f}\", на линейной шкале "
            f"{lin:.3f}\" — то есть её там нет")


def main(argv=()):
    OUT.mkdir(parents=True, exist_ok=True)
    pptx = OUT / "proba-polosy.pptx"
    warns = build(pptx)
    if warns:
        BAD.append(f"[сборка] демонстрационный кадр дал {len(warns)} "
                   f"предупреждений: {warns}")
    else:
        OK.append("сборка")
        say(f"{'[сборка]':<26} два кадра собраны чисто  →  {pptx}")
    probes()
    probe_scale()
    if "--render" in argv:
        if render.render(pptx, OUT / "snaps"):
            BAD.append("[рендер] PDF или снимки не собрались")
    print(f"\nпрошло {len(OK)} · не прошло {len(BAD)}")
    for b in BAD:
        print("  " + b)
    return 1 if BAD else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
