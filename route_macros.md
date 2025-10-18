# route_macros.md — v4.5.1 (Paste‑ready)

- AUTO‑READ
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)`

- GUIDANCE — ask for nucleus options (no numeric quota)
  `ROUTE → GUIDANCE (FREE) for <PACK_ID>: task=NUCLEUS-OPTIONS (chain_id=<CHAIN_ID>)`

- SELECT‑ORG — choose next frozen targets (supports parallel nuclei)
  `ROUTE → SELECT-ORG (FREE) for <PACK_ID>`

- GUIDANCE — pre‑PRO freeze request (may embed q_patch)
  `ROUTE → GUIDANCE (FORM) for <PACK_ID>: pre‑PRO pro_request (may include q_patch)`

- AUTO — verify then apply
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-VERIFY`
  `ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO-APPLY`
