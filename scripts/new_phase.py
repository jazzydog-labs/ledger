#!/usr/bin/env python
"""
new_phase.py - Create a new phase directory for the current date
Usage: python new_phase.py [optional_description]
"""

import os
import sys
from ruamel.yaml import YAML
from datetime import datetime, UTC
from pathlib import Path
from typing import Optional


def get_sessions_directory() -> Path:
    """Get the sessions directory path relative to this script."""
    script_dir = Path(__file__).parent
    sessions_dir = script_dir.parent / "sessions"
    return sessions_dir


def get_next_phase_number(date_dir: Path) -> int:
    """Find the next available phase number for the given date directory."""
    if not date_dir.exists():
        return 1
    
    existing_phases = []
    for item in date_dir.iterdir():
        if item.is_dir() and item.name.isdigit():
            existing_phases.append(int(item.name))
    
    if not existing_phases:
        return 1
    
    return max(existing_phases) + 1


def create_metadata(date: str, phase: int, description: str) -> dict:
    """Create metadata dictionary for the phase."""
    return {
        "date": date,
        "phase": phase,
        "created_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
        "status": "active",
        "participants": [],
        "tools_used": [],
        "description": description
    }


def create_summary_template(date: str, phase: int) -> str:
    """Create summary template content."""
    return f"""# Phase {phase} - {date}

## Goals
- [ ] Define goals for this phase

## Decisions
- [ ] Document key decisions made

## Outcomes
- [ ] Document outcomes and results

## Notes
- Phase created automatically on {datetime.now().strftime('%c')}
"""


def create_phase_directory(description: str = "New phase created automatically") -> Path:
    """Create a new phase directory and return its path."""
    # Get current date and sessions directory
    current_date = datetime.now().strftime("%Y-%m-%d")
    sessions_dir = get_sessions_directory()
    date_dir = sessions_dir / current_date
    
    # Create date directory if it doesn't exist
    if not date_dir.exists():
        print(f"Creating new date directory: {date_dir}")
        date_dir.mkdir(parents=True, exist_ok=True)
    
    # Find next phase number
    phase_num = get_next_phase_number(date_dir)
    phase_dir = date_dir / str(phase_num)
    
    print(f"Creating new phase directory: {phase_dir}")
    phase_dir.mkdir(parents=True, exist_ok=True)
    
    # Create required subdirectories
    (phase_dir / "prompts").mkdir(exist_ok=True)
    (phase_dir / "artifacts").mkdir(exist_ok=True)
    
    # Create metadata.yml
    metadata = create_metadata(current_date, phase_num, description)
    yaml = YAML()
    yaml.default_flow_style = False
    with open(phase_dir / "metadata.yml", "w") as f:
        yaml.dump(metadata, f)
    
    # Create summary.md
    summary_content = create_summary_template(current_date, phase_num)
    with open(phase_dir / "summary.md", "w") as f:
        f.write(summary_content)
    
    return phase_dir


def main():
    """Main function to create a new phase."""
    try:
        # Get description from command line arguments
        description = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "New phase created automatically"
        
        # Create the phase directory
        phase_dir = create_phase_directory(description)
        
        # Print success message
        print("✅ New phase created:", phase_dir)
        print("📁 Structure:")
        print("   ├── prompts/")
        print("   ├── artifacts/")
        print("   ├── metadata.yml")
        print("   └── summary.md")
        print()
        print("You can now start working in this phase directory!")
        
    except Exception as e:
        print(f"❌ Error creating phase: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 