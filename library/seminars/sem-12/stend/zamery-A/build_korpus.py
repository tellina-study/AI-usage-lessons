"""Отбор 30 форм FUNSD testing_data + целевые поля (4-6 на форму) — ДО первого вызова модели."""
import json, os
from korpus_vyborka import main as scan

SELECTED = [
    # (4 категории, n_fields>=4) — 9 форм
    "83553333_3334", "83573282", "83624198", "82092117", "83443897",
    "83823750", "86220490", "82562350", "83594639",
    # (3 категории) — 3 формы
    "92380595", "83635935", "87528380",
    # (count+name, табличные формы отчётов по продажам) — 7 форм
    "86328049_8050", "83641919_1921", "82253362_3364", "86230203_0206",
    "82253245_3247", "82200067_0069", "82252956_2958",
    # (date+name, 4-5 полей) — 3 формы
    "82254765", "91814768_91814769", "93106788",
    # (date+name, 3 поля) — 4 формы (из 5 кандидатов отброшена 83772145 — равноценная,
    # держим круглое число 30)
    "82250337_0338", "82253058_3059", "82491256", "82573104",
    # (1 категория date, >=3 поля) — 3 формы
    "87125460", "86263525", "87528321",
    # (1 категория phone, 3 поля) — 1 форма
    "87594142_87594144",
]
assert len(SELECTED) == 30, len(SELECTED)
assert len(set(SELECTED)) == 30

# Известные трудные случаи, найденные ГЛАЗАМИ до прогона (не по ответу модели):
HARD_FIELDS = {
    ("92380595", "ATTN:"): "рукописное: типографский бланк, а имя получателя дописано от руки поверх напечатанного",
    ("92380595", "Date Received:"): "рукописное + у края кадра (нижняя строка штампа получения)",
    ("83624198", "Tel"): "поле у края кадра (нижняя строка бланка)",
    ("83624198", "Fax"): "поле у края кадра (нижняя строка бланка)",
    ("83823750", "Fax Number"): "визуально двусмысленная цифра (исправление/наложение в факсе — 910-335-7077 читается похоже на 7877/7017)",
    ("82254765", "DATE FORWARDED TO PROMOTION SERVICES:"): "полностью рукописное, от руки вписанная дата (найдено ПОСЛЕ первого прогона чтением отказов глазами — см. score.py::GT_EXCLUDE и README «Что поправлено по чтению глазами»: эталон этого поля в разметке FUNSD испорчен)",
}
# Две находки по чтению ПЕРВОГО прогона глазами (С9.12 канона) живут и применяются в
# score.py (GT_MERGE_DATE_SPLIT / GT_EXCLUDE), не здесь — отбор полей (эта функция)
# уже был зафиксирован и использован для реальных вызовов моделей ДО того, как эти две
# находки обнаружились; трогать состав/порядок targets здесь означало бы разойтись с
# полями field_1..field_N, которые реально стояли в уже отправленных промтах.
# Пары «похожих полей рядом» (критерий трудного случая (в) плана) — не вырезаются как
# отдельные targets, а используются для подписи на кадре.
ADJACENT_PAIRS = {
    "82092117": [("FAX NUMBER:", "PHONE NUMBER:")],
    "83553333_3334": [("Sender Fax Number", "Sender Voice Number"), ("Fax Number", "Recipient Phone Number")],
}

CAT_PRIORITY = ["name", "phone", "date", "count"]

def pick_targets(fields, cap=6):
    # приоритет: по одному полю каждой доступной категории первым проходом,
    # затем добираем до cap, предпочитая разнообразие вопросов (без дублей q_text+a_text)
    seen = set()
    chosen = []
    by_cat = {}
    for f in fields:
        by_cat.setdefault(f["cat"], []).append(f)
    for cat in CAT_PRIORITY:
        lst = by_cat.get(cat, [])
        if lst:
            f = lst[0]
            key = (f["q_text"], f["a_text"])
            if key not in seen:
                seen.add(key)
                chosen.append(f)
    for f in fields:
        if len(chosen) >= cap:
            break
        key = (f["q_text"], f["a_text"])
        if key in seen:
            continue
        seen.add(key)
        chosen.append(f)
    return chosen[:cap]

def main():
    rows = {r["form_id"]: r for r in scan()}
    out = []
    for fid in SELECTED:
        r = rows[fid]
        targets = pick_targets(r["fields"], cap=6)
        tf = []
        for f in targets:
            hard_reason = HARD_FIELDS.get((fid, f["q_text"].strip().rstrip(":").strip() + (":" if f["q_text"].strip().endswith(":") else "")))
            # точное совпадение по исходному q_text тоже пробуем
            hard_reason = hard_reason or HARD_FIELDS.get((fid, f["q_text"]))
            tf.append({
                "q_text": f["q_text"], "a_text": f["a_text"], "cat": f["cat"],
                "edge": f["edge"], "hard_reason": hard_reason,
            })
        out.append({
            "form_id": fid,
            "img": f"{fid}.png",
            "img_w": r["w"], "img_h": r["h"],
            "cats_available": r["cats"],
            "n_fields_available": r["n_fields"],
            "targets": tf,
            "adjacent_pairs": ADJACENT_PAIRS.get(fid, []),
        })
    total_targets = sum(len(o["targets"]) for o in out)
    print(f"{len(out)} форм, {total_targets} целевых полей, "
          f"{sum(1 for o in out for t in o['targets'] if t['hard_reason'])} трудных помеченных глазами")
    with open("korpus/vyborka.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
