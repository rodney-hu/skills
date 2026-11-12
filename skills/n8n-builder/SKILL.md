---
name: n8n-builder
description: >
  Expert n8n workflow architect and builder. Use this skill whenever Rodney asks to build, plan, debug, refactor, or review any n8n workflow — including Apollo → Notion → Instantly pipelines, lead enrichment automations, CRM sync flows, HTTP request nodes, webhook triggers, conditional branching, error handling, data transformation, credential management, or any automation involving n8n. Also trigger on "design an n8n workflow", "build an automation", "n8n best practices", "optimize this workflow", "my n8n workflow is broken", "what nodes should I use", "how do I structure this in n8n", or any request involving workflow architecture, JSON schema design, or automation planning. This skill plans before building, runs phased execution, and enforces deterministic, modular, clean-data principles at every step. Always use this skill before writing any n8n workflow by hand.
---

# n8n Builder

Expert n8n workflow architect. Plans before building. Thinks in nodes, schemas, and execution paths.

## Operating Principles

```
SIMPLICITY > CLEVERNESS
DETERMINISTIC > PROBABILISTIC
MODULAR > MONOLITHIC
SCHEMA-FIRST > DATA AFTER
FILTER EARLY > FILTER LATE
PLAN → BUILD → VALIDATE → TEST → PUBLISH
```

**Never** start building before completing Phase 0 (Plan). Every workflow has a defined input contract, output contract, and failure mode before a single node is placed.

**Trust live MCP tools over training data.** n8n evolves faster than any model's training cutoff. Parameter names drift, new tools land, defaults change. When `get_node_types` contradicts what you remember, trust the tool.

---

## Non-Negotiables

1. **Validate AND verify before publish.** Run `validate_workflow` on SDK code, then `get_workflow_details` after every create/update to check the `connections` object. Validation catches schema errors; it does NOT catch silently dropped wires (the `.to()` inside `.add()` trap, fan-out collapse, merge index off-by-one).
2. **Tokens/secrets never go in text fields.** Always use the n8n credential system. See Credentials section.
3. **Invoke the matching section before any n8n MCP call.** Expressions, agents, subworkflows, error handling — each has rules. Don't call MCP tools blind.

---

## Pre-Build Checklist

- [ ] Workflow describable in one sentence? If not, scope is undefined.
- [ ] Name follows `Verb + Object + Trigger` format?
- [ ] Input contract defined (required + optional fields)?
- [ ] Output contract defined (destination + success signal)?
- [ ] All failure modes named with handling strategy?
- [ ] Filter/reduce step placed as early as possible?
- [ ] Independent side effects branched (not chained)?

---

## MCP Tools Reference

The n8n MCP defers tool descriptions. Use this as the working reference.

### Workflow Management

| Tool | What it does |
|------|--------------|
| `search_workflows` | Search by query (matches name + description; tags not filterable via MCP). Use to discover existing workflows before building. |
| `get_workflow_details` | Fetch full workflow JSON by ID. **Run after every create/update** to verify the `connections` object. |
| `search_folders` | List folders. Cannot create or move folders via MCP. |
| `search_projects` | List projects. |
| `archive_workflow` / `publish_workflow` / `unpublish_workflow` | Soft-delete / activate / deactivate. Validate before publish. |
| `search_executions` | Find executions by status, workflow, time range. |
| `get_execution` | Fetch a specific execution by ID. |

### Building

| Tool | What it does |
|------|--------------|
| `get_sdk_reference` | Fetch n8n Workflow SDK reference. Read once per session before writing code. |
| `get_workflow_best_practices` | Best practices for a technique (`technique: "list"` to see all). Call once per technique. |
| `search_nodes` | Discover nodes by capability. Returns IDs + discriminators (resource/operation/mode). |
| `get_node_types` | Fetch exact TypeScript parameter definitions. **Required before configuring any node.** Never guess parameter names. |
| `create_workflow_from_code` | Save workflow from SDK code. Always include `description`. Pass `skillsUsed`. |
| `update_workflow` | Atomic ops on an existing workflow (max 100, all-or-nothing). Saves a draft; needs `publish_workflow` to go live. |
| `validate_node_config` | Per-node schema validation (1–50 nodes per call). Use during iteration and debugging. Not a replacement for `validate_workflow`. |
| `validate_workflow` | Validate full SDK code before create/update. Necessary but not sufficient — doesn't catch all wiring traps. |
| `list_credentials` | List credentials by type/project. Returns metadata only, never secret values. |

### Testing

| Tool | What it does |
|------|--------------|
| `prepare_test_pin_data` | Returns JSON schemas for nodes needing pin data: triggers, credentialed nodes, HTTP Request. |
| `test_workflow` | Run with supplied pin data. Auto-pins triggers, credentialed nodes, HTTP Request. Code, Edit Fields, IF, Data Tables, Execute Command, sub-workflow calls all run for real. **Ask before running if not-auto-pinned nodes have side effects.** |
| `execute_workflow` | Production execution with real trigger. Wire error handling first. |

### Data Tables

| Tool | What it does |
|------|--------------|
| `create_data_table` | Create a new Data Table. |
| `search_data_tables` | Find existing Data Tables. |
| `add_data_table_rows` | Append rows. |
| `add_data_table_column` / `delete_data_table_column` | Schema changes. |

---

## Phase 0: Plan (Required Before All Builds)

Search for existing workflows first: `search_workflows({ query: 'keyword' })`. If logic already exists as a sub-workflow, use it.

Then produce a **Workflow Blueprint**:

```json
{
  "workflow_name": "string (Verb + Object + Trigger format)",
  "trigger_type": "webhook | schedule | manual | app_event",
  "input_contract": {
    "source": "string",
    "fields_required": ["field1", "field2"],
    "fields_optional": ["field3"]
  },
  "output_contract": {
    "destination": "string",
    "fields_written": ["field1", "field2"],
    "success_signal": "string"
  },
  "phases": [
    { "phase": 1, "label": "string", "nodes": ["NodeType"], "goal": "string" }
  ],
  "failure_modes": [
    { "scenario": "string", "handling": "string" }
  ],
  "credentials_required": ["CredentialName"],
  "estimated_complexity": "low | medium | high"
}
```

**Blueprint must be confirmed** by user before Phase 1 begins.

---

## Lifecycle Stages

| Stage | What happens |
|-------|-------------|
| **1. PLAN** | Phase 0 Blueprint. Search for existing sub-workflows. Confirm scope. |
| **2. BUILD** | Write SDK code. Call `get_sdk_reference` once. Call `get_node_types` for every node before configuring. Use `validate_node_config` per node as you go. |
| **3. VALIDATE** | `validate_workflow` + `get_workflow_details` to inspect `connections`. Surface user-side wire-up checklist (credentials per node, missing folders, MCP access toggle for UI-built workflows). |
| **4. TEST** | `prepare_test_pin_data` → `test_workflow`. Tell user which nodes were pinned. Iterate until output matches intent. |
| **5. PUBLISH** | `publish_workflow` only after stages 3 and 4 are clean. |
| **6. HANDOFF** | Webhook URL (if applicable), trigger cadence, where data goes, what to watch, what's still pending on their side. |

### Three most common stage skips (don't do these):
- **Build before plan** — Starting without confirming what X means or if a sub-workflow already exists.
- **Test before user wire-up** — Running `test_workflow` before the user has verified credentials per node (auto-assigns most recent credential, silently picks wrong one with multiples).
- **Publish without test** — Validation passing means SDK is well-formed; it does NOT mean the workflow is correct.

### Per-workflow MCP access
Workflows created via MCP (`create_workflow_from_code`) default to MCP-accessible. Workflows created in the n8n UI can default to off — invisible to MCP until the user flips the toggle in workflow Settings.

---

## Execution Model: Sequential, Not Parallel

**n8n executes sequentially, left-to-right, top-to-bottom.** Branches that visually appear parallel (fan-out from one source to multiple downstreams) run one after the other, ordered by target node Y-position. There is no automatic concurrency.

Practical consequences:
- A fan-out to three slow HTTP calls runs in series — total latency is the sum, not the max.
- "Parallel" branches share workflow state in execution order; downstream consumers see whatever the last branch left.
- For real concurrency: dispatch sub-workflows with `mode: 'each'` and `waitForSubWorkflow: false`.

Fan-out still the correct pattern for independent side effects (keeps each path isolated from others), just don't design around assumed speed gains:

```
[Normalized Data]
  ├→ [Write Notion]      onError: continueRegularOutput
  ├→ [Notify Slack]      onError: continueRegularOutput
  ├→ [Enroll Instantly]  onError: continueRegularOutput
  └→ [Respond Webhook]
```

---

## Node Architecture Rules

### Control Flow: Use the Right Primitive

| Goal | Use | Never Use |
|------|-----|-----------|
| Drop non-matching items | `Filter` node | IF with empty false branch |
| Two exclusive paths | `IF` node | Nested IFs |
| 3+ paths on a value | `Switch` node + fallback wired | Nested IFs |
| Per-item side effects | `splitInBatches batchSize:1` + loop | Chained HTTP in sequence |
| Two independent data sources | Parallel branches + `Merge combineByPosition` | Chain B after A |

Always wire the `fallbackOutput` on Switch nodes to a logging/review node. Silent data loss is the hardest bug to find.

### Item Count Awareness

Before every connection A → B: *"If A returns N items, should B run N times or once?"*
- If once: `executeOnce: true`
- If per-item: `splitInBatches batchSize:1`
- Never add `alwaysOutputData: true` to "keep the chain alive" — causes downstream crashes on empty data.
- Trust 0-item returns — the chain stopping cleanly is correct behavior.

### The Set-Node Antipattern

The most common antipattern agents produce: a Set node that exists only to extract fields for one downstream consumer.

```
// WRONG
Webhook → Set: { email: $json.body.email } → Notion: email = {{ $json.email }}

// RIGHT
Webhook → Notion: email = {{ $('Webhook Trigger').item.json.body.email }}
```

A Set node earns its place when:
- The same derived value is read by **2+ downstream consumers**
- The derivation is non-trivial (multi-step logic)
- It's the **final node of a sub-workflow**, shaping the return contract
- You need to drop fields by setting `Include Other Fields: false`
- You need to rename fields and want that rename visible in one place

Multiple consecutive Set nodes each defining one field = almost certainly over-extraction. Collapse or delete.

### NoOp Convergence Pattern

When branches merge and downstream nodes need a stable reference point, insert a NoOp node at the convergence:

```
Branch A ──┐
           ├─→ [NoOp: Combine Inputs] ──→ Downstream references $('Combine Inputs').item.json.x
Branch B ──┘
```

If branches produce different shapes, use a Set node instead of NoOp — normalize both branches into one output shape.

### AI Node Rules
- Attach an `outputParserStructured` subnode with JSON schema + `autoFix: true` to every AI agent feeding downstream logic
- Always include `confidence` (0–1) and `reasoning` (string) in AI classification output
- AI without structured output is a non-deterministic data source — it will break downstream nodes
- Tool names and descriptions are part of the prompt. Vague tool names cause silent failures (model skips or mis-selects).

### Naming Conventions
```
[Action] [Entity] [Context]
Examples:
  "Get Contact Apollo"
  "Normalize Webhook Payload"
  "Filter: Qualified Lead?"
  "Upsert Lead Notion"
  "Send Alert Slack"
```
Node names appear in expressions. `$('Normalize Webhook Payload').item.json.email` is readable at 11pm during an incident.

---

## Expressions

### Non-Negotiable: Reference by Node Name, Not `$json`

Use `$('Node Name').item.json.field` over `$json.field`.

`$json` breaks when:
- An intermediate node is inserted (now `$json` refers to the new intermediate, not your source)
- A node clears item context (`Aggregate`, `Code` with Run for All, branching Merge)
- Branches converge via Merge (`$json` is whichever branch fired last — non-deterministic)

`$('Get Contact').item.json.email` is unambiguous. Always the named node's output, regardless of what's between.

### Luxon for Dates, Not the DateTime Node

```ts
{{ DateTime.now().toISO() }}
{{ DateTime.fromISO($('Source').item.json.created_at).toFormat('yyyy-MM-dd') }}
{{ DateTime.now().minus({ days: 7 }).startOf('day').toISO() }}
{{ DateTime.fromISO($('Source').item.json.due).diffNow('days').days }}
```

The DateTime node exists for human users browsing the canvas. Use Luxon in expressions.

### Method Chains

```ts
// Filter + map + join
{{ $json.tags.filter(tag => tag.active).map(tag => tag.name).join(', ') }}

// Find one matching item from another node
{{ $('Get Models').all().find(model => model.json.id === $json.modelId).json.modelName }}

// Aggregate across all items
{{ $('Get Entries').all().map(i => i.json).filter(e => e.eligible).length }}
```

**`executeOnce: true` when using `.all()` for aggregation** — otherwise the node runs N times doing the same full-dataset work. Exception: if `.all()` is combined with `$other.item.json.x` to do per-item lookup (not aggregation), leave `executeOnce` off.

### Multi-Line Logic (IIFE)

When logic is too complex for one line but operates on a single item:

```ts
{{ (() => {
    const items = $json.line_items
    const subtotal = items.reduce((sum, item) => sum + item.price * item.qty, 0)
    const tax = subtotal * 0.08
    return (subtotal + tax).toFixed(2)
})() }}
```

IIFE runs in-process (~2ms vs Code node's ~500ms in a sandboxed VM). Use IIFE before reaching for a Code node for single-item transforms.

### JSON Serializers

- **`.toJsonString()`** → compact JSON. Use in AI prompts (saves tokens).
- **`JSON.stringify(value, null, 2)`** → pretty-printed. Use in emails, Slack messages, human-readable output.

### Type Wrapping

Fields that need to receive a non-string type require the `={{ ... }}` prefix:

```ts
// Number
count: '={{ 100 }}'

// Boolean
active: '={{ true }}'

// Object
config: '={{ { "valid": true } }}'

// Array
tags: '={{ ["a", "b"] }}'
```

### Useful Idioms

```ts
// Default when field might be missing
{{ $json.id || "fallback" }}
{{ $json.user?.profile?.id ?? "anonymous" }}

// ISO timestamp
{{ new Date().toISOString() }}

// Cross-node reference (preferred)
{{ $('Webhook Trigger').item.json.body.customer_id }}

// Conditional
{{ $json.status === 'active' ? 'yes' : 'no' }}
```

### Expression Anti-Patterns

| Anti-pattern | Fix |
|---|---|
| `$json.x` deep in multi-branch workflow | `$('Source Node').item.json.x` |
| DateTime node to format a date | `{{ DateTime.fromISO(...).toFormat('yyyy-MM-dd') }}` |
| Set node building email HTML, then Email node reads it | Inline the HTML directly in the email node's body field |
| `$json.foo.bar` without checking `$json.foo` exists | `$json.foo?.bar` |
| Branches converge with `$json` references downstream | Insert NoOp convergence node, reference by name |

---

## Code Nodes: Decision Tree

```
Need custom logic?
├── Single-field transform → Expression: {{ $json.foo.toUpperCase() }}
├── Multi-line, pure data shaping → Arrow function in Edit Fields
├── Multi-source aggregation, external libs, stateful → Code node
└── Two separate transforms? → Two nodes (Edit Fields → Edit Fields)
```

Code node rules when truly needed:
- One transformation per node. No routing logic, no API calls, no business rules.
- Default JavaScript. Python only when user explicitly asked.
- `$input.all()` for multi-item processing.
- `$input.first().json` for single-item.

---

## Error Handling

### API-Shaped Workflows (Webhook + Respond to Webhook)

Every fallible node needs:
1. `onError: 'continueErrorOutput'` in node config
2. `output(1)` wired to an error handler

Both are required. One without the other = silent failure mode.

Every error branch must end at a `Respond to Webhook`. Hanging error branches = caller timeout.

Status codes map to cause: caller's fault → 4xx, your fault → 5xx. Never 200 on an error path.

### Transient Failures: retryOnFail

Configure on any node making a network call (HTTP Request, Slack, Gmail, OpenAI, DB):

```ts
{
    retryOnFail: true,
    maxTries: 3,
    waitBetweenTries: 5000,  // ms, 5000 is the max
}
```

Absorbs transient 429s so the error output only fires on real failures.

### Unattended Workflows (Scheduled, Queue, Agent Tool)

Configure a workflow-level error workflow in the n8n UI (workflow Settings). Catches what escapes per-node handling: timeouts, crashes between nodes, errors in unwired nodes.

### Error Log Template

```javascript
// Code Node: "Format Error Log"
const error = $input.first().json;

return [{
  json: {
    workflow_name: "{{ $workflow.name }}",
    node_name: "{{ $node.name }}",
    error_type: "data_quality | api_failure | schema_mismatch | rate_limit | auth | unknown",
    error_message: error.message || JSON.stringify(error),
    input_data: $input.first().json,
    timestamp: new Date().toISOString(),
    severity: "error"
  }
}];
```

Route output to: Notion error log, Slack, or email.

### Feedback Loop

- **Error classification**: every error typed — `data_quality | api_failure | schema_mismatch | rate_limit | auth | unknown`
- **Recurrence detection**: same `workflow + node + error_type` 3+ times in 7 days = mandatory workflow audit
- **Run logging**: every execution writes records in / processed / failed / success rate / duration
- **Health thresholds**: success rate < 80% → halt + alert; 4+ recurring errors → halt + audit

---

## Credentials

1. **Secrets via credential system, never in text fields or SDK code.** A Set node hardcoding a token is a text field with extra steps.
2. **List credentials, then bind by ID.** Call `list_credentials({type})` before configuring any auth-needing node. One match: bind via 2-arg `newCredential('Label', 'credId')`. Multiple matches: ask the user which. The 1-arg `newCredential('Label')` is a placeholder — n8n auto-assigns most recently edited credential of that type, silently picks wrong one when user has multiples.
3. **Credential creation is the user's job.** The n8n MCP doesn't expose credential creation. Tell the user the exact credential *type* to create in the UI, then reference by label.
4. **Scope minimally** — read-only when write isn't needed.
5. **Naming**: `Apollo_Prod`, `Notion_Main`, `Instantly_Presold`
6. **If user pastes a secret in chat**: don't put it in a text field even temporarily. Bind to an existing credential if possible. Tell them: "Rotate this token — treat it as leaked."

---

## Sub-Workflows

**Search before building.** `search_workflows({ query: 'Subworkflow' })` — discover what already exists before writing duplicate logic.

**Decision tree:**
```
About to write a logic chunk?
├── Could it be needed in another workflow? → Extract to sub-workflow
├── Is it >5 nodes doing one conceptual thing? → Probably extract
├── Is it a generic concern (auth, retry, parsing, formatting)? → Almost certainly extract
└── Is it one HTTP call with no logic? → Keep inline
```

**Naming prefix**: `Subworkflow: Parse RFC2822 date` — the prefix is what `search_workflows` matches on.

**Trigger mode**: Use `Execute Workflow Trigger` with "Define Below" and typed fields (not passthrough). Exception: sub-workflow receives binary, or takes no inputs at all.

**Return natural shapes**, not storage shapes. If a sub-workflow reads from a Data Table string column holding JSON, parse it before returning — callers should receive arrays as arrays, not stringified blobs.

---

## Debugging Protocol

When something breaks, 80% of causes:
1. **Parameter misconfiguration** → `validate_node_config` on failing node, compare against `get_node_types`
2. **Upstream data stripped** → trace `$json.x` references back; look for intermediate nodes (Aggregate, HTTP-binary, Code in Run-for-All) that replace `$json` with their own output. Fix: reference by node name.
3. **Paths misconnected** → inspect `connections` object in `get_workflow_details`
4. **Item context lost** → downstream of Aggregate/Execute Once: use `$input.all().find(...)` or add a Merge anchor

**Step-by-step:**
1. What did they expect vs. what happened? Get the specific error message.
2. `get_execution({ id })` — which node failed, what input, what error.
3. `get_workflow_details({ id })` — actual current state + connections object.
4. `get_node_types([{ name, resource, operation }])` — compare actual parameter shape vs. configured.
5. `test_workflow` with pinned data — isolates "workflow broken?" from "input weird?"
6. If steps 1–5 pass and behavior is still wrong: check n8n instance version + skill version drift.

**Believe the user.** "This isn't working" means something isn't behaving as expected. Don't dismiss with "it should work." Investigate first.

---

## Data Hygiene Rules

1. **Normalize strings**: trim whitespace, lowercase emails, strip special chars before writing
2. **Null checks**: gate on required field existence before downstream operations
3. **Type coercion**: explicitly cast in Set or Code nodes (string → number, etc.)
4. **Deduplication**: check for existing records before creating (Notion query or Apollo lookup)
5. **Timestamps**: always ISO 8601 (`{{ new Date().toISOString() }}`)
6. **IDs over names**: store external IDs (Apollo ID, Notion page ID) — never reference by name alone

---

## JSON Schema: Standard Workflow Payload

All inter-node payloads conform to this base schema. Extend per workflow.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "status", "source", "created_at"],
  "properties": {
    "id": { "type": "string", "description": "Unique identifier from source system" },
    "status": {
      "type": "string",
      "enum": ["new", "processing", "complete", "error"],
      "description": "Pipeline status of this record"
    },
    "source": { "type": "string", "description": "Origin system — e.g. apollo, webhook, manual" },
    "created_at": { "type": "string", "format": "date-time" },
    "metadata": { "type": "object", "description": "Arbitrary key-value context for this record" }
  }
}
```

---

## Standard Workflow Patterns

### Pattern A: Trigger → Enrich → Store

```
[Trigger] → [Validate Input] → [Enrich via API] → [Transform Data] → [Upsert Destination] → [Log Success]
                ↓                     ↓                                        ↓
           [Error Handler]      [Error Handler]                         [Error Handler]
```

### Pattern B: Poll → Diff → Sync

```
[Schedule Trigger] → [Fetch Source Records] → [Fetch Destination Records]
                                                        ↓
                                            [Merge: Compare Keys]
                                                        ↓
                            [New Records] → [Create] → [Log]
                            [Changed Records] → [Update] → [Log]
                            [No Change] → [Skip]
```

### Pattern C: Webhook → Route → Multi-Destination

```
[Webhook] → [Parse + Validate] → [Switch: Route by Type]
                                         ↓          ↓
                                    [Path A]    [Path B]
                                         ↓          ↓
                                   [Write A]  [Write B]
                                         ↓          ↓
                                   [Merge: Confirm Both] → [Respond 200]
```

---

## Rodney's Active Stack: Apollo → Notion → Instantly

Reference for all Pre-Sold Protocol workflow builds.

**Pipeline Stages:**
1. `Curate` — Apollo search → raw lead list
2. `Qualify` — Fetch website → pass/fail filter → write status to Notion
3. `Research` — Fetch homepage → extract Company + Audience Intelligence → Notion
4. `Compose` — Generate email assets → write to Notion subpages
5. `Package` — Format asset pages in Notion CRM record
6. `Deliver` — Push verified leads + email copy to Instantly campaign

---

## Response Protocol

1. **Identify request type**: New build | Debug | Refactor | QA design | Architecture review
2. **If new build**: Phase 0 Blueprint first — confirm before building. Run `get_sdk_reference` before writing code.
3. **If debug**: Load Debugging Protocol section. Use `get_execution` + `get_workflow_details` before guessing.
4. **If refactor**: Audit against Operating Principles, flag violations, propose clean version.
5. **If QA/validation**: Design guard nodes, boundary checks, and run log first.
6. **Output format**: Always include node list, data flow diagram (text), and JSON schema for key payloads.
7. **Every phase has a "done" signal.** Status advances only after write confirmed. Never optimistically.

---

## Reference Files

Load when relevant — don't load all upfront:

| File | Load When |
|------|-----------|
| `references/qa-validation-feedback.md` | Designing QA gates, validation nodes, idempotency checks, feedback loop, run logging, pre-activation checklist |
| `references/best-practices.md` | Auditing a workflow, reviewing architecture decisions |
| `references/node-patterns.md` | Specific node config patterns, expressions, or copy-paste templates |
| `references/error-handling.md` | Error routing, retry logic, debugging silent failures |
