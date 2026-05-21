#!/usr/bin/env python3
"""
deep_latin_scan.py — deep Latin-token scan for anti-anglicism verification.

ENFORCED per memory rule [[russification]] and CLAUDE.md Pre-USER-GATE Walkthrough Rule п.10.

Pattern-narrow grep маскирует depth — Лекция 8: narrow scan (32 patterns) показал 0-4 hits,
deep scan (broad regex) показал 919 unique tokens в speech.

Usage:
    python3 deep_latin_scan.py <file1.md> [<file2.md> ...]

For PPTX visible text:
    python3 -c "from pptx import Presentation; p=Presentation('library/lectures/lec-NN/rendered/lec-NN.pptx'); \
      [print(s.text_frame.text) for sl in p.slides for s in sl.shapes if s.has_text_frame]" > /tmp/pptx-visible.txt
    python3 deep_latin_scan.py /tmp/pptx-visible.txt

Acceptance: для narrative body — unique - whitelist = ∅ (URLs / case names / brand markers OK).
"""

import re
import sys
import pathlib

BRAND_ALLOWLIST = {
    # Brand names
    "Sora", "Midjourney", "Suno", "ElevenLabs", "OpenAI", "Anthropic", "Adobe",
    "Firefly", "NYT", "Bloomberg", "Reuters", "BBC", "CNN", "RIAA", "DMCA", "CDPA",
    "GDPR", "Wikipedia", "Wikimedia", "YouTube", "GitHub", "Google", "Microsoft",
    "Meta", "Apple", "DeepMind", "DeepSeek", "Claude", "GPT", "ChatGPT", "Gemini",
    "Copilot", "Llama", "Mistral", "Cursor", "Maxar", "Palantir", "Anduril",
    "Stripe", "Linear", "Notion", "Slack", "Zoom", "Figma", "Sentinel", "NASA",
    "DARPA", "ESA", "Pentagon", "EUCOM", "CENTCOM", "Yandex", "VK", "Sber",
    "GigaChat", "YandexGPT", "T-Bank", "Tinkoff", "Goldman", "Sachs", "JPMorgan",
    "Morgan", "Stanley", "Pixar", "Disney", "Spotify", "Netflix",
    # Tech acronyms (с RU расшифровкой обычно где-то)
    "AI", "ML", "LLM", "RAG", "MCP", "API", "GenAI", "RLHF", "CV", "NLP", "UI",
    "UX", "SaaS", "PaaS", "OS", "GPU", "CPU", "TPU", "CC", "PDF", "PNG", "JPG",
    "JPEG", "SVG", "HTML", "CSS", "JSON", "YAML", "URL", "URI", "HTTP", "HTTPS",
    "OAuth", "JWT", "REST", "gRPC", "SQL", "NoSQL", "OODA", "HITL", "LAWS", "SAR",
    "ATR", "MCAS", "ROE", "ARC", "AGI", "MMLU", "HumanEval", "BPE", "QR", "USB",
    "RAM", "ROM", "SSD", "HDD", "WCAG", "OCR", "GAN", "VAE", "RNN", "CNN-arch",
    "LSTM", "BERT", "T5", "XML", "CSV", "ASCII", "UTF", "TLS", "SSL", "VPN",
    "IDE", "CLI", "GUI", "SDK", "API-key", "TTS", "STT",
    # Slide markers / mode names / common neutral
    "v1", "v2", "v3", "vN", "sNN", "LO", "lec",
    # Common version / refs
    "ISBN", "DOI", "arXiv", "TED",
    # File-format / mathematical
    "log", "min", "max", "avg", "sum", "id", "ID",
}

# Lower-case lookup
ALLOW_LOWER = {b.lower() for b in BRAND_ALLOWLIST}


def scan(path: str) -> tuple[int, int, list[tuple[str, int]]]:
    """Scan a file for Latin tokens; return (occurrences, unique, top_hits)."""
    text = pathlib.Path(path).read_text(encoding="utf-8")
    # Strip YAML frontmatter
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
    # Strip code blocks (markdown fenced)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # Strip inline code
    text = re.sub(r"`[^`]+`", "", text)
    # Strip URLs
    text = re.sub(r"https?://\S+", "", text)
    # Strip image / link refs like ![alt](url)
    text = re.sub(r"!?\[[^\]]*\]\([^)]+\)", "", text)
    # Latin word: ≥3 chars, начинается с буквы
    tokens = re.findall(r"\b[A-Za-z][A-Za-z\-]{2,}\b", text)
    hits = [t for t in tokens if t.lower() not in ALLOW_LOWER]
    # Build top frequency list
    from collections import Counter
    counter = Counter(hits)
    top = counter.most_common(50)
    return len(hits), len(set(hits)), top


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 deep_latin_scan.py <file1> [<file2> ...]", file=sys.stderr)
        sys.exit(2)
    total_occ = 0
    total_uniq = 0
    for path in sys.argv[1:]:
        if not pathlib.Path(path).exists():
            print(f"{path}: NOT FOUND", file=sys.stderr)
            continue
        occ, uniq, top = scan(path)
        total_occ += occ
        total_uniq += uniq
        print(f"\n=== {path} ===")
        print(f"  total occurrences: {occ}")
        print(f"  unique tokens:     {uniq}")
        if top:
            print(f"  top hits (count × token):")
            for tok, cnt in top:
                print(f"    {cnt:4d}× {tok}")
        if uniq == 0:
            print("  PASS: unique - whitelist = ∅")
        else:
            print(f"  REVIEW: {uniq} unique tokens вне brand allowlist")
    print(f"\n=== TOTAL ===")
    print(f"  occurrences: {total_occ}")
    print(f"  unique:      {total_uniq}")
    sys.exit(0 if total_uniq == 0 else 1)


if __name__ == "__main__":
    main()
