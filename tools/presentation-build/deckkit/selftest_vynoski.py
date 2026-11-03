# -*- coding: utf-8 -*-
"""САМОПРОВЕРКА ФОРМЫ «РАЗБОР НА ИЗОБРАЖЕНИИ»: кадр, который видно глазами,
и четыре отказа, которые обязаны прозвучать.

Две половины, и вторая без первой ничего не стоит.

ПОЛОВИНА ПЕРВАЯ — НАСТОЯЩИЙ КАДР. Собирается демонстрационный кадр с
настоящим снимком с диска, рендерится в PDF и PNG тем же `soffice` +
`pdftoppm`, каким собирается продукт (`proverki-i-pravila.md`: «инструмент,
через который смотрят, обязан быть тем же, который собирает продукт»).
Снимок берётся из выпуска Лекции 8; ТЕКСТ ВЫНОСОК СЛУЖЕБНЫЙ — это проба
формы, а не материал лекции, и первая выноска набрана тем самым примером,
которым форма заказана.

Доля площади под снимком меряется ПО СОБРАННОМУ ФАЙЛУ (`media.
page_image_share`), а не по намерению раскладки: §2.2 переноса требует ≥55%
площади КАДРА, и единственное место, где это наблюдаемо, — страница.

ПОЛОВИНА ВТОРАЯ — ОТКАЗЫ. Пять выносок · одна выноска · `at` за пределами
[0, 1] · снимка нет на диске. Каждая проба требует СВОЕГО `[выноски]`, а не
любого предупреждения с этим тегом: проба, которой довольно совпадения тега,
зеленеет от соседнего дефекта и перестаёт мерить свой.

Запуск:  python3 -m deckkit.selftest_vynoski   (из `tools/presentation-build`)
         --no-render  — только сборка и отказы, без LibreOffice
"""
import sys
from pathlib import Path

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from . import contrast, media, metrics, prims, render, report, vynoski
from .theme import DEEP, GOLD, LIGHT, MID, SLIDE_W

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent.parent
LEC8 = REPO / "library/lectures/lec-08/rework-v5"
OUT = HERE.parent / "out-vynoski"

# Снимок пробы: 1024 × 676, пропорция 1,51 — при ней вписанное изображение
# берёт 56% площади кадра, то есть порог §2.2 проходится БЕЗ обрезки. Это и
# есть содержательный выбор пробы: обрезкой порог взять легко, вписыванием —
# ровно настолько, насколько позволяет пропорция.
IMG = "assets/screenshots/s26-sgenerirovannaya-ruka.png"

# РАСКЛАДКА ПРОБЫ СЧИТАНА ОТ ПОРОГА, А НЕ ВЗЯТА У `refdeck`. Снимок 55%
# площади при ширине 12,23" требует не меньше 6,03" высоты — то есть на
# заголовок, подпись и поля остаётся 1,47" из семи с половиной. Обычная
# раскладка кадра (заголовок от 0,40, подвал на 6,94) этого порога взять НЕ
# может ни при какой пропорции снимка, и это не дефект пробы: §2.2 переноса
# ровно это и говорит — «текст уходит в выноски и одну нижнюю строку».
# Подвала здесь поэтому нет, а источник стоит последним сегментом подписи,
# как `refdeck.footer` и делает с подписью hero.
MX = 0.55
TITLE_Y, TITLE_H = 0.22, 0.58
BODY_TOP = 0.88


class FakeSlide:
    """Кадр для пробы: ровно то, что `vynoski_of` читает, — `sid` и `meta`.
    Разбирать настоящий файл здесь нечего: форма берёт одно поле."""

    def __init__(self, sid, meta):
        self.sid, self.meta = sid, meta


def demo_meta():
    """Разметка демонстрационного кадра — она же пример в шапке формы."""
    return {"vynoski": {
        "image": IMG,
        "caption": "Служебная проба формы «разбор на изображении». "
                   "Снимок: lec-08/rework-v5/assets/screenshots.",
        "points": [
            {"at": [0.40, 0.20], "side": "left",
             "head": "Отказ 1: псевдобуквы",
             "text": "Сжатие в 48 раз в автокодировщике. Буква размывается "
                     "ещё до работы генератора."},
            {"at": [0.66, 0.50], "side": "right",
             "head": "Служебная выноска 2: заголовок подлиннее, в две строки",
             "text": "Проба переноса: тело в три-четыре строки, чтобы было "
                     "видно, считается высота бокса или угадывается."},
            {"at": [0.44, 0.82], "side": "left",
             "head": "Служебная выноска 3",
             "text": "Короткое тело — бокс обязан стать ниже, а не остаться "
                     "вровень с соседним."},
        ]}}


def build_demo(path, *, meta=None, sid="s01"):
    """Демонстрационный кадр целиком: заголовок, форма, подвал."""
    sl = FakeSlide(sid, meta or demo_meta())
    v = vynoski.vynoski_of(sl, root=LEC8)
    if v is None:
        return None, None
    w = SLIDE_W - 2 * MX
    vynoski.check_vynoski(sid, v, w)
    h = vynoski.vynoski_h(v, w)

    p = prims.new_deck()
    s = prims.blank(p)
    title = "Служебная проба формы «разбор на изображении»"
    sz = metrics.fit_size(title, w, TITLE_H, hi=26.0, lo=19.0, floor=15.0,
                          bold=True, ls=1.08, tag=f"{sid}/заголовок")
    prims.text_box(s, MX, TITLE_Y, w, TITLE_H, title, size=sz, bold=True,
                   color=DEEP, ls=1.08, tag=f"{sid}/заголовок")
    vynoski.draw_vynoski(s, sid, v, MX, BODY_TOP, w, h)
    if BODY_TOP + h > 7.5 - 0.10:
        report.warn(f"[выноски] {sid}: форма уходит за нижний край кадра — "
                    f"низ на {BODY_TOP + h:.2f}\" при холсте 7,50\"")
    p.save(str(path))
    return p, v


# ── пробы отказов ────────────────────────────────────────────────────


def _warns(meta, sid="sX"):
    """Предупреждения ОДНОГО разбора, начисто: состояние отчёта снимается и
    возвращается, иначе пробы считают чужие дефекты своими."""
    saved = report.snapshot()
    report.reset()
    try:
        v = vynoski.vynoski_of(FakeSlide(sid, meta), root=LEC8)
        if v is not None:
            vynoski.check_vynoski(sid, v, SLIDE_W - 2 * MX)
        return list(report.WARNINGS)
    finally:
        report.restore(saved)


def _pt(n, at=(0.5, 0.5), side="left"):
    return {"at": list(at), "side": side, "head": f"Выноска {n}",
            "text": "Служебное тело пробы."}


def probe_five(say):
    """Пятая выноска — отказ, а не ужатый кегль."""
    meta = {"vynoski": {"image": IMG,
                        "points": [_pt(i, (0.30 + 0.08 * i, 0.15 * i),
                                       "left" if i % 2 else "right")
                                   for i in range(1, 6)]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "предел" in w]
    say("пять выносок", bool(hit), hit[:1])
    return bool(hit)


def probe_one(say):
    """Одна выноска — это подпись, а не разбор."""
    meta = {"vynoski": {"image": IMG, "points": [_pt(1, (0.5, 0.4))]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "одна" in w]
    say("одна выноска", bool(hit), hit[:1])
    return bool(hit)


def probe_range(say):
    """`at` за пределами [0, 1] — указатель уехал бы мимо предмета."""
    meta = {"vynoski": {"image": IMG,
                        "points": [_pt(1, (1.4, 0.3), "left"),
                                   _pt(2, (0.7, -0.2), "right")]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "диапазон" in w]
    say("`at` вне [0, 1]", len(hit) == 2, hit[:2])
    return len(hit) == 2


def probe_missing(say):
    """Снимка нет на диске — форме не на чем стоять."""
    meta = {"vynoski": {"image": "assets/screenshots/нет-такого-файла.png",
                        "points": [_pt(1, (0.3, 0.3)), _pt(2, (0.7, 0.6))]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "на диске" in w]
    say("снимка нет на диске", bool(hit), hit[:1])
    return bool(hit)


def probe_covered(say):
    """Бокс, накрывший точку, на которую указывает, отменяет форму."""
    meta = {"vynoski": {"image": IMG,
                        "points": [_pt(1, (0.02, 0.30), "left"),
                                   _pt(2, (0.60, 0.60), "right")]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "накрывает" in w]
    say("бокс накрыл свою точку", bool(hit), hit[:1])
    return bool(hit)


def probe_share(say):
    """Вертикальный снимок порога §2.2 не берёт — и об этом сказано числом."""
    meta = {"vynoski": {"image": "assets/screenshots/s02-moviola.jpg",
                        "points": [_pt(1, (0.35, 0.30)),
                                   _pt(2, (0.62, 0.70), "right")]}}
    hit = [w for w in _warns(meta) if "[выноски]" in w and "площади" in w]
    say("вертикальный снимок не берёт 55%", bool(hit), hit[:1])
    return bool(hit)


PROBES = (probe_five, probe_one, probe_range, probe_missing, probe_covered,
          probe_share)


# ── прогон ───────────────────────────────────────────────────────────


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    do_render = "--no-render" not in argv
    OUT.mkdir(parents=True, exist_ok=True)
    ok = True
    lines = []

    def say(name, good, extra=()):
        nonlocal ok
        ok = ok and good
        lines.append(f"  {'ok ' if good else 'НЕТ'}  {name}")
        for e in extra:
            lines.append(f"         {e[:150]}")

    print("── отказы формы ────────────────────────────────────────")
    for pr in PROBES:
        pr(say)
    print("\n".join(lines))

    print("\n── демонстрационный кадр ───────────────────────────────")
    report.reset()
    pptx = OUT / "proba-vynoski.pptx"
    p, v = build_demo(pptx)
    if p is None:
        print("  НЕТ  кадр не собрался: поле `vynoski` не разобрано")
        return 1
    share = media.page_image_share(p.slides[0])
    w = SLIDE_W - 2 * MX
    print(f"  снимок: {v['image']}")
    print(f"  доля площади кадра под снимком: {100 * share:.1f}% "
          f"(порог §2.2 — {100 * vynoski.DEFAULT.min_share:.0f}%)")
    print(f"  высота формы: {vynoski.vynoski_h(v, w):.2f}\" при колонке "
          f"выноски {vynoski._col_w(v, w, vynoski.DEFAULT):.2f}\"")
    say("снимок ≥55% площади кадра", share >= vynoski.DEFAULT.min_share)

    say("форма не уходит за нижний край", BODY_TOP + vynoski.vynoski_h(v, w)
        <= 7.5 - 0.10)
    mine = [o for o in report.WARNINGS if o.startswith("[выноски]")]
    say("демонстрационный кадр без замечаний формы", not mine, mine)

    contrast.check(p, tag="проба")
    blk = report.blocking()
    say("блокирующих предупреждений нет", not blk, blk)
    oth = [o for o in report.other()
           if not o.startswith("[выноски]")]
    say("предупреждений контраста и пола нет", not oth, oth)
    print(f"  файл: {pptx}")

    if do_render:
        rc = render.render(pptx, OUT / "snaps")
        pngs = sorted((OUT / "snaps").glob("*.png"))
        say("рендер PDF + PNG", rc == 0 and bool(pngs))
        for f in pngs:
            print(f"  снимок страницы: {f}")

    print("\n".join(lines[-6:]))
    print("\nИТОГ: " + ("всё сошлось" if ok else "ЕСТЬ РАСХОЖДЕНИЯ"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
