---
id: n20
type: question_with_option_cards
duration_min: 1.5
assertion: "Four ways to lay out a growing knowledge base -- from 'don't think about it at all' to 'don't keep it in the prompt'"
learning_goal: "Case 2's question (renamed K2-1: 'Prompt Optimization'): bare action cards, no verdicts, no price, no solution composition (A6). Wording tightened by K2-5: every option now explicitly names its own binary choice (move it where, before or after), not a general direction with no address."
visual:
  pattern: question_with_option_cards
  primary: >
    The question in a gold frame and a row of four equal-width cards laid
    out as a spectrum: on the left, "order isn't chosen at all"; on the
    right, "the knowledge base isn't in the prompt at all". No
    explanations, no counterarguments, no markings on the cards --
    the breakdown comes on the next screen.
  backup: >
    WORDING TIGHTENED (K2-5, review 2026-10-29). The earlier edit named a
    direction with no address ("move important items to the start or the
    end" without saying this is a choice between two specific spots;
    "repeat the question around the list" without saying you can repeat it
    only before, only after, or on both sides). The new edit names a
    SPECIFIC binary choice inside each card -- closer to what gets broken
    down by the numbers on n21.

    A NAMED COLLISION, FLAGGED TO THE ORCHESTRATOR (not resolved silently).
    The owner's review names FOUR pairs of options: "base at the start /
    at the end", "append to the end / move it", "frequent items to the
    start / to the end", "repeat the question before / after the base".
    This is NOT four independent first-order cards -- "the base whole at
    the start of the prompt / the base whole at the end of the prompt"
    (right after the instruction vs. right before the client's question)
    is a separate architectural decision about where the LIST ITSELF sits,
    orthogonal to the other three, which are about the order of ITEMS
    inside the list. Two ways to read this: (a) add "base at the start/at
    the end" as a fifth card -- then the vote becomes about two different
    questions at once, and the room picks one of five without knowing it's
    picking along two axes; (b) keep four cards about the order of ITEMS
    (as now), and move the question of "where the list itself sits" into
    the solution beat (n22), where it's discussed explicitly (K2-7, K2-8).
    Option (b) was chosen: it keeps the cards as votable actions (A6) and
    doesn't spawn a fifth option that's really answering a different
    question. The decision is flagged to the orchestrator for confirmation.

    The cards follow SETKA-KEYSOV-S9.md, section "Case 2", subsection
    "Question" in substance; this edit tightened the wording, not the
    substance.

    Checked for leaks (A6), card by card: none names a verdict, none
    names a price, none lists what a built solution would contain, and
    nowhere does it say how many options are reasonable. Outside
    measurements (the middle of the list, caching) aren't on this screen
    at all -- they belong on the beats at n21, n25, and onward.

    A separate check on the fourth card: the words "next session",
    "separate store", and the name of the technique are NOT on it. Calling
    it tomorrow's topic would mark it as obviously correct and pull it off
    the vote -- the same harm as a verdict on a card, just dressed more
    politely. What it is for the arc is stated by the boundary beat (n28).

    Checked against the factual frame: every card is cast with an
    imperative verb -- "append", "move", "repeat", "look up". None of them
    turns into a claim about a property of the model ("the model reads the
    middle worse") in the process -- all four stay actions on the
    knowledge base.

    Card order is a spectrum, not scattered: the first doesn't choose an
    order at all, the second makes order a decision, the third tries to
    sidestep the order question with a repeat, the fourth removes the
    knowledge base from the prompt altogether.
---

# How to Lay Out a Growing Knowledge Base in the Prompt

## Assertion

The knowledge base is growing, and every item in it travels to the model along with the question. Who decides the order they sit in, and by what rule?

## Visual

> **How should a growing knowledge base be laid out in the prompt?**

`append every new item to the end of the current list -- don't think through the order separately` · `move frequently asked or critical items to the start of the list or to its end, by choice` · `repeat the client's question text before the knowledge-base list, after it, or on both sides, to hint at what the model should look for` · `don't keep the base whole in the prompt -- look up the needed item as a separate step on every question`

## Speaker notes

The knowledge base is growing, and all of it travels to the model whole on every request. The question is simple: in what order do its items sit, and who assigns that order. Four ways to answer it.

The first is the one Olga actually uses. A new item gets appended to the end of the current list, and nobody separately thinks about order. That's not laziness or an oversight -- that's exactly how you keep any knowledge base in a text file, and so far it's never hurt anyone.

The second is to make order a decision. Frequently asked and critical topics get moved to either the start of the list or its end -- which specific edge is also part of this decision, not automatic. Order becomes a parameter of the process just like everything else: someone chooses it, and someone revisits it.

The third is to sidestep the order question entirely, by repeating the question. The client's question can be inserted before the whole knowledge base, after it, or on both sides at once. The idea is transparent: whatever sits in the middle, the model will read exactly what it's being asked right next to that question.

The fourth is to remove the knowledge base from the call. It's stored separately, and only the needed item gets substituted into the request text for each specific question. Then the question "what order do the ten items sit in" simply stops existing, because there are no ten items in the request.

Choose with the knowledge that the knowledge base won't stay frozen at ten items. In six months there will be three times as many topics in it, the same person will be adding them in the same text field -- and the choice you make now will be working on this grown list later. And second: whichever of the four ways you pick, someone has to maintain it by hand, or set it up once. Think through who that will be and how often.

Fifteen seconds to choose, then show of hands.
