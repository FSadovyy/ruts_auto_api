import pytest
import allure
from ruts_auto_api.tests_api.api_endpoints import endpoints_1_mainpage as main
from ruts_auto_api.tests_api.api_base.request_list import request_list
from allpairspy import AllPairs as Pairwise
from ruts_auto_api.utils.jsonreader import data

FIO, EMAIL, QUERY = data("fio", "email", "message")
GET_ENDPOINTS = request_list(main, "GET")
POST_ENDPOINTS = request_list(main, "POST")


class TestsApiMainpage:

    @pytest.mark.parametrize("get_endpoint", GET_ENDPOINTS)
    @allure.title("Тест запроса '{get_endpoint.PATH}' на корректный ответ")
    def test_get_correct(self, get_endpoint):
        endpoint = get_endpoint()
        endpoint.make_request()
        endpoint.verify_success()
        endpoint.verify_schema()

    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize("fio, email, message",
                             Pairwise([
                                 FIO["valid"],
                                 EMAIL["valid"],
                                 QUERY["valid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': тело запроса корректно")
    def test_post_correct(self, post_endpoint, fio, email, message):
        endpoint = post_endpoint()
        endpoint.fill_body(
            fio,
            email,
            message)
        endpoint.make_request()
        endpoint.verify_success()

    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize("wrong_fio, email, message",
                             Pairwise([
                                 FIO["invalid"],
                                 EMAIL["valid"],
                                 QUERY["valid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': некорректное значение поля 'fio'")
    def test_post_wrong_fio(self, post_endpoint, wrong_fio, email, message):
        endpoint = post_endpoint()
        endpoint.fill_body(
            wrong_fio,
            email,
            message)
        endpoint.make_request()
        endpoint.verify_error()

    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize("fio, wrong_email, message",
                             Pairwise([
                                 FIO["valid"],
                                 EMAIL["invalid"],
                                 QUERY["valid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': некорректное значение поля 'email'")
    def test_post_wrong_email(self, post_endpoint, fio, wrong_email, message):
        endpoint = post_endpoint()
        endpoint.fill_body(
            fio,
            wrong_email,
            message)
        endpoint.make_request()
        endpoint.verify_error()

    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize("fio, email, wrong_message",
                             Pairwise([
                                 FIO["valid"],
                                 EMAIL["valid"],
                                 QUERY["invalid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': некорректное значение поля 'message'")
    def test_post_wrong_message (self, post_endpoint, fio, email, wrong_message):
        question = post_endpoint()
        question.fill_body(
            fio,
            email,
            wrong_message)
        question.make_request()
        question.verify_error()

    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize('field', ["fio", "email", "message"])
    @pytest.mark.parametrize("fio, email, message",
                             Pairwise([
                                 FIO["valid"],
                                 EMAIL["valid"],
                                 QUERY["valid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': пропущено поле запроса '{field}'")
    def test_post_missing_field(self, post_endpoint, field, fio, email, message):
        endpoint = post_endpoint()
        endpoint.fill_body(
            fio,
            email,
            message)
        endpoint.miss
        endpoint.make_request()
        endpoint.verify_error()


    @pytest.mark.parametrize("post_endpoint", POST_ENDPOINTS)
    @pytest.mark.parametrize('field', ["fio", "email", "message"])
    @pytest.mark.parametrize("fio, email, message",
                             Pairwise([
                                 FIO["valid"],
                                 EMAIL["valid"],
                                 QUERY["valid"]
                             ]))
    @allure.title("Тест запроса '{post_endpoint.PATH}': пропущено поле '{field}' пустое")
    def test_post_missing_field(self, post_endpoint, field, fio, email, message):
        endpoint = post_endpoint()
        endpoint.fill_body(
            fio,
            email,
            message)
        endpoint.empty_field(field)
        endpoint.make_request()
        endpoint.verify_error()
