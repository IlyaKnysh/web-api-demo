from functools import wraps

import requests
import urllib3

from testlib.helpers.logger import logger

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def api_checker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f'REQUEST: {result.request.method}: {result.request.url}')
        if result.request.method == 'POST' or result.request.method == 'PUT':
            logger.info(f'REQUEST_DATA: {result.request.body}')
        if not result.ok:
            raise Exception(f'Error while api request: {result.status_code}":" {result.content}')
        logger.info(f'CONTENT: {result.status_code}":" {result.content}')
        return result

    return wrapper


class BaseApi:
    api_url = ''
    token = None
    session = requests.session()
    session.verify = False

    post_headers = {
        "accept": "application/json",
        "Content-Type": "application/json-patch+json"
    }

    get_headers = {
        "accept": "application/json",
    }

    @classmethod
    @api_checker
    def api_get(cls, path, headers=None, params=None, **kwargs):
        if not headers:
            headers = cls.get_headers
        return cls.session.get(f'{cls.api_url}{path}', headers=headers, params=params)

    @classmethod
    @api_checker
    def api_post(cls, path, headers=None, params=None, data=None, files=None, **kwargs):
        new_params = {}
        if not headers:
            headers = cls.post_headers
        return cls.session.post(f'{cls.api_url}{path}', headers=headers, json=new_params if new_params else params,
                                data=data, files=files)

    @classmethod
    @api_checker
    def api_delete(cls, path, headers=None, params=None, **kwargs):
        if not headers:
            headers = cls.post_headers
        return cls.session.delete(f'{cls.api_url}{path}', headers=headers, params=params)

    @classmethod
    @api_checker
    def api_put(cls, path, headers=None, params=None, **kwargs):
        if not headers:
            headers = cls.post_headers
        return cls.session.put(f'{cls.api_url}{path}', headers=headers, json=params)
