#!/usr/bin/env python3
"""Кейс 4 (issue #311) — СЛИЯНИЕ РАНГОВ (RRF) двух сигналов на тех же 30 сканах CORD.

Зачем. Записка `rework/research-case4-gibrid-reranker.md` разобрала гибрид и реранкер для
картинок ТОЛЬКО по чужим публикациям: там нет ни одного замера на этом стенде, и перенос
приёма Кейса 3 на картинки стоит в ней пометкой «предположение по аналогии с текстом».
Этот прогон закрывает два пункта её §5 — варианты **A** и **B**, и только их (вариант C,
зрительно-языковая модель в роли реранкера, и вариант D, каскад, в этом прогоне НЕ делались).
Чтобы находка в деке опиралась на собственное число, а не на аналогию.

ФОРМУЛА СЛИЯНИЯ — ТА ЖЕ, ЧТО УЖЕ ОБЪЯСНЕНА В ЭТОМ ЖЕ ЗАНЯТИИ.
`rrf_fuse` ниже скопирована дословно из `case3_measure.py` (узел слияния Кейса 3), константа
k = 60 — та же, что стоит в этом коде, в настоящем узле сценария n8n и на кадре `n43-k3-rrf-
mekhanika.md`. Константа НЕ перебиралась под результат: основной результат считается
единственным каноническим k = 60. Перебор k есть, но лежит отдельно и помечен в выдаче как
`k_sweep_marked_experiment` — это проверка чувствительности, а не результат.

ЗАМЕР A — СЛИЯНИЕ ОТПЕЧАТКА И КАРТИНОЧНОГО ЭМБЕДДИНГА.
Задача ровно та же, что в части A `case4_full_retrieval_30.py`: найти ОРИГИНАЛ по его дублю
среди всех 30 сканов. Мягкий дубль (пересканировали: resize×0,97, JPEG q60) и жёсткий
(сняли под углом: поворот 12° + обрезка 4% краёв). Три метода на одной метрике recall@1:
картиночный эмбеддинг · отпечаток · слияние их рангов по RRF. Полные ранжированные списки
(все 30 кандидатов на запрос), а не только ближайший — иначе слияние посчитать нечем.

ЗАМЕР B — СЛИЯНИЕ КАРТИНКИ И ЕЁ ПОДПИСИ.
Задача смысловая, ровно та же, что часть C `case4_full_retrieval_30.py`: для каждого из 30
оригиналов найти ближайший ДРУГОЙ скан. Эталон («золотой сосед») взят ГОТОВЫМ из
`../raw/case4_mm_full_retrieval.json` (`part_C...details[].text_gold_nearest`) и заново НЕ
пересчитывается.

**Тавтология, названная прямо.** Эталон этого замера задан самим текстовым эмбеддингом —
поэтому собственный recall@1 согласия текстового метода с эталоном тривиально равен 1,000.
Это НЕ результат и не достижение текстового метода: это определение эталона, прочитанное
обратно. Честный вопрос замера B поэтому другой: **насколько слияние портит или не портит
текстовый список, добавляя к нему картиночный сигнал.** Именно так и сформулирован вывод.
Отдельно считается `text_self_agreement_with_stored_gold` — совпадение заново посчитанных
текстовых векторов с сохранённым эталоном; это проверка воспроизводимости (ожидается 1,000),
и если она не 1,000 — тавтология неточна ровно на эту долю, и это записывается как есть.

РАНГИ И НИЧЬИ. Список по эмбеддингу — сортировка по косинусу вниз; по отпечатку — по
расстоянию Хэмминга вверх. У отпечатка расстояние целое, поэтому ничьи реальны и частые;
они разбиваются устойчивостью сортировки, то есть порядком корпуса, — ровно так же, как в
Кейсе 3 ничьи целочисленного пересечения токенов. Число кандидатов, стоящих в ничью на
первом месте, считается и выносится в выдачу (`phash_top_tie_size_mean`), чтобы эта
условность была видна, а не спрятана.

ЗЕРНИСТОСТЬ. 30 сканов, шаг recall@1 = 1/30 = 0,033. Различие мельче ~0,1 — это два-три
скана, а не тенденция.

Вызовов: 30 оригиналов + 30 мягких + 30 жёстких картинок (`nvidia/nemotron-3.5-embed-1b:free`,
по одному вызову) + 1 пакетный вызов на 30 распознанных текстов
(`openai/text-embedding-3-small`) = 91. Сбои — в `fail_log`, не маскируются.

Запуск:
  set -a; . /home/harness/.n8n-lab-credentials; set +a
  cd library/seminars/sem-10/stend/measure
  python3 case4_fusion.py                   # -> case4_fusion_raw.json (в ../raw/ копируется вручную)
  python3 case4_fusion.py --rewrite-report  # пересобрать выводы из снятых чисел, без вызовов
"""
import base64
import io
import json
import time

from PIL import Image

# Переиспользованы БЕЗ ИЗМЕНЕНИЙ из замера, числа которого этот прогон обязан воспроизвести:
# та же геометрия дублей, тот же косинус, тот же отпечаток, тот же корпус и порядок сканов.
from case4_full_retrieval_30 import (
    MM_MODEL,
    TEXT_MODEL,
    average_hash,
    cosine,
    hamming,
    hard_dup,
    ids,
    paths,
    samples,
    soft_dup,
    to_data_url,
)
from harness_call import call_raw

K_RRF = 60  # case3_measure.py::rrf_fuse, узел слияния стенда, кадр n43. Не перебирается.
CKPT = "case4_fusion_ckpt.json"
GOLD_SRC = "../raw/case4_mm_full_retrieval.json"

fail_log = []
n_calls = 0
call_s = 0.0


def rrf_fuse(rank_a, rank_b, k=K_RRF):
    """Reciprocal Rank Fusion — классическое, не-ИИ слияние двух ранжирований.

    Скопировано дословно из `case3_measure.py` (тот же узел, та же константа k=60,
    тот же кадр n43). Единственное отличие — k по умолчанию берётся из K_RRF.
    """
    scores = {}
    for rank_list in (rank_a, rank_b):
        for i, doc_id in enumerate(rank_list):
            scores[doc_id] = scores.get(doc_id, 0.0) + 1.0 / (k + i + 1)
    return sorted(scores.keys(), key=lambda d: -scores[d])


# ---------------------------------------------------------------- вызовы
def embed_mm(data_url, tag, retries=4):
    """Один вызов картиночного эмбеддинга через вебхук s10-raw-openrouter.
    Журнал сбоев — честный: каждая неудачная попытка попадает в fail_log, даже если
    следующая попытка выручила (тогда рядом ложится запись `recovered_after_retry`)."""
    global n_calls, call_s
    body = {"model": MM_MODEL, "input": data_url}
    last = None
    for attempt in range(retries):
        t0 = time.time()
        r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=90, sleep=0.5)
        n_calls += 1
        call_s += time.time() - t0
        resp = r["response"] or {}
        if "data" in resp:
            if attempt:
                fail_log.append({"tag": tag, "attempt": attempt, "outcome": "recovered_after_retry"})
            return resp["data"][0]["embedding"]
        last = resp
        fail_log.append({"tag": tag, "attempt": attempt, "exec_id": r.get("exec_id"),
                         "error": json.dumps(last, ensure_ascii=False)[:300]})
        time.sleep(2.0 * (attempt + 1))
    fail_log.append({"tag": tag, "outcome": "FAILED_after_all_retries"})
    print(f"  !! embed FAILED {tag}: {json.dumps(last, ensure_ascii=False)[:160]}")
    return None


def embed_text_batch(texts, tag, retries=3):
    """Один ПАКЕТНЫЙ вызов текстового эмбеддинга на все 30 распознанных текстов —
    так же, как это делает часть B `case4_full_retrieval_30.py`."""
    global n_calls, call_s
    body = {"model": TEXT_MODEL, "input": texts}
    last = None
    for attempt in range(retries):
        t0 = time.time()
        r = call_raw("https://openrouter.ai/api/v1/embeddings", body, timeout=120, sleep=0.5)
        n_calls += 1
        call_s += time.time() - t0
        resp = r["response"] or {}
        if "data" in resp and len(resp["data"]) == len(texts):
            if attempt:
                fail_log.append({"tag": tag, "attempt": attempt, "outcome": "recovered_after_retry"})
            return [d["embedding"] for d in resp["data"]], (resp.get("usage", {}) or {}).get("cost")
        last = resp
        fail_log.append({"tag": tag, "attempt": attempt, "exec_id": r.get("exec_id"),
                         "error": json.dumps(last, ensure_ascii=False)[:300]})
        time.sleep(2.0 * (attempt + 1))
    fail_log.append({"tag": tag, "outcome": "FAILED_after_all_retries"})
    return None, None


# ---------------------------------------------------------------- ранги
def rank_by_cosine(qvec, pool, candidates):
    """Полный ранжированный список: по косинусу вниз. Ничьи (практически невозможны
    на вещественном косинусе) разбиваются порядком корпуса — устойчивостью сортировки."""
    scored = [(cosine(qvec, pool[c]), c) for c in candidates if pool.get(c) is not None]
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored]


def rank_by_hamming(qhash, pool, candidates):
    """Полный ранжированный список: по расстоянию Хэмминга вверх. Ничьи РЕАЛЬНЫ
    (расстояние целое) и разбиваются порядком корпуса — как ничьи пересечения токенов
    в Кейсе 3. Второе возвращаемое — размер ничьей на первом месте."""
    scored = [(hamming(qhash, pool[c]), c) for c in candidates]
    scored.sort(key=lambda x: x[0])
    top_d = scored[0][0]
    tie = sum(1 for d, _ in scored if d == top_d)
    return [c for _, c in scored], tie


def rank_of(ranked, target):
    return ranked.index(target) + 1 if target in ranked else None


def summarize(rows, key_prefix, n_candidates):
    """Свод по одному методу: recall@1, recall@3, среднее место верного ответа.
    Каждое число несёт базу — уровень случайности при том же числе кандидатов."""
    got = [r for r in rows if r.get(f"{key_prefix}_rank") is not None]
    if not got:
        return None
    n = len(got)
    return {
        "n": n,
        "recall_at_1": round(sum(1 for r in got if r[f"{key_prefix}_rank"] == 1) / n, 4),
        "n_correct_at_1": sum(1 for r in got if r[f"{key_prefix}_rank"] == 1),
        "recall_at_3": round(sum(1 for r in got if r[f"{key_prefix}_rank"] <= 3) / n, 4),
        "mean_rank_of_gold": round(sum(r[f"{key_prefix}_rank"] for r in got) / n, 2),
        "chance_level_recall_at_1": round(1 / n_candidates, 4),
    }


def ru(x, nd=3):
    """Число по-русски: запятая, а не точка — выводы отсюда уходят в прозу деки."""
    return f"{x:.{nd}f}".replace(".", ",")


def plural(n, one, few, many):
    n = abs(int(n))
    if n % 10 == 1 and n % 100 != 11:
        return f"{n} {one}"
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return f"{n} {few}"
    return f"{n} {many}"


def fusion_damage(rows, single_key):
    """Что слияние СДЕЛАЛО с лучшим одиночным списком, поштучно: сколько верных ответов
    сбросило с первого места и сколько, наоборот, выручило. Доля этого не показывает:
    она может стоять на месте, пока слияние ломает одно и выручает другое."""
    broke = sum(1 for r in rows
                if r.get(f"{single_key}_rank") == 1 and r.get("fusion_rank") not in (None, 1))
    saved = sum(1 for r in rows
                if r.get(f"{single_key}_rank") not in (None, 1) and r.get("fusion_rank") == 1)
    return broke, saved


def mean_or_none(vals):
    return round(sum(vals) / len(vals), 2) if vals else None


def backfill_derived(out):
    """Производные числа считаются ИЗ `details` — поэтому пересобираются без вызовов API
    и не могут разойтись с таблицами."""
    for name, task in out["measurement_A"]["tasks"].items():
        broke, saved = fusion_damage(task["details"], "mm")
        task["n_broke_mm_correct"] = broke
        task["n_saved_mm_wrong"] = saved
    B = out["measurement_B"]
    rows = B["details"]
    broke, saved = fusion_damage(rows, "txt")
    B["n_broke_text_top1"] = broke
    B["n_saved_text_top1"] = saved  # по построению 0: текстовый top-1 и есть эталон
    B["img_mean_rank_of_gold_on_broken"] = mean_or_none(
        [r["img_rank"] for r in rows if r.get("fusion_rank") not in (None, 1) and r.get("img_rank")])
    B["img_mean_rank_of_gold_on_kept"] = mean_or_none(
        [r["img_rank"] for r in rows if r.get("fusion_rank") == 1 and r.get("img_rank")])
    return out


def build_headline(A, B, sweep):
    """Выводы прогона — собираются ИЗ ИЗМЕРЕННЫХ ЧИСЕЛ, не из ожиданий. Каждая фраза
    несёт рядом базу, на фоне которой слияние оценивается."""
    soft, hard = A["tasks"]["soft"], A["tasks"]["hard"]
    h_mm = hard["mm_only"]["recall_at_1"]
    h_ph = hard["phash_only"]["recall_at_1"]
    h_fu = hard["fusion_rrf"]["recall_at_1"]
    s_mm = soft["mm_only"]["recall_at_1"]
    s_ph = soft["phash_only"]["recall_at_1"]
    s_fu = soft["fusion_rrf"]["recall_at_1"]
    broke = hard.get("n_broke_mm_correct")
    saved = hard.get("n_saved_mm_wrong")
    b_img = B["img_only"]["recall_at_1"]
    b_txt = B["text_only"]["recall_at_1"]
    b_fu = B["fusion_rrf"]["recall_at_1"]
    b_broke = B["n_broke_text_top1"]
    return [
        f"Слияние рангов на этих 30 сканах не помогло ни в одном из двух замеров. Замер A, "
        f"поворот: картиночный эмбеддинг один — {ru(h_mm)}, отпечаток один — {ru(h_ph)}, "
        f"слияние обоих — {ru(h_fu)}. Замер B, смысловая задача: картинка одна — {ru(b_img)}, "
        f"текстовый список — {ru(b_txt)} (тавтология, см. ниже), слияние — {ru(b_fu)}.",

        f"Потеря видна поштучно, а не только долей: на повороте слияние сбросило с первого "
        f"места {plural(broke, 'верный ответ', 'верных ответа', 'верных ответов')} из "
        f"{hard['mm_only']['n_correct_at_1']}, которые картиночный эмбеддинг нашёл сам, и "
        f"выручило ровно {saved} — тот единственный, где он ошибся. Итог — минус "
        f"{plural(broke - saved, 'скан', 'скана', 'сканов')} из 30.",

        f"Цена входа второго сигнала — его собственная слабость на этой задаче: отпечаток на "
        f"повороте даёт {ru(h_ph)}, и RRF, награждающий ровность в обоих списках, переносит "
        f"эту слабость в общий список. Это измеренная ГРАНИЦА приёма, а не его польза. Там, где "
        f"оба сигнала и так у потолка, приём не портит и не улучшает: мягкий дубль — эмбеддинг "
        f"{ru(s_mm)}, отпечаток {ru(s_ph)}, слияние {ru(s_fu)}; единственный промах отпечатка "
        f"слияние здесь выручило, но подниматься выше было некуда — и это лёгкий случай задачи, "
        f"а не свидетельство безвредности.",

        f"Замер B не может сказать, ЛУЧШЕ ли слияние текстового списка: эталон задан самим "
        f"текстовым эмбеддингом, поэтому его {ru(b_txt)} — тавтология, а не достижение. "
        f"Сказать, ПОРТИТ ли, он может: портит, "
        f"{plural(b_broke, 'скан', 'скана', 'сканов')} из 30, и ровно там, где картинка ставит "
        f"верный ответ далеко — на испорченных среднее место верного ответа у картинки "
        f"{ru(B['img_mean_rank_of_gold_on_broken'], 1)} против "
        f"{ru(B['img_mean_rank_of_gold_on_kept'], 1)} на уцелевших.",

        f"Перебор константы приём не спасает: при самом резком k=1 поворот даёт "
        f"{ru(sweep['A_hard']['1'])}, смысловая задача — {ru(sweep['B']['1'])} — всё равно ниже "
        f"лучшего одиночного сигнала ({ru(h_mm)} и {ru(b_txt)}). Помечено как перебор; "
        f"основной результат — канонический k={K_RRF} Кейса 3.",
    ]


LIMITS = [
    "Зернистость — 30 сканов, шаг recall@1 = 1/30 = 0,033. Различие мельче ~0,1 — это два-три "
    "скана, а не тенденция. Обе названные потери (0,367 на повороте и 0,300 на смысловой "
    "задаче) заметно крупнее этого порога; равенство на мягком дубле — ровно нуль, не «почти».",
    "Один корпус и один вид документа: 30 чеков CORD, где весь смысл лежит в распознаваемых "
    "строках. На корпусе со схемами и графиками порядок сил между картинкой и подписью другой "
    "(ColPali на ViDoRe — обратный), и этот результат туда не переносится.",
    "Проверена одна форма слияния — слияние рангов (RRF) с канонической константой стенда. "
    "Взвешенная сумма сходств, нормировка распределений (DBSF) и выпуклая комбинация НЕ "
    "проверялись; у них своя чувствительность к весам.",
    "Эталон замера B задан текстовым эмбеддингом, а не человеком. Он измеряет согласие с "
    "текстовым методом, а не истинную смысловую близость; вопрос «кто из них ближе к правде» "
    "этим замером не решается вовсе.",
    "Мягкий дубль — ЛЁГКИЙ случай обеих задач: оба сигнала стоят у потолка (1,000 и 0,967), "
    "и равенство слияния там — свойство лёгкости задачи, а не свидетельство безвредности "
    "приёма. Трудный случай той же задачи — поворот, и на нём потеря измерена "
    "(tools/seminar-production/README.md §8.11: «ничего не изменилось» проверяется на "
    "лёгкость случая так же, как ноль).",
    "Не делались варианты C (зрительно-языковая модель в роли реранкера) и D (каскад "
    "«отпечаток отбирает — эмбеддинг решает») из §5 записки.",
    "Дубли синтетические и детерминированные — шума матрицы, смаза от руки, бликов и сгиба "
    "бумаги в замере нет (та же оговорка, что у замера границ).",
]


def rewrite_report(path="case4_fusion_raw.json"):
    """Пересобрать выводы и оговорки из УЖЕ снятых чисел — без единого вызова API.
    Нужно, чтобы правка формулировки вывода не стоила нового прогона стенда."""
    out = backfill_derived(json.load(open(path)))
    out["headline"] = build_headline(out["measurement_A"], out["measurement_B"],
                                     out["k_sweep_marked_experiment"])
    out["limits"] = LIMITS
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("\n".join(out["headline"]))
    return out


# ---------------------------------------------------------------- прогон
def run():
    t0 = time.time()
    state = {}

    def ckpt(stage):
        state["_stage"] = stage
        json.dump(state, open(CKPT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # ---------- 1. индекс: 30 оригиналов, картиночный эмбеддинг + отпечаток ----------
    print(f"=== индекс: 30 оригиналов, {MM_MODEL} ===")
    mm_orig, ph_orig = {}, {}
    for sid in ids:
        p = paths[sid]
        mm_orig[sid] = embed_mm(to_data_url(p), f"orig:{sid}")
        # отпечаток индекса — на ПОЛНОМ оригинале файла, как в case4_full_retrieval_30.py
        ph_orig[sid] = average_hash(Image.open(p).convert("RGB"))
        print(f"  orig {sid}: ok={mm_orig[sid] is not None}")
        time.sleep(0.3)
    state["index_ok"] = sum(1 for v in mm_orig.values() if v is not None)
    ckpt("index")

    # ---------- 2. дубли: мягкий и жёсткий, по 30 ----------
    dups = {}
    for name, fn in (("soft", soft_dup), ("hard", hard_dup)):
        print(f"=== 30 {name}-дублей ===")
        mm, ph = {}, {}
        for sid in ids:
            du = fn(paths[sid])
            mm[sid] = embed_mm(du, f"{name}:{sid}")
            # отпечаток дубля — на декодированных байтах ровно той картинки, которая
            # ушла в модель (как в case4_full_retrieval_30.py)
            raw = base64.b64decode(du.split(",", 1)[1])
            ph[sid] = average_hash(Image.open(io.BytesIO(raw)).convert("RGB"))
            print(f"  {name} {sid}: ok={mm[sid] is not None}")
            time.sleep(0.3)
        dups[name] = {"mm": mm, "ph": ph}
        state[f"{name}_ok"] = sum(1 for v in mm.values() if v is not None)
        ckpt(f"dup_{name}")

    # ---------- 3. ЗАМЕР A: слияние отпечатка и картиночного эмбеддинга ----------
    print("\n=== ЗАМЕР A: отпечаток + картиночный эмбеддинг, RRF k=60 ===")
    measurement_A = {
        "task": "найти ОРИГИНАЛ по его дублю среди всех 30 сканов (та же задача, что часть A "
                "case4_full_retrieval_30.py)",
        "n_candidates": len(ids),
        "metric": "recall@1 (+ recall@3 и среднее место верного ответа как база)",
        "tasks": {},
    }
    for name in ("soft", "hard"):
        mm_q, ph_q = dups[name]["mm"], dups[name]["ph"]
        rows, ties = [], []
        for sid in ids:
            row = {"id": sid}
            if mm_q[sid] is not None:
                mm_rank = rank_by_cosine(mm_q[sid], mm_orig, ids)
                row["mm_rank"] = rank_of(mm_rank, sid)
                row["mm_top1"] = mm_rank[0]
            else:
                mm_rank = None
            ph_rank, tie = rank_by_hamming(ph_q[sid], ph_orig, ids)
            ties.append(tie)
            row["phash_rank"] = rank_of(ph_rank, sid)
            row["phash_top1"] = ph_rank[0]
            row["phash_top_tie_size"] = tie
            if mm_rank is not None:
                fused = rrf_fuse(mm_rank, ph_rank)
                row["fusion_rank"] = rank_of(fused, sid)
                row["fusion_top1"] = fused[0]
                row["fusion_flipped_mm"] = (fused[0] != mm_rank[0])
            rows.append(row)
        block = {
            "mm_only": summarize(rows, "mm", len(ids)),
            "phash_only": summarize(rows, "phash", len(ids)),
            "fusion_rrf": summarize(rows, "fusion", len(ids)),
            "phash_top_tie_size_mean": round(sum(ties) / len(ties), 2),
            "n_fusion_flipped_mm_top1": sum(1 for r in rows if r.get("fusion_flipped_mm")),
            "details": rows,
        }
        measurement_A["tasks"][name] = block
        print(f"  {name}: mm={block['mm_only']['recall_at_1']} "
              f"phash={block['phash_only']['recall_at_1']} "
              f"fusion={block['fusion_rrf']['recall_at_1']}")
    state["measurement_A"] = measurement_A
    ckpt("measurement_A")

    # ---------- 4. ЗАМЕР B: слияние картинки и её подписи ----------
    print("\n=== ЗАМЕР B: картинка + подпись, RRF k=60 ===")
    gold_src = json.load(open(GOLD_SRC))
    gold = {r["id"]: r["text_gold_nearest"]
            for r in gold_src["part_C_semantic_similarity_agreement"]["details"]}
    ocr_texts = [s["ocr_text"] for s in samples]
    vecs, text_cost = embed_text_batch(ocr_texts, "text_batch_30")
    text_vecs = dict(zip(ids, vecs)) if vecs else {}

    measurement_B = {
        "task": "для каждого из 30 оригиналов найти ближайший ДРУГОЙ скан (та же задача, что "
                "часть C case4_full_retrieval_30.py); эталон — text_gold_nearest, взят ГОТОВЫМ "
                "из ../raw/case4_mm_full_retrieval.json и заново не пересчитан",
        "n_candidates": len(ids) - 1,
        "tautology_warning": (
            "Эталон задан самим текстовым эмбеддингом, поэтому recall@1 согласия текстового "
            "метода с эталоном тривиально равен 1,000. Это определение эталона, прочитанное "
            "обратно, а НЕ результат текстового метода и не его достижение. Честный вопрос "
            "замера B: насколько слияние портит или не портит текстовый список, добавляя к "
            "нему картиночный сигнал."),
        "gold_source": GOLD_SRC,
        "text_embed_cost_usd": text_cost,
    }
    rows = []
    for sid in ids:
        others = [x for x in ids if x != sid]
        g = gold.get(sid)
        row = {"id": sid, "gold": g}
        img_rank = (rank_by_cosine(mm_orig[sid], mm_orig, others)
                    if mm_orig.get(sid) is not None else None)
        txt_rank = (rank_by_cosine(text_vecs[sid], text_vecs, others)
                    if text_vecs.get(sid) is not None else None)
        if img_rank and g:
            row["img_rank"] = rank_of(img_rank, g)
            row["img_top1"] = img_rank[0]
        if txt_rank and g:
            row["txt_rank"] = rank_of(txt_rank, g)
            row["txt_top1"] = txt_rank[0]
            row["txt_reproduces_stored_gold"] = (txt_rank[0] == g)
        if img_rank and txt_rank and g:
            fused = rrf_fuse(txt_rank, img_rank)
            row["fusion_rank"] = rank_of(fused, g)
            row["fusion_top1"] = fused[0]
            row["fusion_kept_text_top1"] = (fused[0] == txt_rank[0])
        rows.append(row)

    n_txt = sum(1 for r in rows if "txt_reproduces_stored_gold" in r)
    measurement_B.update({
        "img_only": summarize(rows, "img", len(ids) - 1),
        "text_only": summarize(rows, "txt", len(ids) - 1),
        "fusion_rrf": summarize(rows, "fusion", len(ids) - 1),
        "text_self_agreement_with_stored_gold": (
            round(sum(1 for r in rows if r.get("txt_reproduces_stored_gold")) / n_txt, 4)
            if n_txt else None),
        "n_fusion_kept_text_top1": sum(1 for r in rows if r.get("fusion_kept_text_top1")),
        "details": rows,
    })
    print(f"  img={measurement_B['img_only']['recall_at_1']} "
          f"text={measurement_B['text_only']['recall_at_1']} "
          f"fusion={measurement_B['fusion_rrf']['recall_at_1']} "
          f"(текст воспроизвёл эталон: {measurement_B['text_self_agreement_with_stored_gold']})")
    state["measurement_B"] = measurement_B
    ckpt("measurement_B")

    # ---------- 5. ПОМЕЧЕННЫЙ ОПЫТ: перебор константы ----------
    # Основной результат выше посчитан единственной канонической k=60 и ею же остаётся.
    # Это — проверка чувствительности приёма к собственному параметру, помеченная как
    # перебор константы; её числа НЕ являются результатом замера.
    sweep = {"_label": "ПЕРЕБОР КОНСТАНТЫ — не результат замера, проверка чувствительности. "
                       "Основной результат считается k=60 (Кейс 3, кадр n43) и не меняется.",
             "k_values": [1, 10, 60, 100, 1000], "A_hard": {}, "A_soft": {}, "B": {}}
    for k in sweep["k_values"]:
        for name, key in (("hard", "A_hard"), ("soft", "A_soft")):
            mm_q, ph_q = dups[name]["mm"], dups[name]["ph"]
            hit = tot = 0
            for sid in ids:
                if mm_q[sid] is None:
                    continue
                mm_rank = rank_by_cosine(mm_q[sid], mm_orig, ids)
                ph_rank, _ = rank_by_hamming(ph_q[sid], ph_orig, ids)
                tot += 1
                hit += (rrf_fuse(mm_rank, ph_rank, k=k)[0] == sid)
            sweep[key][str(k)] = round(hit / tot, 4) if tot else None
        hit = tot = 0
        for sid in ids:
            others = [x for x in ids if x != sid]
            g = gold.get(sid)
            if not g or mm_orig.get(sid) is None or not text_vecs.get(sid):
                continue
            img_rank = rank_by_cosine(mm_orig[sid], mm_orig, others)
            txt_rank = rank_by_cosine(text_vecs[sid], text_vecs, others)
            tot += 1
            hit += (rrf_fuse(txt_rank, img_rank, k=k)[0] == g)
        sweep["B"][str(k)] = round(hit / tot, 4) if tot else None
    print("\n=== перебор константы (помеченный опыт) ===")
    print(json.dumps({k: sweep[k] for k in ("A_hard", "A_soft", "B")}, ensure_ascii=False))

    # ---------- 6. выдача ----------
    A, B = measurement_A, measurement_B
    out = {
        "purpose": (
            "Домерить на живом стенде два слияния сигналов для Кейса 4 (поиск по "
            "изображениям), чтобы находка про гибрид опиралась на собственное число этого "
            "стенда, а не на аналогию с текстом. Закрывает варианты A и B из §5 записки "
            "rework/research-case4-gibrid-reranker.md; варианты C (реранкер зрительно-"
            "языковой моделью) и D (каскад) в этом прогоне НЕ делались."),
        "method": {
            "fusion_formula": "RRF: очко документа в списке = 1/(k + место), место с 1; "
                              "очки документа из обоих списков складываются; порядок — по сумме вниз",
            "k": K_RRF,
            "k_source": "case3_measure.py::rrf_fuse (узел слияния Кейса 3) = настоящий узел "
                        "сценария n8n = кадр slides/n43-k3-rrf-mekhanika.md. Та же константа, "
                        "чтобы Кейс 4 не противоречил Кейсу 3. Под результат не перебиралась.",
            "rrf_code_origin": "функция скопирована дословно из case3_measure.py",
            "models": {"image": MM_MODEL, "text": TEXT_MODEL},
            "corpus": "30 сканов CORD, ../corpus/cord_sample_meta.json — тот же корпус и тот же "
                      "порядок, что у всех прежних замеров Кейса 4",
            "reused_verbatim": ["to_data_url", "soft_dup", "hard_dup", "average_hash", "hamming",
                                "cosine", "ids", "paths", "samples"],
            "reused_from": "case4_full_retrieval_30.py (импортом, без изменений)",
            "ranking": "эмбеддинг — косинус вниз; отпечаток — расстояние Хэмминга вверх; "
                       "ничьи отпечатка разбиваются порядком корпуса (устойчивость сортировки), "
                       "как ничьи целочисленного пересечения токенов в Кейсе 3",
            "granularity": "30 сканов, шаг recall@1 = 1/30 = 0,033; различие мельче ~0,1 — "
                           "это два-три скана, а не тенденция",
            "n_api_calls_planned": "30 оригиналов + 30 мягких + 30 жёстких картинок + "
                                   "1 пакетный на 30 текстов = 91",
        },
        "measurement_A": A,
        "measurement_B": B,
        "k_sweep_marked_experiment": sweep,
        "fail_log": fail_log,
        "timing": {"total_wall_s": round(time.time() - t0, 1), "n_calls": n_calls,
                   "mean_call_s": round(call_s / n_calls, 3) if n_calls else None},
    }
    backfill_derived(out)
    out["headline"] = build_headline(out["measurement_A"], out["measurement_B"], sweep)
    out["limits"] = LIMITS
    path = "case4_fusion_raw.json"
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"\n=== записано {path}; {n_calls} вызовов, "
          f"{out['timing']['total_wall_s']} с, записей в журнале сбоев: {len(fail_log)} ===")
    return out


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--rewrite-report", action="store_true",
                    help="пересобрать headline/limits/производные из уже снятого "
                         "case4_fusion_raw.json, без единого вызова стенда")
    a = ap.parse_args()
    rewrite_report() if a.rewrite_report else run()
