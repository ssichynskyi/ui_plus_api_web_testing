import pytest

from faker import Faker
from data_collection.api.data_models.woo_commerce.v3 import CustomerResponse, ErrorResponse
from framework.utilities.dao.customer_dao import BasicCustomerDAO
from framework.utilities.dao.exceptions import TooFewDatabaseEntries
from framework.utilities.fake_data import generate_fake_user
from tests.conftest import unauthorized_woo_api_client, readonly_woo_api_client, read_write_woo_api_client


@pytest.fixture(scope="module")
def customer():
    return generate_fake_user()


@pytest.mark.major
def test_create_user_impossible_with_unauthorized(
        unauthorized_woo_api_client,
        customer
):
    resp = unauthorized_woo_api_client.post('customers', customer)
    assert resp.status_code == 401
    ErrorResponse(**resp.json())
    with pytest.raises(TooFewDatabaseEntries):
        BasicCustomerDAO(username=customer['username'])


@pytest.mark.major
def test_create_user_impossible_with_readonly_access(
        readonly_woo_api_client,
        customer
):
    resp = readonly_woo_api_client.post('customers', customer)
    assert resp.status_code == 401
    ErrorResponse(**resp.json())
    with pytest.raises(TooFewDatabaseEntries):
        BasicCustomerDAO(username=customer['username'])


@pytest.mark.critical
@pytest.mark.slow
def test_create_get_and_delete_user(
        read_write_woo_api_client,
        readonly_woo_api_client,
        customer
):
    # CREATE CUSTOMER
    resp = read_write_woo_api_client.post('customers', customer)
    assert resp.status_code == 201
    CustomerResponse(**resp.json())
    BasicCustomerDAO(username=customer['username'])

    # GET CUSTOMER by readonly
    user_id = resp.json()['id']
    resp = read_write_woo_api_client.get(f'customers/{user_id}')
    assert resp.status_code == 200
    CustomerResponse(**resp.json())

    # UPDATE CUSTOMER
    new_email = Faker().ascii_free_email()
    resp = read_write_woo_api_client.put(f'customers/{user_id}', {'email': new_email})
    assert resp.status_code == 200
    CustomerResponse(**resp.json())
    user_in_db = BasicCustomerDAO(username=customer['username'])
    assert user_in_db.email == new_email

    # DELETE CUSTOMER
    resp = read_write_woo_api_client.delete(f'customers/{user_id}', params={'force': 'true'})
    assert resp.status_code == 200
    CustomerResponse(**resp.json())
    with pytest.raises(TooFewDatabaseEntries):
        BasicCustomerDAO(username=customer['username'])
