# PROJECT_INSTRUCTIONS.md — v4.4 (Chain‑Centric Solo Variant) + Connector‑Limited Ops Addendum

> Purpose: make the **question chain** the primary artifact. Keep Option‑A governance, but allow **pack_id to be optional** on FREE forms; **AUTO forms still require pack_id** (Single‑Reader routes to a specific repo pack).

## FORM output rule (unchanged)
Each FORM turn must output **one fenced YAML** with the exact top key shown below. The payloads must match the schemas here.

---

## clarifier_round (FREE → GUIDANCE‑ORG)
```yaml
clarifier_round:
  chain_id: <CHAIN>         # required for FREE forms; a human‑readable namespace for the question chain
  pack_id: <PACK_ID>        # optional; carry through when you already know the repo pack
  level: L0
  review_set: [ "...meta docs only..." ]
  context_horizon: [ { id: "...", why: "..." } ]
  themes: [ { id: T1, label: "...", notes: "..." }, ... ]
  clarifiers: [ { id: C1, abstraction: 0, themes: [T*], status: OPEN|PARKED,
                  prompt: "...", depends_on: [], park_if_unanswered: true, why: "..." }, ... ]
  coverage: { estimated_fraction: 0..1 }
  decision: { freeze_clarifiers: true|false, reason: "..." }
```

## question_nomination (FREE → GUIDANCE‑ORG)
```yaml
question_nomination:
  chain_id: <CHAIN>
  pack_id: <PACK_ID>     # optional
  level: L0
  review_set: [ ... ]
  candidates: [ { id: "...", title: "...", type: WHY|WHAT|HOW, coverage: 0..1,
                 from_clarifiers: [C*], assumptions: ["A→test"], depends_on: [] }, ... ]
  leftovers: [ "..." ]
  decision: { freeze: true|false, reason: "..." }
```

## bank_ops (FREE → GUIDANCE‑ORG)
```yaml
bank_ops:
  chain_id: <CHAIN>
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
```

## selection_decision (FREE → SELECT‑ORG)
```yaml
selection_decision:
  chain_id: <CHAIN>
  chosen:
    - id: "<FROZEN bank id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
```

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed q_patch
```yaml
pro_request:
  chain_id: <CHAIN>
  pack_id: <PACK_ID>   # required when this will later go to AUTO
  acceptance: ["Simplicity Gate", "Assumption Challenge", "UX Backcast", "Prototype Gate",
               "System Scenario", "Coupling Watchlist", "Not‑Doing", "CCR‑Lite"]
  require:
    shared_vars: true
    typed_cross_links: true
    system_scenario: true
  q_patch:
    bank_version: "<sha of QUESTION_BANK.md>"   # Git blob SHA
    items:
      - id: "<FROZEN id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHAT
          depends_on: ["<direct WHY id>"]       # No‑Jump rule: only direct parent(s)
          shared_vars: [ value_object ]         # REQUIRED for WHAT/HOW
          cross_links: [ "<peer id>", "..." ]   # untyped in q/*; types live in graph
          status: FROZEN
```

## auto_response (FORM → AUTO‑READ)   # pack_id is required for AUTO forms
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

## auto_verify (FORM → AUTO)   # pack_id required
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

## auto_apply (FORM → AUTO)   # pack_id required
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
  chain_id: <CHAIN>
  pack_id: <PACK_ID>  # optional
  evaluated_ids: ["<id>"]
  options_considered: ["short notes"]
  new_questions: ["<id or title>"]
```

---

# Question Spec (q/*.yaml) — v4.4
- `id`: string
- `title`: interrogative, concise
- `tier`: WHY|WHAT|HOW
- `domain`: short tag (e.g., BIZ, LGL, OPS, ICP)
- `status`: candidate|FROZEN|committed
- `depends_on`: [ "<direct parent id>", ... ]  # No‑Jump: only direct parents
- `shared_vars`: [name, ...]  # REQUIRED for WHAT/HOW
- `cross_links`: ["<peer id>", ...]            # untyped here; typed semantics in graph
- `assumptions`: [ { id, text, status: open|test|passed|failed, test: "how to learn" } ]
- `risks`:       [ { id, text, mitigation } ]
- `context_refs`: [ "docs/... or url", ... ]
- `notes`: "free text"

# Graph Spec (graph/questions.yaml) — unchanged intent
- Nodes for each `id` with tier/status.
- `edges.vertical`: `{ from: <child>, to: <direct parent>, rel: depends_on }` only.
- `edges.horizontals_typed`: allowed = `shares_var_with|informs|depends|conflicts|risks_with`.
- `shared_vars`: map each var → list of question ids.
- `system_scenarios`: each path crosses ≥2 branches.

# Search Index (new)
- Run `tools/build_question_index.py` to emit:
  - `dist/search_index.json` (id,title,tier,domain,status,tokens,depends_on,horizontals,shared_vars,assumptions,risks,context_refs)
  - `dist/question_matrix.csv` (wide matrix for spreadsheet review)

---

# Handoff & Thread‑Isolation Discipline (Option‑A)
- **Isolated threads (Echo‑Forward)**  
  1) In **GUIDANCE**: emit `pro_request` (with any `q_patch`).  
  2) In **AUTO**: paste the same YAML **verbatim** and route VERIFY.  
  3) If PASS: route APPLY.  
  4) Optional: AUTO‑READ to confirm.
- **Sequencing**: one route per message; FORM turns output exactly one fenced YAML.

---

# Connector‑Limited Ops Addendum (Pattern B)
If AUTO cannot write to GitHub, the Operator performs **mechanical apply via PR** (Single‑Reader invariant holds):
1) Compute `bank_version` (Git blob SHA).
2) Prepare head branch; unzip seed; stage; commit; push.
3) Open PR (head→base) and merge.
4) Confirm via AUTO‑READ.
5) Continue the governed loop.
