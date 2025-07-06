**Prompt for AI Architect**

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

---

### Your Task

Produce an **ultra-concise** high-level design:

1. **Revised `src/` package tree** – list dirs/modules & one-line purpose each.
2. **Interaction sketch** (ASCII arrows ok) showing control flow between layers.
3. New abstractions/services/events enabling freeze/checkout & bulk ops.
4. Key patterns/principles leveraged (CQRS, DDD, plugin registry, etc.) – one line each.
5. Missing cross-cutting concerns to plan for (telemetry, caching, policy, security).

Assume expert audience; hint at mechanisms, do **not** explain basics.