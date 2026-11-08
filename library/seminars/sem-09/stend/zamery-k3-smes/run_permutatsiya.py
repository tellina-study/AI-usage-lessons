#!/usr/bin/env python3
"""Проверка устойчивости выбора решателя к порядку — Часть Б.5 задания З4 (issue #299).

У судьи в деке (n40, Zheng и соавторы, arXiv:2306.05685) уже измерено: вердикт держится за
порядок, в котором лежат варианты. Эта проверка — прямая параллель на РЕШАТЕЛЕ «смеси
экспертов»: те же три уже сгенерированных текста (из `raw/mix-20.json`, основной замер,
НОВОЙ генерации здесь нет — только решатель вызывается повторно) подаются во второй раз через
`s9-m3-mix-resolver` в ПЕРЕСТАВЛЕННОМ порядке — буквы A и C меняются местами (qwen/ministral
меняются местами, llama остаётся на B), а решатель вызывается снова и выбирает заново.

Если решатель на самом деле судит по СОДЕРЖАНИЮ, выбранный ИДЕНТИЧНОСТЬ-ответ (кто из трёх
экспертов) должен остаться тем же, независимо от того, под какой буквой он теперь стоит.
Если выбор держится за ПОЗИЦИЮ (то же явление, что у судьи), после перестановки резолвер
выберет содержимое новой буквы C/A — то есть другого эксперта, даже если текст не поменялся.

Подмножество — 8 из 20 вопросов (бюджет), подобраны так, чтобы захватить разные исходы
основного замера (не только большинство «C»): q1 (выбор был A), q13 и q19 (выбор был B),
q3/q5/q7/q9/q11 (выбор был C) — см. README, «Как выбрано подмножество».

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \\
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_permutatsiya.py --source raw/mix-20.json --output raw/permutatsiya-8.json
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
WEBHOOK = "s9-m3-mix-resolver"

# Индексы вопросов (1-based, порядок TEST_QUESTIONS) — см. docstring про подбор.
# Расширено с исходных 8 до 12 (добавлены 2, 4, 16, 20 — все из «большинства C») после
# первого прогона: бюджет (88/110) оставлял запас, а первые 8 дали неоднородную картину
# (4/8 held), которую стоило проверить на бОльшем числе вопросов из доминирующего паттерна,
# не расширяя при этом основной прогон на 20 вопросов повторно.
SUBSET_INDEXES = [1, 3, 5, 7, 9, 11, 13, 19, 2, 4, 16, 20]

PRICE_QWEN = (0.0000001, 0.0000002)  # решатель — qwen/qwen-2.5-7b-instruct, та же модель


def post_form(question, a, b, c):
    boundary = "----permut8"
    parts = []
    for name, value in (("field-0", question), ("field-1", a), ("field-2", b),
                         ("field-3", c)):
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


def resolve_once(question, a, b, c):
    resp = post_form(question, a, b, c)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
    run_data = {}
    deadline = time.time() + 90
    while time.time() < deadline:
        time.sleep(1.5)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if "Result screen" in run_data:
            break
    runs = run_data.get("Resolver verdict", [])
    if not runs:
        return {"exec_id": exec_id, "choice": None, "reasoning": None, "error": "no run"}
    j = node_json(runs[0])
    out = j.get("output", j)
    tin, tout = node_tokens(runs[0])
    cost = tin * PRICE_QWEN[0] + tout * PRICE_QWEN[1]
    return {"exec_id": exec_id, "choice": out.get("choice"), "reasoning": out.get("reasoning"),
            "tokens_in": tin, "tokens_out": tout, "cost_usd": round(cost, 6)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default="raw/mix-20.json")
    ap.add_argument("--output", default="raw/permutatsiya-8.json")
    args = ap.parse_args()

    src = json.loads((HERE / args.source).read_text(encoding="utf-8"))
    all_results = src["results"]
    assert len(all_results) == 20

    out_path = HERE / args.output
    out = {"subset_indexes": SUBSET_INDEXES, "items": []}
    if out_path.exists():
        out = json.loads(out_path.read_text(encoding="utf-8"))
    done_q = {it["question"] for it in out["items"]}

    for idx in SUBSET_INDEXES:
        r = all_results[idx - 1]
        q = r["question"]
        if q in done_q:
            continue
        qwen_txt = r["experts"]["qwen"]["text"]
        llama_txt = r["experts"]["llama"]["text"]
        ministral_txt = r["experts"]["ministral"]["text"]
        original_choice_letter = r["resolver"]["choice"]
        letter_to_identity_orig = {"A": "qwen", "B": "llama", "C": "ministral"}
        original_choice_identity = letter_to_identity_orig.get(original_choice_letter)

        # Переставленный порядок: A и C меняются местами (qwen <-> ministral), B (llama)
        # остаётся на месте — прямая параллель перестановке пары у Zheng и соавторов.
        print(f"[idx={idx}] {q[:50]:50s} исходный выбор={original_choice_letter} "
              f"({original_choice_identity})", end=" ")
        resp = resolve_once(q, ministral_txt, llama_txt, qwen_txt)
        letter_to_identity_perm = {"A": "ministral", "B": "llama", "C": "qwen"}
        new_choice_identity = letter_to_identity_perm.get(resp.get("choice"))
        held = (new_choice_identity == original_choice_identity)
        print(f"-> переставленный выбор={resp.get('choice')} ({new_choice_identity}) "
              f"удержался={held} exec={resp.get('exec_id')}")

        out["items"].append({
            "question": q, "kb_order_index": idx,
            "original_choice_letter": original_choice_letter,
            "original_choice_identity": original_choice_identity,
            "permuted_order": ["ministral", "llama", "qwen"],
            "permuted_choice_letter": resp.get("choice"),
            "permuted_choice_identity": new_choice_identity,
            "held": held,
            "permuted_reasoning": resp.get("reasoning"),
            "tokens_in": resp.get("tokens_in"), "tokens_out": resp.get("tokens_out"),
            "cost_usd": resp.get("cost_usd"), "exec_id": resp.get("exec_id"),
        })
        out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n",
                             encoding="utf-8")

    held_n = sum(1 for it in out["items"] if it["held"])
    print(f"\nГотово. {len(out['items'])} вопросов, удержался выбор "
          f"в {held_n}/{len(out['items'])} случаях.")


if __name__ == "__main__":
    main()
