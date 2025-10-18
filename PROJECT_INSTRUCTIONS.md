# PROJECT_INSTRUCTIONS.md — v4.5.1 (Solo) + Non‑Numeric Nucleus Addendum

> **FORM discipline:** each FORM turn outputs **one fenced YAML** with the exact top key.
> **Thread isolation:** echo‑forward across threads (Option‑A).

---

## clarifier_round (FREE → GUIDANCE‑ORG)

**Purpose:** surface themes & clarifiers; **no numeric quotas**.

**Notes**
- `chain_id` optional; `pack_id` optional (legacy).
- Clarifiers stay OPEN/PARKED until governance freezes them; q‑files may **reference** clarifier IDs in `origin.from_clarifiers` but do not copy text.

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
  coverage: { estimated_fraction: 0..1 }
  decision: { freeze_clarifiers: true|false, reason: "..." }
```

---

## question_nomination (FREE → GUIDANCE‑ORG)

**Purpose:** nominate candidates and optional *nucleus options*. **No quotas**; clarity > count.

```yaml
question_nomination:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  level: L0
  review_set: [ ... ]
  candidates: [ { id: "...", title: "...", type: WHY|WHAT|HOW, coverage: 0..1,
                 from_clarifiers: [C*], assumptions: ["A→test"], depends_on: [] }, ... ]
  leftovers: [ "..." ]
  decision: { freeze: true|false, reason: "..." }

  nucleus_options:
    - id: "<label>"
      label: "<human title>"
      why: { id: "<WHY id>", title: "<interrogative>" }
      whats:
        - { id: "<WHAT id>", title: "<interrogative>", depends_on: ["<WHY id>"] }
      assumptions: [ { hypothesis: "...", test: "..." }, ... ]
      horizontals_typed:
        - { a: "<id>", with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with }
      system_scenario: [ "step 1", "step 2", "..." ]
```

---

## bank_ops (FREE → GUIDANCE‑ORG)

**Purpose:** maintain/edit the bank table (markdown).

```yaml
bank_ops:
  chain_id: <CHAIN_ID>
  pack_id: <PACK_ID>
  rows_md: |
    | id | title | tier | domain | status | depends_on | source | micro‑WWH |
    |---|---|---|---|---|---|---|---|
```

**Bank status (docs only):** `candidate | nucleus | parked | frozen | committed`.  
**q‑files are FROZEN‑only**.

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

**Purpose:** pick next frozen targets (supports **parallel nuclei**; capacity gate in governance).

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

---

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed q_patch

**Purpose:** freeze nodes by writing/updating q‑files via `q_patch`.

**Lint rules (short):**
- **Typed links →** only `graph/questions.yaml`.
- q‑files use **untyped** `cross_links[]`.
- WHAT/HOW declare `shared_vars[]` when applicable.
- Put provenance as IDs in `origin.*` (no copied text).

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
    bank_version: "<sha of docs/FOUNDATIONS/QUESTION_BANK.md>"
    items:
      - id: "<FROZEN id>"
        path: "q/<id>.yaml"
        body: |
          id: <id>
          tier: WHAT|WHY|HOW
          title: "<interrogative>"
          depends_on: [ "<WHY id>" ]
          shared_vars: [ value_object ]
          origin:
            from_clarifiers: [C*]
            assumptions: [A-*]
            decisions_refs: [D-*]
          cross_links: ["<adjacent id>"]
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

# Handoff & Thread‑Isolation (Option‑A)

1) In **GUIDANCE**: emit `pro_request` (with any `q_patch`).  
2) In **AUTO**: paste that YAML **verbatim**.  
3) Route: `ROUTE → AUTO (FORM) … task=AUTO‑VERIFY`.  
4) If PASS: `ROUTE → AUTO (FORM) … task=AUTO‑APPLY`.  
5) Optional: `AUTO‑READ` to confirm repo truth.

**Sequencing:** one route per message; each FORM turn = one fenced YAML.

---

# Connector‑Limited Ops (Pattern B)

If AUTO can’t write to GitHub, do a short‑lived PR while keeping Single‑Reader = AUTO.

## B1) Get `bank_version`
```bash
git fetch origin
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'
```

## B2) Prepare a head branch
```bash
git checkout -B seed/<PACK_ID>-v1 origin/pack/<PACK_ID>
unzip -o ~/Downloads/<seed_zip>.zip -d .
git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q
git commit -m "<PACK_ID>: seed/apply FROZEN nucleus"
git push -u origin seed/<PACK_ID>-v1
```

## B3) PR (head → base), then merge
- base: `pack/<PACK_ID>`
- head: `seed/<PACK_ID>-v1`

## B4) Confirm via Single‑Reader
```
ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)
```

## B5) Governed loop
**SELECT‑ORG** → **GUIDANCE: pro_request** → **AUTO‑VERIFY** → **AUTO‑APPLY**.

---

# Rules Recap (what lints expect)
- Typed links **only** in `graph/questions.yaml`.
- q‑files: **untyped** `cross_links[]`; WHAT/HOW add `shared_vars[]` when relevant.
- **No numeric quotas** on nucleus options or clarifiers.
- q‑files are **FROZEN‑only**; bank rows use `candidate|nucleus|parked|frozen|committed`.
- Capacity gate may allow **parallel nuclei**.
