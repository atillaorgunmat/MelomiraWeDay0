# audit_checklists.md — v4.5.2 (Operator Audits)

## A. FORM & Routing
- One fenced YAML per FORM turn, correct top key.
- One route per message; echo‑forward exact `pro_request` YAML from GUIDANCE → AUTO.

## B. Bank & Graph Integrity
- QUESTION_BANK rows: statuses only `candidate|nucleus|parked|frozen|committed`. IDs unique.
- Graph has all nodes present in bank; **typed links only in graph** using allowed types: `informs|depends|conflicts|risks_with|shares_var_with`.
- No‑skip: every vertical/horizontal edge is direct.

## C. q‑file Hygiene (FROZEN‑only)
- `q/<ID>.yaml` present for frozen nodes; `tier` and `title` interrogative.
- `cross_links[]` present if adjacent nodes exist (untyped).
- **WHAT/HOW** include `shared_vars[]` when applicable.
- `origin.from_clarifiers` references GUIDANCE clarifier IDs only (no duplicated text).
- Optional: `origin.assumptions` (`A-*`), `origin.decisions_refs` (`D-*`).

## D. System Scenario & Capacity Gate
- At least one `system_scenario` that crosses ≥2 branches exists before freezing a nucleus.
- Capacity gate documented: default 1 nucleus, may allow 2 in parallel when coupling & load allow.

## E. Pattern B (if AUTO cannot write)
- Compute `bank_version` via `git ls-tree ... QUESTION_BANK.md` (40‑hex SHA).
- Short‑lived PR from `origin/pack/<PACK_ID>`; verify remote‑vs‑remote diff is non‑empty.
- Post‑merge `AUTO‑READ` to confirm truth.

## F. Share Bundle
- `tools/make_share_bundle.py` produces `dist/share_bundle.zip` containing: QUESTION_BANK, graph, TRACE map, SCENARIOS, and frozen `q/*`.
