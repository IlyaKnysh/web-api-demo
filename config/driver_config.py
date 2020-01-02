from selene import config as _selene_config

from . import env

_selene_config.timeout = int(env.get('UI_TIMEOUT', 10))

BROWSER = env.get('BROWSER', 'chrome')
REMOTE_IP = env.get('REMOTE_IP', '127.0.0.1')
