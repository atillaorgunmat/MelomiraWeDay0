# GOVERNANCE.solo.md — v4.3 (Solo, Option A) + Appendix: Connector‑Limited Environments

## Modes & Roles
- **GUIDANCE‑ORG (FREE)**: L0 Root‑Finder; clarifiers only. Freeze when coverage ≥ 0.70 and no OPEN clarifiers.
- **AUTO‑READ (FORM)**: The **only live repo reader**; returns `auto_response` with repo_inventory, gaps, share_list, h/v relations, trace_map.
- **SELECT‑ORG (FREE)**: Chooses which **FROZEN** question(s) to implement next; emits `selection_decision` (parents + typed horizontals).
- **GUIDANCE (FORM) pre‑PRO**: Emits `pro_request` (may include `q_patch`) for **FROZEN** items.
- **AUTO‑VERIFY (FORM)**: Validates `q_patch` (Bank Integrity; No‑Skip; Typed Links in graph; Graph Completeness; System Scenario across ≥2 branches).
- **AUTO‑APPLY (FORM)**: Applies patch if PASS; updates Pack Envelope and may emit share bundle.
- **PRO‑EVAL (ADVISORY)**: Non‑writing evaluation and option‑eering; capture narrative in `docs/DECISIONS/<ID>.md`.

## Evidence & FORM Discipline
- FREE: abstraction‑only; no numbers, dates, named entities, or choice verbs.
- FORM: output is **one fenced YAML** per turn.
- Allowed typed links: `shares_var_with | informs | depends | conflicts | risks_with`.
- ≥1 System Scenario must cross ≥2 branches in the pack.
- **ASCII hyphens are canonical** for pack ids/branches to avoid look‑alikes.

## Bank, Graph, Q‑files
- Bank capture home: `docs/FOUNDATIONS/QUESTION_BANK.md`.
- `graph/questions.yaml` holds **typed** link semantics and shared_var dictionaries.
- `q/*` files must include **untyped** `cross_links: [...]` and (for WHAT/HOW) `shared_vars: [...]` aligned to the graph.
- `q/*` are introduced via **q_patch** and applied after **AUTO‑VERIFY PASS**.

## Pack Envelope (required)
`packs/<PACK_ID>/envelope.yaml` points to latest Bank, auto artifacts, selections, requests, verifications, applies, graph.

---

## Appendix A — Connector‑Limited Environment (Pattern B)

1. **Echo‑Forward remains mandatory**: paste the exact `pro_request` YAML from GUIDANCE into AUTO before VERIFY.
2. **Manual Apply via PR (Operator)**:
   - Create a short‑lived head branch with the verified `q_patch` content.
   - Open PR with **base** = `pack/<PACK_ID>`, **head** = `<head-branch>`.
   - Merge PR in the UI to land changes on the **base**.
   - Optional: run `tools/make_share_bundle.py` locally and commit `dist/`, or leave it to the next AUTO‑APPLY.
3. **Single‑Reader invariant holds**: Confirm repository state with **AUTO‑READ** only.
4. **Bank Integrity handshake**:
   - `q_patch.bank_version` must equal the Git **blob SHA** of `docs/FOUNDATIONS/QUESTION_BANK.md`.
   - On FAIL, use AUTO’s `expected_sha` in a re‑emit and re‑VERIFY.
5. **Trace map expectations**:
   - For each ID, `files` includes Bank, Graph, and its `q/<id>.yaml`.
   - `dependents` includes vertical children and typed‑linked peers.
6. **Branch hygiene**:
   - Base is `pack/<PACK_ID>`; avoid “No commits between …” by verifying a diff before opening a PR.
7. **macOS noise & zsh quirks**:
   - Keep `.DS_Store` ignored; quote globs or stage by folders.
