# Module 3: Wire the Agent

## Brief Overview
Learners deploy the LangGraph agent and web UI, connect the generated RACMaaS credentials and MCP service, and run the first structured recommendation.

## Audience and Time
Technical sellers and solution architects; 10 minutes.

## Learning Objectives
- Connect an agent to tenant-scoped RACMaaS and MCP tools.
- Verify structured requirements, recommendations, and inference logs.

## Lab Structure
| Section | Title | Duration |
|---|---|---|
| 1 | Inspect prompt and connection | 3 min |
| 2 | Deploy agent and UI | 4 min |
| 3 | Verify first conversation | 3 min |

## Detailed Steps
1. Inspect the advisor system prompt.
2. Create the RACMaaS connection ConfigMap and Secret from injected attributes.
3. Apply the pinned agent and UI manifests.
4. Submit a sanitized customer scenario.
5. Inspect requirements, tool results, brief, and inference log.

## Key Takeaways
- RACMaaS access is assigned automatically; learners never receive a master key.
- Agent calls and tool calls remain visible for human review.

## Infrastructure Notes
Default inference uses `qwen25-3b-cpu`; no model server or GPU is deployed.
