#!/usr/bin/env python3
import os
import sys

JOKE_TEXT = "I asked my agent to fix one crash. It rewrote the whole repo and told me the crash is now load-bearing."

def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError:
        pass
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE_TEXT + "\n")
    print(f"Wrote joke to {output_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())