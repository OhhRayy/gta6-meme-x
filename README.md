# gta6-meme-x-01 — "The Getaway Driver"

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/OhhRayy/gta6-meme-x/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/OhhRayy/gta6-meme-x/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Entry for the make.fun bounty **"Post a GTA 6 meme on X"** ($500 total, top 50 share it, 1st place $100).
Bounty page: https://make.fun/bounty/gta6-meme-x-01
Deadline: Monday 23 Nov 2026, 21:00 WIB (14:00 UTC).

## The meme

Lucia & Jason finally out in Vice City — and after 13 years of waiting, the getaway
driver is a ghost: make.fun's mascot, white ghost with sparkle eyes, holding its
magenta star coin, at the wheel of a pink convertible at sunset in Leonida.

- Top caption: **"13 YEARS. TWO DELAYS. ONE GETAWAY."**
- Bottom caption: **"THE DRIVER'S A GHOST"**

Why this angle: it is GTA 6-specific (the 13-year wait since GTA V, the delays,
Leon & Lucia, Vice City/Leonida Florida energy) — not a generic gaming joke with
"GTA 6" pasted on — and make.fun's ghost is a character *in* the scene (the driver),
not a sticker in a corner. That is the judge's criterion #1, decided before anything
else: a picture with the ghost beats any picture without one. The picture is
AI-generated original art, captioned with PIL for crisp, correctly spelled text
that stays readable when the judge shrinks it to 480x480.

The final image is `meme-final.png` (1600x1600 PNG). The base art and the caption
script live in `assets/` (`add_captions.py` reproduces the final image from the base).

## The post (X)

The post is the entry: the house reads it from X, an AI judge compares posts two
at a time, places go by win rate. Post from the public X account, attach
`meme-final.png` as the FIRST (and only) picture, and paste the exact text from
`POSTING.md` — it carries the make.fun link, `@makefunai`, and the play code
`makefun-poncho-tiger-beacon`.

## How the entry works

`POST.json` at the root holds the post's address:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

`main.ts` (Node 22, standard library only) copies `POST.json` to `/output/POST.json`.
Nothing the program writes is judged — the house reads the post itself from X.

Run it locally:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`POST.json` now holds the real post URL (posted on X by Fahmi, 20 Nov 2026).

## Status

- [x] Meme made (`meme-final.png`)
- [x] Post text drafted (`POSTING.md`)
- [x] Posted on X by Fahmi (from his phone — the agent cannot post to X from here)
- [x] `POST.json` updated with the real post URL
- [ ] Submitted via the kit CLI (parent/coordinator step, after the post is live)
