
import pytest


@pytest.mark.get_test
@pytest.mark.parametrize(
    "endpoint, expected_status_code",
    [
        ("api/v1/runs", 200),
    ],
)   
def test_get_an_empty_list(test_client, endpoint, expected_status_code):
    response = test_client.set_get(endpoint)
    assert response.json() == []
    assert response.status_code == expected_status_code


@pytest.mark.get_test
@pytest.mark.parametrize(
    "endpoint, expected_status_code",
    [
        ("api/v1/runs", 200),
    ],
)   
def test_get_a_list_of_runs(test_client, endpoint, create_multiple, expected_status_code):
    create_multiple(count=2)
    response_data = {
        "id", "title", "suite_name", "status", "duration_seconds", "created_at"
    }
    response = test_client.set_get(endpoint)
    assert response.status_code == expected_status_code
    response_json = response.json()
    assert len(response_json) > 0
    print(f"Total runs returned: {len(response_json)}")
    for run in response_json:
        assert response_data.issubset(run.keys())
        print(f"Run data: {run}")
    created_dates = [run["created_at"] for run in response_json]
    assert created_dates == sorted(created_dates, reverse=True)
 
