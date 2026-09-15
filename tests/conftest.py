import sqlite3
import pytest
from tests.url import Url_api
from tests.client import TestClient
from tests.url import Url_ui


TEST_DB_PATH = "test_run_hub_test.db"


@pytest.fixture(autouse=True)
def clean_db():
    conn = sqlite3.connect(TEST_DB_PATH)
    conn.execute("DELETE FROM test_runs")
    conn.commit()
    conn.close()
    yield


@pytest.fixture(scope="session")
def base_url() -> str:
    return Url_api().set_Url_api("")


@pytest.fixture
def test_client(base_url) -> TestClient:
    client = TestClient(base_url)
    yield client
    client.session.close()


def _build_payload(title=None, suite_name=None, status=None, duration_seconds=None):
    return {
        "title": title if title is not None else "Test Run Title",
        "suite_name": suite_name if suite_name is not None else "Test Suite Name",
        "status": status if status is not None else "PASSED",
        "duration_seconds": duration_seconds if duration_seconds is not None else 1.0,
    }


@pytest.fixture
def create(test_client):
    def _create(**kwargs):
        payload = _build_payload(**kwargs)
        response = test_client.set_post("api/v1/runs", json=payload)
        assert response.status_code == 201
        return {"id": response.json()["id"], **payload}
    return _create


@pytest.fixture
def create_multiple(create):
    def _create_multiple(count=2, **kwargs):
        return [create(**kwargs) for _ in range(count)]
    return _create_multiple


@pytest.fixture
def url():
    return Url_ui().set_url_ui()


@pytest.fixture
def login_in_as(page, url):
    def _login(title, suite_name, duration_seconds=None, status="PASSED", before_submit=None):
        page.goto(url)
        page.fill("input[name='title']", title)
        page.fill("input[name='suite_name']", suite_name)
        if duration_seconds is not None:
            page.fill("input[name='duration_seconds']", str(duration_seconds))
        page.select_option('select[name="status"]', status)
        if before_submit:
            before_submit(page)
        page.click('button[type="submit"]')
        return page
    return _login