#!/usr/bin/env python3
"""Reproducible chart generation for Лекция 4 deck (QuickChart API → PNG).

Ocean palette LOCKED: deep #21295C / mid #065A82 / light #1C7293 /
teal #028090 / gold #F0AB00 / surface #F4F7FA / grid #E5EAF0.

Charts (functional, embedded via build_lec04.py manage_image):
  c06  s06  3 контекста эффекта (lab +56 / field +14 / legacy -19) diverging
  c08  s08  «почти правильный» 66% — donut highlight
  c12  s12  SWE-bench Verified 88.7 vs Pro 64.3
  c13  s13  GitClear before→after (clones / refactor / churn) grouped
  c17  s17  METR perception-gap (predict -24 / believe -20 / actual +19)

Run: python3 gen_charts.py
"""
import json
import urllib.request
from pathlib import Path

OUT = Path(__file__).parent / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)

DEEP, MID, LIGHT = "#21295C", "#065A82", "#1C7293"
TEAL, GOLD = "#028090", "#F0AB00"
GRID = "#E5EAF0"


def post(spec, name):
    body = json.dumps(spec).encode("utf-8")
    req = urllib.request.Request(
        "https://quickchart.io/chart", data=body,
        headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    p = OUT / name
    p.write_bytes(data)
    print(f"{name}: {len(data)} bytes")


def axis(label, *, mn=None, mx=None, pct=True):
    t = {"display": True, "text": label, "font": {"size": 19}}
    ticks = {"font": {"size": 18}}
    if pct:
        ticks["callback"] = None  # handled by suffix via plugins below
    sc = {"title": t, "ticks": {"font": {"size": 18}},
          "grid": {"color": GRID}}
    if mn is not None:
        sc["min"] = mn
    if mx is not None:
        sc["max"] = mx
    return sc


# ── c06 — s06: один инструмент, три эффекта (diverging) ──
post({
    "width": 900, "height": 540, "backgroundColor": "transparent",
    "version": "4",
    "chart": {
        "type": "bar",
        "data": {
            "labels": ["Лаборатория\n(изолир. задача)",
                       "Поле\n(MS / Accenture)",
                       "Знакомое легаси\n(METR, эксперты)"],
            "datasets": [{
                "data": [56, 14, -19],
                "backgroundColor": [MID, LIGHT, GOLD],
                "borderRadius": 6, "barPercentage": 0.62,
            }],
        },
        "options": {
            "plugins": {"legend": {"display": False}},
            "scales": {
                "y": {"title": {"display": True,
                                "text": "эффект на скорость, %",
                                "font": {"size": 19}},
                      "ticks": {"font": {"size": 18}},
                      "grid": {"color": GRID}},
                "x": {"ticks": {"font": {"size": 17}},
                      "grid": {"display": False}},
            },
        },
    },
}, "c06-context-effect.png")

# ── c08 — s08: «почти правильный» 66% topfrustration donut ──
post({
    "width": 720, "height": 560, "backgroundColor": "transparent",
    "version": "4",
    "chart": {
        "type": "doughnut",
        "data": {
            "labels": ["«почти правильный» — топ-фрустрация (66%)",
                       "остальные ответы (34%)"],
            "datasets": [{
                "data": [66, 34],
                "backgroundColor": [GOLD, "#F4F7FA"],
                "borderColor": ["#FFFFFF", "#FFFFFF"],
                "borderWidth": 2,
            }],
        },
        "options": {
            "cutout": "62%",
            "plugins": {"legend": {"display": False}},
        },
    },
}, "c08-almost-right.png")

# ── c12 — s12: SWE-bench Verified vs Pro ──
post({
    "width": 900, "height": 540, "backgroundColor": "transparent",
    "version": "4",
    "chart": {
        "type": "bar",
        "data": {
            "labels": ["SWE-bench Verified\nзнакомый публичный код",
                       "SWE-bench Pro\nчестный незнакомый код"],
            "datasets": [{
                "data": [88.7, 64.3],
                "backgroundColor": [LIGHT, GOLD],
                "borderRadius": 6, "barPercentage": 0.55,
            }],
        },
        "options": {
            "plugins": {"legend": {"display": False}},
            "scales": {
                "y": {"min": 0, "max": 100,
                      "title": {"display": True,
                                "text": "задач решено, %",
                                "font": {"size": 19}},
                      "ticks": {"font": {"size": 18}},
                      "grid": {"color": GRID}},
                "x": {"ticks": {"font": {"size": 17}},
                      "grid": {"display": False}},
            },
        },
    },
}, "c12-swe-bench.png")

# ── c13 — s13: GitClear before→after ──
post({
    "width": 940, "height": 540, "backgroundColor": "transparent",
    "version": "4",
    "chart": {
        "type": "bar",
        "data": {
            "labels": ["Клоны кода", "Рефакторинг", "Churn (≤2 нед)"],
            "datasets": [
                {"label": "2020–2021", "data": [8.3, 24.1, 5.5],
                 "backgroundColor": LIGHT, "borderRadius": 5},
                {"label": "2024 (AI-эра)", "data": [12.3, 9.5, 7.9],
                 "backgroundColor": GOLD, "borderRadius": 5},
            ],
        },
        "options": {
            "plugins": {"legend": {"position": "top",
                                   "labels": {"font": {"size": 17}}}},
            "scales": {
                "y": {"title": {"display": True, "text": "доля, %",
                                "font": {"size": 19}},
                      "ticks": {"font": {"size": 18}},
                      "grid": {"color": GRID}},
                "x": {"ticks": {"font": {"size": 17}},
                      "grid": {"display": False}},
            },
        },
    },
}, "c13-gitclear.png")

# ── c17 — s17: METR perception-gap (predict / believe / actual) ──
post({
    "width": 940, "height": 540, "backgroundColor": "transparent",
    "version": "4",
    "chart": {
        "type": "bar",
        "data": {
            "labels": ["Прогноз до\n(ускорит)",
                       "Вера после\n(ускорил)",
                       "Измеренный факт\n(время)"],
            "datasets": [{
                "data": [-24, -20, 19],
                "backgroundColor": [LIGHT, LIGHT, GOLD],
                "borderRadius": 6, "barPercentage": 0.6,
            }],
        },
        "options": {
            "plugins": {"legend": {"display": False}},
            "scales": {
                "y": {"title": {"display": True,
                                "text": "изменение времени задачи, %",
                                "font": {"size": 19}},
                      "ticks": {"font": {"size": 18}},
                      "grid": {"color": GRID}},
                "x": {"ticks": {"font": {"size": 17}},
                      "grid": {"display": False}},
            },
        },
    },
}, "c17-metr-gap.png")

print("all charts generated →", OUT)
