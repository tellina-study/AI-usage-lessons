---
id: n39
type: cobuilding
duration_min: 3.0
assertion: "The task arrives as one sentence due Monday; the room lays it out into pieces and answers for each one what it depends on — and it turns out that three pieces out of six are independent, one stands in a queue behind another, one reaches into somebody else's file, and one repeats every time"
learning_goal: "A practical exercise, two moves on one screen. Move 1 — the room names the pieces of the task, the lecturer records six. Move 2 — for each piece the room answers what it depends on; here too the room is asked to say out loud its guess at the number of workers, which the breakdown two screens later will test. The slot is given to the room: the spoken text is deliberately short, the rest of the time the room talks"
visual:
  pattern: cobuilding_config_reveal
  primary: "At the top — the task in one sentence, in a light remark card. Below it a table of six rows: the two moves stand as column headings, move 1 fills the left (the pieces named by the room), move 2 the right (what it depends on). At the bottom — a single plate with the count: how many pieces are independent."
  backup: "Owner's round 5 (issue 225, ZADANIE-KRUG-5.md): \"maybe better to show it as a practical exercise? and discuss with the students how to decompose and speed up tasks?\". The case's former scene (n39, \"Thursday: three checks at once, and it worked\") was removed entirely: it was a ready-made breakdown of somebody else's good luck in which the layout had already been done for the room — three independent edits were presented as a given rather than as the result of work. The form is taken from the co-building of the MCP rung (n13/n14): two moves, the screen filled in from the room's remarks. The task (a landing page with a signup form, due Monday) is taken from the seminar's own product; the composition of the pieces was checked against the live code of the demo repository — src/validate.js (validateForm, the MESSAGES map), the pattern attribute in index.html (ARCHITECTURE.md §3, FIXES-PENDING 5-2). Time figures are named in none of the pieces: no source of this rung measured how long such work takes. Slot 1.5 → 3.0: the increase was taken inside the case (n41 1.5 → 1.5 with no growth, n42 0.75 → 0.5, n46 1.25 → 0.75, n47 1.5 → 1.25, n49 1.75 → 1.25), the case total did not change — 11.75. The speech is deliberately shorter than the slot: the difference is the room's time. Revisions after the classes were held (issue 225, qa/RAZBOR-PROVEDENIYA.md §A4): the facilitator called the setup
    clumsily worded (\"look, it's sort of a bit clumsily worded\", group 2, 46:54) and
    restated it in his own words in both groups. The reason was that the screen carried
    only the client's sentence and the line \"that is the whole setup\": what the project was, where the code sits and what
    the room was supposed to do had to be added by voice. Now the setup reads off the page in full —
    the task, the deadline, the project with its two files, the absence of clarifications — and both moves with their third line
    are written out beneath it. The structure of the exercise did not change: the room lays it out itself, the table below
    stays a check. The composition of the six pieces, the dependencies and the count of independent ones are untouched.
    The build with --block n4 showed an overflow (the table at 2.11″ against a budget of 1.95″, the composition up to 7.78″ against a canvas of 7.50″) — the six cards of move 1 were taken off the screen: they repeated the left column of the table word for word, and once they were removed the screen fitted the canvas with no change to the content."
---

# The task is due Monday. Let us lay it out together

## Assertion

Six pieces inside one sentence. Three of them are independent: one waits for another, one reaches into somebody else's file, one repeats every time.

## Visual

> "The form has to be ready for the ad campaign by Monday."

Friday, evening, and that is the whole setup. The signup form on the landing page from the previous classes: the markup is `index.html`, the validation is `src/validate.js`. There is nobody to ask.

- **Move 1.** Write out what pieces this task consists of.
- **Move 2.** For each one answer: does it need another one's result, does it reach into the same file, does it repeat after all the others.
- **And in one line** — how many workers you would set up for these pieces.

| Move 1 · what sits in the task | Move 2 · what it depends on |
|---|---|
| the "phone" field and its format check | on nothing |
| the error messages — brought to one form | the same file as the field: `src/validate.js` |
| the text of the data-processing consent | on nothing |
| checking the form on a narrow screen | after the field: until the field exists there is nothing to check |
| the pre-release run: branch, tests, build | on nothing, and it repeats after every one of the others |
| the confirmation email to the applicant | on nothing, and it does not touch the code |

> **Independent pieces — three out of six.** One waits for the field. One reaches into the same file. One repeats after every one of the others.

## Speaker notes

Friday, twenty to six. One sentence appears in the chat: "The form has to be ready for the ad campaign by Monday." That is the whole setup. There will be no clarifications — the author of the sentence has left for the weekend, and until Monday morning there is nobody to ask.

The form is the signup form on the landing page from the same project as the previous two classes: the field validation lives in `src/validate.js`, the function is called `validateForm`, the markup is in `index.html`. What exactly "ready for the ad campaign" means is not stated in the setup, and that is part of the task.

Now it is worth stopping. The screen below holds the task already laid out, but the layout is the very work this case was assembled for, and reading the answer does not replace it. Take a sheet of paper or an empty file and make the two moves yourself — they pay off on the very next screen. Both moves and the third line that goes with them are written out on the screen itself: they are read and done, not paraphrased.

**Move one.** What sits in this task? Write it out in pieces — pieces you could pick up and do. Stopping at three is premature: one sentence usually yields more of them than it seems.

**Move two, and it weighs more than the first.** Against each piece answer three questions. Does it need another piece's result. Does it reach into the same file as its neighbor. Does it repeat after other pieces.

**And the third thing, in one line.** Write a number: how many workers you would set up for these pieces. The first one that suggests itself, without deliberation. That number will be needed two screens from now, and written down it holds firmer than thought: what is merely thought, everybody corrects after the fact.

Let us check against each other.

Six pieces come out. The "phone" field with its format check depends on nothing: it is a new field in the markup and a new rule in `validateForm`. The error messages that have to be brought to one form live in the `MESSAGES` map in that same `src/validate.js`. They do not require another piece's result; the file they share is the field's. The text of the data-processing consent depends on nothing and does not touch the validation code at all. Checking the form on a narrow screen comes after the field: until the field exists there is nothing to check. The pre-release run — branch, tests, build — depends on nothing and repeats after every one of the other pieces. The confirmation email to the applicant depends on nothing and does not touch the form's code.

Let us count the independent ones. Three out of six. One piece waits for the field to appear. One reaches into the same file as the field. One repeats after every one of the others — that is, it stands in the task five times over, and that distinction from its neighbors matters more than its size.

If your list came out different — that is fine and even more useful. Everyone's layout is their own; it depends on how work is customarily cut up in this project, and arguing about its composition is more useful than arguing about the number of pieces. One thing has to hold: that for every piece named, the answer to move two's question gets said. The six rows on the screen stand there as a support; there is nothing to copy off them. If you have eight pieces and the dependencies among them have been checked, the layout is done.

The pre-release run deserves a word of its own, because people often forget to count it as work. There is work in it: create the branch, run the tests, build, look at it with your own eyes. It takes time. What distinguishes it from its neighbors is repetition: the other five pieces are done once each, this one after every one of them. One of the five cards on the next screen rests on that distinction, and without it the card would look superfluous.

If the list will not come, it is worth approaching from the other end: what has to be done by Monday for the ad campaign to be able to launch. Two of the six pieces get named straight away, the rest follow them, and along the way it turns out that the campaign needs nowhere near everything on the list.

If a means got into the list instead of a piece — "I'll hand that to a subagent", "I'll start a second session" — write it down separately and go back to the move. The means is chosen on the next screen; here all that is being settled is what the task consists of. In the reverse order the means gets ahead of the layout, and it is the layout that decides it.

Time figures stand against none of the pieces, and that is deliberate: no source of this rung measured how long each of these jobs takes, and a plausible-looking estimate would substitute a feeling for the layout. The independence of the pieces does not depend on duration — it is checked by files and by results, and for choosing a means that is enough.
