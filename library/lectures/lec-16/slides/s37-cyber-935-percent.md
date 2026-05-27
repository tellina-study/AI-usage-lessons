---
id: s37
type: failure_case
duration_min: 2
assertion: "Ransomware-атаки на нефтегаз: +935% между апрелем 2024 и апрелем 2025 (Zscaler). Colonial Pipeline 2021 — VPN без MFA. Безопасность — phase 1, не phase 4."
learning_goal: "Cross-cutting failure: cyber + Colonial canonical"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter-part4.md]
  sections: ["§6.1 Cross-cutting риск 1: киберугрозы"]
visual:
  type: image
  description: "Colonial Pipeline 2021 shutdown news photo OR Zscaler ThreatLabs +935% report cover"
  source_url: "https://www.zscaler.com/blogs/security-research"
  acquisition_tier: 1
visible_numbers: ["+935% ransomware на O&G апр 2024 → апр 2025", "Colonial Pipeline 6 дней shutdown", "$4,4M ransom paid"]
russification_check: "Zscaler, ThreatLabz, Colonial Pipeline, DarkSide, Shell, Clop, MOVEit, Dragos, Claroty, Nozomi Networks, CISA, DOJ — brand list; «многофакторная аутентификация», «защитный/наступательный AI» — RU."
speaker_notes_target_words: 230
---

# Cyber +935% на O&G апр 2024 — апр 2025. Безопасность — phase 1, не phase 4.

## Visible content

Заголовок: «Ransomware на нефтегаз +935% год к году. Counter-trend AI-расширения.» (28pt deep ocean).
Sub: «OT/IT convergence + AI deployment добавляет attack surface. Defensive AI отстаёт от offensive AI.» (16pt italic)

**Слева — Ocean rounded box «Канонические incidents»:**

- **Colonial Pipeline 2021** — DarkSide ransomware → 5 500 миль pipeline shutdown **6 дней** (gold).
- Топливный дефицит на East Coast US.
- **$4,4M ransom paid** (75 BTC; ~$2,3M recovered by DOJ Jun 2021).
- Recovery ~$200M+.
- Атакующий получил доступ через **VPN без MFA** (многофакторная аутентификация).
- **Shell MOVEit 2022 + 2024 vendor compromise** — Clop ransomware через third-party software.

**Справа — Ocean rounded box «Defensive vs Offensive AI structural gap»:**

- **Defensive AI** (anomaly detection в OT-сетях): Dragos, Claroty, Nozomi Networks — leading vendors. Растёт post-Colonial.
- **Offensive AI**: LLM-агенты для automated phishing, social engineering, automated reconnaissance. **Растёт быстрее.**
- AI security ≠ traditional IT security. Adversarial ML, model poisoning, prompt injection — новые классы атак.

**Bottom bar (gold tint) — 3 урока для LO7:**

1. **AI добавляет сложность → поверхность атаки растёт.**
2. **Безопасность — phase 1, не phase 4** (embed cybersecurity в design phase).
3. **AI security ≠ traditional IT security** → specialized AI security teams необходимы.

## Speaker notes

Кибербезопасность — counter-trend AI-расширения нефтегазовой автоматизации. По данным Zscaler, ransomware-атаки на нефтегаз выросли на девятьсот тридцать пять процентов между апрелем 2024 и апрелем 2025 года. База — Zscaler ThreatLabz фиксирует относительный рост числа известных ransomware-инцидентов в секторе year-over-year; абсолютные числа Zscaler не раскрывает в open report. Для контекстуализации масштаба — paradigmatic high-impact case остаётся Colonial Pipeline 2021.

Colonial Pipeline 2021. Атакующий получил доступ через VPN без MFA — многофакторной аутентификации. Pipeline shutdown около шести дней; четыре и четыре десятых миллиона долларов ransom paid — семьдесят пять биткоинов; примерно два и три десятых миллиона recovered Министерством юстиции в июне 2021 года. Операционные потери — десятки миллионов. Recovery cost оценочно двести миллионов плюс. Lesson: flat OT/IT network плюс no MFA на VPN равно unacceptable risk для critical infrastructure.

Shell MOVEit 2022 плюс 2024 vendor compromise. Shell был impacted Clop ransomware через MOVEit file transfer vendor — third-party software, used by multiple companies. Customer data leaked.

Этот рост — не «random fluctuation»; это структурный эффект. OT/IT convergence увеличивает attack surface. Развёртывание AI и цифровых сервисов добавляет новые ML-сервисы, новые конвейеры данных, новые API-эндпоинты — каждый из них потенциальная точка входа. Threat actor capability растёт через offensive AI.

Defensive vs offensive AI — структурный gap. Defensive AI — anomaly detection в OT-сетях, ML-based intrusion detection — Dragos, Claroty, Nozomi Networks. Растёт post-Colonial. Offensive AI — атакующие используют LLM-агенты для automated phishing, social engineering, automated reconnaissance. Растёт быстрее, чем defensive AI.

Три фундаментальных урока для LO7. Первое — AI добавляет сложность, поверхность атаки растёт. Второе — безопасность это phase 1, не phase 4. Embed cybersecurity в design phase. Третье — AI security не равно traditional IT security. Adversarial ML, model poisoning, prompt injection — новые классы атак.
