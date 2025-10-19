# GOVERNANCE.solo.md — v4.5.2-mini

**Goal:** keep the loop tight, objective, and auditable. This file defines roles, gates, pins, and enforcement.

---

## Roles
- **GUIDANCE‑ORG (FREE):** explore, structure, and nominate (`clarifier_round`, `question_nomination`, `bank_ops`). No merges.
- **SELECT‑ORG (FREE):** decide *which* nominated nodes move next → emit **`selection_decision`** with pins. No debates.
- **GUIDANCE (pre‑PRO, FORM):** turn selections into **`pro_request`** with `q_patch` (FROZEN q‑files).
- **AUTO (FORM):** single reader/enforcer → `AUTO‑VERIFY` then `AUTO‑APPLY` and optional `AUTO‑READ`.
- **Operator:** runs zsh‑safe PRs when connectors can’t write. Does not change content.

---

## Pins & Provenance (required in `selection_decision`)
- `bank_version`: blob SHA of `docs/FOUNDATIONS/QUESTION_BANK.md` on base.
- `auto_read_sha`: the commit used for the last `AUTO‑READ`.
- `nomination_ref`: repo path that stores the nomination/clarifier YAML you reference.

**How to get them:**
```bash
git fetch origin
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'  # bank_version
# auto_read_sha: copy from your last AUTO-READ console (the commit shown)
# nomination_ref: path of the YAML checked into docs/GUIDANCE/... or similar
```

Store pins in the envelope (optional) and repeat them in `selection_decision` for traceability.

---

## Acceptance Gates (checked before `q_patch` is accepted)
- **Simplicity Gate:** each node is one clear question; no bundles.
- **Assumption Challenge:** key assumptions listed + test ideas exist.
- **UX Backcast:** what the user/stakeholder sees at success.
- **Prototype Gate:** minimal artifact or sample path is plausible.
- **System Scenario:** the chosen nodes can be walked end‑to‑end.
- **Coupling Watchlist:** risky coupling documented.
- **Not‑Doing:** explicit out‑of‑scope statement.
- **CCR‑Lite:** copy/compliance review for wording and claims.

---

## Policy
- **Typed links live only in `graph/questions.yaml`.**  
  q‑files carry **untyped** `cross_links[]`.  
  WHAT/HOW declare `shared_vars[]` when they share a value object.
- **q‑files are FROZEN‑only.** Bank rows carry other states.
- **No‑Skip:** any WHAT/HOW must have a direct WHY parent.
- **Freeze windows:** changes outside weekly window require reopening with reason.
- **Capacity gate:** default 1 nucleus in flight; may allow 2 when non‑contending (document why).
- **Decision & Assumption registers:** use `docs/DECISIONS/*` and `docs/ASSUMPTIONS/register.yaml`; reference IDs in `origin.*` inside q‑files.
- **Single‑Reader AUTO:** AUTO remains the only reader for repo truth; operator PRs keep that invariant.

---

## Enforcement & Lints
- `tools/validate_question_chain.py`: graph completeness, no‑skip, typed‑link boundaries, shared_vars.
- `tools/build_question_index.py`: builds a search index for GUIDANCE use.
- CI or local scripts can run: `scripts/run_index_build.sh` and a lints runner.

---

## Router Discipline (Echo‑Forward)
- Each thread carries **one FORM** and a **route line** when handing off. Example:
  - `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>` with a `selection_decision` YAML.
  - `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pro_request`
  - `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY` then `AUTO‑APPLY`.
- SELECT‑ORG does **not** debate content; it decides and pins.
