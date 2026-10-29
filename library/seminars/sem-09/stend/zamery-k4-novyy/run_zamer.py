#!/usr/bin/env python3
"""Прогон нового Замера Кейса 4 Семинара 9 — issue #303.

Восемь конфигураций защит × 64 заявки корпуса. Каждая запись результата — настоящая
отправка на опубликованный вебхук плюс прямое чтение `GET /executions/<id>?
includeData=true`: числа берутся из данных узлов исполнения, не из самоотчёта «вебхук
ответил 200» (то же требование, что в `../README.md` и `../zamery-k5-k6/common.py`).

Параллельность устроена так, что чтение исполнения не может перепутать записи: каждая
конфигурация — свой поток и свой сценарий на стенде, а ВНУТРИ конфигурации заявки идут
строго по одной. Поэтому «самое свежее исполнение этого сценария после моего POST» — это
гарантированно моё исполнение, а не чужое. Сверх этого каждая запись проверяется на
совпадение текста, который вернул узел «Данные заявки», с тем, что отправлял прогонщик:
несовпадение помечается `sverka_teksta: false` и в свод не идёт.

    N8N_API_URL=... N8N_API_KEY=... python3 run_zamer.py --pilot      3 заявки × 2 конфиг.
    N8N_API_URL=... N8N_API_KEY=... python3 run_zamer.py              все 8 × 64
    N8N_API_URL=... N8N_API_KEY=... python3 run_zamer.py --dopolnit   только недостающие

`--dopolnit` досылает ТОЛЬКО те пары (конфигурация, заявка), которых нет в файле
результатов, и каждую — живым вызовом. Закешированных ответов этот скрипт не
переиспользует нигде: в этом семинаре уже была цена за переиспользованный ответ как за
повтор (`../zamery-k5-k6/README.md`, `WIRING_CHECK_RESPONSE`).
"""
import json
import os
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

import korpus
from pathlib import Path

HERE = Path(__file__).parent
HOST = "https://n8n.lessons.tellian.io"
REZULTATY = HERE / "rezultaty.jsonl"

KONFIGI = ["0", "p", "r", "c", "pr", "pc", "rc", "prc"]
_lock = threading.Lock()


def env_or_die():
    api_url = os.environ.get("N8N_API_URL")
    api_key = os.environ.get("N8N_API_KEY")
    if not api_url or not api_key:
        print("N8N_API_URL / N8N_API_KEY не заданы — "
              "source /home/harness/.n8n-lab-credentials", file=sys.stderr)
        sys.exit(1)
    return api_url, api_key


def telo_zayavki(z):
    """Ровно то, что уходит на стенд. Ни класса, ни разметки, ни даже номера заявки:
    номер — служебный ярлык прогонщика, а в промт попадает всё, что пришло в теле."""
    return {"name": z["name"], "text": z["text"]}


def post_webhook(code, telo):
    url = f"{HOST}/webhook/s9-m4n-{code}"
    data = json.dumps(telo, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST",
                                  headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return True, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return False, {"http_status": e.code, "body": e.read().decode("utf-8", "replace")[:600]}
    except Exception as e:
        return False, {"error": type(e).__name__, "detail": str(e)[:300]}


def api_get(api_url, api_key, path):
    req = urllib.request.Request(f"{api_url}{path}", headers={"X-N8N-API-KEY": api_key})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def nash_exec_id(api_url, api_key, workflow_id, after_ts_ms):
    import datetime
    for _ in range(12):
        try:
            d = api_get(api_url, api_key, f"/executions?workflowId={workflow_id}&limit=3")
        except Exception:
            time.sleep(0.6)
            continue
        for ex in d.get("data", []):
            st = datetime.datetime.fromisoformat(ex["startedAt"].replace("Z", "+00:00"))
            if st.timestamp() * 1000 >= after_ts_ms - 2000:
                return ex["id"]
        time.sleep(0.6)
    return None


def node_json(run_data, name):
    try:
        return run_data[name][0]["data"]["main"][0][0]["json"]
    except Exception:
        return None


def chitat_ispolnenie(api_url, api_key, exec_id):
    """Дождаться завершения и вернуть выводы узлов. Фиксированного сна недостаточно —
    решение принимается асинхронно (вызов модели), тот же приём, что в common.py."""
    deadline = time.time() + 90
    last = {}
    while time.time() < deadline:
        try:
            ex = api_get(api_url, api_key, f"/executions/{exec_id}?includeData=true")
        except Exception:
            time.sleep(0.8)
            continue
        last = ex
        rd = ex.get("data", {}).get("resultData", {}).get("runData", {})
        if ex.get("finished") or "Итог" in rd or ex.get("status") in ("error", "crashed"):
            return ex, rd
        time.sleep(0.8)
    return last, last.get("data", {}).get("resultData", {}).get("runData", {})


def odna(api_url, api_key, code, wid, z):
    telo = telo_zayavki(z)
    ts = time.time() * 1000
    ok_post, resp = post_webhook(code, telo)
    exec_id = nash_exec_id(api_url, api_key, wid, ts)
    zapis = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "konfiguratsiya": code, "zayavka_id": z["id"], "klass": z["klass"],
        "priem": z["priem"], "vozvrat_polozhen": z["vozvrat_polozhen"],
        "post_ok": ok_post, "execution_id": exec_id,
    }
    if not ok_post:
        zapis["post_otvet"] = resp
    if exec_id is None:
        zapis["oshibka"] = "исполнение не найдено"
        return zapis
    ex, rd = chitat_ispolnenie(api_url, api_key, exec_id)
    zapis["execution_status"] = ex.get("status")
    dannye = node_json(rd, "Данные заявки") or {}
    zapis["sverka_teksta"] = (dannye.get("text") == z["text"]
                              and dannye.get("name") == z["name"])
    meh = node_json(rd, "Механическая проверка")
    if meh is not None:
        zapis["mehanika_blocked"] = meh.get("mehanika_blocked")
        zapis["mehanika_hits"] = meh.get("mehanika_hits")
    klf = node_json(rd, "Разбор классификатора")
    if klf is not None:
        zapis["klf_manipulation"] = klf.get("klf_manipulation")
        zapis["klf_parse_ok"] = klf.get("klf_parse_ok")
        zapis["klf_priznak"] = klf.get("klf_priznak")
        zapis["klf_raw"] = (klf.get("klf_raw") or "")[:400]
        zapis["klf_model"] = klf.get("klf_model")
        zapis["klf_usage"] = klf.get("klf_usage")
    resh = node_json(rd, "Разбор решения")
    itog = node_json(rd, "Итог") or {}
    if resh is not None:
        zapis["decision"] = resh.get("decision")
        zapis["decision_parse_ok"] = resh.get("decision_parse_ok")
        zapis["reason"] = (resh.get("reason") or "")[:300]
        zapis["reshenie_raw"] = (resh.get("reshenie_raw") or "")[:500]
        zapis["reshenie_model"] = resh.get("reshenie_model")
        zapis["reshenie_usage"] = resh.get("reshenie_usage")
        zapis["istochnik"] = "model"
    else:
        zapis["decision"] = itog.get("decision")
        zapis["decision_parse_ok"] = itog.get("decision_parse_ok")
        zapis["reason"] = (itog.get("reason") or "")[:300]
        zapis["istochnik"] = itog.get("istochnik")
    if zapis.get("decision") is None:
        zapis["oshibka"] = "решение не прочитано из исполнения"
        zapis["uzly"] = sorted(rd.keys())
    return zapis


def pishi(zapis):
    with _lock:
        with REZULTATY.open("a", encoding="utf-8") as f:
            f.write(json.dumps(zapis, ensure_ascii=False) + "\n")


def uzhe_est():
    if not REZULTATY.exists():
        return set()
    out = set()
    for line in REZULTATY.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        z = json.loads(line)
        if z.get("decision") is not None:
            out.add((z["konfiguratsiya"], z["zayavka_id"]))
    return out


def potok(api_url, api_key, code, wid, zayavki, sdelano):
    n = 0
    for z in zayavki:
        if (code, z["id"]) in sdelano:
            continue
        zapis = odna(api_url, api_key, code, wid, z)
        pishi(zapis)
        n += 1
        if n % 10 == 0:
            print(f"   [{code}] {n} заявок", flush=True)
    print(f"   [{code}] готово, живых вызовов цепочки: {n}", flush=True)
    return n


def main():
    api_url, api_key = env_or_die()
    ids = json.loads((HERE / "stend-ids.json").read_text(encoding="utf-8"))
    k = korpus.korpus()
    pilot = "--pilot" in sys.argv
    dopolnit = "--dopolnit" in sys.argv
    sdelano = uzhe_est() if dopolnit else set()
    if dopolnit:
        print(f"досылка: в файле уже {len(sdelano)} готовых пар")
    if pilot:
        konfigi, zayavki = ["0", "prc"], [k[0], k[30], k[50]]
    else:
        konfigi, zayavki = KONFIGI, k
    print(f"конфигураций: {len(konfigi)}, заявок: {len(zayavki)}")
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=len(konfigi)) as ex:
        futs = [ex.submit(potok, api_url, api_key, c, ids[c], zayavki, sdelano)
                for c in konfigi]
        vsego = sum(f.result() for f in futs)
    print(f"прогонов цепочки: {vsego}, время: {time.time() - t0:.0f} c")
    print(f"результаты дописаны в {REZULTATY.name}")


if __name__ == "__main__":
    main()
