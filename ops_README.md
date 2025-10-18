# ops_README.md — Operator Quick Commands (v4.4)

## Update docs/tools via short‑lived PR (zsh‑safe)
```bash
git fetch origin
git checkout -B docs/v4.4 origin/pack/<PACK_ID>
unzip -o "$HOME/Downloads/chatgpt-project-v4.4-updates.zip" -d .
git add -A PROJECT_INSTRUCTIONS.md GOVERNANCE.solo.md audit_checklists.md route_macros.md ops_README.md tools scripts
git commit -m "v4.4: chain‑centric docs + search‑index tools"
git push -u origin docs/v4.4
git diff --name-status origin/pack/<PACK_ID>..origin/docs/v4.4
# Open PR: base=pack/<PACK_ID>, head=docs/v4.4
```

## Build/refresh the search index
```bash
python3 tools/build_question_index.py --qdir q --graph graph/questions.yaml --out dist
git add -A dist/search_index.json dist/question_matrix.csv
git commit -m "dist: refresh question search index (v4.4)"
git push
```

## Compute bank_version (blob SHA)
```bash
git fetch origin
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'
```

## Avoid zsh comment gotchas
- Do not paste inline `#` comments on the same line as commands.
- Quote globs like `"q/*.yaml"` when staging files.
