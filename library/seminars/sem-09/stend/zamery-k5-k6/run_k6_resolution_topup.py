#!/usr/bin/env python3
"""Добор 4 вызовов замера 4.1 (Кейс 6, issue #299) — владелец 2026-10-27 указал, что
«везде по 5 замеров», а `sixteenth`/`thirtysecond` в README честно помечены как 3 из 5
(добавлены после основного прогона, см. README «Бюджет вызовов»). Этот скрипт добирает
РОВНО 2 недостающих повтора на каждое из двух разрешений — ПО 5 итогу на каждое, как у
остальных четырёх, — не трогая уже записанные 3+3 (дописывает, не перезаписывает, см.
канон §8.3 «отменил правило — поправь проверку в том же круге», здесь симметрично:
дополнил число — не сотри старое).

Переиспользует `call_once`/`evaluate`/`parse_model_json` из `run_k6_resolution.py`
дословно — тот же вебхук `s9-m6-read`, тот же метод (POST на живой вебхук + чтение
`GET /executions/<id>` для execution id, не самоотчёт).

Usage: N8N_API_URL=... N8N_API_KEY=... python3 run_k6_resolution_topup.py
"""
import json
from pathlib import Path

import run_k6_resolution as R
import common

HERE = Path(__file__).parent
TARGET_N = 5
TOPUP_RESOLUTIONS = ["sixteenth", "thirtysecond"]


def main():
    api_url, api_key = common.env_or_die()
    out_path = HERE / "results-k6-resolution.json"
    data = json.loads(out_path.read_text(encoding="utf-8"))
    by_res = data["by_resolution"]

    for res_name in TOPUP_RESOLUTIONS:
        block = by_res[res_name]
        entries = block["entries"]
        have = len(entries)
        need = TARGET_N - have
        if need <= 0:
            print(f"{res_name}: уже {have} — добор не нужен")
            continue
        info = R.RES_INFO[res_name]
        print(f"\n=== {res_name} ({info['size'][0]}x{info['size'][1]}) — добор {need} "
              f"(было {have}, нужно {TARGET_N}) ===")
        for i in range(have + 1, TARGET_N + 1):
            entry = R.call_once(res_name, api_url, api_key)
            entry["reused_from_wiring_check"] = False
            entry["topup_call"] = True  # честно помечено: добор, не исходный прогон
            if entry["ok"]:
                entry = R.evaluate(entry)
                parsed = entry["parsed"] or {}
                print(f"  #{i} exec={entry.get('execution_id')} "
                      f"sum={parsed.get('sum_rub')} (correct={entry['sum_correct']}) "
                      f"date={parsed.get('date')} (correct={entry['date_correct']}) "
                      f"raw_seen={parsed.get('raw_text_seen', entry.get('raw_content'))}")
            else:
                print(f"  #{i} ОШИБКА: {entry['error']}")
            entries.append(entry)

        block["entries"] = entries
        block["n"] = len(entries)
        block["n_sum_correct"] = sum(1 for e in entries if e.get("sum_correct"))
        block["n_date_correct"] = sum(1 for e in entries if e.get("date_correct"))

    out_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\nСВОДКА (после добора):")
    for res_name in R.RESOLUTIONS:
        r = by_res[res_name]
        print(f"  {res_name:12s} сумма верна {r['n_sum_correct']}/{r['n']}  "
              f"дата верна {r['n_date_correct']}/{r['n']}")
    print(f"\n-> {out_path}")


if __name__ == "__main__":
    main()
