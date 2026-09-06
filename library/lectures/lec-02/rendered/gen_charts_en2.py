#!/usr/bin/env python3
"""Lecture 2 EN (issue #188) — chart regeneration with EN axis/legend
labels via QuickChart API. Ported from gen_assets_v2.py / gen_assets_v3.py
(same styling constants: Ocean palette hexes, DPI/sizing) — only labels
changed to EN; output filenames get an -en suffix.

Charts regenerated:
- s11: tokens-per-char bar chart (EN/RU/ZH/Python labels)
- s19: attention-weights bar chart (EN sentence "The cat ate the mouse
  because it was hungry" tokens, leader "cat" gold)
- s25: ucurve line chart (2023 U-curve vs 2026 flat line)
- s25: nolima bar chart (13 models, 50% baseline dashed line)
"""
import json
import urllib.request
from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"


def _quickchart(cfg, out_name, w, h):
    body = json.dumps({
        "chart": json.dumps(cfg), "width": w, "height": h,
        "format": "png", "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart", data=body,
                                 headers={"Content-Type": "application/json"})
    out = ASSETS / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print(out_name, out.stat().st_size, "bytes")


# ---------------------------------------------------------------- s11 chart
def gen_s11_chart_en():
    cfg = {
        "type": "bar",
        "data": {
            "labels": ["English", "Russian", "Chinese", "Python code"],
            "datasets": [{
                "data": [0.25, 0.5, 0.8, 0.4],
                "backgroundColor": ["#065A82", "#F0AB00", "#065A82", "#028090"],
                "borderRadius": 4,
            }],
        },
        "options": {
            "indexAxis": "y",
            "plugins": {
                "legend": {"display": False},
                "datalabels": {
                    "anchor": "end", "align": "end",
                    "color": "#21295C",
                    "font": {"size": 26, "weight": "bold"},
                    "formatter": "___FMT___",
                },
            },
            "scales": {
                "x": {
                    "min": 0, "max": 1.0,
                    "title": {"display": True, "text": "tokens per character",
                              "color": "#1C7293", "font": {"size": 22}},
                    "ticks": {"color": "#1C7293", "font": {"size": 20}},
                    "grid": {"color": "#E5EAF0"},
                },
                "y": {
                    "ticks": {"color": "#21295C",
                              "font": {"size": 24, "weight": "bold"}},
                    "grid": {"display": False},
                },
            },
        },
    }
    body = json.dumps({
        "chart": json.dumps(cfg).replace('"___FMT___"',
            "function(v){return '~'+v.toString();}"),
        "width": 980, "height": 560, "format": "png",
        "backgroundColor": "white", "version": "4",
    }).encode()
    req = urllib.request.Request("https://quickchart.io/chart",
                                 data=body,
                                 headers={"Content-Type": "application/json"})
    out = ASSETS / "charts/s11-tokens-per-char-v2-en.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(req, timeout=60) as r:
        out.write_bytes(r.read())
    print("s11 chart en:", out, out.stat().st_size, "bytes")


# ---------------------------------------------------------------- s19 chart
def gen_s19_chart_en():
    """Attention weights over 9 tokens of "The cat ate the mouse
    because it was hungry" — this is the (renormalized, sum=1) weight
    distribution FROM the token "it" over the preceding context, per
    the s18 matrix row for "it": leader "cat" gold, "was"/"hungry"
    secondary, rest small."""
    labels = ["The", "cat", "ate", "the", "mouse", "because", "it",
              "was", "hungry"]
    # "cat" leads clearly (0.40), matching the s18 matrix's gold cell;
    # remaining mass distributed over the rest of the context, sum = 1.0
    vals = [0.04, 0.40, 0.05, 0.04, 0.06, 0.08, 0.05, 0.13, 0.15]
    colors = ["#065A82"] * 9
    colors[1] = "#F0AB00"  # "cat"
    cfg = {
        "type": "bar",
        "data": {"labels": labels, "datasets": [{
            "data": vals, "backgroundColor": colors, "borderRadius": 3}]},
        "options": {
            "plugins": {"legend": {"display": False},
                        "datalabels": {"display": False}},
            "scales": {
                "y": {"min": 0, "max": 0.5,
                      "ticks": {"color": "#1C7293", "font": {"size": 16}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"ticks": {"color": "#21295C",
                                "font": {"size": 17, "weight": "bold"}},
                      "grid": {"display": False}},
            },
        },
    }
    _quickchart(cfg, "charts/s19-attention-weights-en.png", 980, 400)


# ---------------------------------------------------------------- s25 ucurve
def gen_s25_ucurve_en():
    """Top tier of s25: U-curve lost-in-the-middle (2023, dashed) vs
    flat line needle-retrieval (2026) — "forgetting is solved"."""
    labels = ["start", "", "middle of document", "", "end"]
    cfg = {
        "type": "line",
        "data": {"labels": labels, "datasets": [
            {"label": "2023 — U-curve (middle fails)",
             "data": [93, 74, 55, 76, 94], "borderColor": "#1C7293",
             "borderDash": [9, 7], "borderWidth": 4, "fill": False,
             "pointRadius": 5, "pointBackgroundColor": "#1C7293",
             "tension": 0.35},
            {"label": "2026 — flat line (needle ~99%)",
             "data": [99, 98, 99, 98, 99], "borderColor": "#028090",
             "borderWidth": 5, "fill": False, "pointRadius": 5,
             "pointBackgroundColor": "#028090", "tension": 0.1},
        ]},
        "options": {
            "plugins": {
                "legend": {"position": "bottom",
                           "labels": {"color": "#21295C",
                                       "font": {"size": 26},
                                       "boxWidth": 30}},
                "datalabels": {"display": False},
            },
            "scales": {
                "y": {"min": 40, "max": 105,
                      "title": {"display": True,
                                "text": ["retrieval accuracy,", "%"],
                                "color": "#1C7293", "font": {"size": 28}},
                      "ticks": {"color": "#1C7293", "font": {"size": 28}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"ticks": {"color": "#21295C", "font": {"size": 26},
                                "maxRotation": 0, "minRotation": 0},
                      "grid": {"display": False}},
            },
        },
    }
    _quickchart(cfg, "charts/s25-ucurve-en.png", 1100, 330)


# ---------------------------------------------------------------- s25 nolima
def gen_s25_nolima_en():
    """NoLiMa: 13 models, accuracy at 32K as % of their own baseline;
    11 below the 50% dashed line (gold)."""
    vals = [58, 53, 47, 44, 41, 38, 35, 33, 30, 27, 24, 20, 15]
    colors = ["#028090" if v >= 50 else "#065A82" for v in vals]
    cfg = {
        "type": "bar",
        "data": {"labels": [""] * 13, "datasets": [{
            "data": vals, "backgroundColor": colors, "borderRadius": 2}]},
        "options": {
            "plugins": {
                "legend": {"display": False},
                "datalabels": {"display": False},
                "annotation": {"annotations": {"half": {
                    "type": "line", "yMin": 50, "yMax": 50,
                    "borderColor": "#F0AB00", "borderWidth": 4,
                    "borderDash": [10, 7],
                    "label": {"enabled": True,
                              "content": "50% of baseline accuracy",
                              "backgroundColor": "#F0AB00",
                              "color": "#21295C",
                              "font": {"size": 19, "weight": "bold"},
                              "position": "end"},
                }}},
            },
            "scales": {
                "y": {"min": 0, "max": 100,
                      "title": {"display": True,
                                "text": ["% of the model's own",
                                         "baseline accuracy"],
                                "color": "#1C7293", "font": {"size": 30}},
                      "ticks": {"color": "#1C7293", "font": {"size": 33}},
                      "grid": {"color": "#E5EAF0"}},
                "x": {"title": {"display": True,
                                "text": "13 models · 32K-token context",
                                "color": "#1C7293", "font": {"size": 33}},
                      "grid": {"display": False}},
            },
        },
    }
    _quickchart(cfg, "charts/s25-nolima-en.png", 980, 480)


if __name__ == "__main__":
    gen_s11_chart_en()
    gen_s19_chart_en()
    gen_s25_ucurve_en()
    gen_s25_nolima_en()
    print("done")
