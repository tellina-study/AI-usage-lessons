---
id: s04
section: "0. Entry"
type: analitika
title: "One mechanism, three scales"
assertion: "Three cases, three orders of magnitude of budget, one economic mechanism: the gain everywhere comes from the devaluation of the failed attempt"
source: "ai.google.dev/gemini-api/docs/pricing (read 10/27/2026) · elevenlabs.io/pricing/api (10/27/2026) · Caixin Global, \"How AI took over China's micro-drama industry,\" 06/01/2026"
blocks:
  - {label: "An image", value: "$0.034–0.05", note: "classic mode: $50–150 per illustration, 1–3 days"}
  - {label: "A minute of speech", value: "$0.03–0.072", note: "classic mode: a voice talent, $50–450 per minute"}
  - {label: "An episode of drama", value: "≈$7–14K", note: "classic mode: ordinary production, ≈$137K"}
  - {label: "The gap across all three", value: "×10–20 at the expensive end, ×1000–4500 at the cheap end", note: "the cheaper the unit, the bigger the gap", key: true}
analitika:
  unit: "price of one trial, in dollars"
  scale: "logarithmic — otherwise the extreme bars are incomparable on one frame"
  caption_rule: "the denominator sits in the bar's caption, not in a footnote"
  bars:
    - {label: "Image\n(per one 1024×1024 image)", model: 0.042, classic: 100, classic_label: "$50–150 for a commissioned image"}
    - {label: "Minute of speech\n(per finished minute)", model: 0.05, classic: 250, classic_label: "$50–450 per minute from a voice talent"}
    - {label: "Micro-drama episode\n(per one episode)", model: 10500, classic: 137000, classic_label: "over 1M yuan for a live-action episode"}
media: "assets/charts/s04-tsena-proby.png"
media_note: "a QuickChart bar chart from this frame's plate numbers: three \"classic mode / with a model\" pairs in one unit — the price of one trial in dollars, logarithmic scale (otherwise 0.042 and 137,000 cannot sit on one frame together). The denominator sits in each row's caption"
timing_min: 2.0
in_bucket: false
status: собран
---

## Visible slide text

**There is one unit on this frame: the price of one trial.**

**Three orders of magnitude of budget. One mechanism: paying for a trial stopped.**

## Speaker notes

The three cases on this frame are separated by three orders of magnitude of budget — from four
cents to fourteen thousand dollars. What they share is exactly one thing, and that one thing is
the content of the frame: the gain everywhere comes from the fact that a failed trial stopped
costing money.

There is one unit on the frame — the price of one trial — and each bar's caption carries a
denominator: exactly what is being paid for. This is not a formality. Half the arguments about
the effect of generative models are arguments about the baseline of comparison, and "a thousand
times cheaper" without saying cheaper than what means nothing at all. That is why, next to every
number on the frame, the classic mode sits counted in the same unit.

Image. A 1024×1024 picture costs three and a third cents through Google's programmatic access,
about five cents through Midjourney's base subscription, and roughly the same through Adobe
Firefly. The classic mode in the same unit is a commissioned illustration from a mid-level
freelancer: fifty to a hundred fifty dollars for a job with a one-to-three-day turnaround. The
gap is a thousand to four and a half thousand times. An important honesty: this is not the only
possible baseline. Against a stock agency's retail license, where one image costs a hundred
thirty to four hundred ninety-nine dollars, the gap reaches fourteen thousand seven hundred
times; against a bulk subscription, where the same image costs two dollars fifty cents, it falls
to seventy-three. Choosing the baseline inside the classic mode alone shifts the result by two
orders of magnitude, and all three numbers have to be named, or the choice of baseline makes the
conclusion for the listener.

A minute of speech. Synthesis costs three to seven cents per finished minute. A voice talent
charges, per finished minute, from fifty dollars at the entry level to four hundred fifty at the
high end. The gap is seven hundred to fifteen thousand times. The unit on both sides is
specifically the finished minute, not an hour of studio time: hourly recording-studio rates do
not belong in this ledger, and must not be mixed in.

A micro-drama episode is already a whole product, and the scale matches. A short vertical serial
episode cost, in ordinary Chinese production, over one million yuan, about a hundred thirty-seven
thousand dollars. With a generative pipeline: fifty to a hundred thousand yuan, seven to
fourteen thousand dollars per episode. A drop of ten to twenty times. Over eight months of 2026,
four hundred thirty thousand episodes came out — one every thirty-six seconds.

And here is what is more interesting about these three rows than any one of them on its own. The
gap is not uniform: at the cheapest unit it runs into the thousands, at the most expensive it
runs ten to twenty. This is not accounted for by chance or by measurement error. It is a
regularity, and it will hold for the whole evening. The more expensive the unit of output, the
smaller the share of its price taken up by the very operation the model makes cheaper, and the
more work remains that the model does not do: coordination, rights, finishing, release. For an
image, that remaining work is close to zero, which is why the gap runs into the thousands. For a
serial episode, there is a lot of it, which is why the gap is only ten to twenty. The order of the
evening's sections is built on this same scale: from the cheapest unit to the most expensive, and
along the way it will become visible how the share of work the model does not close keeps
growing.

The chart on the frame is drawn on a logarithmic scale out of necessity: four cents and a hundred
thirty-seven thousand dollars simply do not fit on one linear scale — the smaller bar would
degenerate into a line as thin as a hair. The log scale lets you see the very thing the frame is
built to show: all three pairs sit at a comparable distance from each other, even though the
absolute values differ by millions of times. One mechanism, three scales.

One last thing worth taking away from this frame. Not one of the six numbers here describes
quality. They describe the price of an attempt, and only that. Whether a generated micro-drama
episode is better than a shot one is a question this frame does not touch at all — and that is
honest, because the economics of the attempt and the quality of the result live on different
axes. The rest of the evening is devoted to what happens when the first axis collapses while the
second stays exactly where it was.
