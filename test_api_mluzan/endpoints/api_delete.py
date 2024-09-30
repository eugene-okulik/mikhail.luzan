import requests
import allure

from .endpoint import Endpoint


class ApiDelete(Endpoint):

    @allure.step('Delete the created object')
    def new_delete(self, new_obj_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{new_obj_id}',
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check the response message')
    def check_response_message(self, new_obj_id):
        assert self.json['message'] == f'Object with id = {new_obj_id} has been deleted.', 'Message is incorrect'
