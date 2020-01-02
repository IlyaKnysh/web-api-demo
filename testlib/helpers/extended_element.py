from selene import factory
from selene.driver import _shared_driver
from selene.elements import SeleneElement, WebDriverWebElementLocator
from selene.helpers import css_or_by_to_by
from selene.support.conditions import be


class ExtendedSeleneElement(SeleneElement):
    def click(self):
        self._execute_on_webelement(
            lambda it: it.click(),
            condition=be.clickable)
        return self

    def js_click(self):
        return factory.get_shared_driver().execute_script("arguments[0].click();", self.get_actual_webelement())

    def set_attribute(self, value):
        return factory.get_shared_driver().execute_script(
            f"arguments[0].setAttribute('value', '{value}')", self.get_actual_webelement())

    def send_keys(self, *value):
        self._execute_on_webelement(
            lambda it: it.send_keys(*value),
            condition=be.existing)
        return self

    def hover(self):
        self._execute_on_webelement(
            lambda it: self._actions_chains.move_to_element(it).perform(),
            condition=be.visible)
        return self

    def is_selected(self):
        return self._execute_on_webelement(
            lambda it: it.is_selected(),
            condition=be.existing)

    @classmethod
    def by_css_or_by(cls, css_selector_or_by, webdriver, context=None):
        if not context:
            context = webdriver

        return ExtendedSeleneElement.by(css_or_by_to_by(css_selector_or_by), webdriver, context)

    @classmethod
    def by(cls, by, webdriver, context=None):
        if not context:
            context = webdriver

        return ExtendedSeleneElement(WebDriverWebElementLocator(by, context), webdriver)


def element(css_selector_or_by):
    return ExtendedSeleneElement.by_css_or_by(css_selector_or_by, _shared_driver)
