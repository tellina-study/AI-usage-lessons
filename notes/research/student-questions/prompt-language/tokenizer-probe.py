#!/usr/bin/env python3
"""
tokenizer-probe.py — эмпирическое измерение токенизации смешанных систем письма.

Issue: tellina-study/AI-usage-lessons#216 (research-prompt-language).
Дата прогона: см. шапку tokenizer-probe-output.txt.

ЦЕЛЬ: измерить (не придумать) сколько токенов дают разные BPE/SentencePiece
токенизаторы на (а) одном смысле в 5 "языках" (EN/RU/AR/ZH/код), (б) одной
строке со смешанными скриптами внутри, (в) кириллице в разных Unicode-формах
(CAPS / эмодзи / NFD-разложение).

КАК ЗАПУСТИТЬ (воспроизводимо):
    python3 -m venv /tmp/tokvenv   # или используйте системный python3
    /tmp/tokvenv/bin/pip install tiktoken transformers
    /tmp/tokvenv/bin/python3 tokenizer-probe.py > tokenizer-probe-output.txt 2>&1

Если сети к huggingface.co / openaipublic.blob.core.windows.net нет —
tiktoken.get_encoding()/AutoTokenizer.from_pretrained() упадут при первой
загрузке словаря (кэш не из коробки). В этой сессии сеть была доступна
2026-10-02, подробности см. в output-файле.

ТОКЕНИЗАТОРЫ В ЭТОМ ПРОГОНЕ (все публичные, без gated-доступа):
  - o200k_base   (tiktoken; GPT-4o/GPT-5 family, byte-level BPE)
  - cl100k_base  (tiktoken; GPT-4/3.5, byte-level BPE)
  - gpt2         (HF; оригинальный byte-level BPE GPT-2, vocab 50257)
  - Qwen2.5-0.5B (HF; tiktoken-based + CJK/мультиязычное расширение, vocab 151643)
  - Llama-3-8B   (HF, зеркало NousResearch/Meta-Llama-3-8B; byte-level BPE, vocab 128000)
  - Gemma-2-9b   (HF, зеркало unsloth/gemma-2-9b-it; SentencePiece byte-fallback, vocab 256000)
  - Mistral-7B-v0.1 (HF; SentencePiece byte-fallback, vocab 32000 — "старый" маленький словарь)

НИЧЕГО в этом файле не подменяет реальный вызов токенизатора — если библиотека
недоступна, функция возвращает None и это отражается в таблице как "n/a",
а не как придуманное число.
"""

import sys
import time
import unicodedata
import datetime

LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


# ---------------------------------------------------------------------------
# 1. Загрузка токенизаторов (каждый — best-effort, с честным fallback)
# ---------------------------------------------------------------------------

TOKENIZERS = {}
ERRORS = {}


def try_load_tiktoken():
    try:
        import tiktoken
        for name in ["o200k_base", "cl100k_base"]:
            t0 = time.time()
            enc = tiktoken.get_encoding(name)
            dt = time.time() - t0
            TOKENIZERS[name] = ("tiktoken", enc)
            log(f"[load] tiktoken:{name} OK ({dt:.2f}s)")
    except Exception as e:
        ERRORS["tiktoken"] = repr(e)
        log(f"[load] tiktoken FAILED: {e!r}")


def try_load_hf():
    try:
        from transformers import AutoTokenizer
    except Exception as e:
        ERRORS["transformers"] = repr(e)
        log(f"[load] transformers FAILED: {e!r}")
        return

    hf_models = {
        "gpt2": "gpt2",
        "qwen2.5-0.5b": "Qwen/Qwen2.5-0.5B",
        "llama-3-8b": "NousResearch/Meta-Llama-3-8B",
        "gemma-2-9b": "unsloth/gemma-2-9b-it",
        "mistral-7b-v0.1": "mistralai/Mistral-7B-v0.1",
    }
    for key, repo in hf_models.items():
        try:
            t0 = time.time()
            tok = AutoTokenizer.from_pretrained(repo)
            dt = time.time() - t0
            TOKENIZERS[key] = ("hf", tok)
            log(f"[load] hf:{repo} OK ({dt:.2f}s, vocab={tok.vocab_size})")
        except Exception as e:
            ERRORS[key] = repr(e)
            log(f"[load] hf:{repo} FAILED: {e!r}")


# ---------------------------------------------------------------------------
# 2. Унифицированный интерфейс: encode -> list[int]; decode_pieces -> list[str]
# ---------------------------------------------------------------------------

def encode(name, text):
    kind, obj = TOKENIZERS[name]
    if kind == "tiktoken":
        return obj.encode(text, disallowed_special=())
    else:
        return obj.encode(text, add_special_tokens=False)


def decode_pieces(name, ids):
    """Вернуть по кусочку на токен — как он декодируется в текст (может быть
    нечитаемый байт-фрагмент посередине многобайтового символа — это и есть
    интересный случай)."""
    kind, obj = TOKENIZERS[name]
    pieces = []
    if kind == "tiktoken":
        for i in ids:
            b = obj.decode_single_token_bytes(i)
            pieces.append(b.decode("utf-8", errors="replace"))
    else:
        toks = obj.convert_ids_to_tokens(ids)
        for t in toks:
            pieces.append(t)
    return pieces


# ---------------------------------------------------------------------------
# 3. Тестовые строки
# ---------------------------------------------------------------------------

SAME_MEANING = {
    "EN": "Please set the timeout to 30 seconds.",
    "RU": "Пожалуйста, установите тайм-аут на 30 секунд.",
    "AR": "من فضلك اضبط مهلة الانتظار على 30 ثانية.",
    "ZH": "请将超时设置为30秒。",
    "CODE": "def set_timeout(seconds: int = 30) -> None:\n    pass",
}
# ВАЖНО: AR/ZH переводы — рабочие (смысл передан верно для демонстрации
# токенизации), это НЕ лингвистическая экспертиза и не claim о точности
# перевода — для измерения токенов это не требуется, значение нужно только
# как "сопоставимый по смыслу текст".

MIXED_SENTENCE = (
    "Привет, set the timeout to 30 секунд — 请注意 — "
    "و اضبط القيمة على الحد الأقصى."
)
# Куски той же строки по отдельности (для теста "налог на переключение"):
MIXED_CHUNKS = [
    "Привет, ",
    "set the timeout to 30 ",
    "секунд — ",
    "请注意 — ",
    "و اضبط القيمة على الحد الأقصى.",
]
assert "".join(MIXED_CHUNKS) == MIXED_SENTENCE, "chunks must reassemble exactly"

# Без разделителя между скриптами — прямой тест claim #1 (пересекает ли
# \p{L}+ в pre-tokenization regex границу письменности, если между буквами
# разных скриптов нет пробела/пунктуации).
NO_SEPARATOR_PAIRS = {
    "lat+cyr (helloПривет)": "helloПривет",
    "lat+han (hello你好)": "hello你好",
    "lat+arab (helloمرحبا)": "helloمرحبا",
    "cyr+han (Привет你好)": "Привет你好",
}

# --- Контрольный тест аддитивности (orchestrator review, issue #216) -------
# Наивный тест "целая строка vs сумма кусков, закодированных ПО ОТДЕЛЬНОСТИ
# без контекста" путает два разных эффекта: (а) смену письменности и
# (б) потерю ведущего пробела у каждого куска при вырезании его из контекста
# (пробел+слово — частый BPE-мёрдж; без него кусок платит лишний токен).
# Этот тест контролирует (б), кодируя каждый кусок (кроме первого) С тем же
# ведущим пробелом, что у него внутри строки — тогда остаётся только (а).
ADDITIVITY_PARTS = [
    "The server must restart now.",
    "Сервер должен перезапуститься сейчас.",
    "服务器必须立即重启。",
    "يجب إعادة تشغيل الخادم الآن.",
]
ADDITIVITY_WHOLE = " ".join(ADDITIVITY_PARTS)

# Второй набор — параллельное предложение на 4 формах, EN как база, для
# демонстрации "токены/символ" vs "токены/смысл" (orchestrator review).
PARALLEL_SENTENCE_2 = {
    "EN": "Please restart the server and check the logs for errors.",
    "RU": "Пожалуйста, перезапустите сервер и проверьте логи на ошибки.",
    "AR": "يرجى إعادة تشغيل الخادم والتحقق من السجلات بحثًا عن الأخطاء.",
    "ZH": "请重启服务器并检查日志中的错误。",
}

CYRILLIC_FORMS = {
    "lowercase": "привет",
    "CAPS": "ПРИВЕТ",
    "with_emoji": "привет👋",
    "may_NFC": "май",  # м-а-й, where й = U+0439 (single codepoint, NFC)
    "may_NFD": unicodedata.normalize("NFD", "май"),  # й -> и + U+0306 (2 codepoints)
    "yolka_NFC": "ёлка",  # ё = U+0451 single codepoint
    "yolka_NFD": unicodedata.normalize("NFD", "ёлка"),  # ё -> е + U+0308
}


# ---------------------------------------------------------------------------
# 4. UTF-8 байты на символ по скриптам (byte-level lower bound, НЕ требует
#    токенизатора вообще — считаем сами, это и есть "механистическое
#    объяснение дороговизны", см. отчёт §2)
# ---------------------------------------------------------------------------

BYTE_SAMPLES = {
    "Latin (a)": "a",
    "Cyrillic (б)": "б",
    "Arabic (ب)": "ب",
    "Han (中)": "中",
    "Emoji (👋)": "👋",
    "Devanagari (क)": "क",
}


def print_byte_table():
    log("\n## Таблица: UTF-8 байт на символ по скриптам (без токенизатора)\n")
    log("| Скрипт (пример) | codepoint(s) | UTF-8 байт |")
    log("|---|---|---|")
    for label, ch in BYTE_SAMPLES.items():
        cps = " ".join(f"U+{ord(c):04X}" for c in ch)
        nbytes = len(ch.encode("utf-8"))
        log(f"| {label} | {cps} | {nbytes} |")


# ---------------------------------------------------------------------------
# 5. Печать таблиц измерений
# ---------------------------------------------------------------------------

def table_same_meaning():
    log("\n## Таблица: один смысл, 5 форм (EN как база)\n")
    header = "| Форма | символов | " + " | ".join(
        f"{name} токенов (×EN)" for name in TOKENIZERS
    ) + " |"
    log(header)
    log("|" + "---|" * (2 + len(TOKENIZERS)))
    base_tokens = {}
    for label, text in SAME_MEANING.items():
        row = [label, str(len(text))]
        for name in TOKENIZERS:
            try:
                n = len(encode(name, text))
            except Exception as e:
                row.append(f"n/a ({e!r})")
                continue
            if label == "EN":
                base_tokens[name] = n
                row.append(f"{n} (1.00×)")
            else:
                b = base_tokens.get(name)
                if b:
                    row.append(f"{n} ({n/b:.2f}×)")
                else:
                    row.append(str(n))
        log("| " + " | ".join(row) + " |")


def table_mixed_vs_sum():
    log("\n## Таблица: смешанная строка vs сумма отдельных кусков (\"налог на переключение\")\n")
    log(f"Полная строка (len={len(MIXED_SENTENCE)} символов):")
    log(f"  `{MIXED_SENTENCE}`")
    log("")
    log("| Токенизатор | токены(полная строка) | Σ токены(куски по отдельности) | разница | разница % |")
    log("|---|---|---|---|---|")
    for name in TOKENIZERS:
        try:
            full_n = len(encode(name, MIXED_SENTENCE))
            chunk_ns = [len(encode(name, c)) for c in MIXED_CHUNKS]
            sum_n = sum(chunk_ns)
            diff = full_n - sum_n
            pct = (diff / sum_n * 100) if sum_n else float("nan")
            log(f"| {name} | {full_n} | {sum_n} ({chunk_ns}) | {diff:+d} | {pct:+.1f}% |")
        except Exception as e:
            log(f"| {name} | n/a | n/a | n/a | n/a ({e!r}) |")


def table_additivity_control():
    """Контроль на границу ведущего пробела (orchestrator review, issue #216).

    Три числа на токенизатор:
      whole               — токены(полная строка, части через один пробел)
      sum_alone           — Σ токены(каждый кусок закодирован БЕЗ контекста)
      sum_with_lead_space — Σ токены(каждый кусок, кроме первого, с ведущим
                             пробелом — т.е. ровно как он стоит в строке)
    Если whole == sum_with_lead_space (с точностью до redistribution на самой
    границе) — это означает, что стоимость смешанного текста АДДИТИВНА по
    языкам, и расхождение whole vs sum_alone — чисто артефакт теста (потеря
    пробела), а не "налог на смешение письменностей".
    """
    log("\n## Таблица: контроль аддитивности (ведущий пробел) — не \"налог\", а артефакт теста\n")
    log(f"Куски: {ADDITIVITY_PARTS}")
    log(f"Целая строка: `{ADDITIVITY_WHOLE}`\n")
    log("| Токенизатор | whole | Σ alone (по кускам) | Σ with_leading_space (по кускам) |")
    log("|---|---|---|---|")
    for name in TOKENIZERS:
        try:
            whole_n = len(encode(name, ADDITIVITY_WHOLE))
            alone = [len(encode(name, p)) for p in ADDITIVITY_PARTS]
            with_space = [
                len(encode(name, p if i == 0 else " " + p))
                for i, p in enumerate(ADDITIVITY_PARTS)
            ]
            log(
                f"| {name} | {whole_n} | {sum(alone)} {alone} | "
                f"{sum(with_space)} {with_space} |"
            )
        except Exception as e:
            log(f"| {name} | n/a | n/a | n/a ({e!r}) |")


def table_parallel_sentence_2():
    log("\n## Таблица: параллельное предложение #2 — токены/символ vs токены/смысл\n")
    log("Один и тот же смысл, EN как база (токены, не символы):\n")
    header = "| Форма | символов | " + " | ".join(
        f"{name} (×EN)" for name in TOKENIZERS
    ) + " |"
    log(header)
    log("|" + "---|" * (2 + len(TOKENIZERS)))
    base = {}
    for label, text in PARALLEL_SENTENCE_2.items():
        row = [label, str(len(text))]
        for name in TOKENIZERS:
            try:
                n = len(encode(name, text))
            except Exception as e:
                row.append(f"n/a")
                continue
            if label == "EN":
                base[name] = n
                row.append(f"{n} (1.00×)")
            else:
                b = base.get(name)
                row.append(f"{n} ({n/b:.2f}×)" if b else str(n))
        log("| " + " | ".join(row) + " |")
    log(
        "\nПРИМЕЧАНИЕ: ZH здесь обычно даёт ×<1.00 (дешевле EN по токенам), "
        "хотя токенов-на-символ у ZH больше — потому что символов в ZH-версии "
        "в разы меньше (иероглиф = слог/морфема, не буква). Токены/символ и "
        "токены/смысл — разные метрики, и таблица \"токены на символ\" одна "
        "НЕ показывает, дороже ли язык по факту передачи одного и того же "
        "смысла."
    )


def show_mixed_boundaries(name):
    log(f"\n### Разбиение смешанной строки токенизатором `{name}` (кусок за куском)\n")
    try:
        ids = encode(name, MIXED_SENTENCE)
        pieces = decode_pieces(name, ids)
        log(f"Всего токенов: {len(ids)}")
        log("")
        log("Декодированные токены (разделитель `|`):")
        log("`" + "|".join(p.replace("\n", "\\n") for p in pieces) + "`")
    except Exception as e:
        log(f"n/a: {e!r}")


def table_no_separator():
    log("\n## Таблица: смена скрипта БЕЗ разделителя (пробела/пунктуации)\n")
    log("Прямая проверка: даже когда между буквами разных скриптов нет пробела\n"
        "(т.е. формально это один `\\p{L}+`-прогон для pre-tokenization regex),\n"
        "склеивает ли BPE-мёрдж токен через границу письменности?\n")
    for label, text in NO_SEPARATOR_PAIRS.items():
        log(f"\n### `{label}` -> `{text}`\n")
        for name in TOKENIZERS:
            try:
                ids = encode(name, text)
                pieces = decode_pieces(name, ids)
                log(f"- **{name}** ({len(ids)} ток.): `" + "|".join(pieces) + "`")
            except Exception as e:
                log(f"- **{name}**: n/a ({e!r})")


def table_cyrillic_forms():
    log("\n## Таблица: кириллица в разных Unicode-формах\n")
    header = "| Форма | строка | codepoints | " + " | ".join(TOKENIZERS) + " |"
    log(header)
    log("|" + "---|" * (3 + len(TOKENIZERS)))
    for label, text in CYRILLIC_FORMS.items():
        ncp = len(text)
        row = [label, text.replace("\n", "\\n"), str(ncp)]
        for name in TOKENIZERS:
            try:
                n = len(encode(name, text))
                row.append(str(n))
            except Exception as e:
                row.append(f"n/a")
        log("| " + " | ".join(row) + " |")


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    log(f"# tokenizer-probe.py — вывод прогона")
    log(f"Дата/время запуска (UTC): {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    log(f"Python: {sys.version}")
    try:
        import tiktoken
        log(f"tiktoken version: {tiktoken.__version__}")
    except Exception:
        pass
    try:
        import transformers
        log(f"transformers version: {transformers.__version__}")
    except Exception:
        pass
    log("")

    log("## Загрузка токенизаторов\n")
    try_load_tiktoken()
    try_load_hf()

    if not TOKENIZERS:
        log("\nНИ ОДИН токенизатор не загрузился. Эмпирика невозможна в этом окружении.")
        log("Ошибки:")
        for k, v in ERRORS.items():
            log(f"  {k}: {v}")
        return

    log(f"\nЗагружено токенизаторов: {len(TOKENIZERS)} -> {list(TOKENIZERS.keys())}")
    if ERRORS:
        log(f"Не загрузились (честно пропущены): {ERRORS}")

    print_byte_table()
    table_same_meaning()
    table_parallel_sentence_2()
    table_mixed_vs_sum()
    table_additivity_control()
    for name in TOKENIZERS:
        show_mixed_boundaries(name)
    table_no_separator()
    table_cyrillic_forms()

    log("\n## Конец вывода\n")


if __name__ == "__main__":
    main()
