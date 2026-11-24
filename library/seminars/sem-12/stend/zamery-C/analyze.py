"""Свод замера C1: пропуски/ложные тревоги раздельно по трём классам и трём методам,
полоса неопределённости SigLIP (К4-методика, мерена заново на этом корпусе), база для
каждого числа. Печатает таблицы в markdown — вставляются в README.md руками один раз,
дальше README — источник правды для кадров (не пересчитывается на лету слайдами)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from corpus import (SMOKE_POS, SMOKE_NEG, SMOKE_DISPUTED, SMOKE_VALTEST_HARDNEG,
                     SMOKE_TRAIN_HARDNEG, SMOKE_GENERAL_NEG, SMOKE_VALTEST_POS,
                     SMOKE_TRAIN_POS_SCENE, SMOKE_TRAIN_POS_IMAGE,
                     FOOD_POS_FULL, FOOD_NEG, FOOD_ANIMAL_NEG, FOOD_B_NEG,
                     FOOD_MINOR_EXCLUDED, FOOD_DISPUTED,
                     SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT, SLIDES_READABLE, SLIDES_BLANK,
                     SLIDES_HARDNEG, SLIDES_GENERAL_NEG_NEW,
                     SMOKE_VALTEST_DIR, SMOKE_TRAIN_DIR)

HERE = Path(__file__).parent
RAW = HERE / "raw"


def load_jsonl(p):
    return {(d["dir"], d["id"]): d for d in (json.loads(l) for l in open(p))}


vision = load_jsonl(RAW / "vision_results.jsonl")
yolo = load_jsonl(RAW / "yolo_results.jsonl")
siglip = load_jsonl(RAW / "siglip_results.jsonl")


def confusion(pos_keys, neg_keys, predicate):
    tp = sum(1 for k in pos_keys if predicate(k))
    fn = len(pos_keys) - tp
    fp = sum(1 for k in neg_keys if predicate(k))
    tn = len(neg_keys) - fp
    return {"tp": tp, "fn": fn, "fp": fp, "tn": tn,
            "miss_rate": round(fn / len(pos_keys), 3) if pos_keys else None,
            "false_alarm_rate": round(fp / len(neg_keys), 3) if neg_keys else None}


def pct(a, b):
    return f"{a}/{b} ({round(100*a/b,1)}%)" if b else "n/a"


print("=" * 70)
print("СЧЁТ ГРЯЗИ (человеческая пометка Open Images vs бизнес-вопрос у1'/е1)")
print("=" * 70)
vt_total = len(SMOKE_VALTEST_HARDNEG) + len(SMOKE_VALTEST_POS) + 1  # +1 disputed(df84409)
tr_total = len(SMOKE_TRAIN_HARDNEG) + len(SMOKE_TRAIN_POS_SCENE) + len(SMOKE_TRAIN_POS_IMAGE) + 6 + 1
print(f"курение val/test (пул 'Cigarette', человеком подтверждён): строго неверно "
      f"{pct(len(SMOKE_VALTEST_HARDNEG), vt_total)} — предмет без человека")
print(f"курение train-добор: строго неверно {pct(len(SMOKE_TRAIN_HARDNEG), tr_total)}")
smoke_total_reviewed = vt_total + tr_total
smoke_total_hardneg = len(SMOKE_VALTEST_HARDNEG) + len(SMOKE_TRAIN_HARDNEG)
print(f"курение ОБЪЕДИНЁННО: строго неверно {pct(smoke_total_hardneg, smoke_total_reviewed)}, "
      f"спорно {pct(len(SMOKE_DISPUTED), smoke_total_reviewed)}")
food_total = len(FOOD_POS_FULL) + len(FOOD_ANIMAL_NEG) + len(FOOD_MINOR_EXCLUDED) + len(FOOD_DISPUTED)
print(f"еда/напитки: животное вместо человека {pct(len(FOOD_ANIMAL_NEG), len(FOOD_POS_FULL)+len(FOOD_ANIMAL_NEG))} "
      f"из позитивно-помеченного пула 'Eating'/'Drinking' (всего просмотрено {food_total}: "
      f"позитив {len(FOOD_POS_FULL)}, несовершеннолетние исключены {len(FOOD_MINOR_EXCLUDED)}, "
      f"спорно {len(FOOD_DISPUTED)})")

print()
print("=" * 70)
print("КЛАСС: КУРЕНИЕ (у1') — позитив n=%d, негатив n=%d" % (len(SMOKE_POS), len(SMOKE_NEG)))
print("=" * 70)

conf_yolo = confusion(SMOKE_POS, SMOKE_NEG, lambda k: yolo.get(k, {}).get("smoke_hit", False))
print("YOLO (нет класса в словаре COCO-80):", conf_yolo)

conf_vision = confusion(SMOKE_POS, SMOKE_NEG,
                         lambda k: (vision.get(k, {}).get("parsed") or {}).get("smoking", False))
print("Vision (gpt-4o-mini, промт у1' дословно):", conf_vision)

for thr in [0.3, 0.5, 0.7]:
    conf_sig = confusion(SMOKE_POS, SMOKE_NEG,
                          lambda k, t=thr: siglip.get(k, {}).get("smoking_en_pos", 0) >= t)
    print(f"SigLIP EN @ порог {thr}:", conf_sig)

conf_sig_ru = confusion(SMOKE_POS, SMOKE_NEG,
                         lambda k: siglip.get(k, {}).get("smoking_ru_pos", 0) >= 0.5)
print("SigLIP RU @ порог 0.5:", conf_sig_ru)

print()
print("=" * 70)
print("КЛАСС: ЕДА И НАПИТКИ (е1) — позитив n=%d, негатив n=%d" % (len(FOOD_POS_FULL), len(FOOD_NEG)))
print("=" * 70)

conf_yolo_f = confusion(FOOD_POS_FULL, FOOD_NEG, lambda k: yolo.get(k, {}).get("food_hit", False))
print("YOLO (словарь COCO покрывает часть сюжета):", conf_yolo_f)

conf_vision_f = confusion(FOOD_POS_FULL, FOOD_NEG,
                           lambda k: (vision.get(k, {}).get("parsed") or {}).get("food_drink", False))
print("Vision:", conf_vision_f)
# отдельно: сколько ложных тревог vision на ЖИВОТНЫХ негативах конкретно (находка кейса B)
animal_keys = [(SMOKE_VALTEST_DIR if False else None, i) for i in []]
from corpus import FOOD_DIR
animal_fp = sum(1 for i in FOOD_ANIMAL_NEG
                 if (vision.get((FOOD_DIR, i), {}).get("parsed") or {}).get("food_drink", False))
print(f"  из них на животных-негативах (не порог, а выдумка): {animal_fp}/{len(FOOD_ANIMAL_NEG)}")
b_fp = sum(1 for k in FOOD_B_NEG if (vision.get(k, {}).get("parsed") or {}).get("food_drink", False))
print(f"  из них на B-сценах (люди на мероприятии, не едят): {b_fp}/{len(FOOD_B_NEG)}")

for thr in [0.3, 0.5, 0.7]:
    conf_sig_f = confusion(FOOD_POS_FULL, FOOD_NEG,
                            lambda k, t=thr: siglip.get(k, {}).get("food_drink_en_pos", 0) >= t)
    print(f"SigLIP EN @ порог {thr}:", conf_sig_f)

print()
print("=" * 70)
print("КЛАСС: СЛАЙДЫ, СТУПЕНЬ 1 (экран/проекция в кадре, не 'наш ли')")
print(f"позитив (экран есть) n={len(SLIDES_SCREEN_PRESENT)}, негатив (экрана нет) n={len(SLIDES_SCREEN_ABSENT)}")
print("=" * 70)

conf_yolo_s = confusion(SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT,
                         lambda k: yolo.get(k, {}).get("screen_hit", False))
print("YOLO (класс 'tv'/'laptop'):", conf_yolo_s)

conf_vision_s = confusion(SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT,
                           lambda k: (vision.get(k, {}).get("parsed") or {}).get("screen_present", False))
print("Vision:", conf_vision_s)
# разложение ложных тревог vision по трём группам негатива (круг 3, добор): печатный
# постер/баннер, принятый пометкой OI за "Presentation", vs обычная B-сцена без экрана
hardneg_fp = sum(1 for k in SLIDES_HARDNEG if (vision.get(k, {}).get("parsed") or {}).get("screen_present", False))
gennew_fp = sum(1 for k in SLIDES_GENERAL_NEG_NEW if (vision.get(k, {}).get("parsed") or {}).get("screen_present", False))
bscene_fp = sum(1 for k in FOOD_B_NEG if (vision.get(k, {}).get("parsed") or {}).get("screen_present", False))
print(f"  из них на печатном постере/баннере, принятом пометкой OI за экран ({len(SLIDES_HARDNEG)}): {hardneg_fp}/{len(SLIDES_HARDNEG)}")
print(f"  из них на обычном \"экрана просто нет\" добора ({len(SLIDES_GENERAL_NEG_NEW)}): {gennew_fp}/{len(SLIDES_GENERAL_NEG_NEW)}")
print(f"  из них на B-сценах мероприятий без экрана ({len(FOOD_B_NEG)}): {bscene_fp}/{len(FOOD_B_NEG)}")

readable_keys = [k for k in SLIDES_SCREEN_PRESENT if k[1] in SLIDES_READABLE]
blank_keys = [k for k in SLIDES_SCREEN_PRESENT if k[1] in SLIDES_BLANK]
print(f"  спот-чек читаемости (6/22 глазами): читаемый n={len(readable_keys)}, "
      f"пустой/нечитаемый n={len(blank_keys)}")
for k in readable_keys + blank_keys:
    v = (vision.get(k, {}).get("parsed") or {}).get("screen_present")
    tag = "читаемый" if k in readable_keys else "пустой"
    print(f"    {k[1]} [{tag}]: vision screen_present={v}")

for thr in [0.3, 0.5, 0.7]:
    conf_sig_s = confusion(SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT,
                            lambda k, t=thr: siglip.get(k, {}).get("screen_present_en_pos", 0) >= t)
    print(f"SigLIP EN @ порог {thr}:", conf_sig_s)

print()
print("=" * 70)
print("ПОЛОСА НЕОПРЕДЕЛЁННОСТИ SigLIP (К4-методика, мерена заново на этом корпусе)")
print("=" * 70)
for cls, pos, neg, key in [
    ("курение", SMOKE_POS, SMOKE_NEG, "smoking_en_pos"),
    ("еда/напитки", FOOD_POS_FULL, FOOD_NEG, "food_drink_en_pos"),
    ("экран", SLIDES_SCREEN_PRESENT, SLIDES_SCREEN_ABSENT, "screen_present_en_pos"),
]:
    pos_scores = sorted(siglip.get(k, {}).get(key, 0) for k in pos)
    neg_scores = sorted(siglip.get(k, {}).get(key, 0) for k in neg)
    best_sum_err, best_thr = None, None
    for thr100 in range(0, 101):
        thr = thr100 / 100
        err = sum(1 for s in pos_scores if s < thr) + sum(1 for s in neg_scores if s >= thr)
        if best_sum_err is None or err < best_sum_err:
            best_sum_err, best_thr = err, thr
    lo = max([s for s in neg_scores], default=0)
    hi = min([s for s in pos_scores], default=1)
    print(f"{cls}: позитив-скоры min/med/max = {pos_scores[0]:.3f}/{pos_scores[len(pos_scores)//2]:.3f}/{pos_scores[-1]:.3f}; "
          f"негатив-скоры min/med/max = {neg_scores[0]:.3f}/{neg_scores[len(neg_scores)//2]:.3f}/{neg_scores[-1]:.3f}; "
          f"лучший порог={best_thr}, сумма ошибок={best_sum_err} из {len(pos)+len(neg)} "
          f"({round(100*best_sum_err/(len(pos)+len(neg)),1)}%)")
    # раздельные доли (поймано/пропустил/ложная тревога) НА ЭТОМ ЖЕ лучшем пороге —
    # пробел, названный сессией кадров: раньше была только сумма ошибок для еды/экрана
    conf_best = confusion(pos, neg, lambda k, t=best_thr: siglip.get(k, {}).get(key, 0) >= t)
    print(f"  @лучший порог {best_thr} раздельно: попал {conf_best['tp']} из {len(pos)}, "
          f"пропустил {conf_best['fn']} из {len(pos)} ({pct(conf_best['fn'], len(pos))}), "
          f"ложная тревога {conf_best['fp']} из {len(neg)} ({pct(conf_best['fp'], len(neg))})")

print()
print("=" * 70)
print("ЛЁГКИЙ / ТРУДНЫЙ СЛУЧАЙ — проверка §8.11")
print("=" * 70)
print("курение: крупная сигарета в кадре (01b07e6cf5803e5b) против кадра на дальнем плане "
      "(01b3fa4d58dcf9d3)")
for sid, dirn in [("01b07e6cf5803e5b", SMOKE_TRAIN_DIR), ("01b3fa4d58dcf9d3", SMOKE_TRAIN_DIR)]:
    k = (dirn, sid)
    print(f"  {sid}: vision={  (vision.get(k, {}).get('parsed') or {}).get('smoking') }, "
          f"siglip={siglip.get(k, {}).get('smoking_en_pos')}")
