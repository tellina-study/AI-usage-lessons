"""Общий детектор `yolov8n` (ultralytics, словарь COCO-80), локально, без сети.
Модель и настройки (С5 канона): yolov8n.pt, conf=0.25 (дефолт ultralytics), 640px вход.
Для класса "курение" словаря нет вовсе (ожидаемый структурный ноль — результат, не
отказ замера). Для "еда/напитки" — словарь COCO покрывает часть сюжета (sandwich,
hot dog, wine glass, cup, bottle, dining table...). Для "слайды" ступени 1 — класс
`tv` (покрывает и мониторы, и проекционные экраны в разметке COCO)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus import all_unique_images

from ultralytics import YOLO

MODEL_PATH = "/tmp/s12-corpora/yolov8n.pt"
CONF = 0.25

FOOD_CLASSES = {"banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog",
                "pizza", "donut", "cake", "bottle", "wine glass", "cup", "bowl",
                "dining table", "fork", "knife", "spoon"}
SMOKE_CLASSES = set()  # нет в COCO-80 — структурный ноль
SCREEN_CLASSES = {"tv", "laptop"}

OUT = Path(__file__).parent / "raw" / "yolo_results.jsonl"
OUT.parent.mkdir(exist_ok=True)


def main():
    model = YOLO(MODEL_PATH)
    items = all_unique_images()
    print(f"running yolov8n on {len(items)} images, conf={CONF}", flush=True)
    with OUT.open("w") as f:
        for n, (d, i) in enumerate(items):
            path = f"{d}/{i}.jpg"
            res = model.predict(path, conf=CONF, verbose=False)[0]
            dets = []
            for box in res.boxes:
                cls_name = model.names[int(box.cls[0])]
                dets.append({"cls": cls_name, "conf": round(float(box.conf[0]), 4)})
            rec = {
                "dir": d, "id": i, "detections": dets,
                "food_hit": any(x["cls"] in FOOD_CLASSES for x in dets),
                "food_best": max([x["conf"] for x in dets if x["cls"] in FOOD_CLASSES], default=None),
                "smoke_hit": any(x["cls"] in SMOKE_CLASSES for x in dets),
                "screen_hit": any(x["cls"] in SCREEN_CLASSES for x in dets),
                "screen_best": max([x["conf"] for x in dets if x["cls"] in SCREEN_CLASSES], default=None),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            if n % 40 == 0:
                print(f"{n+1}/{len(items)}", flush=True)
    print("done.", flush=True)


if __name__ == "__main__":
    main()
