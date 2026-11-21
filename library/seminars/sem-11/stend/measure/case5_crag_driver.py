"""Семинар 11, Кейс 5 — самокоррекция поиска (CRAG-форма). Прогоняет РЕАЛЬНЫЙ,
опубликованный n8n-сценарий «С11 · Кейс 5 — CRAG грейдер + условная ветка (демо-экран)»
(`sborka_case5.py`, webhook `s11-case5-crag`) на трёх типах вопросов, как того требует
задача ARCHITECTURE.md (не три прогона одного и того же вопроса):

  (a) вопрос, явно покрытый источником А, сформулированный близко к тексту —
      ожидание: грейдер CORRECT, прямой ответ.
  (b) вопрос вне покрытия ОБОИХ источников, но тематически близкий к источнику А —
      цель: проверить, не пропустит ли грейдер тематически близкий, но не отвечающий
      по существу кусок как CORRECT (ложноположительный провал, §4.1 п.2 брифа).
  (c) вопрос, покрытый источником А, но сформулированный другими словами, чем текст —
      цель: проверить, не зависает ли грейдер в цикле переформулировки; явный счётчик
      максимум 2 повтора (как в реальном случае Dharshiny5 и в официальном примере
      LangGraph, бриф §2) — цикл НЕ без ограничения.

Счётчик итераций и переформулировка — на стороне ЭТОГО драйвера (роль «агента», который
в реальном проекте вызывает retrieval-sub-workflow как инструмент; сам n8n-сценарий решает
только ОДИН шаг «поиск → грейд → ветка» за вызов, без цикла внутри себя — см. docstring
`sborka_case5.py`).

Корпус — источник А: кластер «Сибирь» (cluster3-1..5), источник Б: кластер «Дилан»
(cluster5-1..4), `corpus/corpus_case1_s10.json` (реальные документы SberQuAD, тот же
корпус, что Кейсы 1/3 Семинара 10 — не придуманный текст).
"""
import json
import sys
import time
import urllib.parse

sys.path.insert(0, ".")
from harness_call import post_form, get_execution

CORPUS_PATH = "../corpus/corpus_case1_s10.json"
SOURCE_A_IDS = ["cluster3-1", "cluster3-2", "cluster3-3", "cluster3-4", "cluster3-5"]
SOURCE_B_IDS = ["cluster5-1", "cluster5-2", "cluster5-3", "cluster5-4"]

data = json.load(open(CORPUS_PATH, encoding="utf-8"))
by_id = {c["id"]: c for c in data["corpus_500"]}
SOURCE_A = [{"id": cid, "text": by_id[cid]["text"]} for cid in SOURCE_A_IDS]
SOURCE_B = [{"id": cid, "text": by_id[cid]["text"]} for cid in SOURCE_B_IDS]

QUESTIONS = {
    "a_in_coverage_close_wording": {
        "label": "(a) покрыт источником А, формулировка близка к тексту",
        "question": (
            "В каком году в Иркутском остроге была построена первая деревянная церковь — "
            "Спасская, и в этом же году заложен мужской Вознесенский монастырь?"
        ),
        "expectation": "ожидание: грейдер CORRECT, прямой ответ (cluster3-5)",
        "max_iterations": 1,
    },
    "b_out_of_coverage_near_topic": {
        "label": "(b) вне покрытия обоих источников, тематически близко к источнику А — "
                  "ТРУДНЫЙ вариант (§8.11 канона): высокое совпадение сущностей "
                  "(«окунь» + «Куйбышевском водохранилище» буквально есть в тексте), "
                  "но конкретное число, которое спрашивает вопрос, в тексте нет",
        "question": (
            "Сколько окуня в тоннах ежегодно вылавливают в Куйбышевском водохранилище?"
        ),
        "easy_variant_question": (
            "Какие виды хвойных деревьев преобладают в тайге Западной Сибири, и сколько "
            "древесины ежегодно заготавливают в этом районе?"
        ),
        "expectation": (
            "цель — проверить, не пропустит ли грейдер тематически близкий / "
            "сущностно-совпадающий, но не отвечающий по существу (нет числа в тоннах) кусок "
            "как CORRECT (ложноположительный провал, §4.1 п.2 брифа, SHAP-находка про "
            "named-entity-alignment грейдер)"
        ),
        "max_iterations": 1,
    },
    "c_in_coverage_reworded": {
        "label": "(c) покрыт источником А, но сформулирован другими словами — найден реальный "
                  "AMBIGUOUS-кейс после честного перебора (9 формулировок, см. notes/decisions.md)",
        "question": (
            "Эффективен ли промысел данного вида рыбы по сравнению с другими обитателями тех "
            "же водоёмов?"
        ),
        "reformulations": [
            # итерация 2 — ближе к словам источника (окунь/Сибирь/озёра/гектар), реально
            # проверено заранее: overlap=5, verdict=CORRECT (не подогнано post-hoc под нужный
            # исход — зафиксировано вместе с этим файлом в driver-пробах)
            (
                "Какова продуктивность окуня в северных озёрах Сибири в пересчёте на "
                "единицу площади водоёма?"
            ),
        ],
        "expectation": (
            "цель — проверить, не зависает ли грейдер в цикле переформулировки; счётчик "
            "ограничен максимум 2 повторами (исходный вопрос + 1 переформулировка), как в "
            "реальном случае Dharshiny5 и в официальном примере LangGraph (бриф §2)"
        ),
        "max_iterations": 2,
    },
}


def call_case5(question, iteration=1, reformulated=False, timeout=120):
    payload = {
        "question": question,
        "source_a": SOURCE_A,
        "source_b": SOURCE_B,
        "iteration": iteration,
        "reformulated": reformulated,
    }
    t0 = time.time()
    resp = post_form("s11-case5-crag", [json.dumps(payload, ensure_ascii=False)])
    waiting = resp.get("formWaitingUrl", "")
    exec_id = urllib.parse.urlparse(waiting).path.rstrip("/").split("/")[-1]
    deadline = time.time() + timeout
    run = {}
    ex = {}
    while time.time() < deadline:
        time.sleep(1.5)
        try:
            ex = get_execution(exec_id)
        except Exception:
            continue
        run = ex.get("data", {}).get("resultData", {}).get("runData", {})
        for candidate in (
            "Использовать как есть (источник-1)",
            "Откат на источник Б (keyword, top-1)",
            "Переформулировать и повторить (источник-1, refined)",
        ):
            if candidate in run:
                entry = run[candidate][0]
                try:
                    out = entry["data"]["main"][0][0]["json"]
                except Exception:
                    out = {"_entry_error": entry.get("error")}
                return {
                    "exec_id": exec_id, "wall_s": round(time.time() - t0, 2),
                    "branch_node": candidate, "result": out, "full_execution": ex,
                }
    return {"exec_id": exec_id, "wall_s": round(time.time() - t0, 2),
            "branch_node": None, "result": None, "full_execution": ex,
            "error": "timeout — ни одна из трёх ветвей не вернула runData за отведённое время"}


def run_easy_variant_probe(key, spec):
    """§8.11 канона: прежде чем предъявить «ноль» (грейдер не дал ложноположительный
    CORRECT), сначала честно прогнать и записать ЛЁГКИЙ вариант того же вопроса — отдельно
    от официального трудного прогона ниже, обе записи предъявляются."""
    q = spec.get("easy_variant_question")
    if not q:
        return None
    r = call_case5(q, iteration=1)
    result = r.get("result") or {}
    print(f"  [лёгкий вариант, для сравнения] вопрос: {q}")
    print(f"    exec_id={r['exec_id']} verdict={result.get('grader_verdict')!r} "
          f"top_doc={result.get('top_doc_id')} overlap={result.get('top_overlap')} "
          f"reason={result.get('grader_reason')!r}")
    return {
        "question": q, "exec_id": r["exec_id"], "wall_s": r["wall_s"],
        "grader_verdict": result.get("grader_verdict"),
        "grader_reason": result.get("grader_reason"),
        "top_doc_id": result.get("top_doc_id"), "top_overlap": result.get("top_overlap"),
        "fallback_doc_id": result.get("fallback_doc_id"),
    }


def run_case(key, spec):
    print(f"\n=== {key}: {spec['label']} ===")
    easy_probe = run_easy_variant_probe(key, spec)
    print(f"вопрос (итерация 1, официальный/трудный прогон): {spec['question']}")
    attempts = []
    question = spec["question"]
    reformulated = False
    iteration = 1
    max_iter = spec["max_iterations"]
    while True:
        r = call_case5(question, iteration=iteration, reformulated=reformulated)
        branch = r.get("branch_node")
        result = r.get("result") or {}
        verdict = result.get("grader_verdict")
        reason = result.get("grader_reason")
        print(f"  попытка {iteration}: exec_id={r['exec_id']} wall={r['wall_s']}с "
              f"branch={branch!r} verdict={verdict!r} reason={reason!r}")
        attempts.append({
            "iteration": iteration,
            "question_this_attempt": question,
            "exec_id": r["exec_id"],
            "wall_s": r["wall_s"],
            "branch_node": branch,
            "grader_verdict": verdict,
            "grader_reason": reason,
            "grader_raw": result.get("grader_raw"),
            "top_doc_id": result.get("top_doc_id"),
            "top_overlap": result.get("top_overlap"),
            "fallback_doc_id": result.get("fallback_doc_id"),
            "fallback_overlap": result.get("fallback_overlap"),
            "final_tag": result.get("final_tag"),
            "final_text": result.get("final_text"),
            "error": r.get("error"),
        })
        needs_retry = bool(result.get("needs_retry"))
        if not needs_retry or iteration >= max_iter:
            stopped_reason = (
                "ответ получен (CORRECT/INCORRECT — не нужен повтор)" if not needs_retry else
                f"упёрлись в лимит итераций ({max_iter}) — AMBIGUOUS не разрешён, "
                f"ответ НЕ ВОЗВРАЩЁН пользователю (та же тишина, что в реальном случае Dharshiny5)"
            )
            print(f"  стоп: {stopped_reason}")
            return {
                "key": key, "label": spec["label"], "expectation": spec["expectation"],
                "easy_variant_probe": easy_probe,
                "attempts": attempts, "stopped_reason": stopped_reason,
                "final_verdict_sequence": [a["grader_verdict"] for a in attempts],
                "resolved": not needs_retry,
            }
        # нужен повтор — переформулировка (из заранее заготовленного списка, не изобретённая
        # на лету post-hoc: см. QUESTIONS[key]["reformulations"])
        reform_list = spec.get("reformulations", [])
        next_idx = iteration - 1  # после итерации 1 берём reform_list[0], и т.д.
        if next_idx >= len(reform_list):
            print("  переформулировок не осталось в заготовленном списке — останов")
            return {
                "key": key, "label": spec["label"], "expectation": spec["expectation"],
                "attempts": attempts,
                "stopped_reason": "переформулировок не осталось раньше, чем лимит итераций",
                "final_verdict_sequence": [a["grader_verdict"] for a in attempts],
                "resolved": False,
            }
        question = reform_list[next_idx]
        reformulated = True
        iteration += 1
        print(f"  AMBIGUOUS → переформулировка (попытка {iteration}): {question}")


if __name__ == "__main__":
    all_results = {}
    for key, spec in QUESTIONS.items():
        all_results[key] = run_case(key, spec)

    out = {
        "workflow": "С11 · Кейс 5 — CRAG грейдер + условная ветка (демо-экран)",
        "webhook": "s11-case5-crag",
        "corpus": {
            "source_a": {"cluster": "Сибирь (cluster3-1..5)", "ids": SOURCE_A_IDS},
            "source_b": {"cluster": "Дилан (cluster5-1..4)", "ids": SOURCE_B_IDS},
        },
        "cases": all_results,
    }
    json.dump(out, open("case5_crag_driver_raw.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print("\n\nсвод записан в case5_crag_driver_raw.json (рабочий файл, не коммитится напрямую — "
          "копируется в ../case5-results.json после прогона)")
    print(json.dumps(
        {k: {"resolved": v["resolved"], "verdicts": v["final_verdict_sequence"],
             "stopped_reason": v["stopped_reason"]} for k, v in all_results.items()},
        ensure_ascii=False, indent=2))
