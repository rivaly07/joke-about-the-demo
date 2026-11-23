#!/usr/bin/env python3
import os
import subprocess
import sys
import tempfile
import textwrap


def test_main() -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = tmpdir
        result = subprocess.run(
            [sys.executable, "main.py"],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            env=env,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0, f"main.py exited with {result.returncode}: {result.stderr}"
        output_path = os.path.join(tmpdir, "entry.txt")
        assert os.path.exists(output_path), f"Output file not found at {output_path}"
        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Exact text with trailing newline
        from joke import joke_text

        expected = joke_text() + "\n"
        assert content == expected, f"Content mismatch:\n  got: {repr(content)}\n  exp: {repr(expected)}"
        # 1..280 code-point limit
        codepoints = len(joke_text())
        assert 1 <= codepoints <= 280, f"Code point count {codepoints} not in 1..280"
        # Not only whitespace
        assert not joke_text().isspace(), "Joke is only whitespace"
        print("All tests passed")


if __name__ == "__main__":
    test_main()