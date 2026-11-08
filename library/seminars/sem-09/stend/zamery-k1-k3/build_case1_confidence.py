#!/usr/bin/env python3
"""Версия 1.5 Кейса 1 — свободный ответ + число уверенности + порог в коде — issue #299.

Правка владельца 2026-10-27: решатель кейса прыгал от версии 1 (свободный самоотчёт) сразу к
версии 2 (структурированная опора на пункт базы + сверка кодом), хотя вариант «модель называет
число уверенности, порог в коде решает» (4-я строка таблицы «Разбор» в SETKA-KEYSOV-S9.md) ни
разу не был построен и не измерен на собственном стенде — только процитирован по внешним
источникам (калибратор 56%@80% против сырой уверенности 48%@80%). Этот скрипт строит и измеряет
именно его, на ТЕХ ЖЕ 15 трудных вопросах (`voprosy_zamer1.HARD_QUESTIONS`), что версии 1 и 2 —
для прямой сравнимости.

Архитектура — копия версии 2 (`case1-v2.json`), с одной заменой: вместо структурированного поля
`grounded_in_item` (enum kb1..kb10) модель отдаёт `answer` + `confidence` (0-100, самооценка).
Порог выбран ДО измерения, не постфактум: 70 — круглое число, середина между «совсем не уверена»
и «уверена полностью», без подгонки по результату.

Публикует сценарий `С9 · Кейс 1, версия 1.5 (уверенность+порог)` (webhook `s9-answer-confidence`)
на `https://n8n.lessons.tellian.io`, затем прогоняет 15 вопросов, читает `GET /executions/<id>
?includeData=true` (не самоотчёт вебхука) и пишет сырые результаты в JSON.

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 build_case1_confidence.py --push
    python3 build_case1_confidence.py --run --output raw/zamer1-5-confidence.json
"""
import argparse
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
WEBHOOK = "s9-answer-confidence"
THRESHOLD = 70

sys.path.insert(0, str(HERE))
from voprosy_zamer1 import HARD_QUESTIONS  # noqa: E402

KB_TEXT = (
    "База знаний учебного центра:\n"
    "kb1 · Оплата: Курс оплачивается на сайте по ссылке в личном кабинете (карта, Робокасса) "
    "или наличными на ресепшене при личном визите. Рассрочка не предусмотрена.\n"
    "kb2 · Перенос занятия: Перенести конкретное занятие можно не позднее чем за 24 часа до "
    "его начала — через личный кабинет (кнопка «Перенести») или сообщением администратору. "
    "Позже 24 часов занятие считается использованным.\n"
    "kb3 · Документы при поступлении: Нужен паспорт (копия разворота) и СНИЛС; если студенту "
    "не исполнилось 18 лет — согласие одного из родителей, бланк в личном кабинете.\n"
    "kb4 · Возврат денег: Возврат оформляется в течение 10 рабочих дней на карту, с которой "
    "была оплата. Для сумм выше 3000 рублей решение проходит через руководителя, это дольше "
    "стандартного срока.\n"
    "kb5 · Пересдача пропущенного занятия: Пересдачи идут каждую вторую субботу месяца, "
    "расписание публикуется в объявлениях личного кабинета за неделю.\n"
    "kb6 · Пропуск без предупреждения: Занятие считается проведённым, бесплатного повтора не "
    "предусмотрено — действует то же правило, что и перенос позже 24 часов.\n"
    "kb7 · Сертификат: Электронный сертификат формируется автоматически и появляется в личном "
    "кабинете в течение 5 рабочих дней после последнего занятия курса.\n"
    "kb8 · Перевод на другой курс: Перевод возможен при наличии мест на новом курсе; разница "
    "в стоимости пересчитывается администратором индивидуально.\n"
    "kb9 · Работа в праздники: Центр не работает в государственные праздники РФ, занятия на "
    "эти даты переносятся автоматически, уведомление приходит в личный кабинет.\n"
    "kb10 · Связь с преподавателем: Написать конкретному преподавателю можно через раздел "
    "«Сообщения» личного кабинета, ответ приходит в течение одного рабочего дня.\n\n"
    "Вопрос клиента: {{ $json['Вопрос'] }}"
)

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}
TELEGRAM_CRED = {"telegramApi": {"id": "kfXE6PWKNzA56vc6", "name": "Telegram account (С8)"}}
TABLE_REF = {"__rl": True, "value": "U5BLSv5cPzVVyRGy", "mode": "list",
             "cachedResultName": "s9_case1_answers"}


def build_workflow():
    return {
        "name": "С9 · Кейс 1, версия 1.5 (уверенность+порог)",
        "nodes": [
            {
                "id": "c1_5_trigger", "name": "Client question",
                "type": "n8n-nodes-base.formTrigger", "typeVersion": 2.2,
                "position": [-180, 0],
                "webhookId": WEBHOOK,
                "parameters": {
                    "path": WEBHOOK,
                    "formTitle": "Вопрос в учебный центр",
                    "formDescription": "Кейс 1 Семинара 9, версия 1.5 — уверенность и порог",
                    "formFields": {"values": [{
                        "fieldLabel": "Вопрос", "fieldType": "textarea",
                        "placeholder": "например: когда вернут деньги за отменённый курс?",
                        "requiredField": True}]},
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "c1_5_model", "name": "Model (answer, confidence)",
                "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
                "position": [60, 260],
                "parameters": {"model": "qwen/qwen-2.5-7b-instruct", "options": {}},
                "credentials": OPENROUTER_CRED,
            },
            {
                "id": "c1_5_extract", "name": "Answer with confidence (structured)",
                "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
                "position": [60, 0],
                "parameters": {
                    "text": "=" + KB_TEXT,
                    "schemaType": "manual",
                    "inputSchema": json.dumps({
                        "type": "object",
                        "properties": {
                            "answer": {"type": "string",
                                       "description": "ответ клиенту по существу, 1-2 "
                                                       "предложения; если не уверена — "
                                                       "честный отказ"},
                            "confidence": {"type": "integer", "minimum": 0, "maximum": 100,
                                           "description": "самооценка уверенности в том, что "
                                                           "ответ точно соответствует базе "
                                                           "знаний: 0 — совсем не уверена, "
                                                           "100 — абсолютно уверена"},
                        },
                        "required": ["answer", "confidence"],
                    }, ensure_ascii=False),
                    "options": {},
                },
            },
            {
                "id": "c1_5_if", "name": f"Confidence >= {THRESHOLD}?",
                "type": "n8n-nodes-base.if", "typeVersion": 2,
                "position": [300, 0],
                "parameters": {"conditions": {
                    "options": {"caseSensitive": True, "typeValidation": "strict"},
                    "combinator": "and",
                    "conditions": [{
                        "leftValue": "={{ $json.output.confidence }}",
                        "rightValue": THRESHOLD,
                        "operator": {"type": "number", "operation": "gte"}}]}},
            },
            {
                "id": "c1_5_write_ok", "name": "Write row (answered)",
                "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
                "position": [540, -80],
                "parameters": {
                    "operation": "insert", "dataTableId": TABLE_REF,
                    "columns": {"mappingMode": "defineBelow", "value": {
                        "version": "v1.5-confidence",
                        "question": "={{ $('Client question').item.json['Вопрос'] }}",
                        "answer": "={{ $json.output.answer }}",
                        "grounded_item": "={{ 'confidence=' + $json.output.confidence }}",
                        "decision": "answered"}, "matchingColumns": [], "schema": []},
                    "options": {}},
            },
            {
                "id": "c1_5_result_ok", "name": "Result screen (answered)",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [780, -80],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Ответ (версия 1.5 — уверенность выше порога)",
                    "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                          "}}<br><br>Ответ: {{ $json.answer }}<br>"
                                          "<small>уверенность: {{ $json.confidence }}</small>",
                    "options": {"appendAttribution": False}},
            },
            {
                "id": "c1_5_notify", "name": "Notify Olga (escalation)",
                "type": "n8n-nodes-base.telegram", "typeVersion": 1.2,
                "position": [540, 160],
                "parameters": {
                    "operation": "sendMessage", "chatId": "266536553",
                    "text": "=Клиент спросил «{{ $('Client question').item.json['Вопрос'] "
                            "}}». Уверенность модели ({{ $('Answer with confidence "
                            "(structured)').item.json.output.confidence }}) ниже порога "
                            f"{THRESHOLD} — вопрос передан вам.",
                    "additionalFields": {}},
                "credentials": TELEGRAM_CRED,
            },
            {
                "id": "c1_5_write_esc", "name": "Write row (escalated)",
                "type": "n8n-nodes-base.dataTable", "typeVersion": 1,
                "position": [780, 160],
                "parameters": {
                    "operation": "insert", "dataTableId": TABLE_REF,
                    "columns": {"mappingMode": "defineBelow", "value": {
                        "version": "v1.5-confidence",
                        "question": "={{ $('Client question').item.json['Вопрос'] }}",
                        "answer": "",
                        "grounded_item": "={{ 'confidence=' + "
                                          "$('Answer with confidence (structured)')"
                                          ".item.json.output.confidence }}",
                        "decision": "escalated"}, "matchingColumns": [], "schema": []},
                    "options": {}},
            },
            {
                "id": "c1_5_result_esc", "name": "Result screen (escalated)",
                "type": "n8n-nodes-base.form", "typeVersion": 1,
                "position": [1020, 160],
                "parameters": {
                    "operation": "completion", "respondWith": "text",
                    "completionTitle": "Передано сотруднику",
                    "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                          "}}<br><br>Подождите, пожалуйста — ответит человек.",
                    "options": {"appendAttribution": False}},
            },
        ],
        "connections": {
            "Client question": {"main": [[{"node": "Answer with confidence (structured)",
                                            "type": "main", "index": 0}]]},
            "Answer with confidence (structured)": {
                "main": [[{"node": f"Confidence >= {THRESHOLD}?", "type": "main", "index": 0}]]},
            f"Confidence >= {THRESHOLD}?": {"main": [
                [{"node": "Write row (answered)", "type": "main", "index": 0}],
                [{"node": "Notify Olga (escalation)", "type": "main", "index": 0}]]},
            "Write row (answered)": {"main": [[{"node": "Result screen (answered)",
                                                 "type": "main", "index": 0}]]},
            "Notify Olga (escalation)": {"main": [[{"node": "Write row (escalated)",
                                                     "type": "main", "index": 0}]]},
            "Write row (escalated)": {"main": [[{"node": "Result screen (escalated)",
                                                  "type": "main", "index": 0}]]},
            "Model (answer, confidence)": {"ai_languageModel": [
                [{"node": "Answer with confidence (structured)",
                  "type": "ai_languageModel", "index": 0}]]},
        },
        "settings": {"executionOrder": "v1"},
    }


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
    (HERE / "case1-v1_5-confidence.json").write_text(
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
    boundary = "----c15boundary"
    body = (f"--{boundary}\r\n"
            'Content-Disposition: form-data; name="field-0"\r\n\r\n'
            f"{question_text}\r\n--{boundary}--\r\n").encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_execution(exec_id):
    req = urllib.request.Request(
        f"{API}/executions/{exec_id}?includeData=true",
        headers={"X-N8N-API-KEY": KEY})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def node_items(run_data, node_name):
    try:
        return run_data[node_name][0]["data"]["main"][0]
    except Exception:
        return None


def run_one(question_text, sleep=0.6, timeout=25):
    resp = post_form(question_text)
    waiting_url = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting_url).path.rstrip("/").split("/")[-1]
    run_data = {}
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(sleep)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run_data = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if "Answer with confidence (structured)" in run_data:
            break
    items = node_items(run_data, "Answer with confidence (structured)")
    output = None
    if items:
        try:
            output = items[0]["json"]["output"]
        except Exception:
            output = None
    return {"exec_id": exec_id, "output": output}


def run_all(output_path):
    results = []
    for q in HARD_QUESTIONS:
        r = run_one(q["question"])
        r["kb_id"] = q["kb_id"]
        r["question"] = q["question"]
        r["correct_by_base"] = q["correct_by_base"]
        results.append(r)
        conf = (r["output"] or {}).get("confidence")
        print(f"  {r['exec_id']}  {q['kb_id']:6s}  confidence={conf}  "
              f"{'ESCALATE' if (conf is None or conf < THRESHOLD) else 'ANSWER'}")
    Path(output_path).write_text(
        json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{len(results)} вопросов записано в {output_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--output", default="raw/zamer1-5-confidence.json")
    args = ap.parse_args()
    if args.push:
        push()
    if args.run:
        run_all(args.output)
    if not args.push and not args.run:
        print("ничего не сделано — передайте --push и/или --run")
