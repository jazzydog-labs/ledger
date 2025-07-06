You are a senior Python architect. Refine the architecture of **Loom**, a Typer-based CLI that orchestrates a “foundry” of Git repos.

---

### Existing Context (snapshot)

```
src/
  main.py   → Typer entry; delegates to LoomController
  core/     → ConfigManager, GitManager, RepoManager
  utils/    → EmojiManager, ColorManager, RepoStatusReader (parallel)
  views/    → RepoView (rich)
  commands/ → individual CLI sub-commands, git/* for git verbs
```

### Functional Objectives

1. Query repo status from anywhere (rich, “locally remote” view).
2. Run loom-approved commands inside any managed repo.
3. Map generic commands (e.g., `run-all-tests`) to repo-specific actions via BOM metadata.
4. Stash changes across **all** repos.
5. “Freeze” current commits across repos → tag, bump version, commit to BOM.
6. Checkout a specific freeze.
7. Any other high-leverage features for local platform dev.


**1. Revised `src/` package tree**

```
src/
  cli/            → Typer commands; translate CLI verbs into application commands
  app/            → orchestration layer; LoomController + use-case façades
  domain/         → pure DDD aggregates (Repo, Foundry, FreezeSnapshot), VOs, policies
  services/       → stateless domain services (RepoStatusSvc, FreezeSvc, BulkExecSvc)
  infra/          → gateways to Git, FS, Shell; transactional boundaries
  plugins/        → entry-point registry of repo-specific “adapters” (pytest, npm, etc.)
  events/         → domain + integration events; simple in-proc bus
  utils/          → Emoji, Color, parallelism helpers, small value helpers
  views/          → Rich/TUI presenters (tables, progress, diff)
```

---

**2. Interaction sketch**

```
CLI(cmd) → app.LoomController → services.* → infra.GitGateway ↔ Git CLI
                                    ↘ events.bus → views.Rich
plugins.* register with services.BulkExecSvc at startup
```

---

**3. New abstractions / services**

| Component                    | Role                                                                                   |
| ---------------------------- | -------------------------------------------------------------------------------------- |
| **FreezeSnapshot** aggregate | Captures commit SHAs + BOM hash for all repos                                          |
| **FreezeSvc**                | `create_freeze(tag)` & `checkout(freeze_id)` orchestrate tag, version bump, BOM commit |
| **BulkExecSvc**              | Fan-out execution of vetted commands across repos with progress + failure roll-up      |
| **StashCoordinator**         | One-shot stash/unstash across repos preserving branch/dirty state                      |
| **Event bus**                | Publishes `FreezeCreated`, `RepoStatusUpdated`, etc. for async hooks/logging           |

---

**4. Patterns / principles**

* **DDD aggregates & policies** keep Git details out of business logic
* **CQRS**: read side (`RepoStatusReader` parallel) vs. command side (`BulkExecSvc`)
* **Plugin registry (Python entry\_points)** for per-repo action mapping
* **Unit of Work** inside infra layer for multi-repo transactional safety
* **Event sourcing-lite** for immutable FreezeSnapshots, enabling time-travel checkouts

---

**5. Cross-cutting concerns to plan**

* Telemetry & structured logging of every bulk op / freeze event
* Local cache of Git metadata (commit graph, status) to avoid churn
* Policy enforcement (allowed commands, branch protections, exec timeouts)
* Secrets handling for repo credentials; SSH/GPG key management
* Concurrency limits + circuit breakers around mass shell invocations
* CLI auth context (who ran what) for audit trails and future multi-user mode

Your task:
- Create a walking skeleton of all the concerns listed above
- This includes directory structure, skeleton code (that can just log to console: "todo: implement <feature>"
- this includes a trivial test case for each feature
- this includes adding in the test so we can run it with `just test` and pytest
- this includes injection of features, e.g. controllers, utils, etc
- this includes concise, minimal documentation updates
- Add a well-thought-out hierarchy of todos for how to implement these features
- This todo hierarchy could be extensive, but that is great.
- Assume an extremely high level of domain expertise, so only point to high-level features in the todo, do not explain how to do it
- DO NOT REFACTOR EXISTING CODE YET -- add that to the TODO.md for someone else to do later