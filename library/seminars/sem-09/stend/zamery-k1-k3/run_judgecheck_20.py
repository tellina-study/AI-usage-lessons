#!/usr/bin/env python3
"""Судья проверяет готовый (кодовый) ответ — расширение на 20 вопросов, issue #299.

n37-n40 ссылались на `s9-m3-judge-check` на старых 6 вопросах («судья проверяет уже готовый
ответ кода»). Коордиатор 2026-10-27 явно попросил обновить ИМЕННО эти слайды актуальными
числами — поэтому эта методика (не входившая в первоначальные «код/судья/комбо» 3 варианта)
тоже прогоняется на всех 20 вопросах, переиспользуя УЖЕ ПОЛУЧЕННЫЕ первые ответы кода
(`raw/zamer3-full-20.json`, `variants.code[i].all_attempts[0]`) — не новая генерация, тот же
текст, который видел код на попытке 1, теперь проверяет судья. Это тот же методический приём,
что и исходный judge-check: «один и тот же текст — два проверяющих».

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_judgecheck_20.py --output raw/zamer3-judgecheck-20.json
"""
import argparse
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")
HOST = "https://n8n.lessons.tellian.io"
WEBHOOK = "s9-m3-judge-check"


def post_form(question, answer, code_said):
    boundary = "----judgecheck20"
    parts = []
    for name, value in (("field-0", question), ("field-1", answer), ("field-2", code_said)):
        parts.append(f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"\r\n\r\n'
                      f"{value}\r\n")
    parts.append(f"--{boundary}--\r\n")
    body = "".join(parts).encode("utf-8")
    req = urllib.request.Request(f"{HOST}/form/{WEBHOOK}", data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(exec_id):
    req = urllib.request.Request(
        f"{API}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="raw/zamer3-full-20.json")
    ap.add_argument("--output", default="raw/zamer3-judgecheck-20.json")
    args = ap.parse_args()

    src = json.loads((HERE / args.source).read_text(encoding="utf-8"))
    code_results = src["variants"]["code"]
    assert len(code_results) == 20

    results = []
    for i, r in enumerate(code_results, start=1):
        q = r["question"]
        first = r["all_attempts"][0]
        answer = first["answer"]
        code_verdict = first.get("Code check", {})
        code_ok = code_verdict.get("ok")
        code_said = "ok" if code_ok else f"not ok ({code_verdict.get('reason', '')})"
        print(f"[{i}/20] {q[:50]:50s}", end=" ")
        resp = post_form(q, answer, code_said)
        waiting_url = resp.get("formWaitingUrl", "")
        exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
        run_data = {}
        deadline = time.time() + 60
        while time.time() < deadline:
            time.sleep(1.2)
            try:
                ex = get_execution(exec_id)
            except Exception:
                continue
            run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
            if "Result screen" in run_data:
                break
        jv = {}
        try:
            jv = run_data["Judge verdict"][0]["data"]["main"][0][0]["json"].get("output", {})
        except Exception:
            pass
        tokens = {"tokens_in": 0, "tokens_out": 0}
        try:
            tr = run_data["Judge verdict"][0]["metadata"]["tracing"]
            tokens = {"tokens_in": tr.get("llm.tokens.in", 0),
                      "tokens_out": tr.get("llm.tokens.out", 0)}
        except Exception:
            pass
        cost = tokens["tokens_in"] * 0.0000001 + tokens["tokens_out"] * 0.0000002
        print(f"code_ok={code_ok} judge_ok={jv.get('ok')} exec={exec_id}")
        results.append({
            "question": q, "exec_id": exec_id, "answer": answer,
            "code_ok": code_ok, "code_reason": code_verdict.get("reason", ""),
            "judge_ok": jv.get("ok"), "judge_reason": jv.get("reason", ""),
            "tokens_in": tokens["tokens_in"], "tokens_out": tokens["tokens_out"],
            "cost_usd": round(cost, 6),
        })
        (HERE / args.output).write_text(
            json.dumps({"count": len(results), "results": results}, ensure_ascii=False,
                       indent=2) + "\n", encoding="utf-8")

    agree = sum(1 for r in results if r["code_ok"] == r["judge_ok"])
    judge_approved_code_rejected = sum(1 for r in results
                                        if r["code_ok"] is False and r["judge_ok"] is True)
    judge_rejected_code_approved = sum(1 for r in results
                                        if r["code_ok"] is True and r["judge_ok"] is False)
    print(f"\nГотово. {len(results)} вопросов. Согласие код/судья: {agree}/{len(results)}. "
          f"Судья одобрил то, что код забраковал: {judge_approved_code_rejected}. "
          f"Судья забраковал то, что код принял: {judge_rejected_code_approved}.")


if __name__ == "__main__":
    main()
