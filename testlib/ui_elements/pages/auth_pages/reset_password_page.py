from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.ui_elements.base_elements import BasePage


class ResetPasswordPage(BasePage):
    password_field = element(by.id('password'))

    confirm_password_field = element(by.id('confirmPassword'))

    reset_password_button = element(by.xpath('//button[text()="Reset Password"]'))

    set_password_button = element(by.xpath('//button[text()="Save"]'))
