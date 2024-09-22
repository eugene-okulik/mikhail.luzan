import allure


class Endpoint:

    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None
    new_obj_id = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check the response code - 200 OK')
    def check_response_code_is_200(self):
        assert self.response.status_code == 200, f'Status code {self.response.status_code} is incorrect'

    @allure.step('Check the "id" key in the response data')
    def check_id_key(self):
        assert 'id' in self.json, 'The "id" key is NOT created'

    @allure.step('Check the "updatedAt" key in the response data')
    def check_updated_at_key(self):
        assert 'updatedAt' in self.json, 'The "updatedAt" key is NOT created'
