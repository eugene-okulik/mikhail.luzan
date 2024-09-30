import pytest

from .endpoints.api_post import ApiPost
from .endpoints.api_put import ApiPut
from .endpoints.api_patch import ApiPatch
from .endpoints.api_delete import ApiDelete
from .tests.test_file import POST_DATA


@pytest.fixture()
def post_endpoint():
    return ApiPost()


@pytest.fixture()
def put_endpoint():
    return ApiPut()


@pytest.fixture()
def patch_endpoint():
    return ApiPatch()


@pytest.fixture()
def delete_endpoint():
    return ApiDelete()


@pytest.fixture()
def new_obj(post_endpoint, delete_endpoint):
    payload = POST_DATA[0]
    post_endpoint.new_post(payload)
    try:
        yield post_endpoint.new_obj_id
    finally:
        delete_endpoint.new_delete(post_endpoint.new_obj_id)
