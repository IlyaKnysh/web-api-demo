import random
import string

from selene import factory

from testlib.helpers.logger import logger


def generate_random_string(num=5, _string=True):
    return "".join(
        random.choice(string.ascii_letters if _string else string.digits.replace('0', '')) for _ in range(num))


def scroll_into_view(_web_element):
    factory.get_shared_driver().execute_script('arguments[0].scrollIntoView();', _web_element.get_actual_webelement())
    return _web_element


def check_if_browser_log_has_errors():
    full_log = factory.get_shared_driver().get_log('browser')
    errors = [x for x in full_log if x.get('level') == 'SEVERE']
    if errors:
        for error in errors:
            logger.error(f'JS ERROR:\n{error}\n')
        return errors
    else:
        return False


def generate_fake_email(mailbox=None):
    insert_position = mailbox.find('@')
    fake_mail = mailbox[:insert_position] + f'+{generate_random_string()}' + mailbox[insert_position:]
    logger.info(f'Email generated: {fake_mail}')
    return fake_mail
