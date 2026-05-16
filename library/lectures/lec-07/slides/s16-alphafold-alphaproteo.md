---
id: s16
type: assertion_visual
duration_min: 2.5
assertion: "AlphaFold предсказал 200M+ структур белков — решённая задача 50-летней давности. AlphaProteo проектирует binders de novo. Нобель 2024."
learning_goal: "AlphaFold/AlphaProteo concrete achievements + Нобель 2024"
learning_outcomes: [LO1, LO2]
frame_mapping: ["Другой AI"]
chapter_ref: "§3.2 — AlphaFold 3 и AlphaProteo"
references: [jumper-2021-nature, abramson-2024-nature, watson-2024-alphaproteo, alphafold-db]
visual:
  pattern: matrix
  primary: "3 evidence-cards в Ocean rounded box (200M+ structures / AlphaProteo 88% BHRF1 / AlphaFold 3 +50% PoseBusters) + AlphaFold 3D snapshot справа"
  illustration:
    type: official_product
    sources:
      - "AlphaFold Protein Structure Database — https://alphafold.ebi.ac.uk/ (front page, screenshot example structure)"
      - "DeepMind AlphaFold blog — https://deepmind.google/technologies/alphafold/"
      - "DeepMind AlphaProteo blog — https://deepmind.google/discover/blog/alphaproteo-generates-novel-proteins-for-biology-and-health-research/"
      - "Abramson et al. 2024 Nature AlphaFold 3 — https://www.nature.com/articles/s41586-024-07487-w"
      - "Watson et al. AlphaProteo arXiv:2409.08022 — https://arxiv.org/abs/2409.08022"
    caption: "AlphaFold DB; AlphaProteo arXiv:2409.08022; Abramson 2024"
interaction: none
---

# AlphaFold 200M+; AlphaProteo проектирует binders de novo

## Assertion

AlphaFold предсказал 200M+ структур белков — решённая задача 50-летней давности. AlphaProteo проектирует binders de novo. Нобель 2024.

## Visual

Слева — три evidence-card в Ocean rounded box (вертикально). Card 1 (Primary mid): заголовок «AlphaFold DB» 20pt, число `200M+ structures` крупно 36pt gold, ниже мелким «alphafold.ebi.ac.uk · open, free». Card 2: заголовок «AlphaProteo (Sep 2024)», число `88% success rate` крупно, ниже «BHRF1 target; 3–300× affinity vs prior methods; first AI binder для VEGF-A». Card 3: заголовок «AlphaFold 3 (Nature May 2024)», число `+50% accuracy` крупно, ниже «PoseBusters benchmark vs classical docking; protein-ligand interactions». Справа — 3D-рендеринг структуры белка из AlphaFold DB (screenshot) в Ocean rounded box. Сверху — assertion + small badge «Нобелевская премия по химии 2024».

## Speaker notes

Самое заметное достижение AI в drug discovery за последние два года — линейка foundation models DeepMind для биологии. Эта линейка получила половину Нобелевской премии по химии 2024 года: Demis Hassabis и John Jumper за AlphaFold разделили её с David Baker за computational protein design в Розетте.

AlphaFold 2 (2021) решила пятидесятилетнюю задачу — предсказание трёхмерной структуры белка по аминокислотной последовательности. К 2024 году в открытой AlphaFold Protein Structure Database — более двухсот миллионов структур белков. База открыта и бесплатна, доступна по адресу alphafold.ebi.ac.uk. DeepMind также заявляет о более чем двух миллионах исследователей-пользователей; эта последняя цифра — self-reported industry metric, не peer-reviewed, поэтому мы её приводим с явной атрибуцией.

AlphaFold 3 (Nature, 8 мая 2024) — diffusion-based архитектура, расширяющая возможности от чисто белков к биомолекулярным комплексам: protein–DNA, protein–RNA, protein–ligand, ion. Улучшение точности примерно на пятьдесят процентов на бенчмарке PoseBusters для protein-ligand interactions — это первый случай, когда AI-система превзошла classical physics-based методы докинга, основной инструмент computational drug discovery последних тридцати лет.

AlphaProteo (DeepMind, 5 сентября 2024) — семейство ML-моделей для de novo дизайна белковых binders. По данным DeepMind: восемьдесят восемь процентов success rate для целевого белка BHRF1; улучшение аффинности в три–триста раз против лучших ранее доступных методов на семи белковых мишенях; первый AI-сгенерированный binder для VEGF-A. Caveat — независимая репликация в других лабораториях публично пока не зафиксирована, поэтому это DeepMind's own claim, а не консенсусный peer-reviewed результат. Важная инженерная деталь: AlphaFold предсказывает структуру; drug discovery требует ещё lead optimization, ADMET, валидации. Это accelerator одной стадии, не replacement всего pipeline.
