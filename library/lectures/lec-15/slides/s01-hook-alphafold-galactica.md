---
id: s01
type: hero_cover
duration_min: 3
assertion: "AlphaFold взял Нобель 2024. Galactica прожила три дня. Это одна эпоха — и одна задача инженера: различить."
learning_goal: "Эмоциональный hook + предъявить две стороны AI-в-науке без выбора стороны"
learning_outcomes: [LO5, LO6]
chapter_ref: "§0.2 — 9 октября 2024 и 15-17 ноября 2022"
failure_bucket: mixed
references: [nobel-chemistry-2024, heaven-2022-galactica-mit-tr, jumper-2021-alphafold-nature]
visual:
  pattern: hero_composite_split
  primary: "Composite ≥40% площади: левая половина — Hassabis + Jumper + Baker на Нобелевской церемонии (Стокгольм, декабрь 2024); правая — скриншот заголовка MIT Technology Review «Why Meta's Galactica only survived three days online» (Heaven, 18 ноября 2022). Между ними — единая bridging caption ⇄ посередине; одинаковая color grade; единый stroke border 4px Ocean palette `#1C7293`."
  acquisition_tiers:
    - "Tier 1: og:image nobelprize.org/prizes/chemistry/2024 (Nobel ceremony photo)"
    - "Tier 2: Wikipedia Commons — File:Nobel_Prize_Chemistry_2024_laureates.jpg (CC-BY-SA)"
    - "Tier 3: DeepMind blog post AlphaFold Nobel coverage октябрь 2024"
    - "Tier 6: fair-use screenshot MIT Technology Review headline (educational excerpt)"
  fallback: "Если composite слабый — switch к single hero AlphaFold ribbon (DeepMind press image), Galactica callback inline на s02"
---

# AlphaFold взял Нобель. Galactica прожила три дня. Различать — задача инженера.

## Visual

Hero ≥40% площади экрана. Composite side-by-side, единая композиция, не два отдельных image-placeholder.

**Левая половина:** Дэвид Бейкер, Демис Хассабис и Джон Джампер на Нобелевской церемонии — Шведская королевская академия наук, 10 декабря 2024. AlphaFold — первая в истории Нобелевская премия по фундаментальной науке, в формулировке которой стоит конкретный AI-продукт.

**Правая половина:** скриншот заголовка MIT Technology Review от 18 ноября 2022 — «Why Meta's Galactica only survived three days online». Galactica — большая языковая модель Meta, обученная на 48 миллионах научных статей. Запущена 15 ноября 2022, отозвана 17 ноября 2022 — модель прожила публично три дня после фактических ошибок и галлюцинированных цитат.

**Между половинами:** одна bridging caption по центру — «AlphaFold ⇄ Galactica». Единый stroke border 4px Ocean palette `#1C7293`. Single composite image at export — не split-screen с риском misalignment.

**Caption attribution внизу:** «Nobel Prize Chemistry 2024 © Nobel Foundation | Galactica retraction headline © MIT Technology Review 2022 (fair-use educational excerpt)».

## Key claim

Эти два события — не противоречие. Они одновременны в более широком смысле: AlphaFold показал, что AI в науке способен на структурный прорыв нобелевского уровня; Galactica показала, что та же базовая технология, применённая без понимания границ, генерирует фабрику статей и убивает доверие к научной литературе.

## Speaker notes

9 октября 2024 года Шведская королевская академия наук объявила лауреатов Нобелевской премии по химии. Половина премии досталась Дэвиду Бейкеру из Вашингтонского университета за вычислительное проектирование белков. Вторая половина разделена между Демисом Хассабисом и Джоном Джампером из DeepMind — за AlphaFold, систему предсказания трёхмерной структуры белков по аминокислотной последовательности. Это первая в истории Нобелевская премия по фундаментальной науке, в формулировке которой стоит конкретный AI-продукт. AlphaFold вошёл в категорию инструмент, без которого современная биология больше не работает, за десять лет существования.

15 ноября 2022 года, за два года до этого Нобеля, Meta запустила Galactica — большую языковую модель, обученную на 48 миллионах научных статей, учебников и справочных материалов, с прямым обещанием помочь учёным в написании и обзоре литературы. Демонстрация в открытом доступе прожила три дня — модель была отозвана 17 ноября 2022 года. За эти три дня пользователи Twitter и Hacker News собрали коллекцию фактических ошибок: Galactica уверенно генерировала научные обзоры про несуществующие исследования, цитировала статьи, которых никогда не было. Заголовок MIT Technology Review от 18 ноября — «Why Meta's Galactica only survived three days online» — стал эталонным предостережением.

Эти два события не противоречат друг другу. AlphaFold показал, что AI в науке способен на структурный прорыв нобелевского уровня. Galactica показала, что та же базовая технология, применённая без понимания границ, генерирует фабрику статей и убивает доверие к научной литературе. Главная задача лекции — научить читателя различать ситуации AlphaFold от ситуаций Galactica.
