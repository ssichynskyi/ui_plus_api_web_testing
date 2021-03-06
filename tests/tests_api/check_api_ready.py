"""This is a pre-requisite test for all API tests"""

import pytest


@pytest.mark.environment
def check_woo_api_server_responds(unauthorized_woo_api_client):
    resp = unauthorized_woo_api_client.get('')
    assert resp.status_code == 200, unauthorized_woo_api_client.get_http_error_message(resp)


@pytest.mark.environment
def check_wp_api_server_responds(unauthorized_wp_api_client):
    resp = unauthorized_wp_api_client.get('')
    assert resp.status_code == 200, unauthorized_wp_api_client.get_http_error_message(resp)
