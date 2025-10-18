# route_macros.md — v4.5

- To AUTO‑READ:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`

- To GUIDANCE (pre‑PRO):
  `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pre‑PRO pro_request (may include q_patch)`

- To AUTO‑VERIFY:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY`

- To AUTO‑APPLY:
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY`

- To SELECT‑ORG:
  `ROUTE → SELECT‑ORG (FREE) for <PACK_ID>`

- To update Assumption Register:
  `ROUTE → GUIDANCE (FREE) for <CHAIN_ID>: assumption_register_ops (commit=true)`

- To log a decision:
  `ROUTE → PRO (FREE) for <CHAIN_ID>: decision_log_ops (commit=true)`
