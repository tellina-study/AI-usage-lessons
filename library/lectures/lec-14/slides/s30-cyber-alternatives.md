---
id: s30
type: assertion_visual
duration_min: 1
assertion: "Альтернативы AI в cyber: YARA+Sigma+Snort, hash-based, NIST SP 800-207 Zero Trust, out-of-band verification, manual threat hunting, CIS/NIST CSF/ISO 27001."
learning_goal: "Cyber alternatives"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema"
---

# Альтернативы AI в cyber — 80% защиты за 20% стоимости

## Visible content

6 карточек в сетке 3×2:
• YARA + Sigma + Snort — Rule-based detection. Сигнатуры + правила. Детерминированно. Дёшево. 70% угроз — известные паттерны.
• Hash-based signatures — MD5 / SHA256 IOC. Известные malware hashes. Мгновенная блокировка. AI не нужен.
• NIST SP 800-207 Zero Trust — Архитектурный подход. «Never trust, always verify». Архитектура важнее ML-модели.
• Проверка через независимый канал (out-of-band) — победа Ferrari/WPP. Перезвонить по официальному номеру. Простой процесс > AI-детектор дипфейков.
• Ручной threat hunting — MITRE ATT&CK. Опытный аналитик с гипотезами > LLM на 10 000 алертах.
• CIS / NIST CSF / ISO 27001 — Базовые фреймворки. Базовая гигиена. 80% защиты за 20% бюджета. AI не нужен.

## Speaker notes

Шесть классов альтернатив AI в кибербезопасности. Это «80% защиты за 20% стоимости» в чистом виде.

YARA, Sigma, Snort. Три rule-based detection engine — YARA для файлов, Sigma для логов, Snort для сетевого трафика. Десятки лет в проде. Сигнатуры обновляются через threat intel feeds. Детерминированно, дёшево. Около семидесяти процентов реальных угроз — это известные паттерны, для которых сигнатуры уже есть.

Hash-based signatures — MD5, SHA256 IOC. Когда известен hash конкретного malware — мгновенная блокировка. AI здесь не нужен и не быстрее.

NIST SP 800-207 Zero Trust. Это не инструмент, это architecture pattern. «Never trust, always verify». Каждое action verify по identity, device, context. ML не нужен — нужна правильная архитектура. Это часто важнее любой ML-модели.

Out-of-band verification. Мы видели на s26 — Ferrari и WPP выиграли деpfake-атаку простыми вопросами вне atypical канала. Это процесс, не технология. Дешевле любого deepfake detector.

Manual threat hunting. Опытный аналитик с MITRE ATT&CK картой и hypothesis-driven approach — часто эффективнее LLM, который перебирает десять тысяч алертов. Threat hunter говорит «давайте проверим, нет ли patterns lateral movement через PowerShell с парами unusual host-to-host». LLM такие гипотезы не сформирует, потому что у него нет контекста именно этого окружения.

CIS Controls, NIST CSF, ISO 27001 — базовые фреймворки compliance. Если не выполняете базовую гигиену по CIS Controls — никакой AI не починит security posture. Восемьдесят процентов защиты — это базовая гигиена. AI поверх базовой гигиены может дать дополнительные пятнадцать процентов. AI без базовой гигиены — ноль.
