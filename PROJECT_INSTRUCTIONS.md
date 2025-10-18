# PROJECT_INSTRUCTIONS.md — v4.5 (Solo Variant, Single‑Bank Policy + Clarifier→Assumption Wiring)

Each FORM turn outputs **one fenced YAML** with the exact top key shown below.
`chain_id` is used in FREE threads (GUIDANCE‑ORG, SELECT‑ORG). `pack_id` is used where AUTO must read the repo.
If both appear, AUTO trusts `pack_id` for repository paths; human threads may reference `chain_id` for narrative continuity.

---

## clarifier_round (FREE → GUIDANCE‑ORG)
```yaml
clarifier_round:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  level: L0
  review_set: [ "...meta docs only..." ]
  context_horizon: [ { id: "...", why: "..." } ]
  themes: [ { id: T1, label: "...", notes: "..." }, ... ]
  clarifiers: [ { id: C1, abstraction: 0, themes: [T*], status: OPEN|PARKED,
                  prompt: "...", depends_on: [], park_if_unanswered: true, why: "..." }, ... ]
  assumptions_emerged: [ { id: "A-...", text: "...", related_ids: ["<q-id>"], test: "..." }, ... ]
  risks_emerged: [ "..." ]
  context_refs_emerged: [ "docs/... or q/..." ]
  coverage: { estimated_fraction: 0..1 }
  decision: { freeze_clarifiers: true|false, reason: "..." }
```
Purpose: capture discussion + harvest assumptions/risks for persistence.

---

## assumption_register_ops (FREE → GUIDANCE‑ORG)
```yaml
assumption_register_ops:
  chain_id: <CHAIN_ID>
  changes:
    - op: upsert
      item: { id: "A-...", text: "...", status: open|in_test|passed|failed|rejected,
              source: GUIDANCE-ORG|PRO|AUTO, related_ids: ["<q-id>", "..."], test: "..." }
    - op: remove
      id: "A-..."
  decision: { commit: true|false, reason: "..." }
```
Purpose: keep a single canonical register at `docs/ASSUMPTIONS/register.yaml`.

---

## question_nomination (FREE → GUIDANCE‑ORG)
```yaml
question_nomination:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  level: L0
  review_set: [ ... ]
  candidates: [ { id: "...", title: "...", type: WHY|WHAT|HOW, coverage: 0..1,
                 from_clarifiers: [C*], assumptions: ["A-..."], depends_on: [] }, ... ]
  leftovers: [ "..." ]
  decision: { freeze: true|false, reason: "..." }
```

---

## bank_ops (FREE → GUIDANCE‑ORG)
**Single‑Bank Policy**: `docs/FOUNDATIONS/QUESTION_BANK.md` contains **all** items with a `status` column:
`CANDIDATE | FROZEN | PARKED | REOPENED | RETIRED`.  
`graph/questions.yaml` must include **only** `FROZEN` nodes.

```yaml
bank_ops:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
    | EX-IND-00 | Why ... ? | WHY | IND | CANDIDATE | — | GUIDANCE | Why: ... |
```
Purpose: capture/replace the table in QUESTION_BANK.md. (Operator applies via PR.)

---

## selection_decision (FREE → SELECT‑ORG)
```yaml
selection_decision:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  chosen:
    - id: "<FROZEN bank id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
```
Purpose: freeze a tiny nucleus (2–3 nodes). Exactly **one** WHY parent per WHAT/HOW.

---

## pro_request (FORM → GUIDANCE pre‑PRO) — includes q_patch
```yaml
pro_request:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate","Assumption Challenge","UX Backcast","Prototype Gate",
               "System Scenario","Coupling Watchlist","Not‑Doing","CCR‑Lite"]
  require:
    shared_vars: true
    typed_cross_links: true
    system_scenario: true
    provenance_limit: 2
  q_patch:
    bank_version: "<sha of QUESTION_BANK.md>"
    items:
      - id: "<id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHY|WHAT|HOW
          depends_on: [ "<WHY id>" ]   # WHAT/HOW only; single direct parent
          status: FROZEN
          origin:
            from_clarifiers: ["C1","C2"]     # ≤2
          shared_vars: [ value_object ]       # WHAT/HOW required
          cross_links: [ "<adjacent id>", "..." ]   # UNTYPED here
          assumptions:
            - { id: "A-...", text: "...", status: open|in_test|passed|failed|rejected, test: "..." }
          risks: [ "short risk notes" ]
          context_refs: [ "docs/...","notes/...","q/..." ]
```
Typed semantics for links live **only** in `graph/questions.yaml`.

---

## auto_response (FORM → AUTO‑READ)
```yaml
auto_response:
  pack_id: <PACK_ID>
  repo_state: empty|seeded
  repo_inventory: [ "paths..." ]
  gaps: [ "missing vs governance..." ]
  share_list: [ "files to share with other modes..." ]
  h_relations: [ { a: "<id>", b: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  v_relations: [ { parent: "<WHY|WHAT id>", child: "<WHAT|HOW id>" } ]
  trace_map: { "<id>": { files: [ "..." ], dependents: [ "..." ] } }
  scaffold_needed: false
```

---

## auto_verify (FORM → AUTO)
```yaml
auto_verify:
  pack_id: <PACK_ID>
  result: PASS|FAIL
  checks:
    bank_integrity: PASS|FAIL
    bank_status_policy: PASS|FAIL     # QUESTION_BANK only uses allowed statuses
    bank_graph_alignment: PASS|FAIL   # graph only contains FROZEN ids
    provenance_limit: PASS|FAIL       # ≤2 clarifiers per q-file
    assumptions_linkage: PASS|FAIL    # any A-* in q/* exists in register
    no_skip: PASS|FAIL
    typed_cross_links: PASS|FAIL      # q/* has untyped cross_links; graph holds typed
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

## decision_log_ops (FREE → GUIDANCE/PRO)
```yaml
decision_log_ops:
  chain_id: <CHAIN_ID>
  entries:
    - id: "D-2025-10-18-01"
      question_id: "<id>"
      decision: "Accepted|Rejected|Deferred"
      rationale: "short"
      impacts: ["<id>", "..."]
      assumptions_touched: ["A-..."]
      follow_ups: ["<new question>", "..."]
  decision: { commit: true|false }
```
Persists to `docs/DECISIONS/decision_log.yaml`.

## pro_eval (ADVISORY)
```yaml
pro_eval:
  chain_id: <CHAIN_ID>
  evaluated_ids: ["<id>"]
  options_considered: ["short notes"]
  new_questions: ["<id or title>"]
```

---

# Handoff & Thread‑Isolation Discipline (Option‑A)
- **Echo‑Forward** the same `pro_request` into AUTO before VERIFY/APPLY.
- One route per message; FORM turns output **exactly one fenced YAML**.

# Connector‑Limited Ops Addendum (Pattern B)
- Same as v4.2; bank_version = blob SHA via `git ls-tree`.

# Operator Route Macros (paste‑ready)
- To AUTO‑READ:  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`
- To GUIDANCE (pre‑PRO):  `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pre‑PRO pro_request (may include q_patch)`
- To AUTO‑VERIFY: `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY`
- To AUTO‑APPLY:  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY`
- To SELECT‑ORG:  `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>`
