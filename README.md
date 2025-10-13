# MelomiraWeDay0 — Day‑0 Foundations

This repository is scaffolded for a **solo‑user** methodology using **Option A**:

- **GUIDANCE (FORM)** *authors* the content (e.g., `q/*`) as a **`q_patch`**.
- **AUTO‑VERIFY (FORM)** *validates* the patch (Bank Integrity, No‑Skip, Typed Links, System Scenario).
- **AUTO‑APPLY (FORM)** *applies* the patch (mechanical merge).
- **PRO‑EVAL (advisory)** evaluates options and spins out new questions (non‑writing).

Other key principles:
- **Single‑Reader policy**: only AUTO reads the live repo; other modes work from AUTO’s **share bundle**.
- **Graph‑as‑code**: `graph/questions.yaml` is **required** before any `q_patch` can pass verification.
- **Typed cross‑links**: allowed edge types → `shares_var_with | informs | depends | conflicts | risks_with`.
- **System Scenario**: ≥1 scenario must cross ≥2 branches per pack (UX Backcast gate).
- **FORM discipline**: every FORM turn returns exactly **one fenced YAML** block (no extra prose).

See `GOVERNANCE.solo.md` and `PROJECT_INSTRUCTIONS.md` for full details.
