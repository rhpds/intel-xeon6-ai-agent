# Intel 201: learner validation and PH author review

Tracking: [GPTEINFRA-17786](https://issues.redhat.com/browse/GPTEINFRA-17786); [RHDPCD-1418](https://issues.redhat.com/browse/RHDPCD-1418).

## Reviewable fixes

The strict inference validator now rejects non-object replies and non-finite latency evidence. Model comparison is optional and requires an allocated alternative; the learner saves and restores the original model and checks both inference stages. Corrected the monthly request/cost scenario so the requested arithmetic is internally consistent.

## Verification boundary

15 local regression tests pass (including eight author-workspace auth checks). Antora 3.1.14 builds the current learner source. These are offline author-package results; synthetic service replies do not establish real model or catalog acceptance.

Offline response checks cover both assigned-model stages and all three MCP tools. No new live Intel 201 deployment/model run passed on October 22. Historical MCP-only evidence is retained separately; full agent inference and browser behavior remain unqualified.

## Requested reviewer actions

Accept connection automation RHDPCD-1422 and wire health/E2E RHDPCD-1423/1424 into the PH-generated catalog. Run the pinned learner deployment, both assigned-model stages and all three tools, browser UI, second-tenant isolation, key lifecycle and capacity checks.

PH maintainers must accept the intake/design, run supported RCARS/intake ingestion and generate the AgnosticV/QA wiring. Browser PH notes are the available reconciliation channel; local API access is unavailable. Dallas and Oberon are development environments, not catalog-onboarding substitutes. Do not advance acceptance tasks or PH stages from these offline checks. Preserve the related source/reference PR history and keep every RHDP PR linked to its onboarding Jira.
