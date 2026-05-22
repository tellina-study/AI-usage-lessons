#!/usr/bin/env python3
"""Generate charts for lec-12 via QuickChart API."""
import json
import urllib.parse
import urllib.request
from pathlib import Path

DEST = Path("/tmp/lec-12-wt/library/lectures/lec-12/rendered/assets/charts")
DEST.mkdir(parents=True, exist_ok=True)

# Ocean palette
COLORS = {
    "deep": "#21295C",
    "mid": "#065A82",
    "light": "#1C7293",
    "teal": "#028090",
    "gold": "#F0AB00",
    "surface": "#F4F7FA",
}


def make_chart(config: dict, out_name: str, w: int = 800, h: int = 500):
    """Generate chart via QuickChart and save."""
    config_json = json.dumps(config)
    url = (
        f"https://quickchart.io/chart?w={w}&h={h}&bkg=white&c="
        + urllib.parse.quote(config_json)
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "lec-12 chart builder"})
        with urllib.request.urlopen(req, timeout=30) as r:
            content = r.read()
        out = DEST / out_name
        out.write_bytes(content)
        print(f"OK {out_name} ({len(content)} bytes)")
        return True
    except Exception as e:
        print(f"FAIL {out_name}: {e}")
        return False


# s08 — Digital twin market: 36 → 180 billion + AI-mfg 155 + OPC-AI 17,15
make_chart({
    "type": "bar",
    "data": {
        "labels": ["Twin 2025", "Twin 2030", "AI mfg 2030", "OPC UA AI 2026"],
        "datasets": [{
            "label": "Размер рынка, млрд $",
            "data": [36.19, 180.28, 155.04, 17.15],
            "backgroundColor": [COLORS["mid"], COLORS["gold"], COLORS["teal"], COLORS["light"]],
            "borderWidth": 0,
        }],
    },
    "options": {
        "plugins": {
            "legend": {"display": False},
            "title": {
                "display": True,
                "text": "Рынки цифровых двойников и AI в производстве 2025-2030",
                "font": {"size": 18, "weight": "bold"},
                "color": COLORS["deep"],
            },
            "datalabels": {
                "color": COLORS["deep"],
                "font": {"size": 16, "weight": "bold"},
                "anchor": "end",
                "align": "top",
                "formatter": "(v) => '$' + v + 'B'",
            },
        },
        "scales": {
            "y": {
                "beginAtZero": True,
                "max": 220,
                "title": {"display": True, "text": "Млрд долларов", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"], "font": {"size": 12}},
                "grid": {"color": "#E5EAF0"},
            },
            "x": {
                "ticks": {"color": COLORS["deep"], "font": {"size": 11}},
                "grid": {"display": False},
            },
        },
    },
}, "s08-market.png", 900, 500)

# s12 — Cost-of-FP cascade waterfall
make_chart({
    "type": "bar",
    "data": {
        "labels": ["Деталей за смену", "FP 1% от 10 000", "Годных отвергнуто"],
        "datasets": [{
            "label": "Штук",
            "data": [10000, 100, 100],
            "backgroundColor": [COLORS["mid"], COLORS["gold"], COLORS["gold"]],
            "borderWidth": 0,
        }],
    },
    "options": {
        "plugins": {
            "legend": {"display": False},
            "title": {
                "display": True,
                "text": "Каскад: 1% FP × 10 000 = 100 годных отвергнуто",
                "font": {"size": 18, "weight": "bold"},
                "color": COLORS["deep"],
            },
            "datalabels": {
                "color": COLORS["deep"],
                "font": {"size": 20, "weight": "bold"},
                "anchor": "end",
                "align": "top",
            },
        },
        "scales": {
            "y": {
                "beginAtZero": True,
                "type": "logarithmic",
                "title": {"display": True, "text": "Штук (лог. шкала)", "color": COLORS["light"], "font": {"size": 14}},
                "ticks": {"color": COLORS["light"], "font": {"size": 12}},
                "grid": {"color": "#E5EAF0"},
            },
            "x": {
                "ticks": {"color": COLORS["deep"], "font": {"size": 14}},
                "grid": {"display": False},
            },
        },
    },
}, "s12-fp-cascade.png", 900, 500)

# s13 — PdM ROI breakdown horizontal bar
make_chart({
    "type": "horizontalBar",
    "data": {
        "labels": [
            "Затраты на обслуживание",
            "Незапланированные простои",
            "Срок службы оборудования",
            "Аварии",
        ],
        "datasets": [{
            "label": "Изменение",
            "data": [32.5, 40, 30, 40],
            "backgroundColor": [COLORS["mid"], COLORS["gold"], COLORS["teal"], COLORS["light"]],
            "borderWidth": 0,
        }],
    },
    "options": {
        "plugins": {
            "legend": {"display": False},
            "title": {
                "display": True,
                "text": "PdM эффект (Deloitte 2026): средние значения по индустрии, %",
                "font": {"size": 17, "weight": "bold"},
                "color": COLORS["deep"],
            },
            "datalabels": {
                "color": "#fff",
                "font": {"size": 16, "weight": "bold"},
                "anchor": "center",
                "align": "center",
                "formatter": "(v) => v + '%'",
            },
        },
        "scales": {
            "xAxes": [{
                "ticks": {
                    "beginAtZero": True,
                    "max": 50,
                    "fontSize": 12,
                    "fontColor": COLORS["light"],
                },
                "scaleLabel": {
                    "display": True,
                    "labelString": "Изменение, %",
                    "fontColor": COLORS["light"],
                    "fontSize": 14,
                },
                "gridLines": {"color": "#E5EAF0"},
            }],
            "yAxes": [{
                "ticks": {"fontColor": COLORS["deep"], "fontSize": 13},
                "gridLines": {"display": False},
            }],
        },
    },
}, "s13-pdm-effects.png", 900, 500)

# s30 — Gartner cancellation chart
make_chart({
    "type": "bar",
    "data": {
        "labels": [
            "Agentic AI\nотменены к 2027",
            "GenAI PoC\nпрекращены к 2025",
            "Twin без ROI\n(слабые данные)",
            "O&G twin: эффект\nкак ожидался",
            "Пользователи: «соотв.\nожиданиям»",
        ],
        "datasets": [{
            "label": "%",
            "data": [40, 30, 75, 11, 14],
            "backgroundColor": [COLORS["gold"], COLORS["mid"], COLORS["teal"], COLORS["light"], COLORS["deep"]],
            "borderWidth": 0,
        }],
    },
    "options": {
        "plugins": {
            "legend": {"display": False},
            "title": {
                "display": True,
                "text": "Разрыв ожиданий: Gartner, EY, context-clue.com 2026",
                "font": {"size": 16, "weight": "bold"},
                "color": COLORS["deep"],
            },
            "datalabels": {
                "color": COLORS["deep"],
                "font": {"size": 18, "weight": "bold"},
                "anchor": "end",
                "align": "top",
                "formatter": "(v) => v + '%'",
            },
        },
        "scales": {
            "y": {
                "beginAtZero": True,
                "max": 90,
                "title": {"display": True, "text": "%", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"]},
                "grid": {"color": "#E5EAF0"},
            },
            "x": {
                "ticks": {"color": COLORS["deep"], "font": {"size": 10}},
                "grid": {"display": False},
            },
        },
    },
}, "s30-gartner-cancellation.png", 900, 500)

# s22 — Sim-to-real gap chart
make_chart({
    "type": "line",
    "data": {
        "labels": ["t=0", "t=10", "t=20", "t=30", "t=40", "t=50", "t=60"],
        "datasets": [
            {
                "label": "Симуляция (нет отложений) — RL держит 300°C",
                "data": [300, 300, 300, 300, 300, 300, 300],
                "borderColor": COLORS["mid"],
                "backgroundColor": "rgba(6,90,130,0.1)",
                "borderWidth": 3,
                "tension": 0.1,
                "fill": False,
            },
            {
                "label": "Реальность (отложения растут) — T расходится",
                "data": [300, 302, 305, 309, 312, 315, 318],
                "borderColor": COLORS["gold"],
                "backgroundColor": "rgba(240,171,0,0.1)",
                "borderWidth": 3,
                "tension": 0.3,
                "fill": False,
            },
        ],
    },
    "options": {
        "plugins": {
            "legend": {"position": "bottom", "labels": {"color": COLORS["deep"], "font": {"size": 12}}},
            "title": {
                "display": True,
                "text": "Разрыв «симуляция → реальность»: тепловые потери и поверхностные отложения",
                "font": {"size": 16, "weight": "bold"},
                "color": COLORS["deep"],
            },
        },
        "scales": {
            "y": {
                "title": {"display": True, "text": "Температура колонны, °C", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"]},
                "min": 295,
                "max": 325,
                "grid": {"color": "#E5EAF0"},
            },
            "x": {
                "title": {"display": True, "text": "Время, дни", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"]},
                "grid": {"display": False},
            },
        },
    },
}, "s22-sim-real-gap.png", 900, 500)

# s35 — Lighthouse Network growth donut
make_chart({
    "type": "doughnut",
    "data": {
        "labels": ["Заводы с AI (90%)", "Без AI (10%)"],
        "datasets": [{
            "data": [90, 10],
            "backgroundColor": [COLORS["gold"], COLORS["surface"]],
            "borderColor": [COLORS["gold"], COLORS["light"]],
            "borderWidth": 2,
        }],
    },
    "options": {
        "plugins": {
            "legend": {"position": "bottom", "labels": {"color": COLORS["deep"], "font": {"size": 14}}},
            "title": {
                "display": True,
                "text": "Lighthouse Network 2026: 90% новых внедрений содержат AI",
                "font": {"size": 16, "weight": "bold"},
                "color": COLORS["deep"],
            },
            "datalabels": {
                "color": "#fff",
                "font": {"size": 22, "weight": "bold"},
                "formatter": "(v) => v + '%'",
            },
        },
        "cutout": "65%",
    },
}, "s35-lighthouse-donut.png", 700, 500)

# s16 — Alarm prediction time-series
make_chart({
    "type": "line",
    "data": {
        "labels": ["−15м", "−10м", "−5м", "0", "+5м", "+10м"],
        "datasets": [
            {
                "label": "ML-предсказание тревоги",
                "data": [0.05, 0.18, 0.42, 0.71, 0.88, 0.94],
                "borderColor": COLORS["mid"],
                "backgroundColor": "rgba(6,90,130,0.2)",
                "borderWidth": 3,
                "tension": 0.4,
                "fill": True,
            },
            {
                "label": "Фактическая тревога (0/1)",
                "data": [0, 0, 0, 0, 0, 1.0],
                "borderColor": COLORS["gold"],
                "borderWidth": 3,
                "borderDash": [10, 5],
                "fill": False,
            },
        ],
    },
    "options": {
        "plugins": {
            "legend": {"position": "bottom", "labels": {"color": COLORS["deep"], "font": {"size": 12}}},
            "title": {
                "display": True,
                "text": "Предсказание тревоги SCADA: ML видит за 5–15 минут до каскада",
                "font": {"size": 16, "weight": "bold"},
                "color": COLORS["deep"],
            },
        },
        "scales": {
            "y": {
                "min": 0,
                "max": 1.1,
                "title": {"display": True, "text": "Вероятность", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"]},
                "grid": {"color": "#E5EAF0"},
            },
            "x": {
                "title": {"display": True, "text": "Время до тревоги", "color": COLORS["light"]},
                "ticks": {"color": COLORS["light"]},
                "grid": {"display": False},
            },
        },
    },
}, "s16-alarm-prediction.png", 900, 500)

print("=== Charts done ===")
