#!/usr/bin/env python3
"""Собрать четыре стадии учебного процесса Семинара 7 и выложить их на стенд.

Четыре файла — это ОДИН процесс на четырёх стадиях, по кейсам занятия:

    stadiya-1.json   форма → шаг модели → строка в таблице
    stadiya-2.json   средний узел заменён на извлечение полей
    stadiya-3.json   у среднего узла повтор и вторая ветка (отказ)
    stadiya-4.json   та же стадия 3, опубликованная (кейс 4 про черновик/Publish)

`sem-07-vyhod.json` — то, что уносит студент, это стадия 4 без привязки к
учётным данным и таблице конкретного стенда (их он заводит у себя).

**Ключ стенда читается из окружения и в репозиторий не попадает.**
    source ~/.n8n-lab.env && python3 sborka.py --push

    python3 sborka.py              только записать json-файлы рядом
    python3 sborka.py --push       записать и выложить на стенд (нужен ключ)
    python3 sborka.py --run        выложить, опубликовать и прогнать проверку
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Идентификаторы стенда. Это НЕ секреты (ключа здесь нет) — ссылки на уже
# созданные на стенде таблицу и учётные данные модели. На другом стенде они
# другие, поэтому в студенческом файле их не будет (см. `dlya_studenta`).
TABLE_ID = "veTTXoSvvgMlOfN1"
TABLE_NAME = "Заявки"
CRED_ID = "VbxiQn8TbqA4R2mw"
CRED_NAME = "OpenRouter account"
MODEL = "openai/gpt-4o-mini"

ZAYAVKA = ("Здравствуйте! Хочу записаться на курс по аналитике. "
           "Перезвоните, пожалуйста, сегодня после шести — телефон "
           "+7 916 000-11-22. Спасибо!")


def rl(value, name):
    """Поле-ссылка n8n (resource locator) — так узел хранит выбор из списка."""
    return {"__rl": True, "value": value, "mode": "list", "cachedResultName": name}


def model_node(pos):
    return {
        "id": "model", "name": "Модель", "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": MODEL, "options": {}},
        "credentials": {"openRouterApi": {"id": CRED_ID, "name": CRED_NAME}},
    }


def form_node(path):
    return {
        "id": "form", "name": "Заявка с сайта", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [0, 0], "webhookId": path,
        "parameters": {
            "path": path,
            "formTitle": "Заявка в учебный центр",
            "formDescription": "Напишите, что нужно — мы перезвоним",
            "formFields": {"values": [
                {"fieldLabel": "Имя", "requiredField": True},
                {"fieldLabel": "Контакт", "requiredField": True},
                {"fieldLabel": "Что нужно", "fieldType": "textarea", "requiredField": True},
            ]},
            "options": {},
        },
    }


def table_node(name, node_id, pos, tema_expr, srochnost_expr, iz_teksta=""):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.dataTable",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "operation": "insert",
            "dataTableId": rl(TABLE_ID, TABLE_NAME),
            "columns": {
                "mappingMode": "defineBelow",
                "value": {
                    "prishlo": "={{ $now.toISO() }}",
                    "imya": "={{ $('Заявка с сайта').item.json['Имя'] }}",
                    "kontakt": "={{ $('Заявка с сайта').item.json['Контакт'] }}",
                    "tekst": "={{ $('Заявка с сайта').item.json['Что нужно'] }}",
                    "tema": tema_expr,
                    "srochnost": srochnost_expr,
                    # Контакт пишется ДВАЖДЫ и в два разных столбца: из формы и
                    # из текста заявки. Это не дублирование — люди регулярно
                    # указывают в сообщении второй номер, и рабочим оказывается
                    # он. На стадии 1 извлечения ещё нет, и столбец пуст.
                    "kontakt_iz_teksta": iz_teksta,
                },
                "matchingColumns": [], "schema": [],
            },
            "options": {},
        },
    }


def ai_link(target):
    """Связь «модель → узел» идёт по отдельному каналу `ai_languageModel`,
    а не по обычному `main` — это и есть подключённый узел модели."""
    return {"Модель": {"ai_languageModel": [[{"node": target, "type": "ai_languageModel", "index": 0}]]}}


def stadiya_1():
    chain = {
        "id": "chain", "name": "Шаг модели", "type": "@n8n/n8n-nodes-langchain.chainLlm",
        "typeVersion": 1.7, "position": [260, 0],
        "parameters": {
            "promptType": "define",
            "text": "=Определи одним словом, о чём эта заявка в учебный центр. "
                    "Ответь только словом.\n\nЗаявка: {{ $json['Что нужно'] }}",
            "messages": {}, "batching": {},
        },
    }
    nodes = [form_node("s7-stadiya-1"), chain, model_node([260, 200]),
             table_node("Строка в таблице", "table", [560, 0],
                        "={{ $json.text }}", "")]
    conn = {"Заявка с сайта": {"main": [[{"node": "Шаг модели", "type": "main", "index": 0}]]},
            "Шаг модели": {"main": [[{"node": "Строка в таблице", "type": "main", "index": 0}]]}}
    conn.update(ai_link("Шаг модели"))
    return {"name": "С7 · стадия 1 — три узла", "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


def extractor(pos, retry=False, on_error=None):
    node = {
        "id": "extract", "name": "Извлечение полей",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "text": "={{ $json['Что нужно'] }}",
            "schemaType": "fromAttributes",
            "attributes": {"attributes": [
                {"name": "tema", "type": "string", "required": True,
                 "description": "о чём заявка: курс, перенос занятия, оплата, другое"},
                {"name": "srochnost", "type": "string", "required": True,
                 "description": "когда человек ждёт ответа: сегодня, на неделе, не указано"},
                {"name": "kontakt", "type": "string",
                 "description": "телефон или почта из текста заявки; если их нет — «не указано»"},
            ]},
            "options": {},
        },
    }
    if retry:
        node["retryOnFail"] = True
        node["maxTries"] = 3
        node["waitBetweenTries"] = 2000
    if on_error:
        node["onError"] = on_error
    return node


def stadiya_2():
    nodes = [form_node("s7-stadiya-2"), extractor([260, 0]), model_node([260, 200]),
             table_node("Строка в таблице", "table", [560, 0],
                        "={{ $json.output.tema }}", "={{ $json.output.srochnost }}",
                        "={{ $json.output.kontakt }}")]
    conn = {"Заявка с сайта": {"main": [[{"node": "Извлечение полей", "type": "main", "index": 0}]]},
            "Извлечение полей": {"main": [[{"node": "Строка в таблице", "type": "main", "index": 0}]]}}
    conn.update(ai_link("Извлечение полей"))
    return {"name": "С7 · стадия 2 — значения вместо прозы", "nodes": nodes,
            "connections": conn, "settings": {"executionOrder": "v1"}}


def stadiya_3(name="С7 · стадия 3 — повтор и ветка отказа", path="s7-stadiya-3"):
    ok = table_node("Строка в таблице", "table", [620, -60],
                    "={{ $json.output.tema }}", "={{ $json.output.srochnost }}",
                    "={{ $json.output.kontakt }}")
    bad = table_node("Та же таблица · не разобрано", "table_err", [620, 220],
                     "не разобрано", "не указано")
    nodes = [form_node(path),
             extractor([260, 0], retry=True, on_error="continueErrorOutput"),
             model_node([260, 240]), ok, bad]
    conn = {
        "Заявка с сайта": {"main": [[{"node": "Извлечение полей", "type": "main", "index": 0}]]},
        "Извлечение полей": {"main": [
            [{"node": "Строка в таблице", "type": "main", "index": 0}],
            [{"node": "Та же таблица · не разобрано", "type": "main", "index": 0}],
        ]},
    }
    conn.update(ai_link("Извлечение полей"))
    return {"name": name, "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


def stadiya_4():
    return stadiya_3("С7 · стадия 4 — опубликованная версия", "s7-stadiya-4")


def dlya_studenta():
    """Файл, который уносит студент: стадия 4 без привязок к ЭТОМУ стенду.

    Снимаются `credentials` узла модели и значение таблицы: и то и другое у
    студента своё, а чужой идентификатор в файле выглядит как сломанный узел
    и стоит ему десяти минут недоумения. Поля при этом остаются — узел
    открывается с пустым выбором, что читается правильно: «выбери своё»."""
    wf = stadiya_4()
    wf["name"] = "Семинар 7 — первый работающий процесс"
    for n in wf["nodes"]:
        n.pop("credentials", None)
        if n["type"] == "n8n-nodes-base.dataTable":
            n["parameters"]["dataTableId"] = {"__rl": True, "value": "", "mode": "list"}
        if n["type"] == "n8n-nodes-base.formTrigger":
            n["parameters"]["path"] = "sem-07"
            n["webhookId"] = "sem-07"
    return wf


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


STADII = {"stadiya-1": stadiya_1, "stadiya-2": stadiya_2,
          "stadiya-3": stadiya_3, "stadiya-4": stadiya_4,
          "sem-07-vyhod": dlya_studenta}


def main():
    push = "--push" in sys.argv or "--run" in sys.argv
    for fname, fn in STADII.items():
        wf = fn()
        (HERE / f"{fname}.json").write_text(
            json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  {fname}.json — {len(wf['nodes'])} узлов")
        if push and fname != "sem-07-vyhod":
            existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
            if wf["name"] in existing:
                wid = existing[wf["name"]]
                api("PUT", f"/workflows/{wid}", wf)
                print(f"     обновлён на стенде: {wid}")
            else:
                wid = api("POST", "/workflows", wf)["id"]
                print(f"     создан на стенде: {wid}")


if __name__ == "__main__":
    main()
