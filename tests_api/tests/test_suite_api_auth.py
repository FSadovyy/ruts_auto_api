import pytest
import allure
import json

USER_ONE = '../../unregistered_user.json'
USER_TWO = '../../registered_user.json'


class TestsApiUnregisteredUser:
    test_user = json.load(open(USER_ONE))

    @allure.title("Тест запроса '/code/send' на корректный ответ")
    def test_send(self):
        user = Send()
        user.fill_body(
            self.test_user["email"],
                    )
        user.make_request()
        user.verify_success()
        user.verify_schema()


    @allure.title("Тест запроса '/auth/signup' на корректный ответ")
    def test_registration(self):
        user = Signup()
        user.fill_body(
            self.test_user["email"],
            self.test_user["password"],
            self.test_user["password"]
        )
        user.make_request()
        user.verify_success()
        user.verify_schema()


class TestsApiRegisteredUser:
    test_user = json.load(open(USER_TWO))

    @allure.title("Тест запроса '/auth/signin' на корректный ответ")
    def test_autorization(self, request):
        user = Signin()
        user.fill_body(
            self.test_user["email"],
            self.test_user["password"],
            True)
        user.make_request()
        user.verify_success()
        user.verify_schema()
        request.cls.token = user.user_token()

    @allure.title("Тест запроса '/auth/me' на корректный ответ")
    def test_me(self):
        user = Me()
        user.fill_header(self.token)
        user.make_request()
        user.verify_success()
        user.verify_schema()

    @allure.title("Тест запроса '/auth/logout' на корректный ответ")
    def test_logout(self):
        user = Logout()
        user.fill_header(self.token)
        user.make_request()
        user.verify_success()
        user.verify_schema()

    @pytest.mark.parametrize("get_endpoint", [Google, Vk])
    @allure.title("Тест запроса '{get_endpoint.PATH}' на корректный ответ")
    def test_network(self, get_endpoint):
        user = get_endpoint()
        user.make_request()
        user.verify_success()
