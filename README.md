# 🚀 Test Run Hub

A simple, effective full-stack service for logging and monitoring automated test execution results. This project was built as a hands-on step for a QA Automation Engineer moving into web application and micro-service development.

---

## 🛠 Tech Stack

| Layer | Tools |
|---|---|
| **Backend** | Python 3, FastAPI, Uvicorn, Pydantic, SQLite / SQLAlchemy |
| **Frontend** | HTML5, Tailwind CSS (via CDN), Vanilla JavaScript (Fetch API) |
| **Testing** | Pytest, Requests, Playwright Python |

---

## 📁 Project Structure

```text
test-run-hub/
├── backend/
│   ├── main.py            # FastAPI server, Pydantic schemas, CORS, and endpoints
│   └── requirements.txt   # Python dependencies
│
├── frontend/
│   └── index.html         # UI (HTML, Tailwind CSS, JS Fetch API)
│
├── tests/
│   ├── test_api.py        # REST API tests (Pytest + Requests)
│   └── test_ui.py         # UI tests (Playwright Python)
│
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

```bash
# 1. Clone the repository
git clone https://github.com/your-username/test-run-hub.git
cd test-run-hub

# 2. Install backend dependencies
pip install -r backend/requirements.txt

# 3. Run the server
uvicorn backend.main:apps --reload

# 4. Open the frontend
# Simply open frontend/index.html in your browser
```

The interactive API docs will be available at **http://127.0.0.1:8000/docs**.

---

## 🧪 Running Tests

```bash
# API tests
pytest tests/test_api.py

# UI tests
pytest tests/test_ui.py
```

---

## 📄 License

This project is open-source and available under the MIT License.