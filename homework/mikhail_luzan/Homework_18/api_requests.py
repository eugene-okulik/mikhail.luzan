import requests


def post():
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
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'createdAt' in resp, 'The "createdAt" key is NOT created'


post()
print(f'\nThe POST request has been successfully executed')


def new_obj():
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
    return response.json()['id']


def del_obj(obj_id):
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')


def put():
    obj_id = new_obj()
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
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    )
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert 'color' in resp['data'], 'The "color" key is NOT added'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'
    del_obj(obj_id)


put()
print(f'\nThe PUT request has been successfully executed')


def patch():
    obj_id = new_obj()
    body = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=body,
        headers=headers
    )
    resp = response.json()
    assert response.status_code == 200, 'Status code is incorrect'
    assert " (Updated Name)" in resp['name'], 'The " (Updated Name)" is NOT added / is partially added'
    assert 'id' in resp, 'The "id" key is NOT created'
    assert 'updatedAt' in resp, 'The "updatedAt" key is NOT created'
    del_obj(obj_id)


patch()
print(f'\nThe PATCH request has been successfully executed')


def delete():
    obj_id = new_obj()
    response = requests.delete(
        f'https://api.restful-api.dev/objects/{obj_id}'
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['message'] == f'Object with id = {obj_id} has been deleted.', 'Message is incorrect'


delete()
print(f'\nThe DELETE request has been successfully executed')
