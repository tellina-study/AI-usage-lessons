#!/usr/bin/env python3
"""
prompt-structure-experiment.py — язык × порядок блоков промпта: есть ли взаимодействие?

Issue: tellina-study/AI-usage-lessons#216 (research-prompt-language), раунд 2.
Вопрос владельца: сохраняется ли оптимальный порядок блоков промпта при смене
языка? Ключевое измерение — не "какой порядок лучше", а меняется ли
РАНЖИРОВАНИЕ 4 порядков между RU и EN (взаимодействие "язык × структура").

ДВА УСЛОВИЯ СЛОЖНОСТИ (калибровочный журнал, см. §Калибровка в отчёте):
  easy — исходный дизайн (8 кандидатов, 4 атрибута, 3 ограничения, простые
         >=/== ограничения). Пилот role_first/RU дал 24/24=100% — ПОТОЛОК,
         на этом условии эффект порядка структурно не измерим. Сохранено
         как самостоятельный результат ("на лёгкой задаче точного выбора
         структура промпта не имеет значения") — проверяется на 4 ячейках
         (role_first и resources_last × RU/EN), не на всех 8.
  hard — усложнённый дизайн (14 кандидатов, 6 атрибутов, 5 ограничений:
         одна негация [!=], одно простое числовое сравнение [cpu >=], одно
         производное/реляционное [price/RAM <=, требует деления двух
         атрибутов], плюс ещё 2; ≥3 форсированных дистрактора 4/5; близко
         расположенные числовые значения — latency шаг 1мс, RAM шаг 0.5ГБ).
         На этом условии прогоняется ПОЛНАЯ сетка 4 порядка × 2 языка (+
         повтор для 2 ячеек — оценка шума прогона-к-прогону).

ЗАДАЧА-НОСИТЕЛЬ (оба условия): выбор единственного кандидата, который
проходит ВСЕ ограничения. Ровно один кандидат проходит все; минимум
2 (easy) / 3 (hard) "почти подходящих" дистрактора проходят ровно N-1 из N
ограничений (гарантируется конструктивно, см. generate_task_easy/hard()).
Чекер — строгий exact-match по извлечённому идентификатору кандидата (regex
`K\\d+`, без учёта регистра/пробелов).

4 ПОРЯДКА БЛОКОВ (одни и те же 5 блоков: РОЛЬ / РЕСУРСЫ / ЗАДАЧА /
ОГРАНИЧЕНИЯ / ФОРМАТ, меняется только порядок):
  role_first        — РОЛЬ → РЕСУРСЫ → ЗАДАЧА → ОГРАНИЧЕНИЯ → ФОРМАТ
  task_first        — ЗАДАЧА → ОГРАНИЧЕНИЯ → РОЛЬ → РЕСУРСЫ → ФОРМАТ
  constraints_last   — РОЛЬ → РЕСУРСЫ → ЗАДАЧА → ФОРМАТ → ОГРАНИЧЕНИЯ
  resources_last      — РОЛЬ → ЗАДАЧА → ОГРАНИЧЕНИЯ → РЕСУРСЫ → ФОРМАТ

2 ЯЗЫКА: RU и EN — EN это перевод той же структуры/содержания (одинаковые
кандидаты в одном и том же порядке, одинаковые ограничения; меняется только
язык текста блоков).

ПАРНЫЙ ДИЗАЙН (hard): одни и те же N_TASKS=24 задания проходят все 8 ячеек
(4 порядка × 2 языка) = 192 вызова. Плюс повтор (второй независимый прогон)
для 2 ячеек — оценка шума прогона-к-прогону (temperature через CLI не
задаётся — это confound, honestly признан в отчёте).

МОДЕЛЬ-БЭКЕНД: CLI `claude -p ... --model haiku ...` (см. call_model()).
Задания генерируются ДЕТЕРМИНИРОВАННО по seed — повторный запуск скрипта
даёт те же задания (но не обязательно тот же ответ модели — сэмплинг
недетерминирован, отсюда и повтор для оценки шума).

КАК ЗАПУСТИТЬ:
    # 1. Пилот hard (одна ячейка, 24 вызова, ~2-4 мин) — калибровка сложности:
    python3 prompt-structure-experiment.py --pilot-hard

    # 2. easy-ceiling (4 ячейки x 24 = 96 вызовов) — проверка потолка:
    python3 prompt-structure-experiment.py --easy-ceiling

    # 3. Полный hard-прогон (192 + 48 повторных = 240 вызовов, ~15-20 мин):
    python3 prompt-structure-experiment.py --full-hard

    # 4. Пересчитать отчёт по уже накопленному raw jsonl без новых вызовов:
    python3 prompt-structure-experiment.py --report-only

Сырые вызовы построчно пишутся в prompt-structure-experiment-raw.jsonl по
мере выполнения (append-only, не теряется при прерывании).

СТОИМОСТЬ/ВРЕМЯ: каждый вызов `claude -p --model haiku` ~6-10 сек,
конкурентность 4 параллельных процесса. Не запускать повторно без нужды —
расход реальных токенов на реальную модель, не симуляция.
"""

import sys
import os
import re
import json
import time
import random
import hashlib
import argparse
import datetime
import subprocess
import concurrent.futures as cf

SEED_EASY = 20261002
SEED_HARD = 20261003
N_TASKS = 24
MODEL = "haiku"
SYS_PROMPT = "You answer exactly as instructed. Output only the final answer, no explanation."
DISALLOWED = "Bash,Read,Write,Edit,WebSearch,WebFetch,Agent,Glob,Grep"
MAX_WORKERS = 2  # снижено с 4: система делит ресурсы с другими параллельными
                 # сессиями claude на этой машине, при concurrency=4 часть
                 # вызовов упиралась в CALL_TIMEOUT_S (см. журнал калибровки)
CALL_TIMEOUT_S = 150
MAX_RETRIES = 2

RAW_JSONL = os.path.join(os.path.dirname(__file__), "prompt-structure-experiment-raw.jsonl")

ORDERS = {
    "role_first": ["role", "resources", "task", "constraints", "format"],
    "task_first": ["task", "constraints", "role", "resources", "format"],
    "constraints_last": ["role", "resources", "task", "format", "constraints"],
    "resources_last": ["role", "task", "constraints", "resources", "format"],
}

# Ячейки для повторного (независимого) прогона на условии hard — оценка
# шума прогона-к-прогону.
REPEAT_CELLS_HARD = [("role_first", "RU"), ("resources_last", "EN")]
# Ячейки для easy-ceiling проверки (не вся сетка — только best/worst-ожидаемые).
EASY_CEILING_CELLS = [("role_first", "RU"), ("role_first", "EN"),
                       ("resources_last", "RU"), ("resources_last", "EN")]

ATTR_LABEL_RU = {
    "cpu": "ядра CPU", "ram": "RAM (ГБ)", "storage": "накопитель", "region": "регион",
    "price": "цена (у.е./мес)", "latency": "задержка (мс)",
}
ATTR_LABEL_EN = {
    "cpu": "CPU cores", "ram": "RAM (GB)", "storage": "storage", "region": "region",
    "price": "price (units/mo)", "latency": "latency (ms)",
}


def satisfies(candidate, constraint):
    attr, op, value = constraint["attr"], constraint["op"], constraint["value"]
    cval = candidate[attr]
    if op == ">=":
        return cval >= value
    elif op == "<=":
        return cval <= value
    elif op == "==":
        return cval == value
    elif op == "!=":
        return cval != value
    raise ValueError(op)


def count_pass(candidate, constraints):
    return sum(1 for c in constraints if satisfies(candidate, c))


# ---------------------------------------------------------------------------
# 1a. EASY: исходный дизайн (8 кандидатов, 4 атрибута, 3 ограничения)
# ---------------------------------------------------------------------------

EASY_CPU_DOMAIN = [4, 8, 16, 32, 64]
EASY_RAM_DOMAIN = [8, 16, 32, 64, 128, 256]
EASY_STORAGE_DOMAIN = ["SSD", "HDD"]
EASY_REGION_DOMAIN = ["EU", "US", "ASIA"]
EASY_DOMAINS = {"cpu": EASY_CPU_DOMAIN, "ram": EASY_RAM_DOMAIN,
                "storage": EASY_STORAGE_DOMAIN, "region": EASY_REGION_DOMAIN}
EASY_NUMERIC = {"cpu", "ram"}
EASY_N_CANDIDATES = 8
EASY_FORCED_NEAR_MISS_N = 2


def generate_task_easy(rng, task_idx):
    attrs = ["cpu", "ram", "storage", "region"]
    constrained_dims = rng.sample(attrs, 3)
    decoy_dim = [a for a in attrs if a not in constrained_dims][0]

    winner = {}
    for a in attrs:
        domain = EASY_DOMAINS[a]
        if a in constrained_dims and a in EASY_NUMERIC:
            winner[a] = rng.choice(domain[1:])
        else:
            winner[a] = rng.choice(domain)

    constraints = []
    for a in constrained_dims:
        op = ">=" if a in EASY_NUMERIC else "=="
        constraints.append({"attr": a, "op": op, "value": winner[a]})

    fail_dim_1, fail_dim_2 = rng.sample(constrained_dims, 2)

    def build_near_miss(fail_dim):
        cand = {}
        for a in attrs:
            if a == fail_dim:
                domain = EASY_DOMAINS[a]
                threshold = winner[a]
                if a in EASY_NUMERIC:
                    choices = [v for v in domain if v < threshold]
                else:
                    choices = [v for v in domain if v != threshold]
                cand[a] = rng.choice(choices)
            elif a in constrained_dims:
                cand[a] = winner[a]
            else:
                cand[a] = rng.choice(EASY_DOMAINS[a])
        return cand

    d1 = build_near_miss(fail_dim_1)
    d2 = build_near_miss(fail_dim_2)
    assert count_pass(d1, constraints) == 2
    assert count_pass(d2, constraints) == 2

    fillers = []
    for _ in range(EASY_N_CANDIDATES - 1 - EASY_FORCED_NEAR_MISS_N):
        for _attempt in range(100):
            cand = {a: rng.choice(EASY_DOMAINS[a]) for a in attrs}
            if count_pass(cand, constraints) < 3:
                fillers.append(cand)
                break
        else:
            raise RuntimeError("easy: could not generate a valid filler")

    pool = [dict(winner, _role="winner")] + \
           [dict(d1, _role="near_miss_1"), dict(d2, _role="near_miss_2")] + \
           [dict(f, _role=f"filler_{i}") for i, f in enumerate(fillers)]
    assert len(pool) == EASY_N_CANDIDATES

    rng.shuffle(pool)
    for i, c in enumerate(pool, 1):
        c["id"] = f"K{i}"

    pass_counts = [count_pass(c, constraints) for c in pool]
    full_match = [c for c, p in zip(pool, pass_counts) if p == 3]
    near_miss = [c for c, p in zip(pool, pass_counts) if p == 2]
    assert len(full_match) == 1
    assert len(near_miss) >= 2

    return {
        "condition": "easy",
        "task_idx": task_idx,
        "candidates": pool,
        "display_attrs": ["cpu", "ram", "storage", "region"],
        "constraints": constraints,
        "winner_id": full_match[0]["id"],
        "near_miss_count": len(near_miss),
    }


def generate_all_tasks_easy(seed=SEED_EASY, n=N_TASKS):
    rng = random.Random(seed)
    return [generate_task_easy(rng, i) for i in range(n)]


# ---------------------------------------------------------------------------
# 1b. HARD v2 (калибровка 2026-10-02, попытка 3 — РЕЖИМ, не градус сложности,
#     по указанию оркестратора): 60 кандидатов, 6 атрибутов, 5 ограничений,
#     задача — АГРЕГАЦИЯ ("самый дешёвый среди подходящих"), не просто
#     "найди подходящего". Это заставляет просканировать весь длинный блок
#     РЕСУРСОВ и сравнить цены, а не остановиться на первом совпадении —
#     именно здесь, по гипотезе оркестратора, порядок блоков (ресурсы до/
#     после инструкции) может начать иметь значение. Попытки 1 (8 кандидатов)
#     и 2 (14 кандидатов, усложнённая ЛОГИКА) дали потолок 100% — усложнение
#     логики не сработало, меняем ось на длину контекста + агрегацию.
#     Это ПОСЛЕДНЯЯ попытка калибровки (прямое указание оркестратора,
#     issue #216 раунд 2) — третьей попытки не будет при любом исходе.
# ---------------------------------------------------------------------------

HARD_CPU_DOMAIN = list(range(4, 33))          # 4..32, шаг 1 (близкие значения)
HARD_RAM_DOMAIN = [round(x * 0.5, 1) for x in range(16, 65)]  # 8.0..32.0, шаг 0.5
HARD_STORAGE_DOMAIN = ["SSD", "HDD", "NVMe"]
HARD_REGION_DOMAIN = ["EU", "US", "ASIA", "SA"]
HARD_PRICE_DOMAIN = list(range(40, 400, 1))   # дробная шкала — ниже вероятность совпадения цен
HARD_LATENCY_DOMAIN = list(range(5, 61))      # 5..60мс, шаг 1 (близкие значения)
HARD_DOMAINS = {"cpu": HARD_CPU_DOMAIN, "storage": HARD_STORAGE_DOMAIN,
                "region": HARD_REGION_DOMAIN, "latency": HARD_LATENCY_DOMAIN}
HARD_N_CANDIDATES = 60
HARD_FORCED_NEAR_MISS_N = 12       # >=10 требование оркестратора, +2 запас
HARD_EXTRA_QUALIFIERS_N = 2        # дополнительные "подходящие, но не самые дешёвые"
HARD_MIN_WINNER_POSITION = 5       # победитель не должен попасть в первые 4 позиции списка


def generate_task_hard(rng, task_idx):
    # Какой из storage/region несёт негацию (!=), какой — равенство (==).
    neg_attr, eq_attr = rng.sample(["storage", "region"], 2)

    winner = {}
    winner["cpu"] = rng.choice(HARD_CPU_DOMAIN[1:])           # >= : исключаем минимум
    winner["latency"] = rng.choice(HARD_LATENCY_DOMAIN[:-1])  # <= : исключаем максимум
    winner[eq_attr] = rng.choice(HARD_DOMAINS[eq_attr])
    winner[neg_attr] = rng.choice(HARD_DOMAINS[neg_attr])
    forbidden_choices = [v for v in HARD_DOMAINS[neg_attr] if v != winner[neg_attr]]
    forbidden_value = rng.choice(forbidden_choices)
    winner["ram"] = rng.choice(HARD_RAM_DOMAIN)
    # Цена победителя — не самая низкая теоретически возможная, чтобы были
    # near-miss с привлекательно низкой ценой, но нарушающие constraint.
    winner["price"] = rng.choice([p for p in HARD_PRICE_DOMAIN if p >= 120])
    winner["derived"] = round(winner["price"] / winner["ram"], 2)
    ratio_threshold = winner["derived"]

    constraints = [
        {"attr": "cpu", "op": ">=", "value": winner["cpu"]},
        {"attr": neg_attr, "op": "!=", "value": forbidden_value},
        {"attr": eq_attr, "op": "==", "value": winner[eq_attr]},
        {"attr": "derived", "op": "<=", "value": ratio_threshold},
        {"attr": "latency", "op": "<=", "value": winner["latency"]},
    ]
    assert count_pass(winner, constraints) == 5

    slots = ["cpu", neg_attr, eq_attr, "derived", "latency"]

    def build_near_miss(fail_slot, price_bias_low):
        cand = {}
        if fail_slot == "cpu":
            choices = sorted([v for v in HARD_CPU_DOMAIN if v < winner["cpu"]],
                              key=lambda v: winner["cpu"] - v)
            cand["cpu"] = choices[0] if rng.random() < 0.7 else rng.choice(choices)
        else:
            cand["cpu"] = winner["cpu"]
        if fail_slot == "latency":
            choices = sorted([v for v in HARD_LATENCY_DOMAIN if v > winner["latency"]],
                              key=lambda v: v - winner["latency"])
            cand["latency"] = choices[0] if rng.random() < 0.7 else rng.choice(choices)
        else:
            cand["latency"] = winner["latency"]
        cand[neg_attr] = forbidden_value if fail_slot == neg_attr else winner[neg_attr]
        if fail_slot == eq_attr:
            choices = [v for v in HARD_DOMAINS[eq_attr] if v != winner[eq_attr]]
            cand[eq_attr] = rng.choice(choices)
        else:
            cand[eq_attr] = winner[eq_attr]
        if fail_slot == "derived":
            cand["ram"] = winner["ram"]
            bad_prices = [p for p in HARD_PRICE_DOMAIN
                          if round(p / cand["ram"], 2) > ratio_threshold]
            cand["price"] = rng.choice(bad_prices) if bad_prices else max(HARD_PRICE_DOMAIN)
        else:
            cand["ram"] = winner["ram"]
            # Приманка: near-miss, нарушающий НЕ-ценовой slot, получает цену
            # НИЖЕ победителя (соблазн для агрегации "самый дешёвый"), иначе
            # цену около/выше победителя — чтобы не все near-miss были дешёвыми.
            if price_bias_low:
                low_choices = [p for p in HARD_PRICE_DOMAIN if p < winner["price"]]
                cand["price"] = rng.choice(low_choices) if low_choices else winner["price"]
            else:
                cand["price"] = winner["price"]
        cand["derived"] = round(cand["price"] / cand["ram"], 2)
        return cand

    near_misses_built = []
    for i in range(HARD_FORCED_NEAR_MISS_N):
        fail_slot = slots[i % len(slots)]
        price_bias_low = (fail_slot != "derived") and (i % 2 == 0)
        nm = build_near_miss(fail_slot, price_bias_low)
        assert count_pass(nm, constraints) == 4, (fail_slot, nm, winner, constraints)
        near_misses_built.append(nm)

    # Доп. "подходящие, но не самые дешёвые" — полностью удовлетворяют всем 5,
    # но дороже победителя (победитель остаётся единственным минимумом цены).
    extra_qualifiers = []
    for _ in range(HARD_EXTRA_QUALIFIERS_N):
        cand = dict(winner)
        for _attempt in range(100):
            higher_prices = [p for p in HARD_PRICE_DOMAIN if p > winner["price"]]
            price = rng.choice(higher_prices)
            # нужен ram такой, что price/ram <= ratio_threshold
            min_ram_needed = price / ratio_threshold
            ram_choices = [r for r in HARD_RAM_DOMAIN if r >= min_ram_needed]
            if ram_choices:
                cand = dict(winner)
                cand["price"] = price
                cand["ram"] = rng.choice(ram_choices)
                cand["derived"] = round(cand["price"] / cand["ram"], 2)
                if count_pass(cand, constraints) == 5 and cand["price"] > winner["price"]:
                    extra_qualifiers.append(cand)
                    break
        else:
            pass  # если не нашли — просто меньше доп.качественных, не критично

    n_fillers = HARD_N_CANDIDATES - 1 - len(near_misses_built) - len(extra_qualifiers)
    fillers = []
    for _ in range(n_fillers):
        for _attempt in range(300):
            cand = {
                "cpu": rng.choice(HARD_CPU_DOMAIN),
                "ram": rng.choice(HARD_RAM_DOMAIN),
                "storage": rng.choice(HARD_STORAGE_DOMAIN),
                "region": rng.choice(HARD_REGION_DOMAIN),
                "price": rng.choice(HARD_PRICE_DOMAIN),
                "latency": rng.choice(HARD_LATENCY_DOMAIN),
            }
            cand["derived"] = round(cand["price"] / cand["ram"], 2)
            if count_pass(cand, constraints) < 5:
                fillers.append(cand)
                break
        else:
            raise RuntimeError("hard: could not generate a valid filler")

    pool = [dict(winner, _role="winner")] + \
           [dict(nm, _role=f"near_miss_{i}") for i, nm in enumerate(near_misses_built)] + \
           [dict(eq, _role=f"extra_qualifier_{i}") for i, eq in enumerate(extra_qualifiers)] + \
           [dict(f, _role=f"filler_{i}") for i, f in enumerate(fillers)]
    assert len(pool) == HARD_N_CANDIDATES, len(pool)

    # Перемешиваем, но следим, чтобы победитель не оказался в первых позициях.
    for _reshuffle in range(50):
        rng.shuffle(pool)
        winner_pos = next(i for i, c in enumerate(pool) if c.get("_role") == "winner")
        if winner_pos >= HARD_MIN_WINNER_POSITION:
            break
    for i, c in enumerate(pool, 1):
        c["id"] = f"K{i}"

    pass_counts = [count_pass(c, constraints) for c in pool]
    qualifiers = [c for c, p in zip(pool, pass_counts) if p == 5]
    near_miss = [c for c, p in zip(pool, pass_counts) if p == 4]
    assert len(qualifiers) >= 1, f"hard task {task_idx}: no qualifier at all"
    prices_sorted = sorted(qualifiers, key=lambda c: c["price"])
    cheapest = prices_sorted[0]
    # уникальность минимума цены среди qualifying set
    assert len(prices_sorted) == 1 or prices_sorted[1]["price"] > cheapest["price"], \
        f"hard task {task_idx}: tie on minimal price among qualifiers"
    assert cheapest["_role"] == "winner", \
        f"hard task {task_idx}: cheapest qualifier is not the intended winner ({cheapest['_role']})"
    assert len(near_miss) >= 10, f"hard task {task_idx}: expected >=10 near-miss(4/5), got {len(near_miss)}"

    return {
        "condition": "hard",
        "task_idx": task_idx,
        "candidates": pool,
        "display_attrs": ["cpu", "ram", "storage", "region", "price", "latency"],
        "constraints": constraints,
        "winner_id": cheapest["id"],
        "n_qualifiers": len(qualifiers),
        "near_miss_count": len(near_miss),
    }


def generate_all_tasks_hard(seed=SEED_HARD, n=16):
    rng = random.Random(seed)
    return [generate_task_hard(rng, i) for i in range(n)]


# ---------------------------------------------------------------------------
# 2. Сборка промпта (RU/EN × 4 порядка), общая для easy/hard
# ---------------------------------------------------------------------------

def _fmt_value_ru(v):
    return v if isinstance(v, str) else str(v)


def build_blocks(task, lang):
    labels = ATTR_LABEL_RU if lang == "RU" else ATTR_LABEL_EN
    cand_lines = []
    for c in task["candidates"]:
        parts = [f"{labels[a]}={_fmt_value_ru(c[a])}" for a in task["display_attrs"]]
        cand_lines.append(f"- {c['id']}: " + ", ".join(parts))
    resources_body = "\n".join(cand_lines)

    cons_lines = []
    for i, con in enumerate(task["constraints"], 1):
        attr, op, value = con["attr"], con["op"], con["value"]
        if attr == "derived":
            if lang == "RU":
                cons_lines.append(f"{i}. цена / RAM (цена в у.е. поделить на RAM в ГБ) <= {value}")
            else:
                cons_lines.append(f"{i}. price / RAM (price in units divided by RAM in GB) <= {value}")
            continue
        op_text = {"≥": ">=", ">=": ">=", "<=": "<=", "==": "=", "!=": "≠"}[op]
        cons_lines.append(f"{i}. {labels[attr]} {op_text} {value}")
    constraints_body = "\n".join(cons_lines)

    is_hard = task.get("condition") == "hard"
    if lang == "RU":
        if is_hard:
            task_text = ("ЗАДАЧА:\nСреди конфигураций, которые удовлетворяют ВСЕМ "
                         "ограничениям ниже, выбери САМУЮ ДЕШЁВУЮ (по полю «цена»). "
                         "Конфигурации, не удовлетворяющие хотя бы одному ограничению, "
                         "не рассматриваются, даже если у них низкая цена.")
        else:
            task_text = ("ЗАДАЧА:\nВыбери ровно ОДНУ конфигурацию сервера, которая "
                         "удовлетворяет ВСЕМ ограничениям ниже.")
        return {
            "role": "РОЛЬ:\nТы — технический консультант, выбирающий конфигурацию "
                    "сервера для клиента по заданным требованиям.",
            "resources": f"РЕСУРСЫ/КОНТЕКСТ:\nДоступные конфигурации серверов:\n{resources_body}",
            "task": task_text,
            "constraints": f"ОГРАНИЧЕНИЯ:\n{constraints_body}",
            "format": "ФОРМАТ ОТВЕТА:\nВыведи только идентификатор подходящей "
                       "конфигурации (например: K3). Больше никаких слов, знаков и пояснений.",
        }
    else:
        if is_hard:
            task_text = ("TASK:\nAmong the configurations that satisfy ALL constraints "
                         "below, choose the CHEAPEST one (by the \"price\" field). "
                         "Configurations that fail even one constraint are not "
                         "considered, even if their price is low.")
        else:
            task_text = ("TASK:\nChoose exactly ONE server configuration that satisfies "
                         "ALL constraints below.")
        return {
            "role": "ROLE:\nYou are a technical consultant selecting a server "
                    "configuration for a client based on given requirements.",
            "resources": f"RESOURCES/CONTEXT:\nAvailable server configurations:\n{resources_body}",
            "task": task_text,
            "constraints": f"CONSTRAINTS:\n{constraints_body}",
            "format": "ANSWER FORMAT:\nOutput only the identifier of the matching "
                       "configuration (e.g., K3). No other words, symbols, or explanations.",
        }


def assemble_prompt(task, lang, order_name):
    blocks = build_blocks(task, lang)
    seq = ORDERS[order_name]
    return "\n\n".join(blocks[k] for k in seq)


# ---------------------------------------------------------------------------
# 3. Вызов модели + извлечение ответа
# ---------------------------------------------------------------------------

def call_model(prompt, timeout=CALL_TIMEOUT_S):
    cmd = [
        "claude", "-p", prompt,
        "--model", MODEL,
        "--system-prompt", SYS_PROMPT,
        "--exclude-dynamic-system-prompt-sections",
        "--disallowedTools", DISALLOWED,
    ]
    t0 = time.time()
    try:
        res = subprocess.run(
            cmd, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=timeout
        )
        dt = time.time() - t0
        return {"ok": True, "stdout": res.stdout, "stderr": res.stderr,
                "returncode": res.returncode, "dt": round(dt, 2)}
    except subprocess.TimeoutExpired:
        return {"ok": False, "error": f"timeout after {timeout}s", "dt": round(time.time() - t0, 2)}
    except Exception as e:
        return {"ok": False, "error": repr(e), "dt": round(time.time() - t0, 2)}


ANSWER_RE = re.compile(r"K\s*-?\s*(\d{1,2})", re.IGNORECASE)


def extract_answer(raw):
    if not raw:
        return None
    m = ANSWER_RE.search(raw)
    if not m:
        return None
    return f"K{int(m.group(1))}"


def run_one_call(task, lang, order_name, repeat_idx=0):
    prompt = assemble_prompt(task, lang, order_name)
    prompt_sha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:16]
    attempt_errors = []
    result = None
    for _attempt in range(1, MAX_RETRIES + 2):
        result = call_model(prompt)
        if result["ok"]:
            break
        attempt_errors.append(result.get("error"))
        time.sleep(1.0)
    record = {
        "condition": task["condition"],
        "task_idx": task["task_idx"],
        "lang": lang,
        "order": order_name,
        "repeat_idx": repeat_idx,
        "prompt_sha256": prompt_sha,
        "prompt": prompt,
        "expected": task["winner_id"],
        "call_ok": result["ok"] if result else False,
        "attempt_errors": attempt_errors,
        "dt_s": result.get("dt") if result else None,
    }
    if result and result["ok"]:
        raw_out = result["stdout"].strip()
        extracted = extract_answer(raw_out)
        record["raw_output"] = raw_out
        record["stderr"] = result.get("stderr", "")[:500]
        record["extracted"] = extracted
        record["correct"] = (extracted == task["winner_id"]) if extracted else False
    else:
        record["raw_output"] = None
        record["extracted"] = None
        record["correct"] = None
    return record


# ---------------------------------------------------------------------------
# 4. Запуск сетки
# ---------------------------------------------------------------------------

def run_grid(tasks, cells, repeat_idx=0, jsonl_path=RAW_JSONL, label="", workers=None):
    workers = workers or MAX_WORKERS
    jobs = []
    for order_name, lang in cells:
        for task in tasks:
            jobs.append((task, lang, order_name))

    results = []
    print(f"[{label}] запускаю {len(jobs)} вызовов, concurrency={workers} ...", flush=True)
    t_start = time.time()
    with cf.ThreadPoolExecutor(max_workers=workers) as ex, open(jsonl_path, "a", encoding="utf-8") as fh:
        futs = {
            ex.submit(run_one_call, task, lang, order_name, repeat_idx): (order_name, lang, task["task_idx"])
            for task, lang, order_name in jobs
        }
        done_n = 0
        for fut in cf.as_completed(futs):
            rec = fut.result()
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            results.append(rec)
            done_n += 1
            if done_n % 10 == 0 or done_n == len(jobs):
                print(f"[{label}] {done_n}/{len(jobs)} готово ({time.time()-t_start:.0f}s)", flush=True)
    print(f"[{label}] завершено за {time.time()-t_start:.0f}s", flush=True)
    return results


# ---------------------------------------------------------------------------
# 5. Статистика
# ---------------------------------------------------------------------------

def binom_pmf(k, n, p=0.5):
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def binom_cdf(k, n, p=0.5):
    return sum(binom_pmf(i, n, p) for i in range(0, k + 1))


def mcnemar_exact_p(n01, n10):
    n = n01 + n10
    if n == 0:
        return None
    k = min(n01, n10)
    p_one_side = binom_cdf(k, n, 0.5)
    return min(1.0, 2 * p_one_side)


def wilson_ci(correct, total, z=1.96):
    if total == 0:
        return (None, None)
    p = correct / total
    denom = 1 + z**2 / total
    center = (p + z*z/(2*total)) / denom
    halfwidth = (z * ((p*(1-p)/total + z*z/(4*total*total)) ** 0.5)) / denom
    return (max(0.0, center - halfwidth), min(1.0, center + halfwidth))


def summarize(records, condition):
    main = [r for r in records if r["repeat_idx"] == 0 and r["condition"] == condition]
    cells = sorted(set((r["order"], r["lang"]) for r in main))
    per_task = {}
    cell_counts = {}
    for order, lang in cells:
        sub = [r for r in main if r["order"] == order and r["lang"] == lang]
        valid = [r for r in sub if r["correct"] is not None]
        correct = sum(1 for r in valid if r["correct"])
        cell_counts[(order, lang)] = (correct, len(valid))
        for r in sub:
            per_task[(order, lang, r["task_idx"])] = r["correct"]
    return cells, cell_counts, per_task


def print_easy_report(records):
    print("\n## EASY-CEILING: точность по 4 ячейкам\n")
    cells, cell_counts, _ = summarize(records, "easy")
    print("| order | lang | correct/valid | accuracy |")
    print("|---|---|---|---|")
    for order, lang in cells:
        c, v = cell_counts[(order, lang)]
        acc = f"{c/v*100:.1f}%" if v else "n/a"
        print(f"| {order} | {lang} | {c}/{v} | {acc} |")
    print("\nЕсли все 4 ячейки на/около 100% — вопрос о порядке блоков на этом "
          "условии НЕРАЗРЕШИМ из-за потолка; интерпретируется как отдельный "
          "честный результат ('на простой задаче точного выбора haiku "
          "структура промпта не имеет значения — модель решает её всегда').")


def print_hard_report(tasks, records):
    cells, cell_counts, per_task = summarize(records, "hard")

    print("\n## HARD: точность по 8 ячейкам (порядок × язык)\n")
    print("| order | lang | correct/valid | accuracy |")
    print("|---|---|---|---|")
    for order, lang in cells:
        c, v = cell_counts[(order, lang)]
        acc = f"{c/v*100:.1f}%" if v else "n/a"
        print(f"| {order} | {lang} | {c}/{v} | {acc} |")

    print("\n## HARD: ранжирование порядков внутри RU и внутри EN\n")
    rankings = {}
    for lang in ["RU", "EN"]:
        ranked = sorted(
            [(order, cell_counts[(order, lang)]) for order in ORDERS if (order, lang) in cell_counts],
            key=lambda x: -x[1][0]
        )
        rankings[lang] = ranked
        print(f"{lang}: " + " > ".join(f"{o} ({c}/{v})" for o, (c, v) in ranked))

    print("\n## HARD: разброс лучший-худший порядок внутри каждого языка\n")
    for lang in ["RU", "EN"]:
        accs = [(order, cell_counts[(order, lang)]) for order in ORDERS if (order, lang) in cell_counts]
        best = max(accs, key=lambda x: x[1][0])
        worst = min(accs, key=lambda x: x[1][0])
        diff_tasks = best[1][0] - worst[1][0]
        diff_pp = (best[1][0]/best[1][1] - worst[1][0]/worst[1][1]) * 100 if best[1][1] and worst[1][1] else None
        print(f"{lang}: best={best[0]} ({best[1][0]}/{best[1][1]}), "
              f"worst={worst[0]} ({worst[1][0]}/{worst[1][1]}), "
              f"разница = {diff_tasks} заданий" + (f" (~{diff_pp:.1f} п.п.)" if diff_pp is not None else ""))

    print("\n## HARD: McNemar (точный, парный) — best vs worst внутри каждого языка\n")
    for lang in ["RU", "EN"]:
        accs = [(order, cell_counts[(order, lang)]) for order in ORDERS if (order, lang) in cell_counts]
        best_order = max(accs, key=lambda x: x[1][0])[0]
        worst_order = min(accs, key=lambda x: x[1][0])[0]
        n01 = n10 = 0
        for t in tasks:
            cb = per_task.get((best_order, lang, t["task_idx"]))
            cw = per_task.get((worst_order, lang, t["task_idx"]))
            if cb is None or cw is None:
                continue
            if cb and not cw:
                n10 += 1
            elif cw and not cb:
                n01 += 1
        p = mcnemar_exact_p(n01, n10)
        print(f"{lang}: {best_order} vs {worst_order} -> дискордантные пары: "
              f"best-only-right={n10}, worst-only-right={n01}, "
              f"McNemar exact p={'n/a (0 дискордантных пар)' if p is None else f'{p:.3f}'}")

    print("\n## HARD: биномиальный 95% CI по каждой ячейке (Wilson)\n")
    for order, lang in cells:
        c, v = cell_counts[(order, lang)]
        lo, hi = wilson_ci(c, v)
        if lo is None:
            print(f"{order}/{lang}: n/a")
        else:
            print(f"{order}/{lang}: {c}/{v} = {c/v*100:.1f}%, 95% CI [{lo*100:.1f}%, {hi*100:.1f}%]")

    print("\n## HARD: согласие знаков разницы между RU и EN по всем 6 парам порядков\n")
    order_names = list(ORDERS.keys())
    agree = 0
    total_pairs = 0
    for i in range(len(order_names)):
        for j in range(i + 1, len(order_names)):
            oa, ob = order_names[i], order_names[j]
            if (oa, "RU") not in cell_counts or (ob, "RU") not in cell_counts:
                continue
            ru_diff = cell_counts[(oa, "RU")][0] - cell_counts[(ob, "RU")][0]
            en_diff = cell_counts[(oa, "EN")][0] - cell_counts[(ob, "EN")][0]
            same_sign = (ru_diff == 0 and en_diff == 0) or (ru_diff * en_diff > 0)
            total_pairs += 1
            if same_sign:
                agree += 1
            print(f"  {oa} vs {ob}: RU diff={ru_diff:+d} заданий, EN diff={en_diff:+d} заданий, "
                  f"{'согласуются' if same_sign else 'РАСХОДЯТСЯ'}")
    print(f"\nИтого согласующихся по знаку пар: {agree}/{total_pairs}")

    print("\n## HARD: повторные прогоны (оценка шума прогона-к-прогону)\n")
    repeats = [r for r in records if r["repeat_idx"] == 1 and r["condition"] == "hard"]
    if not repeats:
        print("Повторные прогоны отсутствуют в накопленных данных.")
    else:
        for order, lang in REPEAT_CELLS_HARD:
            sub1 = [r for r in records if r["order"] == order and r["lang"] == lang
                    and r["repeat_idx"] == 0 and r["condition"] == "hard"]
            sub2 = [r for r in records if r["order"] == order and r["lang"] == lang
                    and r["repeat_idx"] == 1 and r["condition"] == "hard"]
            v1 = [r for r in sub1 if r["correct"] is not None]
            v2 = [r for r in sub2 if r["correct"] is not None]
            c1 = sum(1 for r in v1 if r["correct"])
            c2 = sum(1 for r in v2 if r["correct"])
            print(f"{order}/{lang}: run1 = {c1}/{len(v1)}, run2 = {c2}/{len(v2)}, "
                  f"разница = {c1-c2:+d} заданий (прогон-к-прогону шум при идентичных промптах)")


# ---------------------------------------------------------------------------
# 6. main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pilot-hard", action="store_true", help="калибровка hard: N_HARD заданий, RU/role_first")
    ap.add_argument("--easy-ceiling", action="store_true", help="4 ячейки easy (ceiling-baseline)")
    ap.add_argument("--full-hard", action="store_true", help="полная сетка hard: 8 ячеек x N_HARD + 2 повторные")
    ap.add_argument("--report-only", action="store_true", help="пересчитать отчёт из уже накопленного raw jsonl")
    ap.add_argument("--workers", type=int, default=MAX_WORKERS, help="concurrency для run_grid")
    ap.add_argument("--n-hard", type=int, default=16, help="число заданий hard (протокол калибровки: 16)")
    args = ap.parse_args()

    print("# prompt-structure-experiment.py — вывод прогона")
    print(f"Дата/время запуска (UTC): {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    print(f"SEED_EASY={SEED_EASY}, SEED_HARD={SEED_HARD}, N_TASKS_EASY={N_TASKS}, "
          f"N_HARD={args.n_hard}, MODEL={MODEL}, WORKERS={args.workers}")
    try:
        v = subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=10)
        print(f"claude CLI version: {v.stdout.strip()}")
    except Exception as e:
        print(f"claude CLI version: n/a ({e!r})")
    print()

    easy_tasks = generate_all_tasks_easy()
    hard_tasks = generate_all_tasks_hard(n=args.n_hard)
    print(f"EASY: сгенерировано {len(easy_tasks)} заданий, "
          f"near-miss avg={sum(t['near_miss_count'] for t in easy_tasks)/len(easy_tasks):.2f}")
    print(f"HARD: сгенерировано {len(hard_tasks)} заданий, "
          f"near-miss avg={sum(t['near_miss_count'] for t in hard_tasks)/len(hard_tasks):.2f}, "
          f"qualifiers avg={sum(t['n_qualifiers'] for t in hard_tasks)/len(hard_tasks):.2f}")

    if args.report_only:
        records = []
        with open(RAW_JSONL, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        if any(r["condition"] == "easy" for r in records):
            print_easy_report(records)
        if any(r["condition"] == "hard" for r in records):
            print_hard_report(hard_tasks, records)
        return

    if args.pilot_hard:
        records = run_grid(hard_tasks, [("role_first", "RU")], repeat_idx=0,
                            label="pilot-hard", workers=args.workers)
        valid = [r for r in records if r["correct"] is not None]
        correct = sum(1 for r in valid if r["correct"])
        acc = correct/len(valid)*100 if valid else 0
        print(f"\nКАЛИБРОВКА hard role_first/RU: {correct}/{len(valid)} = "
              f"{acc:.1f}% (валидных {len(valid)}/{len(records)})")
        if acc >= 90:
            print("РЕШЕНИЕ: >=90% -> СТОП. Полную сетку НЕ гнать (правило остановки, см. отчёт).")
        elif acc < 45:
            print("РЕШЕНИЕ: <45% -> ослабить до 40 кандидатов и повторить калибровку ОДИН раз.")
        else:
            print("РЕШЕНИЕ: 45-88% -> зафиксировать seed, гнать полную сетку --full-hard на этом N.")
        return

    if args.easy_ceiling:
        records = run_grid(easy_tasks, EASY_CEILING_CELLS, repeat_idx=0,
                            label="easy-ceiling", workers=args.workers)
        print_easy_report(records)
        return

    if args.full_hard:
        all_cells = [(order, lang) for order in ORDERS for lang in ["RU", "EN"]]
        records = run_grid(hard_tasks, all_cells, repeat_idx=0, label="hard-main-grid", workers=args.workers)
        repeat_records = run_grid(hard_tasks, REPEAT_CELLS_HARD, repeat_idx=1,
                                   label="hard-repeat-cells", workers=args.workers)
        print_hard_report(hard_tasks, records + repeat_records)
        return

    print("Укажите --pilot-hard, --easy-ceiling, --full-hard или --report-only. См. --help.")


if __name__ == "__main__":
    main()
