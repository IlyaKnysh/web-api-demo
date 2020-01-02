import allure
from selene import browser

from testlib.steps.imap_steps.imap_steps import search_email_imap, get_for_forgot_password_link
from testlib.ui_elements.pages.auth_pages.forgot_password_page import ForgotPasswordPage
from testlib.ui_elements.pages.auth_pages.login_page import LoginPage
from testlib.ui_elements.pages.auth_pages.reset_password_page import ResetPasswordPage

login_page = LoginPage()
forgot_password_page = ForgotPasswordPage()
reset_password_page = ResetPasswordPage()


class AuthorizationSteps:
    @allure.step('User Forgot Password feature')
    def send_forgot_password_email(self, email):
        login_page.navigate()
        login_page.forgot_password_link.click()
        forgot_password_page.email_address_field.send_keys(email)
        forgot_password_page.send_email_button.click()

    @allure.step('Use forgot password link')
    def use_forgot_password_link(self, mail, subject_email):
        link = search_email_imap(mail, subject_email, get_for_forgot_password_link, unquote=False).link
        browser.driver().get(link)
        return link

    @allure.step('Set new password')
    def set_new_password(self, password, reset=True):
        reset_password_page.password_field.send_keys(password)
        reset_password_page.confirm_password_field.send_keys(password)

        if reset:
            reset_password_page.reset_password_button.click()
        else:
            reset_password_page.set_password_button.click()

    @allure.step('Authorize to the system')
    def login_to_system(self, username='username', password='password', direct_navigate=True):
        if direct_navigate:
            login_page.navigate()
        login_page.username_field.send_keys(username)
        login_page.password_field.send_keys(password)
        login_page.log_in_button.click()
