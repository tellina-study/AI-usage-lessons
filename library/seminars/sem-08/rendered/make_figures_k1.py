#!/usr/bin/env python3
"""Кейс «Уведомления» Семинара 8 (issue #274) — 4 схемы.

    k1-shema-s-llm.png     слой 1: форма → извлечение полей → узел-модель
                            (сочиняет текст свободно) → Telegram. Риск: модель
                            может добавить деталь, которой не было в заявке.
    k1-shema-bez-llm.png   слой 1: та же цепочка, последний узел — подстановка
                            значений (шаблон). Без вызова модели — без риска.
    k1-n8n-versiya1.png    слой 2 (n8n-стиль): узел `chainLlm` «Compose
                            notification (LLM)» + его модель (`lmChatOpenRouter`,
                            `openai/gpt-4o-mini`) → находка на заявке Олега —
                            буквальный плейсхолдер «[Имя координатора]».
    k1-n8n-versiya2.png    слой 2 (n8n-стиль): узел `Set` «Compose notification
                            (template)» с выражением шаблона → детерминированный
                            текст на заявке Светланы, без плейсхолдера.

Слой 1 — геометрия по образцу `sem-07/rendered/make_figures_c1.py` (прямая
цепочка прямоугольников, общая функция рисует оба варианта, различается
только последний узел — см. `chain4(highlight)`). Слой 2 — новый приём
`n8n_canvas_kit.py` (узел n8n + стрелка + врезка результата), подключённый
рядом в этой же папке.

Имена узлов, промпты и выражения — дословно `BRIEF-PROIZVODSTVO.md` §3 и
`SETKA-KEYSOV-S8.md` «Кейс 1 — Уведомления». Не снимок живого UI n8n —
недостижим в этой среде, см. `notes/mcp-limitations.md` [#233-8].

Запуск: `python3 make_figures_k1.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *
from n8n_canvas_kit import node_n8n, arrow_n8n, callout, legend_n8n, disclaimer

CW = 1600


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def two_lines(d, cx, cy, top, bottom, *, tsz=22, bsz=16, tcol=DEEP, bcol=MUTE, tb=True,
              limit=None, where="?"):
    ft, fb = f(tsz, tb), f(bsz)
    if limit:
        fit(d, top, ft, limit, f"{where} · верх")
        fit(d, bottom, fb, limit, f"{where} · низ")
    th = tsz + bsz + 10
    y = cy - th / 2
    d.text((cx - d.textlength(top, font=ft) / 2, y), top, font=ft, fill=tcol)
    d.text((cx - d.textlength(bottom, font=fb) / 2, y + tsz + 8), bottom, font=fb, fill=bcol)


# ── слой 1: цепочка из 4 узлов, последний узел меняется по варианту ────────
def chain4(with_llm):
    im = Image.new("RGB", (CW, 460), W)
    d = ImageDraw.Draw(im)
    head(d, "Решение с LLM: модель сочиняет текст" if with_llm
            else "Решение без LLM: шаблон подставляет значения", sz=27, x=40, y=16)

    y, h = 170, 150
    xs = [40, 440, 840, 1240]
    bw = 320

    lim = bw - 50

    frame(d, xs[0], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[0] + bw / 2, y + h / 2, "Форма", "заявка от клиента",
              limit=lim, where="узел 1 · форма")

    frame(d, xs[1], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[1] + bw / 2, y + h / 2, "Извлечение полей",
              "имя · тема · доп. темы · контакт", bsz=15, limit=lim, where="узел 2 · извлечение")

    if with_llm:
        frame(d, xs[2], y, bw, h, fill=WARM, stroke=GOLD)
        two_lines(d, xs[2] + bw / 2, y + h / 2, "Узел-модель", "сочиняет текст свободно",
                  tcol=GOLDINK, bcol=GOLDINK, limit=lim, where="узел 3 · модель")
    else:
        frame(d, xs[2], y, bw, h, fill=PALE, stroke=MID)
        two_lines(d, xs[2] + bw / 2, y + h / 2, "Узел-шаблон", "подстановка значений",
                  tcol=DEEP, bsz=15, limit=lim, where="узел 3 · шаблон")

    frame(d, xs[3], y, bw, h, fill=SURF, stroke=TEAL)
    two_lines(d, xs[3] + bw / 2, y + h / 2, "Отправка в Telegram", "сообщение координатору",
              limit=lim, where="узел 4 · telegram")

    for i in range(3):
        arrow(d, xs[i] + bw, y + h / 2, xs[i + 1], y + h / 2, col=MID, wd=4)

    if with_llm:
        clabel(d, CW / 2, 380, "Риск: модель может добавить деталь, которой не было в заявке.",
               24, GOLDINK, True, where="подпись-итог (с LLM)", limit=CW - 120)
        clabel(d, CW / 2, 412, "Плюс цена и задержка вызова модели на каждый прогон.",
               19, MUTE, where="подпись-итог 2 (с LLM)", limit=CW - 120)
    else:
        clabel(d, CW / 2, 380, "Без вызова модели — без риска сочинённой детали.",
               24, MID, True, where="подпись-итог (без LLM)", limit=CW - 120)
        clabel(d, CW / 2, 412, "Та же форма сообщения, собранная один раз в шаблоне.",
               19, MUTE, where="подпись-итог 2 (без LLM)", limit=CW - 120)
    return im


save(chain4(True), "k1-shema-s-llm.png")
save(chain4(False), "k1-shema-bez-llm.png")


# ── слой 2: n8n-стиль, версия 1 (модель) ────────────────────────────────────
def versiya1():
    CH = 660
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: версия с моделью", sz=26, x=40, y=16)

    CY = 200
    node_n8n(d, 40, CY - 65, 260, 130, "Request form", "форма заявки: имя · тема · доп. темы",
              kind="trigger", where="узел формы")

    node_n8n(d, 360, CY - 115, 620, 230,
              "Compose notification (LLM)",
              ["«Напиши короткое дружелюбное уведомление координатору учебного центра",
               "в Telegram о новой многотемной заявке. Имя заявителя: {{имя}}.",
               "Основная тема: {{тема}}. Также упомянуто: {{доп. темы}}.",
               "Пиши по-человечески, одно-два предложения.»"],
              kind="model", subtype="chainLlm", body_sz=14, where="узел-компоновщик (LLM)")

    node_n8n(d, 520, CY + 160, 300, 100, "Model (notification)",
              "lmChatOpenRouter · openai/gpt-4o-mini", kind="model", body_sz=14,
              where="модель уведомления")
    arrow(d, 670, CY + 160, 670, CY + 115, col=GOLD, wd=3, dash=True)
    clabel(d, 820, CY + 140, "подаёт модель узлу", 14, MUTE, where="подпись модели")

    node_n8n(d, 1120, CY - 65, 300, 130, "Send to Telegram",
              "sendMessage · координатору", kind="external", where="узел отправки")

    arrow_n8n(d, 300, 360, CY)
    arrow_n8n(d, 980, 1120, CY)

    callout(d, 1120, CY + 160, 420, 150,
            "Находка — заявка Олега",
            ["в тексте остался буквальный плейсхолдер «[Имя координатора]»,",
             "а не настоящее имя координатора"],
            tone="bad", where="находка Олег")

    legend_n8n(d, 40, CY + 360)
    disclaimer(d, CW / 2, CY + 400)
    return im


# ── слой 2: n8n-стиль, версия 2 (шаблон) ────────────────────────────────────
def versiya2():
    CH = 580
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Слой 2 — узел n8n: версия с шаблоном", sz=26, x=40, y=16)

    CY = 200
    node_n8n(d, 40, CY - 65, 260, 130, "Request form", "форма заявки: имя · тема · доп. темы",
              kind="trigger", where="узел формы v2")

    node_n8n(d, 360, CY - 120, 700, 240,
              "Compose notification (template)",
              ["notification_text = Новая заявка от {{ $('Request form').item.json['Имя'] }}:",
               "тема «{{ $('Vocabulary check').item.json.topic }}»",
               "{{ ... .extra_topics ? ', также: ' + ... : '' }}."],
              kind="code", subtype="Set / Edit Fields", body_sz=14, where="узел-шаблон")

    node_n8n(d, 1200, CY - 65, 300, 130, "Send to Telegram",
              "sendMessage · координатору", kind="external", where="узел отправки v2")

    arrow_n8n(d, 300, 360, CY)
    arrow_n8n(d, 1060, 1200, CY)

    callout(d, 360, CY + 175, 700, 130,
            "Результат — заявка Светланы",
            "«Новая заявка от Светлана: тема «другое», также: перенос занятия · оплата.»",
            tone="ok", where="результат Светлана")

    legend_n8n(d, 40, CY + 350)
    disclaimer(d, CW / 2, CY + 390)
    return im


save(versiya1(), "k1-n8n-versiya1.png")
save(versiya2(), "k1-n8n-versiya2.png")

report()
