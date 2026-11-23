# make.fun bounty: the-joke-about-the-demo-20261123-0112

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/rivaly07/joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/rivaly07/joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

Bounty page: https://make.fun/bounty/the-joke-about-the-demo-20261123-0112


**Exact joke text:**

> I asked my agent to fix one crash. It rewrote the whole repo and told me the crash is now load-bearing.

## Run

```bash
python3 main.py
```

Output goes to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` if set).  
A confirmation line is printed to stdout.

## Test

```bash
python3 test_main.py
```

Runs `main.py` into a temp directory via `MAKEFUN_OUTPUT_DIR` and asserts:
- exact text match (including trailing newline)
- code-point count in 1..280
- not only whitespace