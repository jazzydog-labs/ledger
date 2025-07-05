# Ledger Scripts

This directory contains utility scripts for managing the ledger sessions.

## Scripts

### `new_phase.py`
Creates a new phase directory for the current date in the sessions directory. If the session (date directory) does not exist, it will be created automatically.

**Usage:**
```bash
python ledger/scripts/new_phase.py [optional_description]
```

**Features:**
- Automatically creates date (session) directory if it doesn't exist (YYYY-MM-DD format)
- Finds the next available phase number (1, 2, 3, etc.)
- Creates the required directory structure:
  - `prompts/` - For raw prompt files
  - `artifacts/` - For AI model outputs and summaries
  - `metadata.yml` - Phase metadata with timestamp and description
  - `summary.md` - Template for phase documentation

**Example:**
```bash
# Create a new phase for today
python ledger/scripts/new_phase.py "Working on user authentication"

# Create a new phase with default description
python ledger/scripts/new_phase.py
```

### `log.sh`
Existing logging utility script.

## Directory Structure Created

When you run `new_phase.py`, it creates:

```
sessions/YYYY-MM-DD/N/
├── prompts/          # Raw prompt files
├── artifacts/        # AI model outputs
├── metadata.yml      # Phase metadata
└── summary.md        # Phase documentation
```

Where:
- `YYYY-MM-DD` is the current date (session)
- `N` is the next available phase number 