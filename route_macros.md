# route_macros.md — paste‑ready snippets (v4.4)

- Start L0:
  FOUNDATIONS_GATE=OPEN
  ROUTE → GUIDANCE‑ORG (FREE) for <CHAIN>: task=CLARIFIER_ROUND level=L0 mode=ROOT_FINDER

- To AUTO‑READ:
  ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)

- To SELECT‑ORG:
  ROUTE → SELECT‑ORG (FREE) for <CHAIN>

- To GUIDANCE (pre‑PRO):
  ROUTE → GUIDANCE (FORM) for <CHAIN>/<PACK_ID>: pre‑PRO pro_request (may include q_patch)

- To AUTO‑VERIFY:
  ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY

- To AUTO‑APPLY:
  ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY

- To PRO‑EVAL:
  ROUTE → PRO‑EVAL (FREE) for <CHAIN>

- Echo‑Forward (Isolated threads)
  # 1) Paste last GUIDANCE pro_request YAML into AUTO thread
  # 2) Then run: ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑VERIFY
  # 3) On PASS: ROUTE → AUTO (FORM) for <PACK_ID>: task=AUTO‑APPLY
