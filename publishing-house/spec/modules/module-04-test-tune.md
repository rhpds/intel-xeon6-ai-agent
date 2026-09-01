# Module 4: Test and Tune

## Brief Overview
Learners compare sanitized customer scenarios, modify the system prompt, evaluate a second CPU-served model, and document the resulting agent configuration.

## Audience and Time
Technical sellers and solution architects; 15 minutes.

## Learning Objectives
- Evaluate whether recommendations reflect scenario requirements and tool data.
- Tune prompt behavior and compare model quality and latency.

## Lab Structure
| Section | Title | Duration |
|---|---|---|
| 1 | Compare scenarios | 5 min |
| 2 | Customize and test prompt | 5 min |
| 3 | Compare models and record agent card | 5 min |

## Detailed Steps
1. Run three sanitized scenarios and compare recommendations.
2. Add a migration-path requirement to the system prompt.
3. Redeploy and test the changed prompt.
4. Switch from `qwen25-3b-cpu` to `phi3-mini-cpu`.
5. Compare quality and latency and complete the agent card.

## Key Takeaways
- Prompt changes are governed configuration changes.
- Model selection is a measured quality and latency tradeoff.
- Customer-facing output requires human validation.

## Infrastructure Notes
Both models are authorized through the provisioned RACMaaS virtual key.
