You are a DevOps/CLI assistant.  
Act as if you have a local shell with `git`, `gh` (GitHub CLI), and basic *nix utilities.

Goal (keep it high-level, minimal boilerplate)
----------------------------------------------
Create **three sibling Git repositories**—`crucible`, `forge`, and `vault`—inside the
`jazzydog-labs` org namespace.

High-level intent of each repo
------------------------------
1. **crucible** – ideation space.  
   *Holds only natural-language entity briefs and brainstorming aids.*

2. **forge** – generative factory.  
   *Consumes briefs, runs AI + CLI tooling, and emits immutable artifacts into `out/`.  
   Tooling names are **speculative** (placeholder aliases `cru`, `fr`, `vl`).*

3. **vault** – canonical, read-only registry.  
   *Stores released artifacts exactly as produced by **forge**.  
   **Vault is the single source of truth:** if we need to change generated code  
   (e.g. inject pre-validation into every controller), we MUST go back to  
   `crucible`/`forge`, regenerate, and re-publish—never patch code in place.  
   Projects that consume vault artifacts do so via configuration, not direct edits.*  
   _(MODULAR ENCAPSULATION BABY!)_

What to do
----------
* Create bare repos with a tiny README that states the intent above in one sentence.
* Scaffold **minimal** directory stubs only where obvious (`out/` in forge, maybe `blueprints/`
  in crucible).  Skip deep trees; mark anything uncertain as “TODO (speculative)”.
* Use short alias scripts (`cru`, `fr`, `vl`) as placeholders—empty executable files
  with a one-line comment like `# TODO: implement`.
* Default branch ≡ `main`.  No other branches or tags yet.
* No CI config, no language-specific files, no license (experimental).

Deliverables
------------
**Actually run** the shell commands in sequence and let them complete.  
Show only minimal CLI output confirmations (e.g., repo initialization messages).  
Do **not** merely list the commands—execute them.

Notes & freedoms
----------------
* If any step (e.g. choosing file structure or script shebang) feels opinionated,
  annotate it as “speculative—adjust later”.
* Do **not** flesh out generator commands, schema formats, or tooling internals.
  Leave those as TODO placeholders.
* Keep output focused: executed commands’ results + brief rationale comments; nothing else.