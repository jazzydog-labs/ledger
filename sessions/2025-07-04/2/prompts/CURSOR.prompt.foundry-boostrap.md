
```text
You are tasked with creating the initial version of a repository called `foundry-bootstrap`. This repository is the canonical bootstrapper for the `foundry` ecosystem — a local-first, agent-augmented, multi-repo environment. It sets up global tooling and environment configuration so that all related projects (`foundry`, `anvil`, `archives`, etc.) work consistently across machines.

---

## 🔧 Goals

- Install global development tools and environment dependencies.
- Use **bash only for early-stage bootstrapping** — ideally just enough to get Python (or another orchestrator) up and running.
- After Python is bootstrapped, **delegate orchestration to Python scripts** or another more structured tool.
- Store tool declarations (e.g. brew formulas, pyenv versions, pipx packages) in **structured configuration files**, not in scripts.

---

## 🗂️ Repository Layout (Initial)

```

foundry-bootstrap/  
├── bootstrap.sh # Entry point: minimal bash  
├── install/  
│ ├── install_brew.sh # Installs Homebrew if missing  
│ ├── install_pyenv.sh # Installs pyenv and sets global Python  
│ ├── install_python.sh # Installs Python 3.12 (via pyenv)  
│ └── setup_python_orchestrator.sh # (optional) bootstraps pipx, poetry, etc.  
├── config/  
│ ├── brew.yaml # Tools to install via brew  
│ ├── pipx.yaml # Python CLI tools  
│ ├── pyenv_version.txt # Python version  
│ └── envrc_template # Template for `.envrc`  
├── orchestrate/  
│ └── main.py # Python entrypoint for tool orchestration  
├── README.md

```

---

## ⚙️ Required Tools and Philosophy

### Initial Install via Bash (minimal)
- Homebrew
- pyenv
- Python 3.12 via pyenv
- Python tool bootstrapper (e.g. pipx)

### After Python is Available
- All other orchestration (e.g. `brew install`, `pipx install`) should be run through Python.
- These tools and versions should be defined in config files (e.g., YAML or TOML), **not hardcoded** in orchestration logic.
- Python orchestration script should:
  - Parse tool configuration
  - Check installed versions
  - Install missing tools via subprocess
  - Log clearly, exit safely

### Suggested Global Tools (defined in config)
- `direnv`
- `just`
- `gh` (GitHub CLI)
- `jq`, `fzf`, `ripgrep`, `bat`
- Python CLIs like `black`, `mypy`, `ruff`, `poetry`, `cookiecutter` via `pipx`

---

## 📜 Bootstrap Flow

1. `bootstrap.sh` (bash):
   - Installs brew, pyenv, and Python 3.12
   - Boots a minimal Python environment (pipx or venv)
   - Hands off to Python orchestrator (`main.py`)

2. `main.py` (Python):
   - Reads config files
   - Installs brew packages, pipx CLIs, any other global tools
   - Optionally sets up dotfiles, shell hooks, etc.

---

## 🔄 Extensibility

Future additions should follow these patterns:
- All declarative tool lists go in `config/` (YAML preferred)
- Tool-specific logic (e.g. brew, pipx, npm, asdf) goes in plugins or modules
- No procedural tool installs in bash — treat bash as a bootloader

---

## 📘 README

Ensure the README explains:
- Purpose of `foundry-bootstrap`
- How to run the bootstrap flow
- How to customize the tool list (edit config files)
- How to extend orchestration logic (plug in new types of tools)

---

## 🧠 Summary

Minimize:
- Bash scripting
- Hardcoded tool lists

Emphasize:
- Declarative config
- Python or specialized orchestrators
- Extensible architecture

```