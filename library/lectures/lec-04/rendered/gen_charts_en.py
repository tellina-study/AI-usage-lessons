#!/usr/bin/env python3
"""EN-rendered chart generation for Lecture 4 deck (QuickChart API -> PNG).

English twin of gen_charts_v4.py (issue #172, Ф3 EN re-render). Same specs,
same palette, same numbers; only the visible label strings are translated
per glossary-ru-en.md. Outputs into assets/charts-en/ so the RU charts are
left untouched.

Ocean palette LOCKED: deep #21295C / mid #065A82 / light #1C7293 /
teal #028090 / gold #F0AB00 / surface #F4F7FA / grid #E5EAF0.

Run: python3 gen_charts_en.py
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


# -- c01 -- METR perception gap: predict -24 / believe -20 / actual +19 --
def c01_metr():
    spec = {
        "width": 940, "height": 620, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Predicted\nbefore", "Believed\nafter", "Measured\nactual"],
                "datasets": [{
                    "data": [-24, -20, 19],
                    "backgroundColor": [LIGHT, LIGHT, GOLD],
                    "borderColor": [MID, MID, "#B98400"],
                    "borderWidth": 2,
                    "borderRadius": 8,
                }],
            },
            "options": {
                "plugins": {
                    "legend": {"display": False},
                    "title": {
                        "display": True,
                        "text": "Expected speed-up vs. actual slowdown, %",
                        "font": {"size": 24, "weight": "bold"},
                        "color": DEEP, "padding": 14,
                    },
                    "datalabels": {
                        "anchor": "center", "align": "center",
                        "color": "white",
                        "font": {"size": 30, "weight": "bold"},
                    },
                },
                "scales": {
                    "y": {
                        "title": {"display": True,
                                  "text": "- faster   ·   + slower",
                                  "font": {"size": 18}, "color": DEEP},
                        "ticks": {"font": {"size": 18}},
                        "grid": {"color": GRID},
                        "suggestedMin": -30, "suggestedMax": 26,
                    },
                    "x": {"ticks": {"font": {"size": 20, "weight": "bold"},
                                    "color": DEEP},
                          "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c01-metr-gap.png")


# -- c20 -- GitClear before->after (2020 -> 2024) --
def c20_gitclear():
    spec = {
        "width": 960, "height": 560, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Code clones", "Refactoring", "Churn (2 wk)"],
                "datasets": [
                    {"label": "2020", "data": [8.3, 25, 3.3],
                     "backgroundColor": LIGHT, "borderRadius": 6},
                    {"label": "2024", "data": [12.3, 9, 5.7],
                     "backgroundColor": GOLD, "borderRadius": 6},
                ],
            },
            "options": {
                "plugins": {
                    "legend": {"labels": {"font": {"size": 20}},
                               "position": "top"},
                    "title": {"display": True,
                              "text": "GitClear · 211M lines · tech-debt markers, %",
                              "font": {"size": 22, "weight": "bold"},
                              "color": DEEP, "padding": 12},
                    "datalabels": {"anchor": "end", "align": "end",
                                   "color": DEEP,
                                   "font": {"size": 18, "weight": "bold"}},
                },
                "scales": {
                    "y": {"ticks": {"font": {"size": 18}},
                          "grid": {"color": GRID}, "suggestedMax": 30},
                    "x": {"ticks": {"font": {"size": 19, "weight": "bold"},
                                    "color": DEEP}, "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c20-gitclear.png")


# -- c21 -- SWE-bench Verified ~88 vs Pro ~64 --
def c21_swebench():
    spec = {
        "width": 940, "height": 560, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Verified\n(public)", "Pro\n(private)"],
                "datasets": [{
                    "data": [88, 64],
                    "backgroundColor": [LIGHT, GOLD],
                    "borderColor": [MID, "#B98400"], "borderWidth": 2,
                    "borderRadius": 8,
                }],
            },
            "options": {
                "plugins": {
                    "legend": {"display": False},
                    "title": {"display": True,
                              "text": "SWE-bench: ~24 pp gap, % solved",
                              "font": {"size": 23, "weight": "bold"},
                              "color": DEEP, "padding": 14},
                    "datalabels": {"anchor": "center", "align": "center",
                                   "color": "white",
                                   "font": {"size": 34, "weight": "bold"},
                                   "formatter": None},
                },
                "scales": {
                    "y": {"ticks": {"font": {"size": 18}},
                          "grid": {"color": GRID}, "suggestedMax": 100},
                    "x": {"ticks": {"font": {"size": 20, "weight": "bold"},
                                    "color": DEEP}, "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c21-swe-bench.png")


# -- c24 -- Meta coverage^ (32 vs 5.3) but mutation-kill v (2.4 vs 15) --
def c24_meta():
    spec = {
        "width": 980, "height": 560, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Class coverage", "Mutants killed"],
                "datasets": [
                    {"label": "LLM generation", "data": [32, 2.4],
                     "backgroundColor": GOLD, "borderRadius": 6},
                    {"label": "Narrow targeted method", "data": [5.3, 15],
                     "backgroundColor": TEAL, "borderRadius": 6},
                ],
            },
            "options": {
                "plugins": {
                    "legend": {"labels": {"font": {"size": 19}},
                               "position": "top"},
                    "title": {"display": True,
                              "text": "Meta · more coverage != more defects found, %",
                              "font": {"size": 20, "weight": "bold"},
                              "color": DEEP, "padding": 12},
                    "datalabels": {"anchor": "end", "align": "end",
                                   "color": DEEP,
                                   "font": {"size": 19, "weight": "bold"}},
                },
                "scales": {
                    "y": {"ticks": {"font": {"size": 18}},
                          "grid": {"color": GRID}, "suggestedMax": 38},
                    "x": {"ticks": {"font": {"size": 19, "weight": "bold"},
                                    "color": DEEP}, "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c24-meta-mutation.png")


# -- c33 -- DORA both halves: +7.5 docs / -7.2 stability --
def c33_dora():
    spec = {
        "width": 940, "height": 560, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Documentation", "Delivery\nstability"],
                "datasets": [{
                    "data": [7.5, -7.2],
                    "backgroundColor": [GOLD, TEAL],
                    "borderColor": ["#B98400", "#016170"], "borderWidth": 2,
                    "borderRadius": 8,
                }],
            },
            "options": {
                "plugins": {
                    "legend": {"display": False},
                    "title": {"display": True,
                              "text": "DORA · the AI effect has a paired cost, %",
                              "font": {"size": 23, "weight": "bold"},
                              "color": DEEP, "padding": 14},
                    "datalabels": {"anchor": "center", "align": "center",
                                   "color": "white",
                                   "font": {"size": 30, "weight": "bold"}},
                },
                "scales": {
                    "y": {"title": {"display": True,
                                    "text": "association with AI adoption",
                                    "font": {"size": 17}, "color": DEEP},
                          "ticks": {"font": {"size": 18}},
                          "grid": {"color": GRID},
                          "suggestedMin": -10, "suggestedMax": 10},
                    "x": {"ticks": {"font": {"size": 20, "weight": "bold"},
                                    "color": DEEP}, "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c33-dora.png")


# -- c39 -- Anthropic quiz: 67 (no AI) vs 50 (with AI) --
def c39_anthropic():
    spec = {
        "width": 900, "height": 560, "version": "4",
        "backgroundColor": "white",
        "chart": {
            "type": "bar",
            "data": {
                "labels": ["Without AI", "With AI"],
                "datasets": [{
                    "data": [67, 50],
                    "backgroundColor": [LIGHT, GOLD],
                    "borderColor": [MID, "#B98400"], "borderWidth": 2,
                    "borderRadius": 8,
                }],
            },
            "options": {
                "plugins": {
                    "legend": {"display": False},
                    "title": {"display": True,
                              "text": "Comprehension quiz, % (RCT, n=52)",
                              "font": {"size": 23, "weight": "bold"},
                              "color": DEEP, "padding": 14},
                    "datalabels": {"anchor": "center", "align": "center",
                                   "color": "white",
                                   "font": {"size": 34, "weight": "bold"}},
                },
                "scales": {
                    "y": {"ticks": {"font": {"size": 18}},
                          "grid": {"color": GRID}, "suggestedMax": 80},
                    "x": {"ticks": {"font": {"size": 21, "weight": "bold"},
                                    "color": DEEP}, "grid": {"display": False}},
                },
            },
        },
    }
    post(spec, "c39-anthropic-quiz.png")


if __name__ == "__main__":
    c01_metr()
    c20_gitclear()
    c21_swebench()
    c24_meta()
    c33_dora()
    c39_anthropic()
    print("done")
