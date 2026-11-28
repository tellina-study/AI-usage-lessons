"""Сборка `opisaniya-101.json` — вход замера D и предмет суда кейса B.

Собирает по каждому из 101 снимка три описания: рассказ (caption), поля (fields),
теги детектора (yolo_tags). Плюс печатает строку «цена и задержка» ДВУМЯ прогонами
раздельно (круг 1 — 40 снимков чужой сессией, круг 3 — 61 снимок этой), потому что
задержка у них мерилась в разное время и смешивать её в одно среднее нельзя.

Разброс считается ПО ВСЕМ записям программой, а не глазами по хвосту вывода
(собственный промах этого производства, см. задание круга 3).

Запуск:  python3 build_opisaniya_101.py
"""
import json, statistics as st
from pathlib import Path

HERE = Path(__file__).resolve().parent


def pct(xs, p):
    xs = sorted(xs)
    if not xs: return None
    k = (len(xs) - 1) * p / 100
    f = int(k)
    return xs[f] if f + 1 >= len(xs) else xs[f] + (xs[f + 1] - xs[f]) * (k - f)


def main():
    raz = json.loads((HERE / "razmetka-101.json").read_text(encoding="utf-8"))
    vis = json.loads((HERE / "raw" / "vision_results_101.json").read_text(encoding="utf-8"))
    yolo = json.loads((HERE / "raw_yolo_results_101.json").read_text(encoding="utf-8"))
    by = {(r["id"], r["variant"]): r for r in vis["results"]}
    entries = []
    for e in raz["entries"]:
        if not e["in_corpus"]:
            continue
        cap = by.get((e["id"], "caption"), {})
        fld = by.get((e["id"], "fields"), {})
        entries.append({
            "id": e["id"], "group": e["group"], "razmetka_author": e["razmetka_author"],
            "caption": cap.get("content"),
            "fields": fld.get("parsed"),
            "fields_raw": fld.get("content") if not fld.get("parsed") else None,
            "yolo_tags": yolo["results"].get(e["id"], {}).get("tags", []),
        })
    doc = {"date": "2026-11-24", "corpus_size": len(entries),
           "methods": {"caption": {"model": vis["model"], "system_prompt": vis["sys_caption"],
                                   "user_prompt": vis["user_caption"]},
                       "fields": {"model": vis["model"], "system_prompt": vis["sys_fields"],
                                  "user_prompt": vis["user_fields"]},
                       "yolo": {"model": yolo["model"], "conf_threshold": yolo["conf_threshold"],
                                "vocab": yolo["vocab"]}},
           "entries": entries}
    (HERE / "opisaniya-101.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"снимков {len(entries)}; без рассказа {sum(1 for e in entries if not e['caption'])}; "
          f"поля не распарсились {sum(1 for e in entries if not e['fields'])}; "
          f"без тегов (пустой список) {sum(1 for e in entries if not e['yolo_tags'])}")

    print("\n=== цена и задержка, по всем 202 вызовам, разброс посчитан программой ===")
    hdr = f"{'метод':9s} {'партия':7s} {'N':>4s} {'слов ср':>8s} {'слов мин-макс':>14s} " \
          f"{'$/вызов':>9s} {'$/1000':>8s} {'сек ср':>7s} {'сек p50':>8s} {'сек p95':>8s} {'вх.ток ср':>10s}"
    print(hdr)
    for variant in ("caption", "fields"):
        for batch in ("krug1", "krug3", "ВСЕ"):
            rs = [r for r in vis["results"] if r["variant"] == variant and r.get("content")
                  and (batch == "ВСЕ" or r.get("batch") == batch)]
            if not rs: continue
            w = [r["words"] for r in rs]
            c = [r["cost"] for r in rs if r.get("cost") is not None]
            s = [r["wall_s"] for r in rs if r.get("wall_s") is not None]
            pt = [r["prompt_tokens"] for r in rs if r.get("prompt_tokens")]
            print(f"{variant:9s} {batch:7s} {len(rs):4d} {st.mean(w):8.1f} {min(w):6d}-{max(w):<7d} "
                  f"{st.mean(c):9.5f} {st.mean(c)*1000:8.2f} {st.mean(s):7.2f} {pct(s,50):8.2f} "
                  f"{pct(s,95):8.2f} {st.mean(pt):10.0f}")
    ys = [v["wall_s"] for v in yolo["results"].values()]
    print(f"{'yolo':9s} {'krug3':7s} {len(ys):4d} {'—':>8s} {'—':>14s} "
          f"{0:9.5f} {0:8.2f} {st.mean(ys):7.2f} {pct(ys,50):8.2f} {pct(ys,95):8.2f} {'—':>10s}")

    # корреляция длины ответа и цены — тот самый вывод круга 1, проверяемый на 202 вызовах
    rs = [r for r in vis["results"] if r.get("content") and r.get("cost")]
    w = [r["words"] for r in rs]; c = [r["cost"] for r in rs]
    mw, mc = st.mean(w), st.mean(c)
    num = sum((a - mw) * (b - mc) for a, b in zip(w, c))
    den = (sum((a - mw) ** 2 for a in w) * sum((b - mc) ** 2 for b in c)) ** 0.5
    print(f"\nсвязь длины ответа и цены по всем {len(rs)} вызовам: r = {num/den:+.3f}")
    pt = [r["prompt_tokens"] for r in rs]
    mp = st.mean(pt)
    num2 = sum((a - mp) * (b - mc) for a, b in zip(pt, c))
    den2 = (sum((a - mp) ** 2 for a in pt) * sum((b - mc) ** 2 for b in c)) ** 0.5
    print(f"связь ВХОДНЫХ токенов и цены по тем же {len(rs)} вызовам: r = {num2/den2:+.3f}")
    print(f"входные токены: ср {mp:.0f}, разброс {min(pt)}–{max(pt)}")
    print(f"выходные токены: ср {st.mean([r['completion_tokens'] for r in rs]):.1f}, "
          f"разброс {min(r['completion_tokens'] for r in rs)}–{max(r['completion_tokens'] for r in rs)}")
    tot = sum(c)
    print(f"суммарная цена всех {len(rs)} вызовов: ${tot:.4f}")
    for variant in ("caption", "fields"):
        sub = [r["cost"] for r in rs if r["variant"] == variant]
        print(f"  {variant}: ${sum(sub):.4f} на {len(sub)} вызовов")


if __name__ == "__main__":
    main()
