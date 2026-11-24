#!/usr/bin/env python3
"""Загрузчик корпуса-101 для замера D круга 3 (прежний `corpus_b.py` жёстко
ожидает 40 снимков и оставлен как есть — он воспроизводит круг 1).

Входы: `zamery-B/opisaniya-101.json`, `zamery-B/razmetka-101.json`,
картинки — `zamery-B/corpus-cache/<id>.jpg` (все 101 в одной папке).
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZB = HERE.parent / "zamery-B"
IMAGES = ZB / "corpus-cache"


def load_opisaniya():
    doc = json.loads((ZB / "opisaniya-101.json").read_text(encoding="utf-8"))
    return {e["id"]: e for e in doc["entries"]}, doc["methods"]


def load_razmetka():
    doc = json.loads((ZB / "razmetka-101.json").read_text(encoding="utf-8"))
    return {e["id"]: e for e in doc["entries"] if e["in_corpus"]}


def find_image_path(doc_id):
    p = IMAGES / f"{doc_id}.jpg"
    if not p.exists():
        raise FileNotFoundError(f"нет файла картинки для {doc_id}")
    return p


def corpus_ids():
    op, _ = load_opisaniya()
    rz = load_razmetka()
    ids = sorted(set(op) & set(rz))
    assert len(ids) == 101, f"ожидался 101 снимок корпуса, получено {len(ids)}"
    return ids


def short_id_map(ids):
    m = {}
    for full in ids:
        short = full[:8]
        if short in m:
            raise ValueError(f"короткий префикс {short} не уникален: {m[short]} и {full}")
        m[short] = full
    return m


def resolve_id(s, smap):
    if s in smap.values():
        return s
    if s in smap:
        return smap[s]
    raise KeyError(f"id {s!r} не найден")


if __name__ == "__main__":
    ids = corpus_ids()
    print(f"корпус: {len(ids)} снимков")
    missing = [i for i in ids if not (IMAGES / f"{i}.jpg").exists()]
    print("без файла картинки:", len(missing), missing[:5])
    op, methods = load_opisaniya()
    print("методы:", list(methods.keys()))
    print("без рассказа:", sum(1 for i in ids if not op[i]["caption"]))
