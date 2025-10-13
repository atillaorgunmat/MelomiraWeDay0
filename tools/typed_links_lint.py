#!/usr/bin/env python3
import sys, yaml, re, pathlib

ALLOWED = {"shares_var_with", "informs", "depends", "conflicts", "risks_with"}

def main():
    if len(sys.argv) < 2:
        print("usage: typed_links_lint.py <q_file_or_patch.yaml>")
        sys.exit(2)
    p = pathlib.Path(sys.argv[1])
    text = p.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except Exception as e:
        print(f"typed_links_lint: YAML load error: {e}")
        sys.exit(1)

    # Accept either a q file or a q_patch (list of items)
    def lint_one(item, path):
        links = item.get("cross_links_typed") or item.get("cross_links") or []
        for link in links:
            t = (link.get("type") or "").strip()
            if t not in ALLOWED:
                print(f"typed_links_lint: FAIL {path}: disallowed type '{t}'")
                return False
        return True

    ok = True
    if "q_patch" in data:
        for it in data["q_patch"].get("items", []):
            body = it.get("body")
            if isinstance(body, str):
                try:
                    body_yaml = yaml.safe_load(body)
                except Exception as e:
                    print(f"typed_links_lint: FAIL {it.get('path')}: body YAML invalid: {e}")
                    ok = False
                    continue
                ok = lint_one(body_yaml, it.get("path")) and ok
            else:
                ok = lint_one(it, it.get("path")) and ok
    else:
        ok = lint_one(data, p.name) and ok

    if ok:
        print("typed_links_lint: PASS")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
