from config.env import ENV
from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.ui_elements.base_elements import BasePage


class LoginPage(BasePage):
    path = ENV

    username_field = element(by.id('username'))

    password_field = element(by.id('password'))

    forgot_password_link = element(by.class_name('reset-password-link'))

    log_in_button = element(by.xpath('//button[text()="Log In"]'))
