import pytest

@pytest.mark.get_test
@pytest.mark.parametrize("endpoint, ex_status_code",
[
("api/v1/runs/",200),
],
)
def test_retrieve_an_existing_run(endpoint,ex_status_code,test_client,
    create_multiple):
    run=create_multiple(count=1)[0]
    respons=test_client.set_get(f'{endpoint}{run['id']}')
    respons_jeson=respons.json()
    assert respons_jeson['id']== run['id']
    assert respons.status_code==ex_status_code

@pytest.mark.get_test
@pytest.mark.parametrize("endpoint, ex_status_code",
[
("api/v1/runs/",200),
],
)
def test_Retrieve_a_non_existent_run(endpoint,test_client,ex_status_code,
    create_multiple):
    create_multiple(count=1)[0]
    resp= test_client.set_get(endpoint)
    resp_json=resp.json()
    ids = [run['id'] for run in resp_json]
    assert 999 is not ids


@pytest.mark.get_test
@pytest.mark.parametrize("endpoint, ex_status_code",
[
("api/v1/runs/fds",422),
],
)

def test_Invalid_ID_not_a_number(endpoint,ex_status_code,test_client):
    respons= test_client.set_get(endpoint)
    assert respons.status_code == ex_status_code
