#!/usr/bin/env python3
"""Счёт слов главы по курсовой норме ≥30 000 (CLAUDE.md § Chapter Depth Baseline).

Зачем отдельный инструмент, а не описание метода словами. У главы Лекции 7 метод счёта был
записан во фронтматтере прозой — подробно, десятью строками, с перечислением того, что
снимается. По этому описанию метод воспроизвели дважды, независимо, и получили 84 562 и
94 749: расхождение 12% при разбросе ±2,5%, который тот же фронтматтер объявлял известным.
Вывод, записанный в notes/decisions.md: **словами метод счёта не задаётся.** Два читателя
одного описания расходятся на целую курсовую норму, потому что проза не говорит, что делать
с заголовком внутри снятого раздела, с таблицей, со строкой-ссылкой и с подписью под числом.

Поэтому метод здесь — код, и число главы ссылается на путь к нему, а не на абзац.

    python3 tools/lecture-production/count_chapter_words.py --selftest
    python3 tools/lecture-production/count_chapter_words.py library/lectures/lec-07/rework
    python3 tools/lecture-production/count_chapter_words.py <dir> --parts   # разбивка по частям

Правило, унаследованное от scan_visible_layer.py: проверка, показавшая число, не значит
ничего, пока не доказано, что она считает то, что обещает. Поэтому `--selftest` прогоняет
восемь случаев с заранее известным ответом и падает, если хоть один разошёлся. Запускать
самотест перед тем, как верить числу.

ЧТО СЧИТАЕТСЯ (это содержание главы по правилу курса):
  - связный текст разделов, включая вводные, разборы, оговорки и выводы;
  - определения, примеры, разборы провалов, сквозные словари в теле раздела;
  - блоки самопроверки и развёрнутые ответы Q&A — курс считает их содержанием;
  - таблицы: клетки таблицы — текст, который читатель читает;
  - подписи, пометки силы свидетельства, оговорки о базе.

ЧТО НЕ СЧИТАЕТСЯ:
  - фронтматтер YAML и комментарии в нём;
  - строки заголовков (сам заголовок — навигация, а не содержание);
  - разделы «Оглавление», «Источники», «Сводная библиография», «Глоссарий», «Карта главы»,
    «Changelog» ЦЕЛИКОМ, вместе со всеми вложенными в них подзаголовками — вложенность
    решается уровнем заголовка, и ровно здесь расходились два прежних счётчика;
  - строки, начинающиеся с «Источник», «Источники», «Литература»;
  - пометки проверки [FACT-CHECK: …], [VERIFY-DAY-OF], [VFY…] — это долг, не содержание;
  - разделители, пустые строки, маркеры разметки.

У ссылок вида [текст](адрес) остаётся текст: читатель читает текст, а не адрес.

Записано по #229.
"""
import argparse, glob, os, re, sys

# Снимаемые разделы двух РАЗНЫХ видов, и различать их обязательно.
#
# Почему два вида, а не один список. Части главы начинаются с «## Оглавление (часть N)», а
# содержание внутри них идёт заголовками «###» — то есть ГЛУБЖЕ. Правило «снято до следующего
# заголовка того же или меньшего уровня» на таком файле съедает его целиком: первый прогон
# этого счётчика вернул ноль по шести файлам из восемнадцати. Проза метода этого не различала
# вовсе, и ровно здесь расходились два прежних счётчика главы.
#
# TOC-вид: оглавление, карта частей, changelog — списки, своих подразделов не имеют никогда,
# поэтому снимаются до СЛЕДУЮЩЕГО ЗАГОЛОВКА ЛЮБОГО УРОВНЯ.
TOC_HEADINGS = ('оглавление', 'карта главы', 'карта частей', 'changelog')
# Хвостовой вид: источники, библиография, глоссарий — стоят в конце и ПОДРАЗДЕЛЫ имеют,
# поэтому снимаются до следующего заголовка того же или меньшего уровня.
TAIL_HEADINGS = ('источники', 'источник', 'сводная библиография', 'библиография',
                 'глоссарий', 'литература')

FRONTMATTER = re.compile(r'\A---\n.*?\n---\n', re.S)
HEADING = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
SOURCE_LINE = re.compile(r'^\s*[-*>]?\s*\**\s*(Источник|Источники|Литература)\b')
CHECK_MARKER = re.compile(r'\[(?:FACT-CHECK|VERIFY-DAY-OF|VFY|статус)[^\]]*\]', re.S)
MD_LINK = re.compile(r'\[([^\]\[]*)\]\([^)]*\)')
RULE = re.compile(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$')
TOKEN = re.compile(r"[0-9A-Za-zА-Яа-яЁё][0-9A-Za-zА-Яа-яЁё’'-]*")


def _excluded_kind(title):
    """'toc' | 'tail' | None — какого вида снятый раздел открывает этот заголовок."""
    t = title.strip().strip('*').strip('`').strip().lower()
    if any(t.startswith(h) for h in TOC_HEADINGS):
        return 'toc'
    if any(t.startswith(h) for h in TAIL_HEADINGS):
        return 'tail'
    return None


def count_text(text):
    """Число слов содержания в одном markdown-тексте. Метод — см. docstring модуля."""
    text = FRONTMATTER.sub('', text)
    text = CHECK_MARKER.sub(' ', text)          # до разбора строк: пометки бывают многострочными
    kept = []
    skip_level = None                           # уровень заголовка снятого раздела, если мы внутри
    skip_kind = None                            # 'toc' или 'tail' — чем он кончается
    for line in text.split('\n'):
        m = HEADING.match(line)
        if m:
            level = len(m.group(1))
            if skip_level is not None:
                # TOC кончается на любом следующем заголовке; хвостовой — на том же или меньшем уровне
                if skip_kind == 'toc' or level <= skip_level:
                    skip_level = skip_kind = None
            if skip_level is None:
                kind = _excluded_kind(m.group(2))
                if kind:
                    skip_level, skip_kind = level, kind
            continue                            # строка заголовка не считается никогда
        if skip_level is not None:
            continue
        if RULE.match(line) or SOURCE_LINE.match(line):
            continue
        kept.append(MD_LINK.sub(r'\1', line))
    return len(TOKEN.findall('\n'.join(kept)))


def count_file(path):
    with open(path, encoding='utf-8') as fh:
        return count_text(fh.read())


def part_of(name):
    """Номер части по имени файла: chapter.md -> 1, chapter-part3b.md -> 3."""
    m = re.match(r'chapter(?:-part(\d+))?[a-z]*\.md$', name)
    if not m:
        return None
    return int(m.group(1)) if m.group(1) else 1


def count_chapter(directory):
    files = sorted(glob.glob(os.path.join(directory, 'chapter*.md')))
    by_part, by_file = {}, {}
    for p in files:
        n = part_of(os.path.basename(p))
        if n is None:
            continue
        c = count_file(p)
        by_file[os.path.basename(p)] = c
        by_part[n] = by_part.get(n, 0) + c
    return by_part, by_file, sum(by_part.values())


SELFTEST = [
    ('пустое', '', 0),
    ('фронтматтер не считается',
     '---\nlecture: 7\nlength_words: ~84560  # комментарий во фронтматтере\n---\nодно два три\n', 3),
    ('строка заголовка не считается',
     '## Раздел про отбор на обследование\nодно два\n', 2),
    ('хвостовой раздел снимается вместе с вложенными подзаголовками',
     '## Тело\nодно два\n\n## Источники\n1. Автор, журнал\n### Ещё подзаголовок внутри\nсъело бы это\n', 2),
    ('после хвостового раздела счёт возобновляется на заголовке того же уровня',
     '## Источники\nне считать\n## Тело\nодно два три\n', 3),
    # Случай, на котором первый прогон вернул ноль по шести файлам главы из восемнадцати:
    # «## Оглавление» на уровне 2, а всё содержание части — заголовками уровня 3.
    ('оглавление уровня 2 не съедает содержание уровня 3',
     '## Оглавление (часть 2b)\n- [ссылка](#a)\n- [ссылка](#b)\n### § 3.8 Разбор\nодно два три четыре\n', 4),
    ('оглавление кончается на следующем заголовке любого уровня, хвостовой раздел — нет',
     '## Оглавление\n- пункт\n#### Глубокий заголовок\nсчитается пять слов ровно тут\n', 5),
    ('пометка проверки снимается, в том числе многострочная',
     'одно два `[FACT-CHECK: длинная\nпометка на две строки]` три\n', 3),
    ('у ссылки остаётся текст, адрес снимается',
     'см. [реестр разборов](REESTR-RAZBOROV.md) там\n', 4),
    # 2 слова в шапке + 3 в строке данных = 5; строка-разделитель |---|---| не даёт ни одного.
    ('таблица считается, разделитель — нет',
     '| кто | сколько |\n|---|---|\n| радиолог | сорок восемь |\n', 5),
]


def selftest():
    bad = 0
    for name, text, expected in SELFTEST:
        got = count_text(text)
        ok = got == expected
        if not ok:
            bad += 1
        print(f'{"ок " if ok else "СБОЙ"} {name}: ожидалось {expected}, получено {got}')
    if bad:
        print(f'\nсамотест не прошёл: {bad} из {len(SELFTEST)}. Числу этого счётчика верить нельзя.')
        return 1
    print(f'\nсамотест пройден: {len(SELFTEST)} из {len(SELFTEST)}.')
    return 0


def main():
    ap = argparse.ArgumentParser(description='Счёт слов главы по курсовой норме (CLAUDE.md § Chapter Depth Baseline).')
    ap.add_argument('target', nargs='?', help='каталог главы (где лежат chapter*.md) либо отдельный файл')
    ap.add_argument('--parts', action='store_true', help='разбивка по файлам, а не только по частям')
    ap.add_argument('--selftest', action='store_true', help='прогнать случаи с известным ответом')
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.target:
        ap.error('укажите каталог главы или файл (либо --selftest)')
    if os.path.isfile(a.target):
        print(count_file(a.target))
        return 0
    by_part, by_file, total = count_chapter(a.target)
    if not by_part:
        print(f'в {a.target} не найдено ни одного chapter*.md', file=sys.stderr)
        return 2
    if a.parts:
        for name in sorted(by_file):
            print(f'{by_file[name]:>7}  {name}')
        print()
    print('words_by_part: ' + '{' + ', '.join(f'{k}: {v}' for k, v in sorted(by_part.items())) + '}')
    print(f'length_words:  {total}')
    norm = 30000
    print(f'курсовая норма {norm}: ' + ('взята' if total >= norm else f'НЕ взята, недостаёт {norm - total}')
          + f' ({total / norm:.2f}×)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
