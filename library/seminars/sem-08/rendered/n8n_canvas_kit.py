"""n8n-стилизованный примитив для схем «слой 2» Семинара 8 (issue #274).

**Зачем это отдельный модуль.** Живой скрин интерфейса n8n для стенда занятия
технически недостижим в этой рабочей среде — headless-браузер не поднять
(нет системных библиотек, root недоступен), см. `notes/mcp-limitations.md`
[#233-8] и врезку «Про слой 2» в `SETKA-KEYSOV-S8.md`. Решение владельца —
окончательное: вместо скрина — максимально точная ПРОГРАММНО нарисованная
схема, имитирующая визуальный язык n8n (прямоугольники-узлы со скруглёнными
углами, стрелки-связи слева-направо), с настоящими именами узлов и
настоящими значениями параметров из `stend/*.json` (см. `BRIEF-PROIZVODSTVO.md`
§3). Это не мок — мок-данных здесь нет вовсе; это честная замена снимка,
подписанная как таковая на каждой фигуре.

**Узел n8n (`node_n8n`).** Скруглённый прямоугольник: крупный заголовок —
ИМЯ УЗЛА, как оно стоит на холсте n8n («Compose notification (LLM)»,
«Amount over threshold?»); под ним опционально мелкая строка типа узла
(`chainLlm`, `IF`, `Set`…); под ней — 1-3 строки мелким текстом реального
параметра, выражения или промпта (длинный промпт сокращается до ключевой
фразы с «…» — сокращает вызывающий код, не эта функция). Слева и справа —
два маленьких кружка-порта, как коннекторы на настоящем холсте.

**Четыре вида узла (`kind=`) — разным цветом заливки, строго из палитры
Ocean курса** (`fig_toolkit.py`), без единого цвета мимо неё:

    trigger   форма / webhook / триггер         SURF-заливка, контур TEAL
    model     LLM / модель (`chainLlm` и т.п.)   WARM-заливка, контур GOLD
    code      `Set` / `IF` / код / условие       PALE-заливка, контур MID
    external  Telegram / `HTTP Request` / API    W-заливка,    контур DEEP

**Стрелка (`arrow_n8n`)** — тонкая обёртка над `fig_toolkit.arrow`: соединяет
правый порт одного узла с левым портом следующего на общей оси `y`.

**Врезка результата (`callout`)** — не узел n8n, а карточка-результат
(текст прогона, найденная ошибка, итог сравнения), трёх тонов: `ok` (всё
сошлось), `warn` (неоднозначность/находка), `bad` (настоящая ошибка).

Это НЕ попытка повторить n8n пиксель-в-пиксель — композиция и детализация
ровно того уровня, что нужен залу для разбора конфигурации узла, не для
узнавания точной версии интерфейса.

Подключение — прямым `import` из скрипта-рисовалки, который уже сделал
`sys.path.insert` на `tools/seminar-build` для `fig_toolkit` (тот же
паттерн, что в `make_figures_c3.py`); `n8n_canvas_kit.py` лежит рядом со
скриптами в `rendered/`, отдельного пути искать не нужно:

    from fig_toolkit import *
    from n8n_canvas_kit import *
"""
from fig_toolkit import *

KIND_STYLE = {
    "trigger":  dict(fill=SURF, outline=TEAL, title=DEEP,    tag="форма / триггер"),
    "model":    dict(fill=WARM, outline=GOLD, title=GOLDINK, tag="модель (LLM)"),
    "code":     dict(fill=PALE, outline=MID,  title=DEEP,    tag="код / условие"),
    "external": dict(fill=W,    outline=DEEP, title=DEEP,    tag="внешний сервис"),
}

TONE_STYLE = {
    "ok":   dict(fill=SURF, outline=TEAL, title=MID,  body=MUTE),
    "warn": dict(fill=WARM, outline=GOLD, title=GOLDINK, body=GOLDINK),
    "bad":  dict(fill=W,    outline=RED,  title=RED,  body=MUTE),
}

N8N_DISCLAIMER = ("Программно нарисованная схема в духе n8n — холст недостижим в этой среде "
                  "([#233-8]); имена узлов и значения — настоящие, со стенда.")


def node_n8n(d, x, y, w, h, title, body=None, kind="code", *, subtype=None,
             title_sz=21, sub_sz=14, body_sz=14, body_col=MUTE, pad=16, r=14,
             port=7, where=None):
    """Один узел n8n: заголовок + опциональный тип + 1-3 строки параметра.

    `body` — строка (переносится по словам автоматически) ИЛИ список готовых
    строк (каждая тоже проверяется на ширину и при необходимости переносится
    ещё раз). Длинный промпт сокращай до ключевой фразы с «…» ДО вызова —
    сама функция текст не укорачивает, только переносит и меряет.
    """
    st = KIND_STYLE[kind]
    where = where or title
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=st["fill"],
                        outline=st["outline"], width=4)
    cy = y + h / 2
    d.ellipse([x - port, cy - port, x + port, cy + port], fill=st["outline"])
    d.ellipse([x + w - port, cy - port, x + w + port, cy + port], fill=st["outline"])

    pad_w = w - 2 * pad
    tfo = f(title_sz, True)
    tlines = wrap(d, title, tfo, pad_w)
    for ln in tlines:
        fit(d, ln, tfo, pad_w, f"{where} · заголовок")

    slines = []
    sfo = f(sub_sz, True)
    if subtype:
        slines = wrap(d, subtype, sfo, pad_w)
        for ln in slines:
            fit(d, ln, sfo, pad_w, f"{where} · тип узла")

    blines = []
    bfo = f(body_sz, False)
    if body:
        raw = [body] if isinstance(body, str) else list(body)
        for piece in raw:
            blines.extend(wrap(d, piece, bfo, pad_w))
        for ln in blines:
            fit(d, ln, bfo, pad_w, f"{where} · параметр")

    tlh, slh, blh = title_sz + 7, sub_sz + 6, body_sz + 7
    total_h = len(tlines) * tlh
    if slines:
        total_h += 5 + len(slines) * slh
    if blines:
        total_h += 7 + len(blines) * blh

    yy = y + (h - total_h) / 2
    for ln in tlines:
        d.text((x + (w - d.textlength(ln, font=tfo)) / 2, yy), ln, font=tfo, fill=st["title"])
        yy += tlh
    if slines:
        yy += 5
        for ln in slines:
            d.text((x + (w - d.textlength(ln, font=sfo)) / 2, yy), ln, font=sfo, fill=MUTE)
            yy += slh
    if blines:
        yy += 7
        for ln in blines:
            d.text((x + (w - d.textlength(ln, font=bfo)) / 2, yy), ln, font=bfo, fill=body_col)
            yy += blh


def arrow_n8n(d, x_from, x_to, y, col=MID, wd=4, dash=False):
    """Стрелка порт→порт: от правого порта одного узла до левого порта
    следующего, на общей оси `y`, какую приняли оба узла."""
    arrow(d, x_from, y, x_to, y, col=col, wd=wd, dash=dash)


def callout(d, x, y, w, h, title, body=None, tone="ok", *, title_sz=18,
            body_sz=15, pad=16, r=12, where=None):
    """Карточка-результат (не узел n8n): текст прогона, находка, итог. Тон —
    `ok` / `warn` / `bad`, цвета строго из `TONE_STYLE` (та же палитра
    Ocean, что и у узлов)."""
    st = TONE_STYLE[tone]
    where = where or title
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=st["fill"],
                        outline=st["outline"], width=4)
    pad_w = w - 2 * pad
    tfo = f(title_sz, True)
    tlines = wrap(d, title, tfo, pad_w)
    for ln in tlines:
        fit(d, ln, tfo, pad_w, f"{where} · заголовок")
    blines = []
    bfo = f(body_sz, False)
    if body:
        raw = [body] if isinstance(body, str) else list(body)
        for piece in raw:
            blines.extend(wrap(d, piece, bfo, pad_w))
        for ln in blines:
            fit(d, ln, bfo, pad_w, f"{where} · текст")

    tlh, blh = title_sz + 7, body_sz + 7
    total_h = len(tlines) * tlh + (7 + len(blines) * blh if blines else 0)
    yy = y + (h - total_h) / 2
    for ln in tlines:
        d.text((x + (w - d.textlength(ln, font=tfo)) / 2, yy), ln, font=tfo, fill=st["title"])
        yy += tlh
    if blines:
        yy += 7
        for ln in blines:
            d.text((x + (w - d.textlength(ln, font=bfo)) / 2, yy), ln, font=bfo, fill=st["body"])
            yy += blh


def legend_n8n(d, x, y, kinds=("trigger", "model", "code", "external"), sz=16, gap=230):
    """Компактная расшифровка цвета узла — печатается один раз, внизу схемы."""
    cx = x
    for k in kinds:
        st = KIND_STYLE[k]
        d.rounded_rectangle([cx, y, cx + 32, y + 20], radius=6, fill=st["fill"],
                            outline=st["outline"], width=3)
        d.text((cx + 42, y + 1), st["tag"], font=f(sz), fill=MUTE)
        cx += gap


def disclaimer(d, cx, y, w=1500):
    clabel(d, cx, y, N8N_DISCLAIMER, 16, MUTE, where="n8n-дисклеймер", limit=w)
