import random

from locust import task, tag, HttpUser, SequentialTaskSet, between
from endpoints.endpoint import Endpoint
from tests.test_file import POST_DATA, PATCH_DATA, PUT_DATA


class BaseSequence(SequentialTaskSet):
    base_endpoint = '/objects'
    obj_id = None

    def __init__(self, parent):
        super().__init__(parent)
        self.endpoint = Endpoint()

    @task
    def get_load(self):
        with self.client.get(
            self.base_endpoint,
            headers=self.endpoint.headers,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"GET failed with status {response.status_code}, response: {response.text}")

    @task
    def post_load(self):
        payload = random.choice(POST_DATA)
        with self.client.post(
            self.base_endpoint,
            json=payload,
            headers=self.endpoint.headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                self.obj_id = response.json().get('id')
            else:
                response.failure(f"POST failed with status {response.status_code}, response: {response.text}")

    @task
    def put_load(self, obj_id):
        with self.client.put(
            f'{self.base_endpoint}/{obj_id}',
            name=self.base_endpoint,
            json=PUT_DATA[0],
            headers=self.endpoint.headers,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"PUT failed with status {response.status_code}, response: {response.text},"
                                 f" ID: {self.obj_id}, DATA: {PUT_DATA}")

    @task
    def patch_load(self, obj_id):
        with self.client.patch(
            f'{self.base_endpoint}/{obj_id}',
            name=self.base_endpoint,
            json=PATCH_DATA[0],
            headers=self.endpoint.headers,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure(f"PATCH failed with status {response.status_code}, response: {response.text},"
                                 f" ID: {self.obj_id}, DATA: {PATCH_DATA}")

    @task
    def delete_load(self, obj_id):
        with self.client.delete(
            f'{self.base_endpoint}/{obj_id}',
            name=self.base_endpoint,
            headers=self.endpoint.headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                self.obj_id = None
            else:
                response.failure(f"DELETE failed with status {response.status_code}, response: {response.text}")


class UserFlows(HttpUser):
    wait_time = between(1, 3)

    def __init__(self, parent):
        super().__init__(parent)
        self.base = BaseSequence(self)
        self.obj_ids = []

    @tag('get')
    @task(3)
    def get_sequence(self):
        self.base.get_load()

    @tag('post')
    @task(3)
    def post_sequence(self):
        self.base.get_load()
        self.base.post_load()
        obj_id = self.base.obj_id
        self.obj_ids.append(obj_id)
        self.base.get_load()

    @tag('put')
    @task(2)
    def post_put_sequence(self):
        self.base.get_load()
        self.base.post_load()
        obj_id = self.base.obj_id
        self.obj_ids.append(obj_id)
        self.base.get_load()
        self.base.put_load(obj_id)
        self.base.get_load()

    @tag('patch')
    @task(1)
    def post_patch_sequence(self):
        self.base.get_load()
        self.base.post_load()
        obj_id = self.base.obj_id
        self.obj_ids.append(obj_id)
        self.base.get_load()
        self.base.patch_load(obj_id)
        self.base.get_load()

    @tag('delete')
    @task(1)
    def post_delete_sequence(self):
        self.base.get_load()
        self.base.post_load()
        obj_id = self.base.obj_id
        self.base.get_load()
        self.base.delete_load(obj_id)
        self.base.get_load()

    def on_stop(self):
        for obj_id in self.obj_ids:
            self.base.delete_load(obj_id)
