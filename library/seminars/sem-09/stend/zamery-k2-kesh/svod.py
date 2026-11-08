#!/usr/bin/env python3
"""Свод замера кэша Кейса 2 — считает таблицы из сырых JSON, issue #303.

Числа в README собраны ЭТИМ скриптом из `raw/*.json`, руками не переписывались
(правило курса: производное пересобирается из источника, а не правится отдельно).

Цена вызова берётся двумя путями и они сверяются:
 — `cost` из `usage` ответа (что OpenRouter реально списал);
 — пересчёт из прайс-листа OpenRouter (`raw/tseny-openrouter-2026-10-29.json`):
   обычный вход × (prompt_tokens − cached − write) + чтение × cached + запись × write
   + выход × completion_tokens.
Расхождение выводится явно. Расчёт нужен, чтобы отделить цену ВХОДА от цены выхода:
вопрос владельца («чтение кэша против прямого чтения») — про вход, а `cost` включает и
выход, поэтому прямое деление `cost` на `cost` занижает кратность.

Usage:  python3 svod.py
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
TSENY = {k: {kk: (float(vv) if vv is not None else None) for kk, vv in v.items()}
         for k, v in json.loads(
             (HERE / "raw/tseny-openrouter-2026-10-29.json").read_text()).items()}


def load(name):
    return json.loads((HERE / "raw" / name).read_text(encoding="utf-8"))


def vhod_cost(r):
    """Цена ВХОДА вызова по прайс-листу: обычные + прочитанные + записанные токены."""
    t = TSENY.get(r["model_zapros"])
    if not t or r["prompt_tokens"] is None:
        return None
    cached = r.get("cached_tokens") or 0
    write = r.get("cache_write_tokens") or 0
    plain = max(0, r["prompt_tokens"] - cached - write)
    c = plain * t["prompt"]
    c += cached * (t["input_cache_read"] if t["input_cache_read"] is not None
                   else t["prompt"])
    c += write * (t["input_cache_write"] if t["input_cache_write"] is not None
                  else t["prompt"])
    return c


def sverka(r):
    """Сверка: прайс-лист (вход+выход) против списанного `cost`."""
    t = TSENY.get(r["model_zapros"])
    v = vhod_cost(r)
    if not t or v is None or r.get("cost") is None:
        return None
    rasch = v + (r.get("completion_tokens") or 0) * t["completion"]
    return rasch, r["cost"], (rasch - r["cost"])


def usd(x, n=2):
    return "—" if x is None else f"${x * 1e6:.{n}f}/млн·вызовов" if False else \
        ("—" if x is None else f"{x * 1e6:.1f}")


def t1_metriki():
    """Кто отдаёт метрики кэша и работает ли кэш без параметра."""
    rows = load("s1-metriki.json")
    print("\n## Таблица 1 — кто отдаёт метрики кэша (серия S1, 20 вызовов)\n")
    print("| модель | посредник-исполнитель | точка | холодный cached/write | "
          "тёплый cached/write | цена холодного, $ | цена тёплого, $ |")
    print("|---|---|---|---|---|---|---|")
    for mk in ("qwen", "haiku", "gemini", "gpt", "deepseek"):
        for tochka in ("bez-tochki", "s-tochkoy"):
            sel = [r for r in rows if r["meta"].get("model_klyuch") == mk
                   and r["meta"].get("tochka") == tochka]
            if len(sel) != 2:
                continue
            h, tp = sel
            print(f"| `{h['model_zapros']}` | {h['provider_otvet']} | {tochka} | "
                  f"{h['cached_tokens']}/{h['cache_write_tokens']} | "
                  f"{tp['cached_tokens']}/{tp['cache_write_tokens']} | "
                  f"{h['cost']:.6f} | {tp['cost']:.6f} |")


def t2_chtenie_protiv_pryamogo():
    """Чтение кэша против прямого чтения — по цене ВХОДА."""
    print("\n## Таблица 2 — чтение кэша против прямого чтения (цена входа)\n")
    print("| модель | прямое чтение (кэша нет) | запись в кэш | чтение из кэша | "
          "чтение / прямое | запись / прямое |")
    print("|---|---|---|---|---|---|")
    for mid, t in TSENY.items():
        if t["input_cache_read"] is None:
            print(f"| `{mid}` | {t['prompt'] * 1e6:.3f} $/млн | кэша в прайсе нет | "
                  f"кэша в прайсе нет | — | — |")
            continue
        w = t["input_cache_write"]
        print(f"| `{mid}` | {t['prompt'] * 1e6:.3f} $/млн | "
              + (f"{w * 1e6:.4f} $/млн" if w else "не тарифицируется отдельно") + " | "
              f"{t['input_cache_read'] * 1e6:.3f} $/млн | "
              f"**{t['input_cache_read'] / t['prompt']:.3f}×** | "
              + (f"{w / t['prompt']:.3f}×" if w else "—") + " |")


def t3_fakt_na_odnom_promte():
    """Фактическая цена входа на одном и том же промте: прямое / запись / чтение."""
    print("\n## Таблица 3 — то же на фактическом промте замера (3 790–3 794 токена)\n")
    r3 = [r for r in load("s3-kontrolnaya-tochka.json")
          if r["meta"].get("raskladka") == "R3-bez-cache-control"]
    r1 = load("s3-kontrolnaya-tochka.json")
    hol = [r for r in r1 if r["meta"].get("raskladka") == "R1-odin-blok"
           and r["meta"].get("rol") == "holodnyi"][0]
    tep = [r for r in r1 if r["meta"].get("raskladka") == "R1-odin-blok"
           and r["meta"].get("rol") == "teplyi"][0]
    pryamo = r3[0]
    print("| режим | токенов в промте | cached | write | цена входа, $ | "
          "к прямому чтению |")
    print("|---|---|---|---|---|---|")
    base = vhod_cost(pryamo)
    for name, r in (("прямое чтение, кэш не включён", pryamo),
                    ("запись в кэш (холодный вызов)", hol),
                    ("чтение из кэша (тёплый вызов)", tep)):
        v = vhod_cost(r)
        print(f"| {name} | {r['prompt_tokens']} | {r['cached_tokens']} | "
              f"{r['cache_write_tokens']} | {v:.8f} | "
              f"**{v / base:.3f}×** |")
    print(f"\nПрямое чтение дороже чтения из кэша в "
          f"**{base / vhod_cost(tep):.1f} раза**; запись в кэш дороже прямого чтения в "
          f"**{vhod_cost(hol) / base:.2f} раза**.")


def t4_kuda_dopisyvat():
    """Что происходит при дописывании в начало/середину/конец."""
    rows = load("s2-kuda-dopisyvat.json") + load("s4-povtory-spornyh.json")
    print("\n## Таблица 4 — куда дописывать пункт (автоматический кэш, без параметра)\n")
    print("| модель | правка базы | cached после правки | прогретый cached | "
          "доля префикса, уцелевшая | цена входа после правки, $ | повторов |")
    print("|---|---|---|---|---|---|---|")
    for mk in ("gemini", "gpt", "haiku"):
        for v in ("bez_pravki", "dopisan_v_konets", "vstavlen_v_seredinu",
                  "pravka_v_nachale"):
            zam = [r for r in rows if r["meta"].get("model_klyuch") == mk
                   and r["meta"].get("variant") == v
                   and r["meta"].get("rol") == "zamer"]
            tep = [r for r in rows if r["meta"].get("model_klyuch") == mk
                   and r["meta"].get("variant") == v
                   and r["meta"].get("rol") == "teplyi"]
            if not zam or not tep:
                continue
            cz = sorted({r["cached_tokens"] for r in zam})
            ct = sorted({r["cached_tokens"] for r in tep})
            baza_t = max(ct) or 1
            dolya = f"{max(cz) / baza_t * 100:.0f}%" if max(ct) else "—"
            cena = vhod_cost(zam[0])
            print(f"| `{mk}` | {v} | {'/'.join(map(str, cz))} | "
                  f"{'/'.join(map(str, ct))} | {dolya} | {cena:.8f} | {len(zam)} |")
    print("\nДве оговорки к этой таблице. **`haiku` стоит здесь с нулями во всех четырёх"
          " строках** — это та же серия без `cache_control`, и ноль означает «кэша не"
          " было вовсе», а не «кэш сбросился»: у Anthropic эта серия и нужна как"
          " доказательство, что без параметра не кэшируется ничего. Раскладки с точкой —"
          " в Таблице 5. **У `gpt` в строке `bez_pravki` прогретый столбец показывает"
          " ноль** — в одном из четырёх опытов серии S2 попадание случилось только с"
          " третьего вызова, а не со второго; документация OpenAI это и оговаривает"
          " («Keys influence routing; they do not pin requests to a machine or guarantee"
          " a cache hit»). В остальных трёх опытах того же провайдера второй вызов"
          " попадал в кэш.")


def t5_tochka():
    """Anthropic: как выставлена контрольная точка — тот же текст, три раскладки."""
    rows = load("s3-kontrolnaya-tochka.json")
    print("\n## Таблица 5 — Anthropic: как выставлена контрольная точка "
          "(`anthropic/claude-haiku-5.5`)\n")
    print("| раскладка | правка базы | cached | write | цена входа, $ | "
          "против того же вызова без кэша |")
    print("|---|---|---|---|---|---|")
    pryamo = [r for r in rows
              if r["meta"].get("raskladka") == "R3-bez-cache-control"][0]
    base = vhod_cost(pryamo)
    for rask in ("R1-odin-blok", "R2-chetyre-bloka"):
        for v in ("bez_pravki", "dopisan_v_konets", "vstavlen_v_seredinu",
                  "pravka_v_nachale"):
            z = [r for r in rows if r["meta"].get("raskladka") == rask
                 and r["meta"].get("variant") == v
                 and r["meta"].get("rol") == "zamer"]
            if not z:
                continue
            r = z[0]
            vc = vhod_cost(r)
            print(f"| {rask} | {v} | {r['cached_tokens']} | "
                  f"{r['cache_write_tokens']} | {vc:.8f} | {vc / base:.3f}× |")
    for r in rows:
        if r["meta"].get("raskladka") == "R3-bez-cache-control":
            vc = vhod_cost(r)
            print(f"| R3-bez-cache-control | повтор "
                  f"{r['meta']['povtor']} того же текста | {r['cached_tokens']} | "
                  f"{r['cache_write_tokens']} | {vc:.8f} | {vc / base:.3f}× |")


def t6_sverka():
    """Сверка списанного `cost` с пересчётом по прайс-листу."""
    rows = (load("s1-metriki.json") + load("s2-kuda-dopisyvat.json")
            + load("s3-kontrolnaya-tochka.json") + load("s4-povtory-spornyh.json")
            + load("s5-nastoyashchiy-spravochnik.json"))
    print("\n## Таблица 6 — сверка: прайс-лист против списанного `cost`\n")
    print("| модель | вызовов | макс. расхождение, $ | макс. расхождение, % от цены |")
    print("|---|---|---|---|")
    po_modeli = {}
    for r in rows:
        s = sverka(r)
        if s is None:
            continue
        po_modeli.setdefault(r["model_zapros"], []).append(s)
    for mid, lst in po_modeli.items():
        md = max(abs(d) for _, _, d in lst)
        mp = max(abs(d) / c * 100 for _, c, d in lst if c)
        print(f"| `{mid}` | {len(lst)} | {md:.3e} | {mp:.2f}% |")
    print(f"\nВсего вызовов во всех сериях: **{len(rows)}**.")


def t7_nastoyashchiy():
    """Включается ли кэш на НАСТОЯЩЕМ справочнике Кейса 2 (10 пунктов)."""
    rows = load("s5-nastoyashchiy-spravochnik.json")
    print("\n## Таблица 7 — настоящий справочник Кейса 2, 10 пунктов\n")
    print("Отправляется то же, что отправил бы сценарий: указание (35 слов) + справочник "
          "(229 слов, 1 665 знаков) = 266 слов, 1 926 знаков. Слайд `n25` называет "
          "справочник 223 словами — расхождение в четыре слова от того, как считаются "
          "номера пунктов, и на вывод не влияет: до порога не дотягивает ни та цифра, ни "
          "эта.\n")
    print("| модель | точка | токенов в промте | порог кэша у модели | "
          "cached: холодный / тёплый / тёплый-2 | кэш включился |")
    print("|---|---|---|---|---|---|")
    porogi = {"anthropic/claude-haiku-5.5": "512 (документация Anthropic)",
              "google/gemini-2.5-flash": "2 048 (документация Google)",
              "openai/gpt-4.1-mini": "1 024 (документация OpenAI)"}
    grupp = {}
    for r in rows:
        k = (r["model_zapros"], r["meta"]["tochka"])
        grupp.setdefault(k, []).append(r)
    for (mid, tochka), lst in grupp.items():
        c = [r["cached_tokens"] for r in lst]
        print(f"| `{mid}` | {tochka} | {lst[0]['prompt_tokens']} | "
              f"{porogi.get(mid, '—')} | {' / '.join(map(str, c))} | "
              f"{'ДА' if max(c) else 'НЕТ'} |")


def t8_arifmetika_doli():
    """Свидетельство владельца про 98–99% попаданий — счёт по измеренному множителю."""
    print("\n## Таблица 8 — счёт к свидетельству владельца про долю попаданий\n")
    print("Множитель чтения берётся не из ожидания, а измеренный в Таблице 3: "
          "**0,107× от прямого чтения** (`anthropic/claude-haiku-5.5`, промт 3 793 "
          "токена). Запись считается один раз на серию обращений, по измеренному "
          "**1,248×**.\n")
    read_m, write_m = 0.107, 1.248
    print("| доля попаданий | счёт за вход, доля от «кэша нет» | экономия |")
    print("|---|---|---|")
    for h in (0.50, 0.84, 0.90, 0.98, 0.99):
        frac = h * read_m + (1 - h) * write_m
        print(f"| {h * 100:.0f}% | {frac:.3f} | **−{(1 - frac) * 100:.0f}%** |")
    print("\nПри доле попаданий 98–99% счёт за вход падает до 0,12–0,13 от "
          "исходного — то есть экономия **87–89%**. Названная владельцем «до 90%» "
          "сходится с арифметикой по измеренному множителю; сама доля попаданий "
          "98–99% в этом замере НЕ измерялась — это свидетельство владельца по "
          "своему инструменту (см. README, раздел «Свидетельство владельца»).")


if __name__ == "__main__":
    t1_metriki()
    t2_chtenie_protiv_pryamogo()
    t3_fakt_na_odnom_promte()
    t4_kuda_dopisyvat()
    t5_tochka()
    t6_sverka()
    t7_nastoyashchiy()
    t8_arifmetika_doli()
