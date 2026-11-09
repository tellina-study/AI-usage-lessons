---
id: n30
type: problem_scenario
duration_min: 1.5
assertion: "The answer goes out to the requester with no second read, Olga answers for it — and a month without complaints says nothing about its quality"
learning_goal: "Scene beat of Case 3: a live setup of Olga's need — who she is, what she does, how the center pays for a quiet mistake. No solution versions and no measured numbers."
visual:
  pattern: problem_scenario
  figure: k3-shema-postanovka-en.png
  primary: >
    At the top, the S1 diagram (issue #303, a real PNG): a solid line
    tracing request → classification → model writes the answer → answer
    goes out to the client (an already-existing process, unchanged).
    Separately, a dashed line — "check before sending": what this case is
    about to build, standing between the model's answer and its delivery to
    the client. Below that, a framed inset with the setting, a numbered
    timeline of a single answer from the form to delivery, a closing banner
    about cost, and Olga's own request as a quote. No measured numbers on
    this frame.
  backup: >
    SCHEMA S1 ADDED (wave 3, breakdown 2026-10-29, K3-1): the frame used to
    open straight into the framed inset with no process diagram — a
    violation of S1 (`forma-keysa-s-zamerom.md` §2), flagged in BRIEF §2a as
    violated in Case 3. BROUGHT UP TO A PNG by the designer pass (issue
    #303, "half the cases open with a description instead of a diagram"):
    `rendered/make_figures_k3.py` `postanovka()`, the same visual grammar as
    `k4-shema-postanovka.png`. The quoted blocks "Existing process (solid
    blocks)" and "What we're building (dashed)," which used to carry this in
    prose, are removed as duplicative: the same thing now reads off the
    diagram.

    The dashed block is named as the ACTION the case builds — "check before
    sending" — not as a property of the process: the five requirements for
    the text follow as plain text (not a "grey requirements block"),
    separate from the diagram — this is fix K3-1 ("the grey block is a
    sequence, not requirements; requirements are just text").

    EN figure `k3-shema-postanovka-en.png`, generated for this EN track
    (issue #172/#319) — same layout and composition as the RU
    `k3-shema-postanovka.png`, labels translated: "request," "classification,"
    "model writes the answer," "answer goes to the client" on the solid
    line; "check before sending" on the dashed one.

    The need comes from SETKA-KEYSOV-S9.md, section "Case 3," "Input form"
    and "Setup": the answer goes out right after the model has generated
    it; Olga wants a check before sending. The frame states the need, and
    the idea of self-review is named as her own proposal, same as in the
    grid.

    The character is Olga, the training center's administrator (A13). The
    workload is the same twenty requests a day as in the scene on n06, not
    a new number.

    The five answer requirements are listed per `stend/zamery-k1-k3/README.md`,
    section "Task" of Measurement 2: this is the real wording, the same one
    both in the judge model's prompt and in the checker's code. On this
    frame they stand as the center's own requirements for the text, with
    not a single word yet about who will check them or how.

    What's deliberately NOT shown: not a single run number, and no loop
    version. The scene states the problem and names the cost; the measured
    part is beats n37 and n38.

    The glitch in the answer text, in the middle of Russian words, is not
    invented for color: it was observed on this same rig, on a Case 1 run,
    and is named in ARCHITECTURE.md as a side finding carried into this case
    as is.
---

# Sending an answer with no second read

## Assertion

The requester reads the answer first, before anyone else. Olga sees it only after it's sent.

## Visual

> Twenty requests a day, and the process now closes part of them itself.

1. A short answer, with the needed detail and a pointer to where to go next if the written text isn't enough.
2. No numbers that aren't in the knowledge base, and entirely in Russian — on a past run, a fragment of Chinese characters turned up in the middle of a Russian text.

> **What it costs the training center.** A complaint only arrives for a mistake that was noticed and costly enough — a missed detail goes unnoticed, the person just leaves or asks again.

> Olga: "Let it reread itself, the way I do. It's been answering for a month, no complaints — but then, nobody's read those answers either."

## Speaker notes

Same center, same Olga, same process. Twenty requests a day, and the process now closes part of them on its own: it finds the matching knowledge-base item, writes the answer, sends it. What matters is what's missing from this chain: between "the model wrote it" and "the person read it," nobody stands.

The center does have requirements for the answer, and they're the usual ones, easy to list. Short — the answer is read on a phone. With the needed detail — if someone asked about a deadline, the answer has to give the number of days. With a pointer to where to go next if the written text isn't enough. No numbers that aren't in the knowledge base — a made-up figure sounds more convincing than the rest of the text. And entirely in Russian: on a past run of this same rig, a chunk of Chinese characters turned up in the middle of a Russian answer, and the answer itself was otherwise correct. That didn't make it fit to send.

Five requirements, each one checkable. While Olga was the one answering, she checked them herself, without consulting a list, simply because otherwise she wouldn't have sent it. Now nobody takes that step.

Now the cost, and it's a quiet one. A complaint only arrives for a mistake that was noticed and that was costly enough for the person to come back and point it out. An answer missing a needed detail will never draw a complaint: the person will ask again, or leave, or simply not show up for the retake on the right day. Olga answers for this text. She'll read it only after it's sent, if she reads it at all.

And here is her own proposal, which sounds reasonable and economical: let the model reread itself. She does exactly that by hand — writes, rereads, fixes. And right away she adds what she herself takes as an argument: it's been answering for a month, no complaints. Remember that line — it will have to be checked with a number. A month without complaints proves nothing. There's no reliability in that — only the absence of a reason to check: nobody read the answers this month, including her.
