---
id: n02
type: code_artifact
duration_min: 1.25
assertion: "The repository this session works with is a working prototype with a product, a configuration and a documentation layer, and it has no `.claude/` directory at all: no hook, no skill, no subagent"
learning_goal: "The state of the repository read off the screen rather than reconstructed from memory: what the project is, what it already has, and what it does not have at all. The way into the session is the last line of the listing"
visual:
  pattern: file_tree_snapshot
  primary: "A leading line about what the project is and by what criterion it counts as working. Under it, the monospace listing of the whole `signup-landing` tree, with layer markers to the right of the lines; the last line of the listing, set off by a blank one, is about the missing `.claude/` directory. At the bottom, as a full-width caption, the closing line about text."
  backup: "Дерево сверено 2026-09-27 напрямую по tellina-study/signup-landing-demo, ветка main (дуга Семинара 4 влита, коммит d41f779), через gh api …/git/trees — ARCHITECTURE.md §2. Двадцать четыре строки / 19 непустых / 4 раздела — ЦЕЛЕВОЕ состояние после наряда 7 (WORK-ORDER-demo-repo.md), одобренного владельцем в круге 4; ARCHITECTURE.md §2а. Считано по настоящим коммитам клона (git show origin/main:CLAUDE.md = 20/16/3) плюс переносимый блок наряда 7 — пустой разделитель, заголовок ## Repository etiquette и два пункта, итого четыре строки, из них три непустые. В самом репозитории наряд 7 на момент сборки ещё НЕ выполнен: до его выполнения вход остаётся 20/16/3, и этот слайд опережает репозиторий ровно на наряд 7. `.tasks/` входит в состояние на входе (коммит 14fa124), без неё дерево не совпало бы с репозиторием. Устаревшие захваты assets/captures/22-tree-stage2.txt и 24…27-tree-stageN.txt на этот слайд НЕ идут — сняты с исчезнувшей версии репозитория (ARCHITECTURE.md §2 п. 3). Имена трёх пронумерованных ADR не называются: в сверенном источнике список обрезан. Слайд намеренно не ссылается на прошлое занятие: всё, что нужно знать про проект, напечатано здесь. [EN-track note: provenance kept verbatim in Russian — decision D7 in EN-TRACK-BRIEF.md.]"
---

# Where we left off

## Assertion

The repository this session works with is a working prototype with a product, a configuration and a documentation layer, and it has no `.claude/` directory at all: no hook, no skill, no subagent.

## Visual

> **`signup-landing`** — a static landing page with a submission form for a trial lesson. Readiness is defined like this: the build finishes with code 0, the test suite passes in full, the form has been submitted by hand — both filled in and empty.

```
README.md          spec.md            DECISIONS.md       ← what we build and why
CLAUDE.md          AGENTS.md (symlink to CLAUDE.md)      ← 24 lines, 19 non-empty, 4 sections
doc/adr/           template + 3 ADRs + README.md         ← how decisions were made
.tasks/            README.md · active/ · done/README.md  ← task memory
index.html         package.json       package-lock.json
vite.config.js     playwright.config.ts
src/main.js        src/style.css      src/validate.js    ← the product
tests/form.spec.ts tests/delivery.spec.ts
tests/page-objects/form.page.ts
.gitignore

.claude/  — not there at all: no hook, no skill, no subagent, no configured server
```

Repository: `github.com/tellina-study/signup-landing-demo`, branch `main`.

> "Everything listed is text. The agent may take it into account, and may not."

## Speaker notes

`signup-landing` is a static landing page with a submission form for a trial lesson. It counts as ready when the build finishes with code 0, the test suite passes in full, and the form has been submitted by hand — both filled in and empty.

Look at what it is made of. At the top, what we build: the description, the specification, the decision log. Next to them the instruction file and a link to it under a second name: that is what configures the agent. Below, the directory of decisions and the task memory. At the bottom, the product itself and its tests.

Keep the size of the instruction file in mind: twenty-four lines, nineteen non-empty, four sections. One of the four sections we will need at the very first decision point.

Now the last line, and it matters more than all the rest. There is no `.claude/` directory in this repository: no hook, no skill, no subagent, no configured server. We set the mechanical layer up from scratch.

The address under the tree is real and the repository is public: the tree in it can be counted line by line.

Everything listed is text. The agent may take it into account. It may also not.

---

**Reference.**

*What the commands that check this tree do.* `git clone` takes the repository to your machine in full, history included. `ls -a` in the root prints the contents of the directory, including hidden names with a leading dot — without the `-a` flag you would not see a `.claude/` directory even if it were there. `wc -l CLAUDE.md` counts the lines in the instruction file; there are twenty-four. All three can be checked on your own machine in a minute.

*If asked why twenty-four lines but nineteen non-empty.* Five lines are empty separators between sections. I count both numbers, because later we will look at how much the file has grown — and it grows by content, the same five separators remaining.

*If asked about the second name of the instruction file.* It is a symlink: the same file is reachable under two names so that different tools find it. The content is one, and it is edited in one place.

*If asked what the task memory in `.tasks/` is.* A directory of task files: what is being done, what is done. It appeared in the previous session and has nothing to do with the mechanical layer — it is text, like everything else on this screen.

*If asked what an ADR in the listing is.* A record of an architectural decision: one file per decision — what was chosen, out of what, why. There are three here and a template for new ones. I do not name the three: in the source I verified against, the list is truncated, and I am not going to invent them in a session.
