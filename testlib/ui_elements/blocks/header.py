from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.helpers.utils import scroll_into_view
from testlib.ui_elements.base_elements import BasePage, BaseEnum


class Header(BasePage):
    collapse_button = element(by.id('sidebar-collapse'))

    gear_button = element(by.id('settings-dropdown-toggle'))

    plugins_button = element(by.class_name('plugin-btn'))

    notifications_button = element(by.class_name('announcement-btn'))

    account_button = element(by.class_name('btn-dots'))

    class Settings(BaseEnum):
        EMAIL_SETTINGS = 'Email settings'
        DATABASE_SETTINGS = 'Database settings'
        AUTHENTICATION_SETTINGS = 'Authentication settings'
        USERS_ROLES_AND_REGISTRATION_APPROVAL = 'Users, Roles and Registration Approval'
        CUSTOMIZATION_SETTINGS = 'Customization settings'
        AUDIT = 'Audit'

        @property
        def get_option(self):
            Header.gear_button.click()
            return scroll_into_view(element(by.xpath(f'//li/a/span[contains(text(),"{self.value}")]')))

    class Profile(BaseEnum):
        EDIT_PROFILE = 'Edit Profile'
        LOG_OUT = 'Log Out'

        @property
        def get_option(self):
            Header.account_button.click()
            return self._get()
