#!/usr/bin/env python3
"""Read-only provisioned-tenant checks; e2e validates the solved lab and inference.

Never prints routes, responses, credentials, or raw subprocess errors.
"""
import argparse
import json
import math
import re
import subprocess
import sys
import urllib.request

TOOLS = {"intel_hardware_lookup", "openshift_capabilities", "reference_architectures"}


def validate_response(data, model):
    if not isinstance(data, dict):
        raise ValueError("Response must be an object")
    if not isinstance(data.get("brief"), str) or len(data["brief"].strip()) < 80:
        raise ValueError("Missing substantive solution brief")
    for key, kind in (("requirements", dict), ("hardware_options", list),
                      ("platform_capabilities", list), ("architecture", dict)):
        if not isinstance(data.get(key), kind) or not data[key]:
            raise ValueError("Missing structured solution evidence")
    entries = data.get("inference_log", [])
    if not isinstance(entries, list) or not entries or any(not isinstance(e, dict) for e in entries):
        raise ValueError("Missing inference evidence")
    if any(e.get("error") for e in entries):
        raise ValueError("Inference log contains a failure")
    nodes = {e.get("node") for e in entries if e.get("model") == model}
    if not {"understand_requirements", "generate_brief"} <= nodes:
        raise ValueError("Both model inference stages must succeed with the assigned model")
    if not TOOLS <= {e.get("tool") for e in entries}:
        raise ValueError("Missing MCP tool evidence")
    for e in entries:
        latency = e.get("latency_ms")
        if isinstance(latency, bool) or not isinstance(latency, (int, float)) or not math.isfinite(latency) or latency < 0:
            raise ValueError("Invalid latency evidence")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--context", help="Optional local context; PH runner uses its assigned kubeconfig")
    parser.add_argument("--namespace", required=True)
    parser.add_argument("--mode", choices=["health", "e2e"], default="health")
    parser.add_argument("--model", default="qwen25-3b-cpu")
    args = parser.parse_args()
    if not re.fullmatch(r"user-[a-z0-9][a-z0-9-]*-triforce", args.namespace):
        parser.error("An explicit Intel 201 tenant namespace is required")

    oc = ["oc"] + (["--context", args.context] if args.context else [])

    def read(kind, name):
        result = subprocess.run(oc + ["-n", args.namespace,
                                 "get", kind, name, "-o", "json"], capture_output=True, check=True)
        return json.loads(result.stdout)

    # Check only existence, never retrieve the Secret payload.
    subprocess.run(oc + ["-n", args.namespace,
                    "get", "secret", "litellm-api-key", "-o", "name"],
                   capture_output=True, check=True)
    connection = read("configmap", "racmaas-connection").get("data", {}).get("api-base", "")
    if not connection.startswith("https://") or not connection.endswith("/v1"):
        raise ValueError("Model endpoint has not been provisioned")
    print("PASS: tenant namespace and per-order connection objects exist")
    # Learners deploy the three applications during the exercises. Provisioning
    # health must not require a learner to have completed the lab already.
    if args.mode == "health":
        return
    for name in ("solution-tools", "solution-agent", "solution-ui"):
        deployment = read("deployment", name)
        if deployment.get("status", {}).get("availableReplicas", 0) < 1:
            raise ValueError("A required deployment is unavailable")
    deployment = read("deployment", "solution-agent")
    env = {e["name"]: e for e in deployment["spec"]["template"]["spec"]["containers"][0]["env"]}
    key = env.get("LITELLM_API_KEY", {})
    if "value" in key or key.get("valueFrom", {}).get("secretKeyRef") != {"name": "litellm-api-key", "key": "api-key"}:
        raise ValueError("Agent must reference the provisioned Secret")
    route = read("route", "solution-agent")
    if not route.get("spec", {}).get("tls"):
        raise ValueError("Agent Route requires TLS")
    url = "https://" + route["spec"]["host"]
    with urllib.request.urlopen(url + "/health", timeout=30) as response:
        if json.load(response).get("status") != "healthy":
            raise ValueError("Agent health failed")
    print("PASS: tenant deployments, connection references and agent health")
    if args.mode == "e2e":
        body = json.dumps({"query": "A retailer needs inventory forecasting at 20 edge stores. Recommend Intel hardware, OpenShift capabilities and a reference architecture."}).encode()
        request = urllib.request.Request(url + "/api/v1/advise", data=body,
                                         headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=180) as response:
            validate_response(json.load(response), args.model)
        print("PASS: structured brief, both model stages and all three MCP tools")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError, subprocess.SubprocessError):
        print("FAIL: validation did not pass; inspect the tenant privately with the lab owner", file=sys.stderr)
        sys.exit(1)
