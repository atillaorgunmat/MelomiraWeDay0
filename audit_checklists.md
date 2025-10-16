# audit_checklists.md — minimal operator audits

## L0 (GUIDANCE‑ORG)
- Clarifier grammar: abstraction‑0; no numbers/names/choice verbs.
- Freeze only when coverage ≥ 0.70 and no OPEN. If not, request a one‑round Correction Snapshot.
- Output: one fenced `clarifier_round` → `question_nomination` → `bank_ops` (tables only).

## AUTO‑READ
- One fenced `auto_response` only.
- Must include: repo_inventory, gaps, share_list, h_relations, v_relations, trace_map.
- `scaffold_needed:false` unless Day‑0 gaps demand it.

## SELECT‑ORG
- One fenced `selection_decision`; IDs must be FROZEN in Bank.
- Include vertical parents + typed horizontals.

## GUIDANCE (pre‑PRO)
- One fenced `pro_request`.
- May embed `q_patch` (only FROZEN items). Ensure graph present and typed links used.
- Include acceptance gates and require flags.

## AUTO‑VERIFY
- One fenced `auto_verify: PASS/FAIL` with checks: bank_integrity, no_skip, typed_links, graph_completeness, system_scenario.

## AUTO‑VERIFY (lint expectations)

- If bank_integrity: FAIL, AUTO must include expected_sha for QUESTION_BANK.md in notes. Operator re‑emits pro_request with that SHA and re‑runs VERIFY.

- trace_map_present: files must include docs/FOUNDATIONS/QUESTION_BANK.md, graph/questions.yaml, and q/<id>.yaml for each ID; dependents must include vertical children and typed‑linked peers.
Operator rule: One route per message; do not run VERIFY and READ in the same message.

## AUTO‑APPLY
- One fenced `auto_apply`; envelope updated; share bundle emitted.

## PRO‑EVAL (advisory)
- Non‑writing evaluation; proposes options and new questions (route those back to GUIDANCE‑ORG).
