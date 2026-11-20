#!/usr/bin/env python3
"""Консолидация batch2 (volna 3) в reestr-reshenij-verified.csv (#349, файл 18).

Один проход: парсит 12 файлов verified-cases-batch2/lec-NN-verified-batch2.md
(5 разных форматов таблиц), нормализует к 18-колоночной схеме verified-реестра,
валидирует каждый enum против словаря reestr-reshenij-README.md, дедуплицирует
против (а) текущего verified (289), (б) original (421), (в) внутри batch2,
присваивает финальные ID V{NN}-{след. свободный} и — в режиме --write —
дописывает строки в reestr-reshenij-verified.csv (конкатенация, не перезапись).

Без --write только печатает отчёт (кандидаты, нарушения словаря, дубли).
"""
import csv
import os
import re
import sys
import unicodedata
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
B2DIR = os.path.join(HERE, "verified-cases-batch2")
VER_CSV = os.path.join(HERE, "reestr-reshenij-verified.csv")
ORIG_CSV = os.path.join(HERE, "reestr-reshenij.csv")

INDUSTRY = {4: "sdlc", 5: "product-lifecycle", 6: "cad-cam", 7: "medical-decision",
            8: "trust-recognition", 9: "frontier-space", 10: "agriculture",
            11: "manufacturing", 12: "digital-twins", 13: "logistics",
            14: "telecom-cybersecurity", 15: "scientific-research"}

ENUMS = {
    "axis1_level": {"low", "moderate", "high", "extreme", "unclear"},
    "axis1_mechanism": {"U1", "U2", "U3", "U4", "none", "unclear"},
    "axis2_bucket": {"seconds-minutes", "hours-days", "weeks-months", "season-years",
                     "unclear"},
    "axis2_mechanism": {"F-A", "F-B", "F-C", "none", "unclear"},
    "axis3_class": {"rule-based", "classical-ml", "deep-learning", "foundation-model",
                    "agentic-llm", "sensor-fusion", "hybrid", "unclear"},
    "axis4_gate": {"yes", "no", "not-applicable", "unclear"},
    "axis4_blast_radius": {"low", "medium", "high", "catastrophic", "unclear"},
    "external_driver": {"yes", "no", "mixed", "not-applicable", "unclear"},
    "outcome": {"success", "partial", "failure", "undetermined"},
    "confidence": {"high", "medium", "low"},
}

AXES_FIELDS = list(ENUMS.keys())

# ---- Решения ручного ревью дублей (обоснование — файл 18 §1) ----
# Ложные URL-дубли: РАЗНЫЕ кейсы, делящие один источник (агрегирующая страница/
# отчёт, Wikipedia-обзор, один репорт с несколькими инцидентами) — оставить.
FALSE_URL_DUP_KEEP = {
    (5, "FlavorMind"), (5, "Cadence Cerebrus"), (5, "Shake Shack × NotCo"),
    (6, "Neural Concept × General Motors"), (9, "Saildrone — беспилотный дрон внутри урагана"),
    (13, "TuSimple — первый в мире полностью безводительский"),
    (13, "Kiwibot — раскрытие ручного теле-управления"),
    (13, "Attabotics — массовые увольнения"),
    (14, "Anthropic GTG-15001"), (14, "Anthropic GTG-50014"),
    (14, "Anthropic — один консультант построил платформу слежки"),
}
# Настоящие дубли одного и того же события, пойманные только similarity-ревью
# (имя сформулировано иначе, URL другой) — исключить с причиной.
EXTRA_EXCLUDE = {
    (11, "Rethink Robotics — закрытие"): "то же событие, что L11-015 (закрытие Rethink 2018)",
    (5, "GM × Autodesk — генеративный дизайн кронштейна"): "тот же кейс, что L06-001 (GM seat bracket, Autodesk 2018)",
    (8, "Retool/Fortress Trust"): "то же событие, что V14-013 (Retool, 08.2023)",
    (8, "WPP — попытка дипфейк-атаки"): "то же событие, что L14-071 (WPP deepfake, май 2024)",
    (11, "Tesla Model 3 — «избыточная автоматизация»"): "то же событие, что L11-001/L12-001 (Tesla 2018 over-automation)",
    (11, "Arrival — банкротство"): "тот же крах, что V12-017 (Arrival «микрофабрики»)",
    (13, "Covariant — «неэксклюзивная» сделка"): "то же событие, что V11-012 (Covariant↔Amazon reverse acqui-hire)",
    (14, "NYC MyCity чат-бот"): "тот же кейс, что L05-028 (NYC MyCity)",
    (15, "AlphaFold2 (DeepMind)"): "часть дуги L15-001 (CASP14 входит в описание L15-001)",
    (15, "AlphaFold3 (Google DeepMind"): "часть дуги L15-001 (AF3 входит в описание L15-001)",
    (12, "Rolls-Royce — IntelligentEngine digital twin"): "та же программа, что V11-004 (IntelligentEngine/Azure)",
    (9, "NASA/JPL — отчёт по первым 4 годам AEGIS"): "тот же кейс/исход, что L09-001 (AEGIS), другой артефакт",
    (15, "GNoME (DeepMind)"): "тот же кейс, что L15-011 (GNoME, Nature 2023)",
    (15, "Pangu-Weather (Huawei)"): "тот же кейс, что короткое упоминание L09-032",
}
# Нарушения enum «not-applicable» в колонках, где словарь его не допускает —
# та же категория институциональных кейсов, что V04-016/V11-011 волны 1 → unclear.
ENUM_FIXUP_TO_UNCLEAR = {
    (4, "Software Freedom Conservancy", "axis1_level"),
    (4, "Builder.ai", "axis1_level"),
    (10, "Microsoft Azure Data Manager for Agriculture", "axis1_level"),
    (10, "Microsoft Azure Data Manager for Agriculture", "axis2_bucket"),
}


def match_key(rec, keyset_or_dict):
    for k in keyset_or_dict:
        if k[0] == rec["lecture_num"] and rec["case_name"].startswith(k[1]):
            return k
    return None


def clean(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace("**", "").replace("`", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def norm_name(s):
    s = clean(s).lower()
    return re.sub(r"[^0-9a-zа-яё]+", "", s)


def norm_url(u):
    u = u.strip().rstrip("/").lower()
    u = re.sub(r"^https?://(www\.)?", "", u)
    return u


def header_map(cells):
    """Канонизирует имена колонок заголовка таблицы; None = неизвестная."""
    out = []
    for c in cells:
        c0 = clean(c).lower()
        if c0 in ("#", "id"):
            out.append("local")
        elif c0 == "case_name":
            out.append("case_name")
        elif c0 == "year":
            out.append("year")
        elif c0 == "source_url":
            out.append("source_url")
        elif c0 == "industry":
            out.append("industry")
        elif c0.startswith("описание") or c0.startswith("что произошло"):
            out.append("desc")
        elif c0 == "axis1_level / mechanism":
            out.append("axis1_pair")
        elif c0 == "axis2_bucket / mechanism":
            out.append("axis2_pair")
        elif c0 == "axis4_gate / blast_radius":
            out.append("axis4_pair")
        elif c0 in [f.lower() for f in AXES_FIELDS]:
            out.append([f for f in AXES_FIELDS if f.lower() == c0][0])
        else:
            out.append(None)
    return out


def parse_file(nn):
    path = os.path.join(B2DIR, f"lec-{nn:02d}-verified-batch2.md")
    rows = []
    tbl = []
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        ls = lines[i].strip()
        if ls.startswith("|"):
            # собрать таблицу целиком
            tbl = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i].strip())
                i += 1
            if len(tbl) < 3:
                continue
            # ячейки: учитываем экранированный \| внутри текста
            def split_row(line):
                parts = re.split(r"(?<!\\)\|", line.strip().strip("|"))
                return [p.replace("\\|", "|").strip() for p in parts]
            hdr = header_map(split_row(tbl[0]))
            if "case_name" not in hdr or not any(
                    h in hdr for h in ("axis1_level", "axis1_pair")):
                continue  # не кейс-таблица (сводки, отклонённые кандидаты)
            for line in tbl[2:]:
                cells = split_row(line)
                if len(cells) != len(hdr):
                    print(f"  !! lec-{nn:02d}: строка с {len(cells)} ячейками при "
                          f"{len(hdr)} в заголовке: {cells[0][:60]}…")
                    continue
                rec = {"lecture_num": nn}
                for h, v in zip(hdr, cells):
                    if h is None or h == "desc":
                        continue
                    v = clean(v)
                    if h == "axis1_pair":
                        a, _, b = v.partition("/")
                        rec["axis1_level"], rec["axis1_mechanism"] = a.strip(), b.strip()
                    elif h == "axis2_pair":
                        a, _, b = v.partition("/")
                        rec["axis2_bucket"], rec["axis2_mechanism"] = a.strip(), b.strip()
                    elif h == "axis4_pair":
                        a, _, b = v.partition("/")
                        rec["axis4_gate"], rec["axis4_blast_radius"] = a.strip(), b.strip()
                    else:
                        rec[h] = v
                rows.append(rec)
        else:
            i += 1
    return rows


def main(write=False):
    all_recs = []
    for nn in range(4, 16):
        recs = parse_file(nn)
        print(f"lec-{nn:02d}: {len(recs)} строк из batch2-таблиц")
        all_recs.extend(recs)
    print(f"ИТОГО распарсено: {len(all_recs)}")

    # нормализация year / source_url
    issues = []
    for r in all_recs:
        y = r.get("year", "")
        m = re.search(r"\b(19[5-9]\d|20[0-2]\d)\b", y)
        if not m:
            issues.append(("year", r["lecture_num"], r["case_name"], y))
            r["year_final"] = ""
        else:
            r["year_final"] = m.group(1)
            if y != m.group(1):
                r.setdefault("notes", []).append(f"year как в источнике: «{y}»")
        u = r.get("source_url", "")
        mu = re.search(r"https?://[^\s\)\]]+", u)
        if not mu:
            issues.append(("source_url", r["lecture_num"], r["case_name"], u[:60]))
            r["url_final"] = ""
        else:
            r["url_final"] = mu.group(0).rstrip(").,;")
            if len(re.findall(r"https?://", u)) > 1:
                r.setdefault("notes", []).append("в источнике >1 URL, взят первый")
        # industry из lec-11-таблицы — сверить со словарём лекции
        if "industry" in r and r["industry"] and r["industry"] != INDUSTRY[r["lecture_num"]]:
            issues.append(("industry", r["lecture_num"], r["case_name"], r["industry"]))

    # валидация enum (+ санкционированные fixup'ы not-applicable → unclear)
    enum_viol = []
    for r in all_recs:
        for f in AXES_FIELDS:
            v = r.get(f, "")
            if v not in ENUMS[f]:
                fk = next((k for k in ENUM_FIXUP_TO_UNCLEAR
                           if k[0] == r["lecture_num"]
                           and r["case_name"].startswith(k[1]) and k[2] == f), None)
                if fk and v == "not-applicable":
                    r[f] = "unclear"
                    r.setdefault("notes", []).append(f"{f}: not-applicable→unclear")
                else:
                    enum_viol.append((r["lecture_num"], r["case_name"][:55], f, v))
    print(f"\nНарушения enum-словаря (после fixup'ов): {len(enum_viol)}")
    for e in enum_viol:
        print("  VIOL:", e)
    print(f"Проблемы year/source_url/industry: {len(issues)}")
    for e in issues:
        print("  ISSUE:", e)

    # дедуп
    ver = list(csv.DictReader(open(VER_CSV, encoding="utf-8")))
    orig = list(csv.DictReader(open(ORIG_CSV, encoding="utf-8")))
    ver_names = {norm_name(r["case_name"]): r["id"] for r in ver}
    ver_urls = {norm_url(r["source_url"]): r["id"] for r in ver if r["source_url"]}
    orig_names = {norm_name(r["case_name"]): r["id"] for r in orig}
    dups, seen_b2_names, seen_b2_urls = [], {}, {}
    kept = []
    for r in all_recs:
        nm, ur = norm_name(r["case_name"]), norm_url(r["url_final"])
        key = f"lec-{r['lecture_num']:02d}: {r['case_name'][:60]}"
        xk = match_key(r, EXTRA_EXCLUDE)
        if xk:
            dups.append((key, "manual same-event", EXTRA_EXCLUDE[xk])); continue
        url_exempt = match_key(r, FALSE_URL_DUP_KEEP) is not None
        if nm in ver_names:
            dups.append((key, "verified name", ver_names[nm])); continue
        if ur and ur in ver_urls and not url_exempt:
            dups.append((key, "verified url", ver_urls[ur])); continue
        if nm in orig_names:
            dups.append((key, "original name", orig_names[nm])); continue
        if nm in seen_b2_names:
            dups.append((key, "batch2-internal name", seen_b2_names[nm])); continue
        if ur and ur in seen_b2_urls and not url_exempt:
            dups.append((key, "batch2-internal url", seen_b2_urls[ur])); continue
        seen_b2_names[nm] = key
        if ur:
            seen_b2_urls.setdefault(ur, key)
        kept.append(r)
    print(f"\nТочные дубли (исключены): {len(dups)}")
    for d in dups:
        print("  DUP:", d)
    print(f"Остаётся к добавлению: {len(kept)}")

    # кандидаты в «похожие» (для ручного ревью, не авто-исключение):
    def tokens(s):
        return {t for t in re.findall(r"[0-9a-zа-яё]{4,}", clean(s).lower())
                if t not in ("case", "study")}
    near = []
    for r in kept:
        tt = tokens(r["case_name"])
        for pool, tag in ((ver, "verified"), (orig, "original")):
            for p in pool:
                ov = tt & tokens(p["case_name"])
                if len(ov) >= 2 and len(ov) >= 0.6 * min(len(tt), len(tokens(p["case_name"]))):
                    near.append((f"lec-{r['lecture_num']:02d}", r["case_name"][:60],
                                 tag, p["id"], p["case_name"][:60], sorted(ov)))
    print(f"\nПохожие пары на ручное ревью: {len(near)}")
    for n_ in near:
        print("  NEAR:", n_)

    if not write:
        print("\n(dry-run: --write не указан, CSV не изменён)")
        return

    # присвоение ID и запись
    mx = defaultdict(int)
    for r in ver:
        m = re.match(r"V(\d+)-(\d+)", r["id"])
        mx[int(m.group(1))] = max(mx[int(m.group(1))], int(m.group(2)))
    out_rows = []
    for r in kept:
        nn = r["lecture_num"]
        mx[nn] += 1
        rid = f"V{nn:02d}-{mx[nn]:03d}"
        out_rows.append({
            "id": rid, "lecture_num": str(nn), "industry": INDUSTRY[nn],
            "case_name": r["case_name"], "year": r["year_final"],
            "source_url": r["url_final"],
            **{f: r.get(f, "") for f in AXES_FIELDS[:8]},
            "outcome": r["outcome"], "confidence": r["confidence"],
            "source_file": f"lec-{nn:02d}-verified-batch2.md",
            "source_locator": r["case_name"],
        })
    fieldnames = list(csv.DictReader(open(VER_CSV, encoding="utf-8")).fieldnames)
    with open(VER_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        for row in out_rows:
            w.writerow(row)
    reread = list(csv.DictReader(open(VER_CSV, encoding="utf-8")))
    assert len(reread) == len(ver) + len(out_rows)
    assert len({r["id"] for r in reread}) == len(reread), "дубль ID!"
    print(f"\nЗАПИСАНО: +{len(out_rows)} строк; verified теперь {len(reread)}")
    # карта локальный номер → финальный ID (для секций «батч 2»)
    with open(os.path.join(HERE, "batch2_id_map.csv"), "w", newline="",
              encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["final_id", "lecture_num", "case_name", "year", "outcome"])
        for row in out_rows:
            w.writerow([row["id"], row["lecture_num"], row["case_name"],
                        row["year"], row["outcome"]])
    print("карта ID: batch2_id_map.csv")


if __name__ == "__main__":
    main(write="--write" in sys.argv)
