---
id: s25
type: summary
section: "Section 5. Wrap-up"
duration_min: 1.5
assertion: "An LLM is not always the right tool. Decision tree: when not an LLM"
learning_goal: "Cross-cutting frame 2: ML vs LLM (extends Lec-1)"
learning_outcomes: [LO6]
chapter_ref: "§5.3 [for-slide-s25]"
visual_brief: "A decision tree with the root 'When not an LLM?' and 3 branches: (1) classification over a small set → classical ML, (2) interpretability → rules, (3) <100ms latency → a specialized small model. Otherwise → LLM."
---

# Visible content

## Title bar
"When not an LLM: an ML vs LLM decision tree"

## Body
[A decision tree, Ocean rounded boxes, vertical structure]

**Root:** When is an LLM not the right tool?

[3 branches with icons]

**Branch 1.** Classification over a small fixed set of categories (5-20 classes, labels available)?
→ Classical ML: logistic regression, **XGBoost**, LightGBM, fine-tuned BERT-base.

**Branch 2.** Interpretability needed (regulated industry — finance, medicine, insurance)?
→ Transparent methods: logistic regression with feature importances, decision trees, rules.

**Branch 3.** Response time < 100 ms critical (anti-fraud, on the user's device)?
→ A specialized small model — not an LLM call (200-500 ms).

→ **Otherwise** — an LLM fits (chat, RAG, generation, multi-step reasoning).

[Caption at the bottom]
*The top level. Deeper — Lectures 4-7 (industries).*

## Speaker notes

Let's extend the task × modality classification from Lecture 1 with one practical question: when is an LLM not the right tool. The universal use of large models is attractive, but in a significant number of scenarios it loses on efficiency to classical ML methods.

A simple decision in the form of a three-branch decision tree. **The first branch.** Is the task classification over a small fixed set of categories: 5-20 classes, thousands or tens of thousands of labeled examples? Most likely the choice is classical ML: logistic regression, gradient boosting (the popular libraries XGBoost, LightGBM, CatBoost), a small transformer classifier like BERT-base fine-tuned for the specific task. An LLM here will be more expensive and less accurate.

**The second branch.** Is interpretability or regulability needed — finance, insurance, medicine, the legal sphere, anything where you must explain to a regulator why the model made such a decision? Here the choice is classical methods with a transparent structure: logistic regression with feature importance, decision trees, rule-based systems. In terms of explaining an individual prediction, an LLM is a "black box".

**The third branch.** Is critical response time — under 100 milliseconds? Real-time feed personalization, anti-fraud on a payment gateway, edge devices? Here — a specialized small model (classical ML or a small neural network), not an LLM call with a 200-500 millisecond latency.

In all other cases an LLM is applicable, and often optimal. Especially for tasks requiring natural-language processing, a flexible request format, multi-step reasoning, or the generation of new text or code. This diagram is the top level. The real engineering choice is deeper, and we'll return to it many times in the course: Lectures 4-7 will walk through specific industries — software, finance, retail, medicine — and for each we'll discuss where an LLM is the optimum and where it is over-engineering. Here it's important to fix one thing: an LLM is not a universal hammer. Knowing the mechanics of an LLM's internals is needed, among other things, to carefully understand where it isn't needed.
