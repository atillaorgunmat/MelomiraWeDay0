# GOVERNANCE.solo.md — v4.5.1 (Solo) — Quota‑Free Nucleus & Capacity Gate

This governance file defines roles, gates, and hygiene for the Solo (Option‑A) loop.
It removes numeric quotas (e.g., “exactly 2–3 nucleus options”) in favor of **logic‑first** evaluation.
Capacity is governed explicitly rather than implied by counts.

---

## Roles & Separation
- **GUIDANCE‑ORG (FREE):** clarifiers, nominations, nucleus proposals; prepares `pro_request` with any `q_patch`.
- **SELECT‑ORG (FREE):** chooses the next FROZEN targets (may be multiple nuclei in parallel, within capacity).
- **AUTO (FORM):** Single‑Reader of the live repo; runs VERIFY/APPLY/READ; never authors content.
- **Operator Console:** routes threads; enforces FORM fencing and one‑route‑per‑message.
- **PRO (pre‑PRO inside GUIDANCE FORM):** used to hand q_patches into AUTO; no direct repo writes when connectors are limited.

---

## Acceptance Gates (evaluated during `pro_request`)
- **Simplicity Gate:** nodes have one clear interrogative title; direct dependencies only (No‑Skip).
- **Assumption Challenge:** key hypotheses are visible and testable (may reference `docs/ASSUMPTIONS/register.yaml` A‑IDs).
- **System Scenario:** at least one scenario walks across ≥2 branches when meaningful (temporary single‑branch allowed at Day‑0).
- **Coupling Watchlist:** avoid hidden coupling; use typed horizontals in `graph/questions.yaml` only.
- **UX Backcast / Prototype Gate / Not‑Doing / CCR‑Lite:** apply as relevant; documentation lives in `docs/DECISIONS/` as needed.

---

## Typed Links Policy (strict)
- **Typed horizontals** (`informs|depends|conflicts|risks_with|shares_var_with`) are defined **only** in `graph/questions.yaml`.
- **q‑files must not contain typed links**. They may reference neighbors via **untyped** `cross_links[]`.
- WHAT/HOW nodes that share value objects must declare `shared_vars[]` in their q‑files.

---

## Bank vs q‑files — Status Model
- **Bank rows** may use: `candidate | nucleus | parked | frozen | committed`.
- **q‑files are FROZEN‑only.** Nucleus evaluation happens in the bank (and GUIDANCE threads), not in q‑files.

---

## Nucleus Proposals (quota‑free)
- GUIDANCE may nominate **one or more** nucleus options. Distinctness, dependency clarity, and risk‑reduction value are the review criteria.
- Parallel nuclei are allowed only within the **capacity gate** (see below).

---

## Capacity Gate
- Capacity is explicit. Default policy: **up to 2 nuclei in parallel**.
- Operators may adjust capacity in tooling (e.g., `tools/validation_config.yaml`) or state it in the `selection_decision` rationale.
- Selection that exceeds capacity must PARK excess nuclei or split across cycles.

---

## No‑Skip Rule (dependency hygiene)
- Every WHAT/HOW must list its **direct** parents in `depends_on`.
- Vertical edges are mirrored in `graph/questions.yaml` and checked during VERIFY.

---

## Provenance & Decisions (lightweight)
- q‑files carry **references** to clarifiers/assumptions/decisions via the `origin` block:
  - `origin.from_clarifiers: [C-*]`
  - `origin.assumptions: [A-*]`
  - `origin.decisions_refs: [D-*]`
- Assumptions live in `docs/ASSUMPTIONS/register.yaml` (append‑only log with status).
- Decisions live in `docs/DECISIONS/decision_log.yaml` (append‑only; cross‑reference node IDs).

---

## Option‑A (Echo‑Forward) Discipline
1) GUIDANCE prepares `pro_request` (with any `q_patch`).  
2) AUTO receives the **same YAML verbatim**: route `AUTO‑VERIFY` → `AUTO‑APPLY`.  
3) Optional `AUTO‑READ` confirms truth.  
4) One route per message; each FORM turn outputs **exactly one** fenced YAML.

---

## Pattern‑B (Connector‑Limited) Apply
- When AUTO cannot write, Operators perform a short‑lived PR using the provided commands in the instructions.
- `q_patch.bank_version` MUST use the Git blob SHA of `docs/FOUNDATIONS/QUESTION_BANK.md` on the base branch.
- On lint FAIL: copy `expected_sha` from AUTO and re‑run with the corrected value.

---

## Lint Expectations (summary)
- **Typed link locations:** typed only in `graph/*`; q‑files use `cross_links[]`.
- **Shared vars:** WHAT/HOW declare `shared_vars[]` when applicable.
- **System scenario:** present for the selection; crosses branches when meaningful.
- **Counts:** no numeric quotas enforced by governance.
