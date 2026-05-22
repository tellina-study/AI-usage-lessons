---
id: s29
type: assertion_visual
duration_min: 1
assertion: "Когда AI НЕ нужен в кибербезопасности: forensic-цепочка, нормативные требования, горячая фаза реагирования, сигнатурные угрозы, аппаратные/крипто-примитивы, малый бизнес <50 эндпойнтов."
learning_goal: "Cyber criteria «AI не нужен»"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema"
---

# Когда AI НЕ нужен в cyber — шесть критериев

## Visible content

6 карточек в сетке 3×2:
1. Юридический аудит-трейл (forensic) — Court-admissibility. ML-вероятность в суде не пройдёт. Нужна детерминированная цепочка свидетельств.
2. Нормативные требования — PCI-DSS / HIPAA / SOX. ML-вероятность не проходит аудит. Аудиторы хотят rule-based logic.
3. Горячая фаза реагирования (IR) — Incident response. Скорость > масштаб. Решения принимает человек, не LLM с латентностью 5 секунд.
4. Сигнатурные угрозы — Известные IOC. YARA / Sigma / Snort быстрее, дешевле, детерминированнее.
5. Аппаратные / firmware attestation — TPM, secure boot. Криптографические примитивы. Никогда ML.
6. Малый бизнес <50 эндпойнтов — Стоимость AIOps-лицензии > выгода. Управляющие правила + Defender для бизнеса.

## Speaker notes

Шесть критериев, когда AI не нужен в кибербезопасности. Каждый — структурный, не вкусовой.

Первый — forensic chain, court-admissibility. Любое решение, которое может попасть в суд как evidence, не может быть probabilistic. ML вероятность «эта активность аномальная с p=0,87» в суде не работает. Нужна детерминированная цепочка — конкретное правило, конкретное событие, конкретный audit trail.

Второй — compliance hardlines. PCI-DSS, HIPAA, SOX, ISO 27001. Все эти стандарты ожидают rule-based logic для определённых control activities. ML fails audit — не «возможно», fails.

Третий — IR hot phase. Incident Response — стадии, когда атака ещё развивается, нужно срочно действовать. Скорость важнее scale. LLM с латентностью пять секунд — это медленно. Решения принимает senior SOC analyst, не AI. AI здесь только для контекста, не для решения.

Четвёртый — signature threats. Известные malware signatures, IOC от threat intel feeds. YARA, Sigma, Snort правила — быстрее, дешевле, детерминированнее. Зачем нагружать LLM хешами файлов?

Пятый — hardware и firmware attestation. TPM, secure boot, cryptographic verification. Никогда ML. Это математика, детерминированная криптография. Вероятность здесь — катастрофа.

Шестой — SMB, малый бизнес меньше пятидесяти endpoints. Cost лицензии AIOps платформы выше, чем value AI. Базовые правила, Microsoft Defender для бизнеса, обычная гигиена — достаточно.

Если хотя бы один критерий — auto-mode AI в cyber выключаем.
