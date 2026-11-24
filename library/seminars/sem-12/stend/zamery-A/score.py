#!/usr/bin/env python3
"""Сведение трёх прогонов (vision / OCR+правила / гибрид) против GT.

Нормализация сравнения — одна для всех трёх вариантов (не подбирается под один из
них): нижний регистр; дефисы/скобки заменены пробелом; пробелы схлопнуты и обрезаны
по краям. Точное совпадение нормализованных строк — единственный автоматический
вердикт «верно».

Сопоставление внутри формы — МНОЖЕСТВОМ, но только там, где подпись поля БУКВАЛЬНО
повторяется (несколько «NAME OF ACCOUNT» в таблице, две разных «DATE» на одном
бланке, две «PHONE:») — промт называет модели только текст подписи, без координат на
странице, так что нет основания требовать угадать, какой физический экземпляр подписи
имелся в виду под каким нумерованным field_i. Группировка — по (форма, ТОЧНЫЙ ТЕКСТ
ПОДПИСИ q_text), НЕ по широкой категории (name/phone/date/count). Первая версия этого
файла группировала по категории и из-за этого засчитывала «верно» для поля «Tel», когда
совпадение находилось на самом деле у соседнего «PHONE:» того же бланка — у «Tel» и
«PHONE:» РАЗНЫЙ текст подписи, и это не та неоднозначность, которую стоило прощать:
модель в принципе могла их различить. Поправлено до публикации чисел (не было
опубликовано иначе) — см. README «Проверка группировки». Для каждой такой группы
перебираются перестановки (группы ≤5 элементов, см. build_korpus.py), это применено
ОДИНАКОВО ко всем трём методам, включая OCR+правила.

Что поправлено чтением отказов глазами ПОСЛЕ первого прогона (канон §8.12 — число
грейдера не публикуется без этого чтения; правки названы, а не скрыты):

  1. 83553333_3334 — подпись «Date» в разметке FUNSD связана с ДВУМЯ сущностями
     ответа («November» и «1999», qid=1 исходной разметки) — это одно значение,
     разбитое разметчиком датасета на два текстовых блока, не два поля. Оба
     предсказания (field_3, field_5 в уже отправленном промте) объединяются в одно
     и сравниваются с объединённым эталоном «November 1999».
  2. 82254765, поле «DATE FORWARDED TO PROMOTION SERVICES:» — эталон FUNSD хранит
     «zbulan» (не дата). Прямой просмотр скана показывает рукописную дату вида
     «2/6/97» — сломан сам эталон разметки (ошибка краудсорс-разметки датасета, не
     наша). Поле ИСКЛЮЧЕНО из подсчёта точности для всех трёх методов — сравнение с
     испорченным эталоном не может быть ни «верно», ни «неверно».

Обе правки найдены на числах варианта «мультимодальная модель» (там, где они были видны
первыми) и применены РОВНО ОДИНАКОВО к vision/hybrid/ocr_rules — поправка эталона,
а не метода.
"""
import itertools
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Веха 2 (issue #351, корпус 30->100 форм) — систематическая проверка правдоподобия
# повторена на ВСЕХ 369 целевых полях (не только старых 145). Найден ОДИН новый
# подтверждённый дефект эталона, того же типа, что уже есть ниже (вопрос связан не с
# ответом, а с текстом чужой метки): 71341634, вопрос «Date» (их на форме ДВА с
# одинаковым текстом подписи) — второй связан разметкой FUNSD с текстом «Check#», это
# метка СОСЕДНЕЙ ячейки таблицы «Verification» («Date | Vendor # | Account Month» /
# «Check # | Check Date | Pay Handling»), не ответ на вопрос «Date» вообще. Подтверждено
# прямым просмотром скана и разметки (d['form']: Q=28 'Date', linking=[[28,30]], A=30
# 'Check#'). Ключ расширен до (форма, текст подписи, ТЕКСТ ОТВЕТА), чтобы не исключить
# заодно первый, корректный вопрос «Date» той же формы (у него a_text='03/ 24/ 99') —
# старая запись ниже однозначна и так (её q_text уникален на своей форме), добавление
# a_text в ключ её не меняет.
GT_EXCLUDE = {
    ("82254765", "DATE FORWARDED TO PROMOTION SERVICES:", "zbulan"),
    ("71341634", "Date", "Check#"),
}


def normalize(s):
    """Регистр, пробелы, дефисы — и вообще ЛЮБАЯ пунктуация убраны целиком, остаются
    только буквы и цифры. Это шире минимума плана («пробелы, регистр, дефисы») —
    расширено по чтению отказов глазами (две находки, обе проверены на ВСЕХ трёх
    методах разом, не только там, где это улучшало удобный вариант):
      — OCR систематически склеивает соседние слова без пробела («MikeMozina»,
        «Mr.Randy Spell»), и схлопывание пробелов до одного этого не чинит;
      — модель иногда добавляет/убирает хвостовую пунктуацию, не меняя значения
        («(212) 935-6801.» против «(212) 935 6801» — лишняя точка на конце).
    Риск этого расширения — он же и назван: при очень коротких значениях (разовая
    цифра, двухбуквенный код) полное снятие пунктуации может случайно сблизить два
    РАЗНЫХ значения. На этом корпусе руками проверены все поля короче 3 знаков после
    нормализации (список — README «Проверка коротких значений») — ложных совпадений
    не найдено."""
    if s is None:
        return ""
    s = str(s).lower()
    return re.sub(r"[^0-9a-zа-яё]", "", s)


def best_matching(preds, gts):
    """preds, gts — списки одинаковой длины. Возвращает число точных совпадений при
    ЛУЧШЕМ сопоставлении (перебор перестановок) + саму перестановку индексов gts."""
    n = len(preds)
    if n == 0:
        return 0, []
    npreds = [normalize(p) for p in preds]
    ngts = [normalize(g) for g in gts]
    best = -1
    best_perm = list(range(n))
    for perm in itertools.permutations(range(n)):
        score = sum(1 for i in range(n) if npreds[i] and npreds[i] == ngts[perm[i]])
        if score > best:
            best = score
            best_perm = perm
    return best, best_perm


def load_targets_with_field_index(corpus):
    """Для каждой формы — список (field_key, q_text, cat, a_text, hard_reason), в
    том порядке, в каком targets шли в build_user_prompt (field_1..field_N) — ЭТОТ
    порядок уже зафиксирован в отправленных промтах, менять нельзя."""
    out = {}
    for form in corpus:
        fid = form["form_id"]
        items = []
        for i, t in enumerate(form["targets"], 1):
            if (fid, t["q_text"], t["a_text"]) in GT_EXCLUDE:
                continue
            items.append({"field_key": f"field_{i}", "q_text": t["q_text"], "cat": t["cat"],
                          "a_text": t["a_text"], "hard_reason": t["hard_reason"]})
        out[fid] = items
    return out


def apply_date_split_merge(fid, items, pred_by_key):
    """83553333_3334: field_3 (Date->November) + field_5 (Date->1999) -> одно поле."""
    if fid != "83553333_3334":
        return items, pred_by_key
    keys = [it["field_key"] for it in items if it["q_text"] == "Date"]
    if set(keys) != {"field_3", "field_5"}:
        return items, pred_by_key  # защита: структура не та, что ожидали — не трогаем
    merged_pred = " ".join(
        p for p in (pred_by_key.get("field_3"), pred_by_key.get("field_5")) if p
    ) or None
    new_items = [it for it in items if it["q_text"] != "Date"]
    new_items.append({"field_key": "field_3+5", "q_text": "Date", "cat": "date",
                       "a_text": "November 1999", "hard_reason": None})
    new_pred = dict(pred_by_key)
    new_pred["field_3+5"] = merged_pred
    return new_items, new_pred


def apply_date_split_merge_2(fid, items, pred_by_key):
    """Веха 2 находка — тот же класс дефекта, что apply_date_split_merge выше (одно
    значение даты разметчик FUNSD разбил на несколько ответных текстовых блоков одного
    вопроса), новый конкретный случай: 92091873, вопрос «Date» (их на форме ТРИ с
    одинаковым текстом подписи — не путать с «Date (s)» и «Date Submitted», это другие
    вопросы) связан разметкой с ТРЕМЯ ответами: '6/', '12/', '95'. Прямой просмотр скана:
    строка «Date Rec'd   6/12/95» — одна дата, разбитая по символу «/» на три отдельных
    OCR-бокса в исходной разметке датасета (аннотация: Q=12 'Date', linking=[[12,35],
    [12,36],[12,37]], box-порядок слева направо совпадает с порядком field_1/2/3 в уже
    отправленных промтах — '6/'+'12/'+'95' => «6/12/95», ровно как на скане)."""
    if fid != "92091873":
        return items, pred_by_key
    keys = [it["field_key"] for it in items if it["q_text"] == "Date"]
    if set(keys) != {"field_1", "field_2", "field_3"}:
        return items, pred_by_key  # защита: структура не та, что ожидали — не трогаем
    merged_pred = " ".join(
        p for p in (pred_by_key.get("field_1"), pred_by_key.get("field_2"),
                    pred_by_key.get("field_3")) if p
    ) or None
    new_items = [it for it in items if it["q_text"] != "Date"]
    new_items.append({"field_key": "field_1+2+3", "q_text": "Date", "cat": "date",
                       "a_text": "6/ 12/ 95", "hard_reason": None})
    new_pred = dict(pred_by_key)
    new_pred["field_1+2+3"] = merged_pred
    return new_items, new_pred


def score_method(corpus, targets_by_form, get_pred_by_key, method_label):
    rows = []
    for form in corpus:
        fid = form["form_id"]
        items = targets_by_form[fid]
        pred_by_key = get_pred_by_key(fid, items)
        items, pred_by_key = apply_date_split_merge(fid, items, pred_by_key)
        items, pred_by_key = apply_date_split_merge_2(fid, items, pred_by_key)
        by_label = {}
        for it in items:
            by_label.setdefault(it["q_text"], []).append(it)
        for q_text, its in by_label.items():
            cat = its[0]["cat"]
            preds = [pred_by_key.get(it["field_key"]) for it in its]
            gts = [it["a_text"] for it in its]
            n_exact, perm = best_matching(preds, gts)
            matched_exact = [False] * len(its)
            npreds = [normalize(p) for p in preds]
            ngts = [normalize(g) for g in gts]
            for i in range(len(its)):
                if npreds[i] and npreds[i] == ngts[perm[i]]:
                    matched_exact[i] = True
            for i, it in enumerate(its):
                rows.append({
                    "method": method_label, "form_id": fid, "q_text": it["q_text"],
                    "cat": cat, "gt": it["a_text"], "pred": preds[i],
                    "exact": matched_exact[i], "hard_reason": it["hard_reason"],
                    "group_size": len(its),
                })
    return rows


def main():
    corpus = json.load(open(HERE / "korpus" / "vyborka.json"))
    vision = json.load(open(HERE / "raw" / "vision_results.json"))["per_form"]
    hybrid = json.load(open(HERE / "raw" / "hybrid_results.json"))["per_form"]
    rules = json.load(open(HERE / "raw" / "rules_extraction.json"))

    targets_by_form = load_targets_with_field_index(corpus)

    def vision_pred(fid, items):
        parsed = (vision.get(fid) or {}).get("parsed")
        if not isinstance(parsed, dict):
            return {}
        return {it["field_key"]: parsed.get(it["field_key"]) for it in items}

    def hybrid_pred(fid, items):
        parsed = (hybrid.get(fid) or {}).get("parsed")
        if not isinstance(parsed, dict):
            return {}
        return {it["field_key"]: parsed.get(it["field_key"]) for it in items}

    def rules_pred(fid, items):
        extracted = rules.get(fid, {})
        cursor = {}
        out = {}
        for it in items:
            cat = it["cat"]
            idx = cursor.get(cat, 0)
            vals = extracted.get(cat, [])
            out[it["field_key"]] = vals[idx] if idx < len(vals) else None
            cursor[cat] = idx + 1
        return out

    rows_vision = score_method(corpus, targets_by_form, vision_pred, "vision")
    rows_hybrid = score_method(corpus, targets_by_form, hybrid_pred, "hybrid")
    rows_rules = score_method(corpus, targets_by_form, rules_pred, "ocr_rules")

    for rows, title in [(rows_vision, "Мультимодальная модель"),
                         (rows_hybrid, "Гибрид (OCR-текст -> gpt-4o-mini)"),
                         (rows_rules, "OCR + правила")]:
        print(f"\n=== {title}: {len(rows)} полей (после исключения GT-брака и склейки) ===")
        exact = sum(r["exact"] for r in rows)
        print(f"точных совпадений: {exact}/{len(rows)} = {exact/len(rows):.3f}")
        by_cat = {}
        for r in rows:
            by_cat.setdefault(r["cat"], []).append(r)
        for cat, rs in sorted(by_cat.items()):
            e = sum(x["exact"] for x in rs)
            print(f"  {cat}: {e}/{len(rs)} = {e/len(rs):.3f}")
        hard = [r for r in rows if r["hard_reason"]]
        if hard:
            e = sum(x["exact"] for x in hard)
            print(f"  [трудные помеченные]: {e}/{len(hard)} = {e/len(hard):.3f}")
        easy = [r for r in rows if not r["hard_reason"]]
        e = sum(x["exact"] for x in easy)
        print(f"  [остальные]: {e}/{len(easy)} = {e/len(easy):.3f}")

    all_rows = rows_vision + rows_hybrid + rows_rules
    with open(HERE / "raw" / "scored_all.json", "w", encoding="utf-8") as fh:
        json.dump(all_rows, fh, ensure_ascii=False, indent=2)
    print(f"\nвсего строк сведения: {len(all_rows)} -> raw/scored_all.json")

    # --- Требование оркестратора по Вехе A1: разделить промахи гибрида на два
    # разных по природе класса — поломка разбора ответа (вся форма разом) против
    # содержательной ошибки чтения (поле за полем). ---
    print("\n=== Гибрид: природа промахов (поломка формата vs содержание) ===")
    broken_forms = {fid for fid, v in hybrid.items() if v.get("parsed") is None}
    misses = [r for r in rows_hybrid if not r["exact"]]
    broken_misses = [r for r in misses if r["form_id"] in broken_forms]
    content_misses = [r for r in misses if r["form_id"] not in broken_forms]
    print(f"всего промахов: {len(misses)}")
    print(f"  из-за сломанного JSON (вся форма разом, {len(broken_forms)} форма): "
          f"{len(broken_misses)} ({len(broken_misses)/len(misses):.1%})")
    print(f"  содержательных (OCR потерял/исказил, поле за полем): "
          f"{len(content_misses)} ({len(content_misses)/len(misses):.1%})")
    null_count = sum(1 for r in content_misses if r["pred"] is None)
    print(f"    из них пусто (честное «не нашла»): {null_count}")
    print(f"    из них неверное значение (уверенно, но не то): {len(content_misses)-null_count}")

    # --- Требование оркестратора: число дефектов эталона FUNSD с базой, сопоставимое
    # с «3 из 60 (5,0%)» у соседнего кейса (человеческая разметка Open Images). Только
    # ГЕНУИННЫЕ дефекты самого эталона (не баг нашего кода подсчёта) — найдены
    # систематической проверкой правдоподобия (должна быть цифра в date/phone/count)
    # по всем 145 полям ДО склейки/исключения, подтверждены прямым просмотром скана. ---
    n_total_fields = sum(len(f["targets"]) for f in corpus)
    print("\n=== Дефекты эталона FUNSD, найденные систематической проверкой правдоподобия ===")
    print(f"база: {n_total_fields} целевых полей (до склейки/исключения), n=100 форм, Веха 2")
    print("систематическая проверка (цифра обязательна в date/count, >=5 цифр в phone)"
          " нашла 19 кандидатов (369 полей) — каждый проверен прямым просмотром скана:")
    print("подтверждённые дефекты эталона: 4 (4/369 = 1,1%)")
    print("  1) 82254765 «DATE FORWARDED TO PROMOTION SERVICES:» — эталон «zbulan»,"
          " скан показывает рукописную дату (~2/6/97) [старое, корпус 30, исключено]")
    print("  2) 83553333_3334 «Date» — одно значение разметчик разбил на два"
          " ответных блока («November» + «1999») [старое, корпус 30, склеено]")
    print("  3) 92091873 «Date» — одно значение «6/12/95» разметчик разбил на ТРИ"
          " ответных блока («6/» + «12/» + «95») [новое, Веха 2, корпус 100, склеено]")
    print("  4) 71341634 «Date» (второй вопрос с тем же текстом подписи на форме) —"
          " разметка связала его с «Check#», меткой соседней ячейки таблицы"
          " Verification, а не с ответом [новое, Веха 2, корпус 100, исключено]")
    print("НЕ считаются дефектом эталона (это наша ошибка категоризации ИЛИ не-дефект,"
          " полный список и обоснование — в отчёте Вехи 2, не только здесь):"
          " 86220490 FAX=«Autodial» [старое], 87594142_87594144 Kleeberger [старое],"
          " плюс 14 новых кандидатов из 70 добавленных форм (composite-поля,"
          " легитимные нечисловые значения «N/A»/«Unk.»/«As required»/«One», короткие"
          " внутренние добавочные номера, баг классификатора на «Motel»/«Phone Booth»)")
    print("НЕ считается дефектом эталона (это баг НАШЕГО кода подсчёта, не датасета):"
          " группировка полей по широкой категории вместо точного текста подписи"
          " (исправлено до публикации итоговых чисел)")


if __name__ == "__main__":
    main()
