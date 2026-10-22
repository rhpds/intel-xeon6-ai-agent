# Intel 201 connection provisioning

Run `intel_ai_agent.automation.configure_connection` after the tenant namespace and per-order LiteMaaS virtual key workloads. Pass `intel_201_namespace`, `intel_201_api_base`, and `intel_201_api_key` from provisioner memory. Do not pass the key through Showroom user data, GitOps parameters, or an invocation recorded in shell history.

The role creates the two connection objects consumed by the versioned Triforce agent manifest. It requires an existing tenant namespace. During teardown (`ACTION: destroy`) it removes only these two objects; the LiteMaaS workload must revoke the virtual key and the tenant workload owns namespace deletion.

This collection is source prepared for integration. The PH infrastructure reviewer must assign the base CI and connect the role in the catalog workflow before a fresh-order test can pass.
