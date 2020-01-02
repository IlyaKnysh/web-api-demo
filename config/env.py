import os

from selene import config as _selene_config


def get(key, default=None):
    return os.environ.get(key=key, default=default)


PROJECT_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

TEST_REPORTS_DIR = os.environ.get("TEST_REPORTS_DIR", os.path.join(PROJECT_DIRECTORY, "tests/screenshots"))

SCREEN_PATH = os.path.join(TEST_REPORTS_DIR,
                           "screen_{}.png".format(str(_selene_config.counter)).replace('count(', '').replace(')', ''))

ENV = 'https://env.net'
