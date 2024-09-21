import requests
import allure

from .endpoint import Endpoint


class ApiPost(Endpoint):

    @allure.step('Create data')
    def new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.new_obj_id = self.json.get('id')
        return self.response

    @allure.step('Check the "createdAt" key in the response data')
    def check_created_at_key(self):
        assert 'createdAt' in self.json, 'The "createdAt" key is NOT created'
