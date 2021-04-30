import requests

from json import dumps, loads
from requests_oauthlib import OAuth1
from urllib.parse import urljoin

from framework.base import LoggingObject
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


class APICaller(LoggingObject):

    DEFAULT_HEADER = {'Content-Type': 'application/json'}

    def __init__(self, url, user: APIUser = None, auth: OAuth1 = None):
        """Wrapper for API calls

        Args:
            url: API url
            user: API user. If given, creates and rewrites the auth param
                for a given user
            auth: authentication object. Shall not be provided in case user is defined

        """
        super().__init__(__name__)
        self._url = url
        if user:
            auth = get_user_auth(user)
        self._auth = auth

    def _send_request(self, extension, func, *args, **kwargs):
        url = urljoin(self._url, extension)
        resp = func(url, *args, **kwargs)
        resp_dict = loads(resp.text)
        status_code = resp_dict['data']['status']
        code = resp_dict['code']
        message = resp_dict['message']
        msg = f'Status code: {status_code}. Message: "{code}...{message}"'
        self.logger.warning(f'HTTP response details: {msg}')
        return resp

    def get(self, extension, params: dict = None, **kwargs):
        """HTTP GET request"""
        return self._send_request(extension, requests.get, params=params,
                                  auth=self._auth, **kwargs)

    def post(self, extension: str, data=None, headers: dict = None, **kwargs):
        """HTTP POST request"""
        if not headers:
            headers = self.DEFAULT_HEADER
        if type(data) is dict:
            data = dumps(data)
        return self._send_request(extension, requests.post, data, headers=headers,
                                  auth=self._auth, **kwargs)

    def put(self, extension: str, data: dict, headers: dict = None, **kwargs):
        """HTTP PUT request"""
        if not headers:
            headers = self.DEFAULT_HEADER
        return self._send_request(extension, requests.put, dumps(data),
                                  headers=headers, auth=self._auth, **kwargs)

    def patch(self, extension: str, data: dict, headers: dict = None, **kwargs):
        """HTTP PATCH request"""
        if not headers:
            headers = self.DEFAULT_HEADER
        return self._send_request(extension, requests.patch, dumps(data),
                                  headers=headers, auth=self._auth, **kwargs)

    def delete(self, extension: str, params: dict = None, **kwargs):
        """HTTP DELETE request"""
        return self._send_request(extension, requests.delete, auth=self._auth,
                                  params=params, **kwargs)

    def options(self, extension: str, **kwargs):
        """HTTP OPTIONS request"""
        return self._send_request(extension, requests.options, auth=self._auth, **kwargs)
