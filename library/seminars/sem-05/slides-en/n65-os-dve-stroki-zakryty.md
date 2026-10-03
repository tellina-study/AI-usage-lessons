---
id: n65
type: recap_table
duration_min: 2.25
assertion: "Two rows of the axis are closed — the hook and the skill, each with what was expected of it and what came out in practice; MCP, subagent and process stay empty until the next session"
learning_goal: "A checkpoint, not a resolution: the same five reinforcements the opening named one line each, and two of them now carry a measurement. Synthesis and takeaway theses belong to the next session's closing, not here"
visual:
  pattern: recap_table
  primary: "Light background and a box-table, not a PPTX grid. The leading line is a bridge off the last stage, in the thesis form. The table: five rows in the same order and under the same names as the five definitions of the opening; the top two filled in completely, the bottom three dashed empty slots. At the bottom, as a caption, the slide's only caption. No synthesis, no takeaway theses, no aphorism in a frame."
  backup: "СВЕДЕНО СЕССИЕЙ ОБОБЩЕНИЯ (круг 4, стык 7 сверки): из клетки скилла убран оборот «описание, а не содержимое» — он пришёл сюда из блока скиллов и в закрытии читался чужой фразой. Сказано тем же, чем это сказано на базе n46, то есть утверждением вместо сопоставления «не X, а Y», которое правило А8 запрещает прямо. rework/block-z5-os-promezhutochnaya.md §A.1/§B.2. Колонка «проверка показала» у хука приведена к числу, которое блок «Хуки» реально предъявляет и печатает сам: из ШЕСТИ форм одной команды барьер отклоняет ОДНУ и молчит на пяти (n15, assets/captures/35-selftest-branch-guard-run.txt — 9 PASS / 5 LIMIT / 0 FAIL), плюс человека с терминалом он не видит вовсе (n15). Прежняя формулировка «обходится пятью воспроизведёнными способами» называла пять без базы сравнения; база — шесть форм. КРУГ 4, ДВЕ ПРАВКИ. ПЕРВАЯ: пара колонок «Вы ожидали / На деле» переформулирована в «Что обещает устройство / Что показала проверка» (qa/zamechaniya-golosom-keysy-1-4.txt, 01:12). Новая пара снимает второе лицо. ВТОРАЯ: ведущая строка «Таблица та же, что открывала занятие пустой» снята как ставшая НЕВЕРНОЙ — таблица открытия (n03) переписана в круге 4 целиком. ТРЕТЬЯ ПРАВКА КРУГА 4 — ПЕРЕНОСИМОСТЬ: факт стоит на n03 третьей колонкой, разбор одного переноса — на n64, а здесь объяснение: ОДНА видимая строка под таблицей плюс абзац в речи. Пятой колонки здесь быть не может. Текст строки и абзаца — из research/perenosimost-stupeney.md §6, сжат под слот. Слот 2,00 → 2,25. Проверено 2026-10-01 по 17 первоисточникам. [EN-track note: provenance kept verbatim in Russian — decision D7 in EN-TRACK-BRIEF.md.]"
---

# Two rows of the axis are closed

## Assertion

Two rows of the axis are closed — the hook and the skill, each with what was expected of it and what came out in practice; MCP, subagent and process stay empty until the next session.

## Visual

> The second row is filled in. The same five reinforcements as at the start of the session — two of them now have a measurement.

| Stage | Preventing / solving | What the mechanism promises | What the check showed |
|---|---|---|---|
| Hook | Solving — the rule has already been broken | "We installed a hook, so commits to `main` are closed" | Of six forms of one command it rejects one and stays silent on five; a person with a terminal it does not see at all |
| Skill | Solving — on the signal of the instruction file overloading | "Content is what matters; the description is a detail, we will fill it in later" | Without a precise trigger `description` it will not fire at all: the choice goes by the description, and the file's body is not in the context before it fires |
| MCP | | | |
| Subagent | | | |
| Process | | | |

> **What transfers is the decision, not the way it is written down.** What counts as a violation, when to intervene, what to move into a separate file, which permissions to cut — that is yours, it does not belong to the tool. The event name, the folder, the form of the answer "no", the units of the time budget — every agent has its own. And there may be no mechanism at all: the decision then still holds, and you have to hold it at another level, often a more reliable one.

> "Two rows are filled in. Three stay for the next session."

## Speaker notes

The second row has gone into the table. The reinforcements here are the same five, in the same order as at the start of the session; back then each had one line — what it is. Now two of them carry a measurement.

The hook. We set it up when the rule has already been broken. The mechanism promises: install a hook and commits to the main branch are closed. The check showed otherwise. Of six forms of one and the same command, the barrier rejects one and stays silent on five. The base is obligatory here: five forms of silence mean nothing until you say there are six in total. And the person typing that same command in their own terminal, the barrier does not see.

The skill. We set it up on a signal — when the instruction file has outgrown itself. The mechanism promises that content is what decides and the description can be filled in later. The check showed that the choice goes by the description: without a precise trigger the file will not load even once, however good it is inside.

And the last thing, about all five at once. What transfers is the decision — what counts as a violation, when to intervene, what to move into a separate file, which permissions to cut. What does not transfer is the way it is written down: the event name, the folder, the form of the answer "no", the units of the time budget. And there may be no mechanism at all: the decision then still holds, and a more reliable level holds it.

The three bottom rows are empty not because there is nothing to say about them. We simply did not get to them — the next session will fill them in.

---

**Reference.**

*Where six forms come from.* The barrier's self-test on branch `seminar-5-hook`, commit 9803643: nine checks pass, five run into the limit, none fail. Six forms are six ways of writing the same commit command, which were taken apart at the hook stage. It is started with one command from the repository, and it prints this itself.

*If asked whether that means the hook is useless.* No. It closes the way the agent actually does write to the main branch, and it closes it reliably. The other five are a price you need to know in advance, before it shows up in your project.

*If asked about the "what the mechanism promises" column.* This is not anyone's naivety. That is how the mechanism is described in the documentation and how it looks until you measure it. The difference between that column and the next one is exactly what we spent the hour measuring for.

*If asked why there are five rows but two closed.* Five reinforcements were named at the start, and named honestly: today's session takes two. MCP, subagent and process are the next one; outbound access moved there entirely by the course owner's decision.

*If asked which stages have an agreed common way of being written down.* The skill and outbound access: the format is published, the protocol's owner is neutral, and dozens of tools read the same file. The hook and the subagent have no such agreement — everyone has the practice, and everyone writes it down their own way.

*If asked where to see the measurements.* The repository is public, the branch and the commit are on the previous slides. The self-test can be cloned and run, and the table in it matches what is in this column.

*Kept to myself.* I do not comment on the empty slots for longer than one sentence: the session ends on what has been checked, and three unclosed rows are part of that result. I am not going to apologize for them.
