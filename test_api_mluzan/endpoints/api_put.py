import requests
import allure

from .endpoint import Endpoint


class ApiPut(Endpoint):

    @allure.step('Modify the created data')
    def new_put(self, new_obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check the "color" key in the response data')
    def check_color_key(self):
        assert 'color' in self.json['data'], 'The "color" key is NOT added'
