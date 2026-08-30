---
id: s19
type: case_study
duration_min: 1.5
assertion: "An agent at work: 200 PDFs — a sequence of steps with an explicit tool at each one"
learning_goal: "Show the agent through a worked example with an explicit tool at each step"
learning_outcomes: [LO1, LO4, LO7]
references: [yao-2022-react]
visual:
  pattern: case_with_step_sequence
  primary: "Eyebrow pill «AGENT» at the top. On the left, the «200 PDFs» case. On the right, 7 numbered steps with the tool named for each (file system / reading a PDF / text extraction (OCR / parser) / embeddings + vector DB / search + extraction via LLM / writing to a table (Sheets API / CSV) / orchestrator loop)"
---

# An agent at work: 200 PDFs — a sequence of steps

## Assertion

An agent at work: 200 PDFs — a sequence of steps with an explicit tool at each one.

## Visual

Eyebrow pill «AGENT» in the top-left corner — the same pattern as s15/s16/s17/s18/s19a. On the left, an Ocean rounded box with the case «You have 200 PDF reports. From each, extract the date, the counterparty, the amount. Assemble a summary table». An explanation of why not a model, not a chat, but precisely an agent. On the right, a large Ocean rounded box with 7 numbered steps top to bottom. Each step is an action + a teal-tinted box naming the tool (in English, with the acronyms OCR/PDF/API/CSV/LLM preserved): 1) file system, 2) reading a PDF, 3) text extraction (OCR / parser), 4) embeddings + vector DB, 5) search + extraction via LLM, 6) writing to a table (Sheets API / CSV), 7) orchestrator loop (gold highlight). At the bottom, a gold callout: «Agent = a sequence of tool calls, orchestrated by an LLM».

## Speaker notes

Here is a case where an agent naturally shows up. You have two hundred PDF reports, and from each you need to extract certain fields — the date, the counterparty, the contract amount — and then assemble a summary table. This is a multi-step task with tools: open the file, read it, extract, add to the table. It's a poor fit for a model — there is no specialized model «take two hundred arbitrary PDFs and make a table». It's a poor fit for chat — it's uncomfortable to copy two hundred files into the window. An agent is the natural choice.

Look at the right half of the slide. I've broken the agent's work into seven steps, and for each one the tool the agent uses is shown explicitly. This matters — the agent does not «think» its way through the whole path on its own; at each step it decides which tool is needed right now, which parameters to pass into it, and how to process the result.

Step one — get the list of files. Tool: file system. Step two — open the next PDF. Tool: PDF reader. Step three — extract the text. Tool: text extraction, via OCR if the PDF is scanned, or via a parser if it's structured. Step four — make a summary and put an embedding into the vector DB. Step five — find the key fields by query: «find the signing date», «find the counterparty», «find the amount». This is a combination of search and extraction via the LLM. Step six — write a row into the summary table via the Sheets API or simply into a CSV. Step seven — repeat for all two hundred files; here the orchestrator works, holding the index of the current file and the overall state.

The main point — an agent is a sequence of calls to concrete tools, orchestrated by an LLM. Not «the AI figured it out on its own», but «the AI called the right tools in the right order».
