# Module 2: Deploy the MCP Tools

## Brief Overview
Learners deploy the pinned MCP service and exercise hardware, OpenShift capability, and architecture-pattern tools through JSON-RPC.

## Audience and Time
Technical sellers and solution architects; 10 minutes.

## Learning Objectives
- Deploy and verify an MCP service on OpenShift.
- Inspect sourced structured data returned by three tools.

## Lab Structure
| Section | Title | Duration |
|---|---|---|
| 1 | Deploy and discover tools | 4 min |
| 2 | Query hardware and platform data | 3 min |
| 3 | Query an architecture pattern | 3 min |

## Detailed Steps
1. Apply the pinned solution-tools manifest.
2. Discover the generated route and list all tools.
3. Call the Intel hardware and OpenShift capability tools.
4. Retrieve an illustrative vertical architecture pattern.
5. Verify the pod, tool count, and structured responses.

## Key Takeaways
- MCP exposes tools through a standard protocol.
- Sourced workshop data reduces unsupported model invention.

## Infrastructure Notes
The service uses an immutable Quay image digest and runs in the learner namespace.
