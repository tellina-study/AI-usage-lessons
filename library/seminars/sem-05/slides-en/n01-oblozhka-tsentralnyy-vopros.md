---
id: n01
type: hero_cover
duration_min: 0.75
assertion: "An instruction file is a request: the agent reads it and may not act on it; next to it you place a mechanism that fires on its own, and a mechanism that loads on demand"
learning_goal: "An opening built on one central question, with no run-up and no table of contents. The question stands on its own: it rests on the state of this repository, not on anyone's memory of the previous session"
visual:
  pattern: hero_cover
  figure: ramka-n01-hero.png
  primary: "Dark Ocean background. A large title, under it one leading line in the quiet speech form, then the session's central question in a gold box. The bottom third, full width, is the hero illustration figures/ramka-n01-hero.png (13.333 x 3.4 inches = 45% of the slide area): on the left a white card \"a request\" with the captions \"written down - read\" and the red line \"there is no one to carry it out\", an arrow from it to a row of five segments; the first two are filled gold, carry a lock, and are captioned \"hook - an executable barrier\" and \"skill - loads on demand\", covered by a gold bracket \"two of five today\"; the other three - \"MCP\" with the expansion \"Model Context Protocol\", \"subagent\", \"process\" - are dashed, under the bracket \"three next session\"."
  backup: "Двадцать четыре строки — tellina-study/signup-landing-demo, ветка main: ЦЕЛЕВОЕ состояние после наряда 7 (WORK-ORDER-demo-repo.md), одобренного владельцем в круге 4. Считано по настоящим коммитам клона: git show origin/main:CLAUDE.md = 20 строк / 16 непустых / 3 раздела, плюс переносимый блок наряда 7 (разделитель + заголовок + два пункта) = 24 / 19 / 4. ARCHITECTURE.md §2а. В самом репозитории наряд 7 на момент сборки ещё НЕ выполнен — до его выполнения на входе двадцать строк. Отсутствие .claude/ на входе — ARCHITECTURE.md §2 п. 2, дерево снято через gh api …/git/trees. Утверждение «правило про ветки было записано заранее и агент его нарушил» на обложку по-прежнему НЕ выносится, но основание у этого теперь другое: после наряда 7 строка репозиторного этикета на входе ЕСТЬ (её и цитирует n07), и прежнее основание «её нет вовсе» снято как ставшее неверным. Держится запрет на том, что это целевой ответ развилки 1 и обложке он не принадлежит. Иллюстрация — rendered/make_figures_ramka.py, блок «n01 · обложка»; рисуется программно (PIL, шрифты DejaVu), matplotlib в окружении нет. КРУГ 4, ПРАВИЛО А10 — ТРОНУТО ТОЛЬКО ОФОРМЛЕНИЕ. СОДЕРЖАНИЕ, ЦЕНТРАЛЬНЫЙ ВОПРОС И СОСТАВ ИЛЛЮСТРАЦИИ НЕ ТРОНУТЫ. [EN-track note: this provenance block is kept verbatim in Russian on purpose — decision D7 in EN-TRACK-BRIEF.md. It quotes the course owner's own spoken words and names Russian-language source files; translating it would misrepresent quotations. It is never drawn on a slide and never read by the builder.]"
---

# When a request is not enough: a barrier and on-demand loading

## Assertion

An instruction file is a request: the agent reads it and may not act on it. Next to it you place a mechanism that fires on its own, and a mechanism that loads on demand.

## Visual

> "The agent in this project is configured by twenty-four lines of text. It reads them. There is no mechanism in the project that would carry them out."

> "An instruction file is a request. What do you put next to it so that a rule gets enforced without depending on the agent's decision?"

## Speaker notes

Everything that configures the agent in this project is twenty-four lines of text. It reads them. There is no one to carry them out.

An instruction file is a request. The whole hour today stands on one question: what to put next to it so that a rule is enforced without the agent's good will.

Stay on the word "next to". The file stays as it is; what gets added to it is a layer that fires by itself.

There are five such layers at the bottom. Two are filled in: those are the ones we set up and check today. Three are dashed — they belong to the next session.

---

**Reference.**

*On "then just write the rule more strictly".* This thought comes first and it is a legitimate one. I say that we will test it on this repository a few slides from now and see how far it gets us. I do not refute it ahead of time: the whole first case rests on that test.

*Why the opening talk is short.* The slot is forty-five seconds, and that is the slide's entire budget. Everything that did not fit here is below and gets picked up on the spot, if the room leaves a pause.

*On the five segments at the bottom.* Each fires in its own way and breaks in its own way. The two filled ones already differ in who starts them: one fires by itself, the second the agent opens for itself. Names and definitions come two slides from now.

*On the length of this note.* The spoken part is deliberately under a hundred and twenty words: forty-five seconds does not hold more.

*Where twenty-four lines come from.* The demo repository's instruction file, branch `main`: twenty-four lines, nineteen non-empty, four sections. The repository is public, you can count it yourself. That is the size of the real file this session works with for the whole hour.

*If asked why exactly five.* Five is all the layers you can put next to an instruction file today without changing the file itself. If someone names a sixth, we take it at the break.

*If asked why two rather than all five at once.* Each of the two we also measure: we look at what it promises and what it does. There is not an hour for five such measurements. Five unmeasured mechanisms are exactly the state this session was built because of.

*If asked what the previous session has to do with it.* That is where this repository was put together, and in its last scene the agent wrote to the main branch against a written rule. That is the place we start from, but you do not need to know the previous session to take part: everything required is printed on the next screen.
