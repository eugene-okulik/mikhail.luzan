import requests
import allure

from .endpoint import Endpoint


class ApiPatch(Endpoint):


    @allure.step('Modify the "name" key value')
    def new_patch(self, new_obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response


    @allure.step('Check the updated text')
    def check_updated_text(self):
        assert ' (Updated Name)' in self.json['name'], 'The " (Updated Name)" is NOT added / is partially added'
