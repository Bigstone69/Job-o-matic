================================================================================
AUTOMATED TEST & BUG REPORT
================================================================================
Generated: 2025-11-22 17:50:01

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
Total Bugs Found:  1011

🐛 BUGS BY SEVERITY
--------------------------------------------------------------------------------
HIGH          12 issues
MEDIUM       740 issues
LOW          249 issues
INFO          10 issues

📋 DETAILED BUG LIST
--------------------------------------------------------------------------------

HIGH Priority Issues (12):

[AUTO-022] `sqlalchemy.func` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:9
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-023] `sqlalchemy.and_` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:9
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-025] `src.models.database.Company` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:15
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-026] `src.api.schemas.job_schemas.JobListFilters` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:24
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-041] `typing.Any` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:8
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-069] `pydantic.HttpUrl` imported but unused
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:7
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-098] `src.models.session.init_db` imported but unused
    File: /home/user/Job-o-matic/backend/src/main.py:14
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-143] `sqlalchemy.pool.NullPool` imported but unused
    File: /home/user/Job-o-matic/backend/src/models/session.py:9
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-180] `sqlalchemy.and_` imported but unused
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:11
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-181] `sqlalchemy.or_` imported but unused
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:11
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-182] `src.models.database.Company` imported but unused
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:18
    Tool: ruff | Category: lint
    Details: Code: F401

[AUTO-218] `collections.defaultdict` imported but unused
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:14
    Tool: ruff | Category: lint
    Details: Code: F401


MEDIUM Priority Issues (740):

[AUTO-204] Avoid equality comparisons to `True`; use `Application.is_active:` for truth checks
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:546
    Tool: ruff | Category: lint
    Details: Code: E712

[AUTO-206] Avoid equality comparisons to `True`; use `Application.is_active:` for truth checks
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:573
    Tool: ruff | Category: lint
    Details: Code: E712

[AUTO-264] Class cannot subclass "DeclarativeBase" (has type "Any")  [misc]
    File: src/models/database.py:16
    Tool: mypy | Category: type_error

[AUTO-265] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:32
    Tool: mypy | Category: type_error

[AUTO-266] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:63
    Tool: mypy | Category: type_error

[AUTO-267] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:77
    Tool: mypy | Category: type_error

[AUTO-268] Missing type parameters for generic type "dict"  [type-arg]
    File: src/api/schemas/job_schemas.py:104
    Tool: mypy | Category: type_error

[AUTO-269] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:112
    Tool: mypy | Category: type_error

[AUTO-270] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:135
    Tool: mypy | Category: type_error

[AUTO-271] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:166
    Tool: mypy | Category: type_error

[AUTO-272] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:32
    Tool: mypy | Category: type_error

[AUTO-273] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:63
    Tool: mypy | Category: type_error

[AUTO-274] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:83
    Tool: mypy | Category: type_error

[AUTO-275] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:103
    Tool: mypy | Category: type_error

[AUTO-276] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:116
    Tool: mypy | Category: type_error

[AUTO-277] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:146
    Tool: mypy | Category: type_error

[AUTO-278] "type[ApplicationStatus]" has no attribute "DRAFT"  [attr-defined]
    File: src/services/application_service.py:29
    Tool: mypy | Category: type_error

[AUTO-279] "type[ApplicationStatus]" has no attribute "SUBMITTED"  [attr-defined]
    File: src/services/application_service.py:30
    Tool: mypy | Category: type_error

[AUTO-280] "type[ApplicationStatus]" has no attribute "SUBMITTED"  [attr-defined]
    File: src/services/application_service.py:33
    Tool: mypy | Category: type_error

[AUTO-281] "type[ApplicationStatus]" has no attribute "TECHNICAL"  [attr-defined]
    File: src/services/application_service.py:44
    Tool: mypy | Category: type_error

[AUTO-282] "type[ApplicationStatus]" has no attribute "TECHNICAL"  [attr-defined]
    File: src/services/application_service.py:49
    Tool: mypy | Category: type_error

[AUTO-283] Function is missing a return type annotation  [no-untyped-def]
    File: src/services/application_service.py:72
    Tool: mypy | Category: type_error

[AUTO-284] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/application_service.py:76
    Tool: mypy | Category: type_error

[AUTO-285] "type[ApplicationStatus]" has no attribute "DRAFT"  [attr-defined]
    File: src/services/application_service.py:81
    Tool: mypy | Category: type_error

[AUTO-286] "type[ApplicationStatus]" has no attribute "SUBMITTED"  [attr-defined]
    File: src/services/application_service.py:118
    Tool: mypy | Category: type_error

[AUTO-287] Returning Any from function declared to return "Application | None"  [no-any-return]
    File: src/services/application_service.py:212
    Tool: mypy | Category: type_error

[AUTO-288] Returning Any from function declared to return "list[Application]"  [no-any-return]
    File: src/services/application_service.py:270
    Tool: mypy | Category: type_error

[AUTO-289] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/application_service.py:276
    Tool: mypy | Category: type_error

[AUTO-290] "type[ApplicationStatus]" has no attribute "SUBMITTED"  [attr-defined]
    File: src/services/application_service.py:397
    Tool: mypy | Category: type_error

[AUTO-291] Returning Any from function declared to return "list[ApplicationStatusHistory]"  [no-any-return]
    File: src/services/application_service.py:520
    Tool: mypy | Category: type_error

[AUTO-292] Class cannot subclass "BaseSettings" (has type "Any")  [misc]
    File: src/models/session.py:16
    Tool: mypy | Category: type_error

[AUTO-293] Function is missing a return type annotation  [no-untyped-def]
    File: src/models/session.py:34
    Tool: mypy | Category: type_error

[AUTO-294] Function is missing a return type annotation  [no-untyped-def]
    File: src/models/session.py:50
    Tool: mypy | Category: type_error

[AUTO-295] Call to untyped function "get_engine" in typed context  [no-untyped-call]
    File: src/models/session.py:54
    Tool: mypy | Category: type_error

[AUTO-296] Call to untyped function "get_session_maker" in typed context  [no-untyped-call]
    File: src/models/session.py:81
    Tool: mypy | Category: type_error

[AUTO-297] Call to untyped function "get_engine" in typed context  [no-untyped-call]
    File: src/models/session.py:102
    Tool: mypy | Category: type_error

[AUTO-298] Call to untyped function "ApplicationService" in typed context  [no-untyped-call]
    File: src/api/applications.py:33
    Tool: mypy | Category: type_error

[AUTO-299] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/api/applications.py:37
    Tool: mypy | Category: type_error

[AUTO-300] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/api/applications.py:79
    Tool: mypy | Category: type_error

[AUTO-301] Untyped decorator makes function "create_application" untyped  [misc]
    File: src/api/applications.py:107
    Tool: mypy | Category: type_error

[AUTO-302] Argument "status" to "create_application" of "ApplicationService" has incompatible type "ApplicationStatusEnum"; expected "ApplicationStatus"  [arg-type]
    File: src/api/applications.py:128
    Tool: mypy | Category: type_error

[AUTO-303] Untyped decorator makes function "list_applications" untyped  [misc]
    File: src/api/applications.py:151
    Tool: mypy | Category: type_error

[AUTO-304] Argument "status" to "get_applications" of "ApplicationService" has incompatible type "ApplicationStatusEnum | None"; expected "ApplicationStatus | None"  [arg-type]
    File: src/api/applications.py:174
    Tool: mypy | Category: type_error

[AUTO-305] Untyped decorator makes function "get_application_stats" untyped  [misc]
    File: src/api/applications.py:188
    Tool: mypy | Category: type_error

[AUTO-306] Untyped decorator makes function "get_application" untyped  [misc]
    File: src/api/applications.py:215
    Tool: mypy | Category: type_error

[AUTO-307] Untyped decorator makes function "update_application" untyped  [misc]
    File: src/api/applications.py:252
    Tool: mypy | Category: type_error

[AUTO-308] Untyped decorator makes function "update_application_status" untyped  [misc]
    File: src/api/applications.py:293
    Tool: mypy | Category: type_error

[AUTO-309] Argument "new_status" to "update_status" of "ApplicationService" has incompatible type "ApplicationStatusEnum"; expected "ApplicationStatus"  [arg-type]
    File: src/api/applications.py:315
    Tool: mypy | Category: type_error

[AUTO-310] Untyped decorator makes function "delete_application" untyped  [misc]
    File: src/api/applications.py:332
    Tool: mypy | Category: type_error

[AUTO-311] Untyped decorator makes function "get_application_history" untyped  [misc]
    File: src/api/applications.py:365
    Tool: mypy | Category: type_error

[AUTO-312] Function is missing a return type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:17
    Tool: mypy | Category: type_error

[AUTO-313] Function is missing a type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:20
    Tool: mypy | Category: type_error

[AUTO-314] Function is missing a type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:22
    Tool: mypy | Category: type_error

[AUTO-315] Untyped decorator makes function "search" untyped  [misc]
    File: src/scrapers/jobspy_client.py:67
    Tool: mypy | Category: type_error

[AUTO-316] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:68
    Tool: mypy | Category: type_error

[AUTO-317] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:126
    Tool: mypy | Category: type_error

[AUTO-318] Missing type parameters for generic type "Dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:236
    Tool: mypy | Category: type_error

[AUTO-319] Missing type parameters for generic type "Dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:244
    Tool: mypy | Category: type_error

[AUTO-320] Returning Any from function declared to return "list[str] | None"  [no-any-return]
    File: src/scrapers/jobspy_client.py:248
    Tool: mypy | Category: type_error

[AUTO-321] Missing type parameters for generic type "Dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:264
    Tool: mypy | Category: type_error

[AUTO-322] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/job_search_service.py:82
    Tool: mypy | Category: type_error

[AUTO-323] Returning Any from function declared to return "Company"  [no-any-return]
    File: src/services/job_search_service.py:267
    Tool: mypy | Category: type_error

[AUTO-324] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/job_search_service.py:426
    Tool: mypy | Category: type_error

[AUTO-325] Untyped decorator makes function "search_jobs" untyped  [misc]
    File: src/api/jobs.py:38
    Tool: mypy | Category: type_error

[AUTO-326] Argument "employment_type" to "search_jobs" of "JobSearchService" has incompatible type "list[EmploymentTypeEnum] | None"; expected "list[str] | None"  [arg-type]
    File: src/api/jobs.py:69
    Tool: mypy | Category: type_error

[AUTO-327] Untyped decorator makes function "list_jobs" untyped  [misc]
    File: src/api/jobs.py:94
    Tool: mypy | Category: type_error

[AUTO-328] Untyped decorator makes function "get_job" untyped  [misc]
    File: src/api/jobs.py:144
    Tool: mypy | Category: type_error

[AUTO-329] Untyped decorator makes function "create_manual_job" untyped  [misc]
    File: src/api/jobs.py:174
    Tool: mypy | Category: type_error

[AUTO-330] Untyped decorator makes function "delete_job" untyped  [misc]
    File: src/api/jobs.py:215
    Tool: mypy | Category: type_error

[AUTO-331] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:27
    Tool: mypy | Category: type_error

[AUTO-332] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:79
    Tool: mypy | Category: type_error

[AUTO-333] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:91
    Tool: mypy | Category: type_error

[AUTO-334] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:98
    Tool: mypy | Category: type_error

[AUTO-335] Function is missing a type annotation  [no-untyped-def]
    File: src/main.py:114
    Tool: mypy | Category: type_error

[AUTO-336] Function is missing a type annotation  [no-untyped-def]
    File: src/main.py:126
    Tool: mypy | Category: type_error

[AUTO-337] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/App.tsx:1
    Tool: tsc | Category: type_error

[AUTO-338] Cannot find module 'react' or its corresponding type declarations.
    File: src/App.tsx:2
    Tool: tsc | Category: type_error

[AUTO-339] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/App.tsx:3
    Tool: tsc | Category: type_error

[AUTO-340] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/App.tsx:47
    Tool: tsc | Category: type_error

[AUTO-341] Cannot find module 'axios' or its corresponding type declarations.
    File: src/api/client.ts:7
    Tool: tsc | Category: type_error

[AUTO-342] Property 'env' does not exist on type 'ImportMeta'.
    File: src/api/client.ts:10
    Tool: tsc | Category: type_error

[AUTO-343] Parameter 'config' implicitly has an 'any' type.
    File: src/api/client.ts:23
    Tool: tsc | Category: type_error

[AUTO-344] Parameter 'error' implicitly has an 'any' type.
    File: src/api/client.ts:31
    Tool: tsc | Category: type_error

[AUTO-345] Cannot find namespace 'React'.
    File: src/components/ApplicationCard.tsx:42
    Tool: tsc | Category: type_error

[AUTO-346] Cannot find namespace 'React'.
    File: src/components/ApplicationCard.tsx:49
    Tool: tsc | Category: type_error

[AUTO-347] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:57
    Tool: tsc | Category: type_error

[AUTO-348] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationCard.tsx:57
    Tool: tsc | Category: type_error

[AUTO-349] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:64
    Tool: tsc | Category: type_error

[AUTO-350] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:65
    Tool: tsc | Category: type_error

[AUTO-351] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:66
    Tool: tsc | Category: type_error

[AUTO-352] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:68
    Tool: tsc | Category: type_error

[AUTO-353] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:69
    Tool: tsc | Category: type_error

[AUTO-354] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:71
    Tool: tsc | Category: type_error

[AUTO-355] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:72
    Tool: tsc | Category: type_error

[AUTO-356] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:74
    Tool: tsc | Category: type_error

[AUTO-357] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:75
    Tool: tsc | Category: type_error

[AUTO-358] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:78
    Tool: tsc | Category: type_error

[AUTO-359] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:80
    Tool: tsc | Category: type_error

[AUTO-360] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:85
    Tool: tsc | Category: type_error

[AUTO-361] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:86
    Tool: tsc | Category: type_error

[AUTO-362] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:91
    Tool: tsc | Category: type_error

[AUTO-363] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:92
    Tool: tsc | Category: type_error

[AUTO-364] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:94
    Tool: tsc | Category: type_error

[AUTO-365] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:95
    Tool: tsc | Category: type_error

[AUTO-366] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:98
    Tool: tsc | Category: type_error

[AUTO-367] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:99
    Tool: tsc | Category: type_error

[AUTO-368] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:104
    Tool: tsc | Category: type_error

[AUTO-369] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:105
    Tool: tsc | Category: type_error

[AUTO-370] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:108
    Tool: tsc | Category: type_error

[AUTO-371] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:110
    Tool: tsc | Category: type_error

[AUTO-372] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:111
    Tool: tsc | Category: type_error

[AUTO-373] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:117
    Tool: tsc | Category: type_error

[AUTO-374] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:123
    Tool: tsc | Category: type_error

[AUTO-375] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:124
    Tool: tsc | Category: type_error

[AUTO-376] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:126
    Tool: tsc | Category: type_error

[AUTO-377] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:127
    Tool: tsc | Category: type_error

[AUTO-378] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:131
    Tool: tsc | Category: type_error

[AUTO-379] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:132
    Tool: tsc | Category: type_error

[AUTO-380] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:138
    Tool: tsc | Category: type_error

[AUTO-381] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:144
    Tool: tsc | Category: type_error

[AUTO-382] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:145
    Tool: tsc | Category: type_error

[AUTO-383] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:147
    Tool: tsc | Category: type_error

[AUTO-384] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:148
    Tool: tsc | Category: type_error

[AUTO-385] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-386] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:153
    Tool: tsc | Category: type_error

[AUTO-387] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:159
    Tool: tsc | Category: type_error

[AUTO-388] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:165
    Tool: tsc | Category: type_error

[AUTO-389] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:166
    Tool: tsc | Category: type_error

[AUTO-390] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:168
    Tool: tsc | Category: type_error

[AUTO-391] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:169
    Tool: tsc | Category: type_error

[AUTO-392] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:171
    Tool: tsc | Category: type_error

[AUTO-393] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:174
    Tool: tsc | Category: type_error

[AUTO-394] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:175
    Tool: tsc | Category: type_error

[AUTO-395] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:177
    Tool: tsc | Category: type_error

[AUTO-396] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:178
    Tool: tsc | Category: type_error

[AUTO-397] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:179
    Tool: tsc | Category: type_error

[AUTO-398] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:30
    Tool: tsc | Category: type_error

[AUTO-399] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationList.tsx:30
    Tool: tsc | Category: type_error

[AUTO-400] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:32
    Tool: tsc | Category: type_error

[AUTO-401] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:36
    Tool: tsc | Category: type_error

[AUTO-402] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:37
    Tool: tsc | Category: type_error

[AUTO-403] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:38
    Tool: tsc | Category: type_error

[AUTO-404] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:39
    Tool: tsc | Category: type_error

[AUTO-405] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:40
    Tool: tsc | Category: type_error

[AUTO-406] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:41
    Tool: tsc | Category: type_error

[AUTO-407] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:42
    Tool: tsc | Category: type_error

[AUTO-408] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:43
    Tool: tsc | Category: type_error

[AUTO-409] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:44
    Tool: tsc | Category: type_error

[AUTO-410] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:45
    Tool: tsc | Category: type_error

[AUTO-411] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:46
    Tool: tsc | Category: type_error

[AUTO-412] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:47
    Tool: tsc | Category: type_error

[AUTO-413] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:48
    Tool: tsc | Category: type_error

[AUTO-414] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:49
    Tool: tsc | Category: type_error

[AUTO-415] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:50
    Tool: tsc | Category: type_error

[AUTO-416] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:52
    Tool: tsc | Category: type_error

[AUTO-417] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:59
    Tool: tsc | Category: type_error

[AUTO-418] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:60
    Tool: tsc | Category: type_error

[AUTO-419] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:66
    Tool: tsc | Category: type_error

[AUTO-420] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:72
    Tool: tsc | Category: type_error

[AUTO-421] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:73
    Tool: tsc | Category: type_error

[AUTO-422] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:75
    Tool: tsc | Category: type_error

[AUTO-423] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:76
    Tool: tsc | Category: type_error

[AUTO-424] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:78
    Tool: tsc | Category: type_error

[AUTO-425] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:79
    Tool: tsc | Category: type_error

[AUTO-426] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:86
    Tool: tsc | Category: type_error

[AUTO-427] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:87
    Tool: tsc | Category: type_error

[AUTO-428] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:93
    Tool: tsc | Category: type_error

[AUTO-429] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:99
    Tool: tsc | Category: type_error

[AUTO-430] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:100
    Tool: tsc | Category: type_error

[AUTO-431] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:102
    Tool: tsc | Category: type_error

[AUTO-432] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:103
    Tool: tsc | Category: type_error

[AUTO-433] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:105
    Tool: tsc | Category: type_error

[AUTO-434] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:106
    Tool: tsc | Category: type_error

[AUTO-435] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:112
    Tool: tsc | Category: type_error

[AUTO-436] Type '{ key: number; application: Application; onClick: ((application: Application) => void) | undefined; onStatusClick: ((application: Application) => void) | undefined; onDelete: ((application: Application) => void) | undefined; }' is not assignable to type 'ApplicationCardProps'.
    File: src/components/ApplicationList.tsx:115
    Tool: tsc | Category: type_error

[AUTO-437] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:122
    Tool: tsc | Category: type_error

[AUTO-438] Cannot find namespace 'JSX'.
    File: src/components/ApplicationStatusBadge.tsx:49
    Tool: tsc | Category: type_error

[AUTO-439] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:55
    Tool: tsc | Category: type_error

[AUTO-440] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:56
    Tool: tsc | Category: type_error

[AUTO-441] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:57
    Tool: tsc | Category: type_error

[AUTO-442] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:61
    Tool: tsc | Category: type_error

[AUTO-443] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:62
    Tool: tsc | Category: type_error

[AUTO-444] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:63
    Tool: tsc | Category: type_error

[AUTO-445] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:64
    Tool: tsc | Category: type_error

[AUTO-446] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:70
    Tool: tsc | Category: type_error

[AUTO-447] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:71
    Tool: tsc | Category: type_error

[AUTO-448] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:76
    Tool: tsc | Category: type_error

[AUTO-449] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:80
    Tool: tsc | Category: type_error

[AUTO-450] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:81
    Tool: tsc | Category: type_error

[AUTO-451] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:82
    Tool: tsc | Category: type_error

[AUTO-452] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:87
    Tool: tsc | Category: type_error

[AUTO-453] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:91
    Tool: tsc | Category: type_error

[AUTO-454] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:92
    Tool: tsc | Category: type_error

[AUTO-455] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:97
    Tool: tsc | Category: type_error

[AUTO-456] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:101
    Tool: tsc | Category: type_error

[AUTO-457] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:102
    Tool: tsc | Category: type_error

[AUTO-458] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:107
    Tool: tsc | Category: type_error

[AUTO-459] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:111
    Tool: tsc | Category: type_error

[AUTO-460] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:112
    Tool: tsc | Category: type_error

[AUTO-461] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:117
    Tool: tsc | Category: type_error

[AUTO-462] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:132
    Tool: tsc | Category: type_error

[AUTO-463] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationStatusBadge.tsx:132
    Tool: tsc | Category: type_error

[AUTO-464] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:139
    Tool: tsc | Category: type_error

[AUTO-465] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:26
    Tool: tsc | Category: type_error

[AUTO-466] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationTimeline.tsx:26
    Tool: tsc | Category: type_error

[AUTO-467] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:28
    Tool: tsc | Category: type_error

[AUTO-468] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:33
    Tool: tsc | Category: type_error

[AUTO-469] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:34
    Tool: tsc | Category: type_error

[AUTO-470] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:36
    Tool: tsc | Category: type_error

[AUTO-471] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:37
    Tool: tsc | Category: type_error

[AUTO-472] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:40
    Tool: tsc | Category: type_error

[AUTO-473] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:46
    Tool: tsc | Category: type_error

[AUTO-474] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:48
    Tool: tsc | Category: type_error

[AUTO-475] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:49
    Tool: tsc | Category: type_error

[AUTO-476] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:50
    Tool: tsc | Category: type_error

[AUTO-477] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:55
    Tool: tsc | Category: type_error

[AUTO-478] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:60
    Tool: tsc | Category: type_error

[AUTO-479] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:61
    Tool: tsc | Category: type_error

[AUTO-480] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:62
    Tool: tsc | Category: type_error

[AUTO-481] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:65
    Tool: tsc | Category: type_error

[AUTO-482] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:66
    Tool: tsc | Category: type_error

[AUTO-483] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:70
    Tool: tsc | Category: type_error

[AUTO-484] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:76
    Tool: tsc | Category: type_error

[AUTO-485] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:82
    Tool: tsc | Category: type_error

[AUTO-486] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:86
    Tool: tsc | Category: type_error

[AUTO-487] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:88
    Tool: tsc | Category: type_error

[AUTO-488] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:90
    Tool: tsc | Category: type_error

[AUTO-489] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:93
    Tool: tsc | Category: type_error

[AUTO-490] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:95
    Tool: tsc | Category: type_error

[AUTO-491] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:97
    Tool: tsc | Category: type_error

[AUTO-492] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:98
    Tool: tsc | Category: type_error

[AUTO-493] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:99
    Tool: tsc | Category: type_error

[AUTO-494] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:100
    Tool: tsc | Category: type_error

[AUTO-495] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:102
    Tool: tsc | Category: type_error

[AUTO-496] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:103
    Tool: tsc | Category: type_error

[AUTO-497] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:90
    Tool: tsc | Category: type_error

[AUTO-498] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobCard.tsx:90
    Tool: tsc | Category: type_error

[AUTO-499] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:97
    Tool: tsc | Category: type_error

[AUTO-500] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:99
    Tool: tsc | Category: type_error

[AUTO-501] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:105
    Tool: tsc | Category: type_error

[AUTO-502] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:106
    Tool: tsc | Category: type_error

[AUTO-503] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:108
    Tool: tsc | Category: type_error

[AUTO-504] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:109
    Tool: tsc | Category: type_error

[AUTO-505] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:112
    Tool: tsc | Category: type_error

[AUTO-506] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:113
    Tool: tsc | Category: type_error

[AUTO-507] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:115
    Tool: tsc | Category: type_error

[AUTO-508] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:116
    Tool: tsc | Category: type_error

[AUTO-509] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:118
    Tool: tsc | Category: type_error

[AUTO-510] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:119
    Tool: tsc | Category: type_error

[AUTO-511] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:121
    Tool: tsc | Category: type_error

[AUTO-512] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:122
    Tool: tsc | Category: type_error

[AUTO-513] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:123
    Tool: tsc | Category: type_error

[AUTO-514] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:126
    Tool: tsc | Category: type_error

[AUTO-515] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:128
    Tool: tsc | Category: type_error

[AUTO-516] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:134
    Tool: tsc | Category: type_error

[AUTO-517] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:136
    Tool: tsc | Category: type_error

[AUTO-518] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:138
    Tool: tsc | Category: type_error

[AUTO-519] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:139
    Tool: tsc | Category: type_error

[AUTO-520] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:141
    Tool: tsc | Category: type_error

[AUTO-521] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:142
    Tool: tsc | Category: type_error

[AUTO-522] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:145
    Tool: tsc | Category: type_error

[AUTO-523] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:147
    Tool: tsc | Category: type_error

[AUTO-524] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:149
    Tool: tsc | Category: type_error

[AUTO-525] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-526] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-527] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:154
    Tool: tsc | Category: type_error

[AUTO-528] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:155
    Tool: tsc | Category: type_error

[AUTO-529] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/JobFilters.tsx:5
    Tool: tsc | Category: type_error

[AUTO-530] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:46
    Tool: tsc | Category: type_error

[AUTO-531] Parameter 't' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:47
    Tool: tsc | Category: type_error

[AUTO-532] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:52
    Tool: tsc | Category: type_error

[AUTO-533] Parameter 'p' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:53
    Tool: tsc | Category: type_error

[AUTO-534] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:58
    Tool: tsc | Category: type_error

[AUTO-535] Parameter 's' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:59
    Tool: tsc | Category: type_error

[AUTO-536] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:70
    Tool: tsc | Category: type_error

[AUTO-537] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobFilters.tsx:70
    Tool: tsc | Category: type_error

[AUTO-538] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:72
    Tool: tsc | Category: type_error

[AUTO-539] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:76
    Tool: tsc | Category: type_error

[AUTO-540] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:82
    Tool: tsc | Category: type_error

[AUTO-541] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:88
    Tool: tsc | Category: type_error

[AUTO-542] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:89
    Tool: tsc | Category: type_error

[AUTO-543] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:91
    Tool: tsc | Category: type_error

[AUTO-544] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:93
    Tool: tsc | Category: type_error

[AUTO-545] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:95
    Tool: tsc | Category: type_error

[AUTO-546] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:97
    Tool: tsc | Category: type_error

[AUTO-547] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:101
    Tool: tsc | Category: type_error

[AUTO-548] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:102
    Tool: tsc | Category: type_error

[AUTO-549] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:103
    Tool: tsc | Category: type_error

[AUTO-550] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:105
    Tool: tsc | Category: type_error

[AUTO-551] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:106
    Tool: tsc | Category: type_error

[AUTO-552] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:108
    Tool: tsc | Category: type_error

[AUTO-553] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:110
    Tool: tsc | Category: type_error

[AUTO-554] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:111
    Tool: tsc | Category: type_error

[AUTO-555] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:113
    Tool: tsc | Category: type_error

[AUTO-556] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:114
    Tool: tsc | Category: type_error

[AUTO-557] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:116
    Tool: tsc | Category: type_error

[AUTO-558] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:117
    Tool: tsc | Category: type_error

[AUTO-559] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:123
    Tool: tsc | Category: type_error

[AUTO-560] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:125
    Tool: tsc | Category: type_error

[AUTO-561] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:126
    Tool: tsc | Category: type_error

[AUTO-562] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:128
    Tool: tsc | Category: type_error

[AUTO-563] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:129
    Tool: tsc | Category: type_error

[AUTO-564] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:132
    Tool: tsc | Category: type_error

[AUTO-565] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:133
    Tool: tsc | Category: type_error

[AUTO-566] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:135
    Tool: tsc | Category: type_error

[AUTO-567] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:136
    Tool: tsc | Category: type_error

[AUTO-568] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:139
    Tool: tsc | Category: type_error

[AUTO-569] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:140
    Tool: tsc | Category: type_error

[AUTO-570] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:146
    Tool: tsc | Category: type_error

[AUTO-571] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:148
    Tool: tsc | Category: type_error

[AUTO-572] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:149
    Tool: tsc | Category: type_error

[AUTO-573] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:152
    Tool: tsc | Category: type_error

[AUTO-574] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:153
    Tool: tsc | Category: type_error

[AUTO-575] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:156
    Tool: tsc | Category: type_error

[AUTO-576] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:157
    Tool: tsc | Category: type_error

[AUTO-577] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:162
    Tool: tsc | Category: type_error

[AUTO-578] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:163
    Tool: tsc | Category: type_error

[AUTO-579] Parameter 'e' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:167
    Tool: tsc | Category: type_error

[AUTO-580] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:171
    Tool: tsc | Category: type_error

[AUTO-581] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:174
    Tool: tsc | Category: type_error

[AUTO-582] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:175
    Tool: tsc | Category: type_error

[AUTO-583] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:177
    Tool: tsc | Category: type_error

[AUTO-584] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:178
    Tool: tsc | Category: type_error

[AUTO-585] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:181
    Tool: tsc | Category: type_error

[AUTO-586] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:182
    Tool: tsc | Category: type_error

[AUTO-587] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:188
    Tool: tsc | Category: type_error

[AUTO-588] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:190
    Tool: tsc | Category: type_error

[AUTO-589] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:191
    Tool: tsc | Category: type_error

[AUTO-590] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:194
    Tool: tsc | Category: type_error

[AUTO-591] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:195
    Tool: tsc | Category: type_error

[AUTO-592] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:196
    Tool: tsc | Category: type_error

[AUTO-593] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:199
    Tool: tsc | Category: type_error

[AUTO-594] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:200
    Tool: tsc | Category: type_error

[AUTO-595] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:205
    Tool: tsc | Category: type_error

[AUTO-596] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:206
    Tool: tsc | Category: type_error

[AUTO-597] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:211
    Tool: tsc | Category: type_error

[AUTO-598] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:212
    Tool: tsc | Category: type_error

[AUTO-599] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:213
    Tool: tsc | Category: type_error

[AUTO-600] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:215
    Tool: tsc | Category: type_error

[AUTO-601] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:26
    Tool: tsc | Category: type_error

[AUTO-602] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobList.tsx:26
    Tool: tsc | Category: type_error

[AUTO-603] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:28
    Tool: tsc | Category: type_error

[AUTO-604] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:32
    Tool: tsc | Category: type_error

[AUTO-605] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:33
    Tool: tsc | Category: type_error

[AUTO-606] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:34
    Tool: tsc | Category: type_error

[AUTO-607] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:35
    Tool: tsc | Category: type_error

[AUTO-608] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:36
    Tool: tsc | Category: type_error

[AUTO-609] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:37
    Tool: tsc | Category: type_error

[AUTO-610] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:38
    Tool: tsc | Category: type_error

[AUTO-611] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:39
    Tool: tsc | Category: type_error

[AUTO-612] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:40
    Tool: tsc | Category: type_error

[AUTO-613] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:41
    Tool: tsc | Category: type_error

[AUTO-614] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:42
    Tool: tsc | Category: type_error

[AUTO-615] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:43
    Tool: tsc | Category: type_error

[AUTO-616] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:44
    Tool: tsc | Category: type_error

[AUTO-617] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:45
    Tool: tsc | Category: type_error

[AUTO-618] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:47
    Tool: tsc | Category: type_error

[AUTO-619] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:54
    Tool: tsc | Category: type_error

[AUTO-620] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:55
    Tool: tsc | Category: type_error

[AUTO-621] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:61
    Tool: tsc | Category: type_error

[AUTO-622] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:67
    Tool: tsc | Category: type_error

[AUTO-623] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:68
    Tool: tsc | Category: type_error

[AUTO-624] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:70
    Tool: tsc | Category: type_error

[AUTO-625] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:71
    Tool: tsc | Category: type_error

[AUTO-626] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:73
    Tool: tsc | Category: type_error

[AUTO-627] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:74
    Tool: tsc | Category: type_error

[AUTO-628] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:81
    Tool: tsc | Category: type_error

[AUTO-629] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:82
    Tool: tsc | Category: type_error

[AUTO-630] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:88
    Tool: tsc | Category: type_error

[AUTO-631] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:94
    Tool: tsc | Category: type_error

[AUTO-632] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:95
    Tool: tsc | Category: type_error

[AUTO-633] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:97
    Tool: tsc | Category: type_error

[AUTO-634] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:98
    Tool: tsc | Category: type_error

[AUTO-635] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:100
    Tool: tsc | Category: type_error

[AUTO-636] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:101
    Tool: tsc | Category: type_error

[AUTO-637] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:107
    Tool: tsc | Category: type_error

[AUTO-638] Type '{ key: number; job: Job; onClick: ((job: Job) => void) | undefined; }' is not assignable to type 'JobCardProps'.
    File: src/components/JobList.tsx:109
    Tool: tsc | Category: type_error

[AUTO-639] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:111
    Tool: tsc | Category: type_error

[AUTO-640] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/Layout.tsx:1
    Tool: tsc | Category: type_error

[AUTO-641] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/components/Layout.tsx:2
    Tool: tsc | Category: type_error

[AUTO-642] Cannot find module 'lucide-react' or its corresponding type declarations.
    File: src/components/Layout.tsx:3
    Tool: tsc | Category: type_error

[AUTO-643] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:26
    Tool: tsc | Category: type_error

[AUTO-644] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/Layout.tsx:26
    Tool: tsc | Category: type_error

[AUTO-645] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:28
    Tool: tsc | Category: type_error

[AUTO-646] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:29
    Tool: tsc | Category: type_error

[AUTO-647] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:30
    Tool: tsc | Category: type_error

[AUTO-648] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:32
    Tool: tsc | Category: type_error

[AUTO-649] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:34
    Tool: tsc | Category: type_error

[AUTO-650] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:36
    Tool: tsc | Category: type_error

[AUTO-651] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:37
    Tool: tsc | Category: type_error

[AUTO-652] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:40
    Tool: tsc | Category: type_error

[AUTO-653] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:41
    Tool: tsc | Category: type_error

[AUTO-654] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:55
    Tool: tsc | Category: type_error

[AUTO-655] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:56
    Tool: tsc | Category: type_error

[AUTO-656] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:59
    Tool: tsc | Category: type_error

[AUTO-657] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:69
    Tool: tsc | Category: type_error

[AUTO-658] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:70
    Tool: tsc | Category: type_error

[AUTO-659] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:71
    Tool: tsc | Category: type_error

[AUTO-660] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:72
    Tool: tsc | Category: type_error

[AUTO-661] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:75
    Tool: tsc | Category: type_error

[AUTO-662] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:75
    Tool: tsc | Category: type_error

[AUTO-663] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:78
    Tool: tsc | Category: type_error

[AUTO-664] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:79
    Tool: tsc | Category: type_error

[AUTO-665] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:80
    Tool: tsc | Category: type_error

[AUTO-666] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:82
    Tool: tsc | Category: type_error

[AUTO-667] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:83
    Tool: tsc | Category: type_error

[AUTO-668] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:84
    Tool: tsc | Category: type_error

[AUTO-669] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:85
    Tool: tsc | Category: type_error

[AUTO-670] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/SearchBar.tsx:5
    Tool: tsc | Category: type_error

[AUTO-671] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:51
    Tool: tsc | Category: type_error

[AUTO-672] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/SearchBar.tsx:51
    Tool: tsc | Category: type_error

[AUTO-673] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:52
    Tool: tsc | Category: type_error

[AUTO-674] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:53
    Tool: tsc | Category: type_error

[AUTO-675] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:55
    Tool: tsc | Category: type_error

[AUTO-676] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:56
    Tool: tsc | Category: type_error

[AUTO-677] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:61
    Tool: tsc | Category: type_error

[AUTO-678] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:62
    Tool: tsc | Category: type_error

[AUTO-679] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:66
    Tool: tsc | Category: type_error

[AUTO-680] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:71
    Tool: tsc | Category: type_error

[AUTO-681] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:74
    Tool: tsc | Category: type_error

[AUTO-682] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:75
    Tool: tsc | Category: type_error

[AUTO-683] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:80
    Tool: tsc | Category: type_error

[AUTO-684] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:81
    Tool: tsc | Category: type_error

[AUTO-685] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:85
    Tool: tsc | Category: type_error

[AUTO-686] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:90
    Tool: tsc | Category: type_error

[AUTO-687] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:93
    Tool: tsc | Category: type_error

[AUTO-688] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:94
    Tool: tsc | Category: type_error

[AUTO-689] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:100
    Tool: tsc | Category: type_error

[AUTO-690] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:101
    Tool: tsc | Category: type_error

[AUTO-691] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:106
    Tool: tsc | Category: type_error

[AUTO-692] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:114
    Tool: tsc | Category: type_error

[AUTO-693] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:119
    Tool: tsc | Category: type_error

[AUTO-694] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:121
    Tool: tsc | Category: type_error

[AUTO-695] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:123
    Tool: tsc | Category: type_error

[AUTO-696] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:124
    Tool: tsc | Category: type_error

[AUTO-697] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:130
    Tool: tsc | Category: type_error

[AUTO-698] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:136
    Tool: tsc | Category: type_error

[AUTO-699] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:138
    Tool: tsc | Category: type_error

[AUTO-700] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:140
    Tool: tsc | Category: type_error

[AUTO-701] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:141
    Tool: tsc | Category: type_error

[AUTO-702] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:142
    Tool: tsc | Category: type_error

[AUTO-703] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:145
    Tool: tsc | Category: type_error

[AUTO-704] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:146
    Tool: tsc | Category: type_error

[AUTO-705] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:147
    Tool: tsc | Category: type_error

[AUTO-706] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:150
    Tool: tsc | Category: type_error

[AUTO-707] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:153
    Tool: tsc | Category: type_error

[AUTO-708] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:155
    Tool: tsc | Category: type_error

[AUTO-709] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:156
    Tool: tsc | Category: type_error

[AUTO-710] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:157
    Tool: tsc | Category: type_error

[AUTO-711] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:158
    Tool: tsc | Category: type_error

[AUTO-712] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:159
    Tool: tsc | Category: type_error

[AUTO-713] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/StatusUpdateModal.tsx:5
    Tool: tsc | Category: type_error

[AUTO-714] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:83
    Tool: tsc | Category: type_error

[AUTO-715] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/StatusUpdateModal.tsx:83
    Tool: tsc | Category: type_error

[AUTO-716] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:85
    Tool: tsc | Category: type_error

[AUTO-717] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:91
    Tool: tsc | Category: type_error

[AUTO-718] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:92
    Tool: tsc | Category: type_error

[AUTO-719] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:94
    Tool: tsc | Category: type_error

[AUTO-720] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:95
    Tool: tsc | Category: type_error

[AUTO-721] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:97
    Tool: tsc | Category: type_error

[AUTO-722] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:98
    Tool: tsc | Category: type_error

[AUTO-723] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:100
    Tool: tsc | Category: type_error

[AUTO-724] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:101
    Tool: tsc | Category: type_error

[AUTO-725] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:104
    Tool: tsc | Category: type_error

[AUTO-726] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:105
    Tool: tsc | Category: type_error

[AUTO-727] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:107
    Tool: tsc | Category: type_error

[AUTO-728] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:109
    Tool: tsc | Category: type_error

[AUTO-729] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:112
    Tool: tsc | Category: type_error

[AUTO-730] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:114
    Tool: tsc | Category: type_error

[AUTO-731] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:115
    Tool: tsc | Category: type_error

[AUTO-732] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:120
    Tool: tsc | Category: type_error

[AUTO-733] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:121
    Tool: tsc | Category: type_error

[AUTO-734] Parameter 'e' implicitly has an 'any' type.
    File: src/components/StatusUpdateModal.tsx:124
    Tool: tsc | Category: type_error

[AUTO-735] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:129
    Tool: tsc | Category: type_error

[AUTO-736] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:131
    Tool: tsc | Category: type_error

[AUTO-737] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:133
    Tool: tsc | Category: type_error

[AUTO-738] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:134
    Tool: tsc | Category: type_error

[AUTO-739] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:138
    Tool: tsc | Category: type_error

[AUTO-740] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:139
    Tool: tsc | Category: type_error

[AUTO-741] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:141
    Tool: tsc | Category: type_error

[AUTO-742] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:147
    Tool: tsc | Category: type_error

[AUTO-743] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:153
    Tool: tsc | Category: type_error

[AUTO-744] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:155
    Tool: tsc | Category: type_error

[AUTO-745] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:156
    Tool: tsc | Category: type_error

[AUTO-746] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:160
    Tool: tsc | Category: type_error

[AUTO-747] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:161
    Tool: tsc | Category: type_error

[AUTO-748] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:166
    Tool: tsc | Category: type_error

[AUTO-749] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:167
    Tool: tsc | Category: type_error

[AUTO-750] Parameter 'e' implicitly has an 'any' type.
    File: src/components/StatusUpdateModal.tsx:170
    Tool: tsc | Category: type_error

[AUTO-751] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:177
    Tool: tsc | Category: type_error

[AUTO-752] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:179
    Tool: tsc | Category: type_error

[AUTO-753] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:180
    Tool: tsc | Category: type_error

[AUTO-754] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:184
    Tool: tsc | Category: type_error

[AUTO-755] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:185
    Tool: tsc | Category: type_error

[AUTO-756] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:187
    Tool: tsc | Category: type_error

[AUTO-757] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:188
    Tool: tsc | Category: type_error

[AUTO-758] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:192
    Tool: tsc | Category: type_error

[AUTO-759] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:193
    Tool: tsc | Category: type_error

[AUTO-760] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:200
    Tool: tsc | Category: type_error

[AUTO-761] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:201
    Tool: tsc | Category: type_error

[AUTO-762] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:210
    Tool: tsc | Category: type_error

[AUTO-763] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:216
    Tool: tsc | Category: type_error

[AUTO-764] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:224
    Tool: tsc | Category: type_error

[AUTO-765] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:229
    Tool: tsc | Category: type_error

[AUTO-766] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:235
    Tool: tsc | Category: type_error

[AUTO-767] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:236
    Tool: tsc | Category: type_error

[AUTO-768] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:237
    Tool: tsc | Category: type_error

[AUTO-769] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:238
    Tool: tsc | Category: type_error

[AUTO-770] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:239
    Tool: tsc | Category: type_error

[AUTO-771] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:240
    Tool: tsc | Category: type_error

[AUTO-772] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/hooks/useApplications.ts:7
    Tool: tsc | Category: type_error

[AUTO-773] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:129
    Tool: tsc | Category: type_error

[AUTO-774] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:146
    Tool: tsc | Category: type_error

[AUTO-775] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:146
    Tool: tsc | Category: type_error

[AUTO-776] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:147
    Tool: tsc | Category: type_error

[AUTO-777] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:153
    Tool: tsc | Category: type_error

[AUTO-778] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:170
    Tool: tsc | Category: type_error

[AUTO-779] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:170
    Tool: tsc | Category: type_error

[AUTO-780] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:172
    Tool: tsc | Category: type_error

[AUTO-781] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:172
    Tool: tsc | Category: type_error

[AUTO-782] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-783] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-784] Parameter 'context' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-785] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:204
    Tool: tsc | Category: type_error

[AUTO-786] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:226
    Tool: tsc | Category: type_error

[AUTO-787] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/hooks/useJobs.ts:7
    Tool: tsc | Category: type_error

[AUTO-788] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:124
    Tool: tsc | Category: type_error

[AUTO-789] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:142
    Tool: tsc | Category: type_error

[AUTO-790] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:157
    Tool: tsc | Category: type_error

[AUTO-791] Parameter 'request' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:157
    Tool: tsc | Category: type_error

[AUTO-792] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:161
    Tool: tsc | Category: type_error

[AUTO-793] Cannot find module 'react' or its corresponding type declarations.
    File: src/main.tsx:1
    Tool: tsc | Category: type_error

[AUTO-794] Cannot find module 'react-dom/client' or its corresponding type declarations.
    File: src/main.tsx:2
    Tool: tsc | Category: type_error

[AUTO-795] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/main.tsx:3
    Tool: tsc | Category: type_error

[AUTO-796] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/main.tsx:19
    Tool: tsc | Category: type_error

[AUTO-797] Cannot find module 'react' or its corresponding type declarations.
    File: src/pages/ApplicationsPage.tsx:5
    Tool: tsc | Category: type_error

[AUTO-798] Cannot find name 'Application'.
    File: src/pages/ApplicationsPage.tsx:50
    Tool: tsc | Category: type_error

[AUTO-799] Cannot find name 'Application'.
    File: src/pages/ApplicationsPage.tsx:61
    Tool: tsc | Category: type_error

[AUTO-800] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-801] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/ApplicationsPage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-802] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:83
    Tool: tsc | Category: type_error

[AUTO-803] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:85
    Tool: tsc | Category: type_error

[AUTO-804] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:86
    Tool: tsc | Category: type_error

[AUTO-805] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:88
    Tool: tsc | Category: type_error

[AUTO-806] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:89
    Tool: tsc | Category: type_error

[AUTO-807] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:91
    Tool: tsc | Category: type_error

[AUTO-808] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:92
    Tool: tsc | Category: type_error

[AUTO-809] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-810] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:98
    Tool: tsc | Category: type_error

[AUTO-811] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:102
    Tool: tsc | Category: type_error

[AUTO-812] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:103
    Tool: tsc | Category: type_error

[AUTO-813] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:104
    Tool: tsc | Category: type_error

[AUTO-814] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:106
    Tool: tsc | Category: type_error

[AUTO-815] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:108
    Tool: tsc | Category: type_error

[AUTO-816] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:113
    Tool: tsc | Category: type_error

[AUTO-817] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:114
    Tool: tsc | Category: type_error

[AUTO-818] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:120
    Tool: tsc | Category: type_error

[AUTO-819] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:128
    Tool: tsc | Category: type_error

[AUTO-820] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:129
    Tool: tsc | Category: type_error

[AUTO-821] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:135
    Tool: tsc | Category: type_error

[AUTO-822] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:146
    Tool: tsc | Category: type_error

[AUTO-823] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:147
    Tool: tsc | Category: type_error

[AUTO-824] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:153
    Tool: tsc | Category: type_error

[AUTO-825] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:161
    Tool: tsc | Category: type_error

[AUTO-826] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:162
    Tool: tsc | Category: type_error

[AUTO-827] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:168
    Tool: tsc | Category: type_error

[AUTO-828] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:172
    Tool: tsc | Category: type_error

[AUTO-829] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:176
    Tool: tsc | Category: type_error

[AUTO-830] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:177
    Tool: tsc | Category: type_error

[AUTO-831] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:178
    Tool: tsc | Category: type_error

[AUTO-832] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:183
    Tool: tsc | Category: type_error

[AUTO-833] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:184
    Tool: tsc | Category: type_error

[AUTO-834] Parameter 'e' implicitly has an 'any' type.
    File: src/pages/ApplicationsPage.tsx:187
    Tool: tsc | Category: type_error

[AUTO-835] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:193
    Tool: tsc | Category: type_error

[AUTO-836] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:195
    Tool: tsc | Category: type_error

[AUTO-837] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:197
    Tool: tsc | Category: type_error

[AUTO-838] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:198
    Tool: tsc | Category: type_error

[AUTO-839] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:199
    Tool: tsc | Category: type_error

[AUTO-840] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:203
    Tool: tsc | Category: type_error

[AUTO-841] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:204
    Tool: tsc | Category: type_error

[AUTO-842] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:210
    Tool: tsc | Category: type_error

[AUTO-843] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:216
    Tool: tsc | Category: type_error

[AUTO-844] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:217
    Tool: tsc | Category: type_error

[AUTO-845] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:219
    Tool: tsc | Category: type_error

[AUTO-846] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:220
    Tool: tsc | Category: type_error

[AUTO-847] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:222
    Tool: tsc | Category: type_error

[AUTO-848] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:223
    Tool: tsc | Category: type_error

[AUTO-849] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:228
    Tool: tsc | Category: type_error

[AUTO-850] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:229
    Tool: tsc | Category: type_error

[AUTO-851] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:259
    Tool: tsc | Category: type_error

[AUTO-852] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:260
    Tool: tsc | Category: type_error

[AUTO-853] Cannot find namespace 'React'.
    File: src/pages/ApplicationsPage.tsx:268
    Tool: tsc | Category: type_error

[AUTO-854] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:281
    Tool: tsc | Category: type_error

[AUTO-855] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:282
    Tool: tsc | Category: type_error

[AUTO-856] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:283
    Tool: tsc | Category: type_error

[AUTO-857] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:283
    Tool: tsc | Category: type_error

[AUTO-858] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:284
    Tool: tsc | Category: type_error

[AUTO-859] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:285
    Tool: tsc | Category: type_error

[AUTO-860] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:285
    Tool: tsc | Category: type_error

[AUTO-861] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:286
    Tool: tsc | Category: type_error

[AUTO-862] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:286
    Tool: tsc | Category: type_error

[AUTO-863] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:287
    Tool: tsc | Category: type_error

[AUTO-864] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:308
    Tool: tsc | Category: type_error

[AUTO-865] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:310
    Tool: tsc | Category: type_error

[AUTO-866] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:316
    Tool: tsc | Category: type_error

[AUTO-867] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:317
    Tool: tsc | Category: type_error

[AUTO-868] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:319
    Tool: tsc | Category: type_error

[AUTO-869] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:320
    Tool: tsc | Category: type_error

[AUTO-870] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:326
    Tool: tsc | Category: type_error

[AUTO-871] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:332
    Tool: tsc | Category: type_error

[AUTO-872] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:333
    Tool: tsc | Category: type_error

[AUTO-873] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:336
    Tool: tsc | Category: type_error

[AUTO-874] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:338
    Tool: tsc | Category: type_error

[AUTO-875] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:339
    Tool: tsc | Category: type_error

[AUTO-876] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:341
    Tool: tsc | Category: type_error

[AUTO-877] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:344
    Tool: tsc | Category: type_error

[AUTO-878] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:345
    Tool: tsc | Category: type_error

[AUTO-879] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:352
    Tool: tsc | Category: type_error

[AUTO-880] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:353
    Tool: tsc | Category: type_error

[AUTO-881] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:361
    Tool: tsc | Category: type_error

[AUTO-882] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:367
    Tool: tsc | Category: type_error

[AUTO-883] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:375
    Tool: tsc | Category: type_error

[AUTO-884] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:380
    Tool: tsc | Category: type_error

[AUTO-885] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:386
    Tool: tsc | Category: type_error

[AUTO-886] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:387
    Tool: tsc | Category: type_error

[AUTO-887] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:388
    Tool: tsc | Category: type_error

[AUTO-888] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:389
    Tool: tsc | Category: type_error

[AUTO-889] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:390
    Tool: tsc | Category: type_error

[AUTO-890] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:3
    Tool: tsc | Category: type_error

[AUTO-891] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/DashboardPage.tsx:3
    Tool: tsc | Category: type_error

[AUTO-892] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:4
    Tool: tsc | Category: type_error

[AUTO-893] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:4
    Tool: tsc | Category: type_error

[AUTO-894] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:5
    Tool: tsc | Category: type_error

[AUTO-895] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:7
    Tool: tsc | Category: type_error

[AUTO-896] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:8
    Tool: tsc | Category: type_error

[AUTO-897] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:10
    Tool: tsc | Category: type_error

[AUTO-898] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:11
    Tool: tsc | Category: type_error

[AUTO-899] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:11
    Tool: tsc | Category: type_error

[AUTO-900] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:12
    Tool: tsc | Category: type_error

[AUTO-901] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:12
    Tool: tsc | Category: type_error

[AUTO-902] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:13
    Tool: tsc | Category: type_error

[AUTO-903] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:14
    Tool: tsc | Category: type_error

[AUTO-904] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:15
    Tool: tsc | Category: type_error

[AUTO-905] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:15
    Tool: tsc | Category: type_error

[AUTO-906] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:16
    Tool: tsc | Category: type_error

[AUTO-907] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:16
    Tool: tsc | Category: type_error

[AUTO-908] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:17
    Tool: tsc | Category: type_error

[AUTO-909] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:18
    Tool: tsc | Category: type_error

[AUTO-910] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:19
    Tool: tsc | Category: type_error

[AUTO-911] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:19
    Tool: tsc | Category: type_error

[AUTO-912] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:20
    Tool: tsc | Category: type_error

[AUTO-913] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:20
    Tool: tsc | Category: type_error

[AUTO-914] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:21
    Tool: tsc | Category: type_error

[AUTO-915] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:22
    Tool: tsc | Category: type_error

[AUTO-916] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:23
    Tool: tsc | Category: type_error

[AUTO-917] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:23
    Tool: tsc | Category: type_error

[AUTO-918] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:24
    Tool: tsc | Category: type_error

[AUTO-919] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:24
    Tool: tsc | Category: type_error

[AUTO-920] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:25
    Tool: tsc | Category: type_error

[AUTO-921] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:26
    Tool: tsc | Category: type_error

[AUTO-922] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:27
    Tool: tsc | Category: type_error

[AUTO-923] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/pages/HomePage.tsx:1
    Tool: tsc | Category: type_error

[AUTO-924] Cannot find module 'lucide-react' or its corresponding type declarations.
    File: src/pages/HomePage.tsx:2
    Tool: tsc | Category: type_error

[AUTO-925] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:29
    Tool: tsc | Category: type_error

[AUTO-926] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/HomePage.tsx:29
    Tool: tsc | Category: type_error

[AUTO-927] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:31
    Tool: tsc | Category: type_error

[AUTO-928] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:32
    Tool: tsc | Category: type_error

[AUTO-929] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:34
    Tool: tsc | Category: type_error

[AUTO-930] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:35
    Tool: tsc | Category: type_error

[AUTO-931] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:38
    Tool: tsc | Category: type_error

[AUTO-932] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:39
    Tool: tsc | Category: type_error

[AUTO-933] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:52
    Tool: tsc | Category: type_error

[AUTO-934] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:53
    Tool: tsc | Category: type_error

[AUTO-935] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:56
    Tool: tsc | Category: type_error

[AUTO-936] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:57
    Tool: tsc | Category: type_error

[AUTO-937] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:61
    Tool: tsc | Category: type_error

[AUTO-938] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:65
    Tool: tsc | Category: type_error

[AUTO-939] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:67
    Tool: tsc | Category: type_error

[AUTO-940] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:68
    Tool: tsc | Category: type_error

[AUTO-941] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:70
    Tool: tsc | Category: type_error

[AUTO-942] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:71
    Tool: tsc | Category: type_error

[AUTO-943] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:73
    Tool: tsc | Category: type_error

[AUTO-944] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:74
    Tool: tsc | Category: type_error

[AUTO-945] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:77
    Tool: tsc | Category: type_error

[AUTO-946] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:78
    Tool: tsc | Category: type_error

[AUTO-947] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:81
    Tool: tsc | Category: type_error

[AUTO-948] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-949] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:83
    Tool: tsc | Category: type_error

[AUTO-950] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:85
    Tool: tsc | Category: type_error

[AUTO-951] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:86
    Tool: tsc | Category: type_error

[AUTO-952] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:87
    Tool: tsc | Category: type_error

[AUTO-953] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:87
    Tool: tsc | Category: type_error

[AUTO-954] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:88
    Tool: tsc | Category: type_error

[AUTO-955] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:89
    Tool: tsc | Category: type_error

[AUTO-956] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:91
    Tool: tsc | Category: type_error

[AUTO-957] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:92
    Tool: tsc | Category: type_error

[AUTO-958] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:93
    Tool: tsc | Category: type_error

[AUTO-959] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:94
    Tool: tsc | Category: type_error

[AUTO-960] Cannot find module 'react' or its corresponding type declarations.
    File: src/pages/JobsPage.tsx:7
    Tool: tsc | Category: type_error

[AUTO-961] Parameter 'job' implicitly has an 'any' type.
    File: src/pages/JobsPage.tsx:48
    Tool: tsc | Category: type_error

[AUTO-962] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-963] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/JobsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-964] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:98
    Tool: tsc | Category: type_error

[AUTO-965] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:99
    Tool: tsc | Category: type_error

[AUTO-966] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:101
    Tool: tsc | Category: type_error

[AUTO-967] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:102
    Tool: tsc | Category: type_error

[AUTO-968] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:104
    Tool: tsc | Category: type_error

[AUTO-969] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:105
    Tool: tsc | Category: type_error

[AUTO-970] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:108
    Tool: tsc | Category: type_error

[AUTO-971] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:113
    Tool: tsc | Category: type_error

[AUTO-972] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:117
    Tool: tsc | Category: type_error

[AUTO-973] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:119
    Tool: tsc | Category: type_error

[AUTO-974] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:120
    Tool: tsc | Category: type_error

[AUTO-975] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:121
    Tool: tsc | Category: type_error

[AUTO-976] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:123
    Tool: tsc | Category: type_error

[AUTO-977] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:125
    Tool: tsc | Category: type_error

[AUTO-978] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:128
    Tool: tsc | Category: type_error

[AUTO-979] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:131
    Tool: tsc | Category: type_error

[AUTO-980] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:133
    Tool: tsc | Category: type_error

[AUTO-981] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:135
    Tool: tsc | Category: type_error

[AUTO-982] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:142
    Tool: tsc | Category: type_error

[AUTO-983] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:152
    Tool: tsc | Category: type_error

[AUTO-984] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:157
    Tool: tsc | Category: type_error

[AUTO-985] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:158
    Tool: tsc | Category: type_error

[AUTO-986] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:164
    Tool: tsc | Category: type_error

[AUTO-987] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:170
    Tool: tsc | Category: type_error

[AUTO-988] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:171
    Tool: tsc | Category: type_error

[AUTO-989] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:173
    Tool: tsc | Category: type_error

[AUTO-990] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:174
    Tool: tsc | Category: type_error

[AUTO-991] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:177
    Tool: tsc | Category: type_error

[AUTO-992] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:178
    Tool: tsc | Category: type_error

[AUTO-993] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:179
    Tool: tsc | Category: type_error

[AUTO-994] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:181
    Tool: tsc | Category: type_error

[AUTO-995] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:182
    Tool: tsc | Category: type_error

[AUTO-996] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:184
    Tool: tsc | Category: type_error

[AUTO-997] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:185
    Tool: tsc | Category: type_error

[AUTO-998] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:187
    Tool: tsc | Category: type_error

[AUTO-999] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:188
    Tool: tsc | Category: type_error

[AUTO-1000] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:189
    Tool: tsc | Category: type_error

[AUTO-1001] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:191
    Tool: tsc | Category: type_error


LOW Priority Issues (249):

[AUTO-001] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/api/applications.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-002] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/api/applications.py:10
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-003] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:145
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-004] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:148
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-005] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/applications.py:151
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-006] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/applications.py:153
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-007] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/applications.py:154
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-008] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/applications.py:159
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-009] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:185
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-010] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:212
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-011] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:249
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-012] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:287
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-013] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:290
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-014] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:326
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-015] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:329
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-016] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:359
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-017] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:362
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-018] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/applications.py:365
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-019] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/applications.py:369
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-020] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/applications.py:400
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-021] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:7
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-024] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:11
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-027] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:91
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-028] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:94
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-029] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:98
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-030] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:99
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-031] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:100
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-032] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:103
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-033] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:108
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-034] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:141
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-035] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:171
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-036] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:212
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-037] Within an `except` clause, raise exceptions with `raise ... from err` or `raise ... from None` to distinguish them from errors in exception handling
    File: /home/user/Job-o-matic/backend/src/api/jobs.py:244
    Tool: ruff | Category: lint
    Details: Code: B904

[AUTO-038] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:7
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-039] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-040] `typing.Dict` is deprecated, use `dict` instead
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-042] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:40
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-043] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:41
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-044] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:44
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-045] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:47
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-046] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:48
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-047] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:49
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-048] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:50
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-049] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:66
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-050] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:67
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-051] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:68
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-052] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:69
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-053] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:70
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-054] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:71
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-055] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:72
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-056] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:87
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-057] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:107
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-058] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:109
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-059] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:122
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-060] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:123
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-061] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:124
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-062] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:136
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-063] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:137
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-064] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:138
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-065] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:139
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-066] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:140
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-067] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/application_schemas.py:151
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-068] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:7
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-070] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-071] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:39
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-072] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:39
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-073] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:42
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-074] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:42
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-075] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:46
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-076] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:68
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-077] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:69
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-078] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:70
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-079] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:71
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-080] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:85
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-081] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:86
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-082] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:91
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-083] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:103
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-084] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:103
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-085] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:104
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-086] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:105
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-087] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:115
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-088] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:145
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-089] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:146
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-090] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:148
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-091] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:169
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-092] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:170
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-093] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:171
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-094] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:172
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-095] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:173
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-096] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/api/schemas/job_schemas.py:175
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-097] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/main.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-099] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/models/database.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-100] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/models/database.py:9
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-101] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:62
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-102] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:63
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-103] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:64
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-104] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:73
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-105] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:76
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-106] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:79
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-107] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:94
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-108] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:95
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-109] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:96
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-110] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:97
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-111] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:98
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-112] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:99
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-113] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:108
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-114] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:132
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-115] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:133
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-116] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:141
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-117] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:145
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-118] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:148
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-119] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:158
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-120] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:158
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-121] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:169
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-122] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:197
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-123] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:198
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-124] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:199
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-125] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:200
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-126] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:201
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-127] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:202
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-128] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:203
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-129] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:204
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-130] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:215
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-131] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/models/database.py:218
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-132] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:240
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-133] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:246
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-134] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:271
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-135] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:305
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-136] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:338
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-137] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:341
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-138] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:342
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-139] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:343
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-140] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/models/database.py:344
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-141] Import from `collections.abc` instead: `AsyncGenerator`
    File: /home/user/Job-o-matic/backend/src/models/session.py:7
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-142] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/models/session.py:7
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-144] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-145] `typing.Dict` is deprecated, use `dict` instead
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-146] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-147] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:72
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-148] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:72
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-149] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:73
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-150] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:73
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-151] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:75
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-152] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:77
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-153] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:77
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-154] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:130
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-155] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:131
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-156] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:131
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-157] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:133
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-158] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:135
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-159] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:135
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-160] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:161
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-161] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:161
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-162] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:185
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-163] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:185
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-164] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:236
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-165] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:236
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-166] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:244
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-167] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:244
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-168] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:244
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-169] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:244
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-170] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:251
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-171] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:251
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-172] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:264
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-173] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:264
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-174] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:281
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-175] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:301
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-176] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/scrapers/jobspy_client.py:319
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-177] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-178] `typing.Dict` is deprecated, use `dict` instead
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-179] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-183] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:28
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-184] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:28
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-185] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:82
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-186] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:83
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-187] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:84
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-188] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:119
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-189] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:134
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-190] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:135
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-191] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:181
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-192] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:182
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-193] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:222
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-194] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:223
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-195] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:227
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-196] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:324
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-197] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:356
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-198] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:394
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-199] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:398
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-200] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:464
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-201] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:491
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-202] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:492
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-203] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:530
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-205] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:569
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-207] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:617
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-208] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:619
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-209] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:639
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-210] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:654
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-211] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:654
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-212] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/application_service.py:676
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-213] `typing.List` is deprecated, use `list` instead
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-214] `typing.Dict` is deprecated, use `dict` instead
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-215] `typing.Set` is deprecated, use `set` instead
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-216] `typing.Tuple` is deprecated, use `tuple` instead
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:8
    Tool: ruff | Category: lint
    Details: Code: UP035

[AUTO-217] Import block is un-sorted or un-formatted
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:8
    Tool: ruff | Category: lint
    Details: Code: I001

[AUTO-219] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:33
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-220] Use `tuple` instead of `Tuple` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:33
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-221] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:33
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-222] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:35
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-223] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:35
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-224] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:39
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-225] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:47
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-226] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:49
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-227] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:68
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-228] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:88
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-229] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:88
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-230] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:89
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-231] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:89
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-232] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:91
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-233] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:94
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-234] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:183
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-235] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:184
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-236] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:232
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-237] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:233
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-238] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:272
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-239] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:273
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-240] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:285
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-241] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:286
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-242] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:290
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-243] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:290
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-244] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:291
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-245] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:291
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-246] Use `set` instead of `Set` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:302
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-247] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:303
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-248] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:303
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-249] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:341
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-250] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:341
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-251] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:342
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-252] Use `dict` instead of `Dict` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:342
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-253] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:483
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-254] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:485
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-255] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:486
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-256] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:508
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-257] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:508
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-258] Use `datetime.UTC` alias
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:529
    Tool: ruff | Category: lint
    Details: Code: UP017

[AUTO-259] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:543
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-260] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:543
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-261] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:544
    Tool: ruff | Category: lint
    Details: Code: UP045

[AUTO-262] Use `list` instead of `List` for type annotation
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:544
    Tool: ruff | Category: lint
    Details: Code: UP006

[AUTO-263] Use `X | None` for type annotations
    File: /home/user/Job-o-matic/backend/src/services/job_search_service.py:546
    Tool: ruff | Category: lint
    Details: Code: UP045


INFO Priority Issues (10):

[AUTO-1002] TODO comment found
    File: backend/src/api/applications.py:121
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1003] TODO comment found
    File: backend/src/api/applications.py:168
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1004] TODO comment found
    File: backend/src/api/applications.py:200
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1005] TODO comment found
    File: backend/src/api/applications.py:228
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1006] TODO comment found
    File: backend/src/api/applications.py:267
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1007] TODO comment found
    File: backend/src/api/applications.py:308
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1008] TODO comment found
    File: backend/src/api/applications.py:346
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1009] TODO comment found
    File: backend/src/api/applications.py:378
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-1010] TODO comment found
    File: frontend/src/api/client.ts:24
    Tool: grep | Category: code_quality
    Details: // TODO: Add authentication token when auth is implemented

[AUTO-1011] TODO comment found
    File: frontend/src/api/client.ts:54
    Tool: grep | Category: code_quality
    Details: // TODO: Redirect to login when auth is implemented

💡 RECOMMENDATIONS
--------------------------------------------------------------------------------
⚠️  HIGH: Address high priority issues in current sprint
⚠️  Fix linting issues to maintain code quality

================================================================================