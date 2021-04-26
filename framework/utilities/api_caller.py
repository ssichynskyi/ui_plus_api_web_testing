import requests
from json import dumps
from requests_oauthlib import OAuth1
from urllib.parse import urljoin

from framework.utilities.credentials_helper import APIUser
from framework.utilities.env_config import api_host_config


DEFAULT_API_URL = api_host_config['url']


def get_user_auth(user: APIUser) -> OAuth1:
    return OAuth1(
        user.customer_key,
        user.customer_secret
    )


class APICaller:
    def __init__(self, url=DEFAULT_API_URL, user: APIUser = None, auth: OAuth1 = None):
        self._url = url
        if user:
            auth = get_user_auth(user)
        self._auth = auth

    def get(self, extension, params):
        url = urljoin(self._url, extension)
        return requests.get(url, params, auth=self._auth)

    def post(self, extension: str, payload: dict, headers=None):
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = urljoin(self._url, extension)
        return requests.post(url, dumps(payload), headers=headers, auth=self._auth)
