================================================================================
AUTOMATED TEST & BUG REPORT
================================================================================
Generated: 2025-11-22 18:22:18

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
Total Bugs Found:  757

🐛 BUGS BY SEVERITY
--------------------------------------------------------------------------------
MEDIUM       730 issues
LOW           17 issues
INFO          10 issues

📋 DETAILED BUG LIST
--------------------------------------------------------------------------------

MEDIUM Priority Issues (730):

[AUTO-018] Class cannot subclass "DeclarativeBase" (has type "Any")  [misc]
    File: src/models/database.py:16
    Tool: mypy | Category: type_error

[AUTO-019] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:32
    Tool: mypy | Category: type_error

[AUTO-020] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:61
    Tool: mypy | Category: type_error

[AUTO-021] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:75
    Tool: mypy | Category: type_error

[AUTO-022] Missing type parameters for generic type "dict"  [type-arg]
    File: src/api/schemas/job_schemas.py:102
    Tool: mypy | Category: type_error

[AUTO-023] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:110
    Tool: mypy | Category: type_error

[AUTO-024] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:133
    Tool: mypy | Category: type_error

[AUTO-025] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/job_schemas.py:164
    Tool: mypy | Category: type_error

[AUTO-026] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:32
    Tool: mypy | Category: type_error

[AUTO-027] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:59
    Tool: mypy | Category: type_error

[AUTO-028] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:79
    Tool: mypy | Category: type_error

[AUTO-029] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:97
    Tool: mypy | Category: type_error

[AUTO-030] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:110
    Tool: mypy | Category: type_error

[AUTO-031] Class cannot subclass "BaseModel" (has type "Any")  [misc]
    File: src/api/schemas/application_schemas.py:140
    Tool: mypy | Category: type_error

[AUTO-032] Function is missing a return type annotation  [no-untyped-def]
    File: src/services/application_service.py:72
    Tool: mypy | Category: type_error

[AUTO-033] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/application_service.py:76
    Tool: mypy | Category: type_error

[AUTO-034] Returning Any from function declared to return "Application | None"  [no-any-return]
    File: src/services/application_service.py:210
    Tool: mypy | Category: type_error

[AUTO-035] Returning Any from function declared to return "list[Application]"  [no-any-return]
    File: src/services/application_service.py:268
    Tool: mypy | Category: type_error

[AUTO-036] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/application_service.py:274
    Tool: mypy | Category: type_error

[AUTO-037] Returning Any from function declared to return "list[ApplicationStatusHistory]"  [no-any-return]
    File: src/services/application_service.py:510
    Tool: mypy | Category: type_error

[AUTO-038] Class cannot subclass "BaseSettings" (has type "Any")  [misc]
    File: src/models/session.py:16
    Tool: mypy | Category: type_error

[AUTO-039] Function is missing a return type annotation  [no-untyped-def]
    File: src/models/session.py:34
    Tool: mypy | Category: type_error

[AUTO-040] Function is missing a return type annotation  [no-untyped-def]
    File: src/models/session.py:50
    Tool: mypy | Category: type_error

[AUTO-041] Call to untyped function "get_engine" in typed context  [no-untyped-call]
    File: src/models/session.py:54
    Tool: mypy | Category: type_error

[AUTO-042] Call to untyped function "get_session_maker" in typed context  [no-untyped-call]
    File: src/models/session.py:81
    Tool: mypy | Category: type_error

[AUTO-043] Call to untyped function "get_engine" in typed context  [no-untyped-call]
    File: src/models/session.py:102
    Tool: mypy | Category: type_error

[AUTO-044] Call to untyped function "ApplicationService" in typed context  [no-untyped-call]
    File: src/api/applications.py:33
    Tool: mypy | Category: type_error

[AUTO-045] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/api/applications.py:37
    Tool: mypy | Category: type_error

[AUTO-046] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/api/applications.py:79
    Tool: mypy | Category: type_error

[AUTO-047] Untyped decorator makes function "create_application" untyped  [misc]
    File: src/api/applications.py:107
    Tool: mypy | Category: type_error

[AUTO-048] Argument "status" to "create_application" of "ApplicationService" has incompatible type "ApplicationStatusEnum"; expected "ApplicationStatus"  [arg-type]
    File: src/api/applications.py:128
    Tool: mypy | Category: type_error

[AUTO-049] Untyped decorator makes function "list_applications" untyped  [misc]
    File: src/api/applications.py:151
    Tool: mypy | Category: type_error

[AUTO-050] Argument "status" to "get_applications" of "ApplicationService" has incompatible type "ApplicationStatusEnum | None"; expected "ApplicationStatus | None"  [arg-type]
    File: src/api/applications.py:174
    Tool: mypy | Category: type_error

[AUTO-051] Untyped decorator makes function "get_application_stats" untyped  [misc]
    File: src/api/applications.py:188
    Tool: mypy | Category: type_error

[AUTO-052] Untyped decorator makes function "get_application" untyped  [misc]
    File: src/api/applications.py:215
    Tool: mypy | Category: type_error

[AUTO-053] Untyped decorator makes function "update_application" untyped  [misc]
    File: src/api/applications.py:249
    Tool: mypy | Category: type_error

[AUTO-054] Untyped decorator makes function "update_application_status" untyped  [misc]
    File: src/api/applications.py:290
    Tool: mypy | Category: type_error

[AUTO-055] Argument "new_status" to "update_status" of "ApplicationService" has incompatible type "ApplicationStatusEnum"; expected "ApplicationStatus"  [arg-type]
    File: src/api/applications.py:312
    Tool: mypy | Category: type_error

[AUTO-056] Untyped decorator makes function "delete_application" untyped  [misc]
    File: src/api/applications.py:329
    Tool: mypy | Category: type_error

[AUTO-057] Untyped decorator makes function "get_application_history" untyped  [misc]
    File: src/api/applications.py:362
    Tool: mypy | Category: type_error

[AUTO-058] Function is missing a return type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:17
    Tool: mypy | Category: type_error

[AUTO-059] Function is missing a type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:20
    Tool: mypy | Category: type_error

[AUTO-060] Function is missing a type annotation  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:22
    Tool: mypy | Category: type_error

[AUTO-061] Untyped decorator makes function "search" untyped  [misc]
    File: src/scrapers/jobspy_client.py:67
    Tool: mypy | Category: type_error

[AUTO-062] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:68
    Tool: mypy | Category: type_error

[AUTO-063] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/scrapers/jobspy_client.py:126
    Tool: mypy | Category: type_error

[AUTO-064] Missing type parameters for generic type "dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:229
    Tool: mypy | Category: type_error

[AUTO-065] Missing type parameters for generic type "dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:236
    Tool: mypy | Category: type_error

[AUTO-066] Returning Any from function declared to return "list[str] | None"  [no-any-return]
    File: src/scrapers/jobspy_client.py:240
    Tool: mypy | Category: type_error

[AUTO-067] Missing type parameters for generic type "dict"  [type-arg]
    File: src/scrapers/jobspy_client.py:256
    Tool: mypy | Category: type_error

[AUTO-068] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/job_search_service.py:82
    Tool: mypy | Category: type_error

[AUTO-069] Returning Any from function declared to return "Company"  [no-any-return]
    File: src/services/job_search_service.py:259
    Tool: mypy | Category: type_error

[AUTO-070] Function is missing a type annotation for one or more arguments  [no-untyped-def]
    File: src/services/job_search_service.py:416
    Tool: mypy | Category: type_error

[AUTO-071] Untyped decorator makes function "search_jobs" untyped  [misc]
    File: src/api/jobs.py:37
    Tool: mypy | Category: type_error

[AUTO-072] Argument "employment_type" to "search_jobs" of "JobSearchService" has incompatible type "list[EmploymentTypeEnum] | None"; expected "list[str] | None"  [arg-type]
    File: src/api/jobs.py:68
    Tool: mypy | Category: type_error

[AUTO-073] Untyped decorator makes function "list_jobs" untyped  [misc]
    File: src/api/jobs.py:93
    Tool: mypy | Category: type_error

[AUTO-074] Untyped decorator makes function "get_job" untyped  [misc]
    File: src/api/jobs.py:141
    Tool: mypy | Category: type_error

[AUTO-075] Untyped decorator makes function "create_manual_job" untyped  [misc]
    File: src/api/jobs.py:171
    Tool: mypy | Category: type_error

[AUTO-076] Untyped decorator makes function "delete_job" untyped  [misc]
    File: src/api/jobs.py:212
    Tool: mypy | Category: type_error

[AUTO-077] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:28
    Tool: mypy | Category: type_error

[AUTO-078] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:80
    Tool: mypy | Category: type_error

[AUTO-079] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:92
    Tool: mypy | Category: type_error

[AUTO-080] Function is missing a return type annotation  [no-untyped-def]
    File: src/main.py:99
    Tool: mypy | Category: type_error

[AUTO-081] Function is missing a type annotation  [no-untyped-def]
    File: src/main.py:115
    Tool: mypy | Category: type_error

[AUTO-082] Function is missing a type annotation  [no-untyped-def]
    File: src/main.py:127
    Tool: mypy | Category: type_error

[AUTO-083] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/App.tsx:1
    Tool: tsc | Category: type_error

[AUTO-084] Cannot find module 'react' or its corresponding type declarations.
    File: src/App.tsx:2
    Tool: tsc | Category: type_error

[AUTO-085] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/App.tsx:3
    Tool: tsc | Category: type_error

[AUTO-086] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/App.tsx:47
    Tool: tsc | Category: type_error

[AUTO-087] Cannot find module 'axios' or its corresponding type declarations.
    File: src/api/client.ts:7
    Tool: tsc | Category: type_error

[AUTO-088] Property 'env' does not exist on type 'ImportMeta'.
    File: src/api/client.ts:10
    Tool: tsc | Category: type_error

[AUTO-089] Parameter 'config' implicitly has an 'any' type.
    File: src/api/client.ts:23
    Tool: tsc | Category: type_error

[AUTO-090] Parameter 'error' implicitly has an 'any' type.
    File: src/api/client.ts:31
    Tool: tsc | Category: type_error

[AUTO-091] Cannot find namespace 'React'.
    File: src/components/ApplicationCard.tsx:42
    Tool: tsc | Category: type_error

[AUTO-092] Cannot find namespace 'React'.
    File: src/components/ApplicationCard.tsx:49
    Tool: tsc | Category: type_error

[AUTO-093] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:57
    Tool: tsc | Category: type_error

[AUTO-094] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationCard.tsx:57
    Tool: tsc | Category: type_error

[AUTO-095] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:64
    Tool: tsc | Category: type_error

[AUTO-096] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:65
    Tool: tsc | Category: type_error

[AUTO-097] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:66
    Tool: tsc | Category: type_error

[AUTO-098] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:68
    Tool: tsc | Category: type_error

[AUTO-099] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:69
    Tool: tsc | Category: type_error

[AUTO-100] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:71
    Tool: tsc | Category: type_error

[AUTO-101] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:72
    Tool: tsc | Category: type_error

[AUTO-102] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:74
    Tool: tsc | Category: type_error

[AUTO-103] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:75
    Tool: tsc | Category: type_error

[AUTO-104] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:78
    Tool: tsc | Category: type_error

[AUTO-105] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:80
    Tool: tsc | Category: type_error

[AUTO-106] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:85
    Tool: tsc | Category: type_error

[AUTO-107] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:86
    Tool: tsc | Category: type_error

[AUTO-108] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:91
    Tool: tsc | Category: type_error

[AUTO-109] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:92
    Tool: tsc | Category: type_error

[AUTO-110] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:94
    Tool: tsc | Category: type_error

[AUTO-111] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:95
    Tool: tsc | Category: type_error

[AUTO-112] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:98
    Tool: tsc | Category: type_error

[AUTO-113] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:99
    Tool: tsc | Category: type_error

[AUTO-114] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:104
    Tool: tsc | Category: type_error

[AUTO-115] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:105
    Tool: tsc | Category: type_error

[AUTO-116] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:108
    Tool: tsc | Category: type_error

[AUTO-117] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:110
    Tool: tsc | Category: type_error

[AUTO-118] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:111
    Tool: tsc | Category: type_error

[AUTO-119] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:117
    Tool: tsc | Category: type_error

[AUTO-120] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:123
    Tool: tsc | Category: type_error

[AUTO-121] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:124
    Tool: tsc | Category: type_error

[AUTO-122] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:126
    Tool: tsc | Category: type_error

[AUTO-123] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:127
    Tool: tsc | Category: type_error

[AUTO-124] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:131
    Tool: tsc | Category: type_error

[AUTO-125] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:132
    Tool: tsc | Category: type_error

[AUTO-126] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:138
    Tool: tsc | Category: type_error

[AUTO-127] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:144
    Tool: tsc | Category: type_error

[AUTO-128] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:145
    Tool: tsc | Category: type_error

[AUTO-129] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:147
    Tool: tsc | Category: type_error

[AUTO-130] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:148
    Tool: tsc | Category: type_error

[AUTO-131] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-132] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:153
    Tool: tsc | Category: type_error

[AUTO-133] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:159
    Tool: tsc | Category: type_error

[AUTO-134] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:165
    Tool: tsc | Category: type_error

[AUTO-135] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:166
    Tool: tsc | Category: type_error

[AUTO-136] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:168
    Tool: tsc | Category: type_error

[AUTO-137] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:169
    Tool: tsc | Category: type_error

[AUTO-138] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:171
    Tool: tsc | Category: type_error

[AUTO-139] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:174
    Tool: tsc | Category: type_error

[AUTO-140] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:175
    Tool: tsc | Category: type_error

[AUTO-141] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:177
    Tool: tsc | Category: type_error

[AUTO-142] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:178
    Tool: tsc | Category: type_error

[AUTO-143] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationCard.tsx:179
    Tool: tsc | Category: type_error

[AUTO-144] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:30
    Tool: tsc | Category: type_error

[AUTO-145] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationList.tsx:30
    Tool: tsc | Category: type_error

[AUTO-146] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:32
    Tool: tsc | Category: type_error

[AUTO-147] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:36
    Tool: tsc | Category: type_error

[AUTO-148] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:37
    Tool: tsc | Category: type_error

[AUTO-149] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:38
    Tool: tsc | Category: type_error

[AUTO-150] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:39
    Tool: tsc | Category: type_error

[AUTO-151] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:40
    Tool: tsc | Category: type_error

[AUTO-152] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:41
    Tool: tsc | Category: type_error

[AUTO-153] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:42
    Tool: tsc | Category: type_error

[AUTO-154] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:43
    Tool: tsc | Category: type_error

[AUTO-155] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:44
    Tool: tsc | Category: type_error

[AUTO-156] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:45
    Tool: tsc | Category: type_error

[AUTO-157] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:46
    Tool: tsc | Category: type_error

[AUTO-158] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:47
    Tool: tsc | Category: type_error

[AUTO-159] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:48
    Tool: tsc | Category: type_error

[AUTO-160] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:49
    Tool: tsc | Category: type_error

[AUTO-161] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:50
    Tool: tsc | Category: type_error

[AUTO-162] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:52
    Tool: tsc | Category: type_error

[AUTO-163] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:59
    Tool: tsc | Category: type_error

[AUTO-164] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:60
    Tool: tsc | Category: type_error

[AUTO-165] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:66
    Tool: tsc | Category: type_error

[AUTO-166] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:72
    Tool: tsc | Category: type_error

[AUTO-167] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:73
    Tool: tsc | Category: type_error

[AUTO-168] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:75
    Tool: tsc | Category: type_error

[AUTO-169] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:76
    Tool: tsc | Category: type_error

[AUTO-170] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:78
    Tool: tsc | Category: type_error

[AUTO-171] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:79
    Tool: tsc | Category: type_error

[AUTO-172] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:86
    Tool: tsc | Category: type_error

[AUTO-173] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:87
    Tool: tsc | Category: type_error

[AUTO-174] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:93
    Tool: tsc | Category: type_error

[AUTO-175] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:99
    Tool: tsc | Category: type_error

[AUTO-176] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:100
    Tool: tsc | Category: type_error

[AUTO-177] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:102
    Tool: tsc | Category: type_error

[AUTO-178] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:103
    Tool: tsc | Category: type_error

[AUTO-179] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:105
    Tool: tsc | Category: type_error

[AUTO-180] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:106
    Tool: tsc | Category: type_error

[AUTO-181] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:112
    Tool: tsc | Category: type_error

[AUTO-182] Type '{ key: number; application: Application; onClick: ((application: Application) => void) | undefined; onStatusClick: ((application: Application) => void) | undefined; onDelete: ((application: Application) => void) | undefined; }' is not assignable to type 'ApplicationCardProps'.
    File: src/components/ApplicationList.tsx:115
    Tool: tsc | Category: type_error

[AUTO-183] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationList.tsx:122
    Tool: tsc | Category: type_error

[AUTO-184] Cannot find namespace 'JSX'.
    File: src/components/ApplicationStatusBadge.tsx:49
    Tool: tsc | Category: type_error

[AUTO-185] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:55
    Tool: tsc | Category: type_error

[AUTO-186] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:56
    Tool: tsc | Category: type_error

[AUTO-187] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:57
    Tool: tsc | Category: type_error

[AUTO-188] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:61
    Tool: tsc | Category: type_error

[AUTO-189] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:62
    Tool: tsc | Category: type_error

[AUTO-190] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:63
    Tool: tsc | Category: type_error

[AUTO-191] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:64
    Tool: tsc | Category: type_error

[AUTO-192] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:70
    Tool: tsc | Category: type_error

[AUTO-193] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:71
    Tool: tsc | Category: type_error

[AUTO-194] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:76
    Tool: tsc | Category: type_error

[AUTO-195] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:80
    Tool: tsc | Category: type_error

[AUTO-196] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:81
    Tool: tsc | Category: type_error

[AUTO-197] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:82
    Tool: tsc | Category: type_error

[AUTO-198] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:87
    Tool: tsc | Category: type_error

[AUTO-199] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:91
    Tool: tsc | Category: type_error

[AUTO-200] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:92
    Tool: tsc | Category: type_error

[AUTO-201] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:97
    Tool: tsc | Category: type_error

[AUTO-202] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:101
    Tool: tsc | Category: type_error

[AUTO-203] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:102
    Tool: tsc | Category: type_error

[AUTO-204] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:107
    Tool: tsc | Category: type_error

[AUTO-205] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:111
    Tool: tsc | Category: type_error

[AUTO-206] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:112
    Tool: tsc | Category: type_error

[AUTO-207] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:117
    Tool: tsc | Category: type_error

[AUTO-208] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:132
    Tool: tsc | Category: type_error

[AUTO-209] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationStatusBadge.tsx:132
    Tool: tsc | Category: type_error

[AUTO-210] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationStatusBadge.tsx:139
    Tool: tsc | Category: type_error

[AUTO-211] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:26
    Tool: tsc | Category: type_error

[AUTO-212] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/ApplicationTimeline.tsx:26
    Tool: tsc | Category: type_error

[AUTO-213] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:28
    Tool: tsc | Category: type_error

[AUTO-214] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:33
    Tool: tsc | Category: type_error

[AUTO-215] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:34
    Tool: tsc | Category: type_error

[AUTO-216] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:36
    Tool: tsc | Category: type_error

[AUTO-217] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:37
    Tool: tsc | Category: type_error

[AUTO-218] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:40
    Tool: tsc | Category: type_error

[AUTO-219] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:46
    Tool: tsc | Category: type_error

[AUTO-220] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:48
    Tool: tsc | Category: type_error

[AUTO-221] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:49
    Tool: tsc | Category: type_error

[AUTO-222] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:50
    Tool: tsc | Category: type_error

[AUTO-223] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:55
    Tool: tsc | Category: type_error

[AUTO-224] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:60
    Tool: tsc | Category: type_error

[AUTO-225] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:61
    Tool: tsc | Category: type_error

[AUTO-226] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:62
    Tool: tsc | Category: type_error

[AUTO-227] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:65
    Tool: tsc | Category: type_error

[AUTO-228] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:66
    Tool: tsc | Category: type_error

[AUTO-229] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:70
    Tool: tsc | Category: type_error

[AUTO-230] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:76
    Tool: tsc | Category: type_error

[AUTO-231] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:82
    Tool: tsc | Category: type_error

[AUTO-232] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:86
    Tool: tsc | Category: type_error

[AUTO-233] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:88
    Tool: tsc | Category: type_error

[AUTO-234] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:90
    Tool: tsc | Category: type_error

[AUTO-235] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:93
    Tool: tsc | Category: type_error

[AUTO-236] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:95
    Tool: tsc | Category: type_error

[AUTO-237] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:97
    Tool: tsc | Category: type_error

[AUTO-238] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:98
    Tool: tsc | Category: type_error

[AUTO-239] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:99
    Tool: tsc | Category: type_error

[AUTO-240] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:100
    Tool: tsc | Category: type_error

[AUTO-241] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:102
    Tool: tsc | Category: type_error

[AUTO-242] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/ApplicationTimeline.tsx:103
    Tool: tsc | Category: type_error

[AUTO-243] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:90
    Tool: tsc | Category: type_error

[AUTO-244] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobCard.tsx:90
    Tool: tsc | Category: type_error

[AUTO-245] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:97
    Tool: tsc | Category: type_error

[AUTO-246] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:99
    Tool: tsc | Category: type_error

[AUTO-247] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:105
    Tool: tsc | Category: type_error

[AUTO-248] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:106
    Tool: tsc | Category: type_error

[AUTO-249] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:108
    Tool: tsc | Category: type_error

[AUTO-250] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:109
    Tool: tsc | Category: type_error

[AUTO-251] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:112
    Tool: tsc | Category: type_error

[AUTO-252] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:113
    Tool: tsc | Category: type_error

[AUTO-253] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:115
    Tool: tsc | Category: type_error

[AUTO-254] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:116
    Tool: tsc | Category: type_error

[AUTO-255] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:118
    Tool: tsc | Category: type_error

[AUTO-256] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:119
    Tool: tsc | Category: type_error

[AUTO-257] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:121
    Tool: tsc | Category: type_error

[AUTO-258] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:122
    Tool: tsc | Category: type_error

[AUTO-259] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:123
    Tool: tsc | Category: type_error

[AUTO-260] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:126
    Tool: tsc | Category: type_error

[AUTO-261] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:128
    Tool: tsc | Category: type_error

[AUTO-262] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:134
    Tool: tsc | Category: type_error

[AUTO-263] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:136
    Tool: tsc | Category: type_error

[AUTO-264] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:138
    Tool: tsc | Category: type_error

[AUTO-265] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:139
    Tool: tsc | Category: type_error

[AUTO-266] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:141
    Tool: tsc | Category: type_error

[AUTO-267] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:142
    Tool: tsc | Category: type_error

[AUTO-268] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:145
    Tool: tsc | Category: type_error

[AUTO-269] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:147
    Tool: tsc | Category: type_error

[AUTO-270] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:149
    Tool: tsc | Category: type_error

[AUTO-271] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-272] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:152
    Tool: tsc | Category: type_error

[AUTO-273] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:154
    Tool: tsc | Category: type_error

[AUTO-274] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobCard.tsx:155
    Tool: tsc | Category: type_error

[AUTO-275] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/JobFilters.tsx:5
    Tool: tsc | Category: type_error

[AUTO-276] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:46
    Tool: tsc | Category: type_error

[AUTO-277] Parameter 't' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:47
    Tool: tsc | Category: type_error

[AUTO-278] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:52
    Tool: tsc | Category: type_error

[AUTO-279] Parameter 'p' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:53
    Tool: tsc | Category: type_error

[AUTO-280] Parameter 'prev' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:58
    Tool: tsc | Category: type_error

[AUTO-281] Parameter 's' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:59
    Tool: tsc | Category: type_error

[AUTO-282] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:70
    Tool: tsc | Category: type_error

[AUTO-283] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobFilters.tsx:70
    Tool: tsc | Category: type_error

[AUTO-284] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:72
    Tool: tsc | Category: type_error

[AUTO-285] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:76
    Tool: tsc | Category: type_error

[AUTO-286] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:82
    Tool: tsc | Category: type_error

[AUTO-287] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:88
    Tool: tsc | Category: type_error

[AUTO-288] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:89
    Tool: tsc | Category: type_error

[AUTO-289] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:91
    Tool: tsc | Category: type_error

[AUTO-290] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:93
    Tool: tsc | Category: type_error

[AUTO-291] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:95
    Tool: tsc | Category: type_error

[AUTO-292] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:97
    Tool: tsc | Category: type_error

[AUTO-293] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:101
    Tool: tsc | Category: type_error

[AUTO-294] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:102
    Tool: tsc | Category: type_error

[AUTO-295] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:103
    Tool: tsc | Category: type_error

[AUTO-296] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:105
    Tool: tsc | Category: type_error

[AUTO-297] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:106
    Tool: tsc | Category: type_error

[AUTO-298] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:108
    Tool: tsc | Category: type_error

[AUTO-299] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:110
    Tool: tsc | Category: type_error

[AUTO-300] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:111
    Tool: tsc | Category: type_error

[AUTO-301] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:113
    Tool: tsc | Category: type_error

[AUTO-302] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:114
    Tool: tsc | Category: type_error

[AUTO-303] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:116
    Tool: tsc | Category: type_error

[AUTO-304] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:117
    Tool: tsc | Category: type_error

[AUTO-305] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:123
    Tool: tsc | Category: type_error

[AUTO-306] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:125
    Tool: tsc | Category: type_error

[AUTO-307] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:126
    Tool: tsc | Category: type_error

[AUTO-308] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:128
    Tool: tsc | Category: type_error

[AUTO-309] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:129
    Tool: tsc | Category: type_error

[AUTO-310] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:132
    Tool: tsc | Category: type_error

[AUTO-311] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:133
    Tool: tsc | Category: type_error

[AUTO-312] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:135
    Tool: tsc | Category: type_error

[AUTO-313] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:136
    Tool: tsc | Category: type_error

[AUTO-314] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:139
    Tool: tsc | Category: type_error

[AUTO-315] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:140
    Tool: tsc | Category: type_error

[AUTO-316] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:146
    Tool: tsc | Category: type_error

[AUTO-317] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:148
    Tool: tsc | Category: type_error

[AUTO-318] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:149
    Tool: tsc | Category: type_error

[AUTO-319] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:152
    Tool: tsc | Category: type_error

[AUTO-320] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:153
    Tool: tsc | Category: type_error

[AUTO-321] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:156
    Tool: tsc | Category: type_error

[AUTO-322] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:157
    Tool: tsc | Category: type_error

[AUTO-323] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:162
    Tool: tsc | Category: type_error

[AUTO-324] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:163
    Tool: tsc | Category: type_error

[AUTO-325] Parameter 'e' implicitly has an 'any' type.
    File: src/components/JobFilters.tsx:167
    Tool: tsc | Category: type_error

[AUTO-326] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:171
    Tool: tsc | Category: type_error

[AUTO-327] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:174
    Tool: tsc | Category: type_error

[AUTO-328] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:175
    Tool: tsc | Category: type_error

[AUTO-329] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:177
    Tool: tsc | Category: type_error

[AUTO-330] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:178
    Tool: tsc | Category: type_error

[AUTO-331] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:181
    Tool: tsc | Category: type_error

[AUTO-332] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:182
    Tool: tsc | Category: type_error

[AUTO-333] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:188
    Tool: tsc | Category: type_error

[AUTO-334] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:190
    Tool: tsc | Category: type_error

[AUTO-335] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:191
    Tool: tsc | Category: type_error

[AUTO-336] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:194
    Tool: tsc | Category: type_error

[AUTO-337] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:195
    Tool: tsc | Category: type_error

[AUTO-338] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:196
    Tool: tsc | Category: type_error

[AUTO-339] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:199
    Tool: tsc | Category: type_error

[AUTO-340] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:200
    Tool: tsc | Category: type_error

[AUTO-341] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:205
    Tool: tsc | Category: type_error

[AUTO-342] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:206
    Tool: tsc | Category: type_error

[AUTO-343] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:211
    Tool: tsc | Category: type_error

[AUTO-344] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:212
    Tool: tsc | Category: type_error

[AUTO-345] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:213
    Tool: tsc | Category: type_error

[AUTO-346] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobFilters.tsx:215
    Tool: tsc | Category: type_error

[AUTO-347] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:26
    Tool: tsc | Category: type_error

[AUTO-348] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/JobList.tsx:26
    Tool: tsc | Category: type_error

[AUTO-349] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:28
    Tool: tsc | Category: type_error

[AUTO-350] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:32
    Tool: tsc | Category: type_error

[AUTO-351] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:33
    Tool: tsc | Category: type_error

[AUTO-352] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:34
    Tool: tsc | Category: type_error

[AUTO-353] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:35
    Tool: tsc | Category: type_error

[AUTO-354] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:36
    Tool: tsc | Category: type_error

[AUTO-355] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:37
    Tool: tsc | Category: type_error

[AUTO-356] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:38
    Tool: tsc | Category: type_error

[AUTO-357] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:39
    Tool: tsc | Category: type_error

[AUTO-358] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:40
    Tool: tsc | Category: type_error

[AUTO-359] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:41
    Tool: tsc | Category: type_error

[AUTO-360] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:42
    Tool: tsc | Category: type_error

[AUTO-361] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:43
    Tool: tsc | Category: type_error

[AUTO-362] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:44
    Tool: tsc | Category: type_error

[AUTO-363] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:45
    Tool: tsc | Category: type_error

[AUTO-364] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:47
    Tool: tsc | Category: type_error

[AUTO-365] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:54
    Tool: tsc | Category: type_error

[AUTO-366] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:55
    Tool: tsc | Category: type_error

[AUTO-367] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:61
    Tool: tsc | Category: type_error

[AUTO-368] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:67
    Tool: tsc | Category: type_error

[AUTO-369] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:68
    Tool: tsc | Category: type_error

[AUTO-370] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:70
    Tool: tsc | Category: type_error

[AUTO-371] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:71
    Tool: tsc | Category: type_error

[AUTO-372] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:73
    Tool: tsc | Category: type_error

[AUTO-373] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:74
    Tool: tsc | Category: type_error

[AUTO-374] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:81
    Tool: tsc | Category: type_error

[AUTO-375] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:82
    Tool: tsc | Category: type_error

[AUTO-376] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:88
    Tool: tsc | Category: type_error

[AUTO-377] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:94
    Tool: tsc | Category: type_error

[AUTO-378] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:95
    Tool: tsc | Category: type_error

[AUTO-379] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:97
    Tool: tsc | Category: type_error

[AUTO-380] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:98
    Tool: tsc | Category: type_error

[AUTO-381] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:100
    Tool: tsc | Category: type_error

[AUTO-382] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:101
    Tool: tsc | Category: type_error

[AUTO-383] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:107
    Tool: tsc | Category: type_error

[AUTO-384] Type '{ key: number; job: Job; onClick: ((job: Job) => void) | undefined; }' is not assignable to type 'JobCardProps'.
    File: src/components/JobList.tsx:109
    Tool: tsc | Category: type_error

[AUTO-385] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/JobList.tsx:111
    Tool: tsc | Category: type_error

[AUTO-386] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/Layout.tsx:1
    Tool: tsc | Category: type_error

[AUTO-387] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/components/Layout.tsx:2
    Tool: tsc | Category: type_error

[AUTO-388] Cannot find module 'lucide-react' or its corresponding type declarations.
    File: src/components/Layout.tsx:3
    Tool: tsc | Category: type_error

[AUTO-389] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:26
    Tool: tsc | Category: type_error

[AUTO-390] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/Layout.tsx:26
    Tool: tsc | Category: type_error

[AUTO-391] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:28
    Tool: tsc | Category: type_error

[AUTO-392] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:29
    Tool: tsc | Category: type_error

[AUTO-393] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:30
    Tool: tsc | Category: type_error

[AUTO-394] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:32
    Tool: tsc | Category: type_error

[AUTO-395] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:34
    Tool: tsc | Category: type_error

[AUTO-396] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:36
    Tool: tsc | Category: type_error

[AUTO-397] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:37
    Tool: tsc | Category: type_error

[AUTO-398] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:40
    Tool: tsc | Category: type_error

[AUTO-399] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:41
    Tool: tsc | Category: type_error

[AUTO-400] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:55
    Tool: tsc | Category: type_error

[AUTO-401] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:56
    Tool: tsc | Category: type_error

[AUTO-402] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:59
    Tool: tsc | Category: type_error

[AUTO-403] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:69
    Tool: tsc | Category: type_error

[AUTO-404] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:70
    Tool: tsc | Category: type_error

[AUTO-405] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:71
    Tool: tsc | Category: type_error

[AUTO-406] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:72
    Tool: tsc | Category: type_error

[AUTO-407] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:75
    Tool: tsc | Category: type_error

[AUTO-408] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:75
    Tool: tsc | Category: type_error

[AUTO-409] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:78
    Tool: tsc | Category: type_error

[AUTO-410] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:79
    Tool: tsc | Category: type_error

[AUTO-411] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:80
    Tool: tsc | Category: type_error

[AUTO-412] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:82
    Tool: tsc | Category: type_error

[AUTO-413] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:83
    Tool: tsc | Category: type_error

[AUTO-414] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:84
    Tool: tsc | Category: type_error

[AUTO-415] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/Layout.tsx:85
    Tool: tsc | Category: type_error

[AUTO-416] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/SearchBar.tsx:5
    Tool: tsc | Category: type_error

[AUTO-417] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:51
    Tool: tsc | Category: type_error

[AUTO-418] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/SearchBar.tsx:51
    Tool: tsc | Category: type_error

[AUTO-419] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:52
    Tool: tsc | Category: type_error

[AUTO-420] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:53
    Tool: tsc | Category: type_error

[AUTO-421] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:55
    Tool: tsc | Category: type_error

[AUTO-422] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:56
    Tool: tsc | Category: type_error

[AUTO-423] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:61
    Tool: tsc | Category: type_error

[AUTO-424] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:62
    Tool: tsc | Category: type_error

[AUTO-425] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:66
    Tool: tsc | Category: type_error

[AUTO-426] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:71
    Tool: tsc | Category: type_error

[AUTO-427] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:74
    Tool: tsc | Category: type_error

[AUTO-428] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:75
    Tool: tsc | Category: type_error

[AUTO-429] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:80
    Tool: tsc | Category: type_error

[AUTO-430] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:81
    Tool: tsc | Category: type_error

[AUTO-431] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:85
    Tool: tsc | Category: type_error

[AUTO-432] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:90
    Tool: tsc | Category: type_error

[AUTO-433] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:93
    Tool: tsc | Category: type_error

[AUTO-434] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:94
    Tool: tsc | Category: type_error

[AUTO-435] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:100
    Tool: tsc | Category: type_error

[AUTO-436] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:101
    Tool: tsc | Category: type_error

[AUTO-437] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:106
    Tool: tsc | Category: type_error

[AUTO-438] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:114
    Tool: tsc | Category: type_error

[AUTO-439] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:119
    Tool: tsc | Category: type_error

[AUTO-440] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:121
    Tool: tsc | Category: type_error

[AUTO-441] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:123
    Tool: tsc | Category: type_error

[AUTO-442] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:124
    Tool: tsc | Category: type_error

[AUTO-443] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:130
    Tool: tsc | Category: type_error

[AUTO-444] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:136
    Tool: tsc | Category: type_error

[AUTO-445] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:138
    Tool: tsc | Category: type_error

[AUTO-446] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:140
    Tool: tsc | Category: type_error

[AUTO-447] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:141
    Tool: tsc | Category: type_error

[AUTO-448] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:142
    Tool: tsc | Category: type_error

[AUTO-449] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:145
    Tool: tsc | Category: type_error

[AUTO-450] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:146
    Tool: tsc | Category: type_error

[AUTO-451] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:147
    Tool: tsc | Category: type_error

[AUTO-452] Parameter 'e' implicitly has an 'any' type.
    File: src/components/SearchBar.tsx:150
    Tool: tsc | Category: type_error

[AUTO-453] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:153
    Tool: tsc | Category: type_error

[AUTO-454] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:155
    Tool: tsc | Category: type_error

[AUTO-455] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:156
    Tool: tsc | Category: type_error

[AUTO-456] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:157
    Tool: tsc | Category: type_error

[AUTO-457] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:158
    Tool: tsc | Category: type_error

[AUTO-458] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/SearchBar.tsx:159
    Tool: tsc | Category: type_error

[AUTO-459] Cannot find module 'react' or its corresponding type declarations.
    File: src/components/StatusUpdateModal.tsx:5
    Tool: tsc | Category: type_error

[AUTO-460] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:83
    Tool: tsc | Category: type_error

[AUTO-461] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/components/StatusUpdateModal.tsx:83
    Tool: tsc | Category: type_error

[AUTO-462] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:85
    Tool: tsc | Category: type_error

[AUTO-463] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:91
    Tool: tsc | Category: type_error

[AUTO-464] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:92
    Tool: tsc | Category: type_error

[AUTO-465] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:94
    Tool: tsc | Category: type_error

[AUTO-466] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:95
    Tool: tsc | Category: type_error

[AUTO-467] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:97
    Tool: tsc | Category: type_error

[AUTO-468] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:98
    Tool: tsc | Category: type_error

[AUTO-469] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:100
    Tool: tsc | Category: type_error

[AUTO-470] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:101
    Tool: tsc | Category: type_error

[AUTO-471] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:104
    Tool: tsc | Category: type_error

[AUTO-472] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:105
    Tool: tsc | Category: type_error

[AUTO-473] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:107
    Tool: tsc | Category: type_error

[AUTO-474] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:109
    Tool: tsc | Category: type_error

[AUTO-475] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:112
    Tool: tsc | Category: type_error

[AUTO-476] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:114
    Tool: tsc | Category: type_error

[AUTO-477] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:115
    Tool: tsc | Category: type_error

[AUTO-478] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:120
    Tool: tsc | Category: type_error

[AUTO-479] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:121
    Tool: tsc | Category: type_error

[AUTO-480] Parameter 'e' implicitly has an 'any' type.
    File: src/components/StatusUpdateModal.tsx:124
    Tool: tsc | Category: type_error

[AUTO-481] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:129
    Tool: tsc | Category: type_error

[AUTO-482] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:131
    Tool: tsc | Category: type_error

[AUTO-483] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:133
    Tool: tsc | Category: type_error

[AUTO-484] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:134
    Tool: tsc | Category: type_error

[AUTO-485] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:138
    Tool: tsc | Category: type_error

[AUTO-486] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:139
    Tool: tsc | Category: type_error

[AUTO-487] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:141
    Tool: tsc | Category: type_error

[AUTO-488] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:147
    Tool: tsc | Category: type_error

[AUTO-489] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:153
    Tool: tsc | Category: type_error

[AUTO-490] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:155
    Tool: tsc | Category: type_error

[AUTO-491] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:156
    Tool: tsc | Category: type_error

[AUTO-492] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:160
    Tool: tsc | Category: type_error

[AUTO-493] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:161
    Tool: tsc | Category: type_error

[AUTO-494] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:166
    Tool: tsc | Category: type_error

[AUTO-495] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:167
    Tool: tsc | Category: type_error

[AUTO-496] Parameter 'e' implicitly has an 'any' type.
    File: src/components/StatusUpdateModal.tsx:170
    Tool: tsc | Category: type_error

[AUTO-497] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:177
    Tool: tsc | Category: type_error

[AUTO-498] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:179
    Tool: tsc | Category: type_error

[AUTO-499] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:180
    Tool: tsc | Category: type_error

[AUTO-500] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:184
    Tool: tsc | Category: type_error

[AUTO-501] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:185
    Tool: tsc | Category: type_error

[AUTO-502] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:187
    Tool: tsc | Category: type_error

[AUTO-503] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:188
    Tool: tsc | Category: type_error

[AUTO-504] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:192
    Tool: tsc | Category: type_error

[AUTO-505] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:193
    Tool: tsc | Category: type_error

[AUTO-506] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:200
    Tool: tsc | Category: type_error

[AUTO-507] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:201
    Tool: tsc | Category: type_error

[AUTO-508] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:210
    Tool: tsc | Category: type_error

[AUTO-509] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:216
    Tool: tsc | Category: type_error

[AUTO-510] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:224
    Tool: tsc | Category: type_error

[AUTO-511] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:229
    Tool: tsc | Category: type_error

[AUTO-512] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:235
    Tool: tsc | Category: type_error

[AUTO-513] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:236
    Tool: tsc | Category: type_error

[AUTO-514] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:237
    Tool: tsc | Category: type_error

[AUTO-515] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:238
    Tool: tsc | Category: type_error

[AUTO-516] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:239
    Tool: tsc | Category: type_error

[AUTO-517] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/components/StatusUpdateModal.tsx:240
    Tool: tsc | Category: type_error

[AUTO-518] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/hooks/useApplications.ts:7
    Tool: tsc | Category: type_error

[AUTO-519] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:129
    Tool: tsc | Category: type_error

[AUTO-520] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:146
    Tool: tsc | Category: type_error

[AUTO-521] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:146
    Tool: tsc | Category: type_error

[AUTO-522] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:147
    Tool: tsc | Category: type_error

[AUTO-523] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:153
    Tool: tsc | Category: type_error

[AUTO-524] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:170
    Tool: tsc | Category: type_error

[AUTO-525] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:170
    Tool: tsc | Category: type_error

[AUTO-526] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:172
    Tool: tsc | Category: type_error

[AUTO-527] Binding element 'request' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:172
    Tool: tsc | Category: type_error

[AUTO-528] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-529] Binding element 'applicationId' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-530] Parameter 'context' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:194
    Tool: tsc | Category: type_error

[AUTO-531] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:204
    Tool: tsc | Category: type_error

[AUTO-532] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useApplications.ts:226
    Tool: tsc | Category: type_error

[AUTO-533] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/hooks/useJobs.ts:7
    Tool: tsc | Category: type_error

[AUTO-534] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:124
    Tool: tsc | Category: type_error

[AUTO-535] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:142
    Tool: tsc | Category: type_error

[AUTO-536] Parameter 'data' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:157
    Tool: tsc | Category: type_error

[AUTO-537] Parameter 'request' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:157
    Tool: tsc | Category: type_error

[AUTO-538] Parameter 'error' implicitly has an 'any' type.
    File: src/hooks/useJobs.ts:161
    Tool: tsc | Category: type_error

[AUTO-539] Cannot find module 'react' or its corresponding type declarations.
    File: src/main.tsx:1
    Tool: tsc | Category: type_error

[AUTO-540] Cannot find module 'react-dom/client' or its corresponding type declarations.
    File: src/main.tsx:2
    Tool: tsc | Category: type_error

[AUTO-541] Cannot find module '@tanstack/react-query' or its corresponding type declarations.
    File: src/main.tsx:3
    Tool: tsc | Category: type_error

[AUTO-542] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/main.tsx:19
    Tool: tsc | Category: type_error

[AUTO-543] Cannot find module 'react' or its corresponding type declarations.
    File: src/pages/ApplicationsPage.tsx:5
    Tool: tsc | Category: type_error

[AUTO-544] Cannot find name 'Application'.
    File: src/pages/ApplicationsPage.tsx:50
    Tool: tsc | Category: type_error

[AUTO-545] Cannot find name 'Application'.
    File: src/pages/ApplicationsPage.tsx:61
    Tool: tsc | Category: type_error

[AUTO-546] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-547] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/ApplicationsPage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-548] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:83
    Tool: tsc | Category: type_error

[AUTO-549] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:85
    Tool: tsc | Category: type_error

[AUTO-550] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:86
    Tool: tsc | Category: type_error

[AUTO-551] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:88
    Tool: tsc | Category: type_error

[AUTO-552] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:89
    Tool: tsc | Category: type_error

[AUTO-553] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:91
    Tool: tsc | Category: type_error

[AUTO-554] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:92
    Tool: tsc | Category: type_error

[AUTO-555] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-556] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:98
    Tool: tsc | Category: type_error

[AUTO-557] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:102
    Tool: tsc | Category: type_error

[AUTO-558] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:103
    Tool: tsc | Category: type_error

[AUTO-559] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:104
    Tool: tsc | Category: type_error

[AUTO-560] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:106
    Tool: tsc | Category: type_error

[AUTO-561] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:108
    Tool: tsc | Category: type_error

[AUTO-562] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:113
    Tool: tsc | Category: type_error

[AUTO-563] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:114
    Tool: tsc | Category: type_error

[AUTO-564] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:120
    Tool: tsc | Category: type_error

[AUTO-565] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:128
    Tool: tsc | Category: type_error

[AUTO-566] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:129
    Tool: tsc | Category: type_error

[AUTO-567] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:135
    Tool: tsc | Category: type_error

[AUTO-568] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:146
    Tool: tsc | Category: type_error

[AUTO-569] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:147
    Tool: tsc | Category: type_error

[AUTO-570] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:153
    Tool: tsc | Category: type_error

[AUTO-571] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:161
    Tool: tsc | Category: type_error

[AUTO-572] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:162
    Tool: tsc | Category: type_error

[AUTO-573] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:168
    Tool: tsc | Category: type_error

[AUTO-574] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:172
    Tool: tsc | Category: type_error

[AUTO-575] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:176
    Tool: tsc | Category: type_error

[AUTO-576] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:177
    Tool: tsc | Category: type_error

[AUTO-577] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:178
    Tool: tsc | Category: type_error

[AUTO-578] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:183
    Tool: tsc | Category: type_error

[AUTO-579] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:184
    Tool: tsc | Category: type_error

[AUTO-580] Parameter 'e' implicitly has an 'any' type.
    File: src/pages/ApplicationsPage.tsx:187
    Tool: tsc | Category: type_error

[AUTO-581] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:193
    Tool: tsc | Category: type_error

[AUTO-582] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:195
    Tool: tsc | Category: type_error

[AUTO-583] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:197
    Tool: tsc | Category: type_error

[AUTO-584] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:198
    Tool: tsc | Category: type_error

[AUTO-585] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:199
    Tool: tsc | Category: type_error

[AUTO-586] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:203
    Tool: tsc | Category: type_error

[AUTO-587] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:204
    Tool: tsc | Category: type_error

[AUTO-588] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:210
    Tool: tsc | Category: type_error

[AUTO-589] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:216
    Tool: tsc | Category: type_error

[AUTO-590] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:217
    Tool: tsc | Category: type_error

[AUTO-591] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:219
    Tool: tsc | Category: type_error

[AUTO-592] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:220
    Tool: tsc | Category: type_error

[AUTO-593] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:222
    Tool: tsc | Category: type_error

[AUTO-594] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:223
    Tool: tsc | Category: type_error

[AUTO-595] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:228
    Tool: tsc | Category: type_error

[AUTO-596] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:229
    Tool: tsc | Category: type_error

[AUTO-597] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:259
    Tool: tsc | Category: type_error

[AUTO-598] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:260
    Tool: tsc | Category: type_error

[AUTO-599] Cannot find namespace 'React'.
    File: src/pages/ApplicationsPage.tsx:268
    Tool: tsc | Category: type_error

[AUTO-600] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:281
    Tool: tsc | Category: type_error

[AUTO-601] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:282
    Tool: tsc | Category: type_error

[AUTO-602] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:283
    Tool: tsc | Category: type_error

[AUTO-603] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:283
    Tool: tsc | Category: type_error

[AUTO-604] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:284
    Tool: tsc | Category: type_error

[AUTO-605] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:285
    Tool: tsc | Category: type_error

[AUTO-606] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:285
    Tool: tsc | Category: type_error

[AUTO-607] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:286
    Tool: tsc | Category: type_error

[AUTO-608] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:286
    Tool: tsc | Category: type_error

[AUTO-609] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:287
    Tool: tsc | Category: type_error

[AUTO-610] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:308
    Tool: tsc | Category: type_error

[AUTO-611] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:310
    Tool: tsc | Category: type_error

[AUTO-612] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:316
    Tool: tsc | Category: type_error

[AUTO-613] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:317
    Tool: tsc | Category: type_error

[AUTO-614] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:319
    Tool: tsc | Category: type_error

[AUTO-615] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:320
    Tool: tsc | Category: type_error

[AUTO-616] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:326
    Tool: tsc | Category: type_error

[AUTO-617] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:332
    Tool: tsc | Category: type_error

[AUTO-618] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:333
    Tool: tsc | Category: type_error

[AUTO-619] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:336
    Tool: tsc | Category: type_error

[AUTO-620] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:338
    Tool: tsc | Category: type_error

[AUTO-621] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:339
    Tool: tsc | Category: type_error

[AUTO-622] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:341
    Tool: tsc | Category: type_error

[AUTO-623] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:344
    Tool: tsc | Category: type_error

[AUTO-624] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:345
    Tool: tsc | Category: type_error

[AUTO-625] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:352
    Tool: tsc | Category: type_error

[AUTO-626] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:353
    Tool: tsc | Category: type_error

[AUTO-627] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:361
    Tool: tsc | Category: type_error

[AUTO-628] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:367
    Tool: tsc | Category: type_error

[AUTO-629] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:375
    Tool: tsc | Category: type_error

[AUTO-630] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:380
    Tool: tsc | Category: type_error

[AUTO-631] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:386
    Tool: tsc | Category: type_error

[AUTO-632] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:387
    Tool: tsc | Category: type_error

[AUTO-633] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:388
    Tool: tsc | Category: type_error

[AUTO-634] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:389
    Tool: tsc | Category: type_error

[AUTO-635] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/ApplicationsPage.tsx:390
    Tool: tsc | Category: type_error

[AUTO-636] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:3
    Tool: tsc | Category: type_error

[AUTO-637] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/DashboardPage.tsx:3
    Tool: tsc | Category: type_error

[AUTO-638] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:4
    Tool: tsc | Category: type_error

[AUTO-639] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:4
    Tool: tsc | Category: type_error

[AUTO-640] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:5
    Tool: tsc | Category: type_error

[AUTO-641] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:7
    Tool: tsc | Category: type_error

[AUTO-642] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:8
    Tool: tsc | Category: type_error

[AUTO-643] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:10
    Tool: tsc | Category: type_error

[AUTO-644] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:11
    Tool: tsc | Category: type_error

[AUTO-645] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:11
    Tool: tsc | Category: type_error

[AUTO-646] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:12
    Tool: tsc | Category: type_error

[AUTO-647] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:12
    Tool: tsc | Category: type_error

[AUTO-648] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:13
    Tool: tsc | Category: type_error

[AUTO-649] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:14
    Tool: tsc | Category: type_error

[AUTO-650] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:15
    Tool: tsc | Category: type_error

[AUTO-651] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:15
    Tool: tsc | Category: type_error

[AUTO-652] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:16
    Tool: tsc | Category: type_error

[AUTO-653] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:16
    Tool: tsc | Category: type_error

[AUTO-654] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:17
    Tool: tsc | Category: type_error

[AUTO-655] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:18
    Tool: tsc | Category: type_error

[AUTO-656] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:19
    Tool: tsc | Category: type_error

[AUTO-657] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:19
    Tool: tsc | Category: type_error

[AUTO-658] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:20
    Tool: tsc | Category: type_error

[AUTO-659] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:20
    Tool: tsc | Category: type_error

[AUTO-660] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:21
    Tool: tsc | Category: type_error

[AUTO-661] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:22
    Tool: tsc | Category: type_error

[AUTO-662] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:23
    Tool: tsc | Category: type_error

[AUTO-663] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:23
    Tool: tsc | Category: type_error

[AUTO-664] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:24
    Tool: tsc | Category: type_error

[AUTO-665] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:24
    Tool: tsc | Category: type_error

[AUTO-666] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:25
    Tool: tsc | Category: type_error

[AUTO-667] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:26
    Tool: tsc | Category: type_error

[AUTO-668] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/DashboardPage.tsx:27
    Tool: tsc | Category: type_error

[AUTO-669] Cannot find module 'react-router-dom' or its corresponding type declarations.
    File: src/pages/HomePage.tsx:1
    Tool: tsc | Category: type_error

[AUTO-670] Cannot find module 'lucide-react' or its corresponding type declarations.
    File: src/pages/HomePage.tsx:2
    Tool: tsc | Category: type_error

[AUTO-671] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:29
    Tool: tsc | Category: type_error

[AUTO-672] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/HomePage.tsx:29
    Tool: tsc | Category: type_error

[AUTO-673] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:31
    Tool: tsc | Category: type_error

[AUTO-674] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:32
    Tool: tsc | Category: type_error

[AUTO-675] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:34
    Tool: tsc | Category: type_error

[AUTO-676] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:35
    Tool: tsc | Category: type_error

[AUTO-677] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:38
    Tool: tsc | Category: type_error

[AUTO-678] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:39
    Tool: tsc | Category: type_error

[AUTO-679] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:52
    Tool: tsc | Category: type_error

[AUTO-680] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:53
    Tool: tsc | Category: type_error

[AUTO-681] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:56
    Tool: tsc | Category: type_error

[AUTO-682] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:57
    Tool: tsc | Category: type_error

[AUTO-683] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:61
    Tool: tsc | Category: type_error

[AUTO-684] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:65
    Tool: tsc | Category: type_error

[AUTO-685] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:67
    Tool: tsc | Category: type_error

[AUTO-686] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:68
    Tool: tsc | Category: type_error

[AUTO-687] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:70
    Tool: tsc | Category: type_error

[AUTO-688] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:71
    Tool: tsc | Category: type_error

[AUTO-689] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:73
    Tool: tsc | Category: type_error

[AUTO-690] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:74
    Tool: tsc | Category: type_error

[AUTO-691] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:77
    Tool: tsc | Category: type_error

[AUTO-692] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:78
    Tool: tsc | Category: type_error

[AUTO-693] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:81
    Tool: tsc | Category: type_error

[AUTO-694] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:82
    Tool: tsc | Category: type_error

[AUTO-695] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:83
    Tool: tsc | Category: type_error

[AUTO-696] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:85
    Tool: tsc | Category: type_error

[AUTO-697] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:86
    Tool: tsc | Category: type_error

[AUTO-698] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:87
    Tool: tsc | Category: type_error

[AUTO-699] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:87
    Tool: tsc | Category: type_error

[AUTO-700] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:88
    Tool: tsc | Category: type_error

[AUTO-701] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:89
    Tool: tsc | Category: type_error

[AUTO-702] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:91
    Tool: tsc | Category: type_error

[AUTO-703] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:92
    Tool: tsc | Category: type_error

[AUTO-704] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:93
    Tool: tsc | Category: type_error

[AUTO-705] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/HomePage.tsx:94
    Tool: tsc | Category: type_error

[AUTO-706] Cannot find module 'react' or its corresponding type declarations.
    File: src/pages/JobsPage.tsx:7
    Tool: tsc | Category: type_error

[AUTO-707] Parameter 'job' implicitly has an 'any' type.
    File: src/pages/JobsPage.tsx:48
    Tool: tsc | Category: type_error

[AUTO-708] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-709] This JSX tag requires the module path 'react/jsx-runtime' to exist, but none could be found. Make sure you have types for the appropriate package installed.
    File: src/pages/JobsPage.tsx:96
    Tool: tsc | Category: type_error

[AUTO-710] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:98
    Tool: tsc | Category: type_error

[AUTO-711] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:99
    Tool: tsc | Category: type_error

[AUTO-712] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:101
    Tool: tsc | Category: type_error

[AUTO-713] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:102
    Tool: tsc | Category: type_error

[AUTO-714] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:104
    Tool: tsc | Category: type_error

[AUTO-715] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:105
    Tool: tsc | Category: type_error

[AUTO-716] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:108
    Tool: tsc | Category: type_error

[AUTO-717] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:113
    Tool: tsc | Category: type_error

[AUTO-718] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:117
    Tool: tsc | Category: type_error

[AUTO-719] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:119
    Tool: tsc | Category: type_error

[AUTO-720] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:120
    Tool: tsc | Category: type_error

[AUTO-721] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:121
    Tool: tsc | Category: type_error

[AUTO-722] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:123
    Tool: tsc | Category: type_error

[AUTO-723] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:125
    Tool: tsc | Category: type_error

[AUTO-724] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:128
    Tool: tsc | Category: type_error

[AUTO-725] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:131
    Tool: tsc | Category: type_error

[AUTO-726] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:133
    Tool: tsc | Category: type_error

[AUTO-727] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:135
    Tool: tsc | Category: type_error

[AUTO-728] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:142
    Tool: tsc | Category: type_error

[AUTO-729] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:152
    Tool: tsc | Category: type_error

[AUTO-730] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:157
    Tool: tsc | Category: type_error

[AUTO-731] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:158
    Tool: tsc | Category: type_error

[AUTO-732] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:164
    Tool: tsc | Category: type_error

[AUTO-733] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:170
    Tool: tsc | Category: type_error

[AUTO-734] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:171
    Tool: tsc | Category: type_error

[AUTO-735] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:173
    Tool: tsc | Category: type_error

[AUTO-736] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:174
    Tool: tsc | Category: type_error

[AUTO-737] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:177
    Tool: tsc | Category: type_error

[AUTO-738] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:178
    Tool: tsc | Category: type_error

[AUTO-739] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:179
    Tool: tsc | Category: type_error

[AUTO-740] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:181
    Tool: tsc | Category: type_error

[AUTO-741] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:182
    Tool: tsc | Category: type_error

[AUTO-742] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:184
    Tool: tsc | Category: type_error

[AUTO-743] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:185
    Tool: tsc | Category: type_error

[AUTO-744] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:187
    Tool: tsc | Category: type_error

[AUTO-745] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:188
    Tool: tsc | Category: type_error

[AUTO-746] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:189
    Tool: tsc | Category: type_error

[AUTO-747] JSX element implicitly has type 'any' because no interface 'JSX.IntrinsicElements' exists.
    File: src/pages/JobsPage.tsx:191
    Tool: tsc | Category: type_error


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

[AUTO-748] TODO comment found
    File: backend/src/api/applications.py:121
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-749] TODO comment found
    File: backend/src/api/applications.py:168
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-750] TODO comment found
    File: backend/src/api/applications.py:200
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-751] TODO comment found
    File: backend/src/api/applications.py:228
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-752] TODO comment found
    File: backend/src/api/applications.py:264
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-753] TODO comment found
    File: backend/src/api/applications.py:305
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-754] TODO comment found
    File: backend/src/api/applications.py:343
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-755] TODO comment found
    File: backend/src/api/applications.py:375
    Tool: grep | Category: code_quality
    Details: # TODO: Replace with actual user from auth

[AUTO-756] TODO comment found
    File: frontend/src/api/client.ts:24
    Tool: grep | Category: code_quality
    Details: // TODO: Add authentication token when auth is implemented

[AUTO-757] TODO comment found
    File: frontend/src/api/client.ts:54
    Tool: grep | Category: code_quality
    Details: // TODO: Redirect to login when auth is implemented

💡 RECOMMENDATIONS
--------------------------------------------------------------------------------
⚠️  Fix linting issues to maintain code quality

================================================================================