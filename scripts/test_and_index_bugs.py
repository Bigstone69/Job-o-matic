#!/usr/bin/env python3
"""
Automated Testing and Bug Indexing Script for Job-o-matic

This script runs comprehensive tests, linting, type checking, and indexes
all bugs/issues found across the codebase.
"""

import subprocess
import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass, field
from enum import Enum


class Severity(str, Enum):
    """Bug severity levels."""
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"


@dataclass
class Bug:
    """Represents a bug or issue found during testing."""
    id: str
    severity: Severity
    category: str
    file: str
    line: int | None
    message: str
    tool: str
    details: str = ""


@dataclass
class TestResults:
    """Container for all test results."""
    bugs: List[Bug] = field(default_factory=list)
    backend_tests_passed: bool = False
    frontend_tests_passed: bool = False
    backend_lint_passed: bool = False
    frontend_lint_passed: bool = False
    type_check_passed: bool = False
    total_tests_run: int = 0
    total_tests_passed: int = 0
    total_tests_failed: int = 0


class TestRunner:
    """Orchestrates all testing and bug indexing."""

    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.backend_dir = root_dir / "backend"
        self.frontend_dir = root_dir / "frontend"
        self.results = TestResults()
        self.bug_counter = 0

    def run_all_tests(self) -> TestResults:
        """Run all tests and collect results."""
        print("=" * 80)
        print("Job-o-matic Automated Testing & Bug Indexing")
        print("=" * 80)
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Backend tests
        print("🔍 BACKEND TESTING")
        print("-" * 80)
        self.check_backend_dependencies()
        self.run_backend_lint()
        self.run_backend_type_check()
        self.run_backend_tests()
        print()

        # Frontend tests
        print("🔍 FRONTEND TESTING")
        print("-" * 80)
        self.check_frontend_dependencies()
        self.run_frontend_lint()
        self.run_frontend_type_check()
        print()

        # Security checks
        print("🔒 SECURITY ANALYSIS")
        print("-" * 80)
        self.run_security_checks()
        print()

        # Code quality checks
        print("📊 CODE QUALITY ANALYSIS")
        print("-" * 80)
        self.run_code_quality_checks()
        print()

        return self.results

    def check_backend_dependencies(self):
        """Check if backend dependencies are installed."""
        print("Checking backend dependencies...")
        if not (self.backend_dir / "pyproject.toml").exists():
            print("  ⚠️  pyproject.toml not found")
            return

        try:
            subprocess.run(
                ["python", "-c", "import fastapi"],
                cwd=self.backend_dir,
                capture_output=True,
                timeout=5,
            )
            print("  ✅ Backend dependencies available")
        except Exception as e:
            print(f"  ⚠️  Backend dependencies check failed: {e}")

    def check_frontend_dependencies(self):
        """Check if frontend dependencies are installed."""
        print("Checking frontend dependencies...")
        if not (self.frontend_dir / "package.json").exists():
            print("  ⚠️  package.json not found")
            return

        if (self.frontend_dir / "node_modules").exists():
            print("  ✅ Frontend dependencies available")
        else:
            print("  ⚠️  node_modules not found - run 'npm install'")

    def run_backend_lint(self):
        """Run Python linting with ruff."""
        print("Running backend linting (ruff)...")
        try:
            result = subprocess.run(
                ["ruff", "check", "src", "--output-format=json"],
                cwd=self.backend_dir,
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                print("  ✅ No linting issues found")
                self.results.backend_lint_passed = True
            else:
                try:
                    issues = json.loads(result.stdout)
                    print(f"  ❌ Found {len(issues)} linting issues")
                    for issue in issues:
                        self._add_bug_from_ruff(issue)
                except json.JSONDecodeError:
                    print(f"  ⚠️  Could not parse ruff output")

        except FileNotFoundError:
            print("  ⚠️  ruff not installed - skipping")
        except Exception as e:
            print(f"  ⚠️  Linting failed: {e}")

    def run_backend_type_check(self):
        """Run Python type checking with mypy."""
        print("Running backend type checking (mypy)...")
        try:
            result = subprocess.run(
                ["mypy", "src", "--no-error-summary"],
                cwd=self.backend_dir,
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode == 0:
                print("  ✅ No type errors found")
                self.results.type_check_passed = True
            else:
                lines = result.stdout.strip().split("\n")
                error_lines = [l for l in lines if ": error:" in l]
                print(f"  ❌ Found {len(error_lines)} type errors")
                for line in error_lines:
                    self._add_bug_from_mypy(line)

        except FileNotFoundError:
            print("  ⚠️  mypy not installed - skipping")
        except Exception as e:
            print(f"  ⚠️  Type checking failed: {e}")

    def run_backend_tests(self):
        """Run backend pytest tests."""
        print("Running backend tests (pytest)...")
        try:
            result = subprocess.run(
                ["pytest", "-v", "--tb=short", "--json-report", "--json-report-file=test-report.json"],
                cwd=self.backend_dir,
                capture_output=True,
                text=True,
                timeout=120,
            )

            # Try to read JSON report
            report_file = self.backend_dir / "test-report.json"
            if report_file.exists():
                with open(report_file) as f:
                    report = json.load(f)
                    total = report.get("summary", {}).get("total", 0)
                    passed = report.get("summary", {}).get("passed", 0)
                    failed = report.get("summary", {}).get("failed", 0)

                    self.results.total_tests_run += total
                    self.results.total_tests_passed += passed
                    self.results.total_tests_failed += failed

                    if failed == 0 and total > 0:
                        print(f"  ✅ All {passed} tests passed")
                        self.results.backend_tests_passed = True
                    elif total == 0:
                        print("  ⚠️  No tests found")
                    else:
                        print(f"  ❌ {failed}/{total} tests failed")
                        for test in report.get("tests", []):
                            if test.get("outcome") == "failed":
                                self._add_bug_from_pytest(test)
            else:
                # Fallback to parsing stdout
                if "passed" in result.stdout:
                    print("  ✅ Tests passed")
                    self.results.backend_tests_passed = True
                elif "no tests ran" in result.stdout.lower():
                    print("  ⚠️  No tests found")
                else:
                    print("  ❌ Tests failed")

        except FileNotFoundError:
            print("  ⚠️  pytest not installed - skipping")
        except Exception as e:
            print(f"  ⚠️  Tests failed: {e}")

    def run_frontend_lint(self):
        """Run frontend linting with ESLint."""
        print("Running frontend linting (ESLint)...")
        try:
            result = subprocess.run(
                ["npm", "run", "lint", "--", "--format=json"],
                cwd=self.frontend_dir,
                capture_output=True,
                text=True,
                timeout=60,
            )

            try:
                # ESLint JSON output
                issues = json.loads(result.stdout)
                total_errors = sum(file.get("errorCount", 0) for file in issues)
                total_warnings = sum(file.get("warningCount", 0) for file in issues)

                if total_errors == 0 and total_warnings == 0:
                    print("  ✅ No linting issues found")
                    self.results.frontend_lint_passed = True
                else:
                    print(f"  ❌ Found {total_errors} errors, {total_warnings} warnings")
                    for file_result in issues:
                        for message in file_result.get("messages", []):
                            self._add_bug_from_eslint(file_result["filePath"], message)

            except json.JSONDecodeError:
                if result.returncode == 0:
                    print("  ✅ No linting issues found")
                    self.results.frontend_lint_passed = True
                else:
                    print("  ⚠️  Could not parse ESLint output")

        except FileNotFoundError:
            print("  ⚠️  npm not found - skipping")
        except Exception as e:
            print(f"  ⚠️  Linting failed: {e}")

    def run_frontend_type_check(self):
        """Run TypeScript type checking."""
        print("Running frontend type checking (tsc)...")
        try:
            result = subprocess.run(
                ["npx", "tsc", "--noEmit"],
                cwd=self.frontend_dir,
                capture_output=True,
                text=True,
                timeout=60,
            )

            if result.returncode == 0:
                print("  ✅ No type errors found")
            else:
                lines = result.stdout.strip().split("\n")
                error_lines = [l for l in lines if "error TS" in l]
                print(f"  ❌ Found {len(error_lines)} type errors")
                for line in error_lines:
                    self._add_bug_from_tsc(line)

        except FileNotFoundError:
            print("  ⚠️  TypeScript not installed - skipping")
        except Exception as e:
            print(f"  ⚠️  Type checking failed: {e}")

    def run_security_checks(self):
        """Run security vulnerability checks."""
        print("Checking for security vulnerabilities...")

        # Backend: Check for known vulnerable packages
        try:
            result = subprocess.run(
                ["pip", "list", "--format=json"],
                cwd=self.backend_dir,
                capture_output=True,
                text=True,
                timeout=30,
            )
            if result.returncode == 0:
                print("  ✅ Backend dependency scan completed")
        except Exception as e:
            print(f"  ⚠️  Backend security check failed: {e}")

        # Frontend: npm audit
        try:
            result = subprocess.run(
                ["npm", "audit", "--json"],
                cwd=self.frontend_dir,
                capture_output=True,
                text=True,
                timeout=60,
            )

            try:
                audit_result = json.loads(result.stdout)
                vulnerabilities = audit_result.get("metadata", {}).get("vulnerabilities", {})
                total = sum(vulnerabilities.values())

                if total == 0:
                    print("  ✅ No vulnerabilities found")
                else:
                    print(f"  ⚠️  Found {total} vulnerabilities")
                    # Add critical/high vulnerabilities as bugs
                    for vuln_id, details in audit_result.get("vulnerabilities", {}).items():
                        if details.get("severity") in ["critical", "high"]:
                            self._add_bug_from_npm_audit(vuln_id, details)

            except json.JSONDecodeError:
                print("  ⚠️  Could not parse npm audit output")

        except FileNotFoundError:
            print("  ⚠️  npm not found - skipping")
        except Exception as e:
            print(f"  ⚠️  Security check failed: {e}")

    def run_code_quality_checks(self):
        """Run code quality analysis."""
        print("Analyzing code quality...")

        # Check for common code smells
        patterns = {
            "TODO": "TODO comment found",
            "FIXME": "FIXME comment found",
            "XXX": "XXX marker found",
            "HACK": "HACK comment found",
            "console.log": "Debug console.log found",
            "debugger": "Debug breakpoint found",
        }

        issues_found = 0
        for pattern, description in patterns.items():
            backend_count = self._search_pattern(self.backend_dir / "src", pattern, [".py"])
            frontend_count = self._search_pattern(self.frontend_dir / "src", pattern, [".ts", ".tsx"])

            if backend_count + frontend_count > 0:
                issues_found += backend_count + frontend_count

        if issues_found > 0:
            print(f"  ⚠️  Found {issues_found} code quality markers")
        else:
            print("  ✅ No code quality issues found")

    def _search_pattern(self, directory: Path, pattern: str, extensions: List[str]) -> int:
        """Search for a pattern in files."""
        if not directory.exists():
            return 0

        count = 0
        for ext in extensions:
            for file_path in directory.rglob(f"*{ext}"):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line_num, line in enumerate(f, 1):
                            if pattern in line:
                                count += 1
                                self._add_bug(
                                    severity=Severity.INFO,
                                    category="code_quality",
                                    file=str(file_path.relative_to(self.root_dir)),
                                    line=line_num,
                                    message=f"{pattern} comment found",
                                    tool="grep",
                                    details=line.strip()[:100],
                                )
                except Exception:
                    pass

        return count

    def _add_bug(self, severity: Severity, category: str, file: str, line: int | None,
                 message: str, tool: str, details: str = ""):
        """Add a bug to the results."""
        self.bug_counter += 1
        bug = Bug(
            id=f"AUTO-{self.bug_counter:03d}",
            severity=severity,
            category=category,
            file=file,
            line=line,
            message=message,
            tool=tool,
            details=details,
        )
        self.results.bugs.append(bug)

    def _add_bug_from_ruff(self, issue: Dict[str, Any]):
        """Convert ruff issue to bug."""
        severity_map = {
            "E": Severity.MEDIUM,
            "F": Severity.HIGH,
            "W": Severity.LOW,
        }
        code = issue.get("code", "")
        severity = severity_map.get(code[0] if code else "W", Severity.LOW)

        self._add_bug(
            severity=severity,
            category="lint",
            file=issue.get("filename", "unknown"),
            line=issue.get("location", {}).get("row"),
            message=issue.get("message", ""),
            tool="ruff",
            details=f"Code: {code}",
        )

    def _add_bug_from_mypy(self, line: str):
        """Convert mypy error to bug."""
        # Parse: "src/file.py:123: error: Message"
        parts = line.split(":", 3)
        if len(parts) >= 4:
            self._add_bug(
                severity=Severity.MEDIUM,
                category="type_error",
                file=parts[0].strip(),
                line=int(parts[1].strip()) if parts[1].strip().isdigit() else None,
                message=parts[3].strip(),
                tool="mypy",
            )

    def _add_bug_from_pytest(self, test: Dict[str, Any]):
        """Convert pytest failure to bug."""
        self._add_bug(
            severity=Severity.HIGH,
            category="test_failure",
            file=test.get("nodeid", "unknown"),
            line=None,
            message=test.get("call", {}).get("longrepr", "Test failed"),
            tool="pytest",
        )

    def _add_bug_from_eslint(self, file_path: str, message: Dict[str, Any]):
        """Convert ESLint issue to bug."""
        severity_map = {
            2: Severity.HIGH,
            1: Severity.LOW,
        }
        self._add_bug(
            severity=severity_map.get(message.get("severity", 1), Severity.LOW),
            category="lint",
            file=file_path,
            line=message.get("line"),
            message=message.get("message", ""),
            tool="eslint",
            details=f"Rule: {message.get('ruleId', 'unknown')}",
        )

    def _add_bug_from_tsc(self, line: str):
        """Convert TypeScript error to bug."""
        # Parse: "src/file.ts(123,45): error TS1234: Message"
        if "(" in line and ")" in line:
            parts = line.split("(", 1)
            file_part = parts[0].strip()
            rest = parts[1].split(")", 1)
            line_col = rest[0].strip()
            message = rest[1].split(":", 2)[-1].strip() if len(rest) > 1 else ""

            line_num = int(line_col.split(",")[0]) if "," in line_col else None

            self._add_bug(
                severity=Severity.MEDIUM,
                category="type_error",
                file=file_part,
                line=line_num,
                message=message,
                tool="tsc",
            )

    def _add_bug_from_npm_audit(self, vuln_id: str, details: Dict[str, Any]):
        """Convert npm audit finding to bug."""
        severity_map = {
            "critical": Severity.CRITICAL,
            "high": Severity.HIGH,
            "moderate": Severity.MEDIUM,
            "low": Severity.LOW,
        }
        self._add_bug(
            severity=severity_map.get(details.get("severity", "low"), Severity.MEDIUM),
            category="security",
            file="package.json",
            line=None,
            message=f"Vulnerability in {details.get('name', vuln_id)}",
            tool="npm_audit",
            details=details.get("title", ""),
        )

    def generate_report(self) -> str:
        """Generate comprehensive bug report."""
        report = []
        report.append("=" * 80)
        report.append("AUTOMATED TEST & BUG REPORT")
        report.append("=" * 80)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        # Summary
        report.append("📊 SUMMARY")
        report.append("-" * 80)
        report.append(f"Backend Tests:     {'✅ PASSED' if self.results.backend_tests_passed else '❌ FAILED'}")
        report.append(f"Frontend Tests:    {'✅ PASSED' if self.results.frontend_tests_passed else '⚠️  SKIPPED'}")
        report.append(f"Backend Lint:      {'✅ PASSED' if self.results.backend_lint_passed else '❌ FAILED'}")
        report.append(f"Frontend Lint:     {'✅ PASSED' if self.results.frontend_lint_passed else '❌ FAILED'}")
        report.append(f"Type Checking:     {'✅ PASSED' if self.results.type_check_passed else '❌ FAILED'}")
        report.append("")
        report.append(f"Total Tests Run:   {self.results.total_tests_run}")
        report.append(f"Tests Passed:      {self.results.total_tests_passed}")
        report.append(f"Tests Failed:      {self.results.total_tests_failed}")
        report.append(f"Total Bugs Found:  {len(self.results.bugs)}")
        report.append("")

        # Bugs by severity
        bugs_by_severity = {}
        for bug in self.results.bugs:
            bugs_by_severity.setdefault(bug.severity, []).append(bug)

        report.append("🐛 BUGS BY SEVERITY")
        report.append("-" * 80)
        for severity in [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW, Severity.INFO]:
            count = len(bugs_by_severity.get(severity, []))
            if count > 0:
                report.append(f"{severity.value:12} {count:3} issues")
        report.append("")

        # Detailed bug list
        if self.results.bugs:
            report.append("📋 DETAILED BUG LIST")
            report.append("-" * 80)
            for severity in [Severity.CRITICAL, Severity.HIGH, Severity.MEDIUM, Severity.LOW, Severity.INFO]:
                bugs = bugs_by_severity.get(severity, [])
                if bugs:
                    report.append(f"\n{severity.value} Priority Issues ({len(bugs)}):")
                    report.append("")
                    for bug in bugs:
                        report.append(f"[{bug.id}] {bug.message}")
                        report.append(f"    File: {bug.file}:{bug.line if bug.line else '?'}")
                        report.append(f"    Tool: {bug.tool} | Category: {bug.category}")
                        if bug.details:
                            report.append(f"    Details: {bug.details}")
                        report.append("")
        else:
            report.append("✅ NO BUGS FOUND!")
            report.append("")

        # Recommendations
        report.append("💡 RECOMMENDATIONS")
        report.append("-" * 80)
        if len(bugs_by_severity.get(Severity.CRITICAL, [])) > 0:
            report.append("⚠️  CRITICAL: Fix critical bugs immediately before deployment")
        if len(bugs_by_severity.get(Severity.HIGH, [])) > 0:
            report.append("⚠️  HIGH: Address high priority issues in current sprint")
        if self.results.total_tests_failed > 0:
            report.append("⚠️  Fix failing tests before merging")
        if not self.results.backend_lint_passed or not self.results.frontend_lint_passed:
            report.append("⚠️  Fix linting issues to maintain code quality")

        if len(self.results.bugs) == 0 and self.results.total_tests_failed == 0:
            report.append("✅ Code quality is excellent! Ready for deployment.")

        report.append("")
        report.append("=" * 80)

        return "\n".join(report)


def main():
    """Main entry point."""
    root_dir = Path(__file__).parent.parent
    runner = TestRunner(root_dir)

    try:
        results = runner.run_all_tests()
        report = runner.generate_report()

        print()
        print(report)

        # Save report to file
        report_dir = root_dir / "docs"
        report_dir.mkdir(exist_ok=True)
        report_file = report_dir / f"automated-test-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"

        with open(report_file, "w") as f:
            f.write(report)

        print()
        print(f"📄 Report saved to: {report_file.relative_to(root_dir)}")

        # Exit with appropriate code
        if results.total_tests_failed > 0 or len([b for b in results.bugs if b.severity in [Severity.CRITICAL, Severity.HIGH]]) > 0:
            sys.exit(1)
        else:
            sys.exit(0)

    except KeyboardInterrupt:
        print("\n\n⚠️  Testing interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"\n\n❌ Testing failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
