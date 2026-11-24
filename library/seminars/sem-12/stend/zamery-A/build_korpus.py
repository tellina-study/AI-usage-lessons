"""Отбор форм FUNSD (testing_data + training_data, 199 форм вместе) + целевые поля
(4-6 на форму) — ДО первого вызова модели.

Веха 1 (issue #351, 2026-11-24): расширение корпуса с 30 форм (одного среза,
testing_data) на программный отбор из ОБОИХ срезов. Старый `SELECTED` был РУЧНЫМ
списком 30 form_id (весь пригодный пул testing_data при пороге >=3 целевых поля, минус
1 равноценная форма для круглого числа). Эта версия отбирает программно, без ручного
списка id.

Порог ОСЛАБЛЕН с >=3 до >=2 целевых полей (решение оркестратора 2026-11-24, вторая
итерация Вехи 1 — первая итерация на >=3 дала только 70 форм, заметно меньше
владельческих "~100"). Это не подгонка под удобный результат: ослабление до >=2 было
НАЗВАНО заранее, структурно, в самом README исходного замера, как ожидаемый рычаг
расширения — "расширение требовало бы либо снижения порога (>=2 поля, менее
содержательные формы), либо training_data" (README, "Почему 30, а не больше"). Порог
применён СТРУКТУРНО, по числу полей, до единого просмотра качества ответа модели — тем
же способом, что и порог >=3 раньше.
"""
import json
from collections import Counter

from korpus_vyborka import main as scan

_ALL_ROWS = scan()  # оба среза (testing_data + training_data), 199 строк, с полем "split"
_ROWS_BY_ID = {r["form_id"]: r for r in _ALL_ROWS}

# --- Ядро: тот же порог, что был в оригинале (>=3 целевых поля) — все формы отсюда
# входят в выборку первыми, без исключений (там же лежат все 30 уже оплаченных форм).
CORE_THRESHOLD = 3
CORE = [r for r in _ALL_ROWS if r["n_fields"] >= CORE_THRESHOLD]

# Измерено программно 2026-11-24: 75 форм из 199 проходят порог >=3 целевых поля — 31
# из testing_data (ровно те же 31, что дали исходные 30 — порог не менялся) + 44 из
# training_data. Это МЕНЬШЕ владельческих "~100": training_data несёт другие шаблоны
# документов (служебные записки, R&D-формы — не факсы и табличные отчёты продаж
# testing_data), доля проходящих порог там ниже (44/149=29,5% против 31/50=62% в
# testing_data).
assert len(CORE) == 75, (
    f"ядро (>=3 целевых поля) неожиданного размера ({len(CORE)}, ожидалось 75) — "
    "датасет на диске изменился или порог/классификатор разошлись с README"
)

# --- Добор: "слабый" пул — формы РОВНО с 2 целевыми полями (порог >=2 минус порог >=3,
# т.е. именно пограничная полоса, а не всё подряд) — измерено отдельно: 110 форм проходят
# >=2 (40 testing_data + 70 training_data), из них ровно 35 несут РОВНО 2 поля (та самая
# пограничная полоса, остальные 75 уже в CORE). Добираем до круглого числа 100: нужно
# 100 - 75 = 25 форм из этих 35, по убыванию покрытия (сперва формы с ОБЕИМИ категориями
# представленными, т.е. len(cats)==2, затем с одной), form_id — только чтобы разбить
# ничьи детерминированно. Тот же CAT_PRIORITY-дух: предпочитаем формы с разнообразием
# категорий, не просто первые по алфавиту.
WEAK_BAND = [r for r in _ALL_ROWS if r["n_fields"] == 2]
assert len(WEAK_BAND) == 35, (
    f"пограничная полоса (==2 целевых поля) неожиданного размера ({len(WEAK_BAND)}, "
    "ожидалось 35) — датасет на диске изменился или порог/классификатор разошлись"
)

TARGET_N = 100
_need_from_weak = TARGET_N - len(CORE)
assert 0 <= _need_from_weak <= len(WEAK_BAND), (
    _need_from_weak, len(WEAK_BAND), "добор не может превышать пограничную полосу"
)
_weak_best_first = sorted(WEAK_BAND, key=lambda r: (-len(r["cats"]), -r["n_fields"], r["form_id"]))
_chosen_weak = _weak_best_first[:_need_from_weak]

SELECTED = sorted([r["form_id"] for r in CORE] + [r["form_id"] for r in _chosen_weak])
assert len(SELECTED) == TARGET_N, len(SELECTED)
assert len(set(SELECTED)) == TARGET_N

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
# Все form_id этих двух словарей принадлежат исходным 30 формам testing_data — они
# ОСТАЛИСЬ в SELECTED (проверено assert'ом ниже): все 30 лежат в CORE (>=3 поля), CORE
# целиком входит в выборку без исключений — записи ниже валидны без изменений.
ADJACENT_PAIRS = {
    "82092117": [("FAX NUMBER:", "PHONE NUMBER:")],
    "83553333_3334": [("Sender Fax Number", "Sender Voice Number"), ("Fax Number", "Recipient Phone Number")],
}
_OLD_30_SELECTED = {
    "83553333_3334", "83573282", "83624198", "82092117", "83443897",
    "83823750", "86220490", "82562350", "83594639",
    "92380595", "83635935", "87528380",
    "86328049_8050", "83641919_1921", "82253362_3364", "86230203_0206",
    "82253245_3247", "82200067_0069", "82252956_2958",
    "82254765", "91814768_91814769", "93106788",
    "82250337_0338", "82253058_3059", "82491256", "82573104",
    "87125460", "86263525", "87528321",
    "87594142_87594144",
}
assert len(_OLD_30_SELECTED) == 30
assert _OLD_30_SELECTED.issubset(set(SELECTED)), (
    "старые 30 форм (уже с реальными платными вызовами в raw/vision_results.json / "
    "raw/hybrid_results.json) должны остаться в новой выборке целиком — отброшены: "
    f"{_OLD_30_SELECTED - set(SELECTED)}"
)

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

# Старые по-категорийные итоги (README, 143 поля после правок эталона): имя=65,
# дата=34, телефон=25, число=19 — должны быть сохранены/увеличены (задание Вехи 1 §2).
_OLD_CAT_TOTALS = {"name": 65, "date": 34, "phone": 25, "count": 19}

def main():
    rows = _ROWS_BY_ID
    out = []
    cat_totals = Counter()
    for fid in SELECTED:
        r = rows[fid]
        targets = pick_targets(r["fields"], cap=6)
        tf = []
        for f in targets:
            cat_totals[f["cat"]] += 1
            hard_reason = HARD_FIELDS.get((fid, f["q_text"].strip().rstrip(":").strip() + (":" if f["q_text"].strip().endswith(":") else "")))
            # точное совпадение по исходному q_text тоже пробуем
            hard_reason = hard_reason or HARD_FIELDS.get((fid, f["q_text"]))
            tf.append({
                "q_text": f["q_text"], "a_text": f["a_text"], "cat": f["cat"],
                "edge": f["edge"], "hard_reason": hard_reason,
            })
        out.append({
            "form_id": fid,
            "split": r["split"],
            "img": f"{fid}.png",
            "img_w": r["w"], "img_h": r["h"],
            "cats_available": r["cats"],
            "n_fields_available": r["n_fields"],
            "targets": tf,
            "adjacent_pairs": ADJACENT_PAIRS.get(fid, []),
        })
    total_targets = sum(len(o["targets"]) for o in out)
    by_split = Counter(o["split"] for o in out)
    print(f"{len(out)} форм ({dict(by_split)}), {total_targets} целевых полей, "
          f"{sum(1 for o in out for t in o['targets'] if t['hard_reason'])} трудных помеченных глазами")
    print(f"по категориям: {dict(cat_totals)}")

    # Проверка §2 задания Вехи 1: каждая категория >= старого итога (65/34/25/19).
    for cat, old in _OLD_CAT_TOTALS.items():
        new = cat_totals.get(cat, 0)
        assert new >= old, (
            f"категория '{cat}' упала ниже старого итога после расширения корпуса: "
            f"{new} < {old} — отбор форм нужно скорректировать (приоритизировать формы "
            f"этой категории), это НЕ допускается молча"
        )

    with open("korpus/vyborka.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
