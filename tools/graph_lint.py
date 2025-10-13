#!/usr/bin/env python3
import sys, yaml, pathlib

def main():
    path = pathlib.Path("graph/questions.yaml")
    if not path.exists():
        print("graph_lint: FAIL graph/questions.yaml missing")
        sys.exit(1)
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    nodes = {n["id"]: n for n in data.get("nodes", []) if "id" in n}
    edges = data.get("edges", [])
    # basic checks
    ids = set(nodes.keys())
    ok = True
    for e in edges:
        a = e.get("from") or e.get("parent") or e.get("a")
        b = e.get("to") or e.get("child") or e.get("b")
        if a and a not in ids:
            print(f"graph_lint: FAIL unknown node '{a}'")
            ok = False
        if b and b not in ids:
            print(f"graph_lint: FAIL unknown node '{b}'")
            ok = False
        t = e.get("type")
        if t and t not in {"shares_var_with","informs","depends","conflicts","risks_with","vertical"}:
            print(f"graph_lint: FAIL disallowed edge type '{t}'")
            ok = False
    if ok:
        print("graph_lint: PASS")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
