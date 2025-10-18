# PROJECT_INSTRUCTIONS.md — v4.5.1 (Solo Variant) + Non‑Numeric Nucleus Addendum

> **FORM discipline:** Each FORM turn must output **one fenced YAML** with the exact top key shown below.
> **Thread isolation:** Echo‑forward across threads (see Option‑A at the end).

---

## clarifier_round (FREE → GUIDANCE‑ORG)

**Purpose:** surface themes & clarifiers; no numeric quotas.

**Notes**
- `chain_id` is optional (for multi‑pack chains). `pack_id` is kept for legacy compatibility.
- Clarifiers remain OPEN/PARKED until frozen by governance decisions; they are *referenced* by q‑files via `origin.from_clarifiers` but are **not** copied into the q‑file body.

```yaml
clarifier_round:
  chain_id: <CHAIN_ID>             # optional (e.g., melomiraweday0)
  pack_id: <PACK_ID>               # optional legacy (e.g., P-FND-0001)
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

**Purpose:** nominate candidates and, optionally, one or more *nucleus options*.  
**No numeric caps**. Distinctness and dependency clarity matter more than count.

```yaml
question_nomination:
  chain_id: <CHAIN_ID>         # optional
  pack_id: <PACK_ID>           # optional
  level: L0
  review_set: [ ... ]
  candidates: [ { id: "...", title: "...", type: WHY|WHAT|HOW, coverage: 0..1,
                 from_clarifiers: [C*], assumptions: ["A→test"], depends_on: [] }, ... ]
  leftovers: [ "..." ]
  decision: { freeze: true|false, reason: "..." }

  # Optional nucleus bundles (GUIDANCE MAY return any number ≥1)
  nucleus_options:
    - id: "<label>"
      label: "<human title>"
      why:
        id: "<WHY id>"
        title: "<interrogative>"
      whats:
        - { id: "<WHAT id>", title: "<interrogative>", depends_on: ["<WHY id>"] }
      assumptions: [ { hypothesis: "...", test: "..." }, ... ]
      horizontals_typed:
        - { a: "<id>", with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with }
      system_scenario: [ "step 1", "step 2", "..." ]
```

---

## bank_ops (FREE → GUIDANCE‑ORG)

**Purpose:** maintain/edit the bank table in markdown form.

```yaml
bank_ops:
  chain_id: <CHAIN_ID>   # optional
  pack_id: <PACK_ID>     # optional
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
```

**Bank status vocabulary (docs only):** `candidate | nucleus | parked | frozen | committed`.  
**q‑files are FROZEN‑only** (see rules below).

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

## selection_decision (FREE → SELECT‑ORG)

**Purpose:** choose the next frozen targets (supports **parallel nuclei**; capacity gate handled by governance).

```yaml
selection_decision:
  chain_id: <CHAIN_ID>   # optional
  pack_id: <PACK_ID>     # optional
  chosen:
    - id: "<FROZEN bank id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
```

---

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed q_patch

**Purpose:** freeze specific nodes by writing/updating q‑files via `q_patch`.

**Rules that the lints enforce:**
- **Typed links live only in `graph/questions.yaml`.** q‑files use **untyped** `cross_links[]`.
- WHAT/HOW **must** declare `shared_vars[]` when they participate in shared value objects.
- Add provenance inside `origin` (references only). Do not duplicate clarifier text.

```yaml
pro_request:
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate", "Assumption Challenge", "UX Backcast", "Prototype Gate",
               "System Scenario", "Coupling Watchlist", "Not‑Doing", "CCR‑Lite"]
  require:
    shared_vars: true
    typed_cross_links: true          # means "typed links belong in graph/*, not q/*"
    system_scenario: true
  q_patch:
    bank_version: "<sha of docs/FOUNDATIONS/QUESTION_BANK.md>"
    items:
      - id: "<FROZEN id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHAT|WHY|HOW
          title: "<interrogative>"
          depends_on: [ "<WHY id>" ]
          shared_vars: [ value_object ]        # for WHAT/HOW when applicable
          origin:
            from_clarifiers: [C*]              # IDs only
            assumptions: [A-*]                 # optional IDs from the register
            decisions_refs: [D-*]              # optional; decision log entries
          cross_links: ["<adjacent id>"]       # untyped; typed lives in graph/
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

---

## auto_apply (FORM → AUTO)

```yaml
auto_apply:
  pack_id: <PACK_ID>
  applied: true|false
  commit: "<sha or 'local only'>"
  notes: "short"
```

---

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

## B2) Prepare a head branch with your patch
```bash
git checkout -B seed/<PACK_ID>-v1 origin/pack/<PACK_ID>
unzip -o ~/Downloads/<seed_zip>.zip -d .
git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q
git commit -m "<PACK_ID>: seed/apply FROZEN nucleus (Option‑A, verified)"
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

# Rules Recap (lint expectations)
- Typed links **only** in `graph/questions.yaml` via `horizontals_typed`.
- q‑files use **untyped** `cross_links[]`; WHAT/HOW declare `shared_vars[]` when applicable.
- **No numeric quotas** on nucleus options or clarifiers; guidance may recommend ranges, but lints do not enforce counts.
- q‑files are **FROZEN‑only**; bank rows may use `candidate|nucleus|parked|frozen|committed`.
- Capacity gate is governed (see Governance) and may allow parallel nuclei.
