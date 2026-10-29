#!/usr/bin/env python3
"""Замер кэширования промта — Кейс 2 Семинара 9, issue #303.

Перепрогон вместо замера A из `zamery-k2/README.md`: тот мерил ЛАТЕНТНОСТЬ (единственное,
что отдавал узел chainLlm) и поэтому про кэш ничего сказать не мог. Здесь считаются токены
и деньги из поля `usage` ответа провайдера — `prompt_tokens_details.cached_tokens`,
`prompt_tokens_details.cache_write_tokens`, `cost`, `cost_details`.

Четыре серии:
  S1 «кто вообще отдаёт метрики» — на каждой модели холодный вызов и тёплый тем же текстом.
  S2 «куда дописывать пункт» — четыре варианта базы (без правки / дописан в конец /
     вставлен в середину / правка в начале), перед каждым прогрев базой без правки.
  S3 «Anthropic: как выставляется контрольная точка» — те же четыре варианта в трёх
     раскладках: справочник одним блоком с точкой в конце; справочник четырьмя блоками с
     точкой на последнем (на дописывании точка переезжает за новый пункт); совсем без
     `cache_control`.
  S4 — не прогон, а счёт по собранным числам (см. svod.py).

Usage:
    source /home/harness/.n8n-lab-credentials && set -a && \
        source /home/harness/.n8n-lab-credentials && set +a
    python3 run_kesh.py --series S1 --out raw/s1-metriki.json
"""
import argparse
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import baza  # noqa: E402
from kesh_stend import call  # noqa: E402

MODELS = {
    "qwen":     {"id": "qwen/qwen-2.5-7b-instruct", "provider": ["Phala"],
                 "zachem": "модель стенда Семинара 9 — отдаёт ли она метрики кэша вообще"},
    "haiku":    {"id": "anthropic/claude-haiku-5.5", "provider": ["Anthropic"],
                 "zachem": "Anthropic: точка кэша задаётся явно полем cache_control"},
    "gemini":   {"id": "google/gemini-2.5-flash", "provider": ["Google AI Studio"],
                 "zachem": "Gemini: неявный кэш, точка не задаётся"},
    "gpt":      {"id": "openai/gpt-4.1-mini", "provider": ["OpenAI"],
                 "zachem": "OpenAI: автоматический кэш, точка не задаётся"},
    "deepseek": {"id": "deepseek/deepseek-chat", "provider": ["DeepInfra"],
                 "zachem": "кэш зависит от посредника, а не от имени модели"},
}


def body_plain(model_key, base, marker=False):
    """Промт одной строкой — как его собирает обычный пользователь.

    `marker=True` добавляет cache_control на блок справочника (формат Anthropic,
    OpenRouter пробрасывает его к апстриму).
    """
    m = MODELS[model_key]
    if marker:
        content = [
            {"type": "text", "text": base, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": baza.QUESTION},
        ]
    else:
        content = base + "\n\n" + baza.QUESTION
    return {
        "model": m["id"],
        "messages": [{"role": "user", "content": content}],
        "max_tokens": 60, "temperature": 0,
        "provider": {"order": m["provider"], "allow_fallbacks": False},
        "usage": {"include": True},
    }


def body_bloki(model_key, items, extra_block=None, nonce=None):
    """Справочник четырьмя блоками; контрольная точка — на последнем блоке справочника.

    `extra_block` — дописанный пункт ОТДЕЛЬНЫМ блоком после справочника; точка в этом
    случае переезжает на него (так поступил бы человек, дописывая пункт в конец).
    """
    m = MODELS[model_key]
    chunks = [items[i:i + 20] for i in range(0, len(items), 20)]
    blocks = [{"type": "text",
                "text": baza.instruction(nonce) + "\n\nСПРАВОЧНИК ЦЕНТРА"}]
    for ch in chunks:
        blocks.append({"type": "text", "text": baza.render_items(ch)})
    if extra_block is not None:
        blocks.append({"type": "text", "text": baza.render_items([extra_block])})
    blocks[-1]["cache_control"] = {"type": "ephemeral"}
    blocks.append({"type": "text", "text": baza.QUESTION})
    return {
        "model": m["id"],
        "messages": [{"role": "user", "content": blocks}],
        "max_tokens": 60, "temperature": 0,
        "provider": {"order": m["provider"], "allow_fallbacks": False},
        "usage": {"include": True},
    }


def one(label, body, meta=None):
    r = call(body)
    resp = r.get("response") or {}
    u = (resp.get("usage") or {}) if isinstance(resp, dict) else {}
    ptd = u.get("prompt_tokens_details") or {}
    rec = {
        "label": label,
        "model_zapros": body.get("model"),
        "model_otvet": resp.get("model") if isinstance(resp, dict) else None,
        "provider_otvet": resp.get("provider") if isinstance(resp, dict) else None,
        "exec_id": r["exec_id"], "node_ms": r["node_ms"], "wall_s": r["wall_s"],
        "prompt_tokens": u.get("prompt_tokens"),
        "completion_tokens": u.get("completion_tokens"),
        "cached_tokens": ptd.get("cached_tokens"),
        "cache_write_tokens": ptd.get("cache_write_tokens"),
        "cost": u.get("cost"),
        "cache_discount": (resp.get("cache_discount")
                           if isinstance(resp, dict) else None),
        "or_id": resp.get("id") if isinstance(resp, dict) else None,
        "cost_details": u.get("cost_details"),
        "usage_polya": sorted(u.keys()),
        "prompt_tokens_details_polya": sorted(ptd.keys()),
        "error": (resp.get("error") if isinstance(resp, dict) else None),
        "otvet_text": None,
        "meta": meta or {},
    }
    try:
        rec["otvet_text"] = resp["choices"][0]["message"]["content"][:300]
    except Exception:
        pass
    print(f"  {label:54s} prompt={rec['prompt_tokens']} cached={rec['cached_tokens']} "
          f"write={rec['cache_write_tokens']} cost={rec['cost']} "
          f"prov={rec['provider_otvet']}"
          + (f"  ОШИБКА: {str(rec['error'])[:160]}" if rec["error"] else ""))
    return rec


def series_s1(pause):
    out = []
    base = baza.variant("bez_pravki")
    for mk in MODELS:
        print(f"\n[S1] {mk} — {MODELS[mk]['id']}")
        for marker in (False, True):
            tag = "s-tochkoy" if marker else "bez-tochki"
            for i, kind in enumerate(("holodnyi", "teplyi")):
                out.append(one(f"S1 · {mk} · {tag} · {kind}",
                               body_plain(mk, base, marker=marker),
                               {"seriya": "S1", "model_klyuch": mk, "tochka": tag,
                                "vyzov": kind, "povtor": i}))
                time.sleep(pause)
    return out


def nonce():
    return f"{int(time.time() * 1000) % 100000000:08d}"


def series_s2(pause, keys):
    """Куда дописывать пункт. Три вызова на вариант, все с одной меткой опыта:
    холодный (пишет кэш) → тёплый (читает его, подтверждает, что кэш жив) → правленая база.
    """
    out = []
    for mk in keys:
        print(f"\n[S2] {mk} — {MODELS[mk]['id']} (промт одной строкой, без cache_control)")
        for v in baza.VARIANTS:
            nz = nonce()
            base = baza.variant("bez_pravki", nonce=nz)
            for rol in ("holodnyi", "teplyi"):
                out.append(one(f"S2 · {mk} · {v} · {rol}", body_plain(mk, base),
                               {"seriya": "S2", "model_klyuch": mk, "variant": v,
                                "rol": rol, "nonce": nz}))
                time.sleep(pause)
            out.append(one(f"S2 · {mk} · {v} · ZAMER",
                           body_plain(mk, baza.variant(v, nonce=nz)),
                           {"seriya": "S2", "model_klyuch": mk, "variant": v,
                            "rol": "zamer", "nonce": nz}))
            time.sleep(pause)
    return out


def series_s3(pause, mk="haiku"):
    """Anthropic: как выставляется контрольная точка.

    R1 — справочник ОДНИМ текстовым блоком, cache_control в конце этого блока.
    R2 — справочник ЧЕТЫРЬМЯ блоками, cache_control на последнем блоке справочника;
         в случае дописывания новый пункт идёт ОТДЕЛЬНЫМ блоком и точка переезжает на него.
    R3 — без cache_control вовсе: кэшируется ли хоть что-нибудь по умолчанию.
    Внутри каждого варианта — три вызова с одной меткой опыта (холодный, тёплый, замер).
    """
    out = []

    print(f"\n[S3/R1] {mk} — справочник одним блоком, точка в конце блока")
    for v in baza.VARIANTS:
        nz = nonce()
        base = baza.variant("bez_pravki", nonce=nz)
        for rol in ("holodnyi", "teplyi"):
            out.append(one(f"S3/R1 · {v} · {rol}", body_plain(mk, base, marker=True),
                           {"seriya": "S3", "raskladka": "R1-odin-blok",
                            "model_klyuch": mk, "variant": v, "rol": rol, "nonce": nz}))
            time.sleep(pause)
        out.append(one(f"S3/R1 · {v} · ZAMER",
                       body_plain(mk, baza.variant(v, nonce=nz), marker=True),
                       {"seriya": "S3", "raskladka": "R1-odin-blok",
                        "model_klyuch": mk, "variant": v, "rol": "zamer", "nonce": nz}))
        time.sleep(pause)

    print(f"\n[S3/R2] {mk} — справочник четырьмя блоками, точка на последнем")
    items = list(baza.KB_ITEMS)
    mid = len(items) // 2
    for v in baza.VARIANTS:
        nz = nonce()
        for rol in ("holodnyi", "teplyi"):
            out.append(one(f"S3/R2 · {v} · {rol}", body_bloki(mk, items, nonce=nz),
                           {"seriya": "S3", "raskladka": "R2-chetyre-bloka",
                            "model_klyuch": mk, "variant": v, "rol": rol, "nonce": nz}))
            time.sleep(pause)
        if v == "bez_pravki":
            b = body_bloki(mk, items, nonce=nz)
        elif v == "dopisan_v_konets":
            b = body_bloki(mk, items, extra_block=baza.NEW_ITEM, nonce=nz)
        elif v == "vstavlen_v_seredinu":
            b = body_bloki(mk, items[:mid] + [baza.NEW_ITEM] + items[mid:], nonce=nz)
        else:
            b = body_bloki(mk, [baza.NEW_ITEM] + items, nonce=nz)
        out.append(one(f"S3/R2 · {v} · ZAMER", b,
                       {"seriya": "S3", "raskladka": "R2-chetyre-bloka",
                        "model_klyuch": mk, "variant": v, "rol": "zamer", "nonce": nz}))
        time.sleep(pause)

    print(f"\n[S3/R3] {mk} — совсем без cache_control, три одинаковых вызова")
    nz = nonce()
    base = baza.variant("bez_pravki", nonce=nz)
    for i in range(3):
        out.append(one(f"S3/R3 · povtor {i + 1}", body_plain(mk, base, marker=False),
                       {"seriya": "S3", "raskladka": "R3-bez-cache-control",
                        "model_klyuch": mk, "povtor": i + 1, "rol": "zamer",
                        "nonce": nz}))
        time.sleep(pause)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--series", required=True, choices=["S1", "S2", "S3"])
    ap.add_argument("--out", required=True)
    ap.add_argument("--pause", type=float, default=1.5)
    ap.add_argument("--models", default="haiku,gemini,gpt")
    a = ap.parse_args()
    if a.series == "S1":
        res = series_s1(a.pause)
    elif a.series == "S2":
        res = series_s2(a.pause, [m.strip() for m in a.models.split(",") if m.strip()])
    else:
        res = series_s3(a.pause)
    p = HERE / a.out
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nзаписано: {p}  вызовов: {len(res)}")
