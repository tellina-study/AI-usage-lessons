#!/usr/bin/env python3
"""Собрать стенд повторного Замера Кейса 5 Семинара 9 (трудный случай) — issue #299.

Предыдущий Замер 3.1 (`stend/zamery-k5-k6/README.md`) взял вопрос с ДВУМЯ жёстко
зафиксированными в базе деталями («когда вернут деньги за отменённый курс?») — 25 из 25
повторов при T=0 дали ОДИНАКОВЫЙ ответ по существу, различие было только формулировочным.
Причина установлена в `ARCHITECTURE.md`/находках `research/03`: разброс живёт там, где
ответ нужно СОСТАВИТЬ, а не найти готовым в базе. Этот заход берёт три вопроса именно
такого типа — трудный случай, по аналогии с тем, как `stend/zamery-k1-k3/README.md`
(Замер 1) взял трудные вопросы для Кейса 1 вместо лёгких.

Три сценария, все — копия процесса Кейса 1 версии 1 (свободный ответ, `chainLlm`, база
знаний целиком в промте из `stend/sborka.py`), с явной `Sampling Temperature=0`, имя
начинается на «С9 · замер K5п », вебхук — на `s9-m5p-`:

    k5p-arith.json      Арифметика внутри ответа. Клиент называет свои числа (сумма,
                         сколько занятий прошло из скольких) — в базе (`kb4`) нет готовой
                         формулы для этого случая (там есть только порог 3000 ₽ и срок 10
                         дней для ПОЛНОГО возврата при отмене курса), модели нужно
                         СОСТАВИТЬ способ счёта самой. Мерить: сколько РАЗНЫХ итоговых
                         чисел на 10 повторов.
    k5p-boundary.json   Вопрос на границе правила `kb4` — сумма РОВНО 3000 ₽ (порог
                         «решение проходит через руководителя» сформулирован как «суммы
                         ВЫШЕ 3000 рублей»; 3000 не выше 3000 по букве правила, но это
                         ровно тот формат фразы, который легко прочитать как «от 3000»).
                         Мерить: перекидывается ли РЕШЕНИЕ (обычный порядок / через
                         руководителя) между повторами на одном и том же входе.
    k5p-combo.json      Вопрос, который покрыт не одним, а двумя пунктами базы сразу —
                         `kb6` (пропуск без предупреждения, бесплатного повтора нет) и
                         `kb5` (пересдачи идут каждую вторую субботу месяца). Пункты в
                         напряжении друг с другом: `kb6` запрещает бесплатную пересдачу
                         именно в этом случае, `kb5` описывает расписание пересдач вообще.
                         Мерить: называются ли оба пункта (или хотя бы консистентный
                         набор) и совпадает ли итоговое решение (пересдача положена / нет)
                         между повторами.

## Ключи и зона

Ключи — только из /home/harness/.n8n-lab-credentials через окружение. Правка этой сессии
ограничена `sem-09/stend/zamery-k5-povtorno/` — ни один узел С7/С8/С9-производства, ни
`zamery-k1-k3`/`zamery-k4`/`zamery-k5-k6` этим файлом не трогается (оттуда только читается
`stend/sborka.py` для базы знаний и формы вопроса, импортом модуля, без правок).

    python3 sborka.py                                      только записать json рядом
    N8N_API_URL=... N8N_API_KEY=... python3 sborka.py --push   выложить и опубликовать

`OpenRouter account` (`VbxiQn8TbqA4R2mw`) — существующий credential стенда, переиспользован
без новой инфраструктуры. Модель — `qwen/qwen-2.5-7b-instruct` (та же, что у Кейса 1 С9 и
Замера 3.1/3.2) — проверено `GET https://openrouter.ai/api/v1/models` 2026-10-25, этот id
ещё числится валидным (в отличие от vision-модели предыдущего замера, где id за сутки
перестал существовать).
"""
import importlib.util
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
STEND = HERE.parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Импорт модулем по пути (не `sys.path.insert` + `import sborka`) — тот же приём, что
# `zamery-k5-k6/sborka.py`: несколько файлов в этой цепочке называются одинаково
# `sborka.py`, обычный `import sborka` коллизирует через общий ключ `sys.modules`.
_spec = importlib.util.spec_from_file_location(
    "sem09_stend_sborka", str((STEND / "sborka.py").resolve()))
s9 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(s9)

OPENROUTER_CRED = s9.OPENROUTER_CRED
ANSWER_MODEL = s9.ANSWER_MODEL  # qwen/qwen-2.5-7b-instruct — проверено валидным 2026-10-25


def _free_answer_workflow(path, name, node_label, question_fixed):
    """Общий каркас — тот же, что `zamery-k5-k6.k5_repeat()`: Form Trigger -> model(T=0)
    -> chainLlm (свободный ответ, база целиком в промте) -> Result screen. Вопрос ФИКСИРОВАН
    в самом workflow (не параметр формы) — чтобы прогонщик мог слать один и тот же текст
    10 раз без риска опечатки между повторами; поле формы всё равно существует и заполняется
    тем же текстом (для единообразия с остальными сценариями стенда и ради читаемого экрана
    результата), но содержательно вопрос — константа этого workflow.
    """
    nodes = [s9.client_question_form(path)]
    nodes.append({
        "id": "k5p_model", "name": f"Model ({node_label}, T=0)",
        "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter", "typeVersion": 1,
        "position": [60, 220],
        "parameters": {"model": ANSWER_MODEL, "options": {"temperature": 0}},
        "credentials": OPENROUTER_CRED,
    })
    nodes.append({
        "id": "k5p_answer", "name": f"Answer ({node_label}, T=0)",
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5,
        "position": [60, 0],
        "parameters": {
            "promptType": "define",
            "text": (
                "=Ты — ассистент поддержки учебного центра. Ниже база знаний, которой "
                "можно пользоваться для ответа.\n\n" + s9.kb_text() + "\n\nВопрос клиента: "
                "{{ $json['Вопрос'] }}\n\nОтветь по существу и по-русски, коротко (2-4 "
                "предложения). Если ответа в базе знаний нет и ты не уверена — честно "
                "напиши, что не знаешь, и что ответит сотрудник. Если уверена — отвечай "
                "прямо, без оговорок."
            ),
            "options": {},
        },
    })
    nodes.append({
        "id": "k5p_result", "name": "Result screen", "type": "n8n-nodes-base.form",
        "typeVersion": 1, "position": [300, 0],
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": f"Ответ (замер K5п — {node_label})",
            "completionMessage": "=Вопрос: {{ $('Client question').item.json['Вопрос'] "
                                  "}}<br><br>Ответ: {{ $('" + f"Answer ({node_label}, T=0)"
                                  + "').item.json.text }}",
            "options": {"appendAttribution": False},
        },
    })
    answer_node_name = f"Answer ({node_label}, T=0)"
    model_node_name = f"Model ({node_label}, T=0)"
    conn = {
        "Client question": {"main": [[{"node": answer_node_name, "type": "main", "index": 0}]]},
        answer_node_name: {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        model_node_name: {"ai_languageModel": [[
            {"node": answer_node_name, "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": name, "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


# Вопросы фиксированы здесь же (не только в прогонщике) — это содержательная часть
# сборки, не только испытания; каждый прогонщик должен слать РОВНО этот текст все 10 раз.
QUESTION_ARITH = (
    "Я оплатил курс из 10 занятий на сумму 24000 рублей. Прошло 3 занятия, дальше ходить "
    "не смогу — хочу вернуть деньги за оставшиеся занятия. Сколько мне должны вернуть?")
QUESTION_BOUNDARY = (
    "Я заплатил за курс 3000 рублей и хочу оформить возврат. Решение по моему возврату "
    "будет принимать руководитель, или это пройдёт по обычному порядку?")
QUESTION_COMBO = (
    "Я пропустил занятие без предупреждения. Когда будет следующая пересдача, чтобы я "
    "мог на неё попасть?")


def k5p_arith():
    return _free_answer_workflow(
        "s9-m5p-arith", "С9 · замер K5п — арифметика внутри ответа", "arith", QUESTION_ARITH)


def k5p_boundary():
    return _free_answer_workflow(
        "s9-m5p-boundary", "С9 · замер K5п — граница правила", "boundary", QUESTION_BOUNDARY)


def k5p_combo():
    return _free_answer_workflow(
        "s9-m5p-combo", "С9 · замер K5п — комбинация двух пунктов", "combo", QUESTION_COMBO)


def api(method, path, body=None):
    import urllib.request
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


STAGES = {"k5p-arith": k5p_arith, "k5p-boundary": k5p_boundary, "k5p-combo": k5p_combo}


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
        if not push:
            continue
        if wf["name"] in existing:
            wid = existing[wf["name"]]
            api("PUT", f"/workflows/{wid}", wf)
            action = "обновлён"
        else:
            wid = api("POST", "/workflows", wf)["id"]
            action = "создан"
        api("POST", f"/workflows/{wid}/publish", {})
        print(f"     {action} и опубликован: {wid}")


if __name__ == "__main__":
    main()
