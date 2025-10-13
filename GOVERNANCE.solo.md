# GOVERNANCE.solo.md — v4.2 (Solo Variant, Option A)

## Modes & Roles
- **GUIDANCE‑ORG (FREE)**: L0 Root‑Finder; clarifiers only. Freeze when **coverage ≥ 0.70** and **no OPEN** clarifiers.
- **AUTO‑READ (FORM)**: The **only live repo reader**. Returns `auto_response` with `repo_inventory`, `gaps`, `share_list`, `h_relations`, `v_relations`, `trace_map`.
- **SELECT‑ORG (FREE)**: Chooses which **FROZEN** question(s) to implement next; emits `selection_decision`.
- **GUIDANCE (FORM) pre‑PRO**: Emits `pro_request` and **may include `q_patch`** (full file bodies) for **FROZEN** items.
- **AUTO‑VERIFY (FORM)**: Validates `q_patch` via lints: Bank Integrity, No‑Skip (WHY→WHAT→HOW), Typed Links, Graph Completeness, System Scenario (≥2 branches). Emits `auto_verify: PASS|FAIL`.
- **AUTO‑APPLY (FORM)**: Applies patch if verification passes; updates Pack Envelope.
- **PRO‑EVAL (ADVISORY)**: Non‑writing evaluation; suggests solutions or new questions; outputs feed GUIDANCE‑ORG.

## Acceptance Gates
- **Simplicity**, **Assumption Challenge**, **UX Backcast** (≥1 System Scenario across ≥2 branches),
  **Prototype**, **Coupling Watchlist**, **Not‑Doing**, **CCR‑Lite** (at pack close).

## Bank Discipline
- Bank capture home: `docs/FOUNDATIONS/QUESTION_BANK.md`.
- `q/*` files are introduced via **q_patch** and applied only after **AUTO‑VERIFY PASS** (Option A).

## Evidence & Hygiene
- FREE: abstraction‑only; no numbers, dates, named entities, or choice verbs.
- FORM: exactly **one fenced YAML** output per turn.
- Router Preamble on evaluation threads (ID, direct_deps, Principle/Constraint/Measure status).

## Graph & Links
- `graph/questions.yaml` is **required** before any `q_patch` passes verification.
- Allowed typed edges: `shares_var_with | informs | depends | conflicts | risks_with`.

## Pack Envelope (Required)
`packs/<PACK_ID>/envelope.yaml` carries pointers to the latest Bank, auto artifacts, selections, requests, verifications, applies, and graph.
