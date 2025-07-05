ledger – historical ledger of all generation sessions.

## Workflow

1. Each day gets a new directory in `sessions` (e.g., `YYYY-MM-DD`).
2. Each distinct piece of work within a day gets a new sequentially numbered subdirectory (e.g., `1`, `2`, `3`).
3. Each work directory contains `prompts`, `artifacts`, `metadata.yml`, and `summary.md`.

## Directory Structure

### `prompts/`
Raw prompt files used during the session (e.g., `.txt`, `.md` files sent to AI models).

### `artifacts/`
AI model outputs and summaries (e.g., ChatGPT summaries, Gemini responses, generated documentation).

### `metadata.yml`
Session metadata including date, duration, participants, tools used, and status.

### `summary.md`
Human-readable summary of the session, including goals, decisions, and outcomes.

## Important Notes

- **Artifacts are for AI interactions only** - Do not store generated code or repositories here
- **Generated code goes in its own repository** - Use the appropriate foundry ecosystem repository
- **Prompts and AI outputs are preserved** - These provide valuable context for future sessions