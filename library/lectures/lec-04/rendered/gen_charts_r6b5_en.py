#!/usr/bin/env python3
"""EN twin of gen_charts_r6b5.py (issue #172 — bilingual production).

The RU chart c03b-adoption.png has its title and tick labels baked into the
pixels in Cyrillic, so it CANNOT be reused in the English deck (mirror-check:
an EN artifact must contain no untranslated Russian). This regenerates the
same chart — same numbers, same Ocean palette, same geometry — with English
labels, into assets/charts-en/.

  c03b  s03b  share of developers using AI tools:
              Stack Overflow 2024 = 76%, Stack Overflow 2025 = 84%,
              DORA 2025 = 90% (gold — the most recent and highest point).

Baselines are carried ON the chart itself (the 2024 bar sits next to the 2025
one), per CLAUDE.md § Baseline / Counterfactual Mandate — which applies to the
EN artifacts exactly as it does to the RU ones.

Sources (verified 2026-09, identical to the RU twin — numbers are never
"adjusted" in translation, per glossary-ru-en.md):
  Stack Overflow Developer Survey 2025 press release — 84% (2025) vs 76%
  (2024) use or plan to use AI tools; n > 49,000, 177 countries.
  https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/
  DORA / State of AI-assisted Software Development 2025 — 90% use AI at work
  (+14 pp vs 2024), n > 5,000. https://dora.dev/dora-report-2025/

Run: python3 gen_charts_r6b5_en.py
"""
import json
import urllib.request
from pathlib import Path

OUT = Path(__file__).parent / "assets" / "charts-en"
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
                # a "\n" inside a single string is NOT split (same gotcha the
                # RU twin documents; see notes/mcp-limitations.md).
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
                        "text": "Share of developers using AI tools, %",
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
