"""Прогоняет демо-сценарий «С10 · Кейс 2 — нарезка документа (демо-экран)»
(`sborka.py::case2_chunking_workflow`, id `oLiJHPEy6uII7W5J`) на РЕАЛЬНОМ документе
SberQuAD — том самом, что попадает в `sample[:60]` замера `case2_chunking.py`
(seed=7, CHUNK_SIZE=180): контекст про кибернетику Гордона Паска, где фиксированная
нарезка на 180 символов разрывает эталонный ответ "из любых источников" границей куска
(конец куска [360:540), начало ответа на позиции 528), а нарезка по границам
предложений оставляет весь ответ в одном куске [411:587).

Документ найден детерминированно (тот же seed=7/shuffle, что в самом измерении) —
не придуман и не взят из другого корпуса.
"""
import json
import time
import urllib.parse

from harness_call import post_form, get_execution

DOCUMENT = (
    "Кибернетика включает изучение обратной связи, чёрных ящиков и производных "
    "концептов, таких как управление и коммуникация в живых организмах, машинах и "
    "организациях, включая самоорганизации. Она фокусирует внимание на том, как "
    "что-либо (цифровое, механическое или биологическое) обрабатывает информацию, "
    "реагирует на неё и изменяется или может быть изменено, для того чтобы лучше "
    "выполнять первые две задачи[4]. Стаффорд Бир назвал её наукой эффективной "
    "организации, а Гордон Паск расширил определение, включив потоки информации из "
    "любых источников , начиная со звёзд и заканчивая мозгом."
)
QUESTION = "Из каких источников могут быть потоки информации в определении Гордона Паска?"
ANSWER = "из любых источников"
ANSWER_START = 528
assert DOCUMENT[ANSWER_START:ANSWER_START + len(ANSWER)] == ANSWER, "офсет должен совпадать с реальным текстом"

payload = {
    "document": DOCUMENT,
    "question": QUESTION,
    "answer": ANSWER,
    "answer_start": ANSWER_START,
    "chunk_size": 180,
}

resp = post_form("s10-case2-chunking", [json.dumps(payload, ensure_ascii=False)])
waiting = resp.get("formWaitingUrl", "")
exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
print("exec_id", exec_id)
time.sleep(3)
ex = get_execution(exec_id)
run = ex.get("data", {}).get("resultData", {}).get("runData", {})
print("nodes with data:", list(run.keys()))
print("status:", ex.get("status"), "finished:", ex.get("finished"))
node = "Сравнение: попал ли ответ целиком в один кусок"
if node in run:
    try:
        out = run[node][0]["data"]["main"][0][0]["json"]
        print("--- v1_intact:", out["v1_intact"], " v2_intact:", out["v2_intact"], "---")
        print(out["summary"])
    except Exception as e:
        print("err reading", e, json.dumps(run[node][0], ensure_ascii=False)[:1500])
json.dump(ex, open("case2_chunking_execution.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
