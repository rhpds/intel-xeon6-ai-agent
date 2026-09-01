# Intel Xeon 6 201: Building an AI Agent

## Overview

This hands-on lab demonstrates how an enterprise AI agent combines a language model, structured tools, a system prompt, and orchestration. Participants deploy three MCP tools, a LangGraph advisor agent, and a browser UI in their OpenShift tenant namespace, then use RACMaaS CPU inference on Intel Xeon 6 to generate and evaluate illustrative solution briefs.

## Target Audience

- **Role:** Intel and Red Hat technical sellers and solution architects
- **Experience level:** Intermediate
- **What they already know:** Basic OpenShift command-line use, Kubernetes workload concepts, and introductory generative AI terminology
- **What they don't know:** How MCP tools, LangGraph orchestration, RACMaaS inference, prompts, and model selection combine into an auditable agent workflow

## Prerequisites

- A provisioned RHDP lab account and generated OpenShift credentials; the guide verifies login and namespace access.
- Familiarity with `oc`, `curl`, and JSON; commands are supplied and their results are checked in each module.
- No cluster-admin access, local model download, API-key creation, or GPU knowledge is required.

## Learning Objectives

1. Deploy and verify an MCP tool service that returns sourced Intel and Red Hat platform data.
2. Deploy and connect a LangGraph agent and browser UI to tenant-scoped RACMaaS inference.
3. Evaluate and tune agent output by changing prompts, customer scenarios, and CPU-served models.

## Content Type

Lab (hands-on).

## Products & Technologies

- Red Hat OpenShift Container Platform 4.22
- Red Hat Demo Platform RACMaaS
- Intel Xeon 6 CPU inference with Intel AMX
- LangGraph, Model Context Protocol, Python, and JSON-RPC 2.0

## Module Map

| Module | Title | Duration |
|--------|-------|----------|
| 1 | Anatomy of an Agent | 10 min |
| 2 | Deploy the MCP Tools | 10 min |
| 3 | Wire the Agent | 10 min |
| 4 | Test and Tune | 15 min |
| — | **Total lab** | **45 min** |

## Difficulty Level

Intermediate.

## Environment

**Learner view:** The learner receives credentials for an isolated namespace on the shared `ai-lab-xeon6-inference` OpenShift cluster and an automatically generated, tenant-scoped RACMaaS virtual key. The Showroom includes terminal, OpenShift Console, and Solution Architect UI tabs. No model server is deployed by the learner.

**Automation needed:** Yes. Existing AgnosticV tenant automation creates the user, namespace, quota, Showroom, and seven-day RACMaaS virtual key. Learners deploy the pinned tool, agent, and UI manifests during the exercises.

## Infrastructure Requirements

- **Cloud provider:** CNV
- **Cluster type:** Multinode shared cluster
- **OCP version:** 4.22
- **Topology:** Shared cluster, isolated namespace per learner
- **Sizing:** Existing `ai-lab-xeon6-inference` cluster; tenant quota requests 2 CPU and 2 GiB memory and limits 4 CPU and 4 GiB memory
- **Automation approach:** Ansible through AgnosticV
- **AI/MaaS:** RACMaaS open-source CPU model; default `qwen25-3b-cpu`, with an optional `phi3-mini-cpu` comparison
- **External services:** github.com, quay.io, and RACMaaS
- **Non-GA products:** None identified; final product-version review remains part of Publishing House infrastructure review

## Assessment Strategy

Each module ends with observable checks. Learners verify namespace selection, running pods, three-tool MCP discovery, structured tool responses, RACMaaS-backed requirement extraction and brief generation, visible inference logs, and a working UI. The final module compares prompt behavior and model quality/latency using sanitized scenarios.
