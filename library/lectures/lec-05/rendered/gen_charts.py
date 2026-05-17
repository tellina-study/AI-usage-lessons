"""
QuickChart generation for Лекция 5 deck.

DEPRECATED after Phase 8 (Issue #100): both embedded bar-charts were
removed in the Phase-7 5×QA batched revision —
 - c12 (Stripe/JPMorgan/Visa): mixed %/$bn on one axis = misleading scale
   (presentation-critic P1) → replaced by 3 separate stat-plates on s12.
 - c27 (Amazon/Netflix): pale-grey ghost bars, invisible on projector
   (presentation-critic P1) → replaced by 2 stat-plates on s27.
Neither chart is referenced by build_lec05.py anymore; this file is kept
for provenance only. Run: python3 gen_charts.py  → assets/charts/*.png
"""
import json
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path(__file__).parent / "assets" / "charts"
OUT.mkdir(parents=True, exist_ok=True)


def gen(fname, cfg, w, h):
    c = json.dumps(cfg, ensure_ascii=False)
    qs = urllib.parse.urlencode({
        "c": c, "width": w, "height": h, "version": "4",
        "backgroundColor": "transparent"})
    url = "https://quickchart.io/chart?" + qs
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    with urllib.request.urlopen(
            req, timeout=40, context=ssl.create_default_context()) as r:
        data = r.read()
    (OUT / fname).write_bytes(data)
    print(fname, "OK", len(data), "bytes")


def main():
    # s12 — fraud stats horizontal bar (Stripe / JPMorgan / Visa)
    gen("c12-fraud-stats.png", {
        "type": "bar",
        "data": {
            "labels": [
                "Stripe Radar — снижение фрода, %",
                "JPMorgan — меньше ложных срабатываний, %",
                "Visa — предотвращено, $ млрд FY2023"],
            "datasets": [{
                "data": [32, 30, 40],
                "backgroundColor": ["#065A82", "#028090", "#F0AB00"]}]},
        "options": {
            "indexAxis": "y",
            "plugins": {"legend": {"display": False}},
            "scales": {
                "x": {"ticks": {"font": {"size": 17}}},
                "y": {"ticks": {"font": {"size": 14}}}}}},
        820, 360)

    # s27 — recsys shares (historical McKinsey ~2013 estimate)
    gen("c27-recsys-shares.png", {
        "type": "bar",
        "data": {
            "labels": [
                "Amazon — выручка от рекомендаций",
                "Netflix — просмотры от рекомендаций"],
            "datasets": [{
                "data": [35, 75],
                "backgroundColor": ["#065A82", "#028090"]}]},
        "options": {
            "indexAxis": "y",
            "plugins": {"legend": {"display": False}},
            "scales": {
                "x": {"max": 100, "ticks": {"font": {"size": 17}}},
                "y": {"ticks": {"font": {"size": 15}}}}}},
        780, 300)


if __name__ == "__main__":
    main()
