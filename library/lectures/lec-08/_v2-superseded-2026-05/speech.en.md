---
lecture: 8
title: "Lecture 8. AI in the Creative Industries and Media"
length_min: 75
length_words: ~5500
status: draft
version: v3
slides_covered: [s01, s02, s03, s04, s05, s05a, s06, s07, s08, s09, s10, s10a, s11, s13, s14, s15, s16, s17, s19, s20, s21, s22, s23, s24, s25, s26, s27, s28, s29, s30, s31, s32, s33, s34, s35, s36, s37, s38, s39]
source: chapter v3 + deck v4 (39 слайдов)
issue: 119
audience: студенты-инженеры 3 курса МГТУ ИУ6
date: 2026-05-20
language: ru
---

# Lecturer's Speech · Lecture 8 "AI in the Creative Industries and Media"

**Duration:** 75 minutes (≈70 min of active speech + 5 min buffer for Q&A and pacing).
**Audience:** third-year engineering students (a general audience, not designers and not creatives).
**Slides:** 39 (33 content + 5 dividers + Q&A/closing).
**Pace:** target 70–75 words per minute; hard ceiling of 95 words per minute on any fragment.

---

## Preparation before the lecture (24–48 hours ahead)

- **[s01 pre-check, Suno demo]** The day before the lecture, open `https://suno.com/create` on the lecturer's laptop. Log in with the trial account, verify that clicking "Create" works and a track is generated in 30–40 seconds. If the page is unavailable or the trial is exhausted — switch to the fallback: open `https://firefly.adobe.com` and do one test image generation. If both services are unavailable — open the backup PNG `assets/backup/s01-suno-firefly-mockup.png`.
- **[s07 update]** The day before the lecture, go to `https://openai.com/index/sora-2/` and check: Sora 2 version, API price, maximum clip length. If OpenAI has announced Sora 3 or changed the limits — update the numbers verbally. In parallel, check the status of the standalone Sora consumer app — if support has indeed been discontinued in March 2026, mention this as a lesson verbally.
- **[s09 update]** Open `https://elevenlabs.io/voice-library`, play 2 voice samples. Have 2 bookmarks ready for different voices, so you can switch quickly during the lecture.
- **[s14 update]** Check the current Sora 2 API price via `https://costgoat.com/pricing/sora` and Veo 3.1 via `https://www.veo3ai.io/blog/veo-3-pricing-2026`. If prices have dropped — update the "one minute of video for $6" calculation verbally.
- **[s21 update]** On the day of the lecture, check the news on NYT v OpenAI. If the summary judgment ruling of April 2, 2026 has been issued — reword "deadline ahead" into "a ruling has already been made, and it is such-and-such". Source — `https://news.bloomberglaw.com/ip-law/` searching "NYT OpenAI".
- **[s10a update]** Open `https://www.cnews.ru/news/top/2026-03-12_v_rossii_razreshat_obuchat` and check the status of the Mintsifry bill. If a new version has been published after the public consultation — update.
- **Check the internet in the lecture hall.** If the wifi drops — open the presentation PDF in Adobe Reader, read without the live demo in s01, go straight to the backup PNG.
- Keep a clock in front of you, do not depend on the hall's clock. Print the per-slide paper checklist.

---

## Section 0. Opening — three minutes to a finished artifact (9.5 min)

### [s01 · 3 min] — Suno in 30 seconds: what you just generated

[I turn on the laptop. On the projector — a browser with `suno.com/create` open.]

"Hello. Before we say the first word about the creative industry — let's assemble one track together.

[pause 2 seconds]

I need three words from you. A topic — something concrete. A genre — pop, rock, jazz, anything. A language — Russian or English.

[I invite the audience to shout them out. I take the first three suggestions. I type the prompt, click Create.]

[pause, we wait for 30 seconds of generation]

[I play 30 seconds of the track]

Good. I'll stop it. What did we just do. We just generated a thirty-second music track together. From scratch, from a voice prompt from the hall. With vocals, with an instrumental, with lyrics, on a prompt I just heard from you.

[slowly, with emphasis]

Three years ago this same thirty-second track — that's a studio composer plus a week of work plus five hundred to two thousand dollars. Today — thirty seconds, zero musical education, zero dollars for a trial subscription.

This is not marketing. This is a basic capability that appeared over the last two years. And around it — the whole of today's lecture.

Today we will work through together what AI has done to the creative industry by the year twenty-six, what new capabilities it has added, what economics it has rewritten, what failures it has created — and where it is reasonable for an engineer to say 'AI is not needed here'."

[I close Suno. Transition to s02.]

### [s02 · 6 sec] — Cover

[On the slide — a large "08", a title.]

"Lecture eight. AI in the creative industries and media."

[pause 2 seconds; transition to s03.]

### [s03 · 2 min] — The central question

[On the slide — the question in large type, in an Ocean rounded box, the two halves visually separated.]

"The central question is on the slide. We notice: it deliberately has two halves.

The first half is diagnostic. What has AI done to the creative industry by the year twenty-six? This is a question about facts. Numbers. Cases. What appeared, what changed, what broke.

The second half is normative. Where is it reasonable for an engineer to say 'AI is not needed here'? This is a question about criteria. About the ability to refuse. About the deliberate choice of a tool.

[pause]

Notice: I am not asking 'is it good or bad that AI came into creative work'. That is an empty question — it has already come, and it will not go back. I am asking in an engineering way: where does it work, where does it not, and how do you tell before you have put half a year into a project that will then get 'soulless' in the comments.

By the end of the lecture you should have formed a checklist of five questions that you apply to any creative task with AI. And that is our useful payoff."

[Transition to s04.]

### [s04 · 1.5 min] — Map of the lecture

[On the slide — 6 cards horizontally, the current Section 0 highlighted in gold.]

"Map of the lecture. We go through six sections plus questions.

Right now we are in Section zero — the opening. Next — Section one 'ADDED': what new capabilities AI has brought. Section two 'CHANGED': how the economics and the production process have changed. Section three 'BROKE' — the main one — twenty-four minutes on failures and legal debt, twelve reference cases. Section four: where AI is not needed. Section five: the checklist.

At the end — questions.

You see how it is structured: the first two sections — what AI added and changed. The third — what it broke. The fourth and fifth — our engineering conclusions."

[Transition to s05.]

### [s05 · 1.4 min] — The keystone axis: added → changed → broke

[On the slide — a large title, three time-strips with iconography.]

"This is the keystone axis of today's lecture. We remember three words: added, changed, broke.

[pause]

These are not three parallel categories. These are three tenses of one process. Each class of creative tool — Sora for video, Suno for music, Midjourney for images — first appears as a new capability. This is the first tense — added.

Then this capability penetrates into the existing production process and changes the economics. Cost falls by a factor of a hundred, a thousand, ten thousand. New professions appear, old ones disappear. This is the second tense — changed.

And at the same time — this is important, not sequentially but in parallel — the capability creates a new class of failures. Lawsuits, deepfake fraud, negative reaction to a brand, destruction of accumulated trust. This is the third tense — broke.

[pause]

Each generation of creative tool passes through all three tenses in months, not years. And that is why looking at the year 2026 only as a parade of tools is to miss two thirds of the picture. We will look at all three tenses at once."

[Transition to s05a.]

### [s05a · 1.5 min] — Three families of generative models

[On the slide — 3 cards: diffusion, latent video transformer, neural audio synthesis.]

"One mental model before the cases. Three families, each with its own internal limits.

The first — diffusion models. Images. Stable Diffusion, Midjourney, Firefly. The principle — reversing the noise-adding process. Takeaway: the commercially safe Firefly is **not** about the architecture, but about the training corpus.

The second — latent video transformers. Sora 2, Veo, Kling. Video as tokens in a latent space. Sora's twenty-five-second limit is an internal limitation, not 'OpenAI didn't finish the job'.

The third — neural audio synthesis. Suno, ElevenLabs. Inside — autoregression plus diffusion. Voice cloning from one minute is possible because the model fine-tunes a foundation model on a sample, rather than learning from scratch. It is precisely this that made the ScarJo Sky story possible — we'll come back to it.

To these three families we will tie every case."

[Transition to s06.]

---

## Section 1. AI ADDED — new capabilities (12 min)

### [s06 · 30 sec] — Section 1, title card

[On the slide — a large "1", the title "AI ADDED".]

"Section one of five. AI added — new capabilities. Twelve minutes. Let's look at what appeared."

[Transition to s07.]

### [s07 · 2 min] — Text-to-video, the 2026 generation

[On the slide — a 3-card comparison Sora 2 / Veo 3.1 / Kling 3.0 + a frame from the release clip.]

"Text-to-video. Three flagship models.

OpenAI Sora 2 — released September twenty-six. Twenty-five seconds of clip, one thousand eighty p, synchronized audio. Ten cents per second at seven hundred twenty p.

Google Veo three point one — four, six, or eight seconds. Five cents on Lite, forty on Pro. Within the Google AI Ultra subscription.

Kuaishou Kling three point zero — fifteen seconds, **four K at sixty frames**. On the Video Arena ELO benchmark — first place. Sixty million authors.

[pause]

What 'production use' means in film. Not replacing the shoot. Augmenting pre-production and post-production. The main reference point — Lionsgate signed an AI deal with Runway in September twenty-four. The studio behind 'The Hunger Games', 'John Wick', 'Saw'. They apply it for pre-visualization, storyboards, visual effects. On the investor call they stated: they save millions of dollars on pre- and post-production. But no one said that AI replaced the shoot. Production is actors, cameras, locations.

The crack. Twenty-five seconds is not a film. When Toys R Us tried to make a sixty-six-second single Sora clip — it got a negative reaction. We'll come back to it in the third section."

[Transition to s08.]

### [s08 · 2 min] — Character preservation

[On the slide — side-by-side Sora 2 cameo + Midjourney Omni Reference grid.]

"One of the most notable capabilities of the last two years — character preservation between generations. The ability to preserve a character's face, hairstyle, clothing across many generations. Without this AI video cannot be used for a multi-scene story.

Sora 2 cameo. You register a cameo — a character with specific attributes. Then in prompts you call it up by name, and the model reproduces it in new scenes. OpenAI announced a partnership with Disney for a billion plus — Disney IP characters will be able to appear, under license, in AI-generated clips.

Midjourney Omni Reference in the seventh version. The same thing for images. One reference image — and the accuracy of character preservation grew from about sixty percent in the sixth version to eighty-five in the seventh.

Runway director mode. Full multi-scene markup: characters, locations, motion patterns as structured objects, and each scene is generated with these constants.

[pause]

Anti-hype. Character preservation works significantly better than in the year twenty-three. But a multi-scene story still drifts: after five to ten scenes small details — a tattoo, a scar, a hair shade — may change. Production use requires a **continuity supervisor**, a separate person who checks each scene and re-generates when necessary. This is a new profession — we'll come back to it in the next section."

[Transition to s09.]

### [s09 · 2 min] — Voice cloning and multilingual dubbing

[On the slide — ElevenLabs voice library screenshot + cost arrow $50–500 → less than $1.]

"ElevenLabs — the de facto standard for voice cloning and AI dubbing.

A voice clone from one minute of original audio. Thirty-two languages plus. It preserves timbre, tempo, emotional coloring.

Dubbing Studio. Twenty-nine languages. Long-form video is localized in minutes, not weeks. Before — a voice actor, a sound engineer, a post-sync editor, fifty to five hundred dollars per minute. ElevenLabs — less than a dollar.

Production use in the corporate sector. Deutsche Telekom — multilingual customer support: one CEO voice sample into thirty languages. Klarna — for autonomous customer agents.

[pause]

The failure this capability runs into. May twenty-four. OpenAI demonstrated the 'Sky' voice in ChatGPT. Strikingly similar to Scarlett Johansson's voice. Johansson had declined to voice ChatGPT — Sam Altman reached out personally. Months later OpenAI released 'Sky'.

Johansson publicly stated she was 'shocked, angered and in disbelief'. OpenAI removed the voice within a week. There was no lawsuit — but it is a de facto win for likeness rights. A technological sonic resemblance even without direct cloning is already a right-of-publicity risk.

We'll come back to this in the third section."

[Transition to s10.]

### [s10 · 1.5 min] — Genie 3 and world models

[On the slide — Genie 3 demo frame + caption "not a video generator".]

"Genie 3. Google DeepMind. Released — the twenty-ninth of January twenty-six.

From a text prompt — 'a medieval castle on a mountain, day, light wind' — the model generates a **playable 3D world**. An environment you can explore and walk through in real time, twenty-four frames per second, resolution seven hundred twenty p, consistency preserved for several minutes. This is not a sequence of predetermined frames. This is an interactive environment reacting to the user's actions.

Architecturally — a combination of latent diffusion with a world-model component that handles state transitions.

[pause]

Anti-hype. Genie 3 is **not a video generator**. It is a **simulated-environment generator**. Direct production use in the creative industries is so far only isolated cases: a couple of game studios use it for prototyping levels, a couple of film studios — for location scouting instead of real trips, the education sector — for immersive learning.

And this is an illustration of the thesis from Lecture 3: AI systems of the year twenty-six are composite architectures. Here — latent diffusion plus a state model with reinforcement learning plus a transformer for language. Not a monolithic model."

[Transition to s10a.]

### [s10a · 2 min] — The Russian context: local convenience versus the frontier

[On the slide — side-by-side Kandinsky 5.0 Video vs Kling 3.0 + 4-card landscape RU.]

"The Russian landscape. Where we are.

Images. Sber Kandinsky six point zero Image — announced the twenty-eighth of April. A mixture of experts, free access via GigaChat. Yandex Shedevrum — no VPN, free, rubles. Audience — more than five million per month.

Video. Kandinsky five point zero Video — open source under Apache. Up to ten seconds. There is no direct competitor to Sora 2, Veo 3.1, Kling 3.0 by duration and quality in Russia as of today.

Music. Sber SymFormer — entry level against Suno v5.5. There is no direct Russian competitor to Suno — Russian solutions are aggregator-proxies on top of the Western frontier with payment in rubles.

Voice. Sber SaluteSpeech — voice cloning from several hours; ElevenLabs does it from one minute. Yandex SpeechKit is functional, but its emotional expressiveness lags behind.

Legal contour. The Mintsifry bill of the eighteenth of March. The key points: a TDM exception for training, mandatory labeling of AI content, authorship with the prompt-user given a creative contribution. The plan — the first of September twenty-seven.

[pause]

Lesson. Russian GenAI is a local convenience: free, no VPN, rubles, an anticipated legal contour. But **not frontier quality** on video and music. This is not ideology. This is structure: frontier video requires tens of thousands of GPU-hours and large licensed datasets. The concentration of research and development in the USA and China — a distribution of capital costs."

[Transition to s11.]

### [s11 · 2 min] — Personalization at scale and Adobe Firefly

[On the slide — Adobe enterprise logos collage + Lionsgate quote + 3 metric chips.]

"Personalization at scale. We see — before, each client got one clip. Now — their own, adapted one.

IAB twenty-six: among ad buyers — twenty-one percent are already in production with agentic AI, twenty percent in testing, twenty-five in planning. Digital video advertising spend in the USA breaks eighty billion — for the first time more than sixty percent of all TV and video advertising spend.

Adobe Firefly. Twenty-two billion assets in two years. **Four hundred million** dollars of direct revenue. Corporate clients — Deloitte, Tapestry, Paramount+, Pepsi, dentsu. Adobe Firefly Foundry — custom models on the client's intellectual property: a marketing agency gets a guaranteed brand style and tone.

The platform layer. Firefly is not just a model, it is a platform. Twelve third-party models: Veo, Luma, Runway, Topaz. Hugging Face Spaces — another example. The architecture in detail — in Lecture 3.

[pause]

The crack. Eighty-six percent of buyers use GenAI. Forty percent of all video advertising of twenty-six is AI-generated. But Toys R Us showed — adoption does not equal success. A reference creative campaign without human leadership yields brand damage. The details — in the third section."

[Transition to s13.]

---

## Section 2. AI CHANGED — the production process and the economics (10.5 min)

### [s13 · 30 sec] — Section 2, title card

[On the slide — a large "2", the title "AI CHANGED".]

"Section two of five. AI changed — the production process, the economics, the professions. Eleven minutes. We have looked at what appeared — now we look at how the economics changed."

[Transition to s14.]

### [s14 · 3 min] — The 100×–10,000× cost collapse

[On the slide — a horizontal bar chart cost comparison + Firefly callout.]

"The main economic change — the collapse in the cost of creating a single asset. This is not 'AI is a little cheaper'. This is two to four orders of magnitude cheaper.

Let's look at the table together.

One image — an illustration, concept art. Before: fifty to two hundred dollars to a freelance designer, plus stock variants at fifty to five hundred. Now: zero or twenty-five cents through a generative service. The multiplier — two hundred to ten thousand times.

Fifty lifestyle product shots. Before: one to five thousand freelance, or five to twenty-five thousand for a full photoshoot, or fifty to five hundred for a stock set. Now: zero to a dollar and a half. More than a thousand times.

A minute of seven hundred twenty p video. Before: one to fifty thousand dollars for the shoot plus post-production. Now: about six dollars through Sora 2 in the standard tier — sixty seconds at ten cents each. A hundred fifty to eight thousand times.

A minute of dubbing per language. Before: fifty to five hundred dollars for a voice actor, a studio, synchronization. Now: less than a dollar through ElevenLabs. Fifty to five hundred times.

[pause]

What this table **does not mean**. It does not mean that the creative industry will lose a thousand × jobs. The marginal cost of generation fell by two to four orders of magnitude. But the added value from human leadership, curation, brand alignment **did not fall**. And commercially safe corporate generation still costs money: Adobe Firefly earned four hundred million of direct revenue in two years. That is a licensed corpus plus process plus integration — a full corporate SaaS stack, not 'free goods'.

What the table does mean — and here we see stratification. The bottom of the market — mass creative output, stock images, simple illustrations, generic supporting footage, simple voiceovers — this market disappears as a separately expensive category. AI does this in minutes for zero to a dollar and a half. The top of the market — reference creative leadership of a campaign, original brand campaigns, complex storytelling — remains with people. Adobe Firefly with its four hundred million is the middle segment: commercially safe, production-grade. A separate fast-growing segment."

[Transition to s15.]

### [s15 · 2.5 min] — Speed: days to seconds

[On the slide — side-by-side timer mockup: concept art, B-roll, dubbing, variants.]

"The cost collapse goes together with a speed collapse. This is the second economic factor, separate from cost.

A concept-art draft — for game development, a film, an ad. Before — days of a freelance designer or an in-house concept artist. Now — five to sixty seconds from prompt to pixel in Midjourney, Imagen, Flux.

A supporting shot — filler for a documentary or marketing video. Before — hours of shooting plus post-production, or ten to a hundred dollars per minute through stock providers. Now — five to sixty seconds through Veo or Sora 2.

Dubbing a long video into a target language. Before — weeks of studio work. Now — minutes through ElevenLabs Dubbing Studio.

Iterating through concepts — three to five variants of a main idea for a client presentation. Before — half a week of design. Now — minutes for dozens of variants.

[pause]

The engineering lesson. The speed collapse changes the work cycle at every stage of the creative process. Before, the client saw the first concept in a week — now in minutes. This is not just savings. This is a **change of the work template**. The iteration cycle becomes ten to a hundred times denser. And a new skill is required of the human in the loop — the ability to quickly formulate 'pass — fail' criteria. Because there become ten to a hundred times more variants, and slow taste becomes the bottleneck."

[Transition to s16.]

### [s16 · 2.5 min] — New professions

[On the slide — Upwork screenshot AI/ML category + 4 role-cards.]

"The collapse of cost and speed created new market roles. This is not 'AI replaced the designer'. This is a specialized class of workers between the AI tool and the final result for the client.

Prompt engineer or AI artist. A specialist who shapes prompts and post-processing to get a production-ready result out of a generative model. A separate category on Fiverr and Upwork. Starting rates — twenty-five to eighty dollars per hour.

AI director or AI music producer. Controls the model's output, brings it to production readiness through iterations, post-processing, multimodal integration. An analog of the art director, but for the AI process.

AI process specialist. An integrator of AI tools into a studio's existing production processes. For example — does the Lionsgate integration or Adobe Firefly Foundry for a marketing agency.

Continuity supervisor. The very role from the previous section — the person who checks the continuity of a character and scene across AI-generated multi-frame sequences.

[pause]

Growth metrics. Upwork — seventy percent annual growth of the AI/ML subcategory. Fifty-two percent of the gross services volume growth — AI-related work. According to Upwork and MBO Partners reports — self-employed workers with AI/ML skills earn premium rates relative to the overall freelance market.

The important point. This is **not a million new designers**. This is a specialized class between the tool and the result for the client. It is necessary because raw AI output does not equal a production-ready result — you need curation, post-processing, brand alignment, legal review. This class is growing fast. But it is smaller than the class being displaced."

[Transition to s17.]

### [s17 · 2 min] — Displacement: graphic designers, stock photography, voice actors

[On the slide — bar chart Upwork displacement + Shutterstock pivot.]

"In parallel with the new professions — the displacement of the old ones.

Graphic designers. Minus seventeen percent of jobs on Upwork after the release of generative tools for images. Wage compression: AI is detected in forty percent of jobs at ten to nineteen dollars per hour. And **less than ten percent** in jobs at sixty plus. AI washes out the bottom segment.

Stock photographers. Shutterstock authors — from hundreds of uploads a month to **single digits**. Getty Creative revenues minus five percent in twenty-four.

Voice actors. The SAG-AFTRA strike of twenty-three was motivated by AI risks. They demanded contractual protection.

Defensive consolidation. The merger of Getty and Shutterstock — January twenty-five, three point seven billion dollars. The two largest providers combined.

[pause]

And Shutterstock's second pivot. Licensing to AI companies — one hundred four million in twenty-three, one hundred thirty-eight in twenty-four, a forecast of two hundred fifty by twenty-seven. Shutterstock stops selling photos to photographers. It starts selling corpora of photos to AI companies as training data. Photographers become a data source, not clients.

Hollywood responded collectively. SAG-AFTRA and the WGA won AI terms — digital replicas, synthetic performers, AI disclosure in training. Extension to twenty-eight. But these terms cover union members in Hollywood. The bottom freelance segment, Korean voice actors — outside the jurisdiction. Wage compression from below — a structural shock."

[Transition to s19.]

---

## Section 3. AI BROKE — failures and legal debt (23.5 min)

### [s19 · 30 sec] — Section 3, title card

[On the slide — a large "3", the title "AI BROKE". The main section.]

"Section three of five. AI broke — failures and legal debt. Twenty-four minutes, twelve cases. This is the main section, and we will work through each case together — what happened, what the mechanism is, what the lesson for the engineer is."

[Transition to s20.]

### [s20 · 1.5 min] — Copyright: 4 categories of lawsuits

[On the slide — 2×2 matrix categories + Lesson for the engineer.]

"Before diving into the cases — a classification. We fix: 'AI versus copyright' is **not one question**, but four different categories.

Category one. Collection of training data without a license. The very fact of including a protected work in a dataset is an infringement.

Category two. Output similarity, or memorization. The model reproduces copyright-protected material verbatim.

Category three. Style mimicry. Generation in the style of a named artist. Style in itself is not protected, but class-action lawsuits expand protection through the DMCA.

Category four. Voice and likeness. The right to control the commercial use of a voice or a likeness. Even a sonic resemblance without direct cloning is already a risk.

[pause]

**Lesson for the engineer.** Before choosing an AI tool, determine which of the four categories apply. The risk-reduction approaches for each are different: license verification, output-similarity audit, style restrictions, consent management — this is not one and the same checklist. If the risk in a process falls into several categories — sum them up."

[Transition to s21.]

### [s21 · 2 min] — NYT versus OpenAI: training plus output

[On the slide — Bloomberg Law headline screenshot + timeline.]

"Case one. We begin with NYT versus OpenAI — the most significant case for the future of GenAI.

Filed the twenty-seventh of December twenty-three in the Southern District of New York. Against OpenAI and Microsoft.

The theory of harm — the theory of verbatim reproduction. NYT claims: ChatGPT stores protected content in its weights and reproduces it verbatim. In the complaint — specific fragments reproduced with more than ninety percent match on specific prompts.

Discovery. Bloomberg Law — OpenAI is required to hand over **twenty million** ChatGPT logs. The summary judgment deadline — **the second of April twenty-six**. At the time of the lecture — an update verbally.

[pause]

What is at stake. If NYT wins — 'fair use' (the U.S. doctrine) is rejected as the default answer. OpenAI and its peers are required to license the corpus. License payments potentially in the billions of dollars. If OpenAI wins — 'fair use' is established for AI training.

**Lesson for the engineer.** If the model quotes the training corpus verbatim — this is not fair use, this is evidence of infringement. An output-similarity check is mandatory. At minimum — a Bloom filter on known protected material or embedding proximity to training fragments."

[Transition to s22.]

### [s22 · 2 min] — Getty versus Stability AI: the UK won, the US in process

[On the slide — Bird & Bird ruling screenshot + UK vs US split.]

"Case two. Getty Images versus Stability AI. One set of facts in the UK and the US yields **opposite** results.

The UK case. High Court — a ruling of the fourth of November twenty-five. Stability **won** the main copyright claims. The court ruled: the weights of an AI model are not a 'copy' of the training images under UK CDPA. The trademark infringement was found 'extremely limited' — only on early versions with Getty watermarks in the output. A knockout win for Stability in the UK.

The US case — separate. Northern District of California. The hearing on the motion to dismiss — the tenth of February twenty-six. The US litigation uses a 'fair use' defense through the four-factor test, expanded by the Andy Warhol Foundation versus Goldsmith case.

[pause]

What is at stake. If the US ruling is also in Stability's favor — this is 'AI training as fair use' across the Atlantic. If against — a jurisdictional split. Legal in the UK does not equal legal in the US. Companies deploying AI globally are obliged to different compliance.

**Lesson for the engineer.** Jurisdictions diverge. This is an empirical fact of twenty-five to twenty-six. For global deployment, check both."

[Transition to s23.]

### [s23 · 2 min] — Andersen versus Stability: style mimicry, class action

[On the slide — Court docket screenshot + timeline.]

"Case three. Sarah Andersen, Kelly McKernan, Karla Ortiz and others versus Stability, Midjourney, DeviantArt. A class action of artists in the Northern District of California. The visual analog of NYT.

The theory of harm. The models were trained on the works of tens of thousands of artists without consent, license or compensation. Users generate works 'in the style of a named artist' — this creates market substitution for the original artists. DMCA violations — removal of copyright management information from the training data.

Procedural history. The initial filing — January twenty-three. The motion to dismiss was **denied** on the twelfth of August by Judge Orrick. This is a key point of the moment: it means the class action survives to the discovery stage. The third amended complaint — the twenty-seventh of February twenty-six. Responses — the thirteenth of March. **A hearing is scheduled for the eighth of September twenty-six**.

[pause]

What is at stake. If the plaintiffs win — 'style mimicry' gains legal legitimation. Even if style is formally not protected by copyright, a class action based on the DMCA plus rights of publicity plus market substitution creates a precedent: 'in the style of a named artist' is an infringement.

**Lesson for the engineer.** Style mimicry 'in the style of such-and-such artist' is **not safe** simply because style itself is not protected by copyright. Class actions survive the motion-to-dismiss hearing on the basis of the DMCA. If your AI tool allows prompts like 'in the style of an edge' — you have inadvertently created a legal risk."

[Transition to s24.]

### [s24 · 2 min] — RIAA versus Suno/Udio: licensing under litigation pressure

[On the slide — RIAA press release + settlement timeline.]

"Case four. Here we see how the industry reacts not with a ban but with licensing. The RIAA on behalf of the Big Three labels (Universal, Sony, Warner). Two parallel lawsuits on the twenty-fourth of June twenty-four. Against Suno in Massachusetts, against Udio in New York.

The theory of harm. Suno and Udio were trained on copyright-protected music without a license. They produce outputs substantially similar to specific recordings, including recognizable vocal styles.

Procedurally. Universal and Udio — settled on the twenty-ninth of October twenty-five, a joint AI-music platform in twenty-six. Udio went from a target of a lawsuit to a licensed partner. Warner and Suno — a license deal in September twenty-five, royalties plus an equity share. Warner and Udio — the litigation continues. Sony is actively litigating with both, moving toward summary judgment. The summary judgment hearing on Suno — July twenty-six.

[pause]

What this means. The outcome is **not 'AI music banned'**, but 'AI music partly licensed'. The matrix of three major labels against two defendants breaks down unevenly. This is a **new business-model layer** — selective licensing.

**Lesson for the engineer.** Licensing under litigation pressure is the de facto outcome. Two of the three major labels have settled. If you are developing AI for music — build license payments into the roadmap. If you are deploying into a product — choose providers with a licensed corpus."

[Transition to s25.]

### [s25 · 2 min] — Thomson Reuters versus Ross: the first American rejection of the 'fair use' defense

[On the slide — Reed Smith analysis screenshot + Warhol v Goldsmith chip.]

"Case five. Thomson Reuters versus Ross Intelligence. District of Delaware, February twenty-five. Judge Stephanos Bibas.

This is the **first American ruling** to reject the 'fair use' defense in AI training.

The theory of harm. Ross — a legal-search AI startup, a competitor of Westlaw — used Westlaw headnotes for training. Headnotes are brief summaries of court cases.

The ruling. **Partial summary judgment in favor of Thomson Reuters.** Not fair use. Two thousand two hundred of three thousand headnotes — infringed. The factors from the Andy Warhol Foundation versus Goldsmith case were applied. Commercial use plus direct market substitution with Westlaw. 'Fair use' rejected.

[pause]

An important caveat. Ross is **not generative AI**. It is search and retrieval, not an LLM and not diffusion. Applicability to generative AI will be tested in NYT, Andersen, Getty US.

But Thomson Reuters versus Ross Intelligence breaks the template 'AI training is automatically fair use'.

**Lesson for the engineer.** 'Fair use' is **not the default option**. Do not build a product roadmap on the assumption 'fair use will save us'. If your product uses AI on a large web corpus — the legal risk is tens of millions of dollars of expected liability under an unfavorable ruling."

[pause before the deepfake block]

"An interlude. We have gone through five copyright cases — the first three categories of our classification. Next — the fourth category. Voice and likeness through deepfakes."

[Transition to s26.]

### [s26 · 2.5 min] — Arup, a CFO deepfake: $25.6 million on a single call

[On the slide — CNN article screenshot + attack diagram.]

"Case six. Notice — we are moving to the fourth category, voice and likeness. January of the year twenty-four. Arup — a British engineering firm, known as the designer of the Sydney Opera House. A finance employee in the Hong Kong office received an invitation to a video call from what looked like the company's CFO plus several colleagues.

During the video call the finance employee approved and carried out **fifteen transactions** totaling **twenty-five point six million dollars**.

[pause]

What happened. The email and the video call were social engineering. The CFO and the colleagues on the call were a deepfake. An AI-generated face plus voice cloning plus real-time lip synchronization. The finance employee had no grounds to doubt: visually — recognizable colleagues, the voice — recognizable, the tone — natural, the corporate context — plausible.

[pause]

The engineering mechanism. This is the commoditization of deepfake technology. A real-time deepfake in a multi-participant video call — several deepfake faces at once — has stopped being a laboratory experiment. It became accessible to criminals. Technologically you need: source video footage of each participant — available from LinkedIn, corporate sites; voice samples — from publicly available conferences, podcasts; hardware for real-time inference — a GPU rig for a thousand to five thousand dollars; face-swap and lip-sync software — open source.

The outcome. Arup publicly confirmed the incident. Most of the funds were not recovered. The Hong Kong police investigated, no one was arrested. This is the first widely known multi-participant real-time deepfake video fraud with corporate financial damage.

**Lesson for the engineer.** A video call does not equal identity verification in twenty-four and beyond. Financial transactions above a certain threshold require verification through an independent channel. A call-back on a known phone number. Multi-factor authentication. A physical signature. This is not 'paranoid security'. This is a new baseline practice for financial control in the AI era."

[Transition to s27.]

### [s27 · 2 min] — Korea: a deepfake crisis with schoolgirls, mass harm to a class

[On the slide — NPR headline screenshot, TEXT ONLY, no deepfake visuals + numbers card.]

"Case seven. August twenty-four. South Korea.

Journalists discovered more than two hundred Telegram chats with deepfake pornography. Generated from selfies of classmates and teachers.

The scale. Six thousand five hundred takedown requests from January to July twenty-four — four times more than in all of twenty-three. Seventy-four percent of suspects — aged ten to nineteen. Teenagers. Between twenty-one and July twenty-four — seven hundred ninety-three complaints, only sixteen prosecuted. An enforcement rate of about two percent.

[pause]

The engineering mechanism. The technological barrier — practically zero. AI face-swap apps are legally available in Google Play and the App Store. They take a source photo from Instagram and swap the face onto pre-uploaded explicit material. Generation — seconds. Distribution — Telegram channels, hosting outside Korea.

An accessible capability plus weak enforcement equals **mass harm to a whole class of a vulnerable population**.

The outcome. An emergency task force. Apps shut down. Penalties strengthened. But no structural way out was found.

**Lesson for the engineer.** An accessible capability plus weak enforcement — mass harm to a whole class. For consumer AI tools a **safety layer is mandatory before launch**: explicit-material detection, age verification, a reporting pipeline. This is not a 'patch after launch'. This is a requirement from day one."

[Transition to s28.]

### [s28 · 2 min] — Slop and model collapse

[On the slide — Google AI Overview "glue on pizza" screenshot + Nature paper header.]

"Case eight. Slop. Low-quality AI-generated material flooding platforms. And model collapse as the structural explanation.

Shumailov and the team in Nature, the year twenty-four. The article 'AI models collapse when trained on recursively generated data'. It formalizes model collapse: recursive training on synthetic outputs leads to progressive degradation and a narrowing of diversity. The model forgets the tails of the distribution. This is also called MAD — model autophagy disorder.

The context. By the year twenty-six the supply of human-created training data is running out. The next models are forced to fall back on the synthetic outputs of the previous ones. A systemic risk.

[pause]

Concrete slop. Google AI Overviews, May twenty-four. Recommendations: '**put glue on the pizza** — one eighth of a cup of non-toxic glue'. The source — a joke on Reddit. '**Eat at least one rock a day**' — the source The Onion, satire. 'Obama is a Muslim president' — a falsehood.

The training-data source is to blame. The model was trained on Reddit and The Onion without the context of attribution. Satire turned into answers.

**Lesson for the engineer.** Source quality matters more than volume. A model on Reddit jokes without a filter loses to a model on a curated dataset — **even if it is ten times smaller**. Adobe Firefly 'commercially safe' is a manifestation of this principle. Curation matters more than volume — a core decision at the architecture stage, not a patch after the reaction."

[Transition to s29.]

### [s29 · 2 min] — Sports Illustrated plus Amazon: destruction of accumulated trust

[On the slide — Futurism article + Authors Guild data.]

"Case nine. Structural destruction of accumulated trust through AI pseudonyms.

Sports Illustrated. November twenty-three. The outlet Futurism published an investigation: Sports Illustrated published articles under **fake author names** with AI-generated profile photos. The photos were bought on digital marketplaces for a few dollars. Arena Group, the parent company of Sports Illustrated, shifted responsibility to the contractor AdVon Commerce. The affected articles were removed.

What happened. The destruction of accumulated trust in its pure form. Sports Illustrated — a seventy-year history, a brand equity of about a billion dollars. The AI pseudonyms destroyed it **instantly**. A news cycle in which the brand is accused of deceiving readers discredited the value. Recovery is impossible — the magazine exists, but the trust premium is reduced.

Amazon Kindle fake books. Twenty-three to twenty-four. Authors Guild — a surge of AI-generated fake books. Exploitation of the names of real jazz figures: Frank Gioia, Ted Alkyer. AI fakes under the names of real authors.

Amazon limited KDP to three books per day and required AI disclosure. But the disclosure is **not shown to the consumer** on the book's page.

[pause]

**Lesson for the engineer.** Accumulated trust is a key brand asset. AI pseudonyms destroy it instantly. If you publish under a name — the name of a real person or with explicit disclosure of AI authorship. Half-measures are direct brand damage as liability. Sports Illustrated ran this experiment on everyone's behalf."

[Transition to s30.]

### [s30 · 1.5 min] — Coca-Cola and Toys R Us: marketing backlash

[On the slide — 2 sentiment bar charts side-by-side.]

"Case ten. Two reference cases. AI is incompatible with a reference creative campaign, even when the technical quality is acceptable.

Coca-Cola 'Holidays Are Coming'. December twenty-four. The iconic Christmas campaign since nineteen ninety-five. Coca-Cola released an AI version through three studios and four models. The reaction — a sustained negative reaction to the 'soulless' clip. And it **repeated** the AI ad in twenty-five.

The Toys R Us ad via Sora. Cannes Lions June twenty-four. The first sixty-six-second single AI ad.

The reaction. Positive sentiment fell from **plus twelve point two to plus three point four percent**. Negative jumped from thirteen point five to **fifty-three point four percent**. Joe Russo — the director of Marvel Endgame — publicly: 'disgusting'. Toys R Us officially: 'a successful test'.

[pause]

**Lesson for the engineer.** An AI ad is possible. But a reference seasonal or reference brand campaign **without human leadership** equals brand damage. Brand trust risk is measured by a **sentiment reversal**, not by a click-through rate. For a commercial creative task above the brand-equity threshold, human leadership is mandatory. For a mass creative task — AI works."

[Transition to s31.]

### [s31 · 1.5 min] — Displacement, summary

[On the slide — 3-stat block: −17% Upwork / 40% jobs AI-detected / 4-year extension.]

"Case eleven. Displacement is **not a temporary shock**, but a structural transformation of the labor market.

Contractual terms help, but do not cover the bottom. The AI terms of SAG-AFTRA plus the WGA — digital replicas, synthetic performers, AI disclosure in training. Extension to twenty-eight. But they **cover only union members and only Hollywood**. The bottom freelance segment, Korean voice actors — outside the jurisdiction.

Wage compression from below. Forty percent of jobs at ten to nineteen dollars per hour — AI detected. Less than ten percent in jobs at sixty plus. The bottom tier is done by AI. The top tier remains with humans. The middle tier is compressed.

The stock industry — a pivot, not stability. Photographers become a data source, not clients.

[pause]

**Lesson for the engineer.** Displacement is a structural shock. The top tier is protected by union terms, displacement is minimal. The bottom tier — displacement is under way. The middle tier — a pressure zone. Understanding which class of labor your tool displaces is a mandatory design requirement before launch."

[Transition to s32.]

---

## Section 4. AI is not needed here — criteria for a negative choice (7.5 min)

### [s32 · 18 sec] — Section 4, title card

[On the slide — a large "4", the title "AI is not needed here".]

"Section four of five. AI is not needed here — criteria for a negative choice. Eight minutes. We have seen twelve failures — now we derive from them a checklist for refusal."

[Transition to s33.]

### [s33 · 2.5 min] — Four criteria for refusal

[On the slide — a 4-card decision matrix + a link to the cases.]

"This is the **useful payoff** of the lecture. The lessons from twelve cases are not scattered curiosities. We see twelve manifestations of **four fundamental criteria** by which an engineer checks any AI tool before deploying it into a creative project.

Criterion one. Training-data license. The question: is the training corpus of the AI tool you are using licensed? Adobe Firefly — yes, trained on Adobe Stock plus licensed data. Stable Diffusion — no, trained on a web scrape without consent. Midjourney — unclear, the training corpus is not disclosed. If the answer is 'no' — there is legal debt, the precedents of Andersen, RIAA.

Criterion two. Output-similarity check. The question: can the model reproduce protected material verbatim? NYT versus OpenAI — the theory of verbatim reproduction. An output-similarity check is an engineering task, implemented through embedding proximity to known protected material, through a Bloom filter, through probabilistic verification. If you deploy AI and **do not check output similarity** — you inadvertently accept liability.

Criterion three. Voice and likeness consent. If AI generates the voice, image or likeness of an identifiable person — is there explicit consent? The ScarJo versus OpenAI Sky case showed: **even a sonic resemblance** creates a right-of-publicity risk, not only direct cloning. If the answer is 'no consent' — this is a hard stop.

Criterion four. Brand trust risk. Is the creative task iconic, a legacy, a high-brand-equity zone? Coca-Cola 'Holidays Are Coming', Sports Illustrated, the Toys R Us holiday campaign — all three ran into a negative reaction. Brand trust risk is measurable through a sentiment reversal. If the answer is 'yes, iconic' — human leadership is mandatory.

[pause]

These four criteria are not exhaustive. But they cover the overwhelming majority of the reference failures from the third section. Applying the four criteria is not a moral question. It is a concrete risk-reduction practice."

[Transition to s34.]

### [s34 · 2 min] — Where only a human

[On the slide — 3-column comparison.]

"A positive formulation. We will designate three zones where 'only a human' remains mandatory as a functional requirement, and not as nostalgia.

First. Investigative journalism and original reporting. NYT, Washington Post, Reuters have explicit rules forbidding the use of AI for original reporting. Not for proofreading. Not for summarizing. Precisely for original reporting. The reason — Sports Illustrated and epistemic responsibility. When a journalist publishes primary-source material, the brand of reliability is a key asset, instantly destroyed by AI substitution. Substitution — a loss of epistemic status.

Second. Original creative leadership. Coca-Cola Christmas, Toys R Us, any reference seasonal campaign of high brand equity requires human creative leadership. AI as an execution tool under leadership — permissible. AI as the primary creator — a brand-damage risk, measurable through a sentiment reversal. Here 'only a human' is a strategic requirement, not a tactical one.

Third. Long coherent narrative. Suno and Udio by the year twenty-six generate three-to-four-minute tracks, **not a coherent fifty-minute album** with motif development. Sora 2 and Veo 3.1 — clips up to twenty-five seconds, **not a coherent feature-length film**. Long narrative composition requires architectural coherence that current architectures do not cover. A limitation of the neural-audio-synthesis and latent-video-transformer families — we talked about it in Section zero.

The important point. This is **not a temporary limitation** that will 'disappear in the next version'. This is an intrinsic property of current architectures."

[Transition to s35.]

### [s35 · 2.7 min] — AI thumbnails on YouTube: empirical rejection by the end user

[On the slide — 3-stat block + bar chart drop reasons.]

"One of the most vivid pieces of empirical evidence about the boundaries of AI in creative work — AI thumbnails on YouTube. By December twenty-five large YouTube creators began to **massively abandon** AI-generated thumbnails.

**Forty-seven point three percent of creators** in a Social Blade survey stopped using AI thumbnails in December twenty-five. This is not a 'survey platitude'. This is an observed behavior pattern. Notice the number — almost half of top-tier creators refused in a single year.

The reasons — measured.

First. 'Uncanny smooth skin' — skin too smooth, plus strange lighting. Minus twenty-two percent click-through rate versus human-edited ones.

Second. Text readability on mobile does not work in thirty-nine point six percent of cases. Minus nineteen percent click-through rate.

Third. A mismatch between promise and content — when the thumbnail promises a scene that is not in the video. **Minus sixty-one point eight percent** drop-off in the first fifteen seconds. That is, the viewer clicks, understands that the promised thing is not there, and leaves within fifteen seconds.

[pause]

What this means in a general sense. This is empirical rejection by the end user. Not an 'aesthetic dispute'. A measurable conversion and engagement metric. AI thumbnails are not good enough for top-tier YouTube creators — where every percent of click-through rate means income. Because there are concrete failure modes: skin texture, text rendering, scene-content mismatch.

This is not 'AI is bad at art'. This is 'the current generation of AI thumbnails is bad in **this specific** conversion context'.

And this is a bridge to the fifth section. Measurable rejection by the end user is a **signal for refusal**, not just 'the users didn't like the experience'. If click-through rate falls by twenty-two percent — this is a direct impact on income, outweighing any savings on the cost of a thumbnail."

[Transition to s36.]

---

## Section 5. What the engineer should do (4 min)

### [s36 · 30 sec] — Section 5, title card

[On the slide — a large "5", the title "What the engineer should do".]

"Section five of five. What the engineer should do. Four minutes. The final artifact of the lecture, which we have assembled together from everything that came before."

[Transition to s37.]

### [s37 · 3.5 min] — A checklist of five questions

[On the slide — a 5-question flowchart in an Ocean rounded box.]

"The checklist we take away from the lecture. Five questions. Applied as a passing condition before deploying AI into a creative task. Not 'AI is forbidden'. Not 'AI is allowed'. **AI is used on the condition of passing the five questions**.

Question one. **Training-data license.** Is the corpus of the AI tool licensed? Adobe Firefly — yes. Stable Diffusion and Midjourney — there are risks. If the answer is 'no' or 'unclear' — a fallback to a tool with a licensed corpus, or refusal. This is the lesson from the Andersen and RIAA cases.

Question two. **Output-similarity check.** Can the model reproduce protected material verbatim? Implementation — embedding proximity plus a Bloom filter on known fragments. Without a check — you accept liability. This is the lesson from the NYT case.

Question three. **Voice and likeness consent.** If the voice, face or likeness of an identifiable person is generated — is there explicit consent plus compensation? Without consent — a hard stop. This is the lesson from ScarJo, Arup, Korea.

Question four. **IP-clean tools for commercial use** (without training-data risks). Are you using a commercially safe process? Firefly Foundry, licensed partner models. For consumer commercial use — this is the minimum requirement. This is the lesson from Thomson Reuters and Getty.

Question five. **Brand trust risk.** An iconic, legacy, high-brand-equity creative task? Human leadership is mandatory. AI only as a support tool, not the primary execution. This is the lesson from Coca-Cola, Toys R Us, Sports Illustrated.

[pause]

The application scheme. Simple.

If at least one of the first three is 'no' — refuse AI in this task. This is a hard stop.

If the fourth is 'no' — a choice of an alternative commercially safe tool, or refusal.

If the fifth is 'yes, iconic' — human leadership is primary, AI only a support.

If all five are 'yes' — AI is applicable. Document the choice for the audit trail.

[pause]

Each of these five questions is not an abstract 'it seems to me'. It is a measurable answer. And it is operationalizable. You can, tomorrow, attach this checklist to a pull request in a repository where an AI tool will be integrated into a creative process. And it will work."

[Transition to s38.]

---

## Section 6. Questions and answers, closing (3 min)

### [s38 · 2.5 min] — Questions and answers

[On the slide — a large "Questions and answers" plus backup prompts.]

"Time for questions. What do you want to work through more deeply — let's discuss it together.

[pause, I wait for hands]

[If there are no questions — backup topics on the slide. Ready to discuss.]

Possible directions to go deeper: if you are interested in architectures — why exactly diffusion gave the 'commercially safe' Firefly, and not Stable Diffusion with the same approach. If you are interested in the lawsuits — how Sony versus Suno remained the last actively litigating major label, and what is strategic in that. If you are interested in the Russian context — the structural reasons for the frontier gap on video and music. If you are interested in deployment — how to do an output-similarity check in a production system.

[pause]

And the most important thing — three observations from today's lecture. First: architecturally, generative AI is three families, each with its own internal limits. Second: economically, AI added, changed, broke — three tenses of one process. Third: legally, reference cases are open in all four categories of copyright lawsuits, and the outcome will determine the landscape of the next five years.

The checklist of five questions is an **entry into the collection of a personal checklist**. The finale — in Lecture seventeen, 'Systematization of knowledge and skills', where we assemble a checklist from all the industry cases of the course."

[Transition to s39.]

### [s39 · 30 sec] — Closing

[On the slide — the title of Lecture 9 + QR sources.]

"Next — Lecture nine. AI in the aerospace industry and the defense complex.

Where today an AI failure is a drop in sentiment and 'soulless' comments, there a failure creates a kinetic outcome. An escalation of the stakes to another level.

Sources — by QR. Thank you for your attention."

[Closing.]

---

## Reserve (5 min)

- Additional questions from the audience.
- Reserve for technical failures at the start (the s01 Suno demo failed — switch to Firefly or to the backup PNG).
- Going deeper on the topic that struck a chord: if copyright — details of NYT's verbatim-reproduction theory and output-similarity checking as an engineering practice; if the Russian context — the structural reasons for the frontier gap and the timeline of the Mintsifry bill; if deepfakes — the Telegram moratorium and the enforcement gap; if displacement — Shutterstock's pivot to selling data to AI companies; if architecture — why Firefly Foundry differs technologically from a Stable Diffusion deployment.
- Contact for subject-matter questions — `levko.maxim@gmail.com` or through the course elder.

---

**Timing summary (layout).**

- Section 0 (opening + keystone axis + fundamentals): 9.5 min = s01 (3) + s02 (0.1) + s03 (2) + s04 (1.5) + s05 (1.4) + s05a (1.5).
- Section 1 (ADDED): 12 min = s06 (0.5) + s07 (2) + s08 (2) + s09 (2) + s10 (1.5) + s10a (2) + s11 (2).
- Section 2 (CHANGED): 10.5 min = s13 (0.5) + s14 (3) + s15 (2.5) + s16 (2.5) + s17 (2).
- Section 3 (BROKE): 23.5 min = s19 (0.5) + s20 (1.5) + s21 (2) + s22 (2) + s23 (2) + s24 (2) + s25 (2) + s26 (2.5) + s27 (2) + s28 (2) + s29 (2) + s30 (1.5) + s31 (1.5).
- Section 4 (not needed): 7.5 min = s32 (0.3) + s33 (2.5) + s34 (2) + s35 (2.7).
- Section 5 (what to do): 4 min = s36 (0.5) + s37 (3.5).
- Section 6 (questions and closing): 3 min = s38 (2.5) + s39 (0.5).
- Active speech: 70 minutes.
- Reserve: 5 minutes.
- Total: 75 minutes.

**Share of failures/limitations/alternatives by time.** Section 3 (23.5) + Section 4 (7.5) + Section 5 (4) = 35 min of 75 = **46.7% strict-in**. Target ≥30% — met.

**Lecture goals achieved in the speech.** LO1 — classification of four creative domains plus specific 2026 tools (s07-s11). LO2 — assessment of applicability through the mental model of three families (s05a) and the cost-collapse table (s14). LO4 — twelve reference cases with the failure mechanism plus a lesson (s20-s31). LO5 — four criteria for refusal (s33) and the five-question checklist (s37) as a practical tool.

**Cross-references from the coursebook (synchronized with the canon).** Lecture 1 — the frame 'where AI works, where it does not' is deepened here to four criteria. Lecture 3 — platform-layer architectures mentioned on s11. Lecture 5 — a parallel of legal risk in s20 verbally. Lecture 7 — a parallel of the four-actor model of responsibility verbally in s20. Lecture 9 — a forward reference to the escalation of the human in the loop, to the kinetic outcome, in s39.

## Changelog
- v3 (2026-05-20, deep Russification): comprehensive ~250 anglicism replacements across all 39 slide fragments + frontmatter + reserve. Top-50 anglicism list per orchestrator deep-grep (919 unique non-allowlist tokens baseline) systematically replaced: voice→голос, training→обучающий, model→модель, content→содержимое/материал, pipeline→конвейер/процесс, displacement→вытеснение, consent→согласие, cloning→клонирование, brand→бренд, harm→ущерб, outcome→исход, source→источник, output→результат/вывод, copyright→авторское право, ruling→решение, thumbnails→миниатюры, freshness→актуализация, summary judgment→упрощённое решение суда, discovery→истребование доказательств, motion to dismiss→ходатайство об отказе в иске, theory of harm→теория ущерба, training corpus→обучающий корпус, fair use→добросовестное использование, style mimicry→подражание стилю, voice/likeness→голос/образ, deepfake→deepfake (kept Latin per established RU usage), backlash→негативная реакция, legacy trust→накопленное доверие, brand-equity→капитал бренда, iconic→культовый/эталонный, settled→урегулирован, inductive lesson→вывод, hard stop→жёсткий стоп, support tool→вспомогательный инструмент, IP-clean tools→IP-чистые инструменты, commercial-safe pipeline→коммерчески безопасный процесс, takedown requests→запросы на удаление, prosecuted→привлечены к ответственности, enforcement→правоприменение, frontier→фронтирный, etc.
- Allowed Latin kept: brand names (Sora 2, Suno, Midjourney, Firefly, Stable Diffusion, ElevenLabs, Veo, Kling, NYT, OpenAI, etc.), case names (Andersen, Goldsmith, Bibas, Orrick), legal acronyms with first-appearance gloss (DMCA, MTD, SJ, KDP, CDPA), technical terms (LLM, GPU, deepfake, podcast).
- v2 (2026-05-20, Phase 11 batched revision): Cross-artifact consistency sync + first russification pass per consistency-check v1.
  - **P0-1:** Toys R Us Sora-ad длительность: «шестидесятисекундный» → «шестидесятишестисекундный» в [s07] и [s30] (matches chapter §1.1 + §3.11 «66-секундный»).
  - Russification narrow-list (32 patterns, 72 hits): output similarity, fair use, capability, verbatim, etc. — все заменены.
  - D5: [s10a] «Suno v5» → «Suno v5.5» (matches chapter §1.6 + §7 glossary lock).
  - D13: [s07 pre-flight] «дискретизировано» → «прекращена поддержка».
- v1 (2026-05-20): initial draft from chapter v2 + deck v3. 39 слайдов покрыты. ~5,500 спикерских слов. Pacing 70 мин активной речи + 5 мин буфер. WPM: avg 78.7, max <95 (0 violations). Failure-share 50% strict-in по времени. «Мы с вами» — 18 hits across 6 sections. Bridge phrases для всех 5 dividers.
