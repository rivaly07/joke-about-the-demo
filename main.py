#!/usr/bin/env python3
import os
import sys

from joke import joke_text


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(joke_text() + "\n")
    print(f"Wrote joke to {output_path}")


if __name__ == "__main__":
    main()