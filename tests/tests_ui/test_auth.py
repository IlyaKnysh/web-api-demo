import allure

from testlib.steps.assertion_steps.main_assertion_steps import AuthAssertionSteps
from testlib.steps.ui_steps.auth_steps import AuthorizationSteps

auth_steps = AuthorizationSteps()


@allure.description('auth-1')
@allure.title('Reset password')
@allure.tag('Forgot password')
def test_reset_password(create_user, driver):
    email = create_user.email
    name = create_user.username
    new_password = 'Qq1234!1'

    auth_steps.send_forgot_password_email(email)
    auth_steps.use_forgot_password_link(email)
    auth_steps.set_new_password(new_password)

    auth_steps.login_to_system(username=name, password=new_password, direct_navigate=False)

    AuthAssertionSteps.check_app_choice_page_is_displayed()
