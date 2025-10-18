# ops_README.md — v4.5.1 (Operator Flow)

**Goal:** Make the chain flow deterministic and light‑touch.

## Daily Loop
1) **GUIDANCE‑ORG**: run `clarifier_round` (no quotas).
2) **GUIDANCE‑ORG**: run `question_nomination` and request **nucleus options**.
3) **SELECT‑ORG**: choose targets via `selection_decision` (capacity may allow 2 in parallel).
4) **GUIDANCE‑ORG**: produce `pro_request` (with optional `q_patch` for q‑files).
5) **AUTO**: `AUTO‑VERIFY` → `AUTO‑APPLY`. If write is blocked, use **Pattern B** PR.
6) **AUTO**: `AUTO‑READ` to confirm repository truth.
7) **Operator**: build `dist/share_bundle.zip` (if needed) with `tools/make_share_bundle.py`.

## Branching (Pattern B)
- Always start from `origin/pack/<PACK_ID>`; use short‑lived topic branches.
- Ensure remote‑vs‑remote diff is non‑empty before PR to avoid “no commits between” warnings.

## Hygiene Highlights
- Typed links only in graph; q‑files use untyped `cross_links` and declare `shared_vars` for WHAT/HOW.
- q‑files are **FROZEN‑only**; bank status may be candidate/nucleus/parked/frozen/committed.
- Provenance by reference (`origin.from_clarifiers`, optional `assumptions`, `decisions_refs`).

## Capacity Gate
- Default single nucleus; governance may authorize two in parallel when coupling is low and cycle time/QA allow.
