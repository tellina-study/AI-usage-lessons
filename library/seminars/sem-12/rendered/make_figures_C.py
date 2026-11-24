#!/usr/bin/env python3
"""Программная схема Кейса C Семинара 12 («Определение запрещённого»).
Тулкит — общий `tools/seminar-build/fig_toolkit.py` (canon
`tools/seminar-production/README.md` §7), по образцу `make_figures_B.py`
этого же занятия — рисовалка обслуживает только слайды Кейса C
(`slides/n40-n53`), слайды других кейсов пишут параллельные сессии своими
рисовалками, этот файл их не трогает.

Три фигуры:

    case-c-shema-postanovka.png   n43 — схема С1: сплошное — загрузка и
                                  описание (Кейс B, уже собрано); пунктирное
                                  золотое — премодерация: три флага (этот
                                  кейс строит); серым, за контуром —
                                  публикация/отложено до человека.

    case-c-korpus-primery.png     n46 — пять НАСТОЯЩИХ кадров корпуса со своей
                                  разметкой: позитив и трудный негатив курения,
                                  позитив еды, позитив и трудный негатив экрана.
                                  Два трудных негатива стоят рядом намеренно:
                                  они разной природы — у курения предмет есть,
                                  а человека нет; у экрана предмет похож, а
                                  класс другой (печать, не проекция).

    case-c-vedro-okurkov.png      n41 — тот самый кадр сцены: урна, полная
                                  окурков, без единого человека. Модель
                                  отвечает `smoking: true`.

Снимки — Open Images V7, все под CC BY 2.0, авторы названы ниже в `PHOTOS`.

**Про лица — решение круга 4, оно сменило прежнее.** Первые четыре кадра
отбирались так, чтобы на них не было узнаваемых лиц. Трудный негатив экрана
такого варианта не имеет вовсе: все пять кандидатов `SLIDES_HARDNEG` — это
печатная поверхность ПОЗАДИ ГОВОРЯЩЕГО, и composition «текст на вертикальной
поверхности за человеком» и есть то, что путает модель; вырезав человека, мы
показали бы не тот кадр, который мерили. Взят `1ff27a55871e30db` — взрослый
докладчик за трибуной на публичном мероприятии, CC BY 2.0. Это согласуется с
деком занятия: `case-b-light-hard.png` Кейса B давно показывает аудиторию с
узнаваемыми лицами из того же корпуса.

**Один кандидат исключён отдельно и не по композиции:** `24955fd68bc70264` —
школьный постер, на котором напечатаны имя, класс и школа автора, а в кадре,
по всем признакам, несовершеннолетний. Несовершеннолетние исключены из самого
корпуса (`corpus.py`, `*_MINOR_EXCLUDED`), и на кадр деки такой снимок не идёт
тем более. Подпись автора на кадр НЕ
идёт (`trebovaniya-k-soderzhaniyu-forma.md` §5.12 — источники фотографий на
слайде не подписывать); атрибуция CC BY стоит в заметках слайдов n41/n46,
которые публикуются вместе с деком.

Кэш снимков (`/tmp/s12-corpora/oiv7/images`) в гите не лежит — так же, как у
`make_figures_B.py`: в гит идёт собранный PNG, не исходные jpg. Пропал кэш —
перекачать по `plan-peredelki/korpus/manifest-foto-BC.json` (id ниже, sha256
на файл).

Запуск (из своей папки):

    cd library/seminars/sem-12/rendered
    python3 make_figures_C.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import *  # noqa: F401,F403

HERE = Path(__file__).resolve().parent                     # .../sem-12/rendered
CORPUS = Path("/tmp/s12-corpora/oiv7/images")

# id → (папка среза, автор, лицензия). Атрибуция CC BY 2.0 — в заметках n41/n46.
PHOTOS = {
    "2f75c267eaae09c1": ("C-smoking", "jenny downing", "CC BY 2.0"),
    "193d76cd49bb8a7c": ("C-smoking", "Erich Ferdinand", "CC BY 2.0"),
    "159de001bfb786cc": ("C-fooddrink", "Cristiano Betta", "CC BY 2.0"),
    "0cd992ac5ca38878": ("C-slides", "Josué Goge", "CC BY 2.0"),
    "1ff27a55871e30db": ("C-slides", "Alexander Bonilla", "CC BY 2.0"),
}


def _photo(pid):
    return CORPUS / PHOTOS[pid][0] / f"{pid}.jpg"


def _paste_fit(im, path, x, y, w, h):
    """Вписать снимок в прямоугольник: масштаб по большей стороне, обрезка по центру."""
    photo = Image.open(path).convert("RGB")
    pw, ph = photo.size
    scale = max(w / pw, h / ph)
    photo = photo.resize((int(pw * scale), int(ph * scale)))
    pw, ph = photo.size
    left, top = (pw - w) // 2, (ph - h) // 2
    im.paste(photo.crop((left, top, left + w, top + h)), (int(x), int(y)))


def case_c_shema_postanovka():
    im = Image.new("RGB", (1700, 440), W)
    d = ImageDraw.Draw(im)
    # Заголовка у схемы нет намеренно: кадр n43 уже назван этим же вопросом,
    # и повтор читался на рендере как сбой вёрстки (просмотр глазами, круг 3).
    d.text((40, 40),
            "снимок уже загружен и описан — вопрос в том, можно ли его публиковать",
            font=f(21), fill=LIGHT)

    y1, h1 = 120, 150
    box(d, 40, y1, 420, h1, ["Загрузка + описание", "Кейс B, уже собрано"], SURF,
        tc=DEEP, sz=20, outline=LIGHT, where="узел-описание")
    arrow(d, 460, y1 + h1 / 2, 550, y1 + h1 / 2, col=LIGHT, wd=4)

    box(d, 550, y1, 560, h1, ["Премодерация: три флага", "курение · еда/напитки · слайды"], W,
        tc=DEEP, sz=19, outline=GOLD, where="узел-премодерация")
    arrow(d, 1110, y1 + h1 / 2, 1200, y1 + h1 / 2, col=GOLD, wd=4, dash=True)

    box(d, 1200, y1, 460, h1,
        ["Публикация", "или отложено до человека"], SOFT_GREY,
        tc=GREY_TX, sz=20, outline=GREY_FILL, where="узел-исход")

    save(im, "case-c-shema-postanovka.png")


def case_c_korpus_primery():
    """n46 — корпус предъявлен кадрами, а не только числом. Четыре настоящих
    снимка среза Open Images V7 с той разметкой, по которой их считали.

    Два трудных негатива стоят рядом намеренно, и они разной природы.
    У курения (панель 2) предмет есть, а человека нет — определение у1' такой
    кадр исключает, и на таких кадрах модель даёт 24 из своих 25 ложных тревог.
    У экрана (панель 5) предмет похож, а класс другой: печатный баннер, не
    проекция — на пяти таких кадрах модель ошибается в четырёх."""
    im = Image.new("RGB", (1988, 470), W)
    d = ImageDraw.Draw(im)
    head(d, "Пять кадров корпуса — и разметка, по которой их считали", sz=30)

    pw, ph = 363, 242
    gy, gap, x0 = 96, 18, 50
    panels = [
        ("2f75c267eaae09c1", LIGHT, SURF, DEEP,
         ["курение · ПОЗИТИВ", "сигарета зажжена, в руке"]),
        ("193d76cd49bb8a7c", GOLD, W, GOLDINK,
         ["курение · ТРУДНЫЙ НЕГАТИВ", "предмет есть, человека нет"]),
        ("159de001bfb786cc", LIGHT, SURF, DEEP,
         ["еда и напитки · ПОЗИТИВ", "человек ест"]),
        ("0cd992ac5ca38878", LIGHT, SURF, DEEP,
         ["экран · ПОЗИТИВ", "проекция в кадре"]),
        ("1ff27a55871e30db", GOLD, W, GOLDINK,
         ["экран · ТРУДНЫЙ НЕГАТИВ", "печатный баннер, не проекция"]),
    ]
    for n, (pid, frame, fill, tc, caption) in enumerate(panels):
        x = x0 + n * (pw + gap)
        _paste_fit(im, _photo(pid), x, gy, pw, ph)
        d.rectangle([x, gy, x + pw, gy + ph], outline=frame, width=4)
        box(d, x, gy + ph + 14, pw, 76, caption, fill, tc=tc, sz=17,
            outline=frame, where=f"подпись-{n + 1}")

    save(im, "case-c-korpus-primery.png")


def case_c_vedro_okurkov():
    """n41 — кадр, с которого кейс открывается. Урна, полная окурков, ни одного
    человека; мультимодальная модель отвечает `smoking: true`. На заданный ею же
    вопрос это верно, для архива центра — нет."""
    im = Image.new("RGB", (1700, 620), W)
    d = ImageDraw.Draw(im)
    head(d, "Кадр архива: урна у входа, ни одного человека", sz=30)

    pw, ph = 700, 466
    gx, gy = 60, 104
    _paste_fit(im, _photo("193d76cd49bb8a7c"), gx, gy, pw, ph)
    d.rectangle([gx, gy, gx + pw, gy + ph], outline=GOLD, width=4)

    bx, bw = 840, 800
    box(d, bx, gy + 40, bw, 120,
        ["Ответ модели", "smoking: true"], W, tc=GOLDINK, sz=26, outline=GOLD,
        where="плашка-ответ")
    box(d, bx, gy + 186, bw, 120,
        ["Определение владельца", "человек курит либо изображение курения"],
        SURF, tc=DEEP, sz=20, outline=LIGHT, where="плашка-определение")
    box(d, bx, gy + 332, bw, 134,
        ["Таких кадров среди ложных тревог", "24 из 25"],
        SURF, tc=DEEP, sz=24, outline=LIGHT, where="плашка-счёт")

    save(im, "case-c-vedro-okurkov.png")


if __name__ == "__main__":
    case_c_shema_postanovka()
    case_c_korpus_primery()
    case_c_vedro_okurkov()
    if WARN:
        print("WARN:", *WARN, sep="\n  ")
    report()
