import email
import html
import imaplib
import re
import time
import urllib.parse

from testlib.helpers.logger import logger

generic_charset = '[A-Za-z0-9\/.?=&%_\-;!]*'


class IMAPConnector:
    def __init__(self, user):
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.login = user.login
        self._pass = user.password

    def __enter__(self):
        self.mail.login(self.login, self._pass)
        self.mail.select("inbox")
        return self.mail

    def __exit__(self, *args):
        self.mail.logout()


def search_email_imap(user, fake_mail, func, **kwargs):
    tries = 0
    logger.info(f'Looking for mail in mailbox {user.login}')
    while True:
        with IMAPConnector(user) as connector:
            result, data = connector.search(None, "ALL")
            mails = data[0].split()
            id_list = mails[-20:] if len(mails) > 1 else [mails[-1]]
            for _id in id_list:
                result, data = connector.fetch(_id, "(RFC822)")
                received_email = email.message_from_string(data[0][1].decode("utf-8"))
                funk_res = func(fake_mail, received_email, **kwargs)
                if funk_res:
                    return funk_res
            if tries >= 5:
                raise AssertionError('Email was not received')
            else:
                tries += 1
                logger.info(f'Message was not received after {tries} attempt(s) for {func.__name__}')
                time.sleep(1)


def flatten_email(_email):
    if _email.is_multipart():
        return [payload for message in _email.get_payload() for payload in flatten_email(message)]
    else:
        return [str(_email.get_payload(decode=True))]


def extract_by_pattern(_email, pattern, unquote=True):
    raw_payload = flatten_email(_email)
    for payload in raw_payload:
        clean_body = str(payload).replace(r'\r\n', ' ')
        try:
            return urllib.parse.unquote(
                html.unescape(re.findall(pattern, clean_body)[0])) if unquote else html.unescape(
                re.findall(pattern, clean_body)[0])
        except IndexError:
            continue


def get_for_forgot_password_link(_email, parsed_email, **kwargs):
    if 'reset your Self-Serve password' in parsed_email.get('subject') and parsed_email.get('to') == _email:
        link_pattern = f'(https:{generic_charset}reset-password{generic_charset})'
        return extract_by_pattern(parsed_email, link_pattern, **kwargs)
