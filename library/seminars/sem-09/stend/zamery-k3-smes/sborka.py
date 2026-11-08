#!/usr/bin/env python3
"""Собрать стенд «смесь экспертов» — issue #299, задание З4 (замена 4-й строки Кейса 3).

Владелец (расшифровка `../../qa/kommentarii/kommentarii-2026-10-29.md`, 27:20 и 27:50):
нынешний 4-й вариант проверки ответа («несколько прогонов, берём самый частый ответ»)
меняется на «смесь экспертов»: несколько МАЛЕНЬКИХ моделей решают задачу одновременно, а
модель-решатель выбирает лучший ответ. Задача и корпус — ТЕ ЖЕ, что в `../zamery-k1-k3/`
(Замер 2/4 этого же кейса), иначе новый вариант нельзя сравнить с остальными тремя.

Два сценария:

    s9-m3-mix           основной замер. Pick KB item -> три эксперта генерируют ответ НА ТОТ
                         ЖЕ вопрос независимо (temperature=0, разные модели) -> решатель
                         (структурированный вердикт) выбирает лучший из трёх (A/B/C).
                         4 вызова модели на вопрос (3 эксперта + 1 решатель).

    s9-m3-mix-resolver   решатель БЕЗ генерации — принимает три уже готовых текста ответа
                         (через поля формы) и тот же вопрос, выбирает лучший. Нужен для
                         проверки устойчивости выбора к порядку (Часть Б.5 задания): те же
                         три текста подаются во ВTOРОЙ раз в переставленном порядке, без
                         повторной генерации — только решатель вызывается снова.

Эксперты — три МАЛЕНЬКИЕ модели РАЗНЫХ семейств (проверено доступность прямым
`GET https://openrouter.ai/api/v1/models`, без авторизации, 2026-10-29 — список моделей
провайдера двигается, прежняя попытка этого же семинара уже спотыкалась на несуществующем
id `mistralai/mistral-7b-instruct`, он снят из каталога; взят `mistralai/ministral-8b-2512`,
тот же класс размера 7-8B, другое семейство):

    qwen/qwen-2.5-7b-instruct          (Alibaba Qwen)
    meta-llama/llama-3.1-8b-instruct   (Meta Llama)
    mistralai/ministral-8b-2512        (Mistral AI)

Решатель — `qwen/qwen-2.5-7b-instruct`, ТА ЖЕ модель, что в `zamery-k1-k3` стоит судьёй
(`s9-m3-judge`) — иначе цена и поведение «смеси экспертов» нельзя было бы честно поставить
рядом со строкой «судья» на n40.

Промт решателя НЕ содержит кодового вердикта и не говорит, какой вариант от какой модели —
решатель судит по тексту трёх вариантов и правилам, а не копирует готовый ярлык (см.
`proverka_protechki.py`).

Ключи — только из переменных окружения (`N8N_API_URL`, `N8N_API_KEY`).
"""
import importlib.util as _ilu
import json
import os
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
API = os.environ.get("N8N_API_URL", "")
KEY = os.environ.get("N8N_API_KEY", "")

# Тот же корпус и те же пункты базы, что в zamery-k1-k3 (Замер 2/4 Кейса 3) — импортом
# модуля, не копией, чтобы расхождение корпуса было физически невозможно.
_spec = _ilu.spec_from_file_location(
    "sem09_mix_sborka_zamer3", str(HERE.parent / "zamery-k1-k3" / "sborka_zamer3.py"))
z3 = _ilu.module_from_spec(_spec)
_spec.loader.exec_module(z3)

TEST_QUESTIONS = z3.TEST_QUESTIONS
QMAP_JS = z3.QMAP_JS
CONTACTS_JS = z3.CONTACTS_JS
judge_criteria_text = z3.judge_criteria_text

OPENROUTER_CRED = {"openRouterApi": {"id": "VbxiQn8TbqA4R2mw", "name": "OpenRouter account"}}

# Три маленьких эксперта, три разных семейства — проверено GET /models, см. docstring.
EXPERTS = [
    ("qwen", "qwen/qwen-2.5-7b-instruct"),
    ("llama", "meta-llama/llama-3.1-8b-instruct"),
    ("ministral", "mistralai/ministral-8b-2512"),
]
RESOLVER_MODEL = "qwen/qwen-2.5-7b-instruct"  # та же модель, что судья в zamery-k1-k3


def form_trigger(path, fields):
    return {
        "id": "q_form", "name": "Client question", "type": "n8n-nodes-base.formTrigger",
        "typeVersion": 2.2, "position": [-320, 0], "webhookId": path,
        "parameters": {
            "path": path, "formTitle": "Замер «смесь экспертов» — вопрос",
            "formDescription": "Измерительный стенд Семинара 9, не форма студента",
            "formFields": {"values": [
                {"fieldLabel": f, "fieldType": "textarea", "requiredField": True}
                for f in fields
            ]},
            "options": {"appendAttribution": False},
        },
    }


def pick_kb_item_node(pos):
    """Та же логика сопоставления вопроса с пунктом базы, что в zamery-k1-k3 — без счётчика
    попыток (смесь экспертов не переделывает, решатель выбирает за один проход)."""
    js = (
        "const inp = $input.item.json;\n"
        "const question = inp.question || inp['Вопрос'] || '';\n"
        "const MAP = [\n" + QMAP_JS + "\n];\n"
        "let picked = null;\n"
        "for (const m of MAP) { if (question.includes(m.match)) { picked = m; break; } }\n"
        "if (!picked) picked = MAP[0];\n"
        "return { json: {\n"
        "  question,\n"
        "  kb_id: picked.kb_id, kb_text: picked.kb_text, kb_keyword: picked.kb_keyword,\n"
        "  kb_keyword_pattern: picked.kb_keyword_pattern,\n"
        "  kb_numbers: picked.kb_numbers,\n"
        "} };\n"
    )
    return {
        "id": "pick_kb", "name": "Pick KB item", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": pos,
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript", "jsCode": js},
    }


def model_node(node_id, name, pos, model):
    return {
        "id": node_id, "name": name, "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
        "typeVersion": 1, "position": pos,
        "parameters": {"model": model, "options": {"temperature": 0}},
        "credentials": OPENROUTER_CRED,
    }


def generate_expert_node(node_id, name, pos, kb_ref):
    """Один эксперт решает задачу независимо. ТОТ ЖЕ набор требований к ответу, что в
    zamery-k1-k3 (generate_answer_node) — иначе сравнение «смесь» vs «код»/«судья» было бы
    про другую задачу. Требуемая деталь (`kb_keyword`) — это ПРАВИЛО формы ответа (как и в
    уже измеренных вариантах), не секретный правильный ответ: то же самое уже стоит в
    промте генератора у code/judge/combo, не новый риск протечки (см. proverka_protechki.py
    пункт про это разграничение)."""
    prompt = (
        "=Ты — ассистент поддержки учебного центра. Вот точный пункт базы знаний, на "
        f"который должен опираться ответ:\n\n{{{{ {kb_ref}.item.json.kb_text }}}}\n\n"
        f"Вопрос клиента: {{{{ {kb_ref}.item.json.question }}}}\n\n"
        "Напиши короткий ответ клиенту. СТРОГИЕ требования:\n"
        "1. Не длиннее 280 символов.\n"
        f"2. Явно включи деталь: «{{{{ {kb_ref}.item.json.kb_keyword }}}}».\n"
        "3. Укажи, куда обращаться дальше — администратор, личный кабинет, преподаватель, "
        "сотрудник или руководитель.\n"
        "4. Не используй никаких чисел, кроме тех, что есть в приведённом пункте базы.\n"
        "5. Пиши полностью на русском языке — никакой латиницы и иероглифов."
    )
    return {
        "id": node_id, "name": name,
        "type": "@n8n/n8n-nodes-langchain.chainLlm", "typeVersion": 1.5, "position": pos,
        "parameters": {"promptType": "define", "text": prompt, "options": {}},
    }


def resolver_schema():
    return {
        "type": "object",
        "properties": {
            "choice": {"type": "string", "enum": ["A", "B", "C"],
                       "description": "какой из трёх вариантов лучше всех соответствует "
                                      "правилам — ровно одна буква"},
            "reasoning": {"type": "string",
                          "description": "почему выбран этот вариант, и что не так с "
                                         "двумя остальными"},
        },
        "required": ["choice", "reasoning"],
    }


def resolver_text(kb_ref, a_expr, b_expr, c_expr):
    """Промт решателя. НЕ содержит кодового вердикта и не называет, какая модель за какой
    буквой — решатель видит только три текста и правила. См. proverka_protechki.py."""
    return (
        f"=Пункт базы знаний:\n{{{{ {kb_ref}.item.json.kb_text }}}}\n\n"
        f"Вопрос клиента: {{{{ {kb_ref}.item.json.question }}}}\n\n"
        "Три варианта ответа на этот вопрос (от разных источников, тебе не известно, "
        "от какого именно — суди только по тексту):\n\n"
        f"Вариант A: {a_expr}\n\n"
        f"Вариант B: {b_expr}\n\n"
        f"Вариант C: {c_expr}\n\n"
        "Правила, которым должен соответствовать лучший вариант:\n" + judge_criteria_text(
            f"{{{{ {kb_ref}.item.json.kb_keyword }}}}") + "\n\n"
        "Выбери, какой из трёх вариантов (A, B или C) лучше всех соответствует правилам, "
        "и объясни, что не так с двумя другими."
    )


def resolver_verdict_node(node_id, name, pos, text):
    return {
        "id": node_id, "name": name,
        "type": "@n8n/n8n-nodes-langchain.informationExtractor", "typeVersion": 1,
        "position": pos,
        "parameters": {
            "text": text, "schemaType": "manual",
            "inputSchema": json.dumps(resolver_schema(), ensure_ascii=False, indent=2),
            "options": {},
        },
    }


def result_screen_node(node_id, name, pos, title, message):
    return {
        "id": node_id, "name": name, "type": "n8n-nodes-base.form", "typeVersion": 1,
        "position": pos,
        "parameters": {
            "operation": "completion", "respondWith": "text",
            "completionTitle": title, "completionMessage": message,
            "options": {"appendAttribution": False},
        },
    }


# ---------------------------------------------------------------------------------------
# s9-m3-mix — основной замер: 3 эксперта независимо -> решатель выбирает
# ---------------------------------------------------------------------------------------

def case_mix():
    path = "s9-m3-mix"
    pos_x = {"pick": -40, "qwen": 200, "llama": 420, "ministral": 640, "resolver": 860,
              "result": 1080}
    nodes = [
        form_trigger(path, ["Вопрос"]),
        pick_kb_item_node([pos_x["pick"], 0]),
        model_node("m_e_qwen", "Model (qwen)", [pos_x["qwen"], 180], EXPERTS[0][1]),
        generate_expert_node("e_qwen", "Generate (qwen)", [pos_x["qwen"], 0],
                              "$('Pick KB item')"),
        model_node("m_e_llama", "Model (llama)", [pos_x["llama"], 180], EXPERTS[1][1]),
        generate_expert_node("e_llama", "Generate (llama)", [pos_x["llama"], 0],
                              "$('Pick KB item')"),
        model_node("m_e_ministral", "Model (ministral)", [pos_x["ministral"], 180],
                   EXPERTS[2][1]),
        generate_expert_node("e_ministral", "Generate (ministral)", [pos_x["ministral"], 0],
                              "$('Pick KB item')"),
        model_node("m_resolver", "Model (resolver)", [pos_x["resolver"], 180],
                   RESOLVER_MODEL),
        resolver_verdict_node(
            "resolver", "Resolver verdict", [pos_x["resolver"], 0],
            resolver_text("$('Pick KB item')",
                           "{{ $('Generate (qwen)').item.json.text }}",
                           "{{ $('Generate (llama)').item.json.text }}",
                           "{{ $('Generate (ministral)').item.json.text }}")),
        result_screen_node(
            "result_mix", "Result screen", [pos_x["result"], 0],
            "Смесь экспертов — ответ",
            "=Вопрос: {{ $('Pick KB item').item.json.question }}<br><br>"
            "Выбор решателя: {{ $json.output.choice }}"),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Generate (qwen)", "type": "main", "index": 0}]]},
        "Generate (qwen)": {"main": [[
            {"node": "Generate (llama)", "type": "main", "index": 0}]]},
        "Generate (llama)": {"main": [[
            {"node": "Generate (ministral)", "type": "main", "index": 0}]]},
        "Generate (ministral)": {"main": [[
            {"node": "Resolver verdict", "type": "main", "index": 0}]]},
        "Resolver verdict": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (qwen)": {"ai_languageModel": [[
            {"node": "Generate (qwen)", "type": "ai_languageModel", "index": 0}]]},
        "Model (llama)": {"ai_languageModel": [[
            {"node": "Generate (llama)", "type": "ai_languageModel", "index": 0}]]},
        "Model (ministral)": {"ai_languageModel": [[
            {"node": "Generate (ministral)", "type": "ai_languageModel", "index": 0}]]},
        "Model (resolver)": {"ai_languageModel": [[
            {"node": "Resolver verdict", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · смесь экспертов", "nodes": nodes, "connections": conn,
            "settings": {"executionOrder": "v1"}}


# ---------------------------------------------------------------------------------------
# s9-m3-mix-resolver — решатель отдельно, над УЖЕ ГОТОВЫМИ тремя текстами (для проверки
# устойчивости выбора к порядку, Часть Б.5 задания — те же тексты, другой порядок букв)
# ---------------------------------------------------------------------------------------

def case_mix_resolver_only():
    path = "s9-m3-mix-resolver"
    pick_js = (
        "const inp = $input.item.json;\n"
        "const question = inp['Вопрос'] || '';\n"
        "const a = inp['ОтветA'] || '';\n"
        "const b = inp['ОтветB'] || '';\n"
        "const c = inp['ОтветC'] || '';\n"
        "const MAP = [\n" + QMAP_JS + "\n];\n"
        "let picked = null;\n"
        "for (const m of MAP) { if (question.includes(m.match)) { picked = m; break; } }\n"
        "if (!picked) picked = MAP[0];\n"
        "return { json: {\n"
        "  question, answer_a: a, answer_b: b, answer_c: c,\n"
        "  kb_id: picked.kb_id, kb_text: picked.kb_text, kb_keyword: picked.kb_keyword,\n"
        "  kb_numbers: picked.kb_numbers,\n"
        "} };\n"
    )
    pick = {
        "id": "pick_kb_ro", "name": "Pick KB item", "type": "n8n-nodes-base.code",
        "typeVersion": 2, "position": [-40, 0],
        "parameters": {"mode": "runOnceForEachItem", "language": "javaScript",
                        "jsCode": pick_js},
    }
    nodes = [
        form_trigger(path, ["Вопрос", "ОтветA", "ОтветB", "ОтветC"]),
        pick,
        model_node("m_resolver_ro", "Model (resolver)", [200, 180], RESOLVER_MODEL),
        resolver_verdict_node(
            "resolver_ro", "Resolver verdict", [200, 0],
            resolver_text("$('Pick KB item')",
                           "{{ $('Pick KB item').item.json.answer_a }}",
                           "{{ $('Pick KB item').item.json.answer_b }}",
                           "{{ $('Pick KB item').item.json.answer_c }}")),
        result_screen_node(
            "result_ro", "Result screen", [420, 0], "Решатель — выбор по готовым ответам",
            "=Выбор: {{ $json.output.choice }}"),
    ]
    conn = {
        "Client question": {"main": [[{"node": "Pick KB item", "type": "main", "index": 0}]]},
        "Pick KB item": {"main": [[{"node": "Resolver verdict", "type": "main", "index": 0}]]},
        "Resolver verdict": {"main": [[{"node": "Result screen", "type": "main", "index": 0}]]},
        "Model (resolver)": {"ai_languageModel": [[
            {"node": "Resolver verdict", "type": "ai_languageModel", "index": 0}]]},
    }
    return {"name": "С9 · замер K3 · смесь экспертов, решатель над готовыми ответами",
            "nodes": nodes, "connections": conn, "settings": {"executionOrder": "v1"}}


STAGES = {"n4mix-mix": case_mix, "n4mix-resolver": case_mix_resolver_only}


def api(method, path, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": KEY, "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


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
