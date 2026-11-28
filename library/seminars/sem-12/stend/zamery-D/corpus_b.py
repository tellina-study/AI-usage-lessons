#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Общий загрузчик корпуса B для замера D: тексты рассказа (caption, то, по
чему реально ищут ветки 1 и 2), человеческая разметка «что видно» (истина,
используется только для проверки находок про выдумки — не как индекс поиска)
и пути к файлам картинок на диске (для ветки 3).

Входы (чужая зона, не правлю, см. zhurnal.md за точными коммитами):
- zamery-B/opisaniya.json
- zamery-B/razmetka.json
- /tmp/s12-corpora/oiv7/images/<группа>/<id>.jpg — локальный кэш снимков
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZB = HERE.parent / "zamery-B"
IMAGES_ROOT = Path("/tmp/s12-corpora/oiv7/images")


def load_opisaniya():
    doc = json.loads((ZB / "opisaniya.json").read_text(encoding="utf-8"))
    return {e["id"]: e for e in doc["entries"]}, doc["methods"]


def load_razmetka():
    doc = json.loads((ZB / "razmetka.json").read_text(encoding="utf-8"))
    return {e["id"]: e for e in doc["entries"] if e["in_corpus"]}


def find_image_path(doc_id):
    hits = list(IMAGES_ROOT.glob(f"*/{doc_id}.jpg"))
    if not hits:
        raise FileNotFoundError(f"нет файла картинки для {doc_id}")
    return hits[0]


def corpus_ids():
    op, _ = load_opisaniya()
    rz = load_razmetka()
    ids = sorted(set(op) & set(rz))
    assert len(ids) == 40, f"ожидалось 40 снимков корпуса B, получено {len(ids)}"
    return ids


def short_id_map(ids):
    """Таблицы запросов (`zaprosy-B.md`, `zaprosy-klass1-finalizirovano.md`)
    называют ответы короткими 8-символьными префиксами id Open Images, а
    `razmetka.json`/`opisaniya.json` хранят полные 16-символьные id. Префиксы
    уникальны по корпусу (проверено при каждом вызове) — сопоставление по ним
    безопасно."""
    m = {}
    for full in ids:
        short = full[:8]
        if short in m:
            raise ValueError(f"короткий префикс {short} не уникален: {m[short]} и {full}")
        m[short] = full
    return m


def resolve_id(short_or_full, smap):
    if short_or_full in smap.values():
        return short_or_full
    if short_or_full in smap:
        return smap[short_or_full]
    raise KeyError(f"id {short_or_full!r} не найден ни коротким, ни полным")


if __name__ == "__main__":
    ids = corpus_ids()
    print(f"корпус B: {len(ids)} снимков")
    op, methods = load_opisaniya()
    print("методы:", list(methods.keys()))
    missing_img = [i for i in ids if not list(IMAGES_ROOT.glob(f"*/{i}.jpg"))]
    print("без файла картинки:", missing_img)
