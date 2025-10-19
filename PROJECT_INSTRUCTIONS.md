# PROJECT_INSTRUCTIONS.md — v4.5.2-mini (Solo Variant)

**FORM discipline:** each FORM turn outputs **one fenced YAML** with the top key shown.  
**Thread isolation:** use *Echo‑Forward* (see Handoff).  
**No numeric quotas:** guidance can suggest ranges; lints do not enforce counts.

---

## clarifier_round (FREE → GUIDANCE‑ORG)
**Purpose:** surface themes & clarifiers; keep OPEN/PARKED until freeze. `chain_id` and `pack_id` are optional.

```yaml
clarifier_round:
  chain_id: <CHAIN_ID>        # e.g., melomiraweday0 (optional)
  pack_id: <PACK_ID>          # optional legacy (e.g., P-FND-0001)
  level: L0
  review_set: [ "...meta docs only..." ]
  context_horizon: [ { id: "...", why: "..." } ]
  themes: [ { id: T1, label: "...", notes: "..." }, ... ]
  clarifiers: [ { id: C1, abstraction: 0, themes: [T*], status: OPEN|PARKED,
                  prompt: "...", depends_on: [], park_if_unanswered: true, why: "..." }, ... ]
  coverage: { estimated_fraction: 0..1 }
  decision: { freeze_clarifiers: true|false, reason: "..." }
```

---

## question_nomination (FREE → GUIDANCE‑ORG)
**Purpose:** nominate candidates and optional **nucleus_options** (distinct sets of WHY→WHATs). **No quotas.**

```yaml
question_nomination:
  chain_id: <CHAIN_ID>    # optional
  pack_id: <PACK_ID>      # optional
  level: L0
  review_set: [ ... ]
  candidates: [ { id: "...", title: "...", type: WHY|WHAT|HOW, coverage: 0..1,
                 from_clarifiers: [C*], assumptions: ["A→test"], depends_on: [] }, ... ]
  leftovers: [ "..." ]
  decision: { freeze: true|false, reason: "..." }

  nucleus_options:
    - id: "<O1>"
      label: "<human title>"
      why:   { id: "<WHY id>",  title: "<interrogative>" }
      whats: [ { id: "<WHAT id>", title: "<interrogative>", depends_on: ["<WHY id>"] }, ... ]
      assumptions: [ { hypothesis: "...", test: "..." }, ... ]
      horizontals_typed: [ { a: "<id>", with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
      system_scenario: [ "step 1", "step 2", "..." ]
```

---

## bank_ops (FREE → GUIDANCE‑ORG)
**Purpose:** maintain the bank table (docs only). q‑files remain FROZEN‑only.

```yaml
bank_ops:
  chain_id: <CHAIN_ID>    # optional
  pack_id: <PACK_ID>      # optional
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
```

*Bank status vocabulary (docs only):* `candidate | nucleus | parked | frozen | committed`.

---

## selection_decision (FREE → SELECT‑ORG)
**Purpose:** choose next frozen targets. **Minimal content; no debate.** Provide **pins**:
- `bank_version` (blob SHA of `docs/FOUNDATIONS/QUESTION_BANK.md` on base)
- `auto_read_sha` (commit used for last AUTO‑READ)
- `nomination_ref` (path to the YAML that proposed the options)

```yaml
selection_decision:
  chain_id: <CHAIN_ID>   # optional
  pack_id: <PACK_ID>     # optional
  pins:
    bank_version:  "<40-hex>"
    auto_read_sha: "<40-hex commit>"
    nomination_ref: "docs/GUIDANCE/...yaml"
  chosen:
    - id: "<WHY or WHAT id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
```

---

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed `q_patch`
**Purpose:** write/update q‑files for the selected nodes.

**Rules (enforced by lints):**
- **Typed links live only in `graph/questions.yaml`.** q‑files use **untyped** `cross_links[]`.
- WHAT/HOW **must** declare `shared_vars[]` when they share a value object.
- Add provenance under `origin` (IDs only), not free text.

```yaml
pro_request:
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate","Assumption Challenge","UX Backcast","Prototype Gate",
               "System Scenario","Coupling Watchlist","Not‑Doing","CCR‑Lite"]
  require:
    shared_vars: true
    typed_cross_links: true      # i.e., typed edges in graph/ only
    system_scenario: true
  q_patch:
    bank_version: "<blob sha of QUESTION_BANK.md>"
    items:
      - id: "<FROZEN id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHAT|WHY|HOW
          title: "<interrogative>"
          depends_on: ["<WHY id>"]
          shared_vars: [ value_object ]     # for WHAT/HOW as needed
          origin:
            from_clarifiers: [C*]
            assumptions: [A-*]
            decisions_refs: [D-*]
          cross_links: ["<adjacent id>"]    # untyped; typed edges live in graph/
          status: FROZEN
```

---

## auto_verify (FORM → AUTO)
```yaml
auto_verify:
  pack_id: <PACK_ID>
  result: PASS|FAIL
  checks:
    bank_integrity: PASS|FAIL
    no_skip: PASS|FAIL
    typed_cross_links: PASS|FAIL
    graph_completeness: PASS|FAIL
    system_scenario: PASS|FAIL
  notes: "short"
```

## auto_apply (FORM → AUTO)
```yaml
auto_apply:
  pack_id: <PACK_ID>
  applied: true|false
  commit: "<sha or 'local only'>"
  notes: "short"
```

## pro_eval (ADVISORY)
```yaml
pro_eval:
  pack_id: <PACK_ID>
  evaluated_ids: ["<id>"]
  options_considered: ["short notes"]
  new_questions: ["<id or title>"]
```

---

## Handoff (Echo‑Forward, Option‑A)
1. **GUIDANCE‑ORG** → `question_nomination` (may include `nucleus_options`).  
2. **SELECT‑ORG** → `selection_decision` (pins + chosen).  
3. **GUIDANCE (pre‑PRO)** → `pro_request` with `q_patch`.  
4. **AUTO** → `AUTO‑VERIFY` → `AUTO‑APPLY` → optional `AUTO‑READ`.

**Route macros (paste lines):**
- To SELECT‑ORG: `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>`
- To GUIDANCE (pre‑PRO): `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pro_request`
- To AUTO‑VERIFY: `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY`
- To AUTO‑APPLY:  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY`
- To AUTO‑READ:   `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`

---

## Rules Recap
- Typed links only in `graph/questions.yaml`; q‑files use untyped `cross_links[]`.
- WHAT/HOW declare `shared_vars[]` when applicable.
- **No numeric quotas** for clarifiers or nucleus options.
- q‑files are **FROZEN‑only**; bank rows manage candidate/nucleus/parked/frozen/committed.
- Capacity gate may allow **parallel nuclei** when non‑contending.
