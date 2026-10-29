#!/usr/bin/env python3
"""Третий независимый проход конфигурации `c` (модель-классификатор) — issue #303.

Зачем. Фильтр на входе вызывается двумя конфигурациями основного прогона — `c` и `pc` — с
ОДНОЙ моделью, одним промтом и температурой 0; усиление промта решающей модели до фильтра
структурно не доходит (это соседняя ветка графа), так что по одним и тем же 64 текстам
фильтр обязан был дать один и тот же вердикт. Он дал разный: 5 срабатываний в `c` против
8 в `pc`, расхождение на 5 заявках. Один из двух этих замеров ошибкой назвать нельзя —
нужен третий, чтобы вместо «5 или 8» в протоколе стояло три измерения одной величины.

Пишет в ОТДЕЛЬНЫЙ файл `rezultaty-povtor-c.jsonl`: в основной свод эти записи не идут,
иначе конфигурация `c` оказалась бы измерена вдвое плотнее остальных семи.

    N8N_API_URL=... N8N_API_KEY=... python3 run_povtor_c.py
"""
import json
import time
from pathlib import Path

import korpus
import run_zamer

HERE = Path(__file__).parent
FAYL = HERE / "rezultaty-povtor-c.jsonl"


def main():
    api_url, api_key = run_zamer.env_or_die()
    wid = json.loads((HERE / "stend-ids.json").read_text(encoding="utf-8"))["c"]
    t0 = time.time()
    n = 0
    with FAYL.open("a", encoding="utf-8") as f:
        for z in korpus.korpus():
            zapis = run_zamer.odna(api_url, api_key, "c", wid, z)
            zapis["prohod"] = 3
            f.write(json.dumps(zapis, ensure_ascii=False) + "\n")
            n += 1
            if n % 16 == 0:
                print(f"   {n} заявок", flush=True)
    print(f"прогонов цепочки: {n}, время: {time.time() - t0:.0f} c -> {FAYL.name}")


if __name__ == "__main__":
    main()
