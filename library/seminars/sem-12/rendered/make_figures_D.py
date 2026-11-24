#!/usr/bin/env python3
"""Программные схемы Кейса D Семинара 12 («Поиск по картинкам»).

Тулкит — общий `tools/seminar-build/fig_toolkit.py` (канон
`tools/seminar-production/README.md` §7), по образцу `make_figures_B.py` и
`make_figures_C.py` этого же занятия. Рисовалка обслуживает ТОЛЬКО кадры
Кейса D (`slides/n55`–`n69`); кадры других кейсов пишут параллельные сессии
своими рисовалками, этот файл их не трогает.

Заведена в круге 3 (`PEREDELKA-KRUG-3.md`): у Кейсов B и C схема постановки
(С1) нарисована, у Кейса D её не было вовсе — постановка пересказывалась
словами в теле кадра, что прямо запрещено
`tools/presentation-build/trebovaniya-k-soderzhaniyu-forma.md` §8. Вторая
фигура закрывает находку владельца 3: «покажи настоящие снимки корпуса с их
разметкой и с запросом, который по ним задаётся».

Две фигуры:

    case-d-shema-postanovka.png   n56 — схема С1: сплошное — снимок, описание
                                   (Кейс B, уже собрано); пунктирное золотое —
                                   поиск по архиву (этот кейс строит); серым —
                                   нужный снимок на руках у Ольги.

    case-d-korpus.png             n61 — ТРИ НАСТОЯЩИХ снимка корпуса с
                                   человеческой разметкой и вердиктом
                                   словесной ветки: один попавший запрос
                                   (К-слово) и один промах (К-пересказ), где
                                   выданный и верный снимок — из одной группы
                                   «похожие, но не те».

**Почему именно эти три снимка — и почему подделок здесь нет.**
`zamery-B/razmetka.json` несёт у каждого снимка поле `deck_allowed` с
причиной (решение `PEREDELKA-2026-11-24.md` §13: узнаваемый человек на кадре
деки платит за наш пример, не согласившись на это). Все три взятых снимка
помечены `deck_allowed: true` с причиной «людей нет» / «людей почти нет —
рука с краю», то есть замыливать нечего и никого. Лицензия у всех трёх —
CC BY 2.0 (Flickr, Open Images V7), автор назван подписью на кадре, как
требует и лицензия, и §13.2 того же решения.

    8cb7d659e2d0a541  G8 кружки и кофе   · запрос 1.7, словесная ветка попала
    71681aa82b7ef15f  G4 залы            · запрос 2.7, выдан первым — промах
    c53e9e5ce002345f  G4 залы            · запрос 2.7, верный ответ

Снимки берутся из локального кэша корпуса (`/tmp/s12-corpora/oiv7/images/`,
в гит не кладётся — `zamery-B/fetch_corpus_b.py` его восстанавливает по
манифесту с `sha256` на файл). Если кэша нет — рисовалка падает громко с
указанием, что запустить, а НЕ рисует заглушку: стилизованная карточка
вместо снимка есть ровно тот mock, который запрещён
(`CLAUDE.md`, `[[no-mock-fallbacks]]`).

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_D.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

CACHE = Path("/tmp/s12-corpora/oiv7/images")


def _photo_path(short_id):
    hits = sorted(CACHE.glob(f"*/{short_id}*.jpg"))
    if not hits:
        raise FileNotFoundError(
            f"нет снимка {short_id} в кэше корпуса {CACHE}. "
            f"Восстановить: python3 ../stend/zamery-B/fetch_corpus_b.py "
            f"(сверяет sha256 по manifest-foto-BC.json). Заглушку вместо "
            f"настоящего снимка эта рисовалка не рисует.")
    return hits[0]


def photo(im, d, short_id, x, y, w, h):
    """Настоящий снимок, вписанный в рамку целиком: пропорции сохраняются,
    поля — поверхностный серый, рамка — тиловая. Обрезать кадр нельзя: на
    двух из трёх снимков смысл примера сидит у края (номер на спинке
    кресла, рука с краю подноса)."""
    src = Image.open(_photo_path(short_id)).convert("RGB")
    sw, sh = src.size
    k = min(w / sw, h / sh)
    nw, nh = int(sw * k), int(sh * k)
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=SURF, outline=LIGHT, width=2)
    im.paste(src.resize((nw, nh), Image.LANCZOS), (int(x + (w - nw) / 2), int(y + (h - nh) / 2)))


def case_d_shema_postanovka():
    im = Image.new("RGB", (1760, 400), W)
    d = ImageDraw.Draw(im)
    head(d, "Узел, который строит этот кейс: поиск по архиву", sz=30)
    d.text((40, 64), "описания уже сделаны — по ним ещё никто не искал",
           font=f(21), fill=LIGHT)

    y1, h1 = 150, 160
    box(d, 40, y1, 400, h1, ["Снимок → описание", "Кейс B, уже собрано"], SURF,
        tc=DEEP, sz=20, outline=LIGHT, where="узел-описание")
    arrow(d, 440, y1 + h1 / 2, 530, y1 + h1 / 2, col=LIGHT, wd=4)

    box(d, 530, y1, 600, h1, ["Поиск по архиву", "запрос → снимок"], W,
        tc=DEEP, sz=21, where="узел-поиск")
    dashbox(d, 530, y1, 600, h1, GOLD, width=3)
    arrow(d, 1130, y1 + h1 / 2, 1220, y1 + h1 / 2, col=GOLD, wd=4, dash=True)

    box(d, 1220, y1, 500, h1, ["Нужный снимок", "у Ольги на руках"], SOFT_GREY,
        tc=GREY_TX, sz=20, outline=GREY_FILL, where="узел-исход")

    d.text((530, y1 + h1 + 26),
           "пунктиром — то, чего в процессе нет: этот узел строит сегодняшний кейс",
           font=f(19), fill=GOLDTX)
    save(im, "case-d-shema-postanovka.png")


CARDS = (
    # (x, ширина, запрос, класс, короткий id, разметка человека, вердикт, цвет, исход)
    (40, 680, "подносы с чашками кофе и сладостями", "К-слово", "8cb7d659",
     ["два подноса кофе по-восточному:", "джезва, чашечка, стакан чая, ложка"],
     "верный, первым: 4 леммы из 4", TEAL, True),
    (760, 680, "пустой зал, где у каждого места буквенно-числовой номер",
     "К-пересказ", "71681aa8",
     ["пустой амфитеатр, красно-терракотовые", "кресла, деревянная люстра-колесо"],
     "выдан первым — не тот: 2 леммы из 8", RED, False),
    (1480, 680, "", "", "c53e9e5c",
     ["пустой актовый зал, номера на спинках", "кресел читаются: «K-18», «L-19»"],
     "верный ответ — его в выдаче нет", GREY_TX, None),
)


def case_d_korpus():
    im = Image.new("RGB", (2240, 668), W)
    d = ImageDraw.Draw(im)

    for x, w, zapros, klass, sid, razmetka, verdikt, col, ok in CARDS:
        if zapros:
            d.rounded_rectangle([x, 8, x + w, 80], radius=10, fill=WARM,
                                outline=GOLD, width=2)
            lines = wrap(d, "«" + zapros + "»", f(20, True), w - 28)
            lines_at(d, x + 14, 8 + (72 - len(lines) * 26) // 2, lines,
                     f(20, True), GOLDINK, 26)
            d.text((x, 88), klass, font=f(18, True), fill=MUTE)
        else:
            d.text((x, 88), "тот же запрос", font=f(18, True), fill=MUTE)

        photo(im, d, sid, x, 118, w, 360)

        for ln in razmetka:
            fit(d, ln, f(18), w, f"разметка {sid}")
        lines_at(d, x, 492, razmetka, f(18), INK, 25)

        d.rounded_rectangle([x, 546, x + w, 602], radius=10, fill=SURF,
                            outline=col, width=2)
        if ok is True:
            check_outline(d, x + 32, 571, 13, TEAL)
        elif ok is False:
            xmark(d, x + 32, 574, 12, RED, wd=4)
        else:
            check_outline(d, x + 32, 571, 13, GREY_FILL)
        fit(d, verdikt, f(19, True), w - 72, f"вердикт {sid}")
        d.text((x + 58, 563), verdikt, font=f(19, True), fill=col)

    d.text((40, 616),
           "Выдача поиска по словам описаний. Разметка «что видно» написана человеком до того, "
           "как снимки описала модель.", font=f(17), fill=MUTE)
    d.text((40, 642),
           "Снимки архива — Open Images V7, Flickr, CC BY 2.0: Perica · Heart Internet · CPFL Cultura",
           font=f(17), fill=MUTE)
    save(im, "case-d-korpus.png")


def case_d_vektor():
    """n59 — как снимок и текст запроса попадают в одно пространство.

    Сетка патчей нарисована поверх НАСТОЯЩЕГО снимка корпуса, сжатого ровно
    до того разрешения, которое ждёт модель (224×224): зал видит, что именно
    теряется при сжатии, на кадре, который он уже видел на разборе корпуса.
    Размер вектора (768) проверен запуском модели на этом же снимке.

    Полотно намеренно широкое и низкое: на кадре схема стоит рядом с тремя
    плашками следствий, и при пропорции выше 1:4 вёрстка ужимает её по
    ширине («СХЕМА ЗАЖАТА»), то есть платит за содержание самым крупным,
    на что зал смотрит первым."""
    im = Image.new("RGB", (2240, 520), W)
    d = ImageDraw.Draw(im)

    side = 200
    src = Image.open(_photo_path("8cb7d659")).convert("RGB").resize((224, 224), Image.LANCZOS)
    src = src.resize((side, side), Image.LANCZOS)
    im.paste(src, (40, 40))
    step = side / 14.0                      # 224 / 16 = 14 патчей по стороне
    for i in range(1, 14):
        d.line([40 + i * step, 40, 40 + i * step, 40 + side], fill=(255, 255, 255), width=1)
        d.line([40, 40 + i * step, 40 + side, 40 + i * step], fill=(255, 255, 255), width=1)
    d.rectangle([40, 40, 40 + side, 40 + side], outline=LIGHT, width=2)
    lines_at(d, 40, 40 + side + 10,
             ["снимок сжат до 224×224 точек", "и разрезан на 196 патчей 16×16"],
             f(18), INK, 25)

    arrow(d, 270, 140, 360, 140, col=LIGHT, wd=4)
    box(d, 360, 70, 540, 140,
        ["Картиночная половина", "слои внимания сводят", "все патчи в один вектор"],
        SURF, tc=DEEP, sz=20, outline=LIGHT, where="половина-картинка")

    box(d, 40, 330, 260, 110, ["«значок на лацкане", "выступающего»"], WARM,
        tc=GOLDINK, sz=17, outline=GOLD, where="запрос")
    arrow(d, 305, 385, 360, 385, col=LIGHT, wd=4)
    box(d, 360, 315, 540, 140,
        ["Текстовая половина", "обе половины учили", "на парах «снимок + подпись»"],
        SURF, tc=DEEP, sz=20, outline=LIGHT, where="половина-текст")

    arrow(d, 900, 150, 1090, 210, col=TEAL, wd=4)
    arrow(d, 900, 375, 1090, 315, col=TEAL, wd=4)
    box(d, 1100, 150, 1100, 225,
        ["Одно пространство", "вектор на 768 чисел с каждой стороны",
         "выдача — ближайшие к запросу снимки"],
        W, tc=DEEP, sz=22, outline=TEAL, where="пространство")
    cap = wrap(d, "мельче патча в вектор не попадает — это и есть предел того, "
                  "что способ способен найти", f(18), 1100)
    lines_at(d, 1100, 392, cap, f(18), MUTE, 25)
    save(im, "case-d-vektor.png")


if __name__ == "__main__":
    case_d_shema_postanovka()
    case_d_korpus()
    case_d_vektor()
    if WARN:
        print("WARN:", *WARN, sep="\n  ")
    report()
