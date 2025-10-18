#!/usr/bin/env python3
# tools/build_question_index.py — emit dist/search_index.json and dist/question_matrix.csv
import os, sys, json, argparse, csv
from collections import defaultdict

try:
    import yaml
except Exception as e:
    sys.stderr.write("PyYAML is required. pip install pyyaml\n")

def tokenize(s):
    return [t.lower() for t in (s or "").replace("/", " ").replace("-", " ").split() if t]

def load_q_files(qdir):
    out = {}
    for root, _, files in os.walk(qdir):
        for f in files:
            if f.endswith(".yaml") or f.endswith(".yml"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fh:
                    try:
                        y = yaml.safe_load(fh) or {}
                    except Exception as e:
                        y = {}
                if isinstance(y, dict) and "id" in y:
                    y["_file"] = path
                    out[y["id"]] = y
    return out

def load_graph(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            g = yaml.safe_load(fh) or {}
        return g
    except FileNotFoundError:
        return {}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--qdir", required=True)
    ap.add_argument("--graph", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    q = load_q_files(args.qdir)
    g = load_graph(args.graph)
    htyped = g.get("edges", {}).get("horizontals_typed", []) or []

    # Build adjacency
    horiz = defaultdict(list)
    for e in htyped:
        a, b = e.get("from"), e.get("to")
        if a and b:
            horiz[a].append(b)

    # Build JSON index
    index = []
    for qid, y in sorted(q.items()):
        entry = {
            "id": qid,
            "title": y.get("title"),
            "tier": y.get("tier"),
            "domain": y.get("domain"),
            "status": y.get("status"),
            "depends_on": y.get("depends_on", []) or [],
            "shared_vars": y.get("shared_vars", []) or [],
            "cross_links": y.get("cross_links", []) or [],
            "assumptions": y.get("assumptions", []) or [],
            "risks": y.get("risks", []) or [],
            "context_refs": y.get("context_refs", []) or [],
            "file": y.get("_file"),
            "horizontals_to": horiz.get(qid, []),
            "tokens": sorted(set(tokenize(y.get("title","")) + tokenize(y.get("domain","")))),
        }
        index.append(entry)

    with open(os.path.join(args.out, "search_index.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, indent=2)

    # Build CSV matrix
    csv_path = os.path.join(args.out, "question_matrix.csv")
    cols = ["id","title","tier","domain","status","depends_on","shared_vars","cross_links","horizontals_to","assumptions","risks","context_refs","file"]
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for e in index:
            row = [
                e["id"],
                e["title"] or "",
                e["tier"] or "",
                e["domain"] or "",
                e["status"] or "",
                ";".join(e["depends_on"]),
                ";".join(e["shared_vars"]),
                ";".join(e["cross_links"]),
                ";".join(e["horizontals_to"]),
                ";".join([a.get("id","") for a in e["assumptions"]]) or "",
                ";".join([r.get("id","") for r in e["risks"]]) or "",
                ";".join(e["context_refs"]),
                e["file"] or "",
            ]
            w.writerow(row)

    print("Wrote:", os.path.join(args.out, "search_index.json"))
    print("Wrote:", csv_path)

if __name__ == "__main__":
    main()
