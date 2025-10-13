#!/usr/bin/env python3
import sys, re, pathlib

# Simple check for fenced YAML blocks in a text file.
def main():
    if len(sys.argv) < 2:
        print("usage: form_fencing_lint.py <file.txt>")
        sys.exit(2)
    text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
    if "```yaml" in text and "```" in text.strip().split("```yaml",1)[1]:
        print("form_fencing_lint: PASS")
        sys.exit(0)
    else:
        print("form_fencing_lint: FAIL no fenced YAML block found")
        sys.exit(1)

if __name__ == "__main__":
    main()
