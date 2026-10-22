#!/usr/bin/env python3
"""Сверка: то, что ОТПРАВИЛ БЫ `sborka.py --push`, против того, что на стенде СЕЙЧАС.

Волна 1г «конфетки» Семинара 8 (issue #292), задача D. Повод прямой: узлы на стенде
правились руками через `PUT /workflows/<id>` (узел клиенту в Кейсе 3 — волна 1в), а генератор
про них не знал, и любой следующий `--push` тихо снёс бы правку. Лечится это не памятью, а
проверкой — этой.

ТОЛЬКО ЧТЕНИЕ. Скрипт зовёт `GET /workflows` и ничего не пишет. `--push` он не делает и
делать не умеет.

    N8N_API_URL=... N8N_API_KEY=... python3 sverka_so_stendom.py

ЧТО СРАВНИВАЕТСЯ: набор узлов (имя → тип, версия типа, параметры, привязанный credential) и
все связи. То есть всё, от чего зависит поведение сценария.

ЧТО СОЗНАТЕЛЬНО НЕ СРАВНИВАЕТСЯ, и почему — иначе расхождение показывалось бы там, где его
нет:

* `position` — n8n притягивает координаты к своей сетке (генератор пишет [540, 80], стенд
  отдаёт [544, 80]). Это не различие сценария, а округление холста.
* `webhookId` — n8n сам выдаёт его узлам формы и Telegram при первой публикации; в генераторе
  такого значения нет и быть не может.
* `settings` — стенд дописывает свои значения по умолчанию (`binaryMode`), которых генератор
  не задаёт.
* Поля самого хранилища (`id` воркфлоу, `versionId`, `createdAt`, `updatedAt`, `active`,
  `tags`, `meta`, `pinData`) — они не из генератора вовсе.

Молчаливое «всё сошлось» — это и есть нужный ответ. Любая строка `РАСХОЖДЕНИЕ` означает: либо
стенд правили руками мимо генератора, либо генератор ушёл вперёд стенда, — и до `--push`
нужно понять, какое из двух, потому что `--push` разрешает спор в пользу генератора молча.
"""
import json
import os
import sys
import urllib.request

import sborka

SKIP_NODE_FIELDS = {"position", "webhookId"}

# Значения, которые n8n СЧИТАЕТ ЗНАЧЕНИЯМИ ПО УМОЛЧАНИЮ и не хранит: генератор их пишет явно,
# стенд отдаёт без них. Каждая строка проверена глазами на живом стенде 2026-10-22 — это не
# «похоже на умолчание», а замеренное расхождение формы хранения при одинаковом поведении.
DROPPED_DEFAULTS = {
    "mode": "manual",              # Set-узел: ручная раскладка полей — умолчание
    "respondWith": "text",         # Form completion: текстовый ответ — умолчание
    "operation": "insert",         # Data Table: вставка строки — умолчание
    "requiredField": False,        # поле формы: необязательное — умолчание
}


def normalize(obj, key=None):
    """Убрать из структуры то, что дописывает или выбрасывает сам n8n.

    Что снимается и почему (иначе «расхождение» печаталось бы там, где его нет):

    * `conditions[i].id` — uuid, который n8n выдаёт каждому условию при сохранении;
    * `conditions.options.version` / `options.leftValue` — служебные поля редактора условий;
    * пустой `options: {}` — n8n дописывает его сам;
    * `path` у узла формы — n8n хранит его в `webhookId`, а из параметров убирает;
    * поля из `DROPPED_DEFAULTS` — записаны генератором, не хранятся стендом.
    """
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    if not isinstance(obj, dict):
        return obj
    out = {}
    for k, v in obj.items():
        if k == "id" and "operator" in obj:        # условие IF-узла
            continue
        if k in ("version", "leftValue") and key == "options":
            continue
        if k == "options" and v == {}:
            continue
        if k == "path" and "formFields" in obj:
            continue
        if k in DROPPED_DEFAULTS and v == DROPPED_DEFAULTS[k]:
            continue
        out[k] = normalize(v, k)
    return out


def api(path):
    req = urllib.request.Request(
        os.environ["N8N_API_URL"] + path,
        headers={"X-N8N-API-KEY": os.environ["N8N_API_KEY"]})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def node_shape(n):
    return normalize({k: v for k, v in n.items() if k not in SKIP_NODE_FIELDS})


def compare(name, mine, live):
    diffs = []
    a = {n["name"]: node_shape(n) for n in mine["nodes"]}
    b = {n["name"]: node_shape(n) for n in live["nodes"]}
    for only, where in ((set(a) - set(b), "нет на стенде"),
                        (set(b) - set(a), "нет в генераторе")):
        for nm in sorted(only):
            diffs.append(f"узел «{nm}» — {where}")
    for nm in sorted(set(a) & set(b)):
        if a[nm] != b[nm]:
            for k in sorted(set(a[nm]) | set(b[nm])):
                if a[nm].get(k) != b[nm].get(k):
                    diffs.append(
                        f"узел «{nm}», поле {k}:\n"
                        f"      генератор: {json.dumps(a[nm].get(k), ensure_ascii=False)[:400]}\n"
                        f"      стенд:     {json.dumps(b[nm].get(k), ensure_ascii=False)[:400]}")
    if mine["connections"] != live["connections"]:
        for k in sorted(set(mine["connections"]) | set(live["connections"])):
            if mine["connections"].get(k) != live["connections"].get(k):
                diffs.append(
                    f"связи от «{k}»:\n"
                    f"      генератор: {json.dumps(mine['connections'].get(k), ensure_ascii=False)[:400]}\n"
                    f"      стенд:     {json.dumps(live['connections'].get(k), ensure_ascii=False)[:400]}")
    return diffs


def main():
    for var in ("N8N_API_URL", "N8N_API_KEY"):
        if not os.environ.get(var):
            print(f"{var} не задан — source /home/harness/.n8n-lab-credentials", file=sys.stderr)
            sys.exit(1)
    live = {w["name"]: w for w in api("/workflows?limit=100")["data"]}
    bad = 0
    for fname, fn in sborka.STAGES.items():
        mine = fn()
        if mine["name"] not in live:
            print(f"✗ {fname}: «{mine['name']}» на стенде НЕ НАЙДЕН")
            bad += 1
            continue
        diffs = compare(mine["name"], mine, live[mine["name"]])
        if not diffs:
            print(f"✓ {fname}: сошлось ({len(mine['nodes'])} узлов) — «{mine['name']}»")
        else:
            bad += 1
            print(f"✗ {fname}: РАСХОЖДЕНИЕ — «{mine['name']}»")
            for d in diffs:
                print(f"    {d}")
    print("\nвсё сошлось — `--push` ничего не снесёт" if not bad
          else f"\nрасхождений: {bad} — разобраться ДО `--push`")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
