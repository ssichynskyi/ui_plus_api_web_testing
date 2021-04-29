"""This is a pre-requisite test for all API tests"""

import pytest

from tests.conftest import unauthorized_api_client


@pytest.mark.environment
def check_api_server_responds(unauthorized_api_client):
    resp = unauthorized_api_client.get('')
    assert resp.status_code == 200
