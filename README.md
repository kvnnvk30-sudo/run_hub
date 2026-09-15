# 🚀 Test Run Hub

A simple, effective full-stack service for logging and monitoring automated test execution results. This project was built as a hands-on step for a QA Automation Engineer moving into web application and micro-service development.

---

## 🛠 Tech Stack

| Layer | Tools |
|---|---|
| **Backend** | Python 3, FastAPI, Uvicorn, Pydantic, SQLite / SQLAlchemy |
| **Frontend** | HTML5, Tailwind CSS (via CDN), Vanilla JavaScript (Fetch API) |
| **Testing** | Pytest, Requests, Playwright Python |
| **Infra** | Docker, Docker Compose |

---

## 📁 Project Structure

```text
test-run-hub/
├── backend/
│   ├── Dockerfile
│   ├── main.py            # FastAPI server, Pydantic schemas, CORS, and endpoints
│   └── requirements.txt   # Python dependencies
│
├── frontend/
│   ├── Dockerfile
│   └── index.html         # UI (HTML, Tailwind CSS, JS Fetch API)
│
├── tests/
│   ├── test_api/           # REST API tests (Pytest + Requests)
│   ├── test_ui/             # UI tests (Playwright Python)
│   ├── client.py
│   ├── conftest.py
│   └── url.py
│
├── docker-compose.yml
└── README.md
```

---

## ✨ Features

- 📋 Log automated test runs with title, suite, status, and duration
- 🔍 Browse and inspect run history in a live dashboard
- ⚡ Async REST API built on FastAPI with auto-generated OpenAPI docs
- ✅ Full test coverage — both API and UI layers

---

## 🚀 Getting Started

### Option 1 — Docker (recommended)

```bash
git clone https://github.com/kvnnvk30-sudo/run_hub.git test-run-hub
cd test-run-hub
docker compose up --build
```

- Frontend: **http://localhost:5500**
- Backend API docs (Swagger UI): **http://localhost:8000/docs**

### Option 2 — Run locally without Docker

```bash
# 1. Clone the repository
git clone https://github.com/kvnnvk30-sudo/run_hub.git test-run-hub
cd test-run-hub

# 2. Install backend dependencies
pip install -r backend/requirements.txt

# 3. Run the server
uvicorn backend.main:apps --reload --app-dir backend

# 4. Open the frontend
# Simply open frontend/index.html in your browser
```

---

## 🔌 API Quick Reference

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/runs` | List all test runs |
| GET | `/api/v1/runs/{run_id}` | Get a single test run |
| POST | `/api/v1/runs` | Create a new test run |

### Try it from the terminal

```bash
# List all runs
curl http://localhost:8000/api/v1/runs

# Pretty-print with jq
curl -s http://localhost:8000/api/v1/runs | jq

# Create a run
curl -X POST http://localhost:8000/api/v1/runs \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Login smoke test",
    "suite_name": "auth-suite",
    "status": "PASSED",
    "duration_seconds": 12.5
  }'

# Get a single run
curl http://localhost:8000/api/v1/runs/1
```

---

## 🧪 Running Tests

```bash
cd tests
pytest test_api/
pytest test_ui/
```

---

## 📄 License

This project is open-source and available under the MIT License.