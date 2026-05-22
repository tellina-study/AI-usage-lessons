---
id: s33
type: assertion_visual
duration_min: 2
assertion: "Семь слоёв производственной AI-архитектуры: датчик → сеть → ИИ на границе → MES → twin → облако → человек."
---

## Visible content

7-слойный стек 2026.

## Speaker notes

Производственная AI-архитектура 2026 — семислойный стек. Слой первый: датчики на оборудовании. IIoT через OPC UA + MQTT, sampling rate не менее десятикратного управляющей полосы. Слой второй: сеть. TSN — Time-Sensitive Networking, IEEE 802.1, гарантированная детерминированная задержка Ethernet. Без TSN edge AI с задержкой менее 10 мс невозможен. Слой третий: edge AI. GPU micro-серверы на cabinets, NVIDIA Jetson, Dell edge, Schneider Modicon edge. Инференс менее 10 мс. Слой четвёртый: MES/SCADA. AI как advisory переходит в closed loop. Диспетчерское управление. Слой пятый: цифровой двойник. Siemens Xcelerator + NVIDIA Omniverse + AVEVA + PTC ThingWorx — основные платформы 2026 года. Слой шестой: облако. Обучение моделей, fleet analytics, long-term storage. Слой седьмой: человек в цикле. Safety-critical контуры всегда gated через HITL.

Все семь слоёв должны быть production-grade. Vendors интегрируются без PLC reprogramming: Siemens S7, Allen-Bradley, Rockwell, Schneider — все поддерживают OPC UA как минимум.

Distribution через Lighthouse Network. 220+ заводов в 35 странах. 23 новых сайта в 2026 году. 90% новых внедрений включают AI. Перевес Lighthouse-сайтов +16% по EBIT vs peers. WEF + McKinsey, январь 2026.
