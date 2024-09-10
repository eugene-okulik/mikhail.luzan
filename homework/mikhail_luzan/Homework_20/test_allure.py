import pytest
import requests
import allure


with allure.step('Create the 1st object for the "test_post()" function'):
    obj1 = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

with allure.step('Create the 2nd object for the "test_post()" function'):
    obj2 = {
        "name": "Apple MacBook Air",
        "data": {
            "year": 2020,
            "price": 1999.99,
            "CPU model": "Apple M1",
            "Hard disk size": "2 TB"
        }
    }

with allure.step('Create the 3rd object for the "test_post()" function'):
    obj3 = {
        "name": "Apple MacBook Pro 14",
        "data": {
            "year": 2021,
            "price": 2499.99,
            "CPU model": "Apple M1 Max",
            "Hard disk size": "8 TB"
        }
    }


@allure.story('Create objects')
@pytest.mark.parametrize("body", [obj1, obj2, obj3])
def test_post(session_text, body):
    with allure.step('Prepare test data'):
        headers = {'Content-Type': 'application/json'}
    with allure.step('Create data with prepared objects'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=body,
            headers=headers
        )
    with allure.step('Check the response code - 200 OK'):
        resp = response.json()
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check the "id" key in the response data'):
        assert 'id' in resp, 'The "id" key is NOT created'
    with allure.step('Check the "createdAt" key in the response data'):
        assert 'createdAt' in resp, 'The "createdAt" key is NOT created'


@allure.feature('CRUD')
@allure.story('PUT')
@allure.title('Complete object modification')
@pytest.mark.critical
def test_put(new_obj_id):
    with allure.step('Prepare test data'):
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
    with allure.step('Modify the created data'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{new_obj_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check the response code - 200 OK'):
        resp = response.json()
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check the "color" key in the response data'):
        assert 'color' in resp['data'], 'The "color" key is NOT added'
    with allure.step('Check the "id" key in the response data'):
        assert 'id' in resp, 'The "id" key is NOT created'
    with allure.step('Check the "updatedAt" key in the response data'):
        assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'


@allure.feature('CRUD')
@allure.story('PATCH')
@allure.title('Partial object modification')
@pytest.mark.medium
def test_patch(new_obj_id):
    with allure.step('Prepare test data'):
        body = {
            "name": "Apple MacBook Pro 16 (Updated Name)"
        }
        headers = {'Content-Type': 'application/json'}
    with allure.step('Modify the "name" key value'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{new_obj_id}',
            json=body,
            headers=headers
        )
    with allure.step('Check the response code - 200 OK'):
        resp = response.json()
        assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check the updated text'):
        assert " (Updated Name)" in resp['name'], 'The " (Updated Name)" is NOT added / is partially added'
    with allure.step('Check the "id" key in the response data'):
        assert 'id' in resp, 'The "id" key is NOT created'
    with allure.step('Check the "updatedAt" key in the response data'):
        assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'


@allure.feature('CRUD')
@allure.story('DELETE')
@allure.title('Deleting of the created object')
def test_delete(new_obj_id):
    with allure.step('Delete the created object'):
        response = requests.delete(
            f'https://api.restful-api.dev/objects/{new_obj_id}'
        )
    with allure.step('Check the response code - 200 OK'):
       assert response.status_code == 200, 'Status code is incorrect'
    with allure.step('Check the response message'):
        assert response.json()['message'] == f'Object with id = {new_obj_id} has been deleted.', 'Message is incorrect'
