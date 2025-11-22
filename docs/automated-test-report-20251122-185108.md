================================================================================
AUTOMATED TEST & BUG REPORT
================================================================================
Generated: 2025-11-22 18:51:08

📊 SUMMARY
--------------------------------------------------------------------------------
Backend Tests:     ❌ FAILED
Frontend Tests:    ⚠️  SKIPPED
Backend Lint:      ❌ FAILED
Frontend Lint:     ❌ FAILED
Type Checking:     ❌ FAILED

Total Tests Run:   0
Tests Passed:      0
Tests Failed:      0
Total Bugs Found:  27

🐛 BUGS BY SEVERITY
--------------------------------------------------------------------------------
LOW           17 issues
INFO          10 issues

📋 DETAILED BUG LIST
--------------------------------------------------------------------------------

LOW Priority Issues (17):

[AUTO-001] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:145
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-002] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:148
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-003] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:185
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-004] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:212
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-005] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:246
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-006] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:284
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-007] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:287
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-008] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:323
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-009] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:326
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-010] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:356
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-011] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:359
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-012] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:397
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-013] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:90
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-014] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:138
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-015] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:168
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-016] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:209
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-017] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:241
    Tool: ruff | Category: lint
    Details: Code: B904


INFO Priority Issues (10):

[AUTO-018] TODO comment found
    File: backend/src/api/applications.py:121
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-019] TODO comment found
    File: backend/src/api/applications.py:168
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-020] TODO comment found
    File: backend/src/api/applications.py:200
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-021] TODO comment found
    File: backend/src/api/applications.py:228
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-022] TODO comment found
    File: backend/src/api/applications.py:264
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-023] TODO comment found
    File: backend/src/api/applications.py:305
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-024] TODO comment found
    File: backend/src/api/applications.py:343
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-025] TODO comment found
    File: backend/src/api/applications.py:375
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-026] TODO comment found
    File: frontend/src/api/client.ts:24
    Tool: grep | Category: code_quality
    Details: // TODO: Add authentication token when auth is implemented

[AUTO-027] TODO comment found
    File: frontend/src/api/client.ts:54
    Tool: grep | Category: code_quality
    Details: // TODO: Redirect to login when auth is implemented

💡 RECOMMENDATIONS
--------------------------------------------------------------------------------
⚠️  Fix linting issues to maintain code quality

================================================================================