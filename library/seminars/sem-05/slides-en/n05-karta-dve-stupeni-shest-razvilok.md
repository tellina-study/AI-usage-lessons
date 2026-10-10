---
id: n05
type: lecture_map
duration_min: 2.0
assertion: "Two stages and six decision points: each one names the problem the user sees and what gets decided at it"
learning_goal: "The session map: where we are and where we are going. Each decision point is named by what the user observes and by what gets decided at it; on the way out the repository differs from the one on n02 by exactly two lines"
visual:
  pattern: lecture_map
  figure: ramka-n05-karta.png
  primary: "The figure figures/ramka-n05-karta.png full width: two stages one under the other, each with a name and three decision points in a row. Each decision point has the observed problem on top and a \"we decide\" line under it. Under them, full width, a dashed frame for the next session with three names, MCP with its expansion. No minutes, no answers, no methodological marks, no plates about the `.claude/` directory."
  backup: "Круг 4, три правки. ПЕРВАЯ: снята нижняя полоса «на входе: каталога .claude/ нет» → стрелка → «на выходе: .claude/» — «это совершенно бесполезная информация, убрать надо» (qa/zamechaniya-golosom-keysy-1-4.txt, 04:40). ВТОРАЯ: снята строка «Выбор на каждой развилке делает зал. Ответ предъявляется только после ответа зала» — правило А4, подсказок лектору на слайде быть не должно (05:13); со слайда она ушла В ЗАМЕТКИ, а не пропала. ТРЕТЬЯ: шесть развилок переименованы по А2 — от наблюдаемой пользователем проблемы, а не от решения. Два названия продиктованы владельцем дословно: кейс 1 (03:46) и кейс 3 (04:40); остальные четыре собраны по тому же образцу. ЭТИ ШЕСТЬ СВЕРЕНЫ с заголовками дивайдеров n06, n16, n25, n34, n44, n55 сессией обобщения (круг 4, стык 1 сверки): расходились пять строк из шести, правилась ЭТА схема, ни один дивайдер не тронут. Разбивка по строкам — в комментарии к блоку STEPS в rendered/make_figures_ramka.py. Артефакты ступеней — .claude/settings.json + .claude/hooks/ и .claude/skills/deploy/SKILL.md. «РОВНО НА ДВЕ СТРОКИ» ПРОВЕРЕНО ПОД НАРЯД 7 И ПЕРЕСЧЁТА НЕ ТРЕБУЕТ: две строки здесь — строки ДЕРЕВА, то есть два новых файла (файл настроек и самотест хука), а не строки CLAUDE.md. То же число в том же смысле стоит на n66 и на n68. Артефакты трёх ступеней следующего занятия здесь намеренно не называются. [EN-track note: provenance kept verbatim in Russian — decision D7 in EN-TRACK-BRIEF.md.]"
---

# Two stages, six decision points

## Assertion

Two stages and six decision points: each one names the problem the user sees and what gets decided at it.

## Visual

> By the end of the session the repository tree will differ from the one shown on the second slide by exactly two lines.

## Speaker notes

Two stages, six decision points — the whole route of the session.

The top line of each card is what the person working with the agent sees. Not the name of a mechanism and not its fix: the symptom people arrive with. The agent does not carry out a written procedure. A check was working and silently stopped. The work slowed down because of hooks. Under the symptom, the "we decide" line — what exactly gets chosen at this decision point.

There are no answers on any of the cards. At each decision point you answer first, and only then see the breakdown.

At the bottom, behind the dashed line, three stages of the next session. Names only: what they will add to the repository we do not name today.

And the last line, worth remembering. By the end of the session the repository tree will differ from the one you saw on the second slide by exactly two lines. Two — not ten and not "a directory with settings": we will be counting what actually got added.

The route of the session ends here. Next comes the first decision point, straight away.

---

**Reference.**

*Why six decision points and two stages.* A stage is a tool, a decision point is a decision made on it. The hook has three, because a hook breaks in three different ways: not installed at all, installed and silent, installed and in the way. The skill also has three: what to move out, what it will be opened by, take something ready-made or write your own.

*If asked why exactly these six.* Each one is taken from real work with the demo repository, and each has an artifact you can open. There are no invented decision points here.

*If asked about the three bottom stages.* MCP, subagent and process are the next session in full. Today all that is said about them is that they exist; outbound access moved there entirely by the course owner's decision.

*On the two lines of difference.* There are two lines, and it is a checkable number: the settings file and the hook's self-test, both confirmed by a commit. The skill's file is planned, it has no commit, and on the final slide that will be stated outright.

*If asked why six decision points for two tools.* Because a tool by itself decides nothing: what decides is the choices made on it. Six decision points are six such choices, and each is met in practice more often than the tool itself.

*Kept to myself.* The choice at each decision point is made by the room, and I show the answer only after it has been voiced. This is deliberately not on the slide: when I need the room's answer, I will ask for it.
