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
    t = open(path, encoding='utf-8').read()
    body = t.split('---')[1]
    d = {}
    for line in body.splitlines():
        m = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if m:
            v = m.group(2).strip()
            if v.startswith('"') and v.endswith('"') and len(v) > 1:
                v = v[1:-1]
            d[m.group(1)] = v
    return d

# ── адрес в главе: § и файл части ────────────────────────────────────────
CHAP = {
 's01': 'chapter.md § Введение',
 's02': 'chapter.md §0.1',
 's03': 'chapter.md §0.2',
 's04': 'chapter.md §0.3',
 's05': 'chapter.md §0.4',
 's06': 'chapter.md §0.5',
 's07': 'chapter.md §0.6',
 's08': 'chapter.md §0.10',
 's09': 'chapter.md § Карта главы, §0.11',
 's10': 'chapter.md §0.8, §0.9',
 's11': 'chapter-part1b.md § Раздел 1 (вводка)',
 's12': 'chapter-part1b.md §1.1, §1.2',
 's13': 'chapter-part1b.md §1.3',
 's14': 'chapter-part1b.md §1.3',
 's15': 'chapter-part1b.md §1.4',
 's16': 'chapter-part1b.md §1.5',
 's17': 'chapter-part1b.md §1.5',
 's18': 'chapter-part1b.md §1.6',
 's19': 'chapter-part1b.md §1.6',
 's20': 'chapter-part1b.md §1.7',
 's21': 'chapter-part1b.md §1.7 (+ chapter.md §0.10)',
 's22': 'chapter-part1b.md § Раздел 2 (вводка), §2.1',
 's23': 'chapter-part1b.md §2.1',
 's24': 'chapter-part1b.md §2.2',
 's25': 'chapter-part1b.md §2.2, §2.3',
 's26': 'chapter-part1b.md §2.4',
 's27': 'chapter-part1b.md §2.5',
 's28': 'chapter-part1b.md §2.6',
 's29': 'chapter-part1b.md §2.6',
 's30': 'chapter-part1b.md §2.7',
 's31': 'chapter-part1b.md §2.8',
 's32': 'chapter-part1b.md §2.8',
 's33': 'chapter-part1b.md §2.9',
 's34': 'chapter-part1b.md §2.9, §2.3',
 's35': 'chapter-part2.md § Раздел 3 (вводка)',
 's36': 'chapter-part2.md §3.1',
 's37': 'chapter-part2.md §3.1',
 's38': 'chapter-part2.md §3.2 (+ chapter.md §0.4)',
 's39': 'chapter-part2.md §3.2',
 's40': 'chapter-part2.md §3.3',
 's41': 'chapter-part2.md §3.4',
 's42': 'chapter-part2.md §3.5',
 's43': 'chapter-part2.md §3.6',
 's44': 'chapter-part2.md §3.7',
 's45': 'chapter-part2b.md §3.8 (+ chapter.md §0.3)',
 's46': 'chapter-part2b.md §3.8',
 's47': 'chapter-part2b.md §3.9',
 's48': 'chapter-part2b.md §3.9',
 's49': 'chapter-part2b.md §3.10, §3.11',
 's50': 'chapter-part2b.md §3.12, §3.13',
 's51': 'chapter-part2b.md §3.14',
 's52': 'chapter-part3.md § Раздел 4 (вводка), §4.1',
 's53': 'chapter-part3.md §4.1',
 's54': 'chapter-part3.md §4.2',
 's55': 'chapter-part3.md §4.3',
 's56': 'chapter-part3.md §4.4',
 's57': 'chapter-part3.md §4.5',
 's58': 'chapter-part3.md §4.6',
 's59': 'chapter-part3.md §4.7, §4.8',
 's60': 'chapter-part3.md §4.9',
 's60a': 'chapter-part3.md §4.11 (+ §4.10)',
 's60b': 'chapter-part3b.md § Раздел 5 (вводка), §5.1',
 's61': 'chapter-part3b.md §5.3, §5.4',
 's62': 'chapter-part3b.md §5.6 (+ §5.5)',
 's63': 'chapter-part3b.md §5.7',
 's64': 'chapter-part3b.md §5.9 (+ §5.8)',
 's65': 'chapter-part3c.md § Раздел 6 (вводка), §6.1',
 's66': 'chapter-part3c.md §6.2',
 's67': 'chapter-part3c.md §6.3, §6.5 (+ §6.4)',
 's68': 'chapter-part3c.md §6.6',
 's69': 'chapter-part3c.md §6.7',
 's70': 'chapter-part3d.md §6.8',
 's71': 'chapter-part3d.md §6.9',
 's72': 'chapter-part3d.md §6.10, §6.11',
 's73': 'chapter-part3d.md §6.13 (+ §6.12)',
 's74': 'chapter-part4e.md § Раздел 9 (вводка), §9.1',
 's75': 'chapter-part4e.md §9.1',
 's76': 'chapter-part4e.md §9.1, §9.2',
 's77': 'chapter-part4e.md §9.2',
 's78': 'chapter-part4e.md §9.3',
 's79': 'chapter-part4e.md §9.7',
 's80': 'chapter-part4e.md §9.8',
 's81': 'chapter-part4e.md §9.4',
 's82': 'chapter-part4e.md §9.5',
 's83': 'chapter-part4e.md §9.4',
 's84': 'chapter-part4e.md §9.4',
 's85': 'chapter-part4e.md §9.6',
 's86': 'chapter-part4e.md §9.9',
 's87': 'chapter-part4e.md §9.12 (+ §9.10, §9.11)',
 's88': 'chapter-part5.md § Раздел 10 (вводка), §10.1',
 's89': 'chapter-part5.md §10.2 (+ §10.3)',
 's90': 'chapter-part5.md §10.4',
 's91': 'chapter-part5.md §10.5',
 's92': 'chapter-part5.md §10.6',
 's93': 'chapter-part5.md §10.8 (+ §10.7)',
 's94': 'chapter-part5.md §10.9, §10.10',
 's95': 'chapter-part5.md §10.11',
 's96': 'chapter-part5.md §10.14 (+ §10.12, §10.13)',
 's96a': 'chapter-part5b.md § Раздел 11 (вводка), §11.1',
 's97': 'chapter-part5b.md §11.1, §11.3',
 's98': 'chapter-part5b.md §11.2',
 's99': 'chapter-part5b.md §11.4',
 's100': 'chapter-part5b.md §11.5',
 's101': 'chapter-part5b.md §11.6',
 's102': 'chapter-part5b.md §11.7',
 's103': 'chapter-part5b.md §11.8',
 's103a': 'chapter-part5b.md § Раздел 12 (вводка), §12.1',
 's104': 'chapter-part5b.md §12.1',
 's105': 'chapter-part5b.md §12.2',
 's106': 'chapter-part5c.md § Вопросы и ответы для самопроверки (+ chapter-part5b.md §12.4)',
}

# номер кадра в SLIDE-PLAN.md (106 номеров); вставленные — без номера
PLAN_NO = {}
n = 0
for f in files:
    sid = fm(f)['id']
    if re.fullmatch(r's\d+', sid):
        n += 1
        PLAN_NO[sid] = n
    else:
        PLAN_NO[sid] = None

# раздел плана, которому номер принадлежит (№ → имя раздела SLIDE-PLAN.md)
PLAN_SEC = [(1,10,'Раздел 0. Вход'),(11,21,'Раздел 1. Кто попадает в поле зрения'),
            (22,34,'Раздел 2. Что про человека измерили'),(35,51,'Раздел 3. Кто это прочёл: человек и модель'),
            (52,64,'Раздел 4. Что решили и кто это заметил'),(65,73,'Раздел 7. Чем удерживают'),
            (74,87,'Раздел 6. Лекарство'),(88,96,'Раздел 5. Что стало с теми, кто решает'),
            (97,103,'Раздел 8. Сборка'),(104,106,'Раздел 9. Закрытие')]
def plan_sec(no):
    for a,b,nm in PLAN_SEC:
        if no and a <= no <= b: return nm
    return None

def q(s):
    s = str(s).replace('\\', '\\\\').replace('"', '\\"')
    return '"%s"' % s

from collections import Counter
REAL = set("""s01 s02 s04 s07 s11 s12 s13 s14 s16 s18 s19 s22 s26 s28 s29 s31 s35 s36 s40 s41 s42 s43 s44
s45 s47 s49 s52 s53 s54 s55 s57 s59 s60b s61 s63 s65 s66 s74 s75 s80 s82 s86 s88 s89 s90 s92 s105""".split())
ACQUIRED = {
 's01':'rework/deck/assets/s01-hero-chtenie-mammogrammy.jpg',
 's18':'rework/deck/assets/s18-fundus-kamera-v-kabinete.jpg',
 's22':'rework/deck/assets/s22-rentgenkabinet-pacient-u-pribora.jpg',
 's26':'rework/deck/assets/s26-tekhnik-stavit-cheloveka-k-priboru.jpg',
 's40':'rework/deck/assets/s40-dva-effekta-s-intervalami.png',
 's44':'rework/deck/assets/s44-srez-razmetka-cheloveka-i-modeli.png',
 's52':'rework/deck/assets/s52-sestrinskiy-post.jpg',
 's88':'rework/deck/assets/s88-endoskopicheskiy-kabinet.jpg'}
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
# ЧТО ЭТО. Опись 110 кадров деки со служебными полями на каждый: идентификатор, тип
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
# СОСТАВ: 110 кадров = 106 номеров `SLIDE-PLAN.md` (slides-v3) + 4 вставленных с
# буквенным суффиксом, чтобы сквозная нумерация не поехала:
#   s60a   вывод раздела «Наблюдение»          (решение П11)
#   s60b   дивайдер раздела «Ведение записи»   (решения П11/П12)
#   s96a   дивайдер раздела «Сборка»
#   s103a  дивайдер раздела «Закрытие»
#
# НУМЕРАЦИЯ РАЗДЕЛОВ РАСХОДИТСЯ ТРОЯКО, и это не ошибка выгрузки:
#   deck (файлы кадров) — порядок показа, 0…10, сквозной;
#   SLIDE-PLAN.md       — номера разделов главы при порядке показа 0→1→2→3→4→7→6→5→8→9;
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
    no = PLAN_NO.get(sid)
    W("    local_id: %-28s %s\n" % (q(d.get('local_id','')) + ',' if False else q(d.get('local_id','')),
                                    ("# № %d в SLIDE-PLAN.md" % no) if no else "# вставленный кадр, номера в плане нет"))
    W("    file: %s\n" % ('slides/' + os.path.basename(f)))
    W("    type: %s\n" % d['type'])
    W("    title: %s\n" % q(d.get('title','')))
    ps = plan_sec(no)
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
        W("    media_asset: %s   # поле media в файле кадра ещё пусто, см. deck/images.md §1\n" % q(ACQUIRED[sid]))

SPLIT = [
    ('deck.yaml',       ['0. Вход','1. Отбор — кого вообще смотреть','2. Анализ данных — и группа, на которой он посчитан']),
    ('deck-part2.yaml', ['3. Постановка диагноза — человек читает рядом с моделью','4. Наблюдение за состоянием — кто заметит ухудшение','5. Ведение записи — кто прочтёт её потом','6. Чем удерживают — подпись, процедура, норматив']),
    ('deck-part3.yaml', ['7. Разработка лекарства — удешевили начало, где узкое место','8. Что стало с теми, кто решает','9. Сборка','10. Закрытие']),
]

for i, (fn, seclist) in enumerate(SPLIT, 1):
    o = io.StringIO(); W = o.write
    W(HDR.format(fn=fn, i=i))
    if i == 1:
        W(PREAMBLE)
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
        W("  plan_slides: 106               # номеров в SLIDE-PLAN.md\n")
        W("  inserted_slides: [s60a, s60b, s96a, s103a]\n")
        W("  sum_timing_min: %.2f           # сложено по timing_min файлов кадров\n" % tot_min)
        W("  axis: \"путь одного решения о человеке: удешевили чтение данных — платят вниманием, навыком, подписью и арбитражем\"\n")
        W("  central_question: \"Модель посмотрела первой. Что теперь делает человек — и кто это измерял?\"\n")
        W("  curriculum_level: \"отраслевая лекция L7; strict-in ≥30% обязателен, waiver недоступен\"\n")
        W("  deck_parts: [deck.yaml, deck-part2.yaml, deck-part3.yaml]\n")
        W("  builder: deck/build_lec07.py   # читает slides/*.md, НЕ этот файл\n")
        W("  sources:\n")
        W("    chapter_parts: 16            # chapter.md + 15 файлов chapter-part*.md\n")
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
        W("  plan_frames_only_min: %.2f     # те же 106 кадров по файлам, без четырёх вставленных\n"
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
        W("    note: \"поле media во ВСЕХ 110 файлах кадров пока пусто — каталог slides/ держит другая сессия; пути для восьми добытых в deck/images.md §1\"\n")
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
        W("    effect: \"объявленный состав 108 кадров против 110 на диске\"\n")
        W("    fix: \"дописать два кадра в состав CUT-ORDER.md §1.1\"\n")
        W("  - id: D4\n")
        W("    what: \"у главы есть разделы 7 «Назначение и лечение» (§7.1–7.19) и 8 «Оперативная помощь» (§8.1–8.16), а в деке на них ноль кадров\"\n")
        W("    evidence: \"решение П9 называет это невыполненным обещанием кадра s07; шаг реза А1 CUT-ORDER.md §2 предъявляет их прочерком\"\n")
        W("    effect: \"chapter_ref ни одного кадра не ведёт в chapter-part4.md, -part4b, -part4c, -part4d — четыре файла главы декой не покрыты\"\n")
        W("    fix: \"известное решение, не находка: прочерк по варианту (б) REGROUP.md §4 (поправка П4)\"\n")
        W("  - id: D5\n")
        W("    what: \"одна пара кадров всё ещё несёт дословно одинаковый title (трёхсторонний дубль «Техник флюорографии и годность снимка» закрыт отдельно: issue #229 — s28/s29 переименованы в «Таиланд: …», s26 держит заземление один)\"\n")
        W("    evidence: \"s18 и s19 — оба «Глазное дно без офтальмолога»; каждая другая пара кейс+«что переехало» в деке носит разные title (s31/s32, s41/s42, s47/s48 и т.д.) — эта пара исключение\"\n")
        W("    effect: \"дивайдер раздела 1 называет разбор одним именем без номера — не противоречие само по себе, но расходится с правилом §5.16 «имена дословно совпадают с заголовками кадров», если потребуется различить половины поимённо\"\n")
        W("    fix: \"не входит в issue #229; решение владельца — развести заголовки (например «…: что переехало» по образцу s27/s29) или оставить как есть\"\n")
        W("  - id: D6\n")
        W("    what: \"у шести кадров в assertion стоит не утверждение кадра, а пометка «[шаг ② провисает: …]» или «под рез (П11)»\"\n")
        W("    evidence: \"s68, s71, s72, s81, s85 — пометка о провисании шага ②; s78 и s86 — пометка «под рез»\"\n")
        W("    effect: \"поле assertion служебное и на экран не идёт, но для критика и для речи это не утверждение кадра\"\n")
        W("    fix: \"при сборке содержания вписать утверждение, пометку перенести в отдельное поле\"\n")
    open(fn, 'w', encoding='utf-8').write(o.getvalue())
    print(fn, len(o.getvalue().splitlines()), 'строк')
