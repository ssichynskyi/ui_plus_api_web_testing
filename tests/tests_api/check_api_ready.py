"""This is a pre-requisite test for all API tests"""

import pytest

from tests.conftest import unauthorized_api_client


# ToDo: implement a marker which stop further test execution in this package on failure of this test
def check_api_server_responds(unauthorized_api_client):
    resp = unauthorized_api_client.get('')
    assert resp.status_code == 200
