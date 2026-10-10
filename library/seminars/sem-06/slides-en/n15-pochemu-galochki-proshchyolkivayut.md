---
id: n15
type: mechanics_map
duration_min: 1.5
assertion: "The service asks about permissions once — when the key is issued, and the move \"tick every box in case it turns out to be needed\" is made by almost everyone, the course's author included; a key like that lives not in the repository but in a secrets store, and its leaking is watched over by the provider — by the account of students from a previous cohort, a key exposed in a public repository is blocked within seconds"
learning_goal: "The honest continuation of the decision about the key: knowing which permissions are needed and issuing exactly those are different things, and they come apart on a single movement of the mouse. The slide names the motive for which permissions get issued broad, the place the key lives after it is issued, and the cost of a leak together with the boundary of the protection the provider gives"
visual:
  pattern: mechanics_table
  primary: "At the top — a line about the one moment when permissions are asked about. Below — a table in two substantive columns across four rows: the move almost everyone makes, and what in it comes expensive; the secrets store and the provider's watchdog stand as rows of the same table. A line in gold closes it: the watchdog covers one channel out of many, and a narrow key remains the only thing within your power."
  backup: "Source — a topic the course's author developed at length in both delivered classes of this deck and that the materials only brushed against (transcripts: `qa/rasshifrovki/gruppa-1.txt`, 16:54–17:56; `qa/rasshifrovki/gruppa-2.txt`, 18:11–22:02). Entered per section B of the delivery breakdown (`qa/RAZBOR-PROVEDENIYA.md`), item 4.

    The verbatim supports. The moment of issue: \"it asks you, now which actions will you trust to this key\" (gr. 2, 19:09). The author's admission, which the delivery breakdown calls the strongest place in both classes (§C2): \"your humble servant does the same thing: every box there is, I click straight through, but in reality that is what you should not do\" (gr. 2, 19:09); \"I usually get lazy, because I think, what if at some point later I need to do something, surely I am not going to reissue a new key for that\" (gr. 2, 19:25); the same in group 1 — \"I am guilty of just taking whatever I want so as not to think further about what it is going to do\" (16:54). The store: \"you should of course never keep them in the repository\" + the question about the notion of a secret (gr. 1, 16:54–17:04). Searching for working keys — his own experience: \"I amused myself searching GitHub, I typed in an OpenAI key and found plenty of working keys\" (gr. 1, 17:04). The blocking case — an account by students from a previous cohort: \"at the previous seminar your colleagues told me a neat thing I did not know: OpenRouter now monitors its keys on GitHub, and if you expose a key, it is blocked instantly, within literally a second\" (gr. 2, 20:25).

    The attribution in the material follows the provenance of every piece: the admission is the course author's, searching for working keys is his own experience, and blocking within seconds is an account by students, named as an account. [FACT-CHECK: whether the named provider publishes a watchdog for leaked keys as a stated property of its service and what the declared blocking time is — this was entered into the material PRECISELY as an account by students from a previous cohort, not as a verified property of the service; raising it to a verified fact would require a reference to the provider's documentation and/or to a program by which the hosting platform itself scans for leaked secrets]

    Figures the author named but which were NOT entered into the material: \"there are simply a thousand of them\" about keys found in public repositories (gr. 2, 22:02) — that is a retelling of somebody else's experience (\"some people ran an experiment\"), the count is not his and is not verified; the screen says \"found working ones\" with no figure.

    What the slide does not repeat. Crossing permissions out against the list of operations is broken down on `n13` and is not reassembled here: this screen is about why, in practice, the crossing-out that was broken down does not get done. The environment variable and its boundary (\"the diagnostic command can itself turn out to be a leak channel\") stand on `n14`; here the secrets store is added to them as the place of long-term keeping, which was not in the deck at all."
---

# Why the boxes get clicked straight through — and what comes next

## Assertion

A key's permissions are asked about once — when it is issued. The move "tick every box in case it turns out to be needed" is made by almost everyone, the course's author included.

## Visual

> A key's permissions are asked about one single time — at the moment of issue: the service lists the actions and asks which of them you trust to this key.

| The move almost everyone makes | What in it comes expensive |
|---|---|
| tick every box in a row: "what if I need it later, surely I am not going to reissue the key" | the agent's list of operations is four lines long, and the key was issued for all of them: what was crossed out in the breakdown came back in its entirety |
| put the key within reach — into a file next to the configuration | the file travels into the repository, into the commit history and into the review of edits. The key's home between runs is a secrets store: the name is visible, the value is not |
| count on nobody looking for your key | keys in public repositories do get searched for and do get found working; one of the model providers watches over its own and blocks an exposed one within seconds — by the account of students from a previous cohort |
| remember about permissions once the key has already surfaced somewhere | permissions are changed on the service's side, and after the fact they cancel nothing: whatever the key managed, it managed |

> **The provider's watchdog covers one channel out of many — a private leak, a build log and a screenshot it does not see. A narrow key that has leaked is all that remains within your power after it is issued.**

## Speaker notes

A key's permissions are asked about once — at the moment of issue. The service lists the actions and asks which of them you trust to this key. There will be no second such question, and that makes issuing a key one of those rare places where a decision is taken once and holds for a long time.

The move most often made at that moment, the course's author describes about himself outright: every box there is gets clicked straight through, one after another. The motive for the move is understandable and almost excusable — what if something is needed later, surely you are not going to issue a new key then. It is worth admitting that this is exactly what should not be done, and worth admitting at the same time that knowing it does not get in the move's way. The breakdown of the permissions in the previous conversation took several minutes and produced a list of operations four lines long; one movement of the mouse at the moment of issue brings everything that was crossed out back in its entirety.

The divergence here is worth naming precisely, because it is the content. Knowing which permissions are needed and issuing exactly those are two different pieces of work. The first is done with your head and once, the second is done with your hands and anew every time, on somebody else's screen, at the end of a long form, when what you want is to start working already.

The second move of the same kind is to put the key where it is within reach: into a file next to the connection's configuration. The file then travels into the repository, into the commit history, into the review of edits, into any export of the project. An environment variable removes the key from the file; that was the subject of the previous screen. The key's home between runs is a secrets store: a named cell whose value is handed to the process and is shown neither in the file, nor in review, nor in the build log. The notion of a "secret" in that sense is worth knowing precisely this way: it is a value that has a name, and only the name is visible.

How real a leak is can be checked more cheaply than it seems. The course's author recounts that out of curiosity he searched for model providers' keys in public repositories — and found working ones. There is no point quoting a count here: it is enough that the finds were not isolated.

The providers know about this and watch over it themselves. By the account of students from a previous cohort, one of the model providers follows public repositories and blocks an exposed key within seconds. That sounds reassuring, and the boundary of such protection is worth naming right away. It covers one channel out of many — publication in an open repository, and only at the provider that does the watching. A private leak, a build log, a screenshot, a settings file forwarded to a colleague — a watchdog like that does not see at all. And that protection belongs to the provider: it blocks the key when it sees fit, without asking you.

What of all this remains within your power after the key is issued turns out to be one line. The permissions issued to the key at the moment of creation. A narrow key that has leaked costs less than a broad one — because the cost of a leak is measured by what can be done with the leaked key. From the same thing follows a habit worth acquiring along with your first key: a separate key for each piece of work, with permissions for that piece of work, and reissuing rather than widening when the work changes.
