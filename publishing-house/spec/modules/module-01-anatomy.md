# Module 1: Anatomy of an Agent

## Brief Overview
Learners compare model-only responses with an agent pattern and identify the responsibilities of tools, prompts, and orchestration. They confirm their tenant namespace before deploying resources.

## Audience and Time
Technical sellers and solution architects with basic OpenShift familiarity; 10 minutes.

## Learning Objectives
- Distinguish model synthesis from authoritative tool lookup.
- Identify the model, MCP, LangGraph, and UI components.

## Lab Structure
| Section | Title | Duration |
|---|---|---|
| 1 | Model baseline | 3 min |
| 2 | Agent pattern | 4 min |
| 3 | Components and namespace | 3 min |

## Detailed Steps
1. Review a model-only recommendation and identify unsupported facts.
2. Map requirements, tool facts, and model synthesis responsibilities.
3. Inspect the agent architecture image.
4. Log in and verify the assigned tenant namespace is empty.

## Key Takeaways
- Models synthesize language; tools supply controlled data.
- Agent behavior combines tools, prompts, and orchestration.

## Infrastructure Notes
No cluster-scope permissions are required.
