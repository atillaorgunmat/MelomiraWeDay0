# route_macros.md — paste-ready snippets (ASCII hyphens ONLY)

- To AUTO‑READ:
  ROUTE → AUTO (FORM) for P-FND-0001: task=AUTO-READ (inventory,gaps,share_list,h/v relations,trace_map; no scaffold)

- To SELECT‑ORG:
  ROUTE → SELECT-ORG (FREE) for P-FND-0001

- To GUIDANCE (pre‑PRO):
  ROUTE → GUIDANCE (FORM) for P-FND-0001: pre‑PRO pro_request (may include q_patch)

- Echo‑Forward (Isolated threads)
  # 1) Paste last GUIDANCE pro_request YAML into AUTO thread
  # 2) Then run:
  ROUTE → AUTO (FORM) for P-FND-0001: task=AUTO-VERIFY
  # 3) On PASS:
  ROUTE → AUTO (FORM) for P-FND-0001: task=AUTO-APPLY
