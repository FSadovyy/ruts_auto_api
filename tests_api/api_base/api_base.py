from jsonschema import validate
from .client import Client
from abc import ABC
import allure

BASE_URL = #url

class Request(ABC):

    METHOD: str
    PATH: str
    SCHEMA: dict
    SUCCESS_CODE = 200

    def __init__(self, url=BASE_URL, req_id=None, token=None):
        self.url, self.req_id, self.token = url, req_id, token
        self.body, self.files, self.response = None, None, None
        self.client = Client()

    @allure.step("Убедиться, что в хидере присутствует токен аутентификации")
    def fill_header(self, header):
        self.token = {"Cookie": header}

    def make_request(self):
        modes = {
            "{id}": self.req_id,
            "{token}": self.token
        }

        path = self.path()

        for mod, value in modes.items():
            if mod in path and value is not None:
                path = path.replace(mod, value)

        url = f"{self.url}{path}"

        with allure.step(f"Отправить {self.METHOD} запрос на URL: {url}"):
            self.response = self.client.project_request(self.METHOD, url, json=self.body, headers=self.token,
                                                        files=self.files)

    def path(self):
        return self.PATH

    def user_token(self):
        return self.response.headers['Set-Cookie']

    @allure.step("Убедиться, что код ответа соответствует ошибке")
    def verify_error(self):
        assert not self.response.ok

    @allure.step("Убедиться, что тело ответа в формате json")
    def verify_header(self):
        assert self.response.headers["Content-Type"] == "application/json; charset=UTF-8"

    @allure.step("Убедиться, что схема ответа соответствует указанной в swagger")
    def verify_schema(self):
        validate(instance=self.response.json(), schema=self.SCHEMA)

    @allure.step("Убедиться, что код ответа - {code}")
    def verify_status(self, code):
        assert self.response.status_code == code

    def verify_success(self):
        code = self.SUCCESS_CODE
        with allure.step(f"Убедиться, что код ответа - {code}"):
            assert self.response.status_code == code


class PostRequest(Request):
    FIELDS: dict
    METHOD = "POST"

    def fill_body(self, *args):
        self.body = {k: v for k, v in zip(self.FIELDS, args)}
        with allure.step(f"Задать тело запроса: {self.body}"):
            pass

    @allure.step("Очистить поле '{field}'")
    def empty_field(self, field):
        self.body[field] = ""

    @allure.step("Убрать поле '{field}' из тела запроса")
    def miss_field(self, field):
        del self.body[field]


class GetRequest(Request):
    METHOD = "GET"


class PutRequest(PostRequest):
    METHOD = "PUT"

    def upload_file(self, file_path):
        self.files = {
            'file': open(file_path, 'rb')
        }


class PatchRequest(PostRequest):
    METHOD = "PATCH"

    def fill_field(self, field, arg):
        if self.body is None:
            self.body = {}
        if field in self.FIELDS:
            self.body = {**self.body, **{field: arg}}
