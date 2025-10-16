# GOVERNANCE.solo.md — v4.2 (Solo, Option A) + Appendix: Connector‑Limited Environments

## Modes & Roles
- **GUIDANCE‑ORG (FREE)**: L0 Root‑Finder; clarifiers only. Freeze when coverage ≥ 0.70 and no OPEN clarifiers.
- **AUTO‑READ (FORM)**: The **only live repo reader**; returns `auto_response` with repo_inventory, gaps, share_list, h/v relations, trace_map.
- **SELECT‑ORG (FREE)**: Chooses which **FROZEN** question(s) to implement next; emits `selection_decision`.
- **GUIDANCE (FORM) pre‑PRO**: Emits `pro_request` (may include `q_patch`) for **FROZEN** items.
- **AUTO‑VERIFY (FORM)**: Validates `q_patch` (Bank Integrity; No‑Skip; Typed Links; Graph Completeness; System Scenario across ≥2 branches).
- **AUTO‑APPLY (FORM)**: Applies patch if PASS; updates Pack Envelope and may emit share bundle.
- **PRO‑EVAL (ADVISORY)**: Non‑writing evaluation.

## Evidence & FORM Discipline
- FREE: abstraction‑only; no numbers, dates, named entities, or choice verbs.
- FORM: output is **one fenced YAML** per turn.
- Allowed typed links: `shares_var_with | informs | depends | conflicts | risks_with`.
- ≥1 System Scenario must cross ≥2 branches in the pack.

## Bank & Graph
- Bank capture home: `docs/FOUNDATIONS/QUESTION_BANK.md`.
- `q/*` files are introduced via **q_patch** and applied only after **AUTO‑VERIFY PASS**.
- `graph/questions.yaml` is required before any `q_patch` passes.

## Pack Envelope (required)
`packs/<PACK_ID>/envelope.yaml` points to latest Bank, auto artifacts, selections, requests, verifications, applies, graph.

---

## Appendix A — Connector‑Limited Environment (Pattern B)

When the AUTO connector cannot write repo content:

1. **Echo‑Forward remains mandatory**: paste the exact `pro_request` YAML from GUIDANCE into AUTO before VERIFY.
2. **Manual Apply via PR (Operator)** — allowed mechanical steps:
   - Create a short‑lived head branch with the verified `q_patch` content.
   - Open PR with **base** = `pack/<PACK_ID>`, **head** = `<head-branch>`.
   - Merge PR in the UI to land changes on the **base**.
   - Optional: run `tools/make_share_bundle.py` locally and commit `dist/`, or leave it to the next AUTO‑APPLY.
3. **Single‑Reader invariant holds**: Only **AUTO‑READ** is used to confirm repository state; other modes do not read the repo.
4. **Bank Integrity handshake**:
   - `q_patch.bank_version` must equal the Git **blob SHA** of `docs/FOUNDATIONS/QUESTION_BANK.md`.
   - If VERIFY fails on bank_integrity, AUTO should return `expected_sha`; Operator re‑emits with that value.
5. **Trace map expectations**:
   - For each ID, `files` includes: `docs/FOUNDATIONS/QUESTION_BANK.md`, `graph/questions.yaml`, and `q/<id>.yaml`.
   - `dependents` includes vertical children and typed‑linked peers.
6. **Branch hygiene**:
   - Do not target `main` if the canonical base is `pack/<PACK_ID>`.
   - Avoid “No commits between …” by verifying a diff before opening a PR:
     ```bash
     git fetch origin
     git diff --name-status origin/pack/<PACK_ID>..origin/<head-branch>
     ```
7. **macOS noise & zsh quirks**:
   - Add `.DS_Store` to `.gitignore`; remove stray files with `find . -name ".DS_Store" -print -delete`.
   - Quote globs in zsh (`"q/*.yaml"`) or stage by directories (`git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q`).

---

## Canonical Route Order (Option A)

1) GUIDANCE‑ORG (FREE): `clarifier_round` → `question_nomination` → `bank_ops` (tables).  
2) AUTO‑READ (FORM) to snapshot repo.  
3) SELECT‑ORG (FREE): choose FROZEN question(s).  
4) GUIDANCE (FORM): `pro_request` (may include `q_patch`).  
5) AUTO‑VERIFY (FORM).  
6) AUTO‑APPLY (FORM).  
7) Optional AUTO‑READ (FORM) to confirm envelope/share bundle.
