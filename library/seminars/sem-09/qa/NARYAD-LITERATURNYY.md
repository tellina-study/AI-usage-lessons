# Наряд на литературный проход — Семинар 9, формат сопоставления

Замер оркестратора 2026-10-29, шаблоны `tools/seminar-build/sopostavlenie_figury.py`.

Шаблоны проверены на своих пробах: ловят «не просто читает, а сверяет», «дело не в формате»,
«с одной стороны»; НЕ срабатывают на «сумма не прочитана», «модель не видит текст заявки».

## Три слоя и их счёт

| Слой | Находок | Чинить? |
|---|---|---|
| тело кадра (от `# заголовка` до `## Speaker notes`) | **42** | да |
| заметки (после `## Speaker notes`) | **134** | да — заметки у нас публикуемый текст |
| генераторы схем `rendered/make_figures_*.py` | **60** | только подписи на полотне |
| шапка `---…---` (`visual.backup`, `learning_goal`) | 332 | **НЕТ** — производственный протокол, залу не показывается |

Кейсы 5, 6 и вводная уже на нуле в теле и заметках — их не трогать.

## Пофайлово — тело и заметки

| Файл | тело | заметки |
|---|---|---|
| `n06-k1-stsena.md` | 2 | 5 |
| `n07-k1-vopros.md` | 0 | 7 |
| `n08-k1-razbor.md` | 0 | 3 |
| `n09-k1-reshenie-sloy1.md` | 1 | 4 |
| `n10-k1-n8n-versiya1.md` | 0 | 2 |
| `n11-k1-nastroyka-promta.md` | 0 | 2 |
| `n11a-k1-struktura-testa.md` | 1 | 1 |
| `n12-k1-rezultat-legkiy.md` | 1 | 1 |
| `n13-k1-rezultat-trudnyi.md` | 0 | 3 |
| `n13a-k1-reshenie-uverennost-porog.md` | 0 | 3 |
| `n14-k1-n8n-versiya2.md` | 0 | 1 |
| `n16-k1-rezultat-geyt.md` | 1 | 1 |
| `n17-k1-obobshchenie-granitsa.md` | 1 | 3 |
| `n18-k2-divider.md` | 0 | 1 |
| `n19-k2-stsena.md` | 1 | 1 |
| `n20-k2-vopros.md` | 0 | 2 |
| `n21-k2-razbor.md` | 3 | 5 |
| `n22-k2-reshenie-sloy1.md` | 1 | 1 |
| `n23-k2-n8n-promt.md` | 1 | 1 |
| `n25-k2-kesh-struktura-zamera.md` | 0 | 5 |
| `n25a-k2-kesh-svod.md` | 1 | 5 |
| `n25b-k2-kesh-tochka-validatsii.md` | 1 | 4 |
| `n26a-k2-pyat-napravleniy-zamer.md` | 0 | 6 |
| `n26b-k2-pyat-napravleniy-razbor.md` | 4 | 6 |
| `n27-k2-obobshchenie.md` | 0 | 4 |
| `n28-k2-granitsa.md` | 1 | 0 |
| `n30-k3-stsena.md` | 0 | 2 |
| `n32-k3-razbor.md` | 3 | 2 |
| `n34-k3-n8n-tsikl.md` | 0 | 1 |
| `n35-k3-nastroyka-proveryayushchego.md` | 0 | 1 |
| `n35a-k3-nastroyka-sudi.md` | 0 | 3 |
| `n37-k3-eksperiment-rezultat.md` | 3 | 4 |
| `n38-k3-sudya-ne-soglasen-s-soboy.md` | 0 | 4 |
| `n40-k3-tsena-sudi.md` | 0 | 5 |
| `n40a-k3-kombinatsiya-i-tsikl.md` | 0 | 3 |
| `n41-k3-obobshchenie.md` | 0 | 2 |
| `n42-k3-nyuansy-granitsa.md` | 1 | 5 |
| `n44-k4-postanovka.md` | 1 | 0 |
| `n45-k4-vopros.md` | 0 | 3 |
| `n46-k4-razbor-zashchit.md` | 2 | 1 |
| `n47-k4-model-nastroyki.md` | 1 | 1 |
| `n48a-k4-vosem-konfiguratsiy.md` | 2 | 2 |
| `n49a-k4-razbor-klassy.md` | 2 | 1 |
| `n50-k4-chem-ostanovlena-ataka.md` | 1 | 1 |
| `n51-k4-glavnaya-nahodka.md` | 1 | 3 |
| `n51a-k4-opornaya-liniya-kod.md` | 1 | 3 |
| `n52-k4-chto-srabotalo.md` | 2 | 4 |
| `n53-k4-povtoryaemost-filtra.md` | 0 | 1 |
| `n54-k4-obobshchenie-granitsa.md` | 2 | 5 |

## Генераторы схем — только текст подписей

| Файл | Находок |
|---|---|
| `make_figures_all.py` | 1 |
| `make_figures_common.py` | 16 |
| `make_figures_k1.py` | 6 |
| `make_figures_k2.py` | 8 |
| `make_figures_k3.py` | 8 |
| `make_figures_k4.py` | 2 |
| `make_figures_k5.py` | 3 |
| `make_figures_k6.py` | 12 |
| `make_figures_lestnitsa.py` | 4 |

В `make_figures_common.py` часть попаданий — это САМИ ШАБЛОНЫ запрета
(`_BAN_PHRASES` импортирует `FIGURY`) и строки документации. Их править НЕЛЬЗЯ:
это сторож, а не содержание. Править только строки, которые рисуются на полотне.
