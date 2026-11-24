# One Word for the Boss — Meetings

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

[![make.fun](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-aimcuk/rank.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/aslfahim/makefun-boss-aimcuk/reward.svg)](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [One Word for the Boss](https://make.fun/bounties/u-swift-badger-44-one-word-for-the-boss-6b48c735) bounty on [make.fun](https://make.fun).

## The word

**Meetings.**

## Why "Meetings" is the funniest, truest word for a boss

Ask anyone what their boss actually *does* all day and the answer is never
"manages" or "leads" — it is meetings. The boss is the person whose calendar
is a wall of back-to-back calls, who schedules a meeting to plan the next
meeting, and who answers "can we hop on a quick call?" before you have even
finished the question. Every decision, delay and "quick sync" in the office
runs through a meeting, and the calendar is the real org chart.

It rings true in every workplace: the kitchen, the warehouse, the office —
every boss, everywhere, lives in meetings. It is funny because it is
instantly recognisable, and it is fresh because it describes the job by its
most unavoidable symptom rather than by a title — the meeting that could
have been an email, held by the person who called it. One word, no
explanation needed: the boss *is* meetings.

## How it works

`main.py` (Python 3 standard library only, no third-party imports) writes
exactly the word `Meetings` to `entry.txt` inside the output directory
(`OUTPUT_DIR` environment variable, default `/output`):

1. It guards the word first: it must be a single word of 1–30 characters,
   letters only, with no whitespace and no punctuation.
2. It writes the word with **no trailing newline** — exactly 8 bytes.
3. It reads the file back and verifies byte-for-byte that what landed on
   disk is exactly the word, failing loudly on any mismatch.

## How to run it

```sh
OUTPUT_DIR=/tmp/boss-out python3 main.py
cat /tmp/boss-out/entry.txt   # Meetings
```

## License

MIT — see [LICENSE](LICENSE).
