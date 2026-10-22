#!/usr/bin/env python3
"""Волна 2б «конфетки» Семинара 8 (issue #292) — две СВЕДЁННЫЕ фигуры Кейса 1.

План `qa/PLAN-KONFETKA-INSTRUKTSII-2026-10-22.md` §4.8 сводит по две пары
слайдов Кейса 1 в один экран каждую: n11 + n11a («Версия с моделью на стенде»)
и n14 + n14a («Версия с шаблоном на стенде»). На каждом сведённом экране обязан
поместиться и общий кадр холста, и панель настройки узла, — то есть фигура
теперь одна, а показать должна то, что раньше показывали две.

    k1-stend-versiya1-real.png  холст воркфлоу «Кейс 1 (до)», под ним поле
                                 `Prompt (User Message)` узла `Compose
                                 notification (LLM)` и два его переключателя
    k1-stend-versiya2-real.png  холст воркфлоу «Кейс 1 (после)», под ним поле
                                 `notification_text` узла `Compose
                                 notification (template)` и переключатель
                                 «Include Other Input Fields»

── Чем здесь связаны руки, и почему раскладка именно такая ──────────────────

Полоса содержания слайда — 12,23″ × 5,90″ (`deck_config.py`: WIDTH, BOTTOM
минус заголовок), пропорция 2,07. Фигура с пропорцией НИЖЕ 1,66 не может занять
80% ширины и ловит предупреждение `СХЕМА ЗАЖАТА` (`deck_kit.figure`:
FIG_MIN_FILL). Одновременно §3.6 плана держит пол кегля 7,5 pt на скринах.
Эти два требования тянут в разные стороны, и свести их удалось не сразу —
замеры всех проб, чтобы следующая волна не повторяла их заново:

    холст + панель ОДНА ПОД ДРУГОЙ, обе во всю ширину   → 1,41 · холст 5,6 pt ✗
    то же, с полосами подписей в одну строку            → 1,50 · холст 5,6 pt ✗
    холст и панель РЯДОМ, по высоте вровень             → 5,14 · холст 5,0 pt ✗
    холст сверху + РЯД из двух панелей, полосы подписей → 1,78 · холст 7,7 pt ~
    холст сверху + РЯД из двух панелей, БЕЗ подписей    → 2,01 · холст 7,5 pt ✓

Решающим оказался отказ от полос подписей над кропами. Полоса стоит 40–90 px
высоты каждая, то есть прямо съедает пропорцию, — а работу свою здесь не
делает: в отличие от панельных композитов волны 1а (где кроп показывает
безымянное поле ввода), ЭТИ кропы режутся по границе, внутри которой интерфейс
n8n подписывает себя сам: «Prompt (User Message)», «notification_text»,
«Require Specific Output Format», «Include Other Input Fields». Рисовать над
ними вторую подпись значило бы повторить словами то, что уже написано на
кадре, — ровно то удвоение, которое §3.7 плана запрещает на слайде.

Высота нижнего ряда задана (`ROW2_H`), а ширина левой колонки из неё
ВЫЧИСЛЯЕТСЯ: у двух версий поля настройки разной формы (у версии 1 поле
промпта вытянуто вширь, у версии 2 выражение с именем и типом — вглубь), и
при равном делении пополам версия 2 давала пропорцию 1,80 и холст 6,7 pt.
Подбор ширины под общую высоту ряда выравнивает обе версии на 2,01.

ЧТО НЕ ТРОГАЕТСЯ. Фигуры волн 1а и 1б (`make_figures_crops.py`) этим файлом не
пересобираются — он только ЧИТАЕТ те же исходники `stend/n8n-screenshots-raw/`
и пишет два НОВЫХ имени. Прежние `k1-n8n-versiya1-real.png`,
`k1-n8n-versiya2-real.png`, `k1-n8n-versiya1-nastroyka-llm.png`,
`k1-n8n-versiya2-nastroyka-template.png` остаются на диске: на них стоят
EN-слайды до волны 6, и они же — запасной показ.

Прямоугольник холста — K1_BOX волны 1б, (288, 248, 1660, 648), ПОВТОРЁН здесь
числом, а не импортирован: импорт `make_figures_crops` выполнил бы его целиком
и переписал все восемь фигур той волны. Если K1_BOX там когда-нибудь
изменится, этот файл надо поправить вручную — цена названа, а не спрятана.

Запуск: `python3 make_figures_w2b.py` (из `rendered/`).
"""
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
RAW = HERE.parent / "stend" / "n8n-screenshots-raw"
OUT = HERE / "figures"

DEEP = (0x21, 0x29, 0x5C)
LIGHT = (0x1C, 0x72, 0x93)
W = (255, 255, 255)

BAND_IN = 12.23          # ширина полосы контента слайда (deck_config.WIDTH)
BAND_H_IN = 5.90         # высота полосы под фигурой БЕЗ текстовых блоков
KEGL_FLOOR_PT = 7.5      # пол кегля на скринах (план §3.6)

GAP = 28
ROW2_H = 255             # высота нижнего ряда, px (см. шапку)

# Холст Кейса 1 — тот же прямоугольник, что у волны 1б (см. шапку).
K1_BOX = (288, 248, 1660, 648)

# Панели настройки. Прямоугольники взяты по самим скринам 1900×1100; каждый
# режется так, чтобы в кадр попала СОБСТВЕННАЯ подпись поля из интерфейса.
V1_PROMPT = (753, 236, 1148, 383)     # «Prompt (User Message)» + поле целиком
V1_TOGGLES = (750, 390, 1150, 512)    # оба переключателя, оба выключены
V2_FIELD = (772, 236, 1160, 414)      # `notification_text` · String · выражение
V2_INCLUDE = (750, 505, 1150, 627)    # «Include Other Input Fields» = All


def framed(im, box_w, box_h):
    """Кроп в тиловой рамке, вписанный по центру в прямоугольник ряда."""
    k = box_w / im.width
    small = im.resize((box_w, round(im.height * k)), Image.LANCZOS)
    out = Image.new("RGB", (box_w, box_h), W)
    y = (box_h - small.height) // 2
    out.paste(small, (0, y))
    ImageDraw.Draw(out).rectangle(
        [0, y, box_w - 1, y + small.height - 1], outline=LIGHT, width=2)
    return out


def stend_composite(canvas_src, panel_src, left_box, right_box):
    """Холст и панель — РАЗНЫЕ скрины одного воркфлоу: `case1-before.png` снят
    на холсте, `case1-before-compose.png` — с открытой двойным щелчком панелью
    узла. Отсюда два исходника, а не один."""
    raw = Image.open(RAW / canvas_src).convert("RGB")
    pan = Image.open(RAW / panel_src).convert("RGB")
    canvas = raw.crop(K1_BOX)
    cw = canvas.width

    lsrc, rsrc = pan.crop(left_box), pan.crop(right_box)
    # Ширина левой колонки — та, при которой её высота равна высоте ряда.
    lw = min(round(ROW2_H * lsrc.width / lsrc.height), cw - GAP - 200)
    rw = cw - GAP - lw

    out = Image.new("RGB", (cw, canvas.height + GAP + ROW2_H), W)
    out.paste(canvas, (0, 0))
    ImageDraw.Draw(out).rectangle(
        [0, 0, cw - 1, canvas.height - 1], outline=DEEP, width=2)
    out.paste(framed(lsrc, lw, ROW2_H), (0, canvas.height + GAP))
    out.paste(framed(rsrc, rw, ROW2_H), (lw + GAP, canvas.height + GAP))
    return out, canvas.size, (lsrc.size, lw), (rsrc.size, rw)


def report(name, im, canvas_px, left, right):
    """Пропорция и кегль интерфейса на слайде — числом, а не на глаз.

    Кегль считается для трёх размеров текста интерфейса n8n: 12 px — серые
    подподписи узлов («manual», «sendMessage: message»), 14 px — подписи полей
    в панели, 17 px — имена узлов на холсте и значения полей."""
    ar = im.width / im.height
    w_in = min(BAND_IN, BAND_H_IN * ar)
    fill = w_in / BAND_IN
    print(f"  {name}  {im.size}  пропорция {ar:.2f}  "
          f"на слайде {w_in:.2f}″ ({fill:.0%} полосы"
          f"{'' if fill >= 0.80 else ' — НИЖЕ ПОРОГА 80%'})")
    for label, src_w, fig_w in (("холст", canvas_px[0], im.width),
                                ("панель слева", left[0][0], left[1]),
                                ("панель справа", right[0][0], right[1])):
        pt = w_in * fig_w / im.width * 72 / src_w
        flag = "" if 12 * pt >= KEGL_FLOOR_PT - 0.05 else "  ← 12 px ниже пола 7,5 pt"
        print(f"     кегль [{label}]: 12 px = {12 * pt:.1f} pt, "
              f"14 px = {14 * pt:.1f} pt, 17 px = {17 * pt:.1f} pt{flag}")


for _name, _canvas, _panel, _l, _r in (
    ("k1-stend-versiya1-real.png", "case1-before.png",
     "case1-before-compose.png", V1_PROMPT, V1_TOGGLES),
    ("k1-stend-versiya2-real.png", "case1-after.png",
     "case1-after-compose.png", V2_FIELD, V2_INCLUDE),
):
    _im, _cpx, _left, _right = stend_composite(_canvas, _panel, _l, _r)
    _im.save(OUT / _name)
    report(_name, _im, _cpx, _left, _right)


# ── Сцена Кейса 1 (n06): цепочка, которая уже работала ──────────────────────
#
# План §4.7 требует на сцене НАСТОЯЩИЙ кадр, а не пересказ. Главная забота
# здесь не в кропе, а в том, чего на кадре быть НЕ ДОЛЖНО: следующий экран
# (n07) спрашивает зал, как собрать уведомление из трёх значений, и голосует
# карточками. Любой кадр, на котором виден узел композиции — «Compose
# notification (LLM)» у версии 1 или «(template)» у версии 2, — выдаёт ответ
# за экран до вопроса.
#
# Поэтому: исходник `case1-after.png` (у версии 2 узел экрана результата
# подписан просто `Result screen`, тогда как у версии 1 на том же месте стоит
# `Result screen Model (notification)` — само имя подписи уже называет модель),
# и прямоугольник (300, 425, 1420, 650) — НИЖНЯЯ диагональ холста: `Request
# form` → `Extract fields` → `Vocabulary check` → `Write row` → `Result
# screen`. Ровно те пять узлов, которые заработали на прошлом занятии и с
# которыми Ольга живёт каждый день. Узлы композиции и отправки лежат выше
# y=358 исходника и в кадр не попадают вовсе; от ветки к ним в кадре остаётся
# только серый хвост стрелки, уходящий за верхний край, — он настоящий, и
# закрашивать его было бы подделкой кадра ради удобства.
S7_BOX = (300, 425, 1420, 650)

_s7 = Image.open(RAW / "case1-after.png").convert("RGB").crop(S7_BOX)
_out = Image.new("RGB", _s7.size, W)
_out.paste(_s7, (0, 0))
ImageDraw.Draw(_out).rectangle(
    [0, 0, _s7.width - 1, _s7.height - 1], outline=DEEP, width=2)
_out.save(OUT / "k1-stend-s7-tsepochka-real.png")
_ar = _out.width / _out.height
_w_in = min(BAND_IN, BAND_H_IN * _ar)
_pt = _w_in * 72 / _out.width
print(f"  k1-stend-s7-tsepochka-real.png  {_out.size}  пропорция {_ar:.2f}  "
      f"на слайде {_w_in:.2f}″")
print(f"     кегль [холст]: 12 px = {12 * _pt:.1f} pt, "
      f"17 px = {17 * _pt:.1f} pt")

print("\nволна 2б: собраны 3 новые фигуры Кейса 1. "
      "Фигуры волн 1а/1б не трогались.")
