---
id: s29
type: assertion_visual
duration_min: 3
assertion: "Фарма AI ±0,5% accuracy vs FDA-required ±0,1% precision. AI не подходит для release decision."
---

## Visible content

Concrete worked example по критерию 5.3.

## Speaker notes

Проработанный пример из chapter §5.3 — конкретный сценарий, через который проходит десять критериев.

Сценарий: фармацевтическое производство, AI-система рекомендует дозировку активного компонента в финальной формуляции таблеток. Что AI способен: обучается на исторических партиях, предсказывает оптимальную дозировку с точностью ±0,5% от номинала, 90% accuracy на тестовом наборе. Это респектабельный результат для ML на относительно небольшой выборке.

Что FDA требует. FDA 21 CFR Part 11 — стандарт для электронных записей и подписей в регулируемой фармацевтической среде. GAMP 5 — Good Automated Manufacturing Practice version 5, gold-standard для валидации программных систем в фарма-производстве. Для batch release decision требуется precision ±0,1% от номинала.

Разрыв. AI accuracy ±0,5% — в 5 раз шире (хуже) required tolerance ±0,1%. Это несовместимо. Verdict: AI не подходит для финального release decision.

Альтернатива. AI как advisory tool на этапе process design, где точность ±0,5% полезна. Инженер видит рекомендации AI при дизайне нового продукта, оценивает, принимает или отвергает. Для release — human-in-loop QA плюс statistical batch sampling, validated по USP и GMP.

Cross-reference: лекция 7 ввела FDA 21 CFR Part 11 как принцип. Этот кейс — конкретная инстанцияция того, как принцип работает в фарме. Универсальный паттерн: всегда сравнивайте accuracy AI с required tolerance для решения. Если AI не дотягивает — он не подходит для этого решения, но может подходить для другого.
