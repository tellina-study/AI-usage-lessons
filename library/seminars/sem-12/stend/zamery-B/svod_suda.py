"""Свод суда кейса B: полнота и корректность, по трём методам, тремя знаменателями.

Две меры НЕ смешиваются в одну таблицу (требование владельца по кейсу 2):
  полнота    = покрытых строк разметки / всех строк разметки;
  корректность = подтверждённых утверждений / всех утверждений описания.
Доля «непроверяемо» печатается отдельной колонкой и в корректность не входит.

Разброс по снимкам считается ПО ВСЕМ записям программой (min/медиана/max), а не
глазами по хвосту вывода.

Запуск:  python3 svod_suda.py [--json]
"""
import json, statistics as st, sys, glob
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUD = sorted(glob.glob(str(HERE / "sud" / "sud-*.json")))
raz = {e["id"]: e for e in json.loads((HERE / "razmetka-101.json").read_text(encoding="utf-8"))["entries"]}


def load():
    recs = []
    for f in SUD:
        recs += json.loads(Path(f).read_text(encoding="utf-8"))
    seen = set()
    for r in recs:
        if r["id"] in seen:
            raise SystemExit(f"дубль в суде: {r['id']}")
        seen.add(r["id"])
        r["author"] = raz[r["id"]]["razmetka_author"]
        if r["n_lines"] != len(raz[r["id"]]["what_is_visible"]):
            raise SystemExit(f"{r['id']}: n_lines={r['n_lines']}, в разметке {len(raz[r['id']]['what_is_visible'])}")
        for m in ("cap", "fld", "yolo"):
            if max(r[m]["cov"] or [0]) > r["n_lines"]:
                raise SystemExit(f"{r['id']} {m}: индекс строки за пределами разметки")
    return recs


def block(recs, title):
    print(f"\n### {title} — снимков {len(recs)}, строк разметки {sum(r['n_lines'] for r in recs)}")
    print(f"{'метод':8s} | {'ПОЛНОТА: строк покрыто / всего':34s} | "
          f"{'КОРРЕКТНОСТЬ: подтв / утвержд':30s} | {'противореч':>10s} | {'непроверяемо':>12s}")
    print("-" * 110)
    for m, name in (("cap", "рассказ"), ("fld", "поля"), ("yolo", "теги")):
        cov = sum(len(r[m]["cov"]) for r in recs)
        tot = sum(r["n_lines"] for r in recs)
        p = sum(r[m]["p"] for r in recs); x = sum(r[m]["x"] for r in recs); u = sum(r[m]["u"] for r in recs)
        ass = p + x + u
        per = [len(r[m]["cov"]) / r["n_lines"] for r in recs]
        print(f"{name:8s} | {cov:4d} / {tot:4d} = {cov/tot*100:5.1f}%  "
              f"(по снимку {min(per)*100:4.1f}–{st.median(per)*100:4.1f}–{max(per)*100:5.1f}%) | "
              f"{p:4d} / {ass:4d} = {p/ass*100:5.1f}%{'':9s} | "
              f"{x:4d} ({x/ass*100:4.1f}%) | {u:4d} ({u/ass*100:4.1f}%)")
    # снимки, несущие хотя бы одно противоречие
    for m, name in (("cap", "рассказ"), ("fld", "поля"), ("yolo", "теги")):
        k = sum(1 for r in recs if r[m]["x"] > 0)
        print(f"  снимков с ≥1 противоречием, {name}: {k} из {len(recs)} = {k/len(recs)*100:.1f}%")
    # «непроверяемо» в рассказе — систематический тик
    k = sum(1 for r in recs if r["cap"]["u"] > 0)
    print(f"  снимков, где рассказ несёт ≥1 непроверяемое утверждение: {k} из {len(recs)} = {k/len(recs)*100:.1f}%")


def main():
    recs = load()
    print(f"ПРОСУЖЕНО: {len(recs)} из 101 снимка")
    block(recs, "ВЕСЬ КОРПУС")
    pl = [r for r in recs if r["author"] == "planner"]
    db = [r for r in recs if r["author"] == "dobor"]
    if pl: block(pl, "знаменатель 1: разметка ПЛАНИРОВЩИКА (автор разметки и судья — разные сессии)")
    if db: block(db, "знаменатель 2: разметка ЭТОЙ СЕССИИ (автор разметки и судья совпадают)")
    if "--json" in sys.argv:
        (HERE / "svod-suda.json").write_text(json.dumps({"n": len(recs)}, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
