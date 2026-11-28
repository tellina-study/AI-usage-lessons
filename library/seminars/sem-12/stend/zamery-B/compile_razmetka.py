"""Перекомпиляция разметки-истины срез B из человеческого markdown в JSON.

Зачем переписан: исходный `razmetka.json` (принесён с планирования,
`plan-peredelki/razmetka-B.md`) резал перенесённые строки маркдауна по
физическому concatenate newline, не склеивая продолжение с отступом —
45 из ~51 карточек получили обрубленную последнюю строку «что видно»
(например «белая» вместо «белая миска с бусинами, бумажные пакеты с
ручками, ножницы»). Плюс двойники id у карточек с пометкой «ПЕРЕНЕСЁН»
(запись-заглушка в старой группе + настоящая запись в новой). Источник
истины не правим — `razmetka-B.md` не трогаем; правим только то, как
скрипт его читает.

Запуск:  python3 compile_razmetka.py > razmetka.json
"""
import json
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent.parent / "plan-peredelki" / "razmetka-B.md"
MANIFEST = Path(__file__).resolve().parent.parent.parent / "plan-peredelki" / "korpus" / "manifest-foto-BC.json"
OUT_NOTE = "library/seminars/sem-12/plan-peredelki/razmetka-B.md"

HEADER_RE = re.compile(
    r"^### (?P<id>[0-9a-f]{16}) — (?P<rest>.+)$"
)
# Групповой заголовок на несколько id сразу через ` / ` (например G8 "ещё три
# чашки") — отдельного «что видно» на каждый id в тексте нет, только общее
# «Коротко:»; разбираем id-список отдельно, не даём ему утечь в cur_body
# предыдущей карточки.
MULTI_HEADER_RE = re.compile(
    r"^### (?P<ids>[0-9a-f]{16}(?: / [0-9a-f]{16})+) — (?P<rest>.+)$"
)
GROUP_RE = re.compile(r"^## Группа (?P<gid>G\d+) — (?P<name>.+)$")
TRANSFER_RE = re.compile(r"ПЕРЕНЕСЁН")


def parse_header(rest, gid):
    """Разбирает хвост заголовка `### <id> — корпус: ... · дека: ... [· ТАКЖЕ: ...]`."""
    in_corpus = rest.startswith("корпус: ДА")
    deck_allowed = None
    deck_reason = None
    also = []
    m_deck = re.search(r"дека: (ДА|да|НЕТ)\s*(\(([^)]*)\))?", rest)
    if m_deck:
        deck_allowed = m_deck.group(1) in ("ДА", "да")
        deck_reason = m_deck.group(3)
    for m_also in re.finditer(r"ТАКЖЕ[:]?\s*([^·]+)", rest):
        also.append(m_also.group(1).strip().rstrip("."))
    not_reason = None
    if not in_corpus:
        m_not = re.search(r"корпус: НЕТ\s*(\(([^)]*)\))?", rest)
        if m_not:
            not_reason = m_not.group(2)
    return in_corpus, deck_allowed, deck_reason, also, not_reason


def join_body(lines):
    """Склеивает нумерованный список, где продолжение строки идёт отступом."""
    items = []
    cur = None
    for raw in lines:
        if not raw.strip():
            continue
        if re.match(r"^\d+\.\s", raw):
            if cur is not None:
                items.append(cur.strip())
            cur = re.sub(r"^\d+\.\s", "", raw).rstrip()
        elif raw.startswith("   ") or raw.startswith("\t"):
            # продолжение предыдущего пункта (отступ в markdown-источнике)
            if cur is not None:
                cur = cur.rstrip() + " " + raw.strip()
            else:
                cur = raw.strip()
        elif raw.startswith("Коротко:"):
            if cur is not None:
                items.append(cur.strip())
            cur = raw[len("Коротко:"):].strip()
        else:
            # продолжение без явного отступа (перенос строки в абзаце) —
            # тоже клеим к текущему пункту, не заводим новый
            if cur is not None:
                cur = cur.rstrip() + " " + raw.strip()
            else:
                cur = raw.strip()
    if cur is not None:
        items.append(cur.strip())
    return items


def load_manifest():
    recs = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {r["id"]: r for r in recs}


def main():
    manifest = load_manifest()
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines()
    entries = []
    cur_id = None
    cur_gid = None
    cur_rest = None
    cur_body: list[str] = []
    skip_stub = False

    def flush():
        nonlocal cur_id, cur_rest, cur_body, cur_gid, skip_stub
        if cur_id is None or skip_stub:
            cur_body = []
            return
        in_corpus, deck_allowed, deck_reason, also, not_reason = parse_header(cur_rest, cur_gid)
        what = join_body(cur_body)
        rec = manifest.get(cur_id, {})
        entries.append({
            "id": cur_id,
            "group": cur_gid,
            "in_corpus": in_corpus,
            "deck_allowed": deck_allowed,
            "deck_reason": deck_reason,
            "also_tags": also,
            "excluded_reason": not_reason,
            "what_is_visible": what,
            "license": rec.get("license"),
            "author": rec.get("author"),
            "landing": rec.get("landing"),
            "s3_url": rec.get("s3_url"),
            "sha256_downloaded": rec.get("sha256_downloaded"),
        })
        cur_body = []

    for raw in lines:
        g = GROUP_RE.match(raw)
        if g:
            flush()
            cur_id = None
            cur_gid = g.group("gid")
            continue
        mh = MULTI_HEADER_RE.match(raw)
        if mh:
            flush()
            cur_id = None  # групповой заголовок-список — собственного «что видно» нет
            continue
        h = HEADER_RE.match(raw)
        if h:
            flush()
            cur_id = h.group("id")
            cur_rest = h.group("rest")
            skip_stub = bool(TRANSFER_RE.search(cur_rest))
            continue
        if raw.startswith("---") or raw.startswith("## Сводка") or raw.startswith("## Счёт грязи"):
            flush()
            cur_id = None
            break
        if cur_id is not None:
            cur_body.append(raw)
    flush()

    in_corpus_entries = [e for e in entries if e["in_corpus"]]
    doc = {
        "date": "2026-11-24",
        "author": "планировщик A/B/C (человек-в-контуре), до модельных описаний; "
                   "перекомпилировано сессией кейса B (issue #351) — исходный компилятор "
                   "резал продолжения строк, см. zhurnal.md",
        "source_md": "library/seminars/sem-12/plan-peredelki/razmetka-B.md",
        "corpus_size": len(in_corpus_entries),
        "candidates_total": len(entries),
        "entries": entries,
    }
    json.dump(doc, sys.stdout, ensure_ascii=False, indent=1)
    print()
    print(f"# corpus_size={len(in_corpus_entries)} candidates_total={len(entries)}", file=sys.stderr)


if __name__ == "__main__":
    main()
