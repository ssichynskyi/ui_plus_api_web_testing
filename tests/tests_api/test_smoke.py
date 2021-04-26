from pytest import mark

from framework.utilities.api_caller import APICaller
from framework.utilities.credentials_helper import readonly_api_user, read_write_api_user
from framework.utilities.fake_data import generate_fake_user


def test_create_user_impossible_with_readonly_access():
    api_caller = APICaller(user=readonly_api_user)
    resp = api_caller.post('customers', generate_fake_user())
    assert resp.status_code == 401


def test_create_user():
    api_caller = APICaller(user=read_write_api_user)
    resp = api_caller.post('customers', generate_fake_user())
    assert resp.status_code == 201
