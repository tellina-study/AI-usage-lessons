"""Докачка выбранной порции кандидатов из candidates_C100.json (см.
find_candidates_C100.py) в существующие директории корпуса C-fooddrink/C-slides —
issue #351, Веха «sto-testov». Выбор id детерминированный (сортировка по id, первые N) —
без подгонки под результат. N — явная выборка из доступного пула, не весь пул (пул
174/217, подробности в README §«Корпус»). Пишет sha256 каждого файла в
manifest-additions-C100.json (тот же принцип, что plan-peredelki/korpus/manifest-foto-
BC.json — трассируемость, не бинарник в гит)."""
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

OIV7 = Path("/tmp/s12-corpora/oiv7")
IMAGES = OIV7 / "images"
HERE = Path(__file__).parent

N_FOOD = 70
N_SLIDES = 35
DIR_FOR = {"food": IMAGES / "C-fooddrink", "slides": IMAGES / "C-slides"}
N_FOR = {"food": N_FOOD, "slides": N_SLIDES}


def main():
    cands = json.load(open(OIV7 / "candidates_C100.json"))
    manifest_path = HERE / "manifest-additions-C100.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    done_ids = {m["id"] for m in manifest}

    for cls, items in cands.items():
        items_sorted = sorted(items, key=lambda c: c["id"])
        take = items_sorted[:N_FOR[cls]]
        print(f"{cls}: доступно {len(items_sorted)}, беру выборку {len(take)}")
        d = DIR_FOR[cls]
        d.mkdir(parents=True, exist_ok=True)
        got = 0
        for c in take:
            p = d / f"{c['id']}.jpg"
            if not p.exists():
                try:
                    urllib.request.urlretrieve(c["s3_url"], p)
                except Exception as e:
                    print(f"  ОШИБКА скачивания {c['id']}: {e}")
                    continue
            sha = hashlib.sha256(p.read_bytes()).hexdigest()
            if c["id"] not in done_ids:
                manifest.append({
                    "id": c["id"], "class": cls, "label_name": c["label_name"],
                    "subset": c["subset"], "license": c["license"], "author": c["author"],
                    "landing": c["landing"], "s3_url": c["s3_url"], "sha256": sha,
                })
                done_ids.add(c["id"])
            got += 1
        print(f"  скачано/проверено: {got}")

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    print("манифест:", manifest_path, "записей:", len(manifest))


if __name__ == "__main__":
    main()
