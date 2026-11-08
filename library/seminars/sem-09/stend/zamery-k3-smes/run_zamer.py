#!/usr/bin/env python3
"""Основной замер «смесь экспертов» на 20 вопросах Кейса 3 — issue #299, задание З4.

Прогоняет ТЕ ЖЕ 20 вопросов, что `zamery-k1-k3/sborka_zamer3.TEST_QUESTIONS` (2 на каждый из
10 пунктов базы kb1..kb10), через `s9-m3-mix`: три эксперта (qwen/llama/ministral) решают
вопрос независимо при temperature=0, решатель (qwen, та же модель, что судья в
zamery-k1-k3) выбирает лучший из трёх.

На каждый вопрос сохраняется: текст ответа каждого эксперта, выбор решателя и его объяснение,
токены каждого из 4 вызовов модели (`metadata.tracing.llm.tokens.in/out`, то же поле, что уже
использовано в `zamery-k1-k3/run_zamer3_full20.py` для code/judge/combo — тот же метод счёта
стоимости, иначе строку «смесь» нельзя будет честно поставить в один ряд с n40).

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \\
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_zamer.py --output raw/mix-20.json
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
WEBHOOK = "s9-m3-mix"

_spec = _ilu.spec_from_file_location(
    "sem09_mix_sborka_zamer3_run", str(HERE.parent / "zamery-k1-k3" / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

QUESTIONS = [q["question"] for q in z3.TEST_QUESTIONS]
assert len(QUESTIONS) == 20

# Прайс OpenRouter, GET https://openrouter.ai/api/v1/models без авторизации, 2026-10-29.
PRICES = {
    "qwen/qwen-2.5-7b-instruct": (0.0000001, 0.0000002),
    "meta-llama/llama-3.1-8b-instruct": (0.00000005, 0.00000008),
    "mistralai/ministral-8b-2512": (0.00000015, 0.00000015),
}
EXPERT_NODES = [("qwen", "Generate (qwen)", "qwen/qwen-2.5-7b-instruct"),
                ("llama", "Generate (llama)", "meta-llama/llama-3.1-8b-instruct"),
                ("ministral", "Generate (ministral)", "mistralai/ministral-8b-2512")]
RESOLVER_NODE = "Resolver verdict"
RESOLVER_MODEL = "qwen/qwen-2.5-7b-instruct"


def post_form(question_text):
    boundary = "----mix20"
    body = (f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="field-0"\r\n\r\n'
            f"{question_text}\r\n--{boundary}--\r\n").encode("utf-8")
    req = urllib.request.Request(f"{HOST}/form/{WEBHOOK}", data=body, method="POST")
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
        return t.get("llm.tokens.in", 0), t.get("llm.tokens.out", 0)
    except Exception:
        return 0, 0


def cost(model, tin, tout):
    pin, pout = PRICES[model]
    return tin * pin + tout * pout


def run_one(question):
    resp = post_form(question)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
    run_data = {}
    deadline = time.time() + 180
    while time.time() < deadline:
        time.sleep(1.5)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if "Result screen" in run_data:
            break

    experts = {}
    total_in = total_out = 0
    total_cost = 0.0
    error = None
    for key_, node_name, model in EXPERT_NODES:
        runs = run_data.get(node_name, [])
        if not runs:
            error = error or f"узел {node_name} не отработал"
            experts[key_] = {"text": None, "tokens_in": 0, "tokens_out": 0, "error": True}
            continue
        j = node_json(runs[0])
        tin, tout = node_tokens(runs[0])
        c = cost(model, tin, tout)
        total_in += tin
        total_out += tout
        total_cost += c
        experts[key_] = {"text": j.get("text"), "tokens_in": tin, "tokens_out": tout,
                          "cost_usd": round(c, 6)}

    resolver_runs = run_data.get(RESOLVER_NODE, [])
    resolver = {"choice": None, "reasoning": None, "tokens_in": 0, "tokens_out": 0}
    if resolver_runs:
        rj = node_json(resolver_runs[0])
        out = rj.get("output", rj)
        rtin, rtout = node_tokens(resolver_runs[0])
        rcost = cost(RESOLVER_MODEL, rtin, rtout)
        total_in += rtin
        total_out += rtout
        total_cost += rcost
        resolver = {"choice": out.get("choice"), "reasoning": out.get("reasoning"),
                    "tokens_in": rtin, "tokens_out": rtout, "cost_usd": round(rcost, 6)}
    else:
        error = error or "узел Resolver verdict не отработал"

    return {
        "question": question, "exec_id": exec_id, "error": error,
        "experts": experts, "resolver": resolver,
        "llm_calls": sum(1 for k_ in experts if experts[k_].get("text") is not None)
                     + (1 if resolver_runs else 0),
        "total_tokens_in": total_in, "total_tokens_out": total_out,
        "total_cost_usd": round(total_cost, 6),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="raw/mix-20.json")
    ap.add_argument("--only", type=int, default=None,
                     help="прогнать только первые N вопросов (для калибровки)")
    args = ap.parse_args()

    if not API or not KEY:
        print("N8N_API_URL / N8N_API_KEY не заданы", file=sys.stderr)
        sys.exit(1)

    out_path = HERE / args.output
    results = {"questions_total": len(QUESTIONS), "results": []}
    if out_path.exists():
        results = json.loads(out_path.read_text(encoding="utf-8"))
    done = {r["question"] for r in results["results"]}

    qs = QUESTIONS[:args.only] if args.only else QUESTIONS
    for i, q in enumerate(qs, start=1):
        if q in done:
            continue
        t0 = time.time()
        print(f"[{i}/{len(qs)}] {q[:55]:55s}", end=" ", file=sys.stderr, flush=True)
        try:
            r = run_one(q)
        except Exception as e:
            print(f"ОШИБКА: {e}", file=sys.stderr)
            results["results"].append({"question": q, "error": str(e)})
            out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8")
            continue
        dt = time.time() - t0
        print(f"choice={r['resolver']['choice']} calls={r['llm_calls']} "
              f"${r['total_cost_usd']:.6f} {dt:.1f}s exec={r['exec_id']}", file=sys.stderr)
        results["results"].append(r)
        out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")

    total_calls = sum(r.get("llm_calls", 0) for r in results["results"])
    total_cost = sum(r.get("total_cost_usd", 0) for r in results["results"])
    print(f"\nГотово. LLM-вызовов всего: {total_calls}, суммарная стоимость: ${total_cost:.5f}. "
          f"Записано в {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
