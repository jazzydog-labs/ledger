
# Foundry Conversation Summary
**Date:** 2025-07-04

## 1. Naming & Conceptual Metaphor
- Adopted a metallurgy theme:
  - **crucible** – brainstorming/ideation repository.
  - **forge** – AI–driven generator that turns briefs into immutable artifacts.
  - **vault** – canonical, read‑only registry for generated artifacts.
- Chose **foundry/** as the parent workspace folder that houses all three repos, reflecting a facility with multiple working stations.

## 2. Repository Scaffolds
- **crucible/**
  - Holds prompt templates, blueprints (entity briefs), exploratory notebooks, research materials.
  - No code‑gen or version tags; mutable drafts only.
- **forge/**
  - Contains AI/RAG models, code‑gen templates, pipeline configs, plugins, and an `out/` directory for artifacts.
  - Placeholder CLI aliases: `cru`, `fr`, `vl`.
- **vault/**
  - Stores immutable artifacts exactly as emitted by *forge*.
  - Source‑of‑truth rule: any change must be regenerated upstream rather than patched in place (Modular Encapsulation).
- **ledger/**
  - Added as a fourth repo to capture historical sessions.
  - Directory scheme: `sessions/<ISO‑timestamp>/` with `metadata.yml`, `prompts/`, `artifacts/`, `summary.md`.
  - Append‑only; snapshots automation via placeholder `log.sh`.

## 3. Gemini Prompts Crafted
1. **Trilogy Repos Prompt**  
   - Instructs Gemini to create `crucible`, `forge`, and `vault` inside the org with minimal READMEs, directory stubs, and placeholder scripts.
   - Emphasises speculative sections and excludes implementation details.
2. **Updated Prompt** (adds canonical vault rule).  
3. **CLI‑Execution Prompt** (asks Gemini to *run* commands, not list them).  
4. **Ledger Prompt** – builds the new `ledger` repo using the same minimal, speculative approach.

## 4. Alias & Workflow Notes
- Short placeholder executables (`cru`, `fr`, `vl`) reserved for future tooling.
- Typical developer commands sequence:  
  1. Draft in *crucible*.  
  2. Generate in *forge* (`forge smelt`).  
  3. Publish to *vault* (`forge ship`).  
  4. Snapshot run in *ledger* (`scripts/log.sh`).

## 5. Folder‑Name Discussion
- Considered **anvil/** (environment surface) vs **foundry/** (whole facility).  
- Settled on **foundry/** for breadth and inclusion of external tool calls & orchestrations.

---

*This markdown file acts as an artifact summarising the chat decisions and can be committed to `ledger/sessions/<timestamp>/summary.md`.*
