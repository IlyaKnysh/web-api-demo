import inspect
import time
from types import LambdaType

import allure
from hamcrest import assert_that
from jsonschema import validate, ValidationError
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


def check_that(actual, matcher, message='message', timeout=4, polling=0.1):
    """Wrapper over 'assert_that' to add step in allure report."""
    __tracebackhide__ = True
    with allure.step("Check that " + message):
        if isinstance(actual, LambdaType):
            end_time = time.time() + timeout
            while True:
                try:
                    assert_that(actual(), matcher, message)
                    break
                except AssertionError:
                    if time.time() > end_time:
                        raise AssertionError(message)
                    time.sleep(polling)
                except StaleElementReferenceException:
                    time.sleep(polling)
                except TimeoutException:
                    raise AssertionError(message)
        elif inspect.ismethod(actual):
            try:
                actual(matcher, timeout=timeout)
            except TimeoutException:
                raise AssertionError(message)
        else:
            assert_that(actual, matcher, message)


def check_schema_is_valid(data, schema, message):
    __tracebackhide__ = True
    with allure.step("Check that " + message):
        try:
            validate(data, schema)
        except ValidationError as e:
            raise AssertionError(e)
