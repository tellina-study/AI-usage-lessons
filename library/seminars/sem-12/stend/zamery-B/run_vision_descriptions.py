#!/usr/bin/env python3
"""Семинар 12, Кейс B — два vision-метода (свободный рассказ / поля по схеме) на
40 снимках корпуса B, модель `openai/gpt-4o-mini` через вебхук `s10-raw-openrouter`
(переиспользован из Кейса 1 без изменений — тот же `harness_call.py`/`harness2_lite.py`).

ВАЖНО (находка сессии кейса B, 2026-11-24): submit-POST в `/form/s10-raw-openrouter`
не требует авторизации (N8N_API_KEY не нужен), но ПОЛУЧЕНИЕ результата идёт через
`get_execution()` → управляющий API n8n (`/executions/{id}?includeData=true`,
заголовок `X-N8N-API-KEY`) — и вот ЭТО требует кредов из `.n8n-lab-credentials`.
Эта сессия не имеет к ним доступа (классификатор харнесса блокирует чтение файла по
любому пути). Скрипт написан для запуска ИЗ СЕССИИ, у которой креды есть
(`s12-plan-abc-tri-keysa`, см. сообщение оркестратора) — запустить как есть:

    set -a; source /home/harness/.n8n-lab-credentials; set +a
    cd library/seminars/sem-12/stend/zamery-B
    python3 run_vision_descriptions.py

Выход: raw/vision_results.json — список по каждому id: caption, fields (сырой текст
+ распарсенный JSON), usage/cost/wall_s на вызов. НЕ содержит снимков, не содержит
кредов. Вернуть этот файл сессии кейса B — она меряет (чтением глазами) и судит.
"""
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from harness2_lite import CHAT_MODEL, extract_json, to_data_url, vision_call, word_count

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus-cache"
RAZMETKA = HERE / "razmetka.json"
OUT = HERE / "raw" / "vision_results.json"

SYS_CAPTION = (
    "Ты — система автоматического описания фотографий для архива учебного центра. "
    "Опиши эту фотографию связно, 3-4 предложениями: что происходит, кто и что видно, "
    "в каком помещении. Пиши связный текст, БЕЗ JSON, БЕЗ списков, БЕЗ заголовков — "
    "только сам текст."
)
USER_CAPTION = "Опиши эту фотографию 3-4 предложениями для архива."

SYS_FIELDS = (
    "Ты — система автоматического тегирования фотографий архива учебного центра. "
    "Проанализируй фотографию и верни СТРОГО валидный JSON-объект (без markdown-"
    "ограждения ```, без пояснений до или после — только сам JSON) с полями:\n"
    '- "event_type" (строка): тип мероприятия или сцены на фото, например "лекция", '
    '"семинар", "кофе-брейк", "совещание", "у доски", "другое"\n'
    '- "people_count" (целое число): сколько людей видно в кадре (0, если нет)\n'
    '- "food_or_drink_present" (bool): видны ли в кадре еда или напитки как предметы '
    "(кружки, бутылки, тарелки) — независимо от того, ест ли кто-то в кадре\n"
    '- "screen_or_slide_visible" (bool): виден ли в кадре экран, проектор, телевизор '
    "или доска с читаемым текстом/слайдом\n"
    '- "room_type" (строка): тип помещения, например "аудитория", "конференц-зал", '
    '"учебный класс", "студия", "кафе", "зал"\n'
    "Верни ТОЛЬКО JSON-объект с этими 5 полями и больше ничего."
)
USER_FIELDS = "Заполни поля по схеме для этой фотографии."

VARIANTS = ["caption", "fields"]


def call_one(rid, path, variant):
    img = to_data_url(str(path))
    sys_p, user_p = {
        "caption": (SYS_CAPTION, USER_CAPTION),
        "fields": (SYS_FIELDS, USER_FIELDS),
    }[variant]
    r = vision_call(sys_p, user_p, img)
    r["id"] = rid
    r["variant"] = variant
    if variant == "fields":
        r["parsed"] = extract_json(r["content"])
    r["words"] = word_count(r["content"])
    return r


def main():
    doc = json.loads(RAZMETKA.read_text(encoding="utf-8"))
    ids = [e["id"] for e in doc["entries"] if e["in_corpus"]]
    print(f"корпус: {len(ids)} снимков, модель {CHAT_MODEL}")

    jobs = [(rid, CORPUS / f"{rid}.jpg", v) for rid in ids for v in VARIANTS]
    results = []
    t0 = time.time()
    with ThreadPoolExecutor(6) as ex:
        futs = {ex.submit(call_one, rid, p, v): (rid, v) for rid, p, v in jobs}
        for fut in as_completed(futs):
            rid, v = futs[fut]
            try:
                r = fut.result()
            except Exception as e:
                r = {"id": rid, "variant": v, "error": str(e)}
            results.append(r)
            print(f"{rid} {v}: {'OK' if r.get('content') else 'FAIL ' + str(r.get('raw_error') or r.get('error'))}")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps({
        "model": CHAT_MODEL,
        "sys_caption": SYS_CAPTION,
        "user_caption": USER_CAPTION,
        "sys_fields": SYS_FIELDS,
        "user_fields": USER_FIELDS,
        "n_images": len(ids),
        "n_calls": len(jobs),
        "total_wall_s": round(time.time() - t0, 1),
        "results": results,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = sum(1 for r in results if r.get("content"))
    print(f"\nитого: {ok}/{len(jobs)} вызовов успешно, файл {OUT}")


if __name__ == "__main__":
    main()
