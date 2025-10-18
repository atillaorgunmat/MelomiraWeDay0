# audit_checklists.md — operator audits (v4.4)

## L0 (GUIDANCE‑ORG) — Clarifier Round
- Abstraction only; coverage ≥ 0.70 to freeze. No OPEN clarifiers.
- Output order enforced: `clarifier_round` → `question_nomination` → `bank_ops`.
- `chain_id` present. `pack_id` optional.

## Bank Discipline
- `docs/FOUNDATIONS/QUESTION_BANK.md` exists and rows match graph nodes (ids, tiers, status).
- Every WHAT/HOW row has a direct WHY parent (No‑Jump).

## Q‑File Hygiene
- WHAT/HOW have `shared_vars` defined (can be empty but key must exist).
- Q‑files use **untyped** `cross_links` only.
- Q‑files carry `assumptions[]`, `risks[]`, `context_refs[]` sections (can be empty).

## Graph Discipline
- Typed edges exist only in `graph/questions.yaml`.
- Allowed: `shares_var_with|informs|depends|conflicts|risks_with`.
- At least one `system_scenarios` path crosses ≥2 branches.

## Single‑Reader & Option‑A
- AUTO forms include `pack_id` and are one fenced YAML.
- Echo‑Forward observed before VERIFY.
- On bank_integrity FAIL, Operator re‑emits with AUTO’s `expected_sha`.

## Search Index
- `dist/search_index.json` and `dist/question_matrix.csv` present and updated after q‑patches.
