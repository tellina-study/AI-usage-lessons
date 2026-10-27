# Backup PNG Tier-4 fallback assets

Этот каталог содержит static PNG-резервы для media embeds в deck. Заполняется в Phase 6 visual loop.

## Структура

Один PNG per slide, имя по slide_id, content per slide spec:

| File | Slide | Content |
|---|---|---|
| `s01-suno-firefly-mockup.png` | s01 | Suno create UI или Firefly playground screenshot |
| `s07-sora2-frame.png` | s07 | Sora 2 release reel sample frame |
| `s08-character-consistency.png` | s08 | Midjourney character grid from official showcase |
| `s09-elevenlabs.png` | s09 | ElevenLabs voice library screenshot |
| `s10-genie3.png` | s10 | Genie 3 demo frame from DeepMind blog |
| `s10a-russian-vs-frontier.png` | s10a | Side-by-side Kandinsky 5.0 Video vs Kling 3.0 |
| `s11-firefly-enterprise.png` | s11 | Adobe Firefly enterprise logos + Lionsgate quote |
| `s14-cost-bars.png` | s14 | Cost-collapse bar chart from QuickChart |
| `s15-speed.png` | s15 | Timer mockup comparison |
| `s16-upwork.png` | s16 | Upwork AI/ML category screenshot |
| `s17-displacement.png` | s17 | Bar chart Upwork displacement + Shutterstock licensing |
| `s21-nyt-bloomberg.png` | s21 | Bloomberg Law headline screenshot |
| `s22-getty-uk-ruling.png` | s22 | Bird & Bird ruling article screenshot |
| `s23-andersen-docket.png` | s23 | US District Court docket screenshot |
| `s24-riaa.png` | s24 | RIAA press release screenshot |
| `s25-thomson-ross.png` | s25 | Reed Smith analysis article screenshot |
| `s26-arup.png` | s26 | CNN article «Finance worker pays out $25 million» |
| `s27-korea-npr.png` | s27 | NPR article headline (text only, NO deepfake visuals) |
| `s28-slop.png` | s28 | Google AI Overview «glue on pizza» + Nature paper header |
| `s29-si-futurism.png` | s29 | Futurism investigative article on SI fake authors |
| `s30-sentiment.png` | s30 | 2 sentiment bar charts side-by-side |
| `s31-displacement-3stats.png` | s31 | 3-stat block consolidated |
| `s35-youtube.png` | s35 | 3-stat block + drop reasons bar chart |

## Fallback strategy (per slide)

Tier 1: live online URL (suno.com, firefly.adobe.com etc.) — primary live demo
Tier 2: clickable hyperlink on static thumbnail (embedded in PPTX)
Tier 3: QR-код в углу слайда для офлайн scan
Tier 4: static PNG в `assets/backup/` для emergency (THIS FOLDER)

Phase 5 v1: placeholders embedded в build_lec08.py (`[ FRAME ]`, `[ news screenshot ]`).
Phase 6 visual loop replaces placeholders with real PNGs from this folder.
