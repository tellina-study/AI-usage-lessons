#!/usr/bin/env python3
"""Кейс 3 — комбинация код+судья и демонстрация бесконечного цикла, issue #299.

Правка владельца 2026-10-27: «почему нет проверки с помощью модели, добавь... сделай
комбинацию... покажи кейс с бесконечным лупом и исследования на принудительную остановку».

Судья-модель уже измерена (`case3-judge.json`/`case3-judge-check.json`, README.md «Что замер 2
показал»): на тех же 6 ответах, что код признал годными 5 из 6, судья НИ РАЗУ не согласился —
0 из 6 (`raw/zamer3-judge-check-results.json`). Комбинация «код И судья» СЧИТАНА по этим уже
измеренным вердиктам (не отдельный прогон — методика честно названа), а не домыслена:

    код И судья (строгая комбинация) = ok только если ОБА согласны = 0 из 6
    код ИЛИ судья (мягкая комбинация) = ok если хотя бы один = 5 из 6 (= код один в один)

Строгая комбинация — 0 из 6 — это и есть прямой путь к бесконечному циклу: если судья никогда
не говорит «да», а цикл требует согласия судьи, выход из цикла возможен только через потолок
попыток. Этот скрипт строит и измеряет РЕАЛЬНЫЙ такой цикл — `s9-m3-combo-noceiling`, код И
судья, потолок попыток поднят до 6 (не 3), чтобы честно увидеть, упирается ли цикл в потолок
каждый раз, и что происходит в момент принудительной остановки.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 combo_and_loop.py --push
    python3 combo_and_loop.py --run --output raw/zamer3-combo-loop.json
"""
import argparse
import importlib.util as _ilu
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
WEBHOOK = "s9-m3-combo-noceiling"
COMBO_MAX_ATTEMPTS = 6

_spec = _ilu.spec_from_file_location("sborka_zamer3_combo", str(HERE / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

# поднимаем потолок попыток ТОЛЬКО для этого сценария — не трогаем уже опубликованный
# s9-m3-code (у него MAX_ATTEMPTS=3 остаётся как есть)
z3.MAX_ATTEMPTS = COMBO_MAX_ATTEMPTS


def combine_node(pos):
    js = (
        "const code = $('Code check').item.json.output;\n"
        "const judge = $('Judge verdict').item.json.output;\n"
        "const ok = code.ok === true && judge.ok === true;\n"
        "const reason = ok ? '' : "
        "'код: ' + (code.reason || 'ок') + ' / судья: ' + (judge.reason || 'ок');\n"
        "return { json: { output: { ok, reason, code_ok: code.ok, judge_ok: judge.ok } } };\n"
    )
    return {
        "id": "combine", "name": "Combine (code AND judge)", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": pos,
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript", "jsCode": js},
    }


def build_workflow():
    nodes = [
        z3.form_trigger(WEBHOOK),
        z3.pick_kb_item_node([-20, 0]),
        z3.model_node("m_gen_combo", "Model (generate)", [200, 300]),
        z3.generate_answer_node([200, 0]),
        z3.code_check_node([420, -80]),
        z3.model_node("m_judge_combo", "Model (judge)", [420, 300]),
        z3.judge_verdict_node([420, 80]),
        combine_node([640, 0]),
        z3.retry_if_node([860, 0]),
        z3.prepare_retry_node([860, 220]),
        z3.converged_if_node([1080, -80]),
        z3.write_row_node("write_ok_combo", "Write row (ok)", [1300, -160], "combo",
                           "true", "true", "''"),
        z3.result_screen_node("result_ok_combo", "Result screen (ok)", [1520, -160],
                               "Ответ (код И судья)",
                               "=Вопрос: {{ $('Pick KB item').item.json.question }}<br><br>"
                               "Ответ: {{ $('Generate answer').item.json.text }}"),
        z3.write_row_node("write_notconv_combo", "Write row (not converged)", [1300, 0],
                           "combo", "false", "false", "={{ $json.output.reason }}"),
        z3.result_screen_node(
            "result_notconv_combo", "Result screen (принудительная остановка)", [1520, 0],
            "Остановлено принудительно",
            f"=Не сошлось за {COMBO_MAX_ATTEMPTS} попыток (потолок цикла) — код и судья "
            "вместе ни разу не одобрили ответ. Вопрос передан сотруднику принудительно, "
            "не оставлен крутиться дальше."),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Generate answer", "type": "main", "index": 0}]]},
        "Generate answer": {"main": [[
            {"node": "Code check", "type": "main", "index": 0},
        ]]},
        "Code check": {"main": [[{"node": "Judge verdict", "type": "main", "index": 0}]]},
        "Judge verdict": {"main": [[{"node": "Combine (code AND judge)", "type": "main",
                                      "index": 0}]]},
        "Combine (code AND judge)": {"main": [[
            {"node": "Retry or finish?", "type": "main", "index": 0}]]},
        "Retry or finish?": {"main": [
            [{"node": "Converged?", "type": "main", "index": 0}],
            [{"node": "Prepare retry", "type": "main", "index": 0}],
        ]},
        "Prepare retry": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Converged?": {"main": [
            [{"node": "Write row (ok)", "type": "main", "index": 0}],
            [{"node": "Write row (not converged)", "type": "main", "index": 0}],
        ]},
        "Write row (ok)": {"main": [[
            {"node": "Result screen (ok)", "type": "main", "index": 0}]]},
        "Write row (not converged)": {"main": [[
            {"node": "Result screen (принудительная остановка)", "type": "main", "index": 0}]]},
        "Model (generate)": {"ai_languageModel": [[
            {"node": "Generate answer", "type": "ai_languageModel", "index": 0}]]},
        "Model (judge)": {"ai_languageModel": [[
            {"node": "Judge verdict", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · комбинация код+судья, потолок 6",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def push():
    wf = build_workflow()
    tables = api("GET", "/data-tables")["data"]
    table_id = next(t["id"] for t in tables if t["name"] == z3.S9_TABLE_NAME)
    wf = z3.set_table_id(wf, table_id)
    (HERE / "case3-combo-noceiling.json").write_text(
        json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    if wf["name"] in existing:
        wid = existing[wf["name"]]
        api("PUT", f"/workflows/{wid}", wf)
        print(f"обновлён: {wid}")
    else:
        wid = api("POST", "/workflows", wf)["id"]
        print(f"создан: {wid}")
    api("POST", f"/workflows/{wid}/publish", {})
    print("опубликован")
    return wid


def post_form(question_text):
    url = f"{HOST}/form/{WEBHOOK}"
    boundary = "----combo"
    body = (f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="field-0"\r\n\r\n'
            f"{question_text}\r\n--{boundary}--\r\n").encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=90) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(exec_id):
    req = urllib.request.Request(
        f"{API}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def run_all(output_path):
    questions = [
        "Можно ли перенести занятие, если я заболел?",
        "Когда мне вернут деньги за отменённый курс?",
        "Как связаться с преподавателем по курсу?",
    ]
    results = []
    for q in questions:
        resp = post_form(q)
        waiting_url = resp.get("formWaitingUrl", "")
        exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
        run_data = {}
        deadline = time.time() + 120
        while time.time() < deadline:
            time.sleep(1.5)
            try:
                ex = get_execution(exec_id)
            except Exception:
                continue
            run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
            status = ex.get("data", {}).get("resultData", {}).get("lastNodeExecuted")
            if status in ("Result screen (ok)", "Result screen (принудительная остановка)"):
                break
        # считаем реальное число попыток по числу запусков "Generate answer" в этом execution
        attempts = len(run_data.get("Generate answer", []))
        outcome = "ok" if "Result screen (ok)" in run_data else (
            "forced_stop" if "Result screen (принудительная остановка)" in run_data
            else "unknown")
        results.append({"question": q, "exec_id": exec_id, "attempts": attempts,
                         "outcome": outcome})
        print(f"  {exec_id}  {q[:40]:40s}  попыток={attempts}  исход={outcome}")
    Path(output_path).write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(questions)} вопросов (до {COMBO_MAX_ATTEMPTS} попыток каждый) записано в "
          f"{output_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--output", default="raw/zamer3-combo-loop.json")
    args = ap.parse_args()
    if args.push:
        push()
    if args.run:
        run_all(args.output)
