# G3-SAVED-TURN — independent reviewer verdict

**PASS — scoped to this single disposable hosted saved-turn proof.**

- Candidate C: `59f059711ba11c01aa4a37013225dfa324d225e2`
- Candidate tree: `c7637ecaad5d83efb2382899ec9b6bf638dffb02`
- Separate reviewer commission H: `76646b2c8fed9c685c51662bdbcfe4abb000ef91`
- Setup/baseline: `b4cadd216740f37114aa3da31328fa5b670238ff`

## Independent admission

The fresh ordinary-Chat reviewer began with read-only intake in a private Ubuntu checkout. Verified the staged reader bytes against the exact method pin `8c4a11205c3a3b6df13979a274841e7d8f3391c1` and the digest-addressed binding. The unchanged `hosted_delivery.py consume` returned the matching active assignment, verified original completion (one Send, original sender exit 0, distinct owned saved child), and current H. The original native evidence remains private; this review does not recreate delivery, claim a new Send, or publish private records.

## Candidate and independent tests

H is a direct child of C and differs only in `state/ledger.json`. C has the exact tree above. Its diff from setup changes only `normalizer.py`, `tests/test_normalizer.py` and `evidence/PROOF.md`; the committed workflow is unchanged from setup. The candidate applies `str.strip()` to each string, drops empty stripped values and retains iteration order, case, duplicates and internal whitespace. It satisfies the complete bounded fixture requirement. The added regression test exercises leading/trailing whitespace, empty and whitespace-only entries, order, duplicates, case and internal whitespace; the previous three tests remain unchanged.

Independent command: `python3 -B -m unittest discover -s tests -v`.

- Setup snapshot: 3/3 passed.
- Setup implementation plus exact C tests in a separate scratch snapshot: expected RED, 3 passed and the new trim/drop test failed; exit 1.
- Clean exact C checkout: 4/4 passed, exit 0; no working-tree changes. Candidate diff whitespace check passed.

## Exact-C hosted CI

Read the live GitHub run, original attempt, original attempt jobs and original job log independently; no rerun. [Fixture CI run 45952855813, attempt 1](https://github.com/JayDEmily/automatic-timer-trial-v1-b/actions/runs/45952855813) (workflow ID 431328569, `.github/workflows/ci.yml`, push on `trial/gate-3-hosted-editor-proof-20261127`) completed successfully at exact C. The single required [Test normalizer job 140352476989](https://github.com/JayDEmily/automatic-timer-trial-v1-b/actions/runs/45952855813/job/140352476989) completed successfully, including all steps. The original log contains the actual checkout's exact TESTED_SHA and TESTED_TREE above, all four named passing tests, Ran 4 tests, and OK. Its 13,618 bytes and SHA-256 `b9d49314a39714b9271bbd62cde29cbc456f8343fdff4d23b80782190fb344af` exactly match H.

## Disposition

The independent admission, candidate, exact-C CI and test requirements are satisfied. Terminal PASS for G3-SAVED-TURN only; preserve C, no successor. Earlier recovery cohort, held commissions, unrelated refs, Projects and programme-level Gate 3 acceptance remain outside scope and unchanged. No claim of grouped delivery, four-way concurrency, general release or wider qualification.
