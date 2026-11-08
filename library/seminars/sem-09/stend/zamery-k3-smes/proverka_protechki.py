#!/usr/bin/env python3
"""Проверка промтов «смеси экспертов» на протечку правильного ответа — issue #299, З4.

Зачем отдельный скрипт, а не абзац в README (тот же урок, что уже стоит в
`../zamery-k4-novyy/proverka_protechki.py`): 2026-10-27 в этом же семинаре нашлась протечка
ровно этого класса (Замер K6) — пример формата поля в промте содержал настоящий правильный
ответ, и 30 вызовов измерили копирование подсказки, а не решение задачи. Абзац «я проверил»
в README — самоотчёт; проверка, которую можно перепрогнать, — нет.

В этой задаче нет отдельного секретного «правильного ответа», скрытого от модели (как в K6
была скрыта сумма квитанции) — задача сформулирована как генерация-по-правилам: правило 2
промта («явно включи деталь X») ровно так же стоит в УЖЕ измеренном промте генератора
`zamery-k1-k3/sborka_zamer3.py:generate_answer_node` — это не новый риск, он уже был оценён
там. Риск протечки здесь — другой, и именно его проверяет этот скрипт:

  1. Промт РЕШАТЕЛЯ не должен содержать кодовый вердикт (`ok`/`reason`) ни по одному из
     трёх вариантов — иначе решатель мог бы скопировать готовый ярлык вместо собственного
     выбора (это ЕСТЬ в варианте `judge-check` соседнего замера, но там это и есть предмет
     замера; здесь, в «смеси», это была бы протечка).
  2. Промт решателя не должен называть, какая модель стоит за каким вариантом (A/B/C) —
     иначе «решатель выбирает лучший ответ» подменилось бы «решатель предпочитает модель X
     по имени», что не то же самое измерение.
  3. Ни в одном промте (экспертов и решателя) не должно быть образца ЗАПОЛНЕННОГО ответа —
     готовой фразы, которую модели было бы достаточно скопировать целиком, вместо того чтобы
     решить задачу (тот же класс, что протечка K6).
  4. Промт решателя не должен содержать слов «правильный ответ» / «эталон» / «верно» как
     ярлык одного из трёх вариантов — решатель должен сам определить, какой лучше, не
     прочитать готовый вердикт из текста.
  5. Тело запроса на стенд несёт ровно одно поле `question` (`field-0` формы) для `s9-m3-mix`
     и ровно 4 поля (`question`, `answer_a/b/c`) для `s9-m3-mix-resolver` — лишних полей,
     которые могли бы протащить вердикт в обход промта, нет.

С флагом `--stend` те же проверки прогоняются по ВЫЛОЖЕННЫМ на стенд сценариям
(`GET /workflows/<id>`), не по локальным файлам — то же требование, что в соседнем скрипте
Кейса 4: выложить можно не то, что собрано.
"""
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
CODES = ["n4mix-mix", "n4mix-resolver"]

_EXPR_RE = re.compile(r"\{\{.*?\}\}", re.DOTALL)


def strip_expressions(text):
    """Снять n8n-выражения `{{ ... }}` ПЕРЕД проверкой на протечку. Внутри выражения стоит
    служебная адресация узла (например, `$('Generate (qwen)').item.json.text`) — это имя
    УЗЛА СБОРКИ, оно вычисляется движком n8n и заменяется реальным текстом ответа ДО того,
    как промт уйдёт модели; модель никогда не видит строку «qwen» как текст. Проверять
    протечку по непроверенному шаблону — тот же класс ложного срабатывания, что и
    `grep -P` по кириллице (`notes/mcp-limitations.md`, анти-паттерн cyrillic-pitfalls):
    совпадение есть в шаблоне, а не в том, что реально дойдёт до модели."""
    return _EXPR_RE.sub(" ", text)


def texts_iz_fayla(path):
    """Все литеральные промты (chainLlm/informationExtractor) собранного сценария."""
    wf = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for n in wf["nodes"]:
        if n["type"] in ("@n8n/n8n-nodes-langchain.chainLlm",
                          "@n8n/n8n-nodes-langchain.informationExtractor"):
            out[n["name"]] = n["parameters"]["text"]
    return out, wf


def texts_so_stenda(code, stend_ids):
    api, key = os.environ["N8N_API_URL"], os.environ["N8N_API_KEY"]
    wid = stend_ids[code]
    req = urllib.request.Request(f"{api}/workflows/{wid}",
                                  headers={"X-N8N-API-KEY": key})
    wf = json.loads(urllib.request.urlopen(req, timeout=60).read().decode("utf-8"))
    out = {}
    for n in wf["nodes"]:
        if n["type"] in ("@n8n/n8n-nodes-langchain.chainLlm",
                          "@n8n/n8n-nodes-langchain.informationExtractor"):
            out[n["name"]] = n["parameters"]["text"]
    return out, wf


def main():
    so_stenda = "--stend" in sys.argv
    stend_ids = {}
    if so_stenda:
        stend_ids = json.loads((HERE / "stend-ids.json").read_text(encoding="utf-8"))

    bada = []
    resolver_names = {"Resolver verdict"}

    for code in CODES:
        if so_stenda:
            texts, wf = texts_so_stenda(code, stend_ids)
            print(f"  читаю со стенда: {code} -> {stend_ids[code]}")
        else:
            texts, wf = texts_iz_fayla(HERE / f"{code}.json")

        for name, text in texts.items():
            # Проверяем ЛИТЕРАЛЬНЫЙ текст промта — без n8n-выражений `{{ ... }}`, которые
            # движок подставит реальными данными ДО отправки модели (см. strip_expressions).
            literal = strip_expressions(text)
            low = literal.lower()
            is_resolver = name in resolver_names

            # 3 — образец заполненного ответа (готовая фраза, достаточно скопировать)
            for obrazets in ("клиент подтверждён", '"choice": "a"', '"choice": "b"',
                              '"choice": "c"', "например, выберите a", "лучший вариант — a",
                              "лучший вариант — b", "лучший вариант — c"):
                if obrazets.lower() in low:
                    bada.append(f"{code}/{name}: образец заполненного решения «{obrazets}»")

            if is_resolver:
                # 1 — кодовый вердикт внутри промта решателя
                for marker in ("code check", "code_check", '"ok": true', '"ok": false',
                                "код сказал", "код принял", "код забраковал", "ok=true",
                                "ok=false"):
                    if marker in low:
                        bada.append(f"{code}/{name}: кодовый вердикт «{marker}» в промте "
                                    "решателя")
                # 2 — имя модели за буквой
                for m_name in ("qwen", "llama", "ministral", "мистраль", "квен", "лама"):
                    if m_name in low:
                        bada.append(f"{code}/{name}: имя модели «{m_name}» в промте "
                                    "решателя — решатель не должен знать, кто за буквой")
                # 4 — готовый ярлык правильности
                for marker in ("правильный ответ", "эталон", "ground truth",
                               "заведомо верно", "заведомо неверно"):
                    if marker in low:
                        bada.append(f"{code}/{name}: ярлык «{marker}» в промте решателя")

        # 5 — поля, уходящие в форму (webhook) — ровно question (mix) или question+3 ответа
        # (resolver-only); сверяем по количеству объявленных полей формы.
        form = next(n for n in wf["nodes"] if n["type"] == "n8n-nodes-base.formTrigger")
        fields = [f["fieldLabel"] for f in form["parameters"]["formFields"]["values"]]
        expect = {"n4mix-mix": ["Вопрос"],
                   "n4mix-resolver": ["Вопрос", "ОтветA", "ОтветB", "ОтветC"]}[code]
        if fields != expect:
            bada.append(f"{code}: поля формы {fields} != ожидаемых {expect}")

    if bada:
        print("ПРОТЕЧКА НАЙДЕНА:")
        for b in bada:
            print("  -", b)
        sys.exit(1)
    print("Протечки не найдено"
          + (" (проверено по ВЫЛОЖЕННЫМ на стенд сценариям)." if so_stenda else "."))
    print("Проверено:")
    print("  - промт решателя не содержит кодового вердикта и имён моделей за буквами")
    print("  - ни в одном промте нет образца заполненного решения")
    print("  - промт решателя не содержит ярлыков «правильный ответ»/«эталон»")
    print("  - поля формы — ровно те, что уходят в промт, лишних полей нет")


if __name__ == "__main__":
    main()
