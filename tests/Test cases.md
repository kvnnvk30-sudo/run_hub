# Test Run Hub — Test Cases

## API Test Cases (`/api/v1/runs`)

### GET /api/v1/runs

| ID | Name | Preconditions | Steps | Expected Result |
|----|------|----------------|-------|-------------------|
| API-01 | Get an empty list | No records in DB | GET `/api/v1/runs` | 200 OK, body `[]` |
| API-02 | Get a list of runs | 2+ records exist in DB | GET `/api/v1/runs` | 200 OK, array of objects with fields `id, title, suite_name, status, duration_seconds, created_at` |
| API-03 | Sort by date | Records with different `created_at` exist | GET `/api/v1/runs` | Records sorted by `created_at` descending (newest first) |

### GET /api/v1/runs/{run_id}

| ID | Name | Preconditions | Steps | Expected Result |
|----|------|----------------|-------|-------------------|
| API-04 | Retrieve an existing run | Run with id=1 exists | GET `/api/v1/runs/1` | 200 OK, object with correct data |
| API-05 | Retrieve a non-existent run | No run with id=9999 | GET `/api/v1/runs/9999` | 404 Not Found, `{"detail": "Test run not found"}` |
| API-06 | Invalid id (not a number) | — | GET `/api/v1/runs/abc` | 422 Unprocessable Content |

### POST /api/v1/runs

| ID | Name | Input Data | Expected Result |
|----|------|-------------|-------------------|
| API-07 | Successful run creation | `{title: "Login test", suite_name: "auth-suite", status: "PASSED", duration_seconds: 12.5}` | 201 Created, body contains the created object with `id` and `created_at` |
| API-08 | Missing required field `title` | `{suite_name: "auth-suite", status: "PASSED", duration_seconds: 12.5}` | 422 Unprocessable Content |
| API-09 | Missing required field `suite_name` | `{title: "Login test", status: "PASSED", duration_seconds: 12.5}` | 422 Unprocessable Content |
| API-10 | `title` shorter than minimum length (< 4 chars) | `{title: "ab", ...}` | 422 Unprocessable Content |
| API-11 | `title` longer than maximum length (> 100 chars) | `{title: "a"*101, ...}` | 422 Unprocessable Content |
| API-12 | `suite_name` shorter than minimum length (< 4 chars) | `{suite_name: "ab", ...}` | 422 Unprocessable Content |
| API-13 | Invalid `status` value | `{status: "passed", ...}` (lowercase) | 422 Unprocessable Content |
| API-14 | Invalid `status` value (arbitrary string) | `{status: "DONE", ...}` | 422 Unprocessable Content |
| API-15 | `duration_seconds` = 0 | `{duration_seconds: 0, ...}` | 422 Unprocessable Content (must be `> 0`) |
| API-16 | `duration_seconds` negative | `{duration_seconds: -5, ...}` | 422 Unprocessable Content |
| API-17 | `duration_seconds` as a string | `{duration_seconds: "twelve", ...}` | 422 Unprocessable Content |
| API-18 | Empty request body | `{}` | 422 Unprocessable Content |
| API-19 | Extra/unknown fields in body | `{title: "...", suite_name: "...", status: "PASSED", duration_seconds: 5, extra_field: "x"}` | 201 Created, extra field is ignored (verify behavior — Pydantic drops it by default) |
| API-20 | Verify `created_at` type in response | Valid request | 201 Created, `created_at` is a valid ISO date |

### CORS

| ID | Name | Steps | Expected Result |
|----|------|-------|-------------------|
| API-21 | Preflight request from the frontend | OPTIONS `/api/v1/runs` with frontend Origin | 200 OK, `Access-Control-Allow-Origin` header present |
| API-22 | POST from a different origin | POST with an Origin different from the backend | Request succeeds (allow_origins=["*"]) |

---

## UI Test Cases (`index.html`)

### "New run" Form

| ID | Name | Steps | Expected Result |
|----|------|-------|-------------------|
| UI-01 | Successfully add a run | Fill in all fields with valid values → click "Add run" | Form clears, a new card appears in "Run history" |
| UI-02 | Submit form with empty "Title" field | Leave "Title" empty → click "Add run" | Browser blocks submission (`required` attribute), default browser hint shown |
| UI-03 | "Title" shorter than 4 characters | Enter "ab" in Title → submit | Browser blocks submission (`minlength="4"`) |
| UI-04 | "Suite name" empty | Leave "Suite name" empty → submit | Browser blocks submission (`required`) |
| UI-05 | Status not selected | Leave "Status" select at empty value → submit | Browser blocks submission (`required`) |
| UI-06 | Duration not specified | Leave "Duration" field empty → submit | Browser blocks submission (`required`) |
| UI-07 | Duration = 0 or negative | Enter `0` or `-5` in Duration → submit | Browser blocks it (`min="0.01"`), or the server returns an error and "Error: please check the values you entered." is displayed |
| UI-08 | Server returned an error (invalid data reached the backend) | Submit data that the backend will reject | The `#form-error` block is shown with the text "Error: please check the values you entered." |
| UI-09 | Server unavailable on submit | Stop the backend → submit the form | `#form-error` is shown, the form is not cleared |
| UI-10 | Form clears after a successful submission | Successfully submit a run | All form fields return to their empty/default values |

### "Run History" List

| ID | Name | Steps | Expected Result |
|----|------|-------|-------------------|
| UI-11 | List loads when the page opens | Open `index.html` | The list loads and displays automatically without any user action |
| UI-12 | Empty list of runs | No records in DB → open the page | "Run history" section is empty, no errors |
| UI-13 | Server unavailable on load | Stop the backend → open/refresh the page | Message "Failed to load data. Is the server running?" is shown |
| UI-14 | PASSED status display | A run with status PASSED is in the list | Status badge is green, text "PASSED" |
| UI-15 | FAILED status display | A run with status FAILED is in the list | Status badge is red, text "FAILED" |
| UI-16 | SKIPPED status display | A run with status SKIPPED is in the list | Status badge is yellow/amber, text "SKIPPED" |
| UI-17 | Correctness of displayed data | Add a run with specific title/suite/duration | The card shows exactly this title, suite_name, duration_seconds, and creation date |
| UI-18 | List updates after adding | Add a new run | New card appears in the list without a manual page refresh |
| UI-19 | Date format | A run with a known `created_at` | Date is displayed in a readable local format (not a raw ISO string) |
| UI-20 | Several runs in a row | Add 3+ runs | All cards are displayed, order matches backend sorting (newest on top) |

### Cross-Browser / General Checks

| ID | Name | Steps | Expected Result |
|----|------|-------|-------------------|
| UI-21 | Open via `file://` | Open `index.html` directly by double-clicking | Request to the API is blocked by CORS/protocol — document as a known limitation |
| UI-22 | Form responsiveness | Shrink the browser window width | Form fields switch to a single column (`sm:grid-cols-2` → 1 column) |