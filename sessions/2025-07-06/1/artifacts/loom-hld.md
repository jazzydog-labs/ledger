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