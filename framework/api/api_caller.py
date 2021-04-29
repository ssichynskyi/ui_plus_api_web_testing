import requests

from json import dumps
from requests_oauthlib import OAuth1
from urllib.parse import urljoin

from framework.utilities.credentials_helper import APIUser


def get_user_auth(user: APIUser, **kwargs) -> OAuth1:
    """Returns authentication entity for a given User object"""
    return OAuth1(
        user.customer_key,
        user.customer_secret,
        user.token,
        user.token_secret,
        **kwargs
    )


class APICaller:
    def __init__(self, url, user: APIUser = None, auth: OAuth1 = None):
        """Wrapper for API calls

        Args:
            url: API url
            user: API user. If given, creates and rewrites the auth param
                for a given user
            auth: authentication object. Shall not be provided in case user is defined

        """
        self._url = url
        if user:
            auth = get_user_auth(user)
        self._auth = auth

    def get(self, extension, params: dict = None, **kwargs):
        """HTTP GET request"""
        url = urljoin(self._url, extension)
        return requests.get(url, params=params, auth=self._auth, **kwargs)

    def post(self, extension: str, data=None, headers: dict = None, **kwargs):
        """HTTP POST request"""
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = urljoin(self._url, extension)
        if type(data) is dict:
            data = dumps(data)
        return requests.post(url, data, headers=headers, auth=self._auth, **kwargs)

    def put(self, extension: str, data: dict, headers: dict = None, **kwargs):
        """HTTP PUT request"""
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = urljoin(self._url, extension)
        return requests.put(url, dumps(data), headers=headers, auth=self._auth, **kwargs)

    def patch(self, extension: str, data: dict, headers: dict = None, **kwargs):
        """HTTP PATCH request"""
        if not headers:
            headers = {'Content-Type': 'application/json'}
        url = urljoin(self._url, extension)
        return requests.patch(url, dumps(data), headers=headers, auth=self._auth, **kwargs)

    def delete(self, extension: str, params: dict = None, **kwargs):
        """HTTP DELETE request"""
        url = urljoin(self._url, extension)
        return requests.delete(url, auth=self._auth, params=params, **kwargs)

    def options(self, extension: str, **kwargs):
        """HTTP OPTIONS request"""
        url = urljoin(self._url, extension)
        return requests.options(url, auth=self._auth, **kwargs)
