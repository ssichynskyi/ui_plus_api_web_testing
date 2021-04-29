import pytest
from urllib.parse import urljoin

from framework.api.api_caller import APICaller
from framework.utilities.credentials_helper import (
    woo_api_readonly_user,
    woo_api_read_write_user,
    wp_api_read_write_user
)
from framework.utilities.env_config import api_host_config


HOST_AND_PORT = ':'.join((api_host_config['url'], str(api_host_config['port'])))
WOO_API_URL = urljoin(HOST_AND_PORT, api_host_config['hierarchy']['woo'])
WORDPRESS_API_URL = urljoin(HOST_AND_PORT, api_host_config['hierarchy']['wp'])


@pytest.fixture(scope='package')
def unauthorized_woo_api_client() -> APICaller:
    return APICaller(WOO_API_URL)


@pytest.fixture(scope='package')
def readonly_woo_api_client() -> APICaller:
    return APICaller(WOO_API_URL, user=woo_api_readonly_user)


@pytest.fixture(scope='package')
def read_write_woo_api_client() -> APICaller:
    return APICaller(WOO_API_URL, user=woo_api_read_write_user)


@pytest.fixture(scope='package')
def unauthorized_wp_api_client() -> APICaller:
    return APICaller(WORDPRESS_API_URL)


@pytest.fixture(scope='package')
def read_write_wp_api_client() -> APICaller:
    return APICaller(WORDPRESS_API_URL, user=wp_api_read_write_user)
