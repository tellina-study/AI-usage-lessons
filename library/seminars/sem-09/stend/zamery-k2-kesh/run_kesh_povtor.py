#!/usr/bin/env python3
"""S4 — повторы спорных замеров серии S2, issue #303.

Зачем. В S2 правка в СЕРЕДИНЕ базы дала у двух автоматических провайдеров разный исход:
Gemini сохранил примерно половину префикса (1020 из 2041), OpenAI — ноль. Второе не
выводится из документированной механики префиксного кэша напрямую, поэтому проверяется
повтором: один замер мог быть шумом. Два повтора на каждый спорный случай, каждый со своей
меткой опыта (холодный → тёплый → замер), как в S2.
"""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import baza  # noqa: E402
from run_kesh import body_plain, one, nonce  # noqa: E402

SPORNYE = [("gemini", "vstavlen_v_seredinu"), ("gpt", "vstavlen_v_seredinu"),
           ("gemini", "dopisan_v_konets"), ("gpt", "dopisan_v_konets")]

if __name__ == "__main__":
    out = []
    for mk, v in SPORNYE:
        for p in (1, 2):
            print(f"\n[S4] {mk} · {v} · повтор {p}")
            nz = nonce()
            base = baza.variant("bez_pravki", nonce=nz)
            for rol in ("holodnyi", "teplyi"):
                out.append(one(f"S4 · {mk} · {v} · p{p} · {rol}", body_plain(mk, base),
                               {"seriya": "S4", "model_klyuch": mk, "variant": v,
                                "rol": rol, "povtor": p, "nonce": nz}))
                time.sleep(1.5)
            out.append(one(f"S4 · {mk} · {v} · p{p} · ZAMER",
                           body_plain(mk, baza.variant(v, nonce=nz)),
                           {"seriya": "S4", "model_klyuch": mk, "variant": v,
                            "rol": "zamer", "povtor": p, "nonce": nz}))
            time.sleep(1.5)
    p = HERE / "raw/s4-povtory-spornyh.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nзаписано: {p}  вызовов: {len(out)}")
