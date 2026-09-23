#!/usr/bin/env python3
"""Round-6 Block 5 chart generation (QuickChart API → PNG).

Adds one chart used by the new intro slide s03b «общая статистика по отрасли»
(owner note: «и в начале презы надо добавить общую статистику по отрасли»).

  c03b  s03b  доля разработчиков, использующих AI-инструменты:
              Stack Overflow 2024 = 76%, Stack Overflow 2025 = 84%,
              DORA 2025 = 90% (gold — самая свежая и самая высокая точка).

Baselines are carried ON the chart itself (2024-столбик рядом с 2025-м),
per CLAUDE.md § Baseline / Counterfactual Mandate.

Sources (verified 2026-09):
  Stack Overflow Developer Survey 2025 press release — 84% (2025) vs 76%
  (2024) используют или планируют использовать AI-инструменты; n > 49 000,
  177 стран. https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
  DORA / State of AI-assisted Software Development 2025 — 90% используют AI
  в работе (+14 п.п. к 2024), n > 5 000. https://dora.dev/dora-report-2025/

Run: python3 gen_charts_r6b5.py
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


def c03b_adoption():
    spec = {
        "width": 1100, "height": 420, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                # multi-line tick labels must be ARRAYS in Chart.js —
                # a "\n" inside a single string is NOT split (verified: the
                # first render dropped the year line entirely).
                "labels": [["Stack Overflow", "2024"],
                           ["Stack Overflow", "2025"],
                           ["DORA", "2025"]],
                "datasets": [{
                    "data": [76, 84, 90],
                    "backgroundColor": [LIGHT, MID, GOLD],
                    "borderWidth": 0,
                    "barPercentage": 0.62,
                    "categoryPercentage": 0.72,
                }],
            },
            "options": {
                "plugins": {
                    "legend": {"display": False},
                    "title": {
                        "display": True,
                        "text": "Доля разработчиков, использующих AI-инструменты, %",
                        "color": DEEP,
                        "font": {"size": 22, "weight": "bold"},
                        "padding": {"bottom": 14},
                    },
                    "datalabels": {
                        "anchor": "end", "align": "end", "offset": 2,
                        "color": DEEP,
                        "font": {"size": 30, "weight": "bold"},
                    },
                },
                "layout": {"padding": {"top": 10, "right": 12, "left": 6}},
                "scales": {
                    "y": {
                        "beginAtZero": True, "max": 100,
                        "grid": {"color": GRID},
                        "ticks": {"color": LIGHT, "font": {"size": 18}},
                    },
                    "x": {
                        "grid": {"display": False},
                        "ticks": {"color": DEEP,
                                  "font": {"size": 19, "weight": "bold"}},
                    },
                },
            },
        },
    }
    post(spec, "c03b-adoption.png")


if __name__ == "__main__":
    c03b_adoption()
