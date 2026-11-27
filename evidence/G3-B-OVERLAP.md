# G3-B-OVERLAP - bounded fresh observation

Disposition: observation complete, pending distinct programme acceptance; no new independent PASS.

## Authority and native activation

- Repository: JayDEmily/automatic-timer-trial-v1-b; fresh ref: refs/heads/trial/gate-3-overlap-20261127.
- Direct ledger-only bootstrap: 512fc4b54c9c63754f0231d7b43b479e8484e4bb; sole paused parent 6e9cf46e32ddeeec5b4b0e24e643a1f6a8dd4993. Bootstrap tree b59b2c6daa1a83895eac7dd1168a5a4fe3ad9c84; clean private checkout.
- Manager-observed fresh Project identity and actual invoking native Start (one saved menu choice 1) matched the bootstrap. Original saved Start UTC: 2026-11-27T10:01:09.6171170Z.
- Exact M 8c4a11205c3a3b6df13979a274841e7d8f3391c1; E 5af8187767977e16dbe1fc77d873f963ede82278; CAC 1.1.4 unchanged. All 13 protected staged files byte-matched the exact local pinned method and were non-writable. Sole fresh external static binding read back and verified. Before/after head, tree, branch tip, ledger/assignment/verdict and clean status were identical. No attachment commit, receipt, sender or handoff.

## Actual retained original evidence

- Original ref refs/heads/trial/gate-3-hosted-editor-retry-20261127 read back at terminal V e73109ae5b8759587508f24c7455991d7b0d5c20.
- Original C a8a7d92b40232d266f1a971a5d9464fa08a99d56, actual tree bc640cd356aaf2568b518199ec8593f31bcbfd0f, original direct parent cb81058f610375a9cd26ecbc06251723a259bbcf. H 39122cd00cfc85f175206ed6f0a04b442f8811a3 directly descends from C and changed only ledger; V directly descends from H and changed only review report and ledger. Fresh setup directly descends from V and changed only governing files/ledger; fresh bootstrap only ledger.
- Inspected actual C diff against the prior contract: normalizer uses map(str.strip, lines) and filters empty stripped strings, preserving order, duplicates, case and internal whitespace. Three regression tests cover trimming, blanks and order/duplicates/case/internal whitespace; three baseline tests preserved. C changed exactly normalizer.py, tests/test_normalizer.py and evidence/G3-B1.md. No workflow change.
- Actual Git blob identities at V, paused setup and fresh bootstrap are identical for all retained source, test, workflow and original evidence files. Source/test/workflow and implementation report are identical at C/H/V. Independent review report is the V addition:

| Path | Git blob |
|---|---|
| .github/workflows/ci.yml | `f11bd46b4d4066988603c324c15c92a007ecdf0d` |
| evidence/G3-B1.md | `ccdca32309707636ed16eb9f2d019a9f5a0e95f8` |
| normalizer.py | `bf07ddd56443febb8eb511769b9d441c5886ce6f` |
| reviews/G3-B1.md | `223633c97c78436259a6ba08a3348d9029c363f8` |
| tests/test_normalizer.py | `478f033d1170a3bdd0fd24d44fc2a07e142aa864` |

- Exact original CI result matches the entire H and V candidate_result objects and the fresh retained_original_acceptance.ci object. Original workflow .github/workflows/ci.yml (Fixture CI), push on refs/heads/trial/gate-3-hosted-editor-retry-20261127, run 45961801571, attempt 1, job 140381110554 (Test normalizer), success. Actual previously verified tested SHA/tree C/T; six tests passed, zero failed. Original job log SHA-256 191fc2a9b1b034abc5c3d96adf1bdce60077729494176bb2cf9c951d3cec52e0, 13973 bytes. The distinct review report records original consume, exact C/tree/H, independent test and original CI evidence and terminal PASS. No new CI log retrieval, run or test, per narrow commission.
- Fresh branch inherits evidence of original acceptance only; no fresh candidate-specific CI, independent review or delivery asserted. Original V ledger remains terminal PASS, no successor. Fresh observation cannot adjudicate four-way overlap.

## Original substantive Git operation intervals (UTC)

Process boundaries measured immediately around each executing subprocess; exact argv, return code, stdout/stderr and nanosecond epoch timestamps retained privately. Setup, attachment, chat lifetime and waits excluded. The span below is not claimed to be continuously busy. No sleeps, barriers or work added to extend overlap.

| Operation (target checkout implicit) | Actual UTC start | Actual UTC end | Exit |
|---|---|---|---:|
| `git ls-remote <target-origin> refs/heads/trial/gate-3-overlap-20261127 refs/heads/trial/gate-3-hosted-editor-retry-20261127` | 2026-11-27T10:03:41.220479+00:00 | 2026-11-27T10:03:41.755685+00:00 | 0 |
| `git log --first-parent -5 '--format=%H %P %T %s' 512fc4b54c9c63754f0231d7b43b479e8484e4bb` | 2026-11-27T10:03:41.755978+00:00 | 2026-11-27T10:03:41.766918+00:00 | 0 |
| `git rev-list --parents -n 1 512fc4b54c9c63754f0231d7b43b479e8484e4bb` | 2026-11-27T10:03:41.767216+00:00 | 2026-11-27T10:03:41.774017+00:00 | 0 |
| `git rev-list --parents -n 1 6e9cf46e32ddeeec5b4b0e24e643a1f6a8dd4993` | 2026-11-27T10:03:41.774169+00:00 | 2026-11-27T10:03:41.778392+00:00 | 0 |
| `git rev-list --parents -n 1 e73109ae5b8759587508f24c7455991d7b0d5c20` | 2026-11-27T10:03:41.778508+00:00 | 2026-11-27T10:03:41.782003+00:00 | 0 |
| `git rev-list --parents -n 1 39122cd00cfc85f175206ed6f0a04b442f8811a3` | 2026-11-27T10:03:41.782098+00:00 | 2026-11-27T10:03:41.785387+00:00 | 0 |
| `git rev-parse 'a8a7d92b40232d266f1a971a5d9464fa08a99d56^'` | 2026-11-27T10:03:41.785474+00:00 | 2026-11-27T10:03:41.788567+00:00 | 0 |
| `git rev-parse 'a8a7d92b40232d266f1a971a5d9464fa08a99d56^{tree}'` | 2026-11-27T10:03:41.788651+00:00 | 2026-11-27T10:03:41.791915+00:00 | 0 |
| `git diff --name-status cb81058f610375a9cd26ecbc06251723a259bbcf a8a7d92b40232d266f1a971a5d9464fa08a99d56` | 2026-11-27T10:03:41.792022+00:00 | 2026-11-27T10:03:41.795728+00:00 | 0 |
| `git diff --name-status a8a7d92b40232d266f1a971a5d9464fa08a99d56 39122cd00cfc85f175206ed6f0a04b442f8811a3` | 2026-11-27T10:03:41.795844+00:00 | 2026-11-27T10:03:41.799166+00:00 | 0 |
| `git diff --name-status 39122cd00cfc85f175206ed6f0a04b442f8811a3 e73109ae5b8759587508f24c7455991d7b0d5c20` | 2026-11-27T10:03:41.799282+00:00 | 2026-11-27T10:03:41.802699+00:00 | 0 |
| `git diff --name-status e73109ae5b8759587508f24c7455991d7b0d5c20 6e9cf46e32ddeeec5b4b0e24e643a1f6a8dd4993` | 2026-11-27T10:03:41.802797+00:00 | 2026-11-27T10:03:41.806009+00:00 | 0 |
| `git diff --name-status 6e9cf46e32ddeeec5b4b0e24e643a1f6a8dd4993 512fc4b54c9c63754f0231d7b43b479e8484e4bb` | 2026-11-27T10:03:41.806099+00:00 | 2026-11-27T10:03:41.809651+00:00 | 0 |
| `git ls-tree -r a8a7d92b40232d266f1a971a5d9464fa08a99d56 -- normalizer.py tests/test_normalizer.py .github/workflows/ci.yml evidence/G3-B1.md reviews/G3-B1.md` | 2026-11-27T10:03:41.809775+00:00 | 2026-11-27T10:03:41.813703+00:00 | 0 |
| `git ls-tree -r 39122cd00cfc85f175206ed6f0a04b442f8811a3 -- normalizer.py tests/test_normalizer.py .github/workflows/ci.yml evidence/G3-B1.md reviews/G3-B1.md` | 2026-11-27T10:03:41.813849+00:00 | 2026-11-27T10:03:41.817278+00:00 | 0 |
| `git ls-tree -r e73109ae5b8759587508f24c7455991d7b0d5c20 -- normalizer.py tests/test_normalizer.py .github/workflows/ci.yml evidence/G3-B1.md reviews/G3-B1.md` | 2026-11-27T10:03:41.817375+00:00 | 2026-11-27T10:03:41.821252+00:00 | 0 |
| `git ls-tree -r 6e9cf46e32ddeeec5b4b0e24e643a1f6a8dd4993 -- normalizer.py tests/test_normalizer.py .github/workflows/ci.yml evidence/G3-B1.md reviews/G3-B1.md` | 2026-11-27T10:03:41.821360+00:00 | 2026-11-27T10:03:41.825199+00:00 | 0 |
| `git ls-tree -r 512fc4b54c9c63754f0231d7b43b479e8484e4bb -- normalizer.py tests/test_normalizer.py .github/workflows/ci.yml evidence/G3-B1.md reviews/G3-B1.md` | 2026-11-27T10:03:41.825314+00:00 | 2026-11-27T10:03:41.828710+00:00 | 0 |
| `git diff cb81058f610375a9cd26ecbc06251723a259bbcf a8a7d92b40232d266f1a971a5d9464fa08a99d56 -- normalizer.py tests/test_normalizer.py` | 2026-11-27T10:03:41.828813+00:00 | 2026-11-27T10:03:41.832233+00:00 | 0 |
| `git show a8a7d92b40232d266f1a971a5d9464fa08a99d56:plans/active-execplan.md` | 2026-11-27T10:03:41.832369+00:00 | 2026-11-27T10:03:41.835685+00:00 | 0 |
| `git show a8a7d92b40232d266f1a971a5d9464fa08a99d56:evidence/G3-B1.md` | 2026-11-27T10:03:41.835804+00:00 | 2026-11-27T10:03:41.839066+00:00 | 0 |
| `git show 39122cd00cfc85f175206ed6f0a04b442f8811a3:state/ledger.json` | 2026-11-27T10:03:41.839211+00:00 | 2026-11-27T10:03:41.842766+00:00 | 0 |
| `git show e73109ae5b8759587508f24c7455991d7b0d5c20:state/ledger.json` | 2026-11-27T10:03:41.842956+00:00 | 2026-11-27T10:03:41.846377+00:00 | 0 |
| `git show e73109ae5b8759587508f24c7455991d7b0d5c20:reviews/G3-B1.md` | 2026-11-27T10:03:41.846531+00:00 | 2026-11-27T10:03:41.849965+00:00 | 0 |
| `git show a8a7d92b40232d266f1a971a5d9464fa08a99d56:.github/workflows/ci.yml` | 2026-11-27T10:03:41.850068+00:00 | 2026-11-27T10:03:41.853258+00:00 | 0 |

First measured substantive operation started 2026-11-27T10:03:41.220479+00:00; last ended 2026-11-27T10:03:41.853258+00:00. Separate publication operations and first actual pause/verified disposition are retained in private raw records; the following ledger-only disposition will record the actual pause decision.

## Publication interruption

The first local report commit stopped at 2026-11-27T10:04:19.790713+00:00 UTC because the fresh private clone had no configured Git author identity. No commit or push occurred. The same scoped report was recovered using the verified existing target identity in the private checkout only. The original failed command and timestamp are preserved; no additional substantive source-evidence operations are counted after that interruption.

## Limits

Only this report and a separate paused ledger disposition may be published. No source, tests, workflow, earlier ref, method/entry, new engineering C, new CI, handoff, successor, production or self-acceptance. Original Step 8 RETURN remains pending separate programme review.
