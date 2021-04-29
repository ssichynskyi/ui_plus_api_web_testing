"""This is a pre-requisite test for all tests

It tests if AUT and DB are up and running
"""
import pytest

from framework.utilities.env_config import api_host_config, db_host_config
from framework.verificators.connection_verifier import assert_connection


@pytest.mark.environment
def check_api_server_connection():
    assert_connection(api_host_config['ip'], api_host_config['port'])


@pytest.mark.environment
def check_db_connection():
    assert_connection(db_host_config['ip'], db_host_config['port'])
