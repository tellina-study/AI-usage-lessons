#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Контроль D12 — корпус FUNSD: полный OCR-текст формы (из разметки FUNSD,
`words`/`text` поля — то же самое, что в реальном пайплайне даёт OCR-слой,
здесь уже готово), путь к сканy формы."""
import json
from pathlib import Path

ROOT = Path("/tmp/s12-corpora/funsd/dataset/testing_data")
ANN = ROOT / "annotations"
IMAGES = ROOT / "images"


def load_fulltext():
    out = {}
    for f in sorted(ANN.glob("*.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        text = " | ".join(it["text"] for it in doc["form"] if it["text"].strip())
        out[f.stem] = text
    return out


def image_path(doc_id):
    p = IMAGES / f"{doc_id}.png"
    assert p.exists(), f"нет файла скана для {doc_id}"
    return p


def doc_ids():
    ids = sorted(f.stem for f in ANN.glob("*.json"))
    assert len(ids) == 50, f"ожидалось 50 форм FUNSD testing_data, получено {len(ids)}"
    return ids


if __name__ == "__main__":
    ids = doc_ids()
    texts = load_fulltext()
    print(f"FUNSD testing_data: {len(ids)} форм, {len(texts)} текстов")
