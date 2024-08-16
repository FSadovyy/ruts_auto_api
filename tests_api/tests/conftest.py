import pytest
import json
from ruts_auto_api.tests_api.api_endpoints.endpoints_2_auth import Signin, Logout

TEST_USER = '../../registered_user.json'

@pytest.fixture(scope='session')
def test_user():
    user_file = open(TEST_USER)
    return json.load(user_file)

@pytest.fixture()
def user_authorization(request, test_user):
    user = Signin()
    user.fill_body(*test_user.values(), True)
    user.make_request()
    user.verify_success()
    request.cls.token = user.user_token()
    request.cls.user = test_user
    yield
    user = Logout()
    user.make_request()
    user.verify_success()


