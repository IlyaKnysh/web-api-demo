import enum

from selene import factory

from testlib.helpers import by
from testlib.helpers.extended_element import element
from testlib.helpers.utils import scroll_into_view


class BasePage:
    url = '/'
    path = ''

    page_title = element(by.class_name('page-title'))

    loader = element(by.class_name('loader active'))

    def navigate(self):
        factory.get_shared_driver().get(f'{self.path}{self.url}')
        return self

    alert = element(by.xpath('//div[@role="alert"]'))


class BaseEnum(enum.Enum):
    def _get(self):
        _element = element(by.xpath(f'//li/a/span[text()="{self.value}"]'))
        return scroll_into_view(_element)
