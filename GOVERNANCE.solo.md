# GOVERNANCE.solo.md — v4.4 (Solo, Option‑A) + Chain‑Centric Additions

## Modes & Roles (unchanged rails)
- **GUIDANCE‑ORG (FREE)**: L0 Root‑Finder; clarifiers only; freeze when coverage ≥0.70 and no OPEN clarifiers.
- **SELECT‑ORG (FREE)**: Chooses which **FROZEN** question(s) to implement next; emits `selection_decision`.
- **GUIDANCE (FORM) pre‑PRO**: Emits `pro_request` (may include `q_patch`) for **FROZEN** items.
- **AUTO‑READ / VERIFY / APPLY (FORM)**: Single‑Reader, validation, and mechanical apply.
- **PRO‑EVAL (ADVISORY)**: Non‑writing evaluation.

## Evidence & FORM Discipline
- FREE: abstraction‑only; avoid numbers/dates/names/choice verbs.
- FORM: EXACTLY one fenced YAML per turn.
- Allowed typed links: `shares_var_with | informs | depends | conflicts | risks_with`.
- ≥1 System Scenario must cross ≥2 branches.

## Chain‑Centric Rules
1) **No‑Jump verticals**: a WHAT/HOW can only depend on its direct parent WHY/WHAT. Multi‑level reasoning belongs in the graph, not in `depends_on` lists.
2) **Typed links live in the graph** (`graph/questions.yaml`). Q‑files use **untyped** `cross_links` only.
3) **shared_vars required** on all WHAT/HOW. Use shared vars to couple operational artifacts across branches.
4) **Context continuity**: each q‑file should carry `assumptions[]`, `risks[]`, and `context_refs[]` so decisions survive across cycles.
5) **Searchability**: keep `dist/search_index.json` and `dist/question_matrix.csv` fresh so conversations can query the chain.

## Pack Envelope
`packs/<PACK_ID>/envelope.yaml` pointers are updated on APPLY (bank/blob, graph/blob, verify/apply logs, share bundle hashes).

## Single‑Reader Invariant (Option‑A)
- AUTO is the only live repo reader. Other modes do not read the repo; they rely on AUTO output.

## Appendix A — Connector‑Limited (Pattern B)
- Echo‑Forward is mandatory (paste the same `pro_request` into AUTO before VERIFY).
- Manual Apply via PR is allowed; base=`pack/<PACK_ID>`; verify a diff exists before PR.
- `q_patch.bank_version` must equal the Git blob SHA of `docs/FOUNDATIONS/QUESTION_BANK.md`.
- `trace_map` must list Bank, graph, and q/<id>.yaml per question id.
- macOS/zsh hygiene: quote globs; avoid inline `#` comments when pasting multi‑line command blocks.

## Control‑Node Selection (advisory)
Pick a **minimal nucleus** of WHY nodes first (market value, safety baseline, scoreboard, ICP, workflow, positioning, channel), then 3–4 WHATs that operationalize them. Use `selection_decision` to freeze the next slice.
