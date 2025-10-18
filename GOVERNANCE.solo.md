# GOVERNANCE.solo.md — v4.5.2 (Solo) — Routing & Enforcement

This file defines **conversation flow**, **acceptance gates**, and **capacity** rules. It complements PROJECT_INSTRUCTIONS.md.

## Roles
- **AUTO (Single‑Reader):** reads truth; verifies/applies. Cannot decide scope.
- **GUIDANCE‑ORG:** explores, proposes, and freezes q‑files via `pro_request`.
- **SELECT‑ORG:** chooses among GUIDANCE options; publishes `selection_decision`.
- **PRO (optional):** deep evaluation threads after freeze.
- **Operator:** runs route lines and short‑lived PRs when needed.

## Thread discipline (Echo‑Forward)
- Exactly **one fenced YAML** per FORM turn.
- Use the **route line** and then paste the YAML.
- Do not mix roles in one message. Handoffs cross threads using the same YAML (echo‑forward).

## Handoff contract (provenance)
Every chooser must cite its inputs.
- **SELECT‑ORG → selection_decision** MUST include `provenance.nomination_ref` (the question_nomination it is based on) and `provenance.auto_read_ref` (the AUTO‑READ snapshot/commit).
- **GUIDANCE‑ORG → pro_request** SHOULD include `provenance.selection_ref` (the selection_decision it implements).
Governance will not accept selections without provenance (soft fail → return to sender).

## Acceptance gates
### A. SELECT‑ORG (selection_decision)
- **Immediate parents only** in `vertical_parents`; no cross‑domain jumps.  
  Example: `UNK-BIZ-01` → parent must be `UNK-BIZ-00` (not `UNK-IND-VAL-00`).
- `horizontals_typed` expresses **intent** only; actual edges are added later in `graph/questions.yaml`.
- **Provenance present** as above.
- **Capacity gate** applies (below).

### B. GUIDANCE‑ORG (pro_request)
- Only write **FROZEN** q‑files.
- **Typed links prohibited** in q‑files; use **untyped** `cross_links[]` only.
- WHAT/HOW declare **`shared_vars[]`** when value objects are shared.
- Include `origin.from_clarifiers` ids; do not copy clarifier prose.
- Must pass **AUTO‑VERIFY** checks: `bank_integrity`, `no_skip`, `typed_cross_links`, `graph_completeness`, `system_scenario`.

### C. Graph updates
- Add `horizontals_typed:` edges in `graph/questions.yaml` to reflect the selection intent. Keep edges **direct** and **typed**.

## Capacity gate
- Parallel nuclei are allowed **if** the operator believes throughput is safe. Default policy: **soft‑warn if more than two nuclei** are selected at once; no hard numeric limit. A selection exceeding current capacity may be returned with a “reduce scope” note.

## Decision & Assumption hygiene
- Decisions: record irreversible choices in `docs/DECISIONS/decision_log.yaml` and optional per‑ID notes (e.g., `docs/DECISIONS/UNK-OPS-02.md`). Reference them in q‑files via `origin.decisions_refs`.
- Assumptions: track in `docs/ASSUMPTIONS/register.yaml`; reference via `origin.assumptions` in q‑files.

## Routing macros (paste‑ready)
- AUTO‑READ:  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`
- SELECT‑ORG (choose):  
  `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>` … *(paste **selection_decision** YAML)*
- Freeze via GUIDANCE:  
  `ROUTE → GUIDANCE‑ORG (FORM) for <PACK_ID>: pre‑PRO pro_request (q_patch allowed)`
- AUTO‑VERIFY / APPLY:  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY`  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY`

## Common failure modes (and what to do)
- **SELECT‑ORG lacks provenance** → return with request to include `provenance.*` values.  
- **Vertical jumps** declared (e.g., WHAT parent is a cross‑domain WHY) → reject and request correction.  
- **Typed links added in q‑files** → reject; move them to graph.  
- **Over‑selection vs. capacity** → soft‑warn and ask for reduction or staged selection.

## Freeze windows & reopen triggers
- Freeze windows are weekly by default (operator may choose cadence in `docs/PROCESS/CADENCE.md`).  
- Reopen only on: safety incident, major dependency shift, or capacity breach documented in `docs/RISKS/register.yaml`.
