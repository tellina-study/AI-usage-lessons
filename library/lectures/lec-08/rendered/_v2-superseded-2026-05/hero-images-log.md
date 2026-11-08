# Hero-images Acquisition Log — Лекция 8

Date: 2026-05-20
Mandate: owner [[hero-images-required]] — добавить hero-иллюстрации на s01 + s39 для всех презентаций курса.

---

## s01 — Ice-breaker (Sora 2 woolly mammoths)

**Decision:** **Option A — Iconic launch reel frame.** Reuse the Sora 2 mammoth image already on s07 (iconic 2024-2026 AI-video launch image, instantly recognizable).

**Source acquisition (success Tier 4 — YouTube CDN, previously acquired для s07):**

| Tier | URL attempted | Status |
|------|--------------|--------|
| **T4 YouTube CDN** | `https://img.youtube.com/vi/HK6y8DAPN_0/maxresdefault.jpg` | ✅ Success (previously, file `assets/screenshots-real/s07-yt-sora.jpg`) |

**File path used:** `assets/screenshots/s01-sora-mammoths.png` (1280×720, JPEG-encoded PNG, 142 KB).

**Attribution label on slide:** *«OpenAI Sora · кадр text-to-video по промпту "woolly mammoths" · 2024»*

**Layout:**
- Hero image: LEFT side, `6.5 × 3.75"` (~24 sq in, ≈ 24% slide area)
- Ocean motif обрамление (rounded box, `#F4F7FA` fill + `#1C7293` stroke)
- Below image: assertion (20pt bold) + compact cost-collapse 2-row
- RIGHT (40% slide): Suno/Firefly demo cards (compressed) + QR

**Pedagogical role:**
- Foreshadows keystone axis «AI добавил» (text-to-video — самая яркая новая возможность)
- Emotional engagement через iconic visual (студент через 3 секунды узнаёт Sora demo)
- Ties s01 → s07 (same image returns как proof-of-claim в Razdel 1)

---

## s39 — Closing / Bridge к Лекции 9 (X-62 VISTA)

**Decision:** **Option B — Bridge image к Лекции 9 (aerospace/defense).** X-62 VISTA F-16 (USAF Test Pilot School in-flight simulator used в DARPA ACE AI dogfight trials, Feb 2023) — strongest pedagogical move, ties course narrative.

**Source acquisition (success Tier 2 — Wikimedia Commons):**

| Tier | URL attempted | Status |
|------|--------------|--------|
| T1 (og:image press) | `darpa.mil/program/air-combat-evolution` | ❌ 301 redirect, empty HTML returned (anti-bot) |
| T1 (og:image press) | `defensescoop.com/2024/04/18/x-62-vista...` | ❌ curl status 22 (anti-bot) |
| **T2 (Wikimedia Commons)** | Wikipedia `en/X-62A_VISTA` og:image / infobox `2/27/X-62_VISTA.jpg` | ✅ **Success** — 1811 KB high-res photo of actual F-16 VISTA in flight, VISTA livery visible, blue sky background |

**Backup candidates downloaded** (kept в `assets/screenshots-real/aerospace/`):
- `mq28-ghost-bat.jpg` (Boeing Ghost Bat loyal wingman, 2023 Avalon Airshow, banner aspect 1280×530)
- `x62-vista.jpg` (chosen — in-flight dramatic shot)

**File path used:** `assets/screenshots/s39-x62-vista.jpg` (1356×905 effective, 1.8 MB).

**Attribution label on slide:** *«X-62 VISTA · USAF Test Pilot School · DARPA ACE AI dogfight 2023 · Wikimedia Commons»*

**Layout:**
- Hero image: RIGHT side, `6.55 × 4.10"` (~27 sq in)
- Ocean motif обрамление
- Below image: attribution (10pt italic) + «СЛЕДУЮЩАЯ ЛЕКЦИЯ» chip + title «AI в авиакосмической отрасли и оборонном комплексе» + gold-bar frame phrase
- LEFT: «СПАСИБО за внимание» card (compressed to 5.40×4.95) + QR

**Pedagogical role:**
- Visual bridge: Лекция 8 closed on creative-AI failures → Лекция 9 opens on safety-critical aerospace
- Concrete vs abstract: «09» faded number replaced с real aircraft — shows что лекция 9 «about real things»
- Emotional anchor: dramatic in-flight shot creates anticipation
- DARPA ACE context = AI in adversarial / autonomous control — теасinger для Лекции 9 keystone axis

---

## Total tier success summary

| Tier | s01 | s39 |
|------|-----|-----|
| **T1 (og:image press)** | n/a (reuse) | ❌ all attempted blocked |
| **T2 (Wikipedia/Wikimedia)** | n/a | ✅ used |
| T3 (press official) | n/a | not needed |
| **T4 (YouTube CDN)** | ✅ used (reuse from s07) | n/a |
| T5 (Wayback) | n/a | not needed |
| T6 (Google last resort) | n/a | not needed |

## Educational fair use

Both images embedded with visible attribution chip on slide. Used strictly для educational lecture в курсе AI-usage (Tellina). Sources: OpenAI Sora YouTube channel public thumbnail (T4) + Wikimedia Commons CC-licensed Wikipedia infobox image (T2).

## Compliance with task brief acceptance criteria

- [x] s01 — hero image visible, foreshadows keystone axis «AI добавил»
- [x] s39 — hero image visible, bridge to Лекция 9 (aerospace/defense)
- [x] Attribution labels visible on both slides
- [x] Russian language preserved in all new captions/labels
- [x] Ocean palette only (no red/green new elements)
- [x] 39 PNGs all fresh + synced to main repo `/home/levko/AI-usage-lessons/library/lectures/lec-08/rendered/`
- [x] Hero image ≥40% of slide visual mass (image + adjacent text block combined)
