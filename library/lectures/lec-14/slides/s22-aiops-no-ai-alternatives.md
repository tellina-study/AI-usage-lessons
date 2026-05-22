---
id: s22
type: assertion_visual
duration_min: 1.5
assertion: "AIOps: когда AI НЕ нужен — forensic-цепочка, нормативные требования, редкие события, детерминированная задержка, малый масштаб. Альтернативы: Nagios/Zabbix, SPC, Rundeck, SLO burn-rate."
learning_goal: "AIOps criteria + alternatives"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema"
---

# AIOps: когда НЕ нужен — и чем заменить

## Visible content

Слева — «КОГДА НЕ НУЖЕН»:
• Юридический аудит-трейл (forensic) — каждое решение нужно объяснить суду
• Нормативные требования (PCI-DSS / SOX / HIPAA) — ML-вероятность не проходит аудит
• Редкие события — математика Байеса: PPV падает на низкой базовой ставке
• Детерминированная задержка — URLLC / hot path ядра — ML вносит хвост распределения
• Малый масштаб (<50 серверов) — конфиг + мониторинг дешевле AIOps-лицензии

Справа — «АЛЬТЕРНАТИВЫ»:
• Nagios / Zabbix — мониторинг на правилах. Десятки лет проверено.
• SPC — статистический контроль процессов — 3σ карты Шухарта. Деминг, 1924 → 2026.
• Runbook-as-code — Rundeck / Ansible — детерминированные сценарии.
• SLO burn-rate (Google SRE) — многооконные алерты без ML. Математика бюджета ошибок.
• Chaos engineering — Netflix Chaos Monkey — проверка устойчивости, а не предсказание.

## Speaker notes

Когда AIOps не нужен — пять структурных критериев.

Forensic audit trail. Если нужно объяснить регулятору или суду каждое решение системы — ML probability не работает. Нужна детерминированная цепочка. Аудиторы спрашивают «почему было заблокировано» — «вероятность 0,87» не ответ.

Compliance hardlines. PCI-DSS, SOX, HIPAA, ISO 27001 — все эти стандарты ожидают rule-based logic, не probability. ML model fails audit. Не «возможно fails», а fails.

Rare events. Мы только что разобрали Bayes — на низкой базовой ставке PPV падает. На редких событиях ML делает кучу false positives. Используйте signature-based detection (YARA, Sigma, Snort), threat intel feeds.

Deterministic latency. URLLC, kernel hot path, E911. ML вносит хвост распределения по латентности — иногда ответ за 10 мс, иногда за 500. Для critical path это неприемлемо. PID, MPC, rule-based.

Small scope. Если у вас меньше пятидесяти серверов — стоимость лицензии AIOps платформы выше, чем ценность. Конфиг + monitoring дешевле.

Альтернативы. Nagios и Zabbix — десятки лет проверены, open source, миллионы deployments. SPC — Statistical Process Control от Деминга 1924 года — три-сигма control charts работают и в производстве, и в IT. Runbook-as-code: Rundeck, Ansible — детерминированные workflow с git audit trail. SLO burn-rate от Google SRE — многооконное alerting без ML, математика error budgets. И chaos engineering — Netflix Chaos Monkey — не предсказывает, а проверяет устойчивость к реальным сбоям.

80% защиты за 20% стоимости — это про правильный выбор классики там, где AI не даёт преимущества.
