"""Печатает лист суда по снимкам: разметка, рассказ, поля, теги — компактно.
Судит человек-в-контуре (эта сессия) глазами, печать — только чтобы не листать JSON.

Запуск:  python3 sud_worksheet.py <от> <до>   (индексы 1-based по порядку корпуса)
"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
op = json.loads((HERE / "opisaniya-101.json").read_text(encoding="utf-8"))
raz = {e["id"]: e for e in json.loads((HERE / "razmetka-101.json").read_text(encoding="utf-8"))["entries"]}
a, b = int(sys.argv[1]), int(sys.argv[2])
for i, e in enumerate(op["entries"][a-1:b], a):
    r = raz[e["id"]]
    print(f"\n{'='*78}\n#{i} {e['id']} [{e['group']} · разметка={e['razmetka_author']}]")
    print("РАЗМЕТКА (%d строк):" % len(r["what_is_visible"]))
    for j, l in enumerate(r["what_is_visible"], 1):
        print(f"  R{j}. {l}")
    print("РАССКАЗ:", e["caption"])
    print("ПОЛЯ:", json.dumps(e["fields"], ensure_ascii=False))
    print("ТЕГИ:", ", ".join(f"{t['class']}:{t['conf']}" for t in e["yolo_tags"]) or "(нет)")
