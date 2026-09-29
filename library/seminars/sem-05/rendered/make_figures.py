#!/usr/bin/env python3
"""Схемы механики — рисуются программно (PIL), а не описываются словами.

Масштаб подписей. Рендерер вставляет картинку шириной 12,2 дюйма на канву 13,333.
При ширине полотна 2400 px один пиксель схемы равен 0,366 pt на слайде, поэтому
кегль 38 px читается как 14 pt, 46 px — как 17 pt, 30 px — как 11 pt. Ниже 30 px
не опускаться: на проекторе не читается.

Раздел 1 — ступень 3 «хук», слайды s09–s21:
  khuk-scene.png      s09  сцена кейса signup-landing
  khuk-cobuild.png    s13  три решения хука и почему именно такие
  lifecycle.png       s16  где сидит PreToolUse и что он знает
  khuk-stdin.png      s17  что приходит на стандартный ввод
  contract.png        s18  чем хук отвечает: код возврата и JSON
  khuk-debug.png      s19  два разных тихих отказа и три шага проверки
  bypass.png          s20  пять форм, на которых барьер молчит
  khuk-blindspot.png  s21  агент, человек, субагент
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FM = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FMB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

DEEP = (0x21, 0x29, 0x5C); MID = (0x06, 0x5A, 0x82); LIGHT = (0x1C, 0x72, 0x93)
GOLD = (0xF0, 0xAB, 0x00); TEAL = (0x02, 0x80, 0x90); SURF = (0xF4, 0xF7, 0xFA)
INK = (0x14, 0x1B, 0x2E); MUTE = (0x5B, 0x6B, 0x7F); RED = (0xB3, 0x26, 0x1E)
W = (255, 255, 255); WARM = (0xFF, 0xF7, 0xE2); PALE = (0xE6, 0xEE, 0xF4)

CANVAS = 2400
OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)


def f(sz, b=False, m=False):
    if m:
        return ImageFont.truetype(FMB if b else FM, sz)
    return ImageFont.truetype(FB if b else F, sz)


def t(d, x, y, s, sz=38, col=INK, b=False, m=False, anchor="la"):
    d.text((x, y), s, font=f(sz, b, m), fill=col, anchor=anchor)


def tw(d, s, sz, b=False, m=False):
    return d.textlength(s, font=f(sz, b, m))


def fit(d, s, sz, maxw, b=False, m=False, floor=30):
    """Уменьшает кегль, пока строка не влезет в maxw. Ниже floor не опускается."""
    while sz > floor and tw(d, s, sz, b, m) > maxw:
        sz -= 2
    return sz


def wrap(d, s, sz, maxw, b=False, m=False):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        cand = (cur + " " + w_).strip()
        if tw(d, cand, sz, b, m) <= maxw or not cur:
            cur = cand
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines


def chip(d, x, y, w, h, s, fill, col=W, sz=38, b=True, m=False, r=12):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill)
    sz = fit(d, s, sz, w - 24, b, m)
    t(d, x + w / 2, y + h / 2, s, sz, col, b, m, anchor="mm")


def panel(d, x, y, w, h, fill=SURF, line=LIGHT, r=14, width=3):
    d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=fill, outline=line, width=width)


def arrow(d, x1, y1, x2, y2, col=MID, wd=6, head=20):
    import math
    d.line([x1, y1, x2, y2], fill=col, width=wd)
    a = math.atan2(y2 - y1, x2 - x1)
    d.polygon([(x2, y2),
               (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45)),
               (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))], fill=col)


def caption(d, y, s, sz=34, col=MUTE, b=False):
    t(d, CANVAS / 2, y, s, sz, col, b, anchor="ma")


def new(h):
    im = Image.new("RGB", (CANVAS, h), W)
    return im, ImageDraw.Draw(im)


def save(im, name):
    im.save(OUT / name)


# ────────────────────────────────────────────────────────────── s09 · сцена кейса
im, d = new(620)
t(d, 40, 30, "Один репозиторий, три кадра подряд — та же рабочая сессия", 36, MUTE)
cards = [
    (MID, "Было", ["CLAUDE.md — 20 строк", "3 раздела: проверка,", "границы, задачная память",
                   "правила про ветки нет"]),
    (TEAL, "Дописано перед показом", ["+ раздел Repository etiquette", "20 строк → 26 строк",
                                      "«Прямо в main не коммитим»", "файл загружен в сессию"]),
    (RED, "Через несколько минут", ["агент правит валидацию формы", "git commit — без ветки",
                                    "коммит лёг в main", "запрета не было"]),
]
x = 40
for col, head, lines in cards:
    panel(d, x, 100, 720, 400, fill=SURF, line=col)
    d.rounded_rectangle([x, 100, x + 720, 168], radius=14, fill=col)
    t(d, x + 360, 134, head, 36, W, True, anchor="mm")
    for i, ln in enumerate(lines):
        t(d, x + 28, 202 + i * 66, ln, fit(d, ln, 36, 664), INK)
    x += 780
for i in range(2):
    arrow(d, 40 + 720 + i * 780, 300, 40 + 780 + i * 780, 300, MUTE)
caption(d, 540, "Между вторым и третьим кадром — минуты, а не дни: файл был в контексте на момент коммита.", 34, INK)
save(im, "khuk-scene.png")


# ─────────────────────────────────────────────── s13 · три решения и почему такие
im, d = new(1020)
t(d, 40, 28, "Хук собирается решениями, а не копируется готовым блоком", 36, MUTE)
hdr = [(40, 700, "Вопрос"), (760, 680, "Что фиксируется"), (1460, 900, "Почему именно так")]
d.rounded_rectangle([40, 88, 2360, 156], radius=12, fill=DEEP)
for hx, hw, hs in hdr:
    t(d, hx + 20, 122, hs, 34, W, True, anchor="lm")
rows = [
    ("Проверять до вызова\nили после?", '"PreToolUse"',
     "После вызова барьер уже может только\nсообщить. Остановить — нет: действие\nпроизошло."),
    ("Условие на все\nинструменты или на один?", '"matcher": "Bash"',
     "Шире условие — больше ложных\nсрабатываний и дороже любая ошибка\nв самой логике проверки."),
    ("Откуда хук узнаёт,\nкакая команда пойдёт?", "jq -r '.tool_input.command'",
     "Движок сам отдаёт описание вызова\nна стандартный ввод в виде JSON.\nХук читает из него одно поле."),
]
y = 168
for q, cfg, why in rows:
    panel(d, 40, y, 2320, 250, fill=SURF, line=PALE, width=2)
    for i, ln in enumerate(q.split("\n")):
        t(d, 70, y + 56 + i * 54, ln, fit(d, ln, 38, 650), INK, True)
    chip(d, 770, y + 88, 660, 74, cfg, GOLD, DEEP, 36, True, True)
    for i, ln in enumerate(why.split("\n")):
        t(d, 1470, y + 44 + i * 56, ln, fit(d, ln, 34, 870), MID)
    y += 266
caption(d, 962, "Каждое решение сужает барьер: сначала событие, потом инструмент, потом одно поле.", 34, INK)
save(im, "khuk-cobuild.png")


# ──────────────────────────────────────── s16 · где сидит PreToolUse, что он знает
im, d = new(840)
t(d, 40, 26, "33 события жизненного цикла агента — хук занятия использует одно", 38, INK, True)
groups = [("сессия", 3), ("каждый ход", 4), ("вызовы инструментов", 6), ("команда агентов", 5),
          ("файлы и окружение", 5), ("настройки", 4), ("интерфейс и модель", 4), ("MCP", 2)]
csz, gp = 30, 12
while csz > 20:
    widths = [tw(d, f"{n} · {c}", csz) + 30 for n, c in groups]
    if sum(widths) + gp * (len(groups) - 1) <= 2320:
        break
    csz -= 1
x = (CANVAS - sum(widths) - gp * (len(groups) - 1)) / 2
for (name, n), w in zip(groups, widths):
    on = name == "вызовы инструментов"
    chip(d, x, 92, w, 56, f"{name} · {n}", GOLD if on else PALE, DEEP if on else MUTE, csz, on)
    x += w + gp
strip = [("модель уже\nсобрала аргументы", MID), ("PreToolUse", GOLD),
         ("система\nразрешений", LIGHT), ("инструмент\nисполняется", TEAL),
         ("PostToolUse", MID)]
bw, gap = 404, 56
x = (CANVAS - 5 * bw - 4 * gap) / 2
for i, (label, col) in enumerate(strip):
    lines = label.split("\n")
    d.rounded_rectangle([x, 200, x + bw, 340], radius=14, fill=col)
    for j, ln in enumerate(lines):
        sz = fit(d, ln, 40 if len(lines) == 1 else 36, bw - 30, True)
        t(d, x + bw / 2, 270 - (len(lines) - 1) * 26 + j * 52, ln, sz,
          DEEP if col == GOLD else W, True, anchor="mm")
    if i < len(strip) - 1:
        arrow(d, x + bw + 6, 270, x + bw + gap - 6, 270, MUTE)
    x += bw + gap
panel(d, 40, 420, 1140, 250, fill=WARM, line=GOLD)
t(d, 70, 444, "В этой точке хук уже знает", 34, DEEP, True)
for i, ln in enumerate(["имя инструмента и готовые аргументы",
                        "рабочую директорию и режим разрешений",
                        "идентификатор этого вызова"]):
    t(d, 70, 508 + i * 52, "· " + ln, fit(d, "· " + ln, 34, 1080), INK)
panel(d, 1220, 420, 1140, 250, fill=SURF, line=RED)
t(d, 1250, 444, "И не знает уже никогда", 34, RED, True)
for i, ln in enumerate(["чем вызов закончится и что вернёт",
                        "что агент станет делать дальше",
                        "другие вызовы той же параллельной пачки"]):
    t(d, 1250, 508 + i * 52, "· " + ln, fit(d, "· " + ln, 34, 1080), INK)
caption(d, 706, "Отсюда острая кромка составной команды: ветка читается при запуске хука — до того,", 34, INK)
caption(d, 754, "как строка git switch … && git commit … реально выполнится.", 34, INK)
save(im, "lifecycle.png")


# ──────────────────────────────────────────── s17 · что приходит на стандартный ввод
im, d = new(820)
t(d, 40, 26, "Полное описание вызова на стандартном вводе — хук берёт из него одну строку", 38, INK, True)
panel(d, 40, 92, 1240, 520, fill=(0x18, 0x20, 0x3A), line=LIGHT)
payload = [
    ('{', None), ('  "session_id": "abc123",', None), ('  "cwd": "/home/user/my-project",', None),
    ('  "permission_mode": "default",', None), ('  "hook_event_name": "PreToolUse",', None),
    ('  "tool_name": "Bash",', None), ('  "tool_input": {', None),
    ('    "command": "npm test",', "hit"), ('    "description": "Run test suite",', "trap"),
    ('    "timeout": 120000', None), ('  },', None),
    ('  "tool_use_id": "toolu_01ABC123..."', None), ('}', None),
]
for i, (line, mark) in enumerate(payload):
    yy = 108 + i * 38
    if mark == "hit":
        d.rounded_rectangle([64, yy - 5, 1256, yy + 36], radius=8, fill=(0x4A, 0x3A, 0x08))
    t(d, 80, yy, line, 28, GOLD if mark == "hit" else (RED if mark == "trap" else (0xE8, 0xEF, 0xF7)),
      mark == "hit", True)
chip(d, 40, 664, 1240, 74, "jq -r '.tool_input.command'", GOLD, DEEP, 38, True, True)
arrow(d, 660, 618, 660, 658, GOLD)
notes = [
    (GOLD, "Одно поле из всего объекта", "tool_input.command — та самая строка,\nкоторую агент собирается выполнить."),
    (RED, "Чем плох текстовый поиск", "Рядом лежит description — тоже текст\nпро ту же команду; наивный grep\nзацепит его и решит по чужой строке."),
    (MID, "И ещё одна причина", "Внутри строки JSON прячет\nэкранированные кавычки и переводы\nстрок: git commit -m \"multi\\nline\"\nразбор на sed сломает."),
]
yy = 92
for col, head, body in notes:
    lines = body.split("\n")
    h = 74 + len(lines) * 46
    panel(d, 1330, yy, 1030, h, fill=SURF, line=col, width=3)
    t(d, 1360, yy + 18, head, 34, col, True)
    for j, ln in enumerate(lines):
        t(d, 1360, yy + 72 + j * 46, ln, fit(d, ln, 32, 970), INK)
    yy += h + 16
save(im, "khuk-stdin.png")


# ───────────────────────────────────────────── s18 · чем хук отвечает: код и JSON
im, d = new(660)
t(d, 40, 26, "Два независимых способа ответить — и они спорят не в пользу интуиции", 38, INK, True)
panel(d, 40, 92, 1120, 470, fill=SURF, line=MID)
t(d, 70, 112, "Код возврата", 38, MID, True)
codes = [("0", "решения нет — вызов идёт дальше", MUTE),
         ("2", "блокирует безусловно — даже если\nэтот же хук написал в JSON allow", RED),
         ("1", "не блокирует ничего. В Unix это провал,\nздесь — «неблокирующая ошибка»", GOLD)]
yy = 176
for code, note, col in codes:
    lines = note.split("\n")
    chip(d, 70, yy, 96, 64, code, col, W if col != GOLD else DEEP, 40, True, True)
    for j, ln in enumerate(lines):
        t(d, 190, yy + (4 if len(lines) == 1 else -6) + j * 48, ln, fit(d, ln, 32, 940), INK)
    yy += 46 + len(lines) * 48
panel(d, 1200, 92, 1160, 470, fill=WARM, line=GOLD)
t(d, 1230, 112, "Объект на стандартном выводе", 38, DEEP, True)
t(d, 1230, 168, "hookSpecificOutput.permissionDecision", 32, MID, True, True)
dec = [("deny", "вызов не состоится; текст причины видит агент", RED),
       ("ask", "спросить человека — так хук отвечает вне репозитория", LIGHT),
       ("allow", "пропустить, минуя обычный запрос разрешения", TEAL),
       ("поля нет", "решения нет — это пустой вывод на фиче-ветке", MUTE)]
yy = 220
for val, note, col in dec:
    chip(d, 1230, yy, 250, 60, val, col, W, 34, True, val != "поля нет")
    t(d, 1502, yy + 30, note, fit(d, note, 32, 830), INK, anchor="lm")
    yy += 76
caption(d, 596, "Несколько хуков на одном событии: deny сильнее defer, defer сильнее ask, ask сильнее allow.", 34, INK)
save(im, "contract.png")


# ─────────────────────────────────── s19 · два разных тихих отказа и три шага
im, d = new(740)
t(d, 40, 26, "«Тихо» бывает двух разных сортов — и страшнее выглядит не тот, что опаснее", 38, INK, True)
d.rounded_rectangle([700, 92, 2360, 160], radius=12, fill=DEEP)
t(d, 1110, 126, "интерактивная сессия", 34, W, True, anchor="mm")
t(d, 1950, 126, "фоновый прогон без интерфейса", 34, W, True, anchor="mm")
cells = [
    ("Сломан весь файл настроек", "невалидный JSON; matcher\nзадан массивом вместо строки",
     ("видно сразу", GOLD, "диалог ошибки настроек\nпри старте сессии"),
     ("тихо", RED, "файл пропущен молча,\nузнать — только claude doctor")),
    ("Сломана одна запись", "опечатка в имени события,\nне тот регистр,\nнезаякоренный matcher",
     ("тихо по-настоящему", RED, "ни диалога, ни записи\nв транскрипте"),
     ("тихо", RED, "остальной файл при этом\nработает как обычно")),
]
yy = 172
for head, sub, left, right in cells:
    panel(d, 40, yy, 640, 210, fill=SURF, line=LIGHT)
    t(d, 68, yy + 22, head, fit(d, head, 36, 590), INK, True)
    for j, ln in enumerate(sub.split("\n")):
        t(d, 68, yy + 82 + j * 42, ln, fit(d, ln, 30, 590), MUTE)
    for bx, (verd, col, note) in ((700, left), (1540, right)):
        panel(d, bx, yy, 820, 210, fill=WARM if col == GOLD else SURF, line=col)
        chip(d, bx + 24, yy + 20, fit(d, verd, 34, 400) and tw(d, verd, 34, True) + 44, 56,
             verd, col, DEEP if col == GOLD else W, 34, True)
        for j, ln in enumerate(note.split("\n")):
            t(d, bx + 24, yy + 100 + j * 44, ln, fit(d, ln, 30, 770), INK)
    yy += 226
caption(d, 626, "Три шага проверки: хук виден в /hooks · заведомый нарушитель даёт реакцию, а не веру ·", 32, INK)
caption(d, 666, "негативный контроль — хук пропускает то, что должен пропускать.", 32, INK)
save(im, "khuk-debug.png")


# ────────────────────────────────────── s20 · пять форм, на которых барьер молчит
im, d = new(800)
t(d, 40, 24, "Самотест этого хука: 9 из 9 заявленных проверок сработали —", 38, INK, True)
t(d, 40, 72, "и тот же скрипт сам напечатал 5 случаев, где хук молчит", 38, RED, True)
t(d, 40, 138, "условие хука:", 32, MUTE)
t(d, 300, 138, "grep -qE '(^|[;&|]\\s*)git\\s+commit\\b'", 32, MID, True, True)
t(d, 1230, 138, "— соседние слова git и commit, только в первой строке", 32, MUTE)
rows = [
    ('git commit -m "…" на main', "эталонная форма, ровно под условие", "ОТКАЗ", GOLD),
    ("дефолтная ветка названа trunk", "сравнение жёстко на два имени: main и master", "проходит", RED),
    ('git -C <путь> commit', "между git и commit встал флаг — слова больше не соседние", "проходит", RED),
    ("/usr/bin/git commit", "абсолютный путь — это не буквальное слово git", "проходит", RED),
    ("env git commit", "любая команда-обёртка прячет коммит от условия", "проходит", RED),
    ("git commit во второй строке", "хук читает из стандартного ввода только первую строку", "проходит", RED),
]
yy = 192
for cmd, why, verd, col in rows:
    d.rounded_rectangle([40, yy, 2360, yy + 78], radius=10,
                        fill=WARM if col == GOLD else SURF, outline=col, width=3)
    t(d, 68, yy + 39, cmd, fit(d, cmd, 34, 660, True, True), INK, True, True, anchor="lm")
    t(d, 760, yy + 39, why, fit(d, why, 32, 1240), MUTE, anchor="lm")
    chip(d, 2050, yy + 12, 280, 54, verd, col, DEEP if col == GOLD else W, 32, True)
    yy += 90
caption(d, 744, "Не небрежность условия: оболочка раскрывает слова и алиасы уже после того, "
                "как хук принял решение по тексту.", 34, INK)
save(im, "bypass.png")


# ──────────────────────────────────────────── s21 · агент, человек, субагент
im, d = new(560)
t(d, 40, 26, "Кого этот хук останавливает, а кого не видит вовсе", 38, INK, True)
lanes = [
    (TEAL, "агент вызывает Bash", ["харнесс порождает PreToolUse", "хук получает команду",
                                   "возвращает deny"], "останавливает", TEAL),
    (RED, "человек в своём терминале", ["харнесс события не порождает", "хук не запускается",
                                       "команда просто выполняется"], "не видит вовсе", RED),
    (GOLD, "субагент вызывает Bash", ["хук уровня настроек срабатывает", "deny вынесен корректно",
                                      "есть случаи, где команда прошла"],
     "сработал ≠ принудил", GOLD),
]
x = 40
for col, head, steps, verd, vcol in lanes:
    panel(d, x, 92, 740, 380, fill=SURF, line=col)
    d.rounded_rectangle([x, 92, x + 740, 158], radius=14, fill=col)
    t(d, x + 370, 125, head, fit(d, head, 34, 690, True), DEEP if col == GOLD else W, True, anchor="mm")
    for i, s in enumerate(steps):
        for j, ln in enumerate(wrap(d, s, 32, 670)):
            t(d, x + 26, 186 + i * 76 + j * 40, ("· " if j == 0 else "  ") + ln, 32, INK)
    chip(d, x + 26, 400, 688, 56, verd, vcol, DEEP if vcol == GOLD else W, 34, True)
    x += 780
caption(d, 498, "«Правила в коде — законы» верно строго для агента. Для человека, действующего в обход "
                "агента, этот хук — даже не просьба.", 34, INK)
save(im, "khuk-blindspot.png")


print("схемы:", *[p.name for p in sorted(OUT.glob("*.png"))])
