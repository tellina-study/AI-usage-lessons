#!/usr/bin/env python3
"""Кейс 4 — три фигуры из НАСТОЯЩИХ сканов корпуса, не из нарисованных
«как бы фотографий» (issue #311; канон `tools/presentation-build/README.md`
§5.7: стилизованная подделка под снимок запрещена, а чего нет настоящего —
о том говорят честно, а не рисуют).

Откуда сканы. `stend/corpus/cord_sample/receipt_NN.jpg` — 30 изображений
открытого датасета CORD (чеки), ровно те, на которых считался весь замер
Кейса 4. Ни один пиксель не дорисован: всё, что здесь делается с картинкой,
делается теми же функциями, которыми её готовил замер.

Чем получен каждый кадр — и почему именно так. Модель видит не файл с диска,
а строку запроса: скан, приведённый к 300×450 и пережатый в JPEG. Поэтому на
фигурах стоит ИМЕННО ЭТОТ вид — то, что уходило в модель, а не исходный файл.
Функции-источники берутся импортом из самих замерочных скриптов, а не
переписываются здесь (переписанная копия разошлась бы с замером молча):

  - `stend/measure/case4_full_retrieval_30.py`
      `to_data_url(path, w=300, h=450, q=80)` — опорный вид скана;
      `soft_dup(path)`  — «пересканировали»: уменьшение до 0,97 и обратно,
                          пережатие JPEG с качеством 60;
      `hard_dup(path)`  — «сняли под углом»: поворот на 12°, обрезка 4% с
                          каждого края, качество 80.
      Обе детерминированы — ни `random`, ни времени: кадр на слайде бит в бит
      тот вход, на котором мерили.
  - `stend/measure/case4_quality_limits.py`
      `hard_dup(path, w, h, q, blur)` — та же жёсткая аугментация с
      параметрами точки оси (размер, качество), и `pil_of(data_url)` —
      обратное декодирование строки запроса в картинку.

Оба модуля читают свои пути относительно собственной папки, поэтому импорт
идёт с временной сменой текущего каталога на `stend/measure/` (см.
`_measure_cwd`). Сети при импорте ни один из них не трогает.

Текст, палитра и кегли — `tools/seminar-build/fig_toolkit.py`, тот же
инструмент, что у программных схем занятия (`make_figures_sem10.py`).

ТРИ ВЫХОДНЫХ ФАЙЛА в `rendered/figures/`:

  1. `case4-primery-dubli.png` — четыре кадра в ряд: оригинал `receipt_01`,
     его мягкий дубль, его же дубль, снятый под углом, и чужой чек
     `receipt_10`. Числа под кадрами — `stend/raw/case4_mm_full_retrieval.json`,
     `part_A_near_dup_retrieval.details`, строка `receipt_01`:
     `mm_hard_cosine = 0.9346` при `mm_hard_nearest = receipt_01` (модель на
     повёрнутом дубле узнала свой оригинал) и `phash_hard_nearest =
     receipt_10` при `phash_hard_hamming = 13` (отпечаток на том же дубле
     ошибся и назвал ближайшим чужой чек; 13 из 64 бит average-hash 8×8).

  2. `case4-primery-smysl.png` — то же, но про похожесть по СМЫСЛУ, не про
     повторный скан. Числа — тот же файл, `part_C_semantic_similarity_
     agreement.details`. Сошлись: `receipt_08`/`receipt_16` (`text_gold_
     cosine = 0.7676`, `mm_cosine = 0.6827`, `mm_agrees_with_text = true`) —
     по данным корпуса (`corpus/cord_sample_meta.json`, `gt_parse.menu.nm`)
     это один напиток BLACK SAKURA одной сети в разном объёме порции:
     `[REG]` и `[LG]`. Разошлись: `receipt_00` — текстовый эталон назвал
     ближайшим `receipt_12`, картиночная модель `receipt_04` с `mm_cosine =
     0.5878`. Счёт по всем 30: совпали 8, разошлись 22 (посчитано по
     `mm_agrees_with_text` прямо в этом скрипте, чтобы число на кадре не
     разошлось с файлом).

  3. `case4-granitsy-vhod.png` — границы по входу: один и тот же скан
     `receipt_01` в трёх видах, каждый отрисован ровно так, как уходил в
     модель. Числа — `stend/raw/case4_quality_limits.json`, ось `compression`
     и ось `resolution`, задача `hard_dup`, движок `api`. Опора
     `300x450_q80_blur0`: `mean_b64_chars = 21546.3`, `n_correct = 29` из 30.
     `300x450_q25`: `mean_b64_chars = 9182.9` (43% опоры), `n_correct = 22`.
     `150x225_q80`: `mean_b64_chars = 7691.9` (36% опоры), `n_correct = 11`.
     Вес — СРЕДНЕЕ по 30 сканам (так он и мерился), и на кадре это сказано;
     сам кадр — один из тридцати. Доли взяты из того же столбца, что и счёт
     попаданий (жёсткий дубль), чтобы вес и результат относились к одному и
     тому же прогону.

Все три кадра третьей фигуры приведены к одному экранному размеру — иначе
разница читалась бы как «картинка на слайде меньше», а не как «пикселей
меньше». Уменьшенный вид увеличен обратно соседним пикселем (`Image.NEAREST`),
без досочинения деталей, и это подписано на самой фигуре.

Запуск: `python3 compose_case4_cord_examples.py` (из `rendered/`).
"""
import base64
import io
import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path

from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))
from fig_toolkit import (  # noqa: E402
    DEEP, GOLD, GREY_FILL, LIGHT, MUTE, RED, SURF, TEAL, W,
    box, clabel, f, head, report, save,
)

HERE = Path(__file__).resolve().parent
STEND = HERE.parent / "stend"
MEASURE = STEND / "measure"
CORPUS = STEND / "corpus" / "cord_sample"
RAW = STEND / "raw"


@contextmanager
def _measure_cwd():
    """`case4_full_retrieval_30.py` и `case4_quality_limits.py` читают корпус
    относительным путём (`../corpus/...`) прямо на уровне модуля — импорт
    поэтому идёт из их собственной папки. Сети при импорте ни один не трогает:
    вызовы модели живут внутри функций, которые здесь не зовутся."""
    old = os.getcwd()
    os.chdir(MEASURE)
    sys.path.insert(0, str(MEASURE))
    try:
        yield
    finally:
        sys.path.remove(str(MEASURE))
        os.chdir(old)


with _measure_cwd():
    import case4_full_retrieval_30 as M30     # noqa: E402
    import case4_quality_limits as MQL        # noqa: E402

FULL = json.loads((RAW / "case4_mm_full_retrieval.json").read_text())
LIMITS = json.loads((RAW / "case4_quality_limits.json").read_text())
META = {s["id"]: s for s in json.loads((STEND / "corpus" / "cord_sample_meta.json").read_text())}
NEAR = {r["id"]: r for r in FULL["part_A_near_dup_retrieval"]["details"]}
SEM = {r["id"]: r for r in FULL["part_C_semantic_similarity_agreement"]["details"]}


def scan(sid):
    return str(CORPUS / f"{sid}.jpg")


def pil_of(data_url):
    return Image.open(io.BytesIO(base64.b64decode(data_url.split(",", 1)[1]))).convert("RGB")


def ru(x, nd=3):
    """Число по-русски: запятая, без научной записи (канон «Форма подачи слайда»)."""
    return f"{x:.{nd}f}".replace(".", ",")


def thousands(n):
    return f"{int(round(n)):,}".replace(",", " ")


def znakov(n):
    """«9 183 знака», а не «9 183 знаков»: число на кадре читают вслух."""
    n = int(round(n))
    t = n % 100
    if 11 <= t <= 14:
        return f"{thousands(n)} знаков"
    last = n % 10
    if last == 1:
        return f"{thousands(n)} знак"
    if last in (2, 3, 4):
        return f"{thousands(n)} знака"
    return f"{thousands(n)} знаков"


def place(im, d, pic, x, y, w, h, color, resample=Image.LANCZOS):
    """Настоящий скан на холст: вписывается в заданный прямоугольник, рамка
    рисуется СНАРУЖИ картинки, чтобы не закрасить её собственные пиксели."""
    if pic.size != (w, h):
        pic = pic.resize((w, h), resample)
    im.paste(pic, (int(x), int(y)))
    d.rectangle([x - 3, y - 3, x + w + 2, y + h + 2], outline=color, width=4)


def caption(d, cx, y, lines, col, limit, sz_=17):
    for i, ln in enumerate(lines):
        clabel(d, cx, y + i * (sz_ + 7), ln, sz_, col, b=(i == 0),
               where="подпись кадра", limit=limit)


# ── Фигура 2 — «case4-primery-dubli.png» ────────────────────────────────────
# Что показывает: один и тот же чек, пересканированный и снятый под углом, и
# чужой чек рядом как мера «насколько далеко вообще бывает». Разбор, который
# обязан читаться с кадра: на снятом под углом дубле модель держится, а
# отпечаток ломается — и ломается не «чуть хуже», а называет ближайшим чужой
# документ, который тут же и показан четвёртым кадром.
FIG2_W, FIG2_H = 1860, 812


def primery_dubli():
    im = Image.new("RGB", (FIG2_W, FIG2_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Повторный скан того же чека: что узнаёт модель и что узнаёт отпечаток", sz=28)
    d.text((40, 64), "все четыре кадра — настоящие сканы корпуса ровно в том виде, в каком они",
           font=f(20), fill=LIGHT)
    d.text((40, 90), "уходили в модель: 300×450 точек, JPEG", font=f(20), fill=LIGHT)

    src = scan("receipt_01")
    frames = [
        (pil_of(M30.to_data_url(src)), TEAL,
         ["Оригинал", "receipt_01 — лежит в индексе"]),
        (pil_of(M30.soft_dup(src)), LIGHT,
         ["Пересканировали", "тот же чек, пережат заново"]),
        (pil_of(M30.hard_dup(src)), GOLD,
         ["Сняли под углом", "поворот 12°, края обрезаны"]),
        (pil_of(M30.to_data_url(scan("receipt_10"))), RED,
         ["Чужой чек", "receipt_10 — другой документ"]),
    ]

    iw, ih = 280, 420
    n = len(frames)
    gap = 30
    col_w = (FIG2_W - 80 - gap * (n - 1)) / n
    y_img = 128
    for i, (pic, col, caps) in enumerate(frames):
        cx = 40 + i * (col_w + gap) + col_w / 2
        place(im, d, pic, cx - iw / 2, y_img, iw, ih, col)
        caption(d, cx, y_img + ih + 16, caps, DEEP, col_w)

    y_anchor = y_img + ih + 86
    clabel(d, FIG2_W / 2, y_anchor,
           "Кого каждый метод назвал ближайшим для третьего кадра — снятого под углом",
           20, DEEP, b=True, where="якорь плашек", limit=FIG2_W - 80)

    yp, hp, gp = y_anchor + 40, 112, 40
    pw = (FIG2_W - 80 - gp) / 2
    box(d, 40, yp, pw, hp,
        ["Модель назвала свой оригинал", "сходство 0,935 — ближайший из 30"],
        SURF, tc=DEEP, sz=21, outline=TEAL, where="плашка · модель")
    box(d, 40 + pw + gp, yp, pw, hp,
        ["Отпечаток назвал чужой чек", "13 бит расхождения из 64"],
        SURF, tc=DEEP, sz=21, outline=RED, where="плашка · отпечаток")

    save(im, "case4-primery-dubli.png")


# ── Фигура 3 — «case4-primery-smysl.png» ────────────────────────────────────
# Что показывает: похожесть по СМЫСЛУ — другая задача, чем «тот же документ
# ещё раз». Слева пара, на которой текстовый эталон и картиночная модель
# назвали друг друга; справа случай, где они назвали разных, и это не
# исключение, а большинство: 22 из 30.
FIG3_W, FIG3_H = 1900, 820


def primery_smysl():
    im = Image.new("RGB", (FIG3_W, FIG3_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Похожесть по смыслу: где картиночная модель и текст сошлись, а где разошлись", sz=28)
    d.text((40, 64), "эталон — ближайший чек по распознанному тексту; рядом — кого на том же",
           font=f(20), fill=LIGHT)
    d.text((40, 90), "месте назвала картиночная модель", font=f(20), fill=LIGHT)

    iw, ih = 280, 420
    gap_in, gap_between = 26, 100
    g1 = [
        ("receipt_08", TEAL, ["receipt_08", "BLACK SAKURA, обычная порция"]),
        ("receipt_16", TEAL, ["receipt_16", "BLACK SAKURA, большая порция"]),
    ]
    g2 = [
        ("receipt_00", GOLD, ["receipt_00 — запрос", "билет"]),
        ("receipt_12", MUTE, ["текст назвал этот", "receipt_12 — блузка и пакет"]),
        ("receipt_04", MUTE, ["модель назвала этот", "receipt_04 — кофе и котлета"]),
    ]
    w1 = len(g1) * iw + (len(g1) - 1) * gap_in
    w2 = len(g2) * iw + (len(g2) - 1) * gap_in
    x0 = (FIG3_W - (w1 + gap_between + w2)) / 2
    x2 = x0 + w1 + gap_between

    y_head, y_img = 126, 162
    clabel(d, x0 + w1 / 2, y_head, "Сошлись", 22, TEAL, b=True,
           where="заголовок · сошлись", limit=w1)
    clabel(d, x2 + w2 / 2, y_head, "Разошлись", 22, RED, b=True,
           where="заголовок · разошлись", limit=w2)

    for grp, xg in ((g1, x0), (g2, x2)):
        for i, (sid, col, caps) in enumerate(grp):
            x = xg + i * (iw + gap_in)
            place(im, d, pil_of(M30.to_data_url(scan(sid))), x, y_img, iw, ih, col)
            caption(d, x + iw / 2, y_img + ih + 14, caps, DEEP, iw + gap_in)

    sep_x = x0 + w1 + gap_between / 2
    d.line([sep_x, y_head - 14, sep_x, y_img + ih + 64], fill=GREY_FILL, width=4)

    agree = sum(1 for r in SEM.values() if r["mm_agrees_with_text"])
    total = len(SEM)
    yp, hp = y_img + ih + 94, 110
    box(d, x0, yp, w1, hp,
        ["Оба назвали эту пару",
         f"сходство: текст {ru(SEM['receipt_08']['text_gold_cosine'])} · "
         f"картинка {ru(SEM['receipt_08']['mm_cosine'])}"],
        SURF, tc=DEEP, sz=20, outline=TEAL, where="плашка · сошлись")
    box(d, x2, yp, w2, hp,
        [f"Разошлись у {total - agree} чеков из {total} — сошлись только {agree}",
         f"сходство по картинке на своём ближайшем: {ru(SEM['receipt_00']['mm_cosine'])}"],
        SURF, tc=DEEP, sz=20, outline=RED, where="плашка · разошлись")

    save(im, "case4-primery-smysl.png")


# ── Фигура 4 — «case4-granitsy-vhod.png» ────────────────────────────────────
# Что показывает: где у входа граница. Три вида одного скана, каждый — ровно
# та строка запроса, которую получала модель; под каждым вес этой строки с
# долей от опорного и счёт попаданий из тридцати. Вывод читается сравнением
# второго кадра с третьим: второй легче опоры почти так же сильно, как
# третий, а держится заметно лучше — значит платят не весом, а пикселями.
FIG4_W, FIG4_H = 1860, 806


def granitsy_vhod():
    im = Image.new("RGB", (FIG4_W, FIG4_H), W)
    d = ImageDraw.Draw(im)
    head(d, "Вес файла сжимать можно, пиксели убирать нельзя", sz=28)
    d.text((40, 64), "один и тот же скан, снятый под углом, — ровно в том виде, в каком он уходил",
           font=f(20), fill=LIGHT)
    d.text((40, 90), "в модель; все три кадра приведены к одному экранному размеру",
           font=f(20), fill=LIGHT)

    api = {}
    for axis in ("compression", "resolution"):
        api.update(LIMITS["axes"][axis]["tasks"]["hard_dup"]["engines"]["api"]["points"])
    anchor = api["300x450_q80_blur0"]

    src = scan("receipt_01")
    cols = [
        ("300x450_q80_blur0", 300, 450, 80, TEAL,
         ["300×450 точек, качество 80", "опорный вид"]),
        ("300x450_q25", 300, 450, 25, GOLD,
         ["300×450 точек, качество 25", "те же точки, сильнее сжат"]),
        ("150x225_q80", 150, 225, 80, RED,
         ["150×225 точек, качество 80", "вчетверо меньше точек"]),
    ]

    iw, ih = 280, 420
    gap = 40
    col_w = (FIG4_W - 80 - gap * 2) / 3
    y_img = 128
    for i, (key, w_, h_, q_, col, caps) in enumerate(cols):
        pic = MQL.pil_of(MQL.hard_dup(src, w=w_, h=h_, q=q_, blur=0.0))
        cx = 40 + i * (col_w + gap) + col_w / 2
        place(im, d, pic, cx - iw / 2, y_img, iw, ih, col,
              resample=Image.NEAREST if (w_, h_) != (300, 450) else Image.LANCZOS)
        caption(d, cx, y_img + ih + 14, caps, DEEP, col_w)

        p = api[key]
        share = p["b64_chars_share_of_anchor"]
        lost = anchor["n_correct"] - p["n_correct"]
        lines = [f"Вес: {znakov(p['mean_b64_chars'])}" + ("" if share == 1.0
                                                          else f" — {share:.0%} опоры"),
                 f"Нашёл свой оригинал: {p['n_correct']} из {p['n_scans']}"]
        if lost:
            lines.append(f"на {lost} меньше опорных {anchor['n_correct']}")
        box(d, cx - col_w / 2, y_img + ih + 76, col_w, 112, lines,
            SURF, tc=DEEP, sz=20, outline=col, where=f"плашка {i + 1}")

    d.text((40, FIG4_H - 62),
           "Вес — средняя длина строки запроса по всем 30 сканам; на кадре один из них.",
           font=f(17), fill=MUTE)
    d.text((40, FIG4_H - 38),
           "Уменьшенный кадр увеличен обратно соседним пикселем, без досочинения деталей. "
           "Индекс во всех трёх прогонах лежит в опорном виде — меняется только запрос.",
           font=f(17), fill=MUTE)

    save(im, "case4-granitsy-vhod.png")


if __name__ == "__main__":
    primery_dubli()
    primery_smysl()
    granitsy_vhod()
    report()
