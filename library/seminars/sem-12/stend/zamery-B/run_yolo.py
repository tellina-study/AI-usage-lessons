"""Метод «теги общим детектором» — yolov8n (COCO, 80 классов), локально, CPU.
Порог conf>=0.25 (план §5). Вывод: список класс:уверенность, сортировка по
уверенности убыв.; дубли класса схлопываются (берётся максимум) — так,
как их видел бы человек, листающий теги в карточке архива, не raw-боксы.

Запуск:  .venv/bin/python run_yolo.py
"""
import json
import time
from pathlib import Path

from ultralytics import YOLO

HERE = Path(__file__).resolve().parent
CORPUS = HERE / "corpus-cache"
RAZMETKA = HERE / "razmetka.json"
OUT = HERE / "raw_yolo_results.json"
CONF = 0.25
MODEL_NAME = "yolov8n.pt"


def main():
    doc = json.loads(RAZMETKA.read_text(encoding="utf-8"))
    ids = [e["id"] for e in doc["entries"] if e["in_corpus"]]
    model = YOLO(MODEL_NAME)
    results = {}
    t_all0 = time.time()
    for i in ids:
        p = CORPUS / f"{i}.jpg"
        t0 = time.time()
        r = model.predict(str(p), conf=CONF, verbose=False)[0]
        dt = time.time() - t0
        tags = {}
        for b in r.boxes:
            cls = r.names[int(b.cls[0])]
            conf = float(b.conf[0])
            tags[cls] = max(tags.get(cls, 0.0), conf)
        tag_list = sorted(tags.items(), key=lambda kv: -kv[1])
        results[i] = {
            "tags": [{"class": c, "conf": round(v, 3)} for c, v in tag_list],
            "n_boxes": len(r.boxes),
            "wall_s": round(dt, 3),
        }
        print(i, "->", [f"{c}:{v:.2f}" for c, v in tag_list], f"({dt:.2f}s)")
    total = time.time() - t_all0
    OUT.write_text(json.dumps({
        "model": MODEL_NAME,
        "conf_threshold": CONF,
        "vocab": "COCO 80 классов (общий детектор, не обучен под нашу задачу)",
        "n_images": len(ids),
        "total_wall_s": round(total, 2),
        "results": results,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nитого: {len(ids)} снимков за {total:.1f}с, файл {OUT}")


if __name__ == "__main__":
    main()
