import pytest
import requests


@pytest.fixture(scope='session')
def session_text():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def new_obj_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    obj_id = response.json()['id']
    print('\nbefore test')
    yield obj_id
    print('\nafter test')
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
