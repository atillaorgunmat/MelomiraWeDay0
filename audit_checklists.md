# audit_checklists.md — minimal operator audits (v4.3)

## L0 (GUIDANCE‑ORG)
- Clarifier grammar: abstraction‑0; no numbers/names/choice verbs.
- Freeze only when coverage ≥ 0.70 and no OPEN.
- Output: one fenced `clarifier_round` → `question_nomination` → `bank_ops` (tables only).

## AUTO‑READ
- One fenced `auto_response` only (inventory, gaps, share_list, h_relations, v_relations, trace_map).

## SELECT‑ORG
- One fenced `selection_decision`; IDs must be FROZEN in Bank.
- Include vertical parents + typed horizontals (allowed: shares_var_with|informs|depends|conflicts|risks_with).

## GUIDANCE (pre‑PRO)
- One fenced `pro_request`.
- May embed `q_patch` (only FROZEN items). Ensure graph present and typed links used.
- Include acceptance gates and require flags.

## Q‑file checks (lint‑friendly)
- WHAT/HOW q‑files include `shared_vars: [...]` if graph references them.
- All q‑files use untyped `cross_links: [ "<adjacent id>", ... ]` (not `cross_links_typed`).
- Typed link semantics live only in `graph/questions.yaml`.

## AUTO‑VERIFY
- One fenced `auto_verify: PASS/FAIL` with checks: bank_integrity, no_skip, typed_cross_links (in graph), graph_completeness, system_scenario.

## AUTO‑APPLY
- One fenced `auto_apply`; envelope updated; share bundle emitted (or manual PR in connector‑limited).

## PRO‑EVAL (advisory)
- Non‑writing evaluation; proposes options/new questions (route back to GUIDANCE‑ORG).
