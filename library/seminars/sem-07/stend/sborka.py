#!/usr/bin/env python3
"""Собрать четыре стадии учебного процесса Семинара 7 и выложить их на стенд.

Четыре файла — это ОДИН процесс на четырёх стадиях, по кейсам занятия:

    stage-1.json   полный классификатор: форма → извлечение → справочник → таблица → экран
    stage-2.json   справочник встречается с жизнью: две темы, чужая тема, пустой контакт
    stage-3.json   повтор и вторая ветка: отказ вызова виден на том же экране
    stage-4.json   та же стадия 3 — на ней показывается черновик против Publish

`student.json` — то, что уносит студент: стадия 4 без привязок к ЭТОМУ стенду.

## Три требования владельца (2026-10-12), от которых зависит устройство

1. **Результат виден сразу, без переключений.** Каждая стадия заканчивается узлом
   формы (`operation: completion`): в том же окне браузера, где зал только что отправил
   заявку, печатается что пришло, что вернул шаг модели, что решил справочник и что
   легло в таблицу. Ходить в журнал прогонов и в таблицу не нужно — на занятии это
   стоило бы двух переключений экрана на каждый прогон.

2. **Идентификаторы по-английски, не транслитом.** Столбцы таблицы, имена атрибутов,
   пути форм и имена функций здесь — английские. Русскими остаются только ЗНАЧЕНИЯ
   справочников и подписи, которые читает человек: форма, экран результата и подписи
   полей показываются залу по-русски.

3. **Задача решается полностью и достоверно.** Тема и срочность заполнены ВСЕГДА и
   всегда из справочника. Держится это двумя разными средствами, и оба нужны:
   - **схема с перечислением** (`enum` в схеме извлечения) — модель видит допустимые
     значения и не придумывает своих;
   - **узел справочника** (`Vocabulary check`) — последняя инстанция: что не входит в
     список или пришло пустым, становится `другое` / `не указано`, а не пустой
     клеткой. Схема может быть обойдена, справочник — нет.
   Ровно так это и делается в живой классификации: модель предлагает, справочник решает.

**Ключ стенда читается из окружения и в репозиторий не попадает.**
    source ~/.n8n-lab.env && python3 sborka.py --push

    python3 sborka.py              только записать json-файлы рядом
    python3 sborka.py --push       записать, выложить на стенд и опубликовать
"""
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Привязки стенда. Это НЕ секреты — ссылки на уже созданные на стенде таблицу и
# учётные данные модели. В студенческом файле они сняты (см. `student_file`).
TABLE_ID = "xlDAQCm75jLAKNom"
TABLE_NAME = "requests"
CRED_ID = "VbxiQn8TbqA4R2mw"
CRED_NAME = "OpenRouter account"
MODEL = "openai/gpt-4o-mini"

# Справочники. Значения русские — их читает человек на экране результата и в
# таблице; имена полей английские. Последнее значение каждого списка —
# обязательный «иначе»: без него классификация упирается в пустую клетку.
TOPICS = ["курс", "перенос занятия", "оплата", "другое"]
URGENCY = ["сегодня", "на неделе", "не указано"]


def rl(value, name):
    """Поле-ссылка n8n (resource locator) — так узел хранит выбор из списка."""
    return {"__rl": True, "value": value, "mode": "list", "cachedResultName": name}


def model_node(pos):
    return {
        "id": "model", "name": "Model", "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": MODEL, "options": {}},
        "credentials": {"openRouterApi": {"id": CRED_ID, "name": CRED_NAME}},
    }


def form_node(path):
    """Форма с объяснением наверху.

    Первое поле формы — не поле, а блок разметки (`fieldType: html`): прежде чем
    что-то вводить, студент читает, ЧТО с его текстом произойдёт и в каком
    порядке. Блоки пронумерованы теми же номерами, что узлы на схеме занятия и
    разделы экрана результата (требование владельца 2026-10-12: нумерация
    должна биться, чтобы соответствие не приходилось додумывать)."""
    vvodnaya = (
        "<div style=\"font-size:14px;line-height:1.5\">"
        "<p style=\"margin:0 0 10px\">Заявка пройдёт <b>пять шагов</b>. "
        "После отправки вы увидите каждый из них на одном экране.</p>"
        "<p style=\"margin:0 0 6px\"><b>1 · Форма</b> — то, что вы сейчас заполните: "
        "имя, контакт и свободный текст. Писать можно как человеку, без формата.</p>"
        "<p style=\"margin:0 0 6px\"><b>2 · Извлечение</b> — шаг модели достаёт из текста "
        "<i>тему</i>, <i>срочность</i> и <i>контакт, указанный в тексте</i>.</p>"
        "<p style=\"margin:0 0 6px\"><b>3 · Справочник</b> — сверяет тему и срочность со "
        "списком допустимых значений. Что не из списка или пусто — станет "
        "«другое» и «не указано».</p>"
        "<p style=\"margin:0 0 6px\"><b>4 · Запись</b> — строка уходит в таблицу заявок.</p>"
        "<p style=\"margin:0 0 10px\"><b>5 · Экран результата</b> — покажет все четыре "
        "шага подряд, здесь же.</p>"
        "<p style=\"margin:0\"><b>Справочники:</b> тема — " + " · ".join(TOPICS) +
        "; срочность — " + " · ".join(URGENCY) + ".</p>"
        "</div>")
    return {
        "id": "form", "name": "Request form", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-180, 0], "webhookId": path,
        "parameters": {
            "path": path,
            "formTitle": "Заявка в учебный центр",
            "formDescription": "Так выглядит вход процесса, который мы собираем",
            "formFields": {"values": [
                {"fieldType": "html", "html": vvodnaya},
                {"fieldLabel": "Имя", "requiredField": True},
                {"fieldLabel": "Контакт", "placeholder": "телефон или почта",
                 "requiredField": True},
                {"fieldLabel": "Что нужно", "fieldType": "textarea",
                 "placeholder": "Напишите своими словами — например: "
                                "«хочу на курс по аналитике, перезвоните сегодня»",
                 "requiredField": True},
            ]},
            "options": {"appendAttribution": False},
        },
    }


def extractor(pos, retry=False, on_error=None, with_extra=False):
    """Извлечение полей со схемой, в которой справочник задан перечислением.

    Схема задаётся вручную (`schemaType: manual`), а не описаниями атрибутов:
    описание словами допустимые значения только ПРЕДЛАГАЕТ, а `enum` их
    ПЕРЕЧИСЛЯЕТ, и инструмент требует от модели одно из них."""
    schema = {
        "type": "object",
        "properties": {
            "topic": {"type": "string", "enum": TOPICS,
                      "description": "о чём заявка; если ни одно не подходит — «другое»"},
            "urgency": {"type": "string", "enum": URGENCY,
                        "description": "когда человек ждёт ответа; если не сказано — «не указано»"},
            "contact_from_text": {
                "type": "string",
                "description": "телефон или почта, указанные В ТЕКСТЕ заявки; "
                               "если в тексте их нет — пустая строка"},
        },
        "required": ["topic", "urgency"],
    }
    if with_extra:
        # Кейс 2: главная тема плюс пометка. Без этого поля вторая тема заявки
        # исчезает молча — проверено прогонами стадии 1.
        schema["properties"]["extra_topics"] = {
            "type": "string",
            "description": "остальные темы из этого же списка, если в заявке их "
                           "несколько, через запятую; если тема одна — пустая строка",
        }
    node = {
        "id": "extract", "name": "Extract fields",
        "type": "@n8n/n8n-nodes-langchain.informationExtractor",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "text": "={{ $json['Что нужно'] }}",
            "schemaType": "manual",
            "inputSchema": json.dumps(schema, ensure_ascii=False, indent=2),
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


def vocabulary_node(pos, with_extra=False):
    """Последняя инстанция справочника: клетка не остаётся пустой и не содержит
    значения вне списка. Узел обычный — «задать поля», без кода."""
    topics = json.dumps(TOPICS, ensure_ascii=False)
    urgency = json.dumps(URGENCY, ensure_ascii=False)
    return {
        "id": "vocab", "name": "Vocabulary check", "type": "n8n-nodes-base.set",
        "typeVersion": 3.4, "position": pos,
        "parameters": {
            "mode": "manual",
            "includeOtherFields": True,
            "assignments": {"assignments": [
                {"id": "a1", "name": "topic", "type": "string",
                 "value": "={{ " + topics + ".includes($json.output.topic) "
                          "? $json.output.topic : 'другое' }}"},
                {"id": "a2", "name": "urgency", "type": "string",
                 "value": "={{ " + urgency + ".includes($json.output.urgency) "
                          "? $json.output.urgency : 'не указано' }}"},
                {"id": "a3", "name": "contact_from_text", "type": "string",
                 "value": "={{ $json.output.contact_from_text || '' }}"},
                {"id": "a4", "name": "status", "type": "string", "value": "ok"},
            ] + ([{
                "id": "a5", "name": "extra_topics", "type": "string",
                # Пометка проходит ту же сверку, что и тема: в столбец попадают
                # только значения справочника, и никогда — выдумка.
                "value": "={{ ($json.output.extra_topics || '').split(',')"
                         ".map(s => s.trim()).filter(s => " + topics + ".includes(s))"
                         ".join(' · ') }}",
            }] if with_extra else [])},
            "options": {},
        },
    }


def table_node(name, node_id, pos, from_vocab=True):
    """Запись строки. Значения берутся у узла справочника, а не у модели —
    именно поэтому в таблице не бывает ни пустой темы, ни темы вне списка."""
    if from_vocab:
        vals = {
            "topic": "={{ $json.topic }}",
            "urgency": "={{ $json.urgency }}",
            "contact_from_text": "={{ $json.contact_from_text }}",
            "status": "={{ $json.status }}",
            "extra_topics": "={{ $json.extra_topics || '' }}",
        }
    else:
        vals = {"topic": "другое", "urgency": "не указано",
                "contact_from_text": "", "status": "not_parsed",
                "extra_topics": ""}
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.dataTable",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "operation": "insert",
            "dataTableId": rl(TABLE_ID, TABLE_NAME),
            "columns": {
                "mappingMode": "defineBelow",
                "value": dict({
                    "received_at": "={{ $now.toISO() }}",
                    "name": "={{ $('Request form').item.json['Имя'] }}",
                    "contact": "={{ $('Request form').item.json['Контакт'] }}",
                    "request_text": "={{ $('Request form').item.json['Что нужно'] }}",
                }, **vals),
                "matchingColumns": [], "schema": [],
            },
            "options": {},
        },
    }


def result_screen(node_id, pos, failed=False):
    """Экран результата — схема, пройденная по шагам, в том же окне браузера.

    Разделы пронумерованы и названы ТЕМИ ЖЕ словами, что узлы на схеме занятия
    и блоки вводной на форме (требование владельца 2026-10-12). Соответствие
    «что я вижу» ↔ «какой это узел» не нужно додумывать: номер совпадает."""
    def blok(num, imya, telo):
        return ("<div style=\"margin:0 0 14px;padding:10px 12px;"
                "border-left:3px solid #1C7293;background:#F4F7FA\">"
                "<div style=\"font-size:12px;color:#5B6B7F;letter-spacing:.04em\">"
                "ШАГ " + str(num) + "</div>"
                "<div style=\"font-weight:700;margin:2px 0 6px\">" + imya + "</div>"
                "<div style=\"line-height:1.5\">" + telo + "</div></div>")

    if failed:
        body = "=" + (
            blok(1, "Форма",
                 "{{ $('Request form').item.json['Что нужно'] }}") +
            blok(2, "Извлечение",
                 "<b style=\"color:#B3261E\">вызов не удался</b> — три попытки с "
                 "паузой по две секунды, все три неудачны") +
            blok(3, "Справочник",
                 "тема → <b>другое</b><br>срочность → <b>не указано</b><br>"
                 "<i>справочник сработал и на отказе: пустых клеток нет</i>") +
            blok(4, "Запись",
                 "строка в таблице есть, <b>status = not_parsed</b><br>"
                 "<i>заявка не потеряна — её видно по этому столбцу</i>"))
        title = "Заявка принята, но не разобрана"
    else:
        body = "=" + (
            blok(1, "Форма",
                 "{{ $('Request form').item.json['Что нужно'] }}") +
            blok(2, "Извлечение — что предложила модель",
                 "тема: <b>{{ $('Extract fields').item.json.output.topic }}</b><br>"
                 "срочность: <b>{{ $('Extract fields').item.json.output.urgency }}</b><br>"
                 "контакт из текста: "
                 "<b>{{ $('Extract fields').item.json.output.contact_from_text || '—' }}</b>") +
            blok(3, "Справочник — что осталось после сверки",
                 "тема: <b>{{ $('Vocabulary check').item.json.topic }}</b><br>"
                 "срочность: <b>{{ $('Vocabulary check').item.json.urgency }}</b><br>"
                 "ещё в заявке: "
                 "<b>{{ $('Vocabulary check').item.json.extra_topics || '—' }}</b>") +
            blok(4, "Запись",
                 "строка <b>{{ $json.id }}</b> в таблице requests, "
                 "status = <b>{{ $json.status }}</b>"))
        title = "Заявка разобрана"
    return {
        "id": node_id, "name": "Result screen", "type": "n8n-nodes-base.form",
        "typeVersion": 1, "position": pos,
        "parameters": {
            "operation": "completion",
            "respondWith": "text",
            "completionTitle": title,
            "completionMessage": body,
            "options": {"appendAttribution": False},
        },
    }


def ai_link(target):
    """Связь «модель → узел» идёт по отдельному каналу `ai_languageModel`,
    а не по обычному `main` — это и есть подключённый узел модели."""
    return {"Model": {"ai_languageModel": [[
        {"node": target, "type": "ai_languageModel", "index": 0}]]}}


def chain(nodes, extra=None):
    """Связи «один за другим» по именам узлов, в порядке списка."""
    conn = {}
    for a, b in zip(nodes, nodes[1:]):
        conn[a] = {"main": [[{"node": b, "type": "main", "index": 0}]]}
    if extra:
        conn.update(extra)
    return conn


def stage_1(name="С7 · стадия 1 — полный классификатор", path="s7-stage-1",
            with_extra=False):
    nodes = [form_node(path), extractor([60, 0], with_extra=with_extra),
             model_node([60, 220]), vocabulary_node([300, 0], with_extra=with_extra),
             table_node("Write row", "table", [540, 0]),
             result_screen("screen", [780, 0])]
    conn = chain(["Request form", "Extract fields", "Vocabulary check",
                  "Write row", "Result screen"], ai_link("Extract fields"))
    return {"name": name, "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


def stage_2():
    """Стадия 2 отличается от первой НЕ строением, а тем, что на ней прогоняют:
    заявку с двумя темами, заявку не про наши темы и заявку без контакта.
    Отдельный сценарий нужен, чтобы на занятии первая стадия осталась целой для
    сравнения, а не правилась на глазах у зала."""
    return stage_1("С7 · стадия 2 — справочник и жизнь", "s7-stage-2",
                   with_extra=True)


def stage_3(name="С7 · стадия 3 — повтор и ветка отказа", path="s7-stage-3"):
    nodes = [form_node(path),
             extractor([60, 0], retry=True, on_error="continueErrorOutput",
                       with_extra=True),
             model_node([60, 260]), vocabulary_node([300, -80], with_extra=True),
             table_node("Write row", "table", [540, -80]),
             result_screen("screen", [780, -80]),
             table_node("Write row · not parsed", "table_err", [360, 200], from_vocab=False),
             result_screen("screen_err", [620, 200], failed=True)]
    conn = {
        "Request form": {"main": [[{"node": "Extract fields", "type": "main", "index": 0}]]},
        "Extract fields": {"main": [
            [{"node": "Vocabulary check", "type": "main", "index": 0}],
            [{"node": "Write row · not parsed", "type": "main", "index": 0}],
        ]},
        "Vocabulary check": {"main": [[{"node": "Write row", "type": "main", "index": 0}]]},
        "Write row": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Write row · not parsed": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
    }
    conn.update(ai_link("Extract fields"))
    # Экран отказа — отдельный узел, поэтому связь выше ведёт в него, не в общий.
    conn["Write row · not parsed"] = {"main": [[
        {"node": "Result screen", "type": "main", "index": 0}]]}
    nodes[7]["name"] = "Result screen · not parsed"
    conn["Write row · not parsed"]["main"][0][0]["node"] = "Result screen · not parsed"
    return {"name": name, "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


def stage_4():
    return stage_3("С7 · стадия 4 — опубликованная версия", "s7-stage-4")


def student_file():
    """Файл, который уносит студент: стадия 4 без привязок к ЭТОМУ стенду.

    Снимаются `credentials` узла модели и выбор таблицы: и то и другое у студента
    своё, а чужой идентификатор читается как сломанный узел и стоит ему десяти
    минут недоумения. Поля остаются — узел открывается с пустым выбором, что
    читается правильно: «выбери своё»."""
    wf = stage_4()
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


STAGES = {"stage-1": stage_1, "stage-2": stage_2, "stage-3": stage_3,
          "stage-4": stage_4, "student": student_file}


def main():
    push = "--push" in sys.argv
    existing = {}
    if push:
        existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    for fname, fn in STAGES.items():
        wf = fn()
        (HERE / f"{fname}.json").write_text(
            json.dumps(wf, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"  {fname}.json — {len(wf['nodes'])} узлов")
        if not push or fname == "student":
            continue
        if wf["name"] in existing:
            wid = existing[wf["name"]]
            api("PUT", f"/workflows/{wid}", wf)
            action = "обновлён"
        else:
            wid = api("POST", "/workflows", wf)["id"]
            action = "создан"
        # Publish обязателен: без него боевые прогоны пойдут по прежней версии —
        # ровно то, про что кейс 4.
        api("POST", f"/workflows/{wid}/publish", {})
        print(f"     {action} и опубликован: {wid}")


if __name__ == "__main__":
    main()
