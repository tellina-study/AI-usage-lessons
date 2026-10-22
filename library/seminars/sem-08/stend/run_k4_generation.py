#!/usr/bin/env python3
"""Прогон ЖИВОГО шага генерации карточки Кейса 4 и честная запись измерений.

Волна 1г производства Семинара 8 (issue #292, решение владельца 2026-10-22, вариант «б»):
генерация карточки должна реально стоять на стенде, а не оставаться оценкой по прайсу.
Этот скрипт выкладывает ОДИН workflow — `stage_4_generate()` из `sborka.py` — и прогоняет
через него настоящие отправки формы, после чего читает из прогона то, что нельзя узнать из
прайс-листа: реальную стоимость вызова, настоящий размер и формат файла, время генерации и
`message_id` доставленного сообщения.

    N8N_API_URL=... N8N_API_KEY=... TELEGRAM_BOT_TOKEN=... \
        python3 run_k4_generation.py --runs 3 [--no-push]

**Почему не `sborka.py --push`:** тот выложил бы все семь стадий сразу, включая `stage-4` с
его демо лимита `sendPhoto` — трогать работающее демо ради одной новой ветки незачем. Здесь
создаётся/обновляется ровно один workflow по имени.

Ключи — только из окружения (`/home/harness/.n8n-lab-credentials`, вне репозитория). Токен
бота нужен лишь для `getFile`: забрать из Telegram ту самую картинку, которую он показал
координатору (она уже пережата Telegram'ом — это и есть честный «доставленный» файл).
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.request

import sborka

HOST = "https://n8n.lessons.tellian.io"
WEBHOOK_PATH = "s8-case4-generate"
GEN_NODE = "Generate card (OpenRouter image)"
COST_NODE = "Card bytes and cost"
TG_NODE = "Send generated card (Telegram photo)"
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "n8n-screenshots-raw")

# Три разные заявки — чтобы текст карточки в прогонах отличался и было видно, что модель
# рисует ИМЕННО переданную строку, а не один раз угаданную картинку.
REQUESTS = [
    ("Мария", "maria@example.com", "хочу на курс по аналитике, перезвоните сегодня"),
    ("Олег", "+7 900 111-22-33", "нужно перенести занятие по математике на следующую неделю"),
    ("Нина", "nina@example.com", "вопрос по оплате курса, не срочно"),
    ("Пётр", "+7 900 444-55-66", "запишите на курс по программированию"),
]


def api(method, path, body=None):
    url = os.environ["N8N_API_URL"] + path
    req = urllib.request.Request(
        url, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"X-N8N-API-KEY": os.environ["N8N_API_KEY"],
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    return json.loads(raw) if raw else {}


def push_one(wf):
    """Выложить и опубликовать РОВНО этот workflow (по имени: обновить или создать)."""
    existing = {w["name"]: w["id"] for w in api("GET", "/workflows?limit=100")["data"]}
    if wf["name"] in existing:
        wid = existing[wf["name"]]
        api("PUT", f"/workflows/{wid}", wf)
        action = "обновлён"
    else:
        wid = api("POST", "/workflows", wf)["id"]
        action = "создан"
    api("POST", f"/workflows/{wid}/publish", {})
    print(f"  workflow {action} и опубликован: {wid} — {wf['name']}")
    return wid


def post_form(name, contact, text):
    """Поля формы на проводе зовутся `field-N` по порядку, и блок разметки занимает
    `field-0` — см. notes/mcp-limitations.md [#233-4].

    Ответ формы несёт `formWaitingUrl` с номером прогона — его и берём как id, вместо
    угадывания «последний в списке». Заодно дёргаем этот адрес: только он переводит
    прогон из `waiting` в `success` ([#233-5]), и прогон не остаётся висеть."""
    boundary = "----k4genboundary"
    parts = []
    for i, val in enumerate([name, contact, text], start=1):
        parts.append(f"--{boundary}\r\n")
        parts.append(f'Content-Disposition: form-data; name="field-{i}"\r\n\r\n')
        parts.append(val + "\r\n")
    parts.append(f"--{boundary}--\r\n")
    t0 = time.time()
    for attempt in range(5):
        req = urllib.request.Request(
            f"{HOST}/form/{WEBHOOK_PATH}", data="".join(parts).encode("utf-8"), method="POST")
        req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                resp = json.loads(r.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code != 404 or attempt == 4:
                raise
            time.sleep(3)  # publish только что применён — webhook ещё не поднялся
    wall = time.time() - t0
    url = resp.get("formWaitingUrl", "")
    exec_id = int(url.split("/form-waiting/")[1].split("?")[0]) if "/form-waiting/" in url else None
    return wall, exec_id, url


def finish_waiting(url):
    try:
        urllib.request.urlopen(urllib.request.Request(url, data=b"", method="POST"), timeout=60).read()
    except Exception as e:
        print(f"  (экран результата не запрошен: {e})")


def wait_for_node(exec_id, node, tries=60):
    """Прогон асинхронный — ждём появления нужного узла в `runData`, а не фиксированный
    сон. Статус `waiting` обрывом НЕ считается (см. [#233-5])."""
    for _ in range(tries):
        ex = api("GET", f"/executions/{exec_id}?includeData=true")
        rd = ((ex.get("data") or {}).get("resultData") or {}).get("runData") or {}
        if node in rd:
            return ex, rd
        if ex.get("status") in ("error", "crashed", "canceled"):
            return ex, rd  # ждать нечего: прогон уже кончился отказом
        time.sleep(2)
    return None, None


def exec_wall(ex):
    """Длительность прогона целиком, секунды, по его же `startedAt`/`stoppedAt`.
    У прогона с экраном-завершением `stoppedAt` появляется только после визита на
    экран результата ([#233-5]) — тогда здесь честный `None`, а не выдуманное число."""
    a, b = ex.get("startedAt"), ex.get("stoppedAt")
    if not (a and b):
        return None
    from datetime import datetime
    f = "%Y-%m-%dT%H:%M:%S.%f%z"
    try:
        return round((datetime.strptime(b.replace("Z", "+0000"), f)
                      - datetime.strptime(a.replace("Z", "+0000"), f)).total_seconds(), 2)
    except Exception:
        return None


def node_json(rd, node):
    try:
        return rd[node][0]["data"]["main"][0][0]["json"]
    except Exception:
        return None


def tg_get_file(file_id, dest):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    info = json.loads(urllib.request.urlopen(
        f"https://api.telegram.org/bot{token}/getFile?file_id={file_id}", timeout=60).read())
    path = info["result"]["file_path"]
    blob = urllib.request.urlopen(
        f"https://api.telegram.org/file/bot{token}/{path}", timeout=120).read()
    with open(dest, "wb") as f:
        f.write(blob)
    return len(blob), path


def sniff(blob):
    if blob[:8] == b"\x89PNG\r\n\x1a\n":
        w = int.from_bytes(blob[16:20], "big")
        h = int.from_bytes(blob[20:24], "big")
        return "PNG", w, h
    if blob[:2] == b"\xff\xd8":
        i = 2
        while i < len(blob) - 9:
            if blob[i] != 0xFF:
                i += 1
                continue
            m = blob[i + 1]
            if m in (0xC0, 0xC1, 0xC2):
                h = int.from_bytes(blob[i + 5:i + 7], "big")
                w = int.from_bytes(blob[i + 7:i + 9], "big")
                return "JPEG", w, h
            i += 2 + int.from_bytes(blob[i + 2:i + 4], "big")
        return "JPEG", None, None
    return "unknown", None, None


def trim_exec(ex, note):
    """Прогон несёт base64 картинки дважды (ответ модели и поле `data`) — это 1,1 МБ
    на копию, нечитаемо в репозитории. Строки длиннее 4096 символов заменяются пометкой;
    сама картинка сохранена отдельным файлом, так что ничего не потеряно."""
    def walk(o):
        if isinstance(o, dict):
            return {k: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        if isinstance(o, str) and len(o) > 4096:
            return f"<обрезано при сохранении: {len(o)} символов; {note}>"
        return o
    return walk(ex)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--no-push", action="store_true")
    ap.add_argument("--harvest", action="append", default=[],
                    help="id уже сделанного прогона — прочитать и измерить без нового вызова "
                         "(платная генерация не повторяется зря)")
    args = ap.parse_args()
    for var in ("N8N_API_URL", "N8N_API_KEY", "TELEGRAM_BOT_TOKEN"):
        if not os.environ.get(var):
            print(f"{var} не задан — source /home/harness/.n8n-lab-credentials", file=sys.stderr)
            sys.exit(1)

    wf = sborka.stage_4_generate()
    if not args.no_push:
        push_one(wf)

    rows = []
    plan = [("harvest", int(x)) for x in args.harvest] + [
        ("post", i) for i in range(args.runs)]
    for n, (kind, arg) in enumerate(plan, start=1):
        if kind == "post":
            name, contact, text = REQUESTS[arg % len(REQUESTS)]
            print(f"\n[{n}/{len(plan)}] заявка от {name}: {text}")
            wall, exec_id, waiting_url = post_form(name, contact, text)
            if not exec_id:
                print("  прогон не найден в ответе формы"); continue
        else:
            exec_id, wall, waiting_url = arg, None, None
            name = contact = text = None
            print(f"\n[{n}/{len(plan)}] уже сделанный прогон {exec_id} — только читаем")
        ex, rd = wait_for_node(exec_id, TG_NODE)
        if not rd:
            # Прогон мог не доехать до Telegram не из-за медленности, а из-за ОТКАЗА:
            # модель отвечает текстом без картинки, и цепочка падает на перекодировке.
            # Такой прогон записывается так же честно, как удачный, — он и есть находка.
            ex = api("GET", f"/executions/{exec_id}?includeData=true")
            rd = ((ex.get("data") or {}).get("resultData") or {}).get("runData") or {}
        if waiting_url:
            finish_waiting(waiting_url)
        if TG_NODE not in rd:
            gen = node_json(rd, GEN_NODE) or {}
            msg = (((gen.get("choices") or [{}])[0].get("message")) or {})
            failed = [(k, v[0]["error"].get("message"))
                      for k, v in rd.items() if v and v[0].get("error")]
            row = {
                "exec_id": exec_id, "status": ex.get("status"),
                "request": {"Имя": name, "Контакт": contact, "Что нужно": text},
                "model": gen.get("model"),
                "openrouter_generation_id": gen.get("id"),
                "cost_usd": (gen.get("usage") or {}).get("cost"),
                "image_tokens": ((gen.get("usage") or {})
                                 .get("completion_tokens_details") or {}).get("image_tokens"),
                "generation_node_ms": rd[GEN_NODE][0].get("executionTime") if GEN_NODE in rd else None,
                "no_image_text_reply": msg.get("content"),
                "failed_nodes": failed,
                "telegram_message_id": None,
            }
            rows.append(row)
            with open(os.path.join(RAW, f"exec-{exec_id}-k4-generatsiya.json"), "w",
                      encoding="utf-8") as f:
                json.dump(trim_exec(ex, "картинки в этом прогоне не было вовсе"), f,
                          ensure_ascii=False, indent=1)
            print("  ОТКАЗ: " + json.dumps({k: v for k, v in row.items() if k != "request"},
                                            ensure_ascii=False))
            continue

        cost = node_json(rd, COST_NODE) or {}
        tg = node_json(rd, TG_NODE) or {}
        tg = tg.get("result", tg)  # узел отдаёт сырой ответ Bot API: {ok, result:{…}}
        if name is None:
            form = node_json(rd, "Request form") or {}
            name, contact, text = (form.get("Имя"), form.get("Контакт"), form.get("Что нужно"))
        gen_ms = rd[GEN_NODE][0].get("executionTime")
        b64 = None
        try:
            b64 = rd[COST_NODE][0]["data"]["main"][0][0]["json"]["data"]
        except Exception:
            pass
        row = {
            "exec_id": exec_id,
            "request": {"Имя": name, "Контакт": contact, "Что нужно": text},
            "caption_delivered": tg.get("caption"),
            "model": cost.get("gen_model"),
            "openrouter_generation_id": cost.get("gen_id"),
            "cost_usd": cost.get("gen_cost_usd"),
            "data_url_chars": cost.get("gen_b64_chars"),
            "generation_node_ms": gen_ms,
            # Время ОТВЕТА ФОРМЫ мерить бессмысленно: форма отвечает сразу, цепочка
            # доезжает позже. Честная мера — время прогона целиком, из самого прогона.
            "exec_wall_s": exec_wall(ex),
            "telegram_message_id": tg.get("message_id"),
        }
        if b64:
            blob = base64.b64decode(b64)
            fmt, w, h = sniff(blob)
            png = os.path.join(RAW, f"k4-gen-card-exec{exec_id}.png")
            with open(png, "wb") as f:
                f.write(blob)
            row.update({"model_file_bytes": len(blob), "model_file_format": fmt,
                        "model_file_size_px": f"{w}x{h}" if w else None,
                        "model_file_saved": os.path.basename(png)})
        photos = tg.get("photo") or []
        if photos:
            big = max(photos, key=lambda p: p.get("file_size", 0))
            dest = os.path.join(RAW, f"k4-gen-card-exec{exec_id}-telegram.jpg")
            n, path = tg_get_file(big["file_id"], dest)
            fmt, w, h = sniff(open(dest, "rb").read())
            row.update({"telegram_file_bytes": n, "telegram_file_format": fmt,
                        "telegram_file_size_px": f"{w}x{h}" if w else None,
                        "telegram_file_saved": os.path.basename(dest)})
        rows.append(row)
        out = os.path.join(RAW, f"exec-{exec_id}-k4-generatsiya.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(trim_exec(ex, f"картинка сохранена как k4-gen-card-exec{exec_id}.png"),
                      f, ensure_ascii=False, indent=1)
        print("  " + json.dumps({k: v for k, v in row.items() if k != "request"},
                                ensure_ascii=False))

    summary = os.path.join(RAW, "k4-generatsiya-progony.json")
    with open(summary, "w", encoding="utf-8") as f:
        json.dump({"date": "2026-10-22", "workflow": wf["name"],
                   "model": sborka.IMAGE_MODEL, "runs": rows}, f,
                  ensure_ascii=False, indent=1)
    print(f"\nсводка: {summary}")


if __name__ == "__main__":
    main()
