# Intel 201 acceptance checks

These checks are prepared source, not evidence of a successful dev order. After a reviewer assigns the base CI, wires the connection role into provisioning, and a learner deploys the versioned manifests:

```
python3 qa-automation/validate.py --context <dev-context> --namespace user-<guid>-triforce --mode health
python3 qa-automation/validate.py --context <dev-context> --namespace user-<guid>-triforce --mode e2e
```

Health runs before learner exercises and checks the existing tenant namespace and provisioned connection objects without retrieving the key. E2E runs after the lab is solved, checks application availability/credential references/agent health and submits one synthetic request and requires a substantive structured brief, successful assigned-model inference at both model stages, all three MCP tools, and no logged errors. Neither check proves CPU hardware placement or output accuracy; those require platform evidence and human review. Browser UI, second-tenant isolation, cleanup/key revocation, and a 25-concurrent-user capacity run remain separate gates.

Local regression tests: `python3 -m unittest discover -s qa-automation -p 'test_*.py'`.

Tracking: RHDPCD-1418; automation RHDPCD-1422, health RHDPCD-1423, E2E RHDPCD-1424; integration GPTEINFRA-17786 / INTEL-49. Keep the PH workflow at its actual stage until reviewers accept dev-order evidence.

PH entry points are `healthcheck.yml` (provisioned connection objects, under 60 seconds) and `e2e.yml` (replays the pinned learner deployment, then calls the strict inference validator). The runner must have namespace-scoped access to the assigned lab namespace; do not grant cluster-admin merely for these checks. PH's generated catalog config must enable the QA runner and supply its identity/namespace. E2E applies the learner manifests and belongs on a dev test tenant; health is read-only and safe to repeat. Neither status is marked complete until author acceptance.

Dallas dev evidence (2026-10-20): the pinned 201 MCP service passed health, discovery and structured execution of all three tools. The existing dev model allocation lists `qwen25-3b-cpu`; this alone does not prove the full agent workflow. Full dual-stage model inference, UI, tenant isolation, key revocation and capacity remain pending. PH owns generated AgnosticV; Dallas is not an RHDP catalog deployment.
