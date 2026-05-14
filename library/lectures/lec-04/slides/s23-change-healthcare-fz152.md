---
id: s23
type: assertion_visual
duration_min: 3
assertion: "Медицинские данные — самая защищаемая категория. И самая ценная для атакующих. Change Healthcare (Feb 2024): 190M человек, $2.457 млрд recovery cost."
learning_goal: "Medical data security + AI training datasets risk + ФЗ-152/ФЗ-23"
learning_outcomes: [LO3, LO8]
frame_mapping: ["Безопасность", "Человек vs AI"]
chapter_ref: "§4.5 — Безопасность медицинских данных"
references: [uhg-2024, bleeping-computer-2024, hipaa-journal-2024, sweeney-2002]
visual:
  pattern: matrix
  primary: "News screenshot Change Healthcare + 5 info-cards (190M / $2.457B / 6 TB / multi-week / $22M ransom) + AI connection bridge mosmed.ai 18M+ images"
  illustration:
    type: news
    sources:
      - "UHG official — https://www.unitedhealthgroup.com/newsroom/2024/2024-04-22-uhg-updates-on-change-healthcare-cyberattack.html"
      - "BleepingComputer 190M — https://www.bleepingcomputer.com/news/security/unitedhealth-now-says-190-million-impacted-by-2024-data-breach/"
      - "HIPAA Journal 2024 — https://www.hipaajournal.com/biggest-healthcare-data-breaches-2024/"
      - "House Energy & Commerce — https://energycommerce.house.gov/posts/what-we-learned-change-healthcare-cyber-attack"
    caption: "Change Healthcare breach Feb 2024 (UHG, BleepingComputer)"
interaction: none
---

# Медицинские данные — target №1 для атакующих

## Assertion

Медицинские данные — самая защищаемая категория. И самая ценная для атакующих. Change Healthcare (Feb 2024): 190M человек, $2.457 млрд recovery cost.

## Visual

Сверху ассертион 24pt + small news headline screenshot Change Healthcare breach в Ocean rounded box. По центру — 5 info-cards в горизонтальный ряд в Ocean rounded box: `190M Americans affected` (~57% US pop), `$2.457B recovery cost` (UHG Q3 2024, **gold highlight**), `6 TB exfiltrated`, `multi-week disruption`, `ALPHV/BlackCat $22M ransom paid`. Снизу — bridge-card в Ocean rounded box: «AI connection: medical AI training datasets inherit medical-data security risk. mosmed.ai = 18M+ images → ransomware target scope. Anonymisation ≠ anonymity (Sweeney 2002 re-identification)». Внизу 3 regulation chips: HIPAA · GDPR · ФЗ-152 + ФЗ-23 (1 июля 2025).

## Speaker notes

Медицинские данные — самая защищаемая категория данных в большинстве юрисдикций. И — самая ценная для атакующих, потому что они содержат combinations PII плюс медицинскую историю, которые нельзя «отменить»: номер кредитной карты банк блокирует за минуты, медицинский диагноз — нельзя.

Кейс — Change Healthcare breach, февраль 2024 года, крупнейший healthcare data breach в истории США. Двадцать первого февраля ransomware-группа ALPHV/BlackCat атаковала Change Healthcare — дочернюю компанию UnitedHealth Group, обрабатывающую около трети всех claims в американской системе здравоохранения. Vector атаки — уязвимый Citrix remote access без MFA. Числа: сто девяносто миллионов американцев в затронутом объёме PHI — примерно пятьдесят семь процентов населения США. Шесть терабайт данных эксфильтровано. Двадцать два миллиона долларов выкупа выплачены в Bitcoin. Два миллиарда четыреста пятьдесят семь миллионов долларов — total recovery cost для UHG за третий квартал 2024 года. Многонедельный перерыв в обработке claims по всей US healthcare system.

Связь с medical AI критически важна. Medical AI training datasets наследуют security risk медицинских данных. mosmed.ai имеет более восемнадцати миллионов медицинских изображений в своих datasets. Что произойдёт, если такой dataset эксфильтрован? Анонимизация не равна анонимности: каноническая иллюстрация — re-identification медзаписи губернатора Massachusetts через сопоставление HIPAA-compliant deidentified dataset с публичным voter roll, Sweeney 2002. Полную anonymity при работе со структурированными PII обычно невозможно гарантировать.

Регуляторика. HIPAA (US, 1996) защищает PHI и ePHI. GDPR (EU, 2016/679) — sensitive personal data special category, Article 9. ФЗ-152 (РФ, 2006) с major amendments 2024–2025: с 30 мая 2025 года ужесточённые требования к операторам. ФЗ-23 от 28 февраля 2025 года (data localization): персональные данные граждан РФ не обрабатываются на серверах вне России с 1 июля 2025 года. Инженерный урок: проектируя medical AI, вы проектируете target для criminal groups. Защита: data localization, de-identification + differential privacy, segmentation, secure-by-design pipeline.
