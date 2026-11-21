"""Прогоняет демо-воркфлоу Кейса 4 (sborka_case4.py, webhook s11-case4-scoping) на реальной
паре документов находки (anchor-new3 / Dc-1063) из case4-results.json / corpus_case4.json.
Не часть самого замера (замер уже посчитан офлайн) — проверка, что живой демо-экран n8n
воспроизводит ту же находку на реальных текстах, перед тем как снимать с него скрин.

    set -a; source /home/harness/.n8n-lab-credentials; set +a
    python3 run_case4_demo.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from harness_call import post_form, get_execution
import time
import urllib.parse

HERE = Path(__file__).parent
CORPUS = json.loads((HERE.parent / "corpus" / "corpus_case4.json").read_text())

anchor = next(a for a in CORPUS["anchors"] if a["anchor_id"] == "anchor-new3")
dc1063 = next(c for c in CORPUS["track_d_candidates"] if c["doc_id"] == "Dc-1063")

payload = {
    "question": anchor["question"],
    "course_id": "bio",
    "docs": [
        {"id": "anchor-new3-context", "text": anchor["context"], "course_id": "bio"},
        {"id": "Dc-1063", "text": dc1063["text"], "course_id": "other"},
    ],
}

resp = post_form("s11-case4-scoping", [json.dumps(payload, ensure_ascii=False)])
print("submit response:", json.dumps(resp, ensure_ascii=False)[:500])
waiting = resp.get("formWaitingUrl", "")
exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
print("exec_id:", exec_id)

TARGET_NODES = ["Поиск без скоупинга (весь объединённый индекс)",
                "Поиск со скоупингом (фильтр course_id перед ранжированием)"]

deadline = time.time() + 90
last = None
while time.time() < deadline:
    time.sleep(2)
    try:
        ex = get_execution(exec_id)
    except Exception as e:
        last = str(e)
        continue
    status = ex.get("status")
    finished = ex.get("finished")
    run = ex.get("data", {}).get("resultData", {}).get("runData", {})
    have = [n for n in TARGET_NODES if n in run]
    print("status:", status, "finished:", finished, "nodes ready:", have)
    if len(have) == len(TARGET_NODES):
        for node in TARGET_NODES:
            try:
                out = run[node][0]["data"]["main"][0][0]["json"]
                print(f"--- {node} ---")
                print(json.dumps({k: v for k, v in out.items() if k not in ("docs", "qvec")},
                                  ensure_ascii=False, indent=2))
            except Exception as e:
                print(f"--- {node}: не удалось прочитать ({e})")
        break
else:
    print("timeout, last error:", last)
