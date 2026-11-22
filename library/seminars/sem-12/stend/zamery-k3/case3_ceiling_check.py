#!/usr/bin/env python3
"""Потолок задачи «поиск признака» — по требованию оркестратора после отчёта о
recall@1 = 0,333/0,20 контрольной текстовой ветки.

Вопрос: строка-запрос («CASH 91000», «4,000», «10») физически может встречаться
в нескольких чеках корпуса одновременно — тогда даже идеальный метод не обязан
угадать именно тот чек, из которого запрос вырезан. Если так, низкое recall@1
текстовой ветки — не свойство метода поиска, а свойство самого вопроса (у него
нет единственного верного ответа).

Без новых вызовов модели: берём те же 60 запросов (`line_text` из
`case3_tiles_vs_whole_results.json`) и тот же корпус (`ocr_text` всех 30 чеков
из `cord_sample_meta.json`), считаем для каждого запроса, в скольких чеках
корпуса строка встречается как отдельный токен (границы — не цифра/буква/запятая/
точка с обеих сторон, чтобы «10» не засчитывался внутри «100,000»).

Потолок = доля запросов, у которых ровно один чек-кандидат (сам источник).

    cd library/seminars/sem-12/stend/zamery-k3
    python3 case3_ceiling_check.py
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
CORPUS_META = HERE / "../../../sem-10/stend/corpus/cord_sample_meta.json"
QUERIES = HERE / "raw/case3_tiles_vs_whole_results.json"
OUT = HERE / "raw/case3_ceiling_check_results.json"


def token_match(query_text: str, haystack: str) -> bool:
    pat = re.escape(query_text.strip())
    return re.search(r"(?<![0-9A-Za-z.,])" + pat + r"(?![0-9A-Za-z.,])", haystack) is not None


def analyze(queries, ocr_by_id):
    rows = []
    n_unique = 0
    for q in queries:
        text = q["line_text"].strip()
        sid = q["source_id"]
        matches = sorted(rid for rid, o in ocr_by_id.items() if token_match(text, o))
        is_unique = len(matches) == 1
        if is_unique:
            n_unique += 1
        rows.append({
            "source_id": sid,
            "line_text": text,
            "n_matching_receipts": len(matches),
            "matching_receipts": matches,
            "unique_answer": is_unique,
        })
    return rows, n_unique


def main():
    meta = json.loads(CORPUS_META.read_text(encoding="utf-8"))
    ocr_by_id = {r["id"]: r["ocr_text"] for r in meta}
    res = json.loads(QUERIES.read_text(encoding="utf-8"))

    rows_easy, n_easy = analyze(res["details_easy"], ocr_by_id)
    rows_hard, n_hard = analyze(res["details_hard"], ocr_by_id)

    out = {
        "purpose": ("Потолок задачи: доля из 60 запросов (30 лёгких + 30 трудных, те же, "
                    "что в case3_tiles_vs_whole_results.json и case3_text_control_results.json), "
                    "у которых строка-запрос встречается РОВНО в одном чеке корпуса (значит у "
                    "вопроса физически есть единственный верный ответ). Совпадение — по границе "
                    "токена: строка не засчитывается, если она часть более длинного числа."),
        "method": "re.search с lookaround по не-алфанумерик/,/. с обеих сторон, без новых вызовов модели/API",
        "n_matches_easy": n_easy,
        "n_matches_hard": n_hard,
        "n_total": len(res["details_easy"]) + len(res["details_hard"]),
        "ceiling_easy": n_easy / len(res["details_easy"]),
        "ceiling_hard": n_hard / len(res["details_hard"]),
        "ceiling_combined": (n_easy + n_hard) / (len(res["details_easy"]) + len(res["details_hard"])),
        "details_easy": rows_easy,
        "details_hard": rows_hard,
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Потолок (лёгкий): {n_easy}/{len(rows_easy)} = {out['ceiling_easy']:.4f}")
    print(f"Потолок (трудный): {n_hard}/{len(rows_hard)} = {out['ceiling_hard']:.4f}")
    print(f"Потолок (всего): {out['ceiling_combined']:.4f}")
    print(f"Записано: {OUT}")


if __name__ == "__main__":
    main()
