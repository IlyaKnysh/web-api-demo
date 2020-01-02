import os
import shutil

import allure
import pytest
from selene import factory
from selenium.common.exceptions import WebDriverException

from config import driver as driver_setup
from config.env import SCREEN_PATH, TEST_REPORTS_DIR
from testlib.helpers.logger import logger
from testlib.helpers.utils import check_if_browser_log_has_errors

pytest_plugins = [
    'testlib.fixtures.api_fixtures.api_fixtures'
]


@pytest.yield_fixture(scope='function')
def driver(worker_id, request):
    logger.info(f'Starting driver for {worker_id}')
    ui_driver = driver_setup.Driver().start()
    factory.set_shared_driver(ui_driver)
    logger.info(f'Driver started for {worker_id}')

    yield ui_driver

    try:
        logger.info(f'Close driver for {worker_id}')
        ui_driver.quit()
        logger.info(f'Driver closed for {worker_id}')
    except WebDriverException:
        logger.info(f'Driver is already closed by exception interact hook')


def pytest_exception_interact(node, call, report):
    """Attach screenshot if test failed"""
    if report.failed:
        shutil.rmtree(TEST_REPORTS_DIR, ignore_errors=True)
        shutil.rmtree(os.path.join(TEST_REPORTS_DIR, 'screenshots'), ignore_errors=True)
        os.makedirs(TEST_REPORTS_DIR)
        try:
            check_if_browser_log_has_errors()
            factory.get_shared_driver().save_screenshot(SCREEN_PATH)
            with open(SCREEN_PATH, 'rb') as screen:
                allure.attach(screen.read(), 'screen', allure.attachment_type.PNG)

            factory.get_shared_driver().quit()
        except Exception:
            logger.info(f'failed to make screenshot for exception:\n{report.longrepr}')
