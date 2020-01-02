from hamcrest import equal_to
from selene.conditions import visible

from testlib.helpers.matchers import check_that
from testlib.helpers.utils import check_if_browser_log_has_errors
from testlib.ui_elements.base_elements import BasePage
from testlib.ui_elements.pages.auth_pages.select_app_page import SelectAppPage


class BaseAssertionSteps:
    @staticmethod
    def check_page_title(page_title):
        check_that(BasePage.page_title.text, equal_to(page_title), f'Page title is {page_title}')

    @staticmethod
    def check_alert_message(alert_message):
        check_that(BasePage.alert.text, equal_to(alert_message), f'Alert message is {alert_message}', timeout=20)

    @staticmethod
    def check_js_errors():
        js_errors = check_if_browser_log_has_errors()
        check_that(js_errors, equal_to(False), 'There are no js errors')


class AuthAssertionSteps:
    @staticmethod
    def check_app_choice_page_is_displayed():
        check_that(SelectAppPage.ss_icon.should_be, visible, 'User is redirected to application choice page')
