#!/usr/bin/env python3
"""Сквозная перенумерация слайдов семинара: `n01`…`nNN` без буквенных хвостов.

Правило деки (`tools/seminar-production/README.md` §1, правило А6): нумерация
сквозная, без буквенных префиксов и хвостов, и файл, манифест и фронтматтер
обязаны сходиться по номерам. Буквенный хвост (`n14a`, `n49b`) появляется
законно — когда слайд заводят между двумя уже готовыми и не хотят двигать
полдеки, пока рядом пишут три сессии. Снимать его надо один раз, при сведении,
и машиной: ссылок на слайды в живых файлах порядка тысячи, и руками они
расходятся молча.

Что делает:

* порядок берёт из `deck.yaml` (он сам собран из слайдов генератором), и
  присваивает `n01`…`nNN` по позиции — то есть идентификатор становится равен
  сквозному номеру, который рендерер и так выводит из порядка;
* переименовывает файлы слайдов и схем (обычным `rename`, НЕ `git mv`:
  индекс — зона оркестратора);
* заменяет ссылки во всех названных файлах ОДНИМ проходом, поэтому обмен
  вида `n15 → n16` при `n16 → n18` не сталкивается сам с собой;
* сообщает идентификаторы, которых в карте нет (ссылки на снятые слайды),
  а не правит их молча.

**Зачем список защищённых строк.** Семинары ссылаются друг на друга, и
нумерация у них своя: в живых файлах Семинара 6 нашлось 15 мест, где `nNN` —
это слайд Семинара 5 («Семинар 5 кончается на `n68`», `sem-05/slides/n65-…`,
«заголовки шести дивайдеров Семинара 5»). Перенумерация своей деки переписала
бы их в чужие несуществующие номера — класс ошибки, который не находится
грепом после того, как случился. Поэтому строки с чужими ссылками называются
явно, файлом, и проверяются глазами один раз.

    python3 renumber_slides.py library/seminars/sem-06 --dry
    python3 renumber_slides.py library/seminars/sem-06 \
        --targets targets.txt --protect protect.txt
"""
import argparse
import re
import sys
from pathlib import Path

import yaml

TOKEN = re.compile(r"(?<![0-9A-Za-z_Ѐ-ӿ])n(\d{2}[a-z]?)(?![0-9A-Za-z_Ѐ-ӿ])")


def mapping_from_deck(deck: Path):
    """Карта «старый идентификатор → новый» из порядка слайдов в манифесте."""
    doc = yaml.safe_load(deck.read_text(encoding="utf-8"))
    ids = [s["id"] for s in doc["slides"]]
    if len(ids) != len(set(ids)):
        raise SystemExit("в манифесте повторяются идентификаторы — сначала развести их")
    return {sid: "n%02d" % i for i, sid in enumerate(ids, 1)}


def read_list(path: Path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.append(line)
    return out


def parse_protect(path: Path, root: Path):
    """Защищённые строки файла.

    Две записи на выбор: `отн/путь|кусок текста строки` (привязка к тексту) и
    `отн/путь:номер_строки`. Первая форма предпочтительна: любая правка выше
    по файлу сдвигает номера, и список, собранный номерами, начинает защищать
    не те строки — ровно то, что случилось при сведении Семинара 6 (две записи
    из восемнадцати уехали на строку). Привязка к тексту этого не умеет, а
    неоднозначный или пропавший кусок называется вслух."""
    prot = {}
    for item in read_list(path):
        if "|" in item:
            rel, _, anchor = item.partition("|")
            rel, anchor = rel.strip(), anchor.strip()
            lines = (root / rel).read_text(encoding="utf-8").splitlines()
            found = [i for i, l in enumerate(lines, 1) if anchor in l]
            if len(found) != 1:
                raise SystemExit(
                    f"защита «{rel}|{anchor}»: подходящих строк {len(found)}, "
                    f"нужна ровно одна")
            prot.setdefault(rel, set()).add(found[0])
        else:
            rel, _, num = item.rpartition(":")
            prot.setdefault(rel, set()).add(int(num))
    return prot


def substitute(text, mapping, protected_lines, unknown):
    """Один проход по тексту; защищённые строки не трогаются вовсе."""
    hits = 0
    out = []
    for lineno, line in enumerate(text.split("\n"), 1):
        if lineno in protected_lines:
            out.append(line)
            continue

        def repl(m):
            nonlocal hits
            old = "n" + m.group(1)
            new = mapping.get(old)
            if new is None:
                unknown.setdefault(old, 0)
                unknown[old] += 1
                return m.group(0)
            if new != old:
                hits += 1
            return new

        out.append(TOKEN.sub(repl, line))
    return "\n".join(out), hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", help="папка семинара, например library/seminars/sem-06")
    ap.add_argument("--targets", help="файл со списком путей (относительно root)")
    ap.add_argument("--protect", help="файл со строками «путь|кусок строки» (или «путь:номер»), которые не трогать")
    ap.add_argument("--dry", action="store_true", help="ничего не писать")
    a = ap.parse_args()

    root = Path(a.root).resolve()
    mapping = mapping_from_deck(root / "deck.yaml")
    moved = {k: v for k, v in mapping.items() if k != v}
    print(f"карта: {len(mapping)} слайдов, меняют номер {len(moved)}")
    if not moved:
        print("менять нечего")
        return 0

    targets = read_list(Path(a.targets)) if a.targets else []
    protect = parse_protect(Path(a.protect), root) if a.protect else {}
    for rel in protect:
        if rel not in targets:
            print(f"  ⚠ защищён файл, которого нет в списке правки: {rel}")

    unknown, total, touched = {}, 0, 0
    for rel in targets:
        p = root / rel
        if not p.exists():
            print(f"  ⚠ нет файла: {rel}")
            continue
        text = p.read_text(encoding="utf-8")
        new, hits = substitute(text, mapping, protect.get(rel, set()), unknown)
        if hits:
            touched += 1
            total += hits
            print(f"  {rel}: {hits}")
            if not a.dry:
                p.write_text(new, encoding="utf-8")

    renames = []
    for folder, pattern in (("slides", "n*.md"), ("rendered/figures", "*.png")):
        for f in sorted((root / folder).glob(pattern)):
            m = TOKEN.search(f.name)
            if not m:
                continue
            new_name = TOKEN.sub(lambda x: mapping.get("n" + x.group(1), x.group(0)), f.name, count=1)
            if new_name != f.name:
                renames.append((f, f.with_name(new_name)))
    for src, dst in renames:
        print(f"  переименование: {src.name} → {dst.name}")
        if not a.dry:
            if dst.exists():
                raise SystemExit(f"цель уже существует: {dst}")
            src.rename(dst)

    print(f"\nитого: {total} ссылок в {touched} файлах, {len(renames)} переименований")
    if unknown:
        print("идентификаторы вне карты (ссылки на снятые слайды или чужие деки) — "
              "оставлены как есть, разобрать глазами:")
        for k in sorted(unknown):
            print(f"  {k}: {unknown[k]}")
    if a.dry:
        print("\n(--dry: ничего не записано)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
