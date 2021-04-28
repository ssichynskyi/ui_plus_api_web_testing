"""This is a pre-requisite test for all tests

It tests if AUT and DB are up and running
"""
import pytest

from framework.utilities.env_config import api_host_config, db_host_config
from framework.verificators.connection_verifier import assert_connection


# ToDo: implement a marker which stop further test execution on failure of this test
def check_api_server_connection():
    assert_connection(api_host_config['ip'], api_host_config['port'])


def check_db_connection():
    assert_connection(db_host_config['ip'], db_host_config['port'])
