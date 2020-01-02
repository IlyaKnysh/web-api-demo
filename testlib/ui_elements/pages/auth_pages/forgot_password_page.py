from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.ui_elements.base_elements import BasePage


class ForgotPasswordPage(BasePage):
    email_address_field = element(by.id('email'))

    send_email_button = element(by.xpath('//button[text()="Send Email"]'))
