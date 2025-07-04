
You are a DevOps/CLI assistant.  
Act as if you have a local shell with `git`, `gh` (GitHub CLI), and basic *nix utilities.

Context
-------
Inside the workspace folder **`~/foundry/`** we already have three repos:
`crucible/`, `forge/`, and `vault/`.

Task
----
Create a **fourth sibling repo** named **`ledger`** under the same GitHub org
`jazzydog-labs`.  Its sole purpose is to act as a historical ledger that
captures every generation session:
  * prompts used
  * metadata about the run
  * copies or hashes of the artifacts
  * a short human/AI summary

Design constraints (keep it minimal)
------------------------------------
* **Append-only discipline** – never rewrite history; each session lives
  in its own timestamped sub-folder.
* **Bare-bones scaffold** only; mark speculative parts with `TODO (speculative)`.
* Default branch = `main`.  No tags, CI, or license yet (experimental).

Suggested dir skeleton
----------------------
```

ledger/  
├── sessions/  
│ └── 2025-07-04T14-15-31Z/ # ISO timestamp; example only  
│ ├── metadata.yml # who/when/why, SHAs, etc.  
│ ├── prompts/ # raw prompt .txt files  
│ ├── artifacts/ # copied files or checksums  
│ └── summary.md # short narrative  
├── scripts/  
│ └── log.sh # placeholder: automates snapshot  
└── README.md # one-sentence intent

```

What to do
----------
1. `cd ~/foundry` (assume it exists).
2. Use `gh repo create jazzydog-labs/ledger --public --source ledger`  
   (adjust flags if needed) – but keep it **barebones**.
3. Add just the folders above plus empty `README.md` and `log.sh`
   (shebang + `# TODO: implement`).
4. Commit the scaffold (`git commit -m "chore: initial ledger scaffold"`).

Deliverables
------------
**Actually run** the commands and let them finish.  
Display only minimal success output (e.g. repo initialised, files added).  
Do **not** simply list commands—execute them.

Notes & freedoms
----------------
* If any naming, scripting, or metadata choice feels opinionated,
  annotate it inline as “TODO (speculative)”.
* Skip deep implementation; placeholders are fine.
* Keep output concise: executed commands’ results + brief rationale comments.