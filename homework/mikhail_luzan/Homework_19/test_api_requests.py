import requests
import pytest


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


obj1 = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

obj2 = {
    "name": "Apple MacBook Air",
    "data": {
        "year": 2020,
        "price": 1999.99,
        "CPU model": "Apple M1",
        "Hard disk size": "2 TB"
    }
}

obj3 = {
    "name": "Apple MacBook Pro 14",
    "data": {
        "year": 2021,
        "price": 2499.99,
        "CPU model": "Apple M1 Max",
        "Hard disk size": "8 TB"
    }
}


@pytest.mark.parametrize("body", [obj1, obj2, obj3])
def test_post(session_text, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=body,
        headers=headers
    )
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'createdAt' in resp, 'The "createdAt" key is NOT created'


@pytest.mark.critical
def test_put(new_obj_id):
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_obj_id}',
        json=body,
        headers=headers
    )
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'color' in resp['data'], 'The "color" key is NOT added'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'


@pytest.mark.medium
def test_patch(new_obj_id):
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_obj_id}',
        json=body,
        headers=headers
    )
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert " (Updated Name)" in resp['name'], 'The " (Updated Name)" is NOT added / is partially added'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'


def test_delete(new_obj_id):
    response = requests.delete(
        f'https://api.restful-api.dev/objects/{new_obj_id}'
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {new_obj_id} has been deleted.', 'Message is incorrect'
