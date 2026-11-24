"""OCR + правила: раскладка по якорным подписям полей.

Правила написаны ДО просмотра точности извлечения (по словарю подписей полей,
известному из разметки корпуса, не по тому, что эти правила вернут правильно).
Вход — строки RapidOCR (box, text, conf) одной формы; выход — значение по
категории (name/phone/date/count), если якорь найден, иначе None.

Первая версия (без границ слова) ложно срабатывала внутри посторонних слов —
«TO» находился внутри «ATTORNEY», «ATTENTION». Эта версия якорит с обеих сторон:
подпись не должна быть куском более длинного слова ни слева, ни справа (см.
`tools/seminar-production/README.md` §8.6 — такая же ошибка одностороннего
якоря на кириллице, здесь то же на латинице).
"""
import json
import re

ANCHORS = {
    "name": ["TO", "FROM", "ATTN", "SENDER", "MESSAGE TO", "NAME OF ACCOUNT", "NAME OF GUEST"],
    "phone": ["FAX NUMBER", "FAX NO", "FAX", "PHONE NUMBER", "PHONE NO", "PHONE",
              "TELEPHONE", "VOICE NUMBER", "TEL"],
    "date": ["DATE RECEIVED", "DATE"],
    "count": ["NUMBER OF PAGES", "NO OF PAGES", "PAGES", "NO OF STORES",
              "NUMBER OF STORES", "NUMBER OF", "NO OF", "REPS"],
}


def anchor_regex(phrase):
    letters = re.sub(r"[^A-Z]", "", phrase.upper())
    body = r"\s*".join(re.escape(ch) for ch in letters)
    return re.compile(r"(?<![A-Za-z])" + body + r"(?![A-Za-z])", re.IGNORECASE)


ANCHOR_PATTERNS = {
    cat: sorted(((a, anchor_regex(a)) for a in lst), key=lambda x: -len(x[0]))
    for cat, lst in ANCHORS.items()
}


def extract_fields(lines):
    out = {cat: [] for cat in ANCHORS}
    texts = [l["text"] for l in lines]
    for i, raw in enumerate(texts):
        for cat, pats in ANCHOR_PATTERNS.items():
            matched = False
            for _, pat in pats:
                m = pat.search(raw)
                if not m:
                    continue
                tail = raw[m.end():].lstrip(" :#.-：")
                if tail.strip():
                    out[cat].append(tail.strip())
                    matched = True
                elif i + 1 < len(texts):
                    nxt = texts[i + 1].strip()
                    # не брать следующую строку, если она сама начинается с якоря
                    # любой категории (тогда у ТЕКУЩЕЙ подписи значения нет вовсе)
                    is_next_anchor = any(
                        p2.search(nxt) and p2.search(nxt).start() == 0
                        for pats2 in ANCHOR_PATTERNS.values() for _, p2 in pats2
                    )
                    if nxt and not is_next_anchor:
                        out[cat].append(nxt)
                        matched = True
                if matched:
                    break  # один якорь на строку и категорию — самый длинный уже первый
    return out


def main():
    ocr = json.load(open("raw/ocr_results.json"))["per_form"]
    results = {}
    for fid, data in ocr.items():
        results[fid] = extract_fields(data["lines"])
    with open("raw/rules_extraction.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=2)
    print("готово:", len(results), "форм")


if __name__ == "__main__":
    main()
