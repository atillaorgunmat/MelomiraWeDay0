# audit_checklists.md — v4.5

## Chain Assimilation (per nucleus cycle)
- [ ] QUESTION_BANK.md uses only allowed statuses; new items inserted as CANDIDATE.
- [ ] All FROZEN ids appear in q/* and graph; no CANDIDATE appears in graph.
- [ ] Each WHAT/HOW q/* has: one WHY parent, ≤2 clarifier IDs, shared_vars, untyped cross_links, ≥1 assumption with test, ≥1 context_ref.
- [ ] Any A-* referenced in q/* exists in docs/ASSUMPTIONS/register.yaml.
- [ ] Typed links absent from q/*; present in graph.
- [ ] Decision(s) captured in docs/DECISIONS/decision_log.yaml.
- [ ] AUTO‑VERIFY PASS; AUTO‑APPLY completed; AUTO‑READ reflects new truth.

## Option‑A Hygiene
- [ ] One route per message.
- [ ] Echo‑Forward used for pro_request → AUTO.
- [ ] PRs are short‑lived; remote vs remote diff checked pre‑PR.
