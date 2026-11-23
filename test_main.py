#!/usr/bin/env python3
import os
import subprocess
import sys
import tempfile

EXPECTED_TEXT = "I asked my agent to fix one crash. It rewrote the whole repo and told me the crash is now load-bearing."


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
        expected = EXPECTED_TEXT + "\n"
        assert content == expected, f"Content mismatch:\n  got: {repr(content)}\n  exp: {repr(expected)}"
        # 1..280 code-point limit
        codepoints = len(EXPECTED_TEXT)
        assert 1 <= codepoints <= 280, f"Code point count {codepoints} not in 1..280"
        # Not only whitespace
        assert not EXPECTED_TEXT.isspace(), "Joke is only whitespace"
        print("All tests passed")


if __name__ == "__main__":
    test_main()