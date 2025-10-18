# PROJECT_INSTRUCTIONS.md — v4.5.2 (Solo Variant) + Handoff Protocol

> **FORM discipline:** Each FORM turn must output **one fenced YAML** with the exact top key shown below.  
> **Thread isolation:** Echo‑forward across threads (Option‑A below).  
> **No numeric quotas:** GUIDANCE may *recommend* ranges, but lints do not enforce counts.

## Conversation roles & handoff map (always the same loop)
1) **AUTO‑READ** snapshots repo truth (inventory, gaps, h/v relations, trace).  
2) **GUIDANCE‑ORG** proposes options in `question_nomination` (plus optional `nucleus_options`).  
3) **SELECT‑ORG** chooses in `selection_decision` (may allow parallel nuclei under the capacity gate).  
4) **GUIDANCE‑ORG** freezes chosen nodes via `pro_request` (`q_patch` writes/updates q‑files).  
5) **AUTO** verifies (`AUTO‑VERIFY`) and applies (`AUTO‑APPLY`).  
6) A tiny PR updates `graph/questions.yaml` with **typed horizontals**.  
7) **AUTO‑READ** confirms the new truth.

**Provenance (handoff metadata):** to keep threads self‑describing without extra prose, forms support an optional `provenance` block. Lints may ignore it; governance uses it for acceptance gates.

---

## clarifier_round (FREE → GUIDANCE‑ORG)
**Purpose:** surface themes & clarifiers; no numeric quotas. Clarifiers remain OPEN/PARKED until frozen.

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
**Purpose:** nominate candidates and, optionally, any number of *nucleus options*. No numeric caps.

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

  nucleus_options:
    - id: "<label>"
      label: "<human title>"
      why:   { id: "<WHY id>",  title: "<interrogative>" }
      whats: [ { id: "<WHAT id>", title: "<interrogative>", depends_on: ["<WHY id>"] }, ... ]
      assumptions: [ { hypothesis: "...", test: "..." }, ... ]
      horizontals_typed:
        - { a: "<id>", with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with }
      system_scenario: [ "step 1", "step 2", "..." ]
```

---

## selection_decision (FREE → SELECT‑ORG)
**Purpose:** choose the next frozen targets (supports parallel nuclei; capacity gate governs). **Typed links are intent‑only here**—they are actually wired later in `graph/questions.yaml`.

```yaml
selection_decision:
  chain_id: <CHAIN_ID>   # optional
  pack_id: <PACK_ID>     # optional
  chosen:
    - id: "<FROZEN bank id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]   # immediate parents only; no cross‑domain jumps
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
  provenance:
    nomination_ref: "<commit/pr/message id of the question_nomination this decision is based on>"
    auto_read_ref:  "<commit sha or share‑bundle id used as the snapshot of truth>"
```

---

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed q_patch
**Purpose:** freeze the chosen nodes by writing/updating q‑files.  
**Rules:** typed links live only in `graph/questions.yaml`; q‑files use **untyped** `cross_links[]`. WHAT/HOW declare `shared_vars[]` when applicable. Include `origin` references—do not copy clarifier text.

```yaml
pro_request:
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate","Assumption Challenge","UX Backcast","Prototype Gate",
               "System Scenario","Coupling Watchlist","Not‑Doing","CCR‑Lite"]
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
          shared_vars: [ value_object ]        # WHAT/HOW as needed
          origin:
            from_clarifiers: [C*]
            assumptions: [A-*]                 # optional: ids from docs/ASSUMPTIONS/register.yaml
            decisions_refs: [D-*]              # optional: ids from docs/DECISIONS/decision_log.yaml
          cross_links: ["<adjacent id>"]       # untyped
          status: FROZEN
  provenance:
    selection_ref: "<commit/pr/message id of the selection_decision>"
```

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

- **Sequencing:** one route per message; FORM turns output **exactly one fenced YAML**.

---

# Connector‑Limited Ops Addendum (Pattern B)

If AUTO cannot write to GitHub, the Operator may perform **mechanical apply via PR** while preserving **Single‑Reader = AUTO**.

## B1) Compute `bank_version` (Git blob SHA)
```bash
git fetch origin
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'
```

## B2) Prepare and push a head branch
```bash
git checkout -B seed/<PACK_ID>-v1 origin/pack/<PACK_ID>
unzip -o ~/Downloads/<seed_zip>.zip -d .
git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q
git commit -m "<PACK_ID>: seed/apply FROZEN nucleus (Option‑A, verified)"
git push -u origin seed/<PACK_ID>-v1
```

## B3) PR: head → base
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
- **No numeric quotas** on nucleus options or clarifiers.
- q‑files are **FROZEN‑only**; bank rows may use `candidate|nucleus|parked|frozen|committed`.
- Capacity gate may allow parallel nuclei per Governance.
