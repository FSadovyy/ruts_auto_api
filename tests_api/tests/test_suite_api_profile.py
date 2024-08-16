import pytest
import allure
from ruts_auto_api.utils.path import custom_path
from ruts_auto_api.tests_api.api_endpoints import endpoints_3_profile as main
from ruts_auto_api.tests_api.api_endpoints.endpoints_3_profile import *
from ruts_auto_api.tests_api.api_base.request_list import request_list
from allpairspy import AllPairs as Pairwise
from ruts_auto_api.utils.jsonreader import data

GET_ENDPOINTS = request_list(main, "GET")
EMAIL, QUERY = data("email", "message")


@pytest.mark.usefixtures("user_authorization")
class TestProfile:
    @pytest.mark.parametrize("get_endpoint", GET_ENDPOINTS)
    @allure.title("Тест запроса '{get_endpoint.PATH}' на корректный ответ")
    def test_user(self, get_endpoint):
        endpoint = get_endpoint()
        endpoint.fill_header(self.token)
        endpoint.make_request()
        endpoint.verify_success()
        endpoint.verify_schema()

    @allure.title("Тест запроса '/profile/commands' на корректный ответ")
    @pytest.mark.parametrize("name, email",
                             Pairwise([
                                 QUERY["valid"],
                                 EMAIL["valid"]
                             ]))
    def test_commands(self, name, email):
        endpoint = CommandsPost()
        endpoint.fill_header(self.token)
        endpoint.fill_body(
            name,
            email
        )
        endpoint.make_request()
        endpoint.verify_success()

    @allure.title("Тест запроса '/profile/avatar' на корректный ответ")
    def test_avatar(self):
        endpoint = AvatarPut()
        endpoint.fill_header(self.token)
        endpoint.upload_file(custom_path("ruts_auto_api/data/jpeg/avatar.jpg"))
        endpoint.make_request()
        endpoint.verify_success()

    @allure.title("Тест запроса '/profile/password' на корректный ответ")
    def test_password(self):
        endpoint = Password()
        endpoint.fill_header(self.token)
        endpoint.fill_body(self.user["password"],
                           "123456789",
                           "123456789")
        endpoint.make_request()
        endpoint.verify_success()
        endpoint.fill_body("123456789",
                           self.user["password"],
                           self.user["password"])
        endpoint.make_request()
        endpoint.verify_success()
