"""Один vision-вызов на уникальный кадр корпуса Кейса C — модель gpt-4o-mini через
вебхук стенда s10-raw-openrouter (харнесс Семинара 10, переиспользован без изменений,
см. README). Промт цитирует определения владельца у1'/е1/с1 ДОСЛОВНО и просит три флага
разом — экономично (один вызов отвечает на три класса) и соответствует С5 канона (модель
и её настройки названы). Результаты дописываются построчно в raw/vision_results.jsonl —
скрипт резюмируем (пропускает уже обработанные id).
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from harness2_lite import vision_call, to_data_url, extract_json
from corpus import all_unique_images

OUT = Path(__file__).parent / "raw" / "vision_results.jsonl"
OUT.parent.mkdir(exist_ok=True)

SYSTEM_PROMPT = """Ты инструмент премодерации фотоархива мероприятий учебного центра перед публикацией.
Проверь кадр по трём определениям дословно и ответь СТРОГО JSON без markdown-ограждения:
{"smoking": true|false, "food_drink": true|false, "screen_present": true|false}

Определения:
1. "smoking" — курение (у1'): в кадре либо человек курит: сигарета, вейп или трубка,
   зажжённая, во рту или в руке; либо присутствует изображение курения — плакат, реклама
   на стене, кадр на экране.
2. "food_drink" — еда и напитки (е1): человек ест или пьёт, либо накрытый стол как
   главный сюжет кадра. Еда/напитки на краю кадра без активного действия человека —
   false.
3. "screen_present" — экран (ступень 1 класса "слайды", с1 без сверки "наш ли материал"):
   в кадре читаемый экран, проектор или крупная проекция (не вопрос о содержимом,
   только о присутствии такого объекта в кадре)."""


def already_done():
    done = set()
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            try:
                d = json.loads(line)
                done.add((d["dir"], d["id"]))
            except Exception:
                pass
    return done


def main():
    items = all_unique_images()
    done = already_done()
    todo = [(d, i) for d, i in items if (d, i) not in done]
    print(f"total={len(items)} done={len(done)} todo={len(todo)}", flush=True)
    for n, (d, i) in enumerate(todo):
        path = f"{d}/{i}.jpg"
        try:
            img = to_data_url(path, w=512)
            r = vision_call(SYSTEM_PROMPT, "Проверь кадр по трём флагам.", img)
            parsed = extract_json(r["content"])
            rec = {"dir": d, "id": i, "parsed": parsed, "raw": r["content"],
                   "cost": r.get("cost"), "wall_s": r.get("wall_s"),
                   "prompt_tokens": r.get("prompt_tokens"), "error": r.get("raw_error")}
        except Exception as e:
            rec = {"dir": d, "id": i, "parsed": None, "raw": None, "error": str(e)}
        with OUT.open("a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        if n % 10 == 0:
            print(f"{n+1}/{len(todo)} {d.split('/')[-1]}/{i} -> {rec['parsed']}", flush=True)
        time.sleep(0.2)
    print("done.", flush=True)


if __name__ == "__main__":
    main()
