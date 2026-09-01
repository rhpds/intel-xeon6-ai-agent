# intel-xeon6-ai-agent

A 45-minute hands-on lab for Intel and Red Hat technical sellers and solution architects. Learners deploy a lightweight LangGraph solution-advisor agent on Red Hat OpenShift, connect three MCP tools for sourced Intel hardware and Red Hat platform information, and generate an illustrative solution brief using tenant-scoped RACMaaS CPU inference on Intel Xeon 6. The lab demonstrates agent orchestration, structured tool calling, and human validation of AI-generated recommendations. Triforce provides the versioned application implementation, while this project owns the learner-facing Showroom content and Publishing House lifecycle.

**Owner:** jkershawrh
**Migrated from:** https://github.com/jkershawrh/intel-xeon6-ai-agent-201

---

## What was set up

1. Repository created (migrated from existing Showroom repo)
2. `catalog-info.yaml` added to repository
3. Registered in Developer Hub catalog
4. Orchestrator workflow started — your AI-guided content pipeline is running!

## What happens next

Claude will walk you through the entire content lifecycle — from intake and spec creation, through Jira tracking and reviews, all the way to a published lab on RHDP. Just follow the prompts!

## Getting started

### DevSpaces (recommended)

1. Open in DevSpaces: `https://devspaces.apps.ocpv-infra02.wdc07.infra.demo.redhat.com#https://github.com/rhpds/intel-xeon6-ai-agent`
2. Use Claude via the **extension** or the **CLI**:
   - **Extension:** Click the **Claude** icon in the sidebar, click **New Session**. If the Claude icon is not visible, open **Extensions** (`Ctrl/Cmd+Shift+X`), find **Claude Code for VS Code** under the DevSpaces section, click it, then click **Enable (Workspace)**.
   - **CLI:** Open a terminal and run `claude`
3. Run `/rhdp-publishing-house` — and you're off!

### Local machine

1. Install the skills:
   ```
   git clone -b prod https://github.com/rhpds/rhdp-publishing-house-skills.git ~/.claude/skills/publishing-house
   ```
2. Clone the repo:
   ```
   git clone https://github.com/rhpds/intel-xeon6-ai-agent
   ```
3. `cd intel-xeon6-ai-agent`
4. Start Claude CLI: `claude`
5. Run `/rhdp-publishing-house` — and you're off!
