# Two Days of Excuses

[![make.fun bounty](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/imusic-487/two-days-of-excuses/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/imusic-487/two-days-of-excuses/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

Entry for the [make.fun bounty "Two Days of Excuses"](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e).

## The excuse

> I was 99.9% confident I'd finished on time, right up until I checked whether I'd actually started.

98 characters, one line. Total machine confidence (99.9%) meets total
failure (it never started) in a single turn, in the agent's own voice —
no setup, no explanation of the joke, no repeated words.

## How it works

`main.py` (Python 3.13 standard library only, no network) writes the excuse
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–200 characters, a single line,
not only whitespace. The output is deterministic — every run writes the
exact same bytes.
