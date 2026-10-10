---
id: n03
type: keystone_axis
duration_min: 1.75
assertion: "Five mechanisms get placed next to an instruction file, and what tells them apart is what sets each one going: the environment, the agent itself, an external system, a separate role, the way the work is ordered"
learning_goal: "The session's vocabulary: five reinforcements, one line each. The slide gives the room the words it will answer the next question with, and does not say which reinforcement is better or which of them are covered today. An untouchable slide, never cut however short the time runs"
visual:
  pattern: keystone_scope_map
  primary: "Light background and a box-table, not a PPTX grid. The leading line is about the room looking at a vocabulary rather than a recommendation. Under it a table of five rows and two columns: on the left the name of the reinforcement, on the right one line - what it is. All ten cells are filled; there are no dashed slots on the slide. There is no closing caption: the slide ends on the last row of the table."
  backup: "Круг 4, переписан целиком. Прежняя редакция — пустая таблица оси на пять строк и четыре колонки, где заполнены были только имена ступеней, а пятнадцать ячеек стояли пунктирными слотами. Владелец прочёл её вслух и назвал дословно: «нерастопная табличка с попыткой дать инструкцию… и в принципе не очень понятно, зачем это нужно, потому что что будет сегодня мы говорим через слайд, а здесь по идее должна быть подводка к следующему вопросу» (qa/zamechaniya-golosom-keysy-1-4.txt, 00:56 и 01:12). Состав новой редакции продиктован там же, 01:42. Формулировки хука и скилла взяты ДОСЛОВНО с баз механики n08 и n36 — зал не должен услышать два разных определения хука за пять минут. MCP раскрывается при первом появлении (tools/editorial/README.md §3, правило безусловное). Порядок строк совпадает с порядком карточек на n04 и n67: на этом держится возврат вопроса в закрытии. ТРЕТЬЯ КОЛОНКА, КРУГ 4: владелец — «надо проверить и явно указать в определениях — зависят ли рассматриваемые инструменты от кодинг-агента (надеюсь нет)». Пять формулировок взяты ДОСЛОВНО из research/perenosimost-stupeney.md §7. Здесь только ФАКТ, без объяснения: объяснение стоит в закрытии на n65, разбор одного переноса целиком — на n64. Слот 1,50 → 1,75. Проверено 2026-10-01 по 17 первоисточникам; ни одно утверждение не держится на вторичных обзорах. [EN-track note: provenance kept verbatim in Russian — decision D7 in EN-TRACK-BRIEF.md.]"
---

# Five reinforcements that get placed next to an instruction file

## Assertion

Five mechanisms get placed next to an instruction file, and what tells them apart is what sets each one going: the environment, the agent itself, an external system, a separate role, the way the work is ordered.

## Visual

> Five mechanisms get placed next to an instruction file. One line each — what it is, what sets it going, and whether it transfers to another tool.

| Reinforcement | What it is | Does it transfer |
|---|---|---|
| Hook | A command that **the environment runs on its own** at a set moment in the agent's work. | **The practice** — everyone has it. **The way it is written down** — everyone's is their own; some agents have no mechanism at all. |
| Skill | A procedure in **a separate file**; the agent opens it itself. | **An open format** — dozens of agents read the same file. |
| MCP | **Model Context Protocol** — a connection to an external system; through it the agent reaches data the repository does not hold. | **An open protocol** — it has a neutral owner and a shared specification. |
| Subagent | A separate role with **reduced permissions**; you start it on one task and get back only the result. | **The practice** — everyone has it. **The declaration format** — everyone's is their own. |
| Process | **The way the work is ordered, written down as files**: a plan, a record kept as you go, a check before handing over. | **Transfers in full** — these are ordinary files, no mechanism required. |

## Speaker notes

Five different mechanisms can be placed next to an instruction file. Before choosing between them, let us agree on what each one is — one line, no internals.

A hook is a command that the environment runs on its own, at a set moment in the agent's work. The agent is not asked about it.

A skill is a procedure written down as a separate file. The agent opens it itself, when it is needed.

MCP, Model Context Protocol, is a connection to an external system. Through it the agent reaches data that physically is not in the repository.

A subagent is a separate role with reduced permissions. You start it on one task and get back only the result of the work.

A process is the way the work is ordered, written down as files: a plan, a record kept as you go, a check before handing over.

The third column is whether this is tied to one tool. Today — just the fact. Three rows of five transfer: the skill and outbound access have a published format, and a process is ordinary files. For the hook and the subagent, everyone has the practice, but everyone writes it down their own way. Why the line falls there, I will say at the end.

Five rows are five different answers to one question: what sets the mechanism going. For the hook it is the environment, for the skill the agent itself, for MCP an external system, for the subagent a separate role, for the process the order you have established.

---

**Reference.**

*If asked why it is so short.* This is only the naming. We take the hook apart before the first case, the skill before the fourth, and there will be a whole slide for each. For now one line per tool is enough: later you will need all five at once.

*If asked how a hook differs from a process.* A hook fires inside a single action of the agent and gets to intervene in it. A process lives above the whole body of work and is checked by eye and by commands, after the fact. One mechanism is a moment, the other an order.

*If asked why MCP is in Latin letters.* It is the name of a protocol; there is no accepted Russian name for it. The expansion is on the slide precisely so that the letters do not stay three letters.

*If asked where the third column comes from.* A check against vendor documentation and specification texts, the first of October; seventeen primary sources, listed in the materials. A full walk-through of one transfer comes before the closing, on its own slide.

*If asked whether one can get by with a single one.* You can, and most projects live that way. The whole question is which one and on what signal — and that is the content of today's session.

*If "so which of these are we setting up" comes up.* I answer that we talk about that one slide from now, and I name nothing ahead of time: the next slide is a question, and the room gives the answer.
