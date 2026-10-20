#!/usr/bin/env python3
"""Кейс «Проверка на повтор» Семинара 8 (issue #274) — 4 схемы.

    k2-shema-gibrid.png        слой 1, АРХИТЕКТУРНАЯ схема кейса (переделана
                               ВТОРОЙ РАЗ 2026-10-20, тем же днём: первая
                               переделка подавала гибрид как рекомендацию по
                               одному измерению — к вечеру того же дня
                               владелец явно подтвердил голосом, что хотел
                               перехода на гибрид хэш+jev как РЕАЛЬНО
                               СОБРАННОЕ решение, не как гипотезу; оркестратор
                               в тот же день перестроил живой n8n-стенд через
                               API — см. n21.md фронтматтер за полной записью
                               обеих правок): два шага гибрида — дешёвый
                               механический предфильтр (хэш, 15/20 литеральных
                               совпадений бесплатно) → проверка смыслом,
                               РЕШЕНИЕ — специализированный сервис (jev,
                               20/20) вместо модели общего назначения (17/20).
                               Честная оговорка на фигуре теперь не про «ещё
                               не поменяли архитектуру», а про то, что
                               обобщаемость за пределы этого набора (один
                               язык, одна тематика) не проверена.
    k2-n8n-mehanika.png        программная версия слоя 2 (n8n-стиль), ЗАМЕНЕНА
                               на слайде n22 реальным скрином
                               (k2-n8n-mehanika-real.png) 2026-10-20; файл
                               оставлен на диске нетронутым для истории, слайд
                               на него больше не ссылается. `Set` «Normalize +
                               hash» → `IF` «Exact duplicate in window?» → два
                               исхода — эта механика не менялась ни на одной
                               из двух переделок архитектуры.
    k2-n8n-llm-provexa.png     программная версия слоя 2 (n8n-стиль) для
                               ДОРОГОГО шага версии с моделью-судьёй —
                               слайд n23 больше не использует эту схему: узел
                               модели-судьи реально удалён со стенда и заменён
                               узлом jev (см. n23.md). Файл оставлен на диске
                               нетронутым как запись устройства прежней
                               версии цепочки, не как актуальный источник.
    k2-n8n-test-stend-real.png ДОБАВЛЕНО 2026-10-20 (issue #274), владелец:
                               «ты сам смотрел на скрины? в последнем разделе
                               почти нет, в остальных тоже мало. пересмотри и
                               добавь». Слайд n20 (таблица сравнения 4 схем)
                               был ПОЛНОСТЬЮ текстовым — ни одного скрина.
                               Фигура — настоящий кроп живого n8n-стенда,
                               воркфлоу «C8 · Кейс 2 — тест дедупликации
                               (стенд, 4 схемы)», тот самый тестовый процесс,
                               на котором измерены числа, уже стоящие в
                               таблице n20. ПОДТВЕРЖДАЮЩАЯ, не вводная —
                               рисуется ПОСЛЕ таблицы и честной находки
                               (`fig_after` в deck-config.yaml, тот же приём,
                               что у n31). Источник и построение — см.
                               `test_stend_real()` ниже и backup n20.md.

Числа и формулировки — дословно `SETKA-KEYSOV-S8.md` «Кейс 2 — Проверка на
повтор» (таблица четырёх схем) и `BRIEF-PROIZVODSTVO.md` §3; измерение jev —
`stend/duplicate-check-results.json` → `jev_measured`. Слой 1 (эта схема)
остаётся программной архитектурной иллюстрацией, не снимком UI — слой 2
(n22/n23) теперь использует настоящие скрины живого стенда, см. их
фронтматтер.

Запуск: `python3 make_figures_k2.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, legend_n8n, disclaimer

CW = 1600


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


# ── слой 1: решённая архитектура — хэш первым, jev на оставшееся ───────────
def gibrid():
    CH = 600
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Решение: хэш первым, jev — на дорогом шаге",
         sz=24, x=40, y=16)

    BOX_Y, BOX_H = 150, 250

    # Шаг 1 — дешёвый механический предфильтр
    ax, aw = 60, 600
    frame(d, ax, BOX_Y, aw, BOX_H, fill=PALE, stroke=MID, sw=4)
    yy = BOX_Y + 26
    for ln in wrap(d, "Шаг 1 — дешёвый механический предфильтр", f(20, True), aw - 48):
        fit(d, ln, f(20, True), aw - 48, "шаг 1 · заголовок")
        clabel(d, ax + aw / 2, yy, ln, 20, DEEP, True, where="шаг 1 · заголовок", limit=aw - 48)
        yy += 27
    yy += 10
    for piece in ("Берёт на себя буквальные повторы бесплатно и мгновенно, "
                  "без единого вызова модели.",
                  "На тесте (предыдущий экран): 15 из 20 — все буквальные "
                  "повторы, 0 перефразировок."):
        for ln in wrap(d, piece, f(16), aw - 48):
            fit(d, ln, f(16), aw - 48, "шаг 1 · текст")
            clabel(d, ax + aw / 2, yy, ln, 16, MUTE, where="шаг 1 · текст", limit=aw - 48)
            yy += 22
        yy += 8

    # Стрелка между шагами
    GAP = 140
    arrow(d, ax + aw, BOX_Y + BOX_H / 2, ax + aw + GAP, BOX_Y + BOX_H / 2, col=MID, wd=4)
    clabel(d, ax + aw + GAP / 2, BOX_Y + BOX_H / 2 - 40, "не разрешено", 14, MUTE,
           where="подпись стрелки 1", limit=GAP - 10)
    clabel(d, ax + aw + GAP / 2, BOX_Y + BOX_H / 2 - 22, "однозначно", 14, MUTE,
           where="подпись стрелки 2", limit=GAP - 10)

    # Шаг 2 — проверка смыслом, решение — jev
    bx, bw = ax + aw + GAP, 600
    frame(d, bx, BOX_Y, bw, BOX_H, fill=PALE, stroke=TEAL, sw=4)
    yy = BOX_Y + 26
    for ln in wrap(d, "Шаг 2 — проверка смыслом: решение — jev", f(20, True), bw - 48):
        fit(d, ln, f(20, True), bw - 48, "шаг 2 · заголовок")
        clabel(d, bx + bw / 2, yy, ln, 20, DEEP, True, where="шаг 2 · заголовок", limit=bw - 48)
        yy += 27
    yy += 10
    for piece in ("Специализированный сервис точнее универсальной модели "
                  "на этом тесте и дешевле по публичному прайсу.",
                  "На тесте: 20 из 20 — без единой ошибки, против 17 из 20 "
                  "у дешёвой модели-судьи. Узел собран и стоит на стенде."):
        for ln in wrap(d, piece, f(16), bw - 48):
            fit(d, ln, f(16), bw - 48, "шаг 2 · текст")
            clabel(d, bx + bw / 2, yy, ln, 16, MUTE, where="шаг 2 · текст", limit=bw - 48)
            yy += 22
        yy += 8

    # Честная оговорка — на самой схеме, не только в тексте слайда
    dashbox(d, 60, BOX_Y + BOX_H + 40, bx + bw - 60, 110, col=GREY_TX, width=3, r=10)
    clabel(d, CW / 2, BOX_Y + BOX_H + 62,
           "Измерение одно, на 20 парах одного языка и одной тематики (запись на курсы) —",
           17, MUTE, where="оговорка 1", limit=bw + aw + 20)
    clabel(d, CW / 2, BOX_Y + BOX_H + 86,
           "обобщаемость за пределы этого набора не проверена. Это честная граница измерения,",
           17, MUTE, where="оговорка 2", limit=bw + aw + 20)
    clabel(d, CW / 2, BOX_Y + BOX_H + 110,
           "а не повод не внедрять: цепочка на стенде дальше уже собрана именно так.",
           17, MUTE, where="оговорка 3", limit=bw + aw + 20)
    return im


save(gibrid(), "k2-shema-gibrid.png")


# ── слой 2: n8n-стиль, механика хэша + IF ───────────────────────────────────
def mehanika():
    CH = 500
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: нормализация, хэш, сравнение", sz=25, x=40, y=16)

    CY = 220
    node_n8n(d, 40, CY - 110, 560, 220,
              "Normalize + hash",
              ["normalized_hash = $('Request form').item.json['Что нужно']",
               ".toLowerCase().trim().replace(/\\s+/g, ' ')"],
              kind="code", subtype="Set", body_sz=15, where="узел нормализации")

    node_n8n(d, 700, CY - 110, 520, 220,
              "Exact duplicate in window?",
              ["условие: normalized_hash строго равен recent_same_contact_hash",
               "(строковое сравнение, оба уже в lowercase)"],
              kind="code", subtype="IF", body_sz=15, where="узел IF")

    arrow_n8n(d, 600, 700, CY)

    node_n8n(d, 1310, CY - 150, 260, 110, "совпало", "гасится бесплатно, без записи",
              kind="code", body_sz=14, where="исход — совпало")
    node_n8n(d, 1310, CY + 40, 260, 110, "не совпало", "заявка идёт дальше по цепочке",
              kind="trigger", body_sz=14, where="исход — не совпало")

    arrow(d, 1220, CY, 1310, CY - 95, col=MID, wd=3)
    clabel(d, 1270, CY - 110, "true", 15, MUTE, where="метка true")
    arrow(d, 1220, CY, 1310, CY + 95, col=MID, wd=3)
    clabel(d, 1270, CY + 100, "false", 15, MUTE, where="метка false")

    legend_n8n(d, 40, CY + 210)
    disclaimer(d, CW / 2, CY + 250)
    return im


save(mehanika(), "k2-n8n-mehanika.png")


# ── слой 2: n8n-стиль, проверка моделью + реальные прогоны ─────────────────
def llm_provexa():
    CH = 560
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: проверка моделью на тот же вопрос иначе",
         sz=24, x=40, y=16)

    CY = 220
    node_n8n(d, 40, CY - 130, 820, 260,
              "Same question, reworded?",
              ["«Это новое сообщение: «{{новый текст}}». Недавнее сообщение того же",
               "контакта: «{{старый текст}}». Это тот же вопрос, просто сформулированный",
               "иначе? Ответь строго «да» или «нет».»"],
              kind="model", subtype="chainLlm", body_sz=15, where="узел проверки LLM")

    callout(d, 960, CY - 130, 580, 120,
            "Прогон 1 — буквальный повтор",
            "точное совпадение поймало мгновенно: заявка не записана, ответа не было;"
            " сам прогон технически успешен",
            tone="ok", where="прогон 1")
    callout(d, 960, CY + 10, 580, 120,
            "Прогон 2 — перефразировка",
            "точное совпадение не поймало — дошло до модели, модель ответила «да»",
            tone="warn", where="прогон 2")

    legend_n8n(d, 40, CY + 190)
    disclaimer(d, CW / 2, CY + 230)
    return im


save(llm_provexa(), "k2-n8n-llm-provexa.png")


# ── тестовый стенд: настоящий скрин воркфлоу сравнения 4 схем (n20) ────────
def test_stend_real():
    """Кроп живого n8n-стенда, без перерисовки — только вырезка прямоугольника
    из RAW-скрина, тем же приёмом, что `make_figure_k3_real_captions.py`
    (кроп заново из необрезанного файла, граница проверяема по исходнику).

    Источник: `stend/n8n-screenshots-raw/case2-test-4schemes.png` (1900×1100,
    Playwright, живой стенд https://n8n.lessons.tellian.io, снят 2026-10-20),
    воркфлоу «C8 · Кейс 2 — тест дедупликации (стенд, 4 схемы)»: узлы `Test
    pair (webhook)` → `Jev decision (noul)` (httpRequest) и `LLM judge`
    (с подузлом `Judge model`) параллельно → `Combine` (Input 1 / Input 2) →
    `Shape result` → `Respond`.

    Кроп (230, 340, 1740, 810) исходного файла — ТОЛЬКО граф узлов:
    без breadcrumb/заголовка канваса (строка с названием воркфлоу, где был
    бы и workflow id — канон §2–§3), без вкладок Editor/Executions/
    Evaluations, без бейджа Published, без левой колонки иконок приложения,
    без правой плавающей панели зума/поиска, без кнопки «Execute workflow»
    и без нижней панели Logs. Результат 1510×470 (соотношение 3,21) —
    landscape, та же причина, что у `k2-n8n-jev-real.png` (n23 backup):
    портретный кроп не укладывается в раскладку приёма без сжатия
    (`deck_kit.py: FIG_MIN_FILL`/`FIG_NATURAL_H`).
    """
    raw = Image.open(
        _Path(__file__).resolve().parents[1] / "stend" / "n8n-screenshots-raw"
        / "case2-test-4schemes.png"
    ).convert("RGB")
    crop = raw.crop((230, 340, 1740, 810))
    save(crop, "k2-n8n-test-stend-real.png")


test_stend_real()

report()
