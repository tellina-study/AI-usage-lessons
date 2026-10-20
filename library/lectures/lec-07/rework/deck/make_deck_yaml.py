#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Сборка deck.yaml / deck-part2.yaml / deck-part3.yaml из фронтматтера slides/*.md.

Запускать из каталога deck/:  python3 make_deck_yaml.py

Зачем скрипт, а не правка руками. Манифест и файлы кадров -- два описания одного
состава; в Лекции 5 они разошлись на 153 поля и 2 кадра, ничего при этом не сломав,
потому что сборка их не читает. Здесь манифест ВЫГРУЖАЕТСЯ из файлов кадров, и
разойтись может только одно поле -- chapter_ref, которое держится на суждении и
живёт в словаре CHAP ниже (в главе нет маркеров for-slide-sNN, адрес сопоставлен по
содержанию кадра и оглавлениям частей главы).

Перезапускать после КАЖДОЙ правки состава деки или фронтматтера кадров.

Правятся руками три структуры: CHAP (адрес в главе), ACQUIRED (добытые иллюстрации --
дубль deck/images.md 1, там же лицензии) и REAL (кадры, которым по их собственному
media_needed нужен настоящий снимок).
"""
import re, glob, os, io
from collections import OrderedDict

SL = 'slides'
files = sorted(glob.glob(os.path.join(SL, 's*.md')),
               key=lambda f: (int(re.match(r's(\d+)', os.path.basename(f)).group(1)),
                              re.match(r's\d+([a-z]?)', os.path.basename(f)).group(1)))

def fm(path):
    """Фронтматтер кадра → плоский словарь скалярных полей.

    ВСТРОЧНЫЙ КОММЕНТАРИЙ У НЕЗАКАВЫЧЕННОГО ЗНАЧЕНИЯ ОТРЕЗАЕТСЯ, и это не
    косметика. Поле вида `in_bucket: false   # кадр смешанный: охват по
    странам — нейтральная статистика,` попадало в значение ЦЕЛИКОМ, а
    значение идёт в `marks: { … }` — поточную карту YAML. Запятая внутри
    такого комментария рвала карту, и ВЕСЬ `deck.yaml` перестал
    разбираться как YAML: `yaml.parser.ParserError … line 262`. Прожито
    молча: сборщик деки читает `slides/*.md`, а не манифест, поэтому ни
    одно предупреждение сборки на это не указывало, файл на глаз выглядел
    целым, и сломан он был ещё до переезда кадров (проверено на версии из
    `HEAD`). Правило отреза — то же, что в YAML: ` #` вне кавычек
    начинает комментарий.

    Закавыченные значения оставлены как были, нарочно: у них комментарий
    выходит ЗА кавычки (`local_id: "s1-02b"  # вставленный кадр`), в
    поточную карту такие поля не попадают, и как YAML это читается верно.
    """
    t = open(path, encoding='utf-8').read()
    body = t.split('---')[1]
    d = {}
    for line in body.splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m:
            v = m.group(2).strip()
            if not v.startswith('"'):
                v = re.split(r'\s+#', v, maxsplit=1)[0].strip()
            if v.startswith('"') and v.endswith('"') and len(v) > 1:
                v = v[1:-1]
            d[m.group(1)] = v
    return d


def razbiraetsya(fn):
    """МЕРА БЕРЁТСЯ С ВЫВОДА: разбирается ли ЗАПИСАННЫЙ файл как YAML.

    Манифест читают другие инструменты, а не сборщик деки, поэтому
    сломанный `deck.yaml` не вызывает ни одного предупреждения сборки и
    живёт незамеченным — именно так он и прожил круг с поточной картой,
    порванной запятой из встрочного комментария (см. `fm`). Проверка
    стоит здесь, а не отдельным сторожем, чтобы отчёт о записи файла и
    отчёт о его годности были одной строкой и расходиться не могли.
    """
    import yaml
    try:
        yaml.safe_load(open(fn, encoding='utf-8'))
        return '· YAML разбирается'
    except Exception as e:
        return '· YAML НЕ РАЗБИРАЕТСЯ: %s' % str(e).splitlines()[0]

# ── адрес в главе: § и файл части ────────────────────────────────────────
CHAP = {
 's01': 'chapter.md § Введение',
    's01a': 'chapter.md § Обзор предмета (цикл оказания медицинской помощи)',
    's01b': 'chapter.md § Обзор предмета (как получают данные · классические режимы) + chapter-part1b.md §1.2 + chapter-part1c.md §2.1, chapter-part2.md §3.1, chapter-part3.md §4.2, chapter-part3b.md §5.1–5.2, chapter-part3c.md §6.3',
    's11a': 'chapter-part1b.md § Раздел 1 (вводка), §1.1, §1.2, §1.3 + chapter.md § Обзор предмета (три опоры порядка)',
    's12a': 'chapter-part1b.md § Скрининговые программы по странам и участие ИИ',
    's12b': 'chapter-part1b.md § Раздел 1 (вводка) — новый материал (issue #278 §10.2): происхождение скрининга как класса практики (Wilson–Jungner 1968, массовая флюорография Глазго 1957, Reiser 1978) пока не отражён в тексте главы, добавлен только в деку',
    's15a': 'chapter-part1b.md §1.4 (продолжение разбора s15: арбитраж, асимметрия доверия, честный пробел обучения/обновления/дрейфа)',
    's16a': 'chapter-part1b.md §1.5 (продолжение разбора s16: опубликованная архитектура — вероятностный граф и правила для красных флагов)',
    's18b': 'chapter-part1b.md §1.6 (продолжение разбора s18/s18a: архитектура EyeArt, пост-маркетинговое обновление 510(k) K213037, германское измерение чувствительности к популяции)',
    's22a': 'chapter-part1c.md § Раздел 2 (вводка), §2.1, §2.2, §2.4',
    's60ba': 'chapter-part3b.md § Раздел 5 (вводка), §5.1, §5.2',
    's60bb': 'chapter-part3b.md §5.2 (три классических режима; доля текста по Steinkamp 2022 и Wang 2017)',
    's73ca': 'chapter-part5.md § Раздел 10 (вводка), §10.1',
 's03': 'chapter.md §0.2',
 's05': 'chapter.md §0.4',
 's05a': 'chapter-part5b.md §11.1, §11.2',
 's11': 'chapter-part1b.md § Раздел 1 (вводка)',
 's12': 'chapter-part1b.md §1.1, §1.2, §1.3',
 's13': 'chapter-part1b.md §1.3',
 's15': 'chapter-part1b.md §1.4',
 's16': 'chapter-part1b.md §1.5',
 's18': 'chapter-part1b.md §1.6',
 's19': 'chapter-part1b.md §1.6а (отечественный разбор: Москва, модель на месте второго читателя маммограмм — что за случай, устройство, цена, оба классических режима)',
 's19a': 'chapter-part1b.md §1.6а (продолжение разбора s19: контур допуска и пересмотра — пять калибровок, четыре версии, состав технических отказов, нюансы надёжности, что переехало)',
 's20': 'chapter-part1b.md §1.7',
 's22': 'chapter-part1c.md § Раздел 2 (вводка), §2.1',
 's24': 'chapter-part1c.md §2.2, §2.3',
  's26': 'chapter-part1c.md §2.4',
 's26a': 'chapter-part1c.md §2.5',
 's27': 'chapter-part1c.md §2.5а',
 's27a': 'chapter-part1c.md §2.5б',
 's27b': 'chapter-part1c.md §2.5б',
 's27c': 'chapter-part1c.md §2.5в',
 's28': 'chapter-part1c.md §2.6',
 's30': 'chapter-part1c.md §2.7',
 's30a': 'chapter-part1c.md §2.7',
 's31': 'chapter-part1c.md §2.8',
 's33': 'chapter-part1c.md §2.9',
 's33a': 'chapter-part1c.md §2.9 (рабочее правило — четыре вопроса)',
 's35': 'chapter-part2.md § Раздел 3 (вводка), §3.1',
 's36': 'chapter-part2.md §3.1',
 's37': 'chapter-part2.md §3.1',
 's38': 'chapter-part2.md §3.2 (+ chapter.md §0.4)',
 's41': 'chapter-part2.md §3.4',
 's44': 'chapter-part2.md §3.7',
 's47': 'chapter-part2b.md §3.9',
 's49': 'chapter-part2b.md §3.10, §3.11',
 's49a': 'chapter-part2.md §3.3',
 's49b': 'chapter-part4d.md §8.8',
 's49e': 'chapter-part3.md §4.1-§4.5 (устройство шкалы, цена обеих ошибок, счёт режимов, модель)',
 's49f': 'chapter-part3.md §4.6-§4.9 (арифметика потока, вторая проверка, что переехало)',
 's49g': 'chapter-part2b.md §3.11а (отечественный разбор: Москва, AIDA — заключительный диагноз по медкарте; устройство, набор кодов, классический режим, отказ модели отвечать)',
 's49h': 'chapter-part2b.md §3.11а (продолжение разбора s49g: точка расхождения врача и модели, трудные случаи, строгий счёт против синонимичного, что переехало)',
 's49d': 'chapter-part2.md § Раздел 3 (вводка), §3.3, §3.4 + chapter-part2b.md §3.8 + chapter-part4d.md §8.8',
 's50': 'chapter-part2b.md §3.12, §3.13',
 's60b': 'chapter-part3b.md § Раздел 5 (вводка), §5.1',
 's60c': 'chapter-part3b.md §5.1, §5.2',
 's61': 'chapter-part3b.md §5.3, §5.4',
 's62': 'chapter-part3b.md §5.6 (+ §5.5)',
 's63': 'chapter-part3b.md §5.7',
 's63a': 'chapter-part3b.md §5.8 (+ §5.7)',
 's64': 'chapter-part3b.md §5.9 (+ §5.8)',
 's73b': 'chapter-part5.md § Раздел 10 (вводка), §10.1',
 's73c': 'chapter-part5.md §10.2 (+ §10.3)',
 's73d': 'chapter-part5.md §10.4, §10.5',
 's73da': 'chapter-part5.md § Удержание квалификации по странам (безномерный подраздел между §10.5 и §10.5а)',
 's73f': 'chapter-part5.md §10.6, §10.8 (+ §10.7)',
 's73ga': 'chapter-part5.md §10.8а',
 's73i': 'chapter-part5.md §10.14 (+ §10.8, §10.11, §10.13)',
 's73j': 'chapter-part5.md §10.13 (+ §10.14) — различение двух режимов одного класса инструмента; кадр переставлен ПЕРЕД сводом стадии, файл кадра лежит под именем s73gb, идентификатор показа прежний',
 's96a': 'chapter-part5b.md § Раздел 11 (вводка), §11.1',
 's97': 'chapter-part5b.md §11.1, §11.2, §11.3',
 's101': 'chapter-part5b.md §11.6',
 's102': 'chapter-part5b.md §11.7',
 's103': 'chapter-part5b.md §11.8',
 's104': 'chapter-part5b.md §12.1',
 's105': 'chapter-part5b.md §12.2',
 's106': 'chapter-part5c.md § Вопросы и ответы для самопроверки (+ chapter-part5b.md §12.4)',
}


_CHISLO = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть',
           7: 'семь', 8: 'восемь', 9: 'девять'}


def uncovered_part4():
    """Файлы главы `chapter-part4*`, в которые не ведёт ни один `chapter_ref`.

    Считается с диска, а не вписано в примечание словами: ровно эту строку уже
    однажды обогнала жизнь. Разрез `chapter-part4.md` по лимиту 600 строк добавил
    `chapter-part4a.md`, а примечание продолжало говорить «четыре файла» и
    перечислять четыре имени — то есть производное было набрано руками и потому
    соврало при первом же изменении состава главы. Возвращает готовую пару
    (перечень имён, число словом) под подстановку в текст примечания.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    chap_dir = os.path.dirname(here)
    names = sorted(os.path.basename(p) for p in
                   glob.glob(os.path.join(chap_dir, 'chapter-part4*.md')))
    covered = {n for n in names if any(n in v for v in CHAP.values())}
    miss = [n for n in names if n not in covered]
    shown = ', '.join([miss[0]] + ['-' + n[len('chapter-'):-len('.md')]
                                   for n in miss[1:]]) if miss else 'ни один файл'
    k = len(miss)
    slovo = 'файл' if k % 10 == 1 and k % 100 != 11 else (
        'файла' if k % 10 in (2, 3, 4) and k % 100 not in (12, 13, 14)
        else 'файлов')
    return shown, '%s %s' % (_CHISLO.get(k, str(k)), slovo)

def sostav():
    """Состав деки, посчитанный с диска: всего кадров, сколько из них номера плана,
    сколько вставлено с буквенным суффиксом, и их перечень.

    Набранный руками состав здесь уже один раз соврал: примечание говорило «110 кадров
    = 106 номеров плана + 4 вставленных» и перечисляло s60a/s60b/s96a/s103a, когда на
    диске лежало 109 кадров, 91 номер плана и 18 вставленных — девять сессий переделали
    деку, а производное примечание об этом не узнало. То же, что уже случилось с
    примечанием про `chapter-part4*` (см. `uncovered_part4`), и лечится тем же.
    """
    nums = [s for s, lid in PLAN_LID.items() if lid]
    ins = sorted((s for s, lid in PLAN_LID.items() if not lid),
                 key=lambda s: (int(re.match(r's(\d+)', s).group(1)),
                                re.match(r's\d+([a-z]*)', s).group(1)))
    return len(PLAN_LID), len(nums), len(ins), ins


def chapter_files():
    """Сколько файлов главы лежит на диске: chapter.md плюс все chapter-part*.md."""
    here = os.path.dirname(os.path.abspath(__file__))
    chap_dir = os.path.dirname(here)
    return len(glob.glob(os.path.join(chap_dir, 'chapter*.md')))

def plural(n, one, few, many):
    """Согласование существительного с числом: 1 группа · 2 группы · 5 групп."""
    if n % 100 in (11, 12, 13, 14):
        return many
    if n % 10 == 1:
        return one
    if n % 10 in (2, 3, 4):
        return few
    return many

def dup_titles():
    """Группы кадров, несущих дословно одинаковый `title`.

    Считается с диска: прежняя редакция D5 называла одну пару поимённо (s18/s19), и
    переделка деки эту пару развела, а восемь вернувшихся карт стадии завели два новых
    дубля по три и по пять кадров — запись о расхождении при этом не поменялась ни
    словом. Набранный руками перечень расхождений расходится с диском ровно так же, как
    любое другое производное.
    """
    byt = OrderedDict()
    for f in files:
        d = fm(f)
        byt.setdefault(d.get('title', ''), []).append(d['id'])
    return [(ti, ids) for ti, ids in byt.items() if len(ids) > 1]


def sluzhebnye_assertion():
    """Кадры, у которых в `assertion` стоит не утверждение кадра, а служебная пометка."""
    out = []
    for f in files:
        d = fm(f)
        a = d.get('assertion', '')
        if 'провисает' in a or 'под рез' in a:
            out.append((d['id'], 'шаг ②' if 'провисает' in a else 'под рез'))
    return out


def wired_slides():
    """Кадры, у которых поле `media` заполнено, то есть снимок реально встаёт в сборку."""
    return [fm(f)['id'] for f in files if (fm(f).get('media') or '').strip()]

# Адрес кадра в SLIDE-PLAN.md берётся ИЗ `local_id` КАДРА, а не из его позиции в деке.
#
# Прежняя редакция считала номер плана позиционно — «сколько кадров с чисто числовым `id`
# прошло до этого» — и потому врала при любом изменении состава: на сборке 2026-10-13
# кадры «Сборки» (`s97` `s99` `s101` `s102` `s103`) выходили с пометкой
# `plan_section: "Раздел 6. Лекарство"`, а `s74`, дивайдер самого раздела о лекарстве, —
# с «Раздел 4. Что решили». Дека разошлась с планом на пятнадцать номеров, и позиционный
# счёт сдвинулся весь целиком. Поймано перезом R1 (2026-10-14), который сдвинул состав ещё
# раз и сделал ложь видимой.
#
# `local_id` — это и есть идентификатор кадра В ПЛАНЕ (`В-05`, `s6-03`, `s5-01`), он лежит
# в файле кадра и переездом кадра по деке не меняется. Поэтому раздел плана читается из его
# приставки, а «номер плана против вставленного каркасом кадра» — по наличию буквенного
# хвоста у самого `local_id` (`s6-03` — номер плана, `s6-03a` — вставленный).
PLAN_LID = {}
for f in files:
    _d = fm(f)
    _lid = (_d.get('local_id') or '').strip()
    PLAN_LID[_d['id']] = _lid if re.fullmatch(r'(В|s\d)-\d+', _lid) else None

# приставка `local_id` → имя раздела в SLIDE-PLAN.md
PLAN_SEC = {'В': 'Раздел 0. Вход',
            's1': 'Раздел 1. Кто попадает в поле зрения',
            's2': 'Раздел 2. Что про человека измерили',
            's3': 'Раздел 3. Кто это прочёл: человек и модель',
            's4': 'Раздел 4. Что решили и кто это заметил',
            's5': 'Раздел 5. Что стало с теми, кто решает',
            's6': 'Раздел 6. Лекарство',
            's7': 'Раздел 7. Чем удерживают',
            's8': 'Раздел 8. Сборка',
            's9': 'Раздел 9. Закрытие'}


def plan_sec(sid):
    """Раздел плана для кадра — по приставке его `local_id`. Работает и для вставленных
    кадров: вставка `s6-07a` принадлежит тому же разделу плана, что и `s6-07`."""
    lid = (fm_by_sid.get(sid) or '')
    pref = lid.split('-')[0] if '-' in lid else ''
    return PLAN_SEC.get(pref)


fm_by_sid = {fm(f)['id']: (fm(f).get('local_id') or '').strip() for f in files}

def q(s):
    s = str(s).replace('\\', '\\\\').replace('"', '\\"')
    return '"%s"' % s

from collections import Counter
REAL = set("""
s01 s11 s12 s13 s16 s18 s22 s26 s28 s31
s36 s41 s44 s47 s49 s49a s60b s61 s63 s73b
s73c s73d s73f s105
""".split())
ACQUIRED = {
 's01':'rework/deck/assets/s01-hero-chtenie-mammogrammy.jpg',
 's18':'rework/deck/assets/s18-fundus-kamera-v-kabinete.jpg',
 's22':'rework/deck/assets/s22-rentgenkabinet-pacient-u-pribora.jpg',
 's26':'rework/deck/assets/s26-tekhnik-stavit-cheloveka-k-priboru.jpg',
 's49a':'rework/deck/assets/s40-dva-effekta-s-intervalami.png',
 's44':'rework/deck/assets/s44-srez-razmetka-cheloveka-i-modeli.png',
 's73b':'rework/deck/assets/s88-endoskopicheskiy-kabinet.jpg',
 's105':'rework/deck/assets/s105-hero-uvedomlenie-ob-otzyve-izdeliya-verkh.png'}
secs = OrderedDict()
for f in files:
    d = fm(f); secs.setdefault(d['section'], []).append((f, d))
flat = [(f, d) for v in secs.values() for f, d in v]
tot_slides = len(flat)
tot_min = sum(float(d['timing_min']) for _, d in flat)
in_min = sum(float(d['timing_min']) for _, d in flat if d['in_bucket'] == 'true')

def q(s):
    s = str(s).replace('\\', '\\\\').replace('"', '\\"')
    return '"%s"' % s

HDR = """# library/lectures/lec-07/rework/deck/{fn}  —  часть {i} из 3
#
# Служебный манифест деки Лекции 7 «Решение о человеке: кто смотрит, кто подписывает,
# кто платит». Issue #229 · ветка issue-lec-07-rework.
"""

PREAMBLE = """#
# ЧТО ЭТО. Опись {vsego} кадров деки со служебными полями на каждый: идентификатор, тип
# кадра, заголовок, раздел, адрес в главе (`chapter_ref`) и `timing_min`. Тайминг и
# методические поля живут ЗДЕСЬ и во фронтматтере файла кадра — на видимом слое кадра
# они запрещены (CLAUDE.md § «No Timing / No Methodology in Slides»), и переносить их
# туда нельзя.
#
# ЧЕМ ЭТО НЕ ЯВЛЯЕТСЯ — входом сборки. `build_lec07.py` читает фронтматтер
# `slides/*.md` и не импортирует этот файл ни одной строкой. Устройство то же, что в
# Лекции 5, и там же записано, чем оно опасно: два описания одного состава способны
# разойтись, ничего не сломав. Поэтому КАЖДОЕ поле ниже выгружено из фронтматтера
# файла кадра программой, а не набрано руками. Исключение одно — `chapter_ref`: в
# главе нет маркеров `[for-slide-sNN]`, и адрес сопоставлен по содержанию кадра и
# оглавлениям частей главы. Это единственное поле манифеста, которое держится на
# суждении, и проверять при расхождении надо его.
#
# СОСТАВ, посчитанный с диска: {vsego} кадров. Номеров `SLIDE-PLAN.md` (slides-v3)
# среди них — {nums} из 106; остальные {nins} кадров каркас ВСТАВИЛ, и у них номера в плане
# нет: это кадры, чей `local_id` несёт буквенный хвост (`s6-07a` — вставка к номеру `s6-07`).
# Считается это по `local_id`, а не по идентификатору показа: `id` говорит, где кадр СТОИТ,
# `local_id` — какое место плана он занимает, и после переза R1 эти две вещи окончательно
# разошлись. Снятый номер не переиспользуется: на идентификаторы ссылаются манифесты, разборы
# прожарок и другие сессии, поэтому в номерах плана зияют пропуски — {propusk} номеров плана
# в деке нет, причина по каждому в `slides/_snyato/README.md` и `slides-snyatye/README.md`.
# Вставленные: {ins_list}.
# Что делает каждый — в его собственной записи ниже (`type`, `title`, `section`); списком
# здесь это не повторяется, потому что набранный руками список состава тут уже соврал.
#
# НУМЕРАЦИЯ РАЗДЕЛОВ РАСХОДИТСЯ ТРОЯКО, и это не ошибка выгрузки:
#   deck (файлы кадров) — порядок показа, 0…10, сквозной;
#   SLIDE-PLAN.md       — номера разделов главы при порядке показа 0→1→2→3→4→7→6→5→8→9;
#                         порядок показа после переза R1 — 0→1→2→3→4→5→6→7→8→9→10, где
#                         раздел показа 7 — «Профессиональная квалификация: поддержание и
#                         износ» (план зовёт его
#                         Разделом 5 и даёт ему номера 88–96; в деке эти кадры лежат под
#                         идентификаторами s73b…s73j, чтобы порядок показа читался по id);
#   chapter             — 0…12, включая §7 «Назначение и лечение» и §8 «Оперативная
#                         помощь», у которых в деке НЕТ ни одного кадра (решения П9/П11,
#                         шаг реза А1 в CUT-ORDER.md §2).
# `section` — имя раздела показа; `plan_section` печатается только там, где план зовёт
# это место иначе; `chapter_ref` — адрес в главе в её собственной нумерации.
#
# КАК ЧИТАТЬ ПОЛЕ `marks`: `in_bucket` — кадр целиком внутри ведра провалов и границ
# (partial → false, рубрика `fix-brief.md` §5) · `vfy` — на кадре есть число под
# пересверку в день лекции · `status` — состояние файла кадра · `media_status` — одно из
# `acquired` (снимок добыт, лежит в `deck/assets/`, путь в `media_asset`, лицензия в
# `deck/images.md` §1) · `real_image_needed` (кадр просит настоящий снимок, не добыт) ·
# `builder_drawn` (схема, плашки, матрица — снимок не нужен) · `no_decision` (поле
# `media_needed` в файле кадра пусто, вопрос не задавали).
#
# ЧАСТИ: deck.yaml (мета + разделы 0–2) · deck-part2.yaml (разделы 3–6) ·
#        deck-part3.yaml (разделы 7–10 + totals + divergences).
"""

def slide_block(f, d, W, cur):
    sid = d['id']
    W("  - id: %s\n" % sid)
    no = PLAN_LID.get(sid)
    W("    local_id: %-28s %s\n" % (q(d.get('local_id','')),
                                    "# номер SLIDE-PLAN.md" if no
                                    else "# вставленный кадр, номера в плане нет"))
    W("    file: %s\n" % ('slides/' + os.path.basename(f)))
    W("    type: %s\n" % d['type'])
    W("    title: %s\n" % q(d.get('title','')))
    ps = plan_sec(sid)
    if ps and ps.split('.')[0].replace('Раздел ','') != cur.split('.')[0]:
        W("    plan_section: %s\n" % q(ps))
    W("    chapter_ref: %s\n" % q(CHAP.get(sid,'НЕ СОПОСТАВЛЕН')))
    W("    timing_min: %s\n" % d['timing_min'])
    mn = (d.get('media_needed') or '').strip()
    if sid in ACQUIRED: ms = 'acquired'
    elif sid in REAL:   ms = 'real_image_needed'
    elif mn:            ms = 'builder_drawn'
    else:               ms = 'no_decision'
    mv = (d.get('media') or '').strip()
    W("    marks: { in_bucket: %s, vfy: %s, status: %s, media_status: %s }\n"
      % (d['in_bucket'], d['vfy'], q(d['status']), ms))
    if sid in ACQUIRED:
        W("    media_asset: %s%s\n" % (q(ACQUIRED[sid]),
          "" if mv else "   # поле media в файле кадра ещё пусто, см. deck/images.md §1"))

# Разделы после слияния 2+3 (#229, указание А владельца): стадийных разделов
# семь вместо восьми, нумерация 4-10 съехала на 3-9. Разбивка по трём манифестам
# пересобрана по числу кадров: 30 · 30 · 24.
#
# ПЕРЕНУМЕРОВАНО ПРИ СЛИЯНИИ РАЗДЕЛОВ 1 и 2/3 (#285). Раздел 2/3 разрезал прежний
# «2. Исследование и постановка диагноза» на две настоящие стадии главы — «2.
# Инструментальная и лабораторная диагностика» и «3. Постановка диагноза» (коммит
# 9f43c43b0, канон #286 §14), и нумерация ниже съехала на единицу. Этот перечень
# НИ НА ОДНОЙ из двух веток обновлён не был, и обе оставили его прежним: сборка
# падала `KeyError: '2. Исследование и постановка диагноза'`, то есть манифесты
# не пересобирались с самого разреза — закоммиченный `deck-part3.yaml` раздела
# 2/3 всё ещё называл «5. Итоги», тогда как Итоги стали шестым разделом.
# Состав каждого манифеста при этом СОХРАНЁН: где стоял прежний раздел 2, теперь
# стоят оба его куска, а остальные разделы только сменили номер.
SPLIT = [
    ('deck.yaml',       ['0. Вход','1. Первичный скрининг и отбор на обследование','2. Инструментальная и лабораторная диагностика','3. Постановка диагноза']),
    ('deck-part2.yaml', ['4. Ведение медицинской документации','5. Профессиональная квалификация: поддержание и износ']),
    ('deck-part3.yaml', ['6. Итоги','7. Закрытие']),
]

for i, (fn, seclist) in enumerate(SPLIT, 1):
    o = io.StringIO(); W = o.write
    W(HDR.format(fn=fn, i=i))
    if i == 1:
        _v, _n, _i, _il = sostav()
        W(PREAMBLE.format(vsego=_v, nums=_n, nins=_i, propusk=106 - _n,
                          ins_list=' · '.join(_il)))
    else:
        W("#\n# Продолжение `deck.yaml`. Устройство, оговорки и правило чтения полей — в части 1;\n")
        W("# здесь только записи кадров%s.\n" % (" плюс сводка, расхождения и порядок реза" if i == 3 else ""))
    W("\n")

    if i == 1:
        W("deck:\n")
        W("  lecture_number: 7\n")
        W("  issue: 229\n")
        W("  title: \"Лекция 7. Решение о человеке: кто смотрит, кто подписывает, кто платит\"\n")
        W("  language: ru\n")
        W("  status: karkas\n")
        W("  version: deck-v1-karkas\n")
        W("  slot_min: 90\n")
        W("  qa_min: 10\n")
        W("  content_target_min: 80.00      # слот минус вопросы; цель CUT-ORDER.md §1.1\n")
        W("  total_slides: %d\n" % tot_slides)
        W("  plan_slides: 106               # номеров в SLIDE-PLAN.md; в деке стоит %d из них\n"
          % sostav()[1])
        W("  inserted_slides: [%s]\n" % ', '.join(sostav()[3]))
        W("  sum_timing_min: %.2f           # сложено по timing_min файлов кадров\n" % tot_min)
        W("  axis: \"путь одного решения о человеке: удешевили чтение данных — платят вниманием, навыком, подписью и арбитражем\"\n")
        W("  central_question: \"Модель посмотрела первой. Что теперь делает человек — и кто это измерял?\"\n")
        W("  curriculum_level: \"отраслевая лекция L7; strict-in ≥30% обязателен, waiver недоступен\"\n")
        W("  deck_parts: [deck.yaml, deck-part2.yaml, deck-part3.yaml]\n")
        W("  builder: deck/build_lec07.py   # читает slides/*.md, НЕ этот файл\n")
        W("  sources:\n")
        W("    chapter_parts: %d            # chapter.md + файлы chapter-part*.md, сочтено с диска\n"
          % chapter_files())
        W("    plan: SLIDE-PLAN.md\n")
        W("    plan_tables: [SLIDE-PLAN-table.md, SLIDE-PLAN-desc-A.md, SLIDE-PLAN-desc-B.md, SLIDE-PLAN-desc-C.md]\n")
        W("    block_plans: plans/          # поимённые минуты кадров\n")
        W("    cut_order: CUT-ORDER.md\n")
        W("    decisions: decisions-owner.md\n")
        W("    images: deck/images.md\n")
        W("  generator: deck/make_deck_yaml.py   # выгружает ЭТОТ файл из slides/*.md; перезапускать после правок фронтматтера\n")
        W("\n")
        W("palette:                         # Ocean Gradient, зафиксирована курсом\n")
        W("  primary_deep: \"#21295C\"\n")
        W("  primary_mid: \"#065A82\"\n")
        W("  primary_light: \"#1C7293\"\n")
        W("  teal: \"#028090\"\n")
        W("  gold: \"#F0AB00\"                # не реже раза на кадр, проверяется сборщиком\n")
        W("  surface: \"#F4F7FA\"\n")
        W("  background: \"#FFFFFF\"\n")
        W("\n")
        W("motif:\n")
        W("  type: ocean_rounded_box        # на содержательных кадрах; на обложке мотива нет\n")
        W("  radius_pt: 12\n")
        W("  stroke: \"#1C7293\"\n")
        W("  surface: \"#F4F7FA\"\n")
        W("\n")
        W("slide_types:                     # значения поля type, с числом кадров\n")
        tc = Counter(d['type'] for _, d in flat)
        TD = {'cover':'обложка','case':'разбор или картина работы','summary':'вывод раздела или свод',
              'norm':'норматив, устройство, правило','map':'карта стадии или сетка курса',
              'comparison':'два столбца «что получается / что не получается»',
              'divider':'дивайдер раздела','question':'вопрос залу или вопросы в конце'}
        for t, c in sorted(tc.items(), key=lambda x: -x[1]):
            W("  %-12s { count: %3d, meaning: %s }\n" % (t + ':', c, q(TD.get(t,'—'))))
        W("\n")
        W("sections:                        # разделы показа: кадров и минут, сложено по файлам\n")
        for s, v in secs.items():
            m = sum(float(d['timing_min']) for _, d in v)
            W("  - { name: %s,\n" % q(s))
            W("      slides: %d, timing_min: %.2f, range: [%s, %s] }\n" % (len(v), m, v[0][1]['id'], v[-1][1]['id']))
        W("\n")

    W("slides:\n")
    for s in seclist:
        W("\n  # ─── %s · %d кадров · %.2f мин ───\n"
          % (s, len(secs[s]), sum(float(d['timing_min']) for _, d in secs[s])))
        for f, d in secs[s]:
            slide_block(f, d, W, s)

    if i == 3:
        W("\n")
        W("totals:\n")
        W("  slides: %d\n" % tot_slides)
        W("  timing_min: %.2f               # сложено по файлам кадров\n" % tot_min)
        W("  plan_budget_min: 80.00         # заявлено CUT-ORDER.md §1.1 для 106 кадров плана\n")
        W("  plan_frames_only_min: %.2f     # только номера плана, без вставленных кадров\n"
          % (tot_min - sum(float(d['timing_min']) for _, d in flat if not re.fullmatch(r's\d+', d['id']))))
        W("  plus_qa_min: %.2f\n" % (tot_min + 10))
        W("  slot_min: 90\n")
        W("  overrun_min: %.2f              # против слота 90 с десятью минутами вопросов\n" % (tot_min + 10 - 90))
        W("  strict_in_min: %.2f\n" % in_min)
        W("  strict_in_share: \"%.1f%%\"      # порог курса 30%%; счёт по минутам, partial → out\n" % (100*in_min/tot_min))
        W("  vfy_slides: %d                 # кадров с числом под пересверку в день лекции\n"
          % sum(1 for _, d in flat if d['vfy'] == 'true'))
        W("  by_status:\n")
        for k, c in sorted(Counter(d['status'] for _, d in flat).items(), key=lambda x: -x[1]):
            W("    %s: %d\n" % (q(k), c))
        W("  media:                         # разбор и адреса — deck/images.md\n")
        W("    acquired: %d                   # лежит в deck/assets/, лицензия проверена поимённо\n" % len(ACQUIRED))
        W("    real_image_needed: %d          # просит настоящий снимок по своему media_needed, не добыт\n" % len(REAL - set(ACQUIRED)))
        W("    builder_drawn: %d              # схема, плашки, матрица, таблица — снимок не нужен\n"
          % sum(1 for _, d in flat if d['id'] not in REAL and (d.get('media_needed') or '').strip()))
        W("    no_decision: %d                # media_needed пусто: вопрос не задавали\n"
          % sum(1 for _, d in flat if not (d.get('media_needed') or '').strip()))
        W("    wired: %d                     # поле media в файле кадра заполнено, кадр реально встаёт в сборку\n"
          % sum(1 for _, d in flat if (d.get('media') or '').strip()))
        _w = wired_slides()
        W("    note: \"поле media заполнено у %d кадров — %s; счёт сделан по диску. Расхождение, которое из этого видно: словарь ACQUIRED этого генератора знает %d пути, то есть media_status = acquired выставлен не всем кадрам, у которых снимок реально встаёт в сборку. ACQUIRED — дубль deck/images.md §2, и сверять его с §2 и с deck/assets/ — отдельная работа, не правка chapter_ref\"\n"
          % (len(_w), ', '.join(_w), len(ACQUIRED)))
        W("\n")
        W("# РАСХОЖДЕНИЯ плана, файлов кадров и арифметики реза. Выписаны, НЕ исправлены:\n")
        W("# манифест описывает то, что есть на диске, а решение по каждому — владельца.\n")
        W("# D1 (issue #229) закрыт ПРАВИЛЬНОЙ стороной: предыдущий круг перенёс s18/s19\n")
        W("# (глазное дно) физически в раздел 2, доверившись их собственному (ошибочному) полю\n")
        W("# section вместо проверки его по fix-brief.md §1 — решения П6/П7 decisions-owner.md\n")
        W("# к этому случаю не относятся, они про границу «анализ данных» ↔ «постановка\n")
        W("# диагноза». fix-brief.md §1/§14 закрепляет глазное дно за разделом 1 (s1-08);\n")
        W("# глава (chapter-part1b.md §1.6) независимо подтверждает то же место. Файлы\n")
        W("# s18…s29 возвращены на дооктябрьские номера — физический порядок снова совпадает\n")
        W("# и с полем section, и со SLIDE-PLAN.md, и с §1.6/§2.6 главы. На диске этого\n")
        W("# расхождения больше нет.\n")
        W("divergences:\n")
        W("  - id: D2\n")
        W("    what: \"сумма timing_min по файлам — %.2f против 80,00, заявленных CUT-ORDER.md §1.1 для 106 кадров\"\n" % (tot_min - 2.15))
        W("    evidence: \"по поимённым минутам планов блоков: лекарство 10,50 против 13,20 по файлам (+2,70); сборка 4,90 против 5,80 (+0,90); удерживают 8,60 против 8,80 (+0,20); отбор 8,20 против 8,30; ядро 12,75 против 12,85; измерили 9,75 против 9,60 (−0,15)\"\n")
        W("    effect: \"перебор слота %.2f минуты (%.2f + 10 против 90), а не 1,25, как считает CUT-ORDER.md §1.1\"\n" % (tot_min+10-90, tot_min))
        W("    effect_2: \"лестница А (шаги А2 + А3 = −1,50 по файлам) цель не берёт: остаётся %.2f + 10 = %.2f\"\n" % (tot_min-1.50, tot_min-1.50+10))
        W("    fix: \"решение владельца: либо вернуть поимённые минуты планов в файлы кадров, либо пересчитать CUT-ORDER.md от %.2f\"\n" % tot_min)
        W("  - id: D3\n")
        W("    what: \"s96a и s103a (дивайдеры «Сборки» и «Закрытия», 0,90 минуты вдвоём) в арифметике CUT-ORDER.md §1.1 не числятся\"\n")
        W("    evidence: \"§1.1 считает +2 структурных кадра перегруппировки (0,50 + 0,75 = 1,25) — это s60b и s60a; про s96a и s103a там ни строки\"\n")
        W("    effect: \"объявленный состав 108 кадров против %d на диске\"\n" % tot_slides)
        W("    fix: \"дописать два кадра в состав CUT-ORDER.md §1.1\"\n")
        W("  - id: D4\n")
        W("    what: \"у главы есть разделы 7 «Назначение и лечение» (§7.1–7.19) и 8 «Оперативная помощь» (§8.1–8.16), а в деке на них ноль кадров\"\n")
        W("    evidence: \"решение П9 называет это невыполненным обещанием кадра s07 (сам кадр снят при сокращении входа, в деке его нет); шаг реза А1 CUT-ORDER.md §2 предъявляет их прочерком\"\n")
        W("    effect: \"chapter_ref ни одного кадра не ведёт в %s — %s главы декой не покрыты\"\n" % (uncovered_part4()))
        W("    fix: \"известное решение, не находка: прочерк по варианту (б) REGROUP.md §4 (поправка П4)\"\n")
        _dups = dup_titles()
        W("  - id: D5\n")
        W("    what: \"%d %s кадров несут дословно одинаковый title; счёт сделан по диску, не вписан словами\"\n"
          % (len(_dups), plural(len(_dups), 'группа', 'группы', 'групп')))
        if _dups:
            W("    evidence:\n")
            for _ti, _ids in _dups:
                W("      - %s  # %d %s: %s\n" % (q(_ti), len(_ids),
                  plural(len(_ids), 'кадр', 'кадра', 'кадров'), ', '.join(_ids)))
        else:
            W("    evidence: \"дублей title на диске нет\"\n")
        W("    effect: \"дивайдер и карта слайдов называют разные кадры одним именем без номера — расходится с правилом §5.16 «имена дословно совпадают с заголовками кадров», как только половины понадобится различить поимённо. Прежняя редакция этой записи называла пару s18/s19: переделка деки её развела, а восемь вернувшихся карт стадии завели дубли крупнее\"\n")
        W("    fix: \"не входит в issue #229; решение владельца — развести заголовки карт по имени стадии («Карта стадии: наблюдение») или оставить как есть\"\n")
        _sl = sluzhebnye_assertion()
        W("  - id: D6\n")
        W("    what: \"у %d %s в assertion стоит не утверждение кадра, а служебная пометка («[шаг ② провисает: …]» или «под рез (П11)»); счёт сделан по диску\"\n"
          % (len(_sl), plural(len(_sl), 'кадра', 'кадров', 'кадров')))
        W("    evidence: \"%s\"\n" % ('; '.join('%s — %s' % (i, k) for i, k in _sl)
                                       if _sl else 'служебных пометок в assertion на диске не осталось'))
        W("    effect: \"поле assertion служебное и на экран не идёт, но для критика и для речи это не утверждение кадра\"\n")
        W("    fix: \"при сборке содержания вписать утверждение, пометку перенести в отдельное поле\"\n")
    open(fn, 'w', encoding='utf-8').write(o.getvalue())
    print(fn, len(o.getvalue().splitlines()), 'строк', razbiraetsya(fn))
