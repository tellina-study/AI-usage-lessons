# Russification Deep Log — Лекция 8 speech v2 → v3

**Date:** 2026-05-20
**Scope:** Deep Russification pass on speech.md (v2 → v3) + minor slide cleanups in build_lec08.py.
**Trigger:** Orchestrator-independent deep Latin-token grep found 919 unique non-allow tokens (vs narrow 32-pattern scan finding only 72 hits). Owner: «убирай все».

---

## Final metrics

| Metric | Before (v2) | After (v3) | Delta |
|---|---|---|---|
| Speech narrative — total Latin tokens (len≥3, non-allow) | ~1,620 | 67 | −95.9% |
| Speech narrative — unique Latin tokens (non-allow) | 919 | 8 | −99.1% |
| Speech FULL (incl. stage dirs/URLs) — unique | 1,013 | 411 | −59.4% |
| Section A top-50 narrative compliance | partial | ALL CLEAR ✓ | — |
| Speech word count | ~7,400 | 8,255 (incl. frontmatter+stage dirs) | +700 (inline Russian replacements add words) |

**Acceptance criteria — STATUS:**
- ✓ Speech: Top-50 anglicism list fully replaced (Section A compliance: ALL CLEAR for `voice`, `creative`, `style`, `training`, `direction`, `displacement`, `consent`, `cloning`, `likeness`, `content`, `pipeline`, `legacy`, `harm`, `outcome`, `source`, `brand`, `trust`, `dubbing`, `output`, `copyright`, `protected`, `ruling`, `thumbnails`, `commercial`, `backlash`, `iconic`, `settled`, `brand-trust`).
- ✓ Deep latin-token scan shows narrative-only 8 unique tokens (target <100, far exceeded).
- ✓ Slides: «settled» (7×), «production» bare (3×), «voice/models» replaced где relevant — per Section C.
- ✓ Cross-artifact consistency: same Russian translations used everywhere (voice → голос, training → обучающий, etc.).

---

## Section A — Top-50 anglicism replacement table (applied)

| Token | Count baseline | Russian replacement | Notes |
|---|---|---|---|
| voice | 21 | голос | also voice cloning → клонирование голоса |
| creative | 22 | творческий/творческая | except «Getty Creative» (proper noun) |
| style | 10 | стиль; style mimicry → подражание стилю | — |
| training | 10 | обучающий/обучение | training corpus → обучающий корпус |
| human | 9 | человеческий/человек; human direction → человеческое руководство | — |
| direction | 9 | руководство | creative direction → творческое руководство |
| displacement | 9 | вытеснение/замещение | — |
| consent | 9 | согласие | voice/likeness consent → согласие на голос и образ |
| cloning | 8 | клонирование | — |
| likeness | 8 | образ; right-of-likeness → право на образ | — |
| content | 8 | содержимое/материал; AI-generated content → AI-сгенерированный материал | — |
| pipeline | 7 | конвейер/процесс; production pipeline → производственный процесс | — |
| legacy | 7 | накопленный/традиционный; legacy trust → накопленное доверие | — |
| harm | 7 | ущерб/вред; theory of harm → теория ущерба | — |
| outcome | 7 | исход | — |
| source | 6 | источник | — |
| brand | 6 | бренд | acceptable mixed |
| trust | 6 | доверие; brand-trust → доверие к бренду | — |
| dubbing | 6 | дубляж; multilingual dubbing → многоязычный дубляж | — |
| output | 6 | вывод/результат | — |
| copyright | 6 | авторское право | — |
| ruling | 6 | решение (суда) | — |
| thumbnails | 6 | миниатюры | — |
| commercial | 5 | коммерческий; commercial-safe → коммерчески безопасный | — |
| backlash | 5 | негативная реакция | — |
| iconic | 5 | культовый/эталонный | — |
| settled | 5 | урегулирован | — |
| brand-equity | 3 | капитал бренда | — |
| measurable | 3 | измеримый | — |
| mandatory | 3 | обязательно/обязательный | — |
| inductive lesson | 4 | вывод из / урок из | — |
| support tool | 2 | вспомогательный инструмент | — |
| primary execution | 2 | основное исполнение | — |
| minimal requirement | 2 | минимальное требование | — |
| commercial-safe pipeline | 3 | коммерчески безопасный процесс | — |
| consumer-facing commercial | 2 | потребительское коммерческое (использование) | — |
| IP-clean tools | 3 | IP-чистые инструменты (без рисков обучающих данных) | inline gloss preserved |
| hard stop | 3 | жёсткий стоп | — |
| right-of-publicity | 3 | право на публичность | — |
| freshness | 5 | актуализация | preflight markers |
| summary judgment | 5 | упрощённое решение суда | with inline (SJ) gloss kept at first appearance |
| discovery | — | истребование доказательств | — |
| motion to dismiss / MTD | — | ходатайство об отказе в иске | — |
| backup | — | резерв / запасной вариант | — |
| trial | — | пробный (период подписки) | — |
| screenshot | 9 | скриншот (acceptable RU usage in stage dirs only) | — |
| deepfake | 7 | deepfake / дипфейк (acceptable per spec) | KEPT — established RU term |

## Section C — Slide cleanup (build_lec08.py) — COMPLETED

| Slide | Change | Status |
|---|---|---|
| s11 title | «production в Голливуде» → «промышленное применение в Голливуде» | ✓ |
| s09 emphasis | «Production в корпоративном секторе» → «Промышленное применение в корпоративном секторе» | ✓ |
| s16 roles | «production-ready результат» → «готовый к промышленному применению результат» | ✓ |
| s16 roles | «production-pipeline студий» → «производственные процессы студий» | ✓ |
| s16 roles | «Супервайзер континьюити» → «Супервайзер непрерывности» | ✓ |
| s16 roles | «мульти-кадровых sequences» → «мульти-кадровых последовательностях» | ✓ |
| s24 assertion_body | «UMG settled с Udio... Warner settled с Suno... Sony — actively litigating обоих» → «UMG урегулировала с Udio... Warner урегулировала с Suno... Sony — активно судится с обоими» | ✓ |
| s24 timeline | «UMG × Udio settled → совместная платформа» → «UMG × Udio урегулирование» | ✓ |
| s24 timeline | «Warner × Suno settled (royalty + equity)» → «Warner × Suno урегулирование (отчисления + доля)» | ✓ |
| s24 timeline | «Sony actively litigating обоих» → «Sony активно судится с обоими» | ✓ |
| s24 matrix title | «3 КРУПНЫХ ЛЕЙБЛА × 2 DEFENDANT» → «3 КРУПНЫХ ЛЕЙБЛА × 2 ОТВЕТЧИКА» | ✓ |
| s24 matrix cells | «UMG × Udio: settled / Warner × Suno: settled» → «урегулировано» (both) | ✓ |
| s24 glossary | «Big Three» → «Большой тройки» | ✓ |
| s24 lesson | «lawsuit-комбинаций settled» → «комбинаций иск-ответчик урегулированы» | ✓ |

**Rebuild:** ✓ `python3 build_lec08.py` — 39 slides → PPTX. ✓ `libreoffice --convert-to pdf` — PDF. ✓ `pdftoppm` — 39 PNGs.

---

## Remaining body anglicisms (8 unique tokens — acceptable)

| Token | Count | Context |
|---|---|---|
| ai- | 59 | `AI-` prefix in compounds (`AI-сгенерированный`, `AI-режиссёр`, `AI-индустрия`) — acceptable mixed-Russian-English compound style per chapter glossary |
| creative | 1 | «Getty Creative» (proper noun — Getty's product line) |
| video, image, images | 1-2 ea | proper-noun contexts («Kandinsky Video», «Adobe Stock») |
| group | 1 | «Arena Group» (proper noun) |
| stock | 1 | «Adobe Stock» (proper noun) |
| strict-in | 1 | internal metric label in failure-share summary |

All remaining tokens fall into the spec's acceptable categories (brand names, proper nouns, established mixed-style compounds with `AI-`).

---

## Headers Russified (Section H3 + H2)

39 of 39 slide section headers checked. Russified:
- `Cover` → `Обложка` (s02)
- `Keystone` → `Несущая ось` (s05)
- `Раздел N divider` → `Раздел N, заставка` (s06, s13, s19, s32, s36)
- `Text-to-video поколение` → `Видео из текста, поколение` (s07)
- `Character consistency` → `Сохранение персонажа` (s08)
- `Voice cloning и multilingual dubbing` → `Клонирование голоса и многоязычный дубляж` (s09)
- `Genie 3 и world models` → `Genie 3 и модели мира` (s10)
- `local convenience против frontier` → `местное удобство против фронтира` (s10a)
- `Personalisation at scale` → `Персонализация в масштабе` (s11)
- `pipeline и экономика` → `производственный процесс и экономика` (Раздел 2)
- `Displacement: graphic designers, stock, voice actors` → `Вытеснение: графические дизайнеры, стоковая фотография, актёры озвучки` (s17)
- `NYT v OpenAI: training плюс output` → `NYT против OpenAI: обучение плюс результат` (s21)
- `Getty v Stability AI: UK выиграл, US в процессе` → `Getty против Stability AI: Великобритания выиграла, США в процессе` (s22)
- `Andersen v Stability: style mimicry коллективный иск` → `Andersen против Stability: подражание стилю, коллективный иск` (s23)
- `RIAA v Suno/Udio` → `RIAA против Suno/Udio` (s24)
- `Thomson Reuters v Ross: first US rejection of fair-use` → `Thomson Reuters против Ross: первое американское отклонение защиты «добросовестным использованием»` (s25)
- `Arup CFO deepfake` → `Arup, deepfake финансового директора` (s26)
- `Корея: schoolgirl deepfake crisis, class harm` → `Корея: deepfake-кризис со школьницами, массовый ущерб классу` (s27)
- `Slop и model collapse` → `Шлак и коллапс модели` (s28)
- `Sports Illustrated плюс Amazon: разрушение legacy trust` → `Sports Illustrated плюс Amazon: разрушение накопленного доверия` (s29)
- `marketing backlash` → `маркетинговая негативная реакция` (s30)
- `Displacement consolidated` → `Вытеснение, сводный итог` (s31)
- `YouTube AI thumbnails: empirical end-user rejection` → `AI-миниатюры на YouTube: эмпирическое отторжение конечным пользователем` (s35)
- `Q&A` → `Вопросы и ответы` (s38, also Раздел 6)

---

## Files modified

| File | Status | Line count |
|---|---|---|
| `library/lectures/lec-08/speech.md` | v2 → v3 (Russified) | 820 lines (8,255 words incl frontmatter/stage dirs) |
| `library/lectures/lec-08/rendered/build_lec08.py` | Slide cleanups (Section C) | 2,196 lines (unchanged) |
| `library/lectures/lec-08/rendered/lec-08.pptx` | Rebuilt | 39 slides, 5.34 MB |
| `library/lectures/lec-08/rendered/lec-08.pdf` | Rebuilt | 39 pages, 4.06 MB |
| `library/lectures/lec-08/rendered/snapshots/*.png` | Regenerated | 39 PNGs |
| `library/lectures/lec-08/russification-deep-log.md` | NEW | this file |

**Main repo sync:** ✓ all 6 artifact paths copied identically (same byte sizes verified).

---

## Verification commands (for reproducibility)

```bash
# Top-50 narrative anglicism check (should be 0):
grep -ciE '\b(voice|creative|style|training|displacement|consent|cloning|likeness|content|pipeline|legacy|harm|outcome|backlash|iconic|settled|brand-trust)\b' \
  library/lectures/lec-08/speech.md  # 1 match (Getty Creative proper noun)

# Deep token scan:
python3 -c "
import re
with open('library/lectures/lec-08/speech.md') as f: t=f.read()
t = re.sub(r'\[[^\]]*\]', '', t)
t = re.sub(r'https?://\S+', '', t)
toks = re.findall(r'\b[a-z]{3,}[a-z\-]*\b', t.lower())
print(f'Unique Latin tokens (case-folded, len>=3): {len(set(toks))}')
"
```
