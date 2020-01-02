import allure
from hamcrest import equal_to

from testlib.data_providers.api.api_schema import *
from testlib.helpers.matchers import check_schema_is_valid, check_that
from testlib.steps.api_steps.api_steps import ApiSteps


@allure.description('cnt-1')
@allure.title('Test success get /api/project-management/application/id')
@allure.tag('Application')
def test_get_application(add_application):
    app_name = add_application.app_name
    response = ApiSteps().Application().get_application(app_name=app_name)

    check_schema_is_valid(response.json(), APPLICATION_SCHEMA, 'Get accesses schema is valid')


@allure.description('cnt-2')
@allure.title('Test success get /api/project-management/application/id')
@allure.tag('Application')
def test_delete_application(add_application):
    app_name = add_application.app_name
    response = ApiSteps().Application().delete_application(app_name=app_name)

    check_that(response.text, equal_to('true'), 'App was successfully deleted')


@allure.description('cnt-3')
@allure.title('Test success post /api/project-management/applications')
@allure.tag('ApplicationsManagement')
def test_search_applications(add_application):
    response = ApiSteps().ApplicationsManagement().get_current_user_applications()

    check_schema_is_valid(response.json(), CURRENT_APPLICATIONS_SCHEMA, 'Post applications schema is valid')
