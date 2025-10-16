# Operator Quick Commands (Connector‑Limited)

## Verify base has the seed
git fetch origin
git ls-tree -r --name-only origin/pack/<PACK_ID> | grep '^q/.*\.yaml$' | wc -l

## Get blob SHA for Bank (use in q_patch.bank_version)
git ls-tree origin/pack/<PACK_ID> docs/FOUNDATIONS/QUESTION_BANK.md | awk '{print $3}'

## Re-seed on a head branch and open PR
git checkout -B seed/<PACK_ID>-v1 origin/pack/<PACK_ID>
unzip -o ~/Downloads/<seed_zip>.zip -d .
git add -A docs/FOUNDATIONS docs/TRACE docs/SCENARIOS graph q
git commit -m "<PACK_ID>: seed FROZEN nucleus (Option-A, verified)"
git push -u origin seed/<PACK_ID>-v1

# Open PR in UI with base=pack/<PACK_ID>, head=seed/<PACK_ID>-v1, then merge.
