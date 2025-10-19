# PROJECT_INSTRUCTIONS.md — v4.5.2 (Handoff‑Compact, Solo)

**FORM discipline:** every FORM turn outputs **one fenced YAML** whose top key matches the section name.
**Echo‑Forward:** paste the prior YAML verbatim in the receiving thread; then send a one‑line ROUTE macro.

---

## clarifier_round (FREE → GUIDANCE‑ORG)

Purpose: surface themes & clarifiers; no numeric quotas. `chain_id` optional; `pack_id` kept for legacy.

```yaml
clarifier_round:
  chain_id: <CHAIN_ID>     # optional (e.g., melomiraweday0)
  pack_id: <PACK_ID>       # optional legacy (e.g., P-FND-0001)
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

Purpose: nominate candidate nodes and optional **nucleus_options**. No numeric caps.

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
    - id: "<label>"
      label: "<human title>"
      why: { id: "<WHY id>", title: "<interrogative>" }
      whats: [ { id: "<WHAT id>", title: "<interrogative>", depends_on: ["<WHY id>"] } ]
      assumptions: [ { hypothesis: "...", test: "..." }, ... ]
      horizontals_typed: [ { a: "<id>", with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
      system_scenario: [ "step 1", "step 2", "..." ]
```

---

## selection_decision (FREE → SELECT‑ORG)

Purpose: choose the next **FROZEN targets**. Supports **parallel nuclei**. The decision MAY cite which nucleus option(s) it selected.

```yaml
selection_decision:
  chain_id: <CHAIN_ID>   # optional
  pack_id: <PACK_ID>     # optional
  selected_from: ["<nucleus option id>", "..."]  # optional provenance
  chosen:
    - id: "<bank id>"
      tier: WHY|WHAT|HOW
      vertical_parents: ["<id>", "..."]
      horizontals_typed: [ { with: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  rationale: "one line"
```

---

## pro_request (FORM → GUIDANCE pre‑PRO) — may embed q_patch

Purpose: author/modify **q‑files** to freeze the decision. Lints enforce: typed links live in `graph/*` only; q‑files keep **untyped** `cross_links[]`. WHAT/HOW should declare `shared_vars[]` when they use shared value objects. Use `origin` for provenance (references, not full text).

```yaml
pro_request:
  pack_id: <PACK_ID>
  acceptance: ["Simplicity Gate","Assumption Challenge","UX Backcast","Prototype Gate",
               "System Scenario","Coupling Watchlist","Not‑Doing","CCR‑Lite"]
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
          depends_on: ["<WHY id>"]
          shared_vars: [ value_object ]     # WHAT/HOW when applicable
          origin:
            from_clarifiers: [C*]
            assumptions: [A-*]              # optional IDs from register
            decisions_refs: [D-*]           # optional; decisions log
          cross_links: ["<adjacent id>"]    # untyped only
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

## auto_apply (FORM → AUTO) — **ledger only**

AUTO never pushes code in connector‑limited setups. Use PRs. After merge, AUTO records what happened.

```yaml
auto_apply:
  pack_id: <PACK_ID>
  applied: true|false
  mode: operator|connector
  commit: "<merge sha or 'local only'>"
  notes: "short"
```

---

## auto_response (FORM → AUTO‑READ)

```yaml
auto_response:
  pack_id: <PACK_ID>
  repo_state: empty|seeded
  repo_inventory: [ "paths..." ]
  gaps: [ "missing vs governance..." ]
  share_list: [ "files..." ]
  h_relations: [ { a: "<id>", b: "<id>", type: informs|depends|conflicts|risks_with|shares_var_with } ]
  v_relations: [ { parent: "<WHY|WHAT id>", child: "<WHAT|HOW id>" } ]
  trace_map: { "<id>": { files: [ "..." ], dependents: [ "..." ] } }
  scaffold_needed: false
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

### Echo‑Forward Contract (strict)

1) Post the prior YAML **verbatim** in the receiving thread.  
2) Immediately send the one‑line ROUTE macro.  
3) The receiver replies with its own FORM YAML.  
4) Operator performs PRs when needed (Pattern‑B), then echoes `auto_apply` (mode: operator).

### Rules Recap (lints expect)

- Typed links only in `graph/questions.yaml` (`horizontals_typed`).  
- q‑files: untyped `cross_links[]`; WHAT/HOW add `shared_vars[]` when applicable.  
- No numeric quotas on nuclei/clarifiers.  
- q‑files are **FROZEN‑only**; bank rows may be `candidate|nucleus|parked|frozen|committed`.  
- Single‑Reader: only **AUTO** reads repo; other threads rely on **share_list** and echo‑forward.
