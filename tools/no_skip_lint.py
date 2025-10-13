#!/usr/bin/env python3
import sys, yaml, pathlib

def main():
    if len(sys.argv) < 2:
        print("usage: no_skip_lint.py <q_patch.yaml>")
        sys.exit(2)
    data = yaml.safe_load(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")) or {}
    ok = True
    items = (data.get("q_patch") or {}).get("items", [])
    for it in items:
        body = it.get("body")
        if isinstance(body, str):
            body = yaml.safe_load(body)
        tier = (body or {}).get("tier")
        deps = (body or {}).get("depends_on", [])
        if tier == "HOW" and not deps:
            print(f"no_skip_lint: FAIL {it.get('path')}: HOW missing WHAT parent")
            ok = False
    if ok:
        print("no_skip_lint: PASS")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
