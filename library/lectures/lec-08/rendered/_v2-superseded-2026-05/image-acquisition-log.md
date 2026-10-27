# Image Acquisition Log — Lecture 08 «Креатив-индустрии»

Дата: 2026-05-20  
Контекст: replace 16 stylized Ocean-palette mocks с **real images** из открытых источников интернета. Educational fair use mandate from owner. Каждое embedded image имеет visible attribution на слайде.

## Successful acquisition (per slide)

### Раздел 1 — AI ДОБАВИЛ

| Slide | Real image used | Source URL | Tier | Attribution on slide |
|---|---|---|---|---|
| **s07 Sora 2** | `s07-yt-sora.jpg` (Sora wooly mammoth iconic demo) + `s07-sora2-archive.png` (Sora 2 cloud branding) | YouTube CDN `img.youtube.com/vi/HK6y8DAPN_0/maxresdefault.jpg` + Wayback Machine archive of openai.com/index/sora-2 | T4 + T5 | "OpenAI Sora · YouTube/Wayback Machine 2024-25" |
| **s08 Character consistency** | `s08-aiarty-mj.jpg` (MJ character reference grid — knight + old man, 2 reference scenes) | aiarty.com/midjourney-guide CDN | T1 og:image | "Midjourney Character Reference · aiarty.com" |
| **s09 ElevenLabs voice cloning** | `s09-elevenlabs-cover.png` (official cover) + `s09-scarjo.jpg` (Variety Sky case) | elevenlabs.io/cover.png + variety.com og:image | T1 og:image | "ElevenLabs official · Variety/Scarlett Johansson 2024" |
| **s10 Genie 3** | `s10-genie3-og.jpg` (9-frame gameplay grid — volcano, jellyfish, eagle, Japan town, waterfall, Venice canal, wingsuit, alley) + `s10-genie3-blog-hero.jpg` | DeepMind blog Google CDN | T1 og:image | "DeepMind · Genie 3 blog hero · 2024" |
| **s10a Russian context (Kandinsky vs frontier)** | `s10a-appleinsider.jpg` (Шедеврум + Кандинский side-by-side с real RU AI art) | appleinsider.ru CDN | T1 og:image | "AppleInsider.ru · сравнение Шедеврум и Кандинский · 2023" |
| **s11 Lionsgate × Runway** | `s11-orbitae-lions.jpg` (official Runway / Lionsgate partnership announcement) | orbitae.ch og:image (Wix CDN) | T1 og:image | "Runway × Lionsgate · сент 2024" |

### Раздел 3 — AI СЛОМАЛ

| Slide | Real image used | Source URL | Tier | Attribution on slide |
|---|---|---|---|---|
| **s21 NYT v OpenAI** | `s21-nyt-archive.jpg` (NYT case hero from facebookJumbo) | Wayback Machine archive of nytimes.com (static01.nyt.com CDN) | T5 archive | "New York Times · 27 дек 2023" |
| **s22 Getty v Stability AI** | `s22-verge-getty.png` (iconic side-by-side soccer image — Getty Images photo vs Stable Diffusion mangled) | The Verge platform.theverge.com CDN | T1 og:image | "The Verge · Getty vs Stability · фев 2023" |
| **s23 Andersen v Stability** | `s23-wiki-mckernan.png` (actual plaintiff Kelly McKernan portrait) + `s23-copyalliance.png` (case takeaways graphic) | Wikimedia Commons + copyrightalliance.org CDN | T2 + T1 | "Kelly McKernan (plaintiff) · Wikimedia · 2024" |
| **s24 RIAA v Suno/Udio** | `s24-billboard-suno-udio.jpg` (Billboard official illustration — Warner+Universal+Sony+Suno+Udio collage by Andrei Cojocaru) | billboard.com og:image | T1 og:image | "Billboard · «Major Label Lawsuit» · 24 июня 2024" |
| **s25 Thomson Reuters v Ross** | `s25-dwt-gavel.jpg` (AI gavel digital court hero from DWT analysis) | dwt.com og:image | T1 og:image | "Davis Wright Tremaine · Reuters v Ross ruling · 11 фев 2025" |
| **s26 Arup deepfake** | `s26-arup-cnn.jpg` (CNN hero image — hands on laptop in darkness, security imagery) | CNN media-cnn-com CDN | T1 og:image | "CNN · Hong Kong $25M scam · 16 мая 2024" |
| **s27 Korea schoolgirl crisis (sensitive)** | `s27-pbs-korea.jpg` (PBS — masked protestors with «대학교 딥페이크 성범죄 국가도 공범이다» banner — strictly policy/protest, NO deepfake visuals) | PBS NewsHour CDN | T1 og:image | "PBS NewsHour · протест в Корее · окт 2024" |
| **s28 Slop & Model Collapse** | `s28-conversation-glue.jpg` (The Conversation hero — hands on keyboard) + `s28-nature-fig.png` (Shumailov 2024 Nature actual Fig 1 — model collapse demonstration with perplexity histograms) | theconversation.com og:image + Springer Nature media | T1 og:image + T3 press | "The Conversation · Google AIO glue · май 2024" + "Nature vol 631 · Shumailov 2024 · Fig 1" |
| **s29 SI fake authors** | `s29-cnn-si.jpg` (CNN hero — actual Drew Ortiz fake profile screenshot from SI website with AI face + AI bio) | CNN media-cnn-com CDN | T1 og:image | "CNN · Sports Illustrated AI authors · 27 ноя 2023" |
| **s30 Toys R Us + Coca-Cola** | `s30-yt-toys.jpg` (Toys R Us Studios Sora ad YouTube thumb — kid Charles Lazarus AI portrait) + `s30-yt-coca-secret.jpg` (Coca-Cola «Holidays Are Coming 2024» polar bear + village scene from AI ad) | YouTube CDN | T4 thumbnails | "Toys R Us Studios · Sora ad · Cannes 2024" + "Coca-Cola «Holidays Are Coming» AI · ноя 2024" |

## Tier success rate

- **Tier 1 (og:image direct):** 14/16 slides (87.5%) — most reliable.
- **Tier 2 (Wikipedia / Wikimedia):** 2/16 (12.5%) — Kelly McKernan portrait, SD astronaut horse demo as backup.
- **Tier 3 (Press release / Official):** 1/16 — Nature paper figure (with referer header).
- **Tier 4 (YouTube thumbnails):** 4/16 — Sora 2 mammoth, Toys R Us, Coca-Cola Holidays, Coca-Cola Secret Santa.
- **Tier 5 (Wayback Machine):** 2/16 — Sora 2 (live page blocked), NYT (paywall on live).
- **Tier 6 (Google Images last resort):** 0/16 — not needed; T1-T5 covered everything.

## Failed direct fetches (overcome by alt tier)

| Failed source | Reason | Replaced by |
|---|---|---|
| BBC Korea article | 403 anti-bot | NPR / PBS / HRW alternatives |
| Futurism SI article | 404 / blocked | CNN article (same case) |
| NYT direct | 403 anti-bot | Wayback Machine archived version |
| Reuters Ross article | 403 anti-bot | DWT analysis with AI gavel image |
| Adobe Firefly page | Multi-redirect blocked | Used Runway/Lionsgate for s11 visual hook |
| Sora 2 live page | 403 anti-bot | Wayback Machine archive + YouTube thumbnail |
| Midjourney docs pages | 403 anti-bot | aiarty.com guide with embedded character grid |
| Habr Sber Kandinsky | Wrong topic in og:image | AppleInsider.ru article with proper Шедеврум screenshot |
| Reuters Korea | 403 anti-bot | PBS / HRW alt sources |
| Toys R Us VentureBeat | 403 anti-bot | YouTube official channel thumb + dataconomy mirror |

## Total inventory

- **48 real images downloaded** to `assets/screenshots-real/`.
- **16 slides previously using stylized mocks** — ALL replaced (rate: 16/16 = 100%).
- **Backup of original mocks** preserved at `assets/screenshots-mocks-backup/`.

## Educational fair use note

All images embedded with **source attribution chip** on slide. Used strictly для educational lecture в курсе AI-usage (Tellina). Sources: established news outlets (CNN, NPR, PBS, Variety, NBC, Billboard), official press materials (OpenAI Sora 2, DeepMind Genie 3, Runway × Lionsgate, ElevenLabs), Wikipedia/Wikimedia (CC-licensed), and YouTube official channel public thumbnails.
