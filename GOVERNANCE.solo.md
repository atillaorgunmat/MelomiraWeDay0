# GOVERNANCE.solo.md — v4.5.1 (Solo Variant) + Non‑Numeric Nucleus

**Purpose.** Align roles, gates, and hygiene so chains can be proposed, frozen, and traced with minimal friction. This variant removes numeric quotas on clarifiers and nucleus options, enforces typed‑link placement only in the graph, and allows parallel nuclei via a capacity gate.

---

## Roles & Threads (Option‑A, Echo‑Forward)

- **GUIDANCE‑ORG (FREE)**: runs `clarifier_round`, `question_nomination` (may include any number of `nucleus_options`), maintains `bank_ops`, and authors `pro_request` (with optional `q_patch`). May also emit `pro_eval` advisory notes.
- **SELECT‑ORG (FREE)**: emits `selection_decision` for the next FROZEN targets (supports parallel nuclei per capacity gate).
- **AUTO (FORM)**: the **single live repo reader/writer**. Accepts `auto_read`, `auto_verify`, `auto_apply`. If writing is disabled, the Operator follows **Pattern B** (short‑lived PR) while keeping Single‑Reader = AUTO.
- **Operator Console**: routes messages, enforces FORM fencing and one‑route‑per‑message discipline. Does not author domain content.

**Echo‑Forward**: The exact YAML emitted in GUIDANCE for `pro_request` must be pasted **verbatim** into AUTO for `AUTO‑VERIFY` → `AUTO‑APPLY`.

---

## Core Invariants

1. **Single‑Reader = AUTO.** All repository truth comes from AUTO `auto_response`/`auto_read`.
2. **No numeric quotas.** GUIDANCE may return any number of clarifiers or nucleus options; quality and direct dependencies matter more than counts.
3. **Typed links live only in `graph/questions.yaml`.** Use `horizontals_typed` with types from: `informs | depends | conflicts | risks_with | shares_var_with`.
4. **q‑files are FROZEN‑only.** Bank rows may use: `candidate | nucleus | parked | frozen | committed`.
5. **q‑file hygiene.**
   - Use **untyped** `cross_links: ["<id>"]` (typed semantics belong in the graph).
   - **WHAT/HOW** declare `shared_vars: [ ... ]` when value‑objects are shared across nodes.
   - Record provenance only by **reference** inside `origin`:
     ```yaml
     origin:
       from_clarifiers: [C*]     # IDs from GUIDANCE clarifier_round
       assumptions:    [A-*]     # optional IDs from docs/ASSUMPTIONS/register.yaml
       decisions_refs: [D-*]     # optional IDs from docs/DECISIONS/decision_log.yaml
     ```
6. **No‑skip rule.** Every edge must be direct. Vertical parents must exist in the bank; horizontals must use allowed types (in graph only).
7. **Capacity gate.** Default execution is one nucleus at a time; governance may permit **two parallel nuclei** when capacity and coupling allow.
8. **Freeze windows & reopen triggers.** Decisions freeze at weekly gates; reopen only via documented triggers (e.g., safety incident, brand‑guideline breach, capacity failure, material assumption falsified).

---

## Acceptance Gates (PRO readiness)

- **Simplicity Gate** (clear question, single intent)
- **Assumption Challenge** (hypotheses + tests listed or referenced)
- **UX Backcast** (what success artifacts/users see)
- **Prototype Gate** (evidence plan or tiny pilot)
- **System Scenario** (at least one path that crosses ≥2 branches)
- **Coupling Watchlist** (shared_vars & typed links reviewed)
- **Not‑Doing** (out‑of‑scope noted)
- **CCR‑Lite** (clarity, completeness, retrievability)

Only when these pass should GUIDANCE emit a `pro_request` to freeze nodes.

---

## Governed Loop

1. **GUIDANCE‑ORG**: `clarifier_round` (OPEN/PARKED; no quotas).
2. **GUIDANCE‑ORG**: `question_nomination` (may include any number of `nucleus_options`).
3. **SELECT‑ORG**: `selection_decision` (can pick 1–2 nuclei per capacity gate).
4. **GUIDANCE‑ORG**: `pro_request` (with optional `q_patch` of q‑files).
5. **AUTO**: `AUTO‑VERIFY` → `AUTO‑APPLY`. If apply cannot write, Operator uses **Pattern B** (short‑lived PR).
6. **AUTO**: `AUTO‑READ` to confirm inventory/gaps/share_list/relations/trace.
7. **Operator**: build/share bundle (e.g., `tools/make_share_bundle.py`).

---

## Pattern B (Connector‑limited, short‑lived PR)

- Compute `bank_version` for `q_patch` via:
  ```bash
  git fetch origin
  git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'
  ```
- Prepare a topic branch from `origin/pack/<PACK_ID>`, unzip the patch, `git add`, commit, push, open PR, merge.
- Confirm via `AUTO‑READ` after merge.

---

## Lints & What They Enforce

- **form_fencing_lint.py** — exactly one fenced YAML per FORM turn; correct top keys.
- **bank_lint.py** — bank table integrity; allowed statuses; no unknown IDs.
- **graph_lint.py** — typed links only in graph; verticals/horizontals sane; `shared_vars` integrity.
- **typed_links_lint.py** — allowed types only; no typed links in q‑files.
- **no_skip_lint.py** — direct deps only (no gaps).

---

## Decision & Assumption Records

- **Assumptions** live in `docs/ASSUMPTIONS/register.yaml` (IDs `A-*`).
- **Decisions (optional)** live in `docs/DECISIONS/decision_log.yaml` (IDs `D-*`).
- Q‑files reference these IDs via `origin.assumptions` and `origin.decisions_refs`. Keep sources of truth single and referenced.

---

## Routing Macros (paste‑ready lines)

- To AUTO‑READ:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`
- To GUIDANCE (pre‑PRO):
  `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pre‑PRO pro_request (may include q_patch)`
- To AUTO‑VERIFY:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-VERIFY`
- To AUTO‑APPLY:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-APPLY`
- To SELECT‑ORG:
  `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>`

---

## Out‑of‑Scope (Solo Variant)

No multi‑writer automation, no background code runners, no unmanaged links between packs. All cross‑pack links must be explicit in the graph or parked until governance adds them.
