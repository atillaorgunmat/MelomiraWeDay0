# GOVERNANCE.solo.md — v4.5 (Solo, Option‑A) — Single‑Bank + Assumption Wiring

## Roles & Threads
- **GUIDANCE‑ORG (FREE)**: explores clarifiers, nominates questions, harvests assumptions, proposes nucleus.
- **SELECT‑ORG (FREE)**: freezes a tiny nucleus (2–3 nodes) with explicit parents and typed horizontals.
- **PRO (FORM)**: authors `pro_request` + `q_patch` bodies meeting acceptance gates.
- **AUTO (FORM)**: single reader of the repo; VERIFY/APPLY; echoes back `auto_response`.

## Bank Policy (Single‑Bank)
- `docs/FOUNDATIONS/QUESTION_BANK.md` is the only table of questions. Allowed `status` values:
  - `CANDIDATE`: discussed, not yet selected.
  - `FROZEN`: accepted and represented by q/* and graph.
  - `PARKED`: intentionally paused; not in graph.
  - `REOPENED`: previously frozen; now under change.
  - `RETIRED`: no longer pursued.
- `graph/questions.yaml` contains **only** `FROZEN` ids. Lints enforce alignment.

## Chain Rules
- Exactly **one** WHY parent for each WHAT/HOW (`depends_on: ["<WHY>"]`). Other influences are **typed horizontals** in the graph.
- q/* for FROZEN items only. WHAT/HOW must include:
  - `origin.from_clarifiers` (≤2 ids),
  - `shared_vars`, `cross_links` (untyped),
  - `assumptions[]` referencing the Register,
  - `context_refs[]`.
- Typed edge semantics (`informs`, `depends`, `conflicts`, `risks_with`, `shares_var_with`) live only in the graph.

## Assumption Register
- Canonical file: `docs/ASSUMPTIONS/register.yaml`.
- Item: `{id,text,status,source,related_ids,test}` with statuses `open|in_test|passed|failed|rejected`.
- Any `A-*` referenced in q/* must exist in the Register (VERIFY enforces).

## Reopen Triggers
- Safety incident; legal change; failed assumption; material capacity breach; or partner rejection pattern.
- When triggered, set affected q/* to `REOPENED` in the Bank, log via `decision_log_ops`, and run a small nucleus cycle.

## Option‑A Discipline
- Echo‑Forward the exact `pro_request` into AUTO.
- One route per message. FORM turns output exactly one fenced YAML.

## Acceptance Gates (lite)
- **Simplicity Gate**: single WHY parent; ≤2 clarifier IDs; ≤7 fields in q/* body.
- **Assumption Challenge**: each WHAT/HOW references ≥1 assumption with a test.
- **UX Backcast**: 3–5 step usage path exists.
- **Prototype Gate**: if relevant, a stub pilot or rubric exists.
- **System Scenario**: at least one scenario crosses ≥2 branches.
- **Typed Link Hygiene**: typed links only in graph; untyped only in q/*.

## Operator Expectations
- Provide paste‑ready ROUTE lines; short‑lived PRs; confirm via AUTO‑READ.
- Never mix content authoring with governance in the same message.
