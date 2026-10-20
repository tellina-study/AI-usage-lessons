#!/usr/bin/env python3
"""Кейс «Проверка на повтор» Семинара 8 (issue #274) — 4 схемы.

    k2-shema-sravnenie.png    слой 1, ГЛАВНАЯ схема кейса: четыре столбца —
                               точное совпадение (хэш) 15/20 (75%), TF-IDF +
                               косинус 13/20 (65%, хуже хэша), дешёвая
                               LLM-судья 17/20 (85%), внешний сервис jev —
                               20/20 (100%, лучший из четырёх; блокер прежнего
                               измерения был ошибкой авторинга узла, не правом
                               доступа — исправлено 2026-10-20). Три схемы
                               переизмерены 2026-10-19 на НОВОМ наборе 20 пар
                               (исходный набор первого измерения не
                               сохранился), jev измерен 2026-10-20 на том же
                               наборе — stend/duplicate-check-results.json.
    k2-n8n-mehanika.png        слой 2 (n8n-стиль): `Set` «Normalize + hash» →
                               `IF` «Exact duplicate in window?» → два исхода.
    k2-n8n-llm-provexa.png     слой 2 (n8n-стиль): `chainLlm` «Same question,
                               reworded? (LLM)» + результат на двух реальных
                               прогонах (буквальный повтор / перефразировка).

Числа и формулировки — дословно `SETKA-KEYSOV-S8.md` «Кейс 2 — Проверка на
повтор» (таблица четырёх схем) и `BRIEF-PROIZVODSTVO.md` §3. Слой 2 — не
снимок живого UI n8n, недостижим в этой среде, см. `notes/mcp-limitations.md`
[#233-8].

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


# ── слой 1: четыре столбца сравнения, реальные числа ────────────────────────
def sravnenie():
    CH = 580
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Четыре способа найти повтор — на одних и тех же 20 парах",
         sz=25, x=40, y=16)

    cols = [
        dict(x=40, title="Точное совпадение (хэш)", pct="15/20 (75%)", col=MID, line=LIGHT,
             fill=SURF, measured=True,
             good="поймала все 5 буквальных повторов и все 10 разных вопросов",
             bad="пропустила все 5 перефразировок — 0% на них"),
        dict(x=430, title="TF-IDF + косинус (порог 0,3)", pct="13/20 (65%)", col=RED, line=RED,
             fill=SURF, measured=True,
             good="хуже хэша, не наравне",
             bad="те же 5 перефразировок + 2 ложных срабатывания, где хэш не ошибается"),
        dict(x=820, title="Дешёвая LLM-судья (gpt-4o-mini)", pct="17/20 (85%)", col=GOLDINK,
             line=GOLD, fill=WARM, measured=True,
             good="поймала все 10 дублей",
             bad="3 ложных срабатывания — не все объясняются совпадением слов"),
        dict(x=1210, title="Внешний сервис (jev)", pct="20/20 (100%)", col=TEAL,
             line=TEAL, fill=PALE, measured=True,
             good="все 10 дублей и все 10 разных вопросов — без единой ошибки",
             bad="одно измерение на 20 парах одной темы — не основание менять готовую архитектуру"),
    ]
    CW_COL = 350
    BAR_Y, BAR_H = 150, 250

    for c in cols:
        frame(d, c["x"], BAR_Y, CW_COL, BAR_H, fill=c["fill"], stroke=c["line"], sw=4)
        lines = wrap(d, c["title"], f(19, True), CW_COL - 32)
        yy = BAR_Y + 18
        for ln in lines:
            fit(d, ln, f(19, True), CW_COL - 32, f"заголовок «{c['title']}»")
            clabel(d, c["x"] + CW_COL / 2, yy, ln, 19, DEEP, True,
                   where=f"заголовок «{c['title']}»", limit=CW_COL - 32)
            yy += 26

        pct_sz = 32 if c["measured"] else 24
        clabel(d, c["x"] + CW_COL / 2, yy + 8, c["pct"], pct_sz, c["col"], True,
               where=f"число «{c['title']}»", limit=CW_COL - 32)

        track_y = yy + (56 if c["measured"] else 46)
        if c["measured"]:
            # тонкая полоса-прогресс под числом — доля правильных ответов
            frac = int(c["pct"].split("/")[0])
            d.rounded_rectangle([c["x"] + 24, track_y, c["x"] + CW_COL - 24, track_y + 14],
                                radius=7, fill=GREY_FILL)
            fw = (CW_COL - 48) * frac / 20
            d.rounded_rectangle([c["x"] + 24, track_y, c["x"] + 24 + fw, track_y + 14],
                                radius=7, fill=c["col"])
        else:
            # не измерено — пунктирный намёк вместо полосы (ряд коротких штрихов)
            seg_y = track_y + 7
            xx = c["x"] + 24
            while xx < c["x"] + CW_COL - 24:
                d.line([(xx, seg_y), (xx + 14, seg_y)], fill=GREY_FILL, width=4)
                xx += 22

        gy = track_y + 32
        for txt, col in ((c["good"], MID if c["measured"] else GREY_TX),
                         (c["bad"], RED if c is cols[1] else (GOLDINK if c is cols[2] else MUTE))):
            glines = wrap(d, txt, f(14), CW_COL - 32)
            for ln in glines:
                fit(d, ln, f(14), CW_COL - 32, f"пояснение «{c['title']}»")
                clabel(d, c["x"] + CW_COL / 2, gy, ln, 14, col, where=f"пояснение «{c['title']}»",
                       limit=CW_COL - 32)
                gy += 18
            gy += 4

    clabel(d, CW / 2, 496,
           "Числа — измерение на 20 тестовых парах (хэш/TF-IDF/LLM-судья — 2026-10-19,",
           18, MUTE, where="подвал 1", limit=CW - 100)
    clabel(d, CW / 2, 520,
           "jev — 2026-10-20, тот же набор), не предположение. Лучший результат — не повод менять архитектуру.",
           18, MUTE, where="подвал 2", limit=CW - 100)
    return im


save(sravnenie(), "k2-shema-sravnenie.png")


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

report()
