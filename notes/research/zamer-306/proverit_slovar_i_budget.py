#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Счёт «изобретённых раскладок» и нарушений бюджета знаков — для ОБЕИХ
записей (слоты и HTML), по ОДНОЙ и той же мере.

Для слотов (`blocks:`/`scheme:`/`columns:`/`figure:` во фронтматтере):
читает фронтматтер файла кадра и ищет ключ ВНЕ закрытого перечня, который
читает соответствующий модуль ядра (`plates.py`/`scheme.py`/`axis.py`/
`columns.py`/`figure.py`). Часть этих ключей сборка и сама называет
([схема] печатает `_unknown` для `scheme:`-полей) — но НЕ печатает для
`blocks:`/`columns:`/`figure:`, потому что `plates_of`/`columns_of`/
`figure_of` лишний ключ молча отбрасывают без проверки. Это asymmetрия
самого ядра, и здесь она не чинится — здесь она измеряется.

Для HTML — дублирует проверку `html2kadr.parse_kadr_html`, уже выполненную
переводчиком; здесь нужна только затем, чтобы оба замера шли одним числом
через один и тот же отчёт `otchet-slovarya.json`.

Бюджет знаков на слот — ТЕ ЖЕ значения, что в `skelet-slotov.md`/
`slovar-tegov.md` (они там выведены прогоном через `deckkit.metrics`,
здесь просто переиспользованы как константы, чтобы не разводить две копии
одного измерения).
"""
import json
import sys
from pathlib import Path

import yaml

REPO = Path("/home/harness/harness-projects/256/.worktrees/folder-288/session-0b2adb13-7ee7af40")
ZAMER_DIR = REPO / "notes" / "research" / "zamer-306"
sys.path.insert(0, str(ZAMER_DIR))

# Закрытые перечни ключей — ТЕ ЖЕ, что в `tools/presentation-build/deckkit/`.
PLATE_KEYS = {"label", "value", "note", "key"}
SCHEME_TOP_KEYS = {"kind", "caption", "rows", "arrows", "entry", "exit",
                   "steps_arrows", "axis", "direction", "marks", "unit",
                   "base", "zero", "from", "to"}
SCHEME_ROW_KEYS = {"label", "steps", "arrows", "empty"}
SCHEME_STEP_KEYS = {"text", "step", "ai"}
AXIS_MARK_KEYS = {"value", "label", "key", "lo", "hi", "base"}
COLUMNS_SIDE_KEYS = {"head", "items"}
FIGURE_KEYS = {"value", "unit", "base", "note"}

BUDGET = {
    "plashka.label": 55, "plashka.value_digit": 48, "plashka.value_word": 72,
    "plashka.note": 85,
    "os.mark_label_3": 48, "os.mark_label_4": 37, "os.mark_label_5": 29,
    "os.unit": 134, "os.caption": 145,
    "stolbec.head": 97, "stolbec.punkt": 110,
    "shema.step4": 81, "shema.step3": 84, "shema.label": 33,
    "shema.caption": 145,
    "chislo.value": 16, "chislo.unit": 202, "chislo.base": 233,
    "chislo.note": 250,
}


def _extra(d, allowed):
    if not isinstance(d, dict):
        return []
    return sorted(k for k in d if k not in allowed)


def proverit_slot_file(path):
    """Один файл кадра (`sNN-*.md`) → (invented_keys[], budget_viol[])."""
    text = Path(path).read_text(encoding="utf-8")
    import re
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return [f"{path.name}: фронтматтер не найден"], []
    meta = yaml.safe_load(m.group(1)) or {}
    invented, budget = [], []

    if "blocks" in meta and meta["blocks"]:
        for i, p in enumerate(meta["blocks"], 1):
            for k in _extra(p, PLATE_KEYS):
                invented.append(f"{path.name}: blocks[{i}] ключ `{k}` вне "
                                 "закрытого перечня plates.py (НЕ поймано "
                                 "сборкой молча)")
            val = str(p.get("value") or "")
            is_digit = any(c.isdigit() for c in val)
            lim = BUDGET["plashka.value_digit" if is_digit else "plashka.value_word"]
            if len(val) > lim:
                budget.append(f"{path.name}: plashka value «{val[:30]}…» "
                               f"{len(val)} знаков (> {lim})")
            lab = str(p.get("label") or "")
            if len(lab) > BUDGET["plashka.label"]:
                budget.append(f"{path.name}: plashka label «{lab[:30]}…» "
                               f"{len(lab)} знаков (> {BUDGET['plashka.label']})")
            note = str(p.get("note") or "")
            if note and len(note) > BUDGET["plashka.note"]:
                budget.append(f"{path.name}: plashka note «{note[:30]}…» "
                               f"{len(note)} знаков (> {BUDGET['plashka.note']})")

    if "scheme" in meta and meta["scheme"]:
        sch = meta["scheme"]
        for k in _extra(sch, SCHEME_TOP_KEYS):
            invented.append(f"{path.name}: scheme ключ `{k}` вне закрытого "
                             "перечня scheme.py")
        if sch.get("kind") == "shkala":
            for i, mk in enumerate(sch.get("marks") or [], 1):
                for k in _extra(mk, AXIS_MARK_KEYS):
                    invented.append(f"{path.name}: marks[{i}] ключ `{k}` "
                                     "вне закрытого перечня axis.py")
                lab = str(mk.get("label") or "")
                n = len(sch.get("marks") or [])
                lim = BUDGET["os.mark_label_5"] if n >= 5 else (
                    BUDGET["os.mark_label_4"] if n == 4 else BUDGET["os.mark_label_3"])
                if len(lab) > lim:
                    budget.append(f"{path.name}: zasechka label «{lab[:30]}…» "
                                   f"{len(lab)} знаков (> {lim}, n_marks={n})")
            unit = str(sch.get("unit") or "")
            if len(unit) > BUDGET["os.unit"]:
                budget.append(f"{path.name}: os unit {len(unit)} знаков "
                               f"(> {BUDGET['os.unit']})")
            cap = str(sch.get("caption") or "")
            if len(cap) > BUDGET["os.caption"]:
                budget.append(f"{path.name}: os caption {len(cap)} знаков "
                               f"(> {BUDGET['os.caption']})")
        else:
            rows = sch.get("rows") or []
            for i, r in enumerate(rows, 1):
                for k in _extra(r, SCHEME_ROW_KEYS):
                    invented.append(f"{path.name}: rows[{i}] ключ `{k}` вне "
                                     "закрытого перечня scheme.py (ROW_KEYS)")
                steps = r.get("steps") or []
                n_steps = len(steps)
                lim = BUDGET["shema.step4"] if n_steps >= 4 else BUDGET["shema.step3"]
                for step in steps:
                    if isinstance(step, dict):
                        for k in _extra(step, SCHEME_STEP_KEYS):
                            invented.append(f"{path.name}: step ключ `{k}` "
                                             "вне закрытого перечня (STEP_KEYS)")
                        t = str(step.get("text") or step.get("step") or "")
                    else:
                        t = str(step)
                    if len(t) > lim:
                        budget.append(f"{path.name}: шаг схемы «{t[:30]}…» "
                                       f"{len(t)} знаков (> {lim}, n_steps={n_steps})")
                lab = str(r.get("label") or "")
                if lab and len(lab) > BUDGET["shema.label"]:
                    budget.append(f"{path.name}: подпись ряда «{lab[:30]}…» "
                                   f"{len(lab)} знаков (> {BUDGET['shema.label']})")
            cap = str(sch.get("caption") or "")
            if cap and len(cap) > BUDGET["shema.caption"]:
                budget.append(f"{path.name}: scheme caption {len(cap)} "
                               f"знаков (> {BUDGET['shema.caption']})")

    if "columns" in meta and meta["columns"]:
        cols = meta["columns"]
        for side in ("left", "mid", "right"):
            c = cols.get(side)
            if not c:
                continue
            for k in _extra(c, COLUMNS_SIDE_KEYS):
                invented.append(f"{path.name}: columns.{side} ключ `{k}` "
                                 "вне закрытого перечня columns.py")
            head = str(c.get("head") or "")
            if len(head) > BUDGET["stolbec.head"]:
                budget.append(f"{path.name}: columns.{side} head {len(head)} "
                               f"знаков (> {BUDGET['stolbec.head']})")
            for it in c.get("items") or []:
                if len(str(it)) > BUDGET["stolbec.punkt"]:
                    budget.append(
                        f"{path.name}: columns.{side} пункт «{str(it)[:30]}…» "
                        f"{len(str(it))} знаков (> {BUDGET['stolbec.punkt']})")

    if "figure" in meta and meta["figure"]:
        fig = meta["figure"]
        for k in _extra(fig, FIGURE_KEYS):
            invented.append(f"{path.name}: figure ключ `{k}` вне закрытого "
                             "перечня figure.py")
        val = str(fig.get("value") or "")
        if len(val) > BUDGET["chislo.value"]:
            budget.append(f"{path.name}: figure value «{val}» {len(val)} "
                           f"знаков (> {BUDGET['chislo.value']})")
        for key in ("unit", "base", "note"):
            v = str(fig.get(key) or "")
            lim = BUDGET[f"chislo.{key}"]
            if v and len(v) > lim:
                budget.append(f"{path.name}: figure {key} {len(v)} знаков "
                               f"(> {lim})")

    return invented, budget


def proverit_html_file(path):
    import html2kadr
    text = Path(path).read_text(encoding="utf-8")
    field, warns = html2kadr.parse_kadr_html(text, where=path.name)
    invented = [w for w in warns]
    budget = []
    if field:
        if "blocks" in field:
            for p in field["blocks"]:
                val = p.get("value") or ""
                is_digit = any(c.isdigit() for c in val)
                lim = BUDGET["plashka.value_digit" if is_digit else "plashka.value_word"]
                if len(val) > lim:
                    budget.append(f"{path.name}: znachenie «{val[:30]}…» "
                                   f"{len(val)} знаков (> {lim})")
                lab = p.get("label") or ""
                if len(lab) > BUDGET["plashka.label"]:
                    budget.append(f"{path.name}: podpis «{lab[:30]}…» "
                                   f"{len(lab)} знаков (> {BUDGET['plashka.label']})")
                note = p.get("note") or ""
                if note and len(note) > BUDGET["plashka.note"]:
                    budget.append(f"{path.name}: ogovorka {len(note)} "
                                   f"знаков (> {BUDGET['plashka.note']})")
        if "scheme" in field and field["scheme"].get("kind") == "shkala":
            sch = field["scheme"]
            n = len(sch["marks"])
            lim = BUDGET["os.mark_label_5"] if n >= 5 else (
                BUDGET["os.mark_label_4"] if n == 4 else BUDGET["os.mark_label_3"])
            for mk in sch["marks"]:
                lab = mk.get("label") or ""
                if len(lab) > lim:
                    budget.append(f"{path.name}: podpis zasechki {len(lab)} "
                                   f"знаков (> {lim})")
            if len(sch.get("unit") or "") > BUDGET["os.unit"]:
                budget.append(f"{path.name}: edinica {len(sch['unit'])} "
                               f"знаков (> {BUDGET['os.unit']})")
            if len(sch.get("caption") or "") > BUDGET["os.caption"]:
                budget.append(f"{path.name}: podpis_osi "
                               f"{len(sch['caption'])} знаков "
                               f"(> {BUDGET['os.caption']})")
        elif "scheme" in field:
            sch = field["scheme"]
            for r in sch["rows"]:
                n_steps = len(r["steps"])
                lim = BUDGET["shema.step4"] if n_steps >= 4 else BUDGET["shema.step3"]
                for t in r["steps"]:
                    if len(t) > lim:
                        budget.append(f"{path.name}: shag «{t[:30]}…» "
                                       f"{len(t)} знаков (> {lim})")
                if r.get("label") and len(r["label"]) > BUDGET["shema.label"]:
                    budget.append(f"{path.name}: ryad podpis "
                                   f"{len(r['label'])} знаков "
                                   f"(> {BUDGET['shema.label']})")
            if sch.get("caption") and len(sch["caption"]) > BUDGET["shema.caption"]:
                budget.append(f"{path.name}: podpis_shemy "
                               f"{len(sch['caption'])} знаков "
                               f"(> {BUDGET['shema.caption']})")
        if "columns" in field:
            for side in ("left", "right"):
                c = field["columns"][side]
                if len(c["head"]) > BUDGET["stolbec.head"]:
                    budget.append(f"{path.name}: zagolovok {side} "
                                   f"{len(c['head'])} знаков "
                                   f"(> {BUDGET['stolbec.head']})")
                for it in c["items"]:
                    if len(it) > BUDGET["stolbec.punkt"]:
                        budget.append(f"{path.name}: punkt «{it[:30]}…» "
                                       f"{len(it)} знаков "
                                       f"(> {BUDGET['stolbec.punkt']})")
        if "figure" in field:
            fig = field["figure"]
            if len(fig["value"]) > BUDGET["chislo.value"]:
                budget.append(f"{path.name}: znachenie «{fig['value']}» "
                               f"{len(fig['value'])} знаков "
                               f"(> {BUDGET['chislo.value']})")
            for key in ("unit", "base", "note"):
                v = fig.get(key) or ""
                lim = BUDGET[f"chislo.{key}"]
                if v and len(v) > lim:
                    budget.append(f"{path.name}: {key} {len(v)} знаков "
                                   f"(> {lim})")
    return invented, budget


def proverit_nabor(nabor):
    sd = ZAMER_DIR / nabor
    invented_all, budget_all = [], []
    md_files = sorted(sd.glob("s*-kadr*.md"))
    html_files = sorted(sd.glob("kadr-*.html"))
    for f in md_files:
        inv, bud = proverit_slot_file(f)
        invented_all += inv
        budget_all += bud
    for f in html_files:
        inv, bud = proverit_html_file(f)
        invented_all += inv
        budget_all += bud
    result = {"nabor": nabor, "invented": invented_all, "budget": budget_all}
    (sd / "otchet-slovarya.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{nabor}: изобретённых ключей {len(invented_all)} · "
          f"нарушений бюджета {len(budget_all)}")
    for w in invented_all:
        print("  [изобретено] " + w)
    for w in budget_all:
        print("  [бюджет] " + w)
    return result


if __name__ == "__main__":
    naborees = sys.argv[1:] or ["nabor-1", "nabor-2", "nabor-3", "nabor-4"]
    for nb in naborees:
        proverit_nabor(nb)
