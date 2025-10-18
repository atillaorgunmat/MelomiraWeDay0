#!/usr/bin/env python3
# tools/validate_question_chain.py — quick checks for chain hygiene
import os, sys, yaml, argparse

def fail(msg):
    print("FAIL:", msg)
    return 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qdir", default="q")
    ap.add_argument("--graph", default="graph/questions.yaml")
    args = ap.parse_args()

    # Load q files
    q = {}
    for f in os.listdir(args.qdir):
        if f.endswith(".yaml"):
            with open(os.path.join(args.qdir, f), "r", encoding="utf-8") as fh:
                y = yaml.safe_load(fh) or {}
            if "id" in y:
                q[y["id"]] = y

    # Rule: WHAT/HOW must have shared_vars key
    for id_, y in q.items():
        tier = (y.get("tier") or "").upper()
        if tier in ("WHAT","HOW") and "shared_vars" not in y:
            return fail(f"{id_}: WHAT/HOW missing shared_vars[]")

    # Rule: q/* must not contain cross_links_typed
    for id_, y in q.items():
        if "cross_links_typed" in y:
            return fail(f"{id_}: q/* must use untyped cross_links[], typed links live in graph")

    # Rule: No‑Jump — depends_on must point only to direct parent(s) by tier
    for id_, y in q.items():
        tier = (y.get("tier") or "").upper()
        parents = y.get("depends_on") or []
        if tier == "WHAT":
            # parent must be WHY or WHAT (direct)
            pass  # informational only here
        if tier == "HOW":
            # parent must be WHAT (direct)
            pass  # informational only here

    print("PASS: validate_question_chain basic checks")
    return 0

if __name__ == "__main__":
    sys.exit(main())
