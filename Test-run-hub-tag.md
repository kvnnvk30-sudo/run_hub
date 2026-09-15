# Technical Architecture Document (TAD)
## Test Run Hub
```
cd backend
pip install -r requirements.txt
uvicorn main:apps --reload
```
---

## 1. System Overview

**Test Run Hub** is a lightweight full-stack micro-service designed for logging, managing, and inspecting automated test execution runs. Built specifically to bridge QA Automation engineering with backend and web application development, the system exposes a RESTful API and provides an interactive front-end user interface for monitoring test results in real time.

---

## 2. System Architecture

The system follows a classic **decoupled client-server architecture** with direct browser-to-API communication via asynchronous HTTP requests.

```
+-------------------------------------------------------+
|                       Frontend                         |
|   Single-Page Application (HTML5 + Tailwind CSS CDN)   |
|   Asynchronous Fetch API / JavaScript UI Handler        |
+---------------------------+---------------------------+
                            |
                 HTTP REST (JSON / CORS)
                            |
+---------------------------v---------------------------+
|                       Backend                           |
|   FastAPI Application Server (Uvicorn ASGI)             |
|   Pydantic Data Schemas & Validation Layer               |
|   SQLite Database (SQLAlchemy ORM Data Access)           |
+-------------------------------------------------------+
```

---

## 3. Core Components & Technology Stack

| Component | Technology / Tool | Purpose |
|---|---|---|
| **Language** | Python 3.10+ | Core application runtime and business logic layer |
| **Backend Framework** | FastAPI | High-performance, async web framework for REST API endpoints |
| **ASGI Server** | Uvicorn | Lightning-fast async server implementation running FastAPI |
| **Data Validation** | Pydantic v2 | Strict type checking, data serialization, and payload schema validation |
| **Persistence Layer** | SQLite3 / SQLAlchemy | Embedded relational database for test run history and status logging |
| **Frontend Interface** | HTML5, Tailwind CSS (CDN), Vanilla JS | Zero-build-step client dashboard utilizing native Fetch API for HTTP interaction |
| **Testing Framework** | Pytest & Playwright | Automated end-to-end UI and REST API test coverage suites |

---

## 4. REST API Specifications

The backend exposes RESTful endpoints with automatic OpenAPI (Swagger) documentation generated at `/docs`.

### 4.1 Endpoints Summary

| HTTP Method | Endpoint | Description | Request Body | Response |
|---|---|---|---|---|
| `GET` | `/api/v1/runs` | Retrieve all recorded test runs | N/A | `200 OK` (Array of `TestRun`) |
| `POST` | `/api/v1/runs` | Create a new test run entry | `TestRunCreate` (JSON) | `201 Created` (`TestRun` Object) |
| `GET` | `/api/v1/runs/{run_id}` | Get details of a specific test run | N/A | `200 OK` / `404 Not Found` |

### 4.2 Data Transfer Objects (DTO) Schema

```python
class TestRunCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    suite_name: str = Field(..., min_length=2, max_length=50)
    status: Literal["PASSED", "FAILED", "SKIPPED"]
    duration_seconds: float = Field(..., ge=0.0)


class TestRunResponse(TestRunCreate):
    id: int
    created_at: datetime
```

---

## 5. Security & Middleware Configuration

- **Cross-Origin Resource Sharing (CORS):** Configured via FastAPI `CORSMiddleware` to allow explicitly trusted local origins (e.g., `http://localhost:5500`, `http://127.0.0.1:8000`) during frontend-backend communication.
- **Data Input Sanitization:** Handled strictly by Pydantic models to prevent payload injection and type mismatches.

---

## 6. Quality Assurance & Testability Matrix

The architecture is purpose-built to facilitate automated QA validation:

- **API Automated Testing:** Tested using `pytest` and `requests` / `httpx` for verifying HTTP status codes, payload structures, and boundary checks.
- **UI Automated Testing:** Covered by `Playwright Python` for cross-browser interaction testing, DOM validation, form submissions, and async state updates.