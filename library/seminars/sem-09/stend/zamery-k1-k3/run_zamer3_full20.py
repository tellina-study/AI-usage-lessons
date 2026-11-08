#!/usr/bin/env python3
"""Полный замер 20×3 (Кейс 3) — issue #299, правка владельца 2026-10-27.

Прогоняет ОДИН И ТОТ ЖЕ набор из 20 вопросов (`sborka_zamer3.TEST_QUESTIONS`, 2 вопроса на
каждый из 10 пунктов базы) через ТРИ уже опубликованных на стенде сценария:

    s9-m3-code               цикл, проверяющий — код, потолок 3 попытки
    s9-m3-judge               цикл, проверяющий — судья-модель, потолок 3 попытки
    s9-m3-combo-noceiling      цикл, проверяющий — код И судья (строгая комбинация),
                               потолок 6 попыток (см. combo_and_loop.py)

На каждую попытку сохраняется: текст ответа, вердикт(ы), причина отказа и токены вызова
модели (`llm.tokens.in/out` из `metadata.tracing` узла — то же поле, что n8n пишет для
каждого LLM-вызова). Стоимость считается по актуальному публичному прайсу OpenRouter для
`qwen/qwen-2.5-7b-instruct` (получен напрямую `GET https://openrouter.ai/api/v1/models`,
без авторизации, 2026-10-27): $0.0000001/входной токен, $0.0000002/выходной токен.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_zamer3_full20.py --output raw/zamer3-full-20.json
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

_spec = _ilu.spec_from_file_location("sborka_zamer3_full20", str(HERE / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

QUESTIONS = [q["question"] for q in z3.TEST_QUESTIONS]
assert len(QUESTIONS) == 20

# Прайс OpenRouter для qwen/qwen-2.5-7b-instruct, проверено прямым GET без авторизации
# https://openrouter.ai/api/v1/models, 2026-10-27: pricing.prompt=0.0000001,
# pricing.completion=0.0000002 ($/токен).
PRICE_IN_PER_TOKEN = 0.0000001
PRICE_OUT_PER_TOKEN = 0.0000002

VARIANTS = {
    "code": {
        "webhook": "s9-m3-code",
        "max_attempts": 3,
        "gen_node": "Generate answer",
        "verdict_nodes": ["Code check"],
        "ok_screen": "Result screen (ok)",
        "fail_screen": "Result screen (не сошлось)",
        "timeout_s": 180,
    },
    "judge": {
        "webhook": "s9-m3-judge",
        "max_attempts": 3,
        "gen_node": "Generate answer",
        "verdict_nodes": ["Judge verdict"],
        "ok_screen": "Result screen (ok)",
        "fail_screen": "Result screen (не сошлось)",
        "timeout_s": 180,
    },
    "combo": {
        "webhook": "s9-m3-combo-noceiling",
        "max_attempts": 6,
        "gen_node": "Generate answer",
        "verdict_nodes": ["Code check", "Judge verdict", "Combine (code AND judge)"],
        "ok_screen": "Result screen (ok)",
        "fail_screen": "Result screen (принудительная остановка)",
        "timeout_s": 300,
    },
}


def post_form(webhook, question_text):
    url = f"{HOST}/form/{webhook}"
    boundary = "----full20"
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


def node_json(run_entry):
    try:
        return run_entry["data"]["main"][0][0]["json"]
    except Exception:
        return {}


def node_tokens(run_entry):
    try:
        t = run_entry["metadata"]["tracing"]
        return {"tokens_in": t.get("llm.tokens.in", 0), "tokens_out": t.get("llm.tokens.out", 0)}
    except Exception:
        return {"tokens_in": 0, "tokens_out": 0}


def run_one(variant_name, question):
    v = VARIANTS[variant_name]
    resp = post_form(v["webhook"], question)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
    run_data = {}
    deadline = time.time() + v["timeout_s"]
    while time.time() < deadline:
        time.sleep(1.5)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if v["ok_screen"] in run_data or v["fail_screen"] in run_data:
            break

    gen_runs = run_data.get(v["gen_node"], [])
    attempts = len(gen_runs)
    converged = v["ok_screen"] in run_data
    timed_out = not converged and v["fail_screen"] not in run_data

    all_attempts = []
    call_tokens = []  # по одному элементу на каждый LLM-вызов (generate [+ judge])
    for i in range(attempts):
        gen_json = node_json(gen_runs[i])
        answer = gen_json.get("text")
        gtok = node_tokens(gen_runs[i])
        call_tokens.append(gtok)
        attempt_record = {"attempt": i + 1, "answer": answer,
                           "gen_tokens_in": gtok["tokens_in"], "gen_tokens_out": gtok["tokens_out"]}
        for vn in v["verdict_nodes"]:
            vr = run_data.get(vn, [])
            if i < len(vr):
                vjson = node_json(vr[i])
                out = vjson.get("output", vjson)
                attempt_record[vn] = out
                # Judge verdict и Combine — LLM/код-вызовы с собственными токенами (Code
                # check — чистый JS, без tracing, node_tokens() вернёт нули корректно).
                if vn == "Judge verdict":
                    jtok = node_tokens(vr[i])
                    attempt_record["judge_tokens_in"] = jtok["tokens_in"]
                    attempt_record["judge_tokens_out"] = jtok["tokens_out"]
                    call_tokens.append(jtok)
        all_attempts.append(attempt_record)

    total_tokens_in = sum(c["tokens_in"] for c in call_tokens)
    total_tokens_out = sum(c["tokens_out"] for c in call_tokens)
    cost_usd = total_tokens_in * PRICE_IN_PER_TOKEN + total_tokens_out * PRICE_OUT_PER_TOKEN

    return {
        "question": question, "variant": variant_name, "exec_id": exec_id,
        "attempts": attempts, "converged": converged, "timed_out": timed_out,
        "all_attempts": all_attempts,
        "final_answer": node_json(gen_runs[-1]).get("text") if gen_runs else None,
        "llm_calls": len(call_tokens), "total_tokens_in": total_tokens_in,
        "total_tokens_out": total_tokens_out, "cost_usd": round(cost_usd, 6),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="raw/zamer3-full-20.json")
    ap.add_argument("--variants", default="code,judge,combo",
                     help="подмножество вариантов через запятую (для частичного/возобновляемого прогона)")
    ap.add_argument("--max-seconds-per-question", type=int, default=600,
                     help="если один вопрос реально занял больше — печатает предупреждение "
                          "в stderr (ручная проверка критерия СТОП из задачи)")
    args = ap.parse_args()
    variants = args.variants.split(",")

    if not API or not KEY:
        print("N8N_API_URL / N8N_API_KEY не заданы — источник credentials не сделан",
              file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.output)
    results = {"questions_total": len(QUESTIONS), "variants": {}}
    if out_path.exists():
        # возобновление после частичного прогона — не теряем уже посчитанное
        results = json.loads(out_path.read_text(encoding="utf-8"))

    for variant_name in variants:
        bucket = results["variants"].setdefault(variant_name, [])
        done_questions = {r["question"] for r in bucket}
        print(f"=== variant={variant_name} ({len(done_questions)}/{len(QUESTIONS)} уже есть) ===",
              file=sys.stderr)
        for i, q in enumerate(QUESTIONS, start=1):
            if q in done_questions:
                continue
            t0 = time.time()
            print(f"[{variant_name} {i}/20] {q[:55]:55s}", end=" ", file=sys.stderr, flush=True)
            try:
                r = run_one(variant_name, q)
            except Exception as e:
                print(f"ОШИБКА: {e}", file=sys.stderr)
                bucket.append({"question": q, "variant": variant_name, "error": str(e)})
                out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8")
                continue
            dt = time.time() - t0
            print(f"попыток={r['attempts']} converged={r['converged']} "
                  f"${r['cost_usd']:.5f} {dt:.1f}s", file=sys.stderr)
            if dt > args.max_seconds_per_question:
                print(f"  !! ВНИМАНИЕ: вопрос занял {dt:.0f}s — выше порога "
                      f"{args.max_seconds_per_question}s из задания, см. критерий СТОП",
                      file=sys.stderr)
            bucket.append(r)
            out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8")

    total_calls = sum(r.get("llm_calls", 0) for b in results["variants"].values() for r in b)
    total_cost = sum(r.get("cost_usd", 0) for b in results["variants"].values() for r in b)
    print(f"\nГотово. LLM-вызовов всего: {total_calls}, суммарная оценочная стоимость: "
          f"${total_cost:.4f}. Записано в {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
