# PROJECT_INSTRUCTIONS.md — v4.2 (Solo Variant) + Connector‑Limited Ops Addendum

Each FORM turn must output **one fenced YAML** with the exact top key shown below.

## clarifier_round (FREE → GUIDANCE‑ORG)
```yaml
clarifier_round:
  pack_id: <PACK_ID>
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
  pack_id: <PACK_ID>
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
  pack_id: <PACK_ID>
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
```

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

## selection_decision (FREE → SELECT‑ORG)
```yaml
selection_decision:
  pack_id: <PACK_ID>
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
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate", "Assumption Challenge", "UX Backcast", "Prototype Gate",
               "System Scenario", "Coupling Watchlist", "Not‑Doing", "CCR‑Lite"]
  require:
    shared_vars: true
    typed_cross_links: true
    system_scenario: true
  q_patch:
    bank_version: "<sha of QUESTION_BANK.md>"
    items:
      - id: "<FROZEN id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHAT
          depends_on: [ "<WHY id>" ]
          shared_vars: [ value_object ]
          cross_links_typed:
            - { with: "<adjacent id>", type: risks_with }
          status: FROZEN
```

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

# Handoff & Thread‑Isolation Discipline (Option‑A)

- **Isolated threads (Echo‑Forward)**  
  1) In **GUIDANCE** thread: emit the `pro_request` (with any `q_patch`).  
  2) In **AUTO** thread: paste that same YAML **verbatim**.  
  3) Send the route line: `ROUTE → AUTO (FORM) … task=AUTO‑VERIFY`.  
  4) If PASS, send: `ROUTE → AUTO (FORM) … task=AUTO‑APPLY`.  
  5) Optional: `AUTO‑READ` to confirm inventory/gaps/share_list/relations/trace.

- **Sequencing**: one route per message; FORM turns output **exactly one fenced YAML**.

---

# Connector‑Limited Ops Addendum (Pattern B)

If AUTO cannot write to GitHub, the Operator may perform **mechanical apply via PR** while preserving **Single‑Reader = AUTO**:

## B1) Compute `bank_version` (Git blob SHA)
```bash
git fetch origin
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'
# Use this 40‑hex value in q_patch.bank_version
```

## B2) Prepare the seed on a head branch
```bash
git checkout -B seed/<PACK_ID>-v1 origin/pack/<PACK_ID>
unzip -o ~/Downloads/<seed_zip>.zip -d .
git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q
git commit -m "<PACK_ID>: seed FROZEN nucleus (Option‑A, verified)"
git push -u origin seed/<PACK_ID>-v1
```

## B3) Open PR (head → base) and merge
- base: `pack/<PACK_ID>`
- head: `seed/<PACK_ID>-v1`

## B4) Confirm via Single‑Reader
```
ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)
```

## B5) Continue governed loop
- **SELECT‑ORG** → **GUIDANCE: pro_request** → **AUTO‑VERIFY** → **AUTO‑APPLY**.

---

# Operator Route Macros (paste‑ready)

- To AUTO‑READ:  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`

- To GUIDANCE (pre‑PRO):  
  `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pre‑PRO pro_request (may include q_patch)`

- To AUTO‑VERIFY:  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY`

- To AUTO‑APPLY:  
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY`

- To SELECT‑ORG:  
  `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>`
