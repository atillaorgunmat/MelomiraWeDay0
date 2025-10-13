#!/usr/bin/env python3
import sys, yaml, pathlib, zipfile

def main():
    env = yaml.safe_load(pathlib.Path("packs/P-FND-0001/envelope.yaml").read_text(encoding="utf-8"))
    share_list = []
    # always include Bank, graph, trace
    base = ["docs/FOUNDATIONS/QUESTION_BANK.md", "graph/questions.yaml", "docs/TRACE/trace_map.yaml"]
    share_list.extend(base)
    # include last selection and pro_request if present
    for key in ("selection_ref","pro_request_ref","auto_response_ref"):
        ref = (env.get("pack_envelope") or {}).get(key) or {}
        p = ref.get("path")
        if p and pathlib.Path(p).exists():
            share_list.append(p)
    zip_path = pathlib.Path("dist/P-FND-0001-share.zip")
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in share_list:
            if pathlib.Path(p).exists():
                z.write(p, arcname=p)
    print(f"share bundle: {zip_path}")
if __name__ == "__main__":
    main()
