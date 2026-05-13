---
id: s22
type: assertion_visual
duration_min: 4
assertion: "LLM в медицине ≠ медицинский AI. 3 documented anti-pattern cases на 2025-2026: vendor accountability, adversarial hallucination, mass self-diagnosis."
learning_goal: "3 LLM anti-pattern cases: Tessa vendor accountability + adversarial 83% + 40M self-diagnosis"
learning_outcomes: [LO3, LO8]
frame_mapping: ["LLM anti-pattern", "Безопасность", "Человек vs AI"]
chapter_ref: "§5.3 — LLM-анти-паттерны в медицине"
references: [npr-2023-tessa, ai-incident-db-545, comm-medicine-2025, beckers-2025, gallup-2025]
visual:
  pattern: matrix
  primary: "3 case-cards в Ocean rounded box: NEDA Tessa timeline + Adversarial 83% + 40M self-diagnosis; NEDA framed «vendor accountability story»"
  illustration:
    type: news
    sources:
      - "NPR 2023 — https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea"
      - "AI Incident Database 545 — https://incidentdatabase.ai/cite/545/"
      - "Communications Medicine 2025 — https://www.nature.com/articles/s43856-025-01021-3"
      - "Becker's Hospital Review 40M — https://www.beckershospitalreview.com/healthcare-information-technology/ai/40m-americans-turn-to-chatgpt-for-healthcare-report/"
      - "Gallup AI healthcare survey — https://news.gallup.com/poll/707789/americans-turning-supplement-healthcare-visits.aspx"
    caption: "NEDA Tessa May 2023; Adversarial 83% 2025; OpenAI/Gallup 40M"
interaction: none
---

# LLM в медицине ≠ medical AI — 3 documented cases

## Assertion

LLM в медицине ≠ медицинский AI. 3 documented anti-pattern cases на 2025–2026: vendor accountability, adversarial hallucination, mass self-diagnosis.

## Visual

3 равные case-cards в Ocean rounded box, вертикально на всю ширину слайда. Card 1 — «NEDA Tessa scandal»: иконка `message-circle-warning`, 3-event mini-timeline: «~2018–2022 rule-based» → «March 2023 Cass switches к generative БЕЗ NEDA approval» → «May 30, 2023 Sharon Maxwell screenshots → suspend 24h». Frame badge **gold**: «vendor accountability story». Card 2 — «Adversarial hallucination 83%»: иконка `alert-octagon`, число `83%` крупно gold; «Communications Medicine 2025; 6 LLMs; 300 clinical vignettes; mitigation prompt halves but not zero». Card 3 — «Patient self-diagnosis 40M»: иконка `users`, число `40M Americans` крупно; «3 of 5 US adults use AI for health past 3 months; OpenAI/Gallup 2024–2025; регулирование не успевает».

## Speaker notes

LLM в медицине — это не то же самое, что medical AI. Это важное различие. Medical AI, который проходит FDA-одобрение, — специализированная computer vision или табличная модель с подтверждённой клинической валидацией. LLM в медицинском контексте — general-purpose language model, который случилось так, что используется для медицинских вопросов; и в этом качестве на 2025–2026 годы зафиксированы три documented anti-pattern cases.

Первый кейс — NEDA Tessa, vendor accountability story. National Eating Disorders Association с примерно 2018 года использовала чат-бот Tessa, разработанный компанией Cass, как первую линию helpline. Изначально Tessa был rule-based: чёткий decision-tree, никакой генерации, никаких советов вне предварительно одобренных сценариев. Это design choice со стороны NEDA — eating disorders requires clinical safety design. В марте 2023 года Cass самовольно сменила Tessa с rule-based на generative LLM — без согласования с NEDA, без новой клинической валидации. 30 мая 2023 года Sharon Maxwell опубликовала скриншоты: Tessa в новой форме советовал терять один-два фунта в неделю, удерживать дефицит калорий пятьсот-тысячу в день, целиться на две тысячи калорий максимум в день — классические eating disorder triggers. NEDA сняла Tessa с обращения в течение двадцати четырёх часов. Урок: generative AI ≠ rule-based AI; vendor design changes могут обойти clinical safety design.

Второй кейс — adversarial hallucination. Communications Medicine 2025 года: шесть ведущих LLM на трёхстах клинических vignette'ах с подсаженной фейк-деталью. Модели повторяли или расширяли подсаженный фейк в восьмидесяти трёх процентах случаев. Mitigation prompt снижал rate примерно вдвое, но не до нуля. Урок: LLMs are gullible к planted errors; человеческая верификация фактов требуется для каждого факта.

Третий кейс — patient self-diagnosis. Примерно сорок миллионов американцев используют ChatGPT для healthcare-вопросов; три из пяти взрослых — за последние три месяца. Регулирование за этим не успевает. Если строите medical-adjacent LLM-product — design choices масштабируются на десятки миллионов людей.
