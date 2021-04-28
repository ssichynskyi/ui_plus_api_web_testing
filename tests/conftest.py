import pytest

from framework.api.api_caller import APICaller
from framework.utilities.credentials_helper import readonly_api_user, read_write_api_user


@pytest.fixture(scope='package')
def unauthorized_api_client():
    return APICaller()


@pytest.fixture(scope='package')
def readonly_api_client():
    return APICaller(user=readonly_api_user)


@pytest.fixture(scope='package')
def read_write_api_client():
    return APICaller(user=read_write_api_user)
