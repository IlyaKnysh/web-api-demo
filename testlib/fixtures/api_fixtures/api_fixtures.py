import re
from collections import namedtuple

import pytest

from testlib.api.helpers_api import BaseApi
from testlib.helpers.utils import generate_random_string, generate_fake_email
from testlib.steps.api_steps.api_steps import ApiSteps


@pytest.yield_fixture(scope='session')
def authorize_via_api():
    response = ApiSteps().Auth().post_login()
    access_token = re.search("name='access_token'.*value='(.*)' />", response.text).group(1)
    BaseApi.token = access_token


@pytest.fixture(scope='function')
def add_application(authorize_via_api):
    return_tuple = namedtuple('return_tuple', ['response', 'app_name'])
    app_name = generate_random_string()
    response = ApiSteps().Application().create_application(custom_id=app_name, name=app_name)

    return return_tuple(response=response, app_name=app_name)


@pytest.fixture(scope='function')
def create_user(authorize_via_api):
    return_tuple = namedtuple('return_tuple', ['email', 'username', 'password'])
    email = generate_fake_email()
    name = generate_random_string(10)
    password = 'Password1!'
    ApiSteps().UserManagement().create_user(email=email, password=password, confirm_password=password, username=name,
                                            first_name=name, last_name=name, connect=False)

    return return_tuple(email=email, username=name, password=password)
