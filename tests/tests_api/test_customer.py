import pytest

from faker import Faker
from data_collection.api.data_models.woo_commerce.v3 import CustomerResponse, ErrorResponse
from framework.utilities.dao.customer_dao import CustomerDAO
from framework.utilities.dao.dao_helpers import generate_dao_objects
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
    users = generate_dao_objects(CustomerDAO, CustomerDAO.TABLE,
                                 filter_criteria={CustomerDAO.LOGIN: customer['username']})
    assert len(users) == 0


@pytest.mark.major
def test_create_user_impossible_with_readonly_access(
        readonly_woo_api_client,
        customer
):
    resp = readonly_woo_api_client.post('customers', customer)
    assert resp.status_code == 401
    ErrorResponse(**resp.json())
    users = generate_dao_objects(CustomerDAO, CustomerDAO.TABLE,
                                 filter_criteria={CustomerDAO.LOGIN: customer['username']})
    assert len(users) == 0


@pytest.mark.critical
@pytest.mark.slow
def test_create_get_and_delete_user(
        read_write_woo_api_client,
        readonly_woo_api_client,
        customer
):
    # CREATE CUSTOMER
    resp = read_write_woo_api_client.post('customers', customer)
    assert resp.status_code == 201, read_write_woo_api_client.get_http_error_message(resp)
    CustomerResponse(**resp.json())
    users = generate_dao_objects(CustomerDAO, CustomerDAO.TABLE,
                                 filter_criteria={CustomerDAO.LOGIN: customer['username']})
    assert len(users) == 1

    # GET CUSTOMER by readonly
    user_id = resp.json()['id']
    resp = read_write_woo_api_client.get(f'customers/{user_id}')
    assert resp.status_code == 200, read_write_woo_api_client.get_http_error_message(resp)
    CustomerResponse(**resp.json())

    # UPDATE CUSTOMER
    new_email = Faker().ascii_free_email()
    resp = read_write_woo_api_client.put(f'customers/{user_id}', {'email': new_email})
    assert resp.status_code == 200, read_write_woo_api_client.get_http_error_message(resp)
    CustomerResponse(**resp.json())
    users_in_db = generate_dao_objects(CustomerDAO, CustomerDAO.TABLE,
                                       filter_criteria={CustomerDAO.LOGIN: customer['username']})
    assert len(users_in_db) == 1
    assert users_in_db[0].email == new_email

    # DELETE CUSTOMER
    resp = read_write_woo_api_client.delete(f'customers/{user_id}', params={'force': 'true'})
    assert resp.status_code == 200, read_write_woo_api_client.get_http_error_message(resp)
    CustomerResponse(**resp.json())
    users = generate_dao_objects(CustomerDAO, CustomerDAO.TABLE,
                                 filter_criteria={CustomerDAO.LOGIN: customer['username']})
    assert len(users) == 0
