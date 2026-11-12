# 3B Framework — Execution Reference

Use this reference when building the Project Execution Plan in Phase 3. The 3B Framework structures all technical builds in three sequential phases. The sequence is rigid — Brain before Blueprint, Blueprint before Build. Execution within each phase is flexible.

---

## The 3 Phases

### BRAIN — Intelligence Gathering
*No code written here. This is the research and alignment phase.*

Goals:
- Confirm market research from Phase 2 is sufficient or identify gaps
- Gather any additional technical docs, API references, or design inspiration
- Lock the north star: one sentence, one success metric

Done when: You have everything needed to write the PRD without guessing.

---

### BLUEPRINT — Scope Lock
*The PRD is the Blueprint. This phase produces and finalizes it.*

Goals:
- Complete the PRD template with all sections populated
- Define MVP hypothesis and 3-feature max
- Build the Post-MVP Quarantine list — every cut feature goes here, not in the trash
- Confirm tech stack is the simplest option that tests the hypothesis

Done when: PRD is complete, scope is locked, quarantine list exists.

**Complexity check:** If the tech stack section has more than 3 libraries, push back. Ask: "What's the simplest stack that proves the hypothesis?"

---

### BUILD — Execution Engine
*Strict separation: logic engine first, UI second. Never touch the frontend until data flows.*

#### Step 1: Logic Engine (Backend/Data)
- Connect data sources, build core processing, validate data flow
- Use MCP integrations as direct data connections rather than writing setup code
- Treat MCPs like USB-C cables — plug in directly

**Engine Check (mandatory checkpoint):**
> Is data flowing from input to output correctly?
> - YES → move immediately to UI. Stop touching the backend.
> - NO → stay here. Fix the data connection. Do not proceed.

#### Step 2: Interface (Frontend/UI)
- Build the UI after the engine check passes
- Use screenshot-based feedback for layout fixes — circle the problem, describe the fix
- Use pre-built component libraries over custom designs when stuck

**3-Prompt Stop-Loss Rule:**
If the AI fails to produce the correct output after 3 attempts on the same problem:
- Stop. Do not attempt a 4th iteration.
- Pivot to a simpler alternative (pre-built template, different library, simplified design)
- A working solution today beats a perfect solution that's 3 days away.

**Launch Decision (mandatory checkpoint):**
> Does data flow? Does the UI satisfy the core success metric?
> - YES → ship it. Add remaining aesthetic preferences to the quarantine list. Push to a live URL.
> - NO → identify whether this is a critical break or a stylistic preference. Only critical breaks block launch.

---

## Pivot Optionality

The sequence is fixed. The tools are flexible.

- **Data pivot:** If the planned database or integration is failing, switch to a simpler solution (Google Sheets, SQLite, standard SQL table). The goal is data flow, not the specific tool.
- **UI pivot:** If a custom design cannot be replicated, abandon it. Use a standard component library. A functional button today beats a beautiful button next week.
- **Root defect rule:** If the same piece of code keeps breaking, stop fixing the symptom. Go back to the original prompt/instructions, find the flaw, and rebuild the step from scratch.

---

## Key Principle

> The ultimate success metric is a working project at a live URL. Exercise whatever technical flexibility is required to reach that URL.
