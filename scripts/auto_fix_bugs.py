#!/usr/bin/env python3
"""
Automated Bug Fix Script

Automatically fixes common code quality issues found by the testing script.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str], cwd: Path, description: str) -> bool:
    """Run a command and return success status."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0:
            print(f"   ✅ Success")
            return True
        else:
            print(f"   ⚠️  Some issues remain")
            return False
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        return False


def main():
    """Main entry point."""
    root_dir = Path(__file__).parent.parent
    backend_dir = root_dir / "backend"

    print("=" * 80)
    print("Automated Bug Fixing")
    print("=" * 80)
    print()

    fixes_applied = 0

    # Fix 1: Remove unused imports with autoflake
    print("🔍 Fixing unused imports...")
    try:
        result = subprocess.run(
            ["pip", "install", "autoflake", "-q"],
            capture_output=True,
            timeout=60,
        )
        if result.returncode == 0:
            if run_command(
                ["autoflake", "--remove-all-unused-imports", "--in-place", "--recursive", "src"],
                backend_dir,
                "Removing unused imports"
            ):
                fixes_applied += 1
    except Exception as e:
        print(f"   ⚠️  Could not install autoflake: {e}")

    # Fix 2: Auto-fix ruff issues
    if run_command(
        ["ruff", "check", "src", "--fix"],
        backend_dir,
        "Auto-fixing ruff issues"
    ):
        fixes_applied += 1

    # Fix 3: Format code with ruff
    if run_command(
        ["ruff", "format", "src"],
        backend_dir,
        "Formatting code with ruff"
    ):
        fixes_applied += 1

    # Fix 4: Update type hints (Python 3.10+ style)
    print()
    print("💡 Manual fixes needed:")
    print("   - Replace `List` with `list` in type hints")
    print("   - Replace `Dict` with `dict` in type hints")
    print("   - Replace `Optional[X]` with `X | None`")
    print("   - Replace `datetime.timezone.utc` with `datetime.UTC`")
    print("   - Replace `== True` with truth checks")
    print()
    print(f"✅ Applied {fixes_applied} automated fixes")
    print()
    print("Run './scripts/test_and_index_bugs.py' again to verify fixes")


if __name__ == "__main__":
    main()
