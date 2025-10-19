# GOVERNANCE.solo.md — v4.5.2 (Handoff‑Compact)

**Roles**
- **Operator**: routes, echo‑forwards YAML, runs PRs (Pattern‑B), never authors content.  
- **GUIDANCE‑ORG**: produces `clarifier_round`, `question_nomination`, and `pro_request`.  
- **SELECT‑ORG**: produces `selection_decision` (no prose).  
- **AUTO**: produces `auto_verify`, `auto_apply` (ledger), and `auto_response` (reader).

**Principles**
- **Single‑Reader**: only AUTO reads the repo. Others consume `share_list` + pasted context.  
- **Echo‑Forward Discipline**: paste prior YAML verbatim; then send the route macro.  
- **No Numeric Quotas**: coverage is qualitative; capacity gating decides parallelism.  
- **Typed Links in Graph**: all typed horizontals live in `graph/questions.yaml`. q‑files use untyped `cross_links[]`.  
- **FROZEN‑only q‑files**: bank status may vary, but q‑files commit only when FROZEN.  
- **Provenance**: q‑files use `origin` to reference clarifiers/assumptions/decisions (IDs only).

**Capacity Gate**
- Default allows **up to 2 parallel nuclei** when weekly capacity ≥ 1 FROZEN node. SELECT‑ORG enforces this.

**Decision & Assumption Registers**
- `docs/DECISIONS/decision_log.yaml` and `docs/ASSUMPTIONS/register.yaml` hold entries with IDs (D‑*, A‑*).  
- Each `pro_request.q_patch.items[*].body.origin` may reference these IDs.

**Freeze Windows & Reopen Triggers**
- Freeze after `auto_apply.applied: true`. Reopen only via documented triggers (safety incident, dependency change, KPI invalidation).

**Pattern‑B (Connector‑limited)**
1) AUTO → `auto_verify` PASS.  
2) Operator raises PR.  
3) On merge, Operator posts `auto_apply` with `mode: operator` and the merge SHA.  
4) AUTO may follow with `auto_response` for confirmation.

**SELECT‑ORG Decision Heuristics**
- Prefer nuclei that (a) unblock measurement/KPIs, (b) reduce legal risk, or (c) validate right‑to‑win.  
- Maintain vertical completeness (WHY→WHAT) and register required typed horizontals for the graph.

**Audit Cheatsheet**
- `scripts/run_index_build.sh` for search index.  
- `tools/validate_question_chain.py` for typed‑link and no‑skip checks.
