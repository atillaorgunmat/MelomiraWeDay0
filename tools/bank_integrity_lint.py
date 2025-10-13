#!/usr/bin/env python3
import sys, pathlib, re, yaml

def parse_bank(path):
    txt = pathlib.Path(path).read_text(encoding="utf-8").splitlines()
    ids = set()
    statuses = {}
    for line in txt:
        if not line.strip().startswith("|"):
            continue
        cols = [c.strip() for c in line.strip().split("|")[1:-1]]
        if len(cols) < 8:
            continue
        _id, title, tier, domain, status = cols[0], cols[1], cols[2], cols[3], cols[4]
        if _id and _id != "id":
            ids.add(_id)
            statuses[_id] = status
    return ids, statuses

def main():
    bank_path = "docs/FOUNDATIONS/QUESTION_BANK.md"
    ids, statuses = parse_bank(bank_path) if pathlib.Path(bank_path).exists() else (set(), {})
    q_dir = pathlib.Path("q")
    if not q_dir.exists():
        print("bank_integrity_lint: PASS (no q/* present)")
        sys.exit(0)
    ok = True
    for q in q_dir.glob("*.yaml"):
        data = yaml.safe_load(q.read_text(encoding='utf-8')) or {}
        _id = data.get("id") or q.stem
        st = statuses.get(_id, None)
        if st != "FROZEN":
            print(f"bank_integrity_lint: FAIL {q.name}: not FROZEN in Bank")
            ok = False
    if ok:
        print("bank_integrity_lint: PASS")
        sys.exit(0)
    sys.exit(1)

if __name__ == "__main__":
    main()
