#!/usr/bin/env python3
"""S5 — настоящий справочник Кейса 2 (10 пунктов), issue #303.

Остальные серии идут на раздутой базе из 60 пунктов: на меньшей кэш у части провайдеров
не включается вовсе, и механику было бы не видно. Эта серия отвечает на обратный вопрос —
а включается ли кэш на НАШЕМ справочнике, том самом, который правит Ольга. Три модели,
по два одинаковых вызова (холодный и тёплый) с меткой опыта; у Anthropic — с явной
контрольной точкой, то есть в самых выгодных для кэша условиях.
"""
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import baza  # noqa: E402
from run_kesh import body_plain, one, nonce  # noqa: E402

if __name__ == "__main__":
    out = []
    real = baza.KB_REAL
    txt = baza.base_text(real)
    print(f"настоящий справочник: {len(real)} пунктов, {len(txt.split())} слов, "
          f"{len(txt)} символов")
    for mk, marker in (("haiku", True), ("haiku", False), ("gemini", False),
                       ("gpt", False)):
        nz = nonce()
        base = baza.base_text(real, nonce=nz)
        tag = "s-tochkoy" if marker else "bez-tochki"
        print(f"\n[S5] {mk} · {tag}")
        for rol in ("holodnyi", "teplyi", "teplyi2"):
            out.append(one(f"S5 · {mk} · {tag} · {rol}",
                           body_plain(mk, base, marker=marker),
                           {"seriya": "S5", "model_klyuch": mk, "tochka": tag,
                            "rol": rol, "nonce": nz,
                            "spravochnik": "nastoyashchiy-10-punktov"}))
            time.sleep(1.5)
    p = HERE / "raw/s5-nastoyashchiy-spravochnik.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nзаписано: {p}  вызовов: {len(out)}")
