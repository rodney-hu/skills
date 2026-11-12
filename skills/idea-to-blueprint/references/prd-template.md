# PRD Template — Technical Builds

Use this template when the project type is **Asset** (tool with UI) or **Workflow** (automation/background processing). Populate every section using context gathered in Phases 1 and 2. Do not re-ask questions already answered — map existing answers to the appropriate fields.

---

# [Project Name] — PRD

**Purpose:** Single source of truth for what gets built. Defines features, data contracts, acceptance criteria, and constraints.

---

## 1. Project Overview

### Project Name
`[project-name]` *(kebab-case)*

### Project Type
- [ ] Asset (web-based tool with UI)
- [ ] Workflow (automation/background processing)

### Goal
*One sentence describing what problem this solves.*

### User
*[Who] doing [what] in [context] needs [outcome].*

### Success Metric
*One number that proves this works.*
Format: [Metric] of [Value] within [Timeframe]

---

## 2. Tech Stack

**Frontend:**
- Framework: [React 18 / Next.js 14 / Vue 3 / None]
- UI Library: [shadcn/ui / Tailwind / None]
- State Management: [Zustand / Context / None]

**Backend:**
- Runtime: [Node.js / Python / None]
- Framework: [Express / FastAPI / None]
- Database: [Supabase / PostgreSQL / SQLite / None]

**Special Libraries:**
- [Library]: [Purpose]

**Hosting:**
- Platform: [Vercel / Netlify / Railway / Local]
- Auth: [Supabase Auth / Clerk / None]

*If using standard patterns, write "Standard React + Supabase stack"*

---

## 3. Skills & Integrations

### Skills to Load
- `[skill-name]`: [Purpose]

*Write "None" if no additional skills needed.*

### MCP Servers
- `[server-name]`: [Integration purpose]
  - Endpoints: [key functions]
  - Auth: [requirements]

*Write "None" if no MCP integrations.*

### External APIs
- **[Service]:** [Purpose] — [Docs URL]

*Write "None" if fully standalone.*

---

## 4. Architecture

### Folder Structure
```
/src
  /[custom-folder]: [Purpose]
```
*Write "None — using standard structure" if no additions.*

### Special Patterns
*Any project-specific architecture patterns.*

*Write "None — following standard patterns" if no deviations.*

---

## 5. Data Model

### Core Types
```typescript
type [Entity] = {
  id: string
  // fields...
}
```

### Relationships
*[Entity A] → [Entity B] (1:many), etc.*

---

## 6. Input/Output Contract

### Input
*What data comes in? (form inputs, API response, CSV, database query)*

### Processing
*What happens to the data? (calculate, filter, aggregate, transform)*

### Output
*What's produced? (dashboard view, CSV, PDF, API response)*

### Sample Data
```json
[
  { "field": "value" }
]
```

---

## 7. Features & Scope

### MVP Features — Ship First
*Maximum 3 features. Each must directly test the MVP hypothesis.*

#### Feature 1: [Name]
**Description:** What it does in 1-2 sentences.

**Acceptance Criteria:**
- [ ] Specific testable condition
- [ ] Specific testable condition
- [ ] Specific testable condition

**Dependencies:** [Other features this requires, or "None"]

#### Feature 2: [Name]
**Description:** What it does in 1-2 sentences.

**Acceptance Criteria:**
- [ ] Specific testable condition
- [ ] Specific testable condition

**Dependencies:** [None]

#### Feature 3: [Name] *(only if required to test hypothesis)*
**Description:** What it does in 1-2 sentences.

**Acceptance Criteria:**
- [ ] Specific testable condition

**Dependencies:** [None]

---

### Post-MVP Quarantine
*Everything cut from v1 goes here — not deleted, quarantined.*

- [Feature]: [Why it's post-MVP]
- [Feature]: [Why it's post-MVP]

### Explicitly Out of Scope (v1)
*Features we are NOT building in this version, full stop.*

- [Feature]
- [Feature]

---

## 8. Constraints

### Critical Edge Cases (MVP Only)
- **No data state:** [How should the UI look?]
- **API failure:** [Fallback behavior?]
- **Invalid input:** [Validation rules?]

*All other edge cases (large datasets, slow connections) → Post-MVP.*

### Performance Requirements
- **Load time:** [e.g., "<2 seconds initial load"]
- **Max records:** [e.g., "Handle 1,000 entries"]
- **Users:** [e.g., "Single user" or "100 concurrent"]

### Technical Constraints
- **Must use:** [e.g., "Supabase RLS for all queries"]
- **Cannot use:** [e.g., "No third-party analytics"]
- **Special requirements:** [e.g., "Must work offline"]

---

## 9. Environment Setup

### Required Environment Variables
```bash
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
```

### Initial Setup Steps
1. [Step]
2. [Step]

---

## 10. Success Checklist

### MVP Complete When:
- [ ] All MVP features pass acceptance criteria
- [ ] Deployed to [platform]: [URL]
- [ ] Success metric validated: [reference from Section 1]
- [ ] Error handling implemented
- [ ] README complete
