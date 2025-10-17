# ops_README.md — Operator Handbook (v4.3)

## Golden rules
- One route per message; FORM = one fenced YAML.
- AUTO is the only live repo reader (Single‑Reader). Confirm state with AUTO‑READ.

## Typical loop
1) AUTO‑READ → snapshot.
2) SELECT‑ORG (FREE) → pick FROZEN target(s) + edges.
3) GUIDANCE (FORM) → `pro_request` (add `q_patch` if editing q/*); Echo‑Forward to AUTO.
4) AUTO‑VERIFY → if bank_integrity FAIL, re‑emit with expected_sha.
5) AUTO‑APPLY → connector‑limited: manual PR; then AUTO‑READ confirm.

## Quick commands
- Bank blob SHA:
  `git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'`
- Verify diff before PR:
  `git diff --name-status origin/pack/<PACK_ID>..origin/<head-branch>`

## Lint hints
- q‑files: use `cross_links` (untyped) and include `shared_vars` for WHAT/HOW.
- graph/questions.yaml: keep typed edges (shares_var_with|informs|depends|conflicts|risks_with).
