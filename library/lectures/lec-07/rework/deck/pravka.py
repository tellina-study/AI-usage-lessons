#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Правка одного кадра: фронтматтер · видимый текст · довески к заметкам.

Зачем скриптом, а не перезаписью файла целиком: заметки лектора — 500–800
слов, и переписывать их ради смены четырёх строк видимого текста значит
рисковать потерять абзац.

Зачем ТЕКСТОВОЙ врезкой, а не `yaml.dump` фронтматтера: манифест деки читает
фронтматтер СВОИМ построчным разбором (`make_deck_yaml.fm`), и снимает он
только ДВОЙНЫЕ кавычки. Полный дамп переписал бы `title: "…"` в одинарных
кавычках — разбор бы их не снял, и в манифест поехал бы заголовок с кавычками
внутри. Поэтому здесь меняются ровно названные ключи, остальные строки
переносятся байт в байт.

    python3 pravka.py <файл> --fm fm.yaml --vid vid.md --zam zam.md
    python3 pravka.py <файл> --del-fm blocks,scheme

`--fm` — файл с готовыми строками фронтматтера (как они должны лежать в кадре,
с кавычками); ключи из него заменяют одноимённые, новые дописываются в конец.
`--zam` встаёт ПЕРЕД строкой «**Источники.**», если она есть.
"""
import argparse
import re
import sys
from pathlib import Path

KEY = re.compile(r"^([a-z_]+):")


def split_keys(fm_text):
    """Фронтматтер → [(ключ, его строки)] с сохранением порядка и байтов."""
    out, cur = [], None
    for ln in fm_text.split("\n"):
        m = KEY.match(ln)
        if m:
            cur = [m.group(1), [ln]]
            out.append(cur)
        elif cur is not None:
            cur[1].append(ln)
        else:
            out.append([None, [ln]])
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--fm")
    ap.add_argument("--vid")
    ap.add_argument("--zam")
    ap.add_argument("--del-fm")
    a = ap.parse_args()

    p = Path(a.path)
    raw = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.S)
    if not m:
        print(f"{p}: нет фронтматтера")
        return 1
    keys, body = split_keys(m.group(1)), m.group(2)

    if a.fm:
        patch = split_keys(Path(a.fm).read_text(encoding="utf-8").rstrip("\n"))
        for k, lines in patch:
            if k is None:
                continue
            for seg in keys:
                if seg[0] == k:
                    seg[1] = lines
                    break
            else:
                keys.append([k, lines])

    drop = {k.strip() for k in (a.del_fm or "").split(",") if k.strip()}
    keys = [s for s in keys if s[0] not in drop]

    if a.vid:
        new = Path(a.vid).read_text(encoding="utf-8").strip()
        body, n = re.subn(r"(##\s*Видимый текст слайда\s*\n)(.*?)(?=\n##\s|\Z)",
                          lambda _m: _m.group(1) + "\n" + new + "\n",
                          body, count=1, flags=re.S)
        if not n:
            print(f"{p}: раздела видимого текста не нашлось")
            return 1

    if a.zam:
        add = Path(a.zam).read_text(encoding="utf-8").strip()
        if "**Источники.**" in body:
            body = body.replace("**Источники.**", add + "\n\n**Источники.**", 1)
        else:
            body = body.rstrip() + "\n\n" + add + "\n"

    fm = "\n".join("\n".join(lines) for _k, lines in keys)
    p.write_text("---\n" + fm.strip("\n") + "\n---\n" + body, encoding="utf-8")
    print(f"{p}: правлено")
    return 0


if __name__ == "__main__":
    sys.exit(main())
