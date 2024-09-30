import pytest


POST_DATA = [
    {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 1849.99,
     "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Apple MacBook Air", "data": {"year": 2020, "price": 1999.99,
     "CPU model": "Apple M1", "Hard disk size": "2 TB"}},
    {"name": "Apple MacBook Pro 14", "data": {"year": 2021, "price": 2499.99,
     "CPU model": "Apple M1 Max", "Hard disk size": "8 TB"}}
]

PUT_DATA = [
    {"name": "Apple MacBook Pro 16", "data": {"year": 2019, "price": 2049.99,
     "CPU model": "Intel Core i9", "Hard disk size": "1 TB", "color": "silver"}}
]

PATCH_DATA = [
    {"name": "Apple MacBook Pro 16 (Updated Name)"}
]


@pytest.mark.smoke
@pytest.mark.parametrize('data', POST_DATA)
def test_post(post_endpoint, data):
    post_endpoint.new_post(payload=data)
    post_endpoint.check_response_code_is_200()
    post_endpoint.check_id_key()
    post_endpoint.check_created_at_key()


@pytest.mark.smoke
@pytest.mark.parametrize('data', PUT_DATA)
def test_put(put_endpoint, new_obj, data):
    put_endpoint.new_put(new_obj, payload=data)
    put_endpoint.check_response_code_is_200()
    put_endpoint.check_color_key()
    put_endpoint.check_id_key()
    put_endpoint.check_updated_at_key()


@pytest.mark.regression
@pytest.mark.parametrize('data', PATCH_DATA)
def test_patch(patch_endpoint, new_obj, data):
    patch_endpoint.new_patch(new_obj, payload=data)
    patch_endpoint.check_response_code_is_200()
    patch_endpoint.check_updated_text(updated_text=data['name'])
    patch_endpoint.check_id_key()
    patch_endpoint.check_updated_at_key()


@pytest.mark.smoke
def test_delete(delete_endpoint, new_obj):
    delete_endpoint.new_delete(new_obj)
    delete_endpoint.check_response_code_is_200()
    delete_endpoint.check_response_message(new_obj)
