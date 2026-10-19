#!/usr/bin/env python3
"""Zillow — концептуальный разбавитель Семинара 8 (issue #274) — 2 схемы,
слой 1 (генерические, системно-нейтральные, не n8n-стиль — у Zillow своего
стенда нет, см. SETKA-KEYSOV-S8-part2.md «Наше решение (без демо)»).

    zillow-shema-bez-geyta.png   как это работало: Zestimate → решение о
                                  покупке БЕЗ обязательного гейта → покупка
                                  исполняется → (нет окна мониторинга —
                                  показано как погашенный, пунктирный шаг) →
                                  ошибка видна только в квартальном отчёте.
    zillow-shema-s-geytom.png    альтернатива С гейтом: Zestimate →
                                  человек-андеррайтер (выше порога риска) →
                                  покупка → circuit breaker, еженедельная
                                  проверка.

Форма — та же, что у `k1-shema-s-llm.png` / `k1-shema-bez-llm.png`
(цепочка прямоугольников слева направо, подпись-итог снизу); «нет окна
мониторинга» нарисован тем же приёмом «погашенного» шага, что проверка-ромб
в `sem-07/rendered/make_figures_c1.py` (серый, пунктирный контур).

Числа и формулировки — дословно `SETKA-KEYSOV-S8-part2.md`
«Концептуальный разбавитель — Zillow».

Запуск: `python3 make_figures_zillow.py` (из `rendered/`).
"""
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parents[4] / "tools" / "seminar-build"))

from fig_toolkit import *

CW = 1600
DEAD = GREY_FILL
DEADTX = GREY_TX


def frame(d, x, y, w, h, *, fill=SURF, stroke=LIGHT, sw=3, r=14, dashed=False):
    if dashed:
        dashbox(d, x, y, w, h, stroke, width=sw, r=r)
    else:
        d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=stroke, width=sw)


def two_lines(d, cx, cy, top, bottom, *, tsz=19, bsz=14, tcol=DEEP, bcol=MUTE, tb=True,
              limit=None, where="?"):
    ft, fb = f(tsz, tb), f(bsz)
    if limit:
        fit(d, top, ft, limit, f"{where} · верх")
        fit(d, bottom, fb, limit, f"{where} · низ")
    th = tsz + bsz + 10
    y = cy - th / 2
    d.text((cx - d.textlength(top, font=ft) / 2, y), top, font=ft, fill=tcol)
    d.text((cx - d.textlength(bottom, font=fb) / 2, y + tsz + 8), bottom, font=fb, fill=bcol)


# ── как работало: без гейта ─────────────────────────────────────────────────
def bez_geyta():
    CH = 460
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Zillow Offers — как принималось решение без гейта", sz=25, x=40, y=16)

    y, h = 170, 150
    xs = [40, 440, 840, 1240]
    bw = 320
    lim = bw - 50

    frame(d, xs[0], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[0] + bw / 2, y + h / 2, "Zestimate", "алгоритмическая оценка дома",
              bsz=15, limit=lim, where="узел 1 · zestimate")

    frame(d, xs[1], y, bw, h, fill=WARM, stroke=GOLD)
    two_lines(d, xs[1] + bw / 2, y + h / 2, "Решение о покупке",
              "без обязательного гейта", tcol=GOLDINK, bcol=GOLDINK, bsz=15,
              limit=lim, where="узел 2 · решение")

    frame(d, xs[2], y, bw, h, fill=DEAD, stroke=DEADTX, dashed=True)
    two_lines(d, xs[2] + bw / 2, y + h / 2, "Покупка исполняется", "окна мониторинга нет",
              tcol=DEADTX, bcol=DEADTX, bsz=15, limit=lim, where="узел 3 · без окна")

    frame(d, xs[3], y, bw, h, fill=SURF, stroke=RED, sw=3)
    two_lines(d, xs[3] + bw / 2, y + h / 2, "Квартальный отчёт", "здесь и видна ошибка",
              tcol=RED, bsz=15, limit=lim, where="узел 4 · отчёт")

    for i in range(3):
        arrow(d, xs[i] + bw, y + h / 2, xs[i + 1], y + h / 2,
              col=DEADTX if i == 2 else MID, wd=4, dash=(i == 2))

    clabel(d, CW / 2, 370, "Ошибка накапливается незаметно между кварталами, не внутри них.",
           22, RED, True, where="подпись-итог", limit=CW - 120)
    clabel(d, CW / 2, 402,
           "Списание запасов $304,4 млн за 3 кв. 2021, $407,9 млн по итогам года; сокращение ~25% штата.",
           17, MUTE, where="подпись-детали", limit=CW - 100)
    return im


save(bez_geyta(), "zillow-shema-bez-geyta.png")


# ── альтернатива: с гейтом ──────────────────────────────────────────────────
def s_geytom():
    CH = 460
    im = Image.new("RGB", (CW, CH), W)
    d = ImageDraw.Draw(im)
    head(d, "Альтернатива с гейтом: человек выше порога риска + circuit breaker",
         sz=24, x=40, y=16)

    y, h = 170, 150
    xs = [40, 440, 840, 1240]
    bw = 320
    lim = bw - 50

    frame(d, xs[0], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[0] + bw / 2, y + h / 2, "Zestimate", "алгоритмическая оценка (вход)",
              bsz=14, limit=lim, where="узел 1 · zestimate")

    frame(d, xs[1], y, bw, h, fill=SURF, stroke=DEEP, sw=4)
    two_lines(d, xs[1] + bw / 2, y + h / 2, "Человек-андеррайтер", "выше порога суммы/риска",
              tcol=DEEP, bsz=14, limit=lim, where="узел 2 · человек")

    frame(d, xs[2], y, bw, h, fill=SURF, stroke=LIGHT)
    two_lines(d, xs[2] + bw / 2, y + h / 2, "Покупка", "исполняется решением человека",
              bsz=14, limit=lim, where="узел 3 · покупка")

    frame(d, xs[3], y, bw, h, fill=SURF, stroke=DEEP, sw=4)
    two_lines(d, xs[3] + bw / 2, y + h / 2, "Circuit breaker", "проверка отклонения еженедельно",
              tcol=DEEP, bsz=13, limit=lim, where="узел 4 · breaker")

    for i in range(3):
        arrow(d, xs[i] + bw, y + h / 2, xs[i + 1], y + h / 2, col=MID, wd=4)

    clabel(d, CW / 2, 380, "Решение выше порога риска — у человека, не у модели.",
           24, MID, True, where="подпись-итог", limit=CW - 120)
    clabel(d, CW / 2, 412, "Окно контроля — неделя, не квартал.",
           19, MUTE, where="подпись-итог 2", limit=CW - 120)
    return im


save(s_geytom(), "zillow-shema-s-geytom.png")

report()
