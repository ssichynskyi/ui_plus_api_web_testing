# -*- coding: utf-8 -*-

import re
import os
import yaml

from pathlib import Path
from framework.utilities.dict_merger import merge_dicts


CONFIG_PATH = 'config'
"""path to config files folder from project root."""


class ConfigInconsistencyException(ValueError):
    pass


class ConfigParser:
    """Extracts the data from the configuration file given."""
    def __new__(cls, path):
        with open(path, 'r') as f:
            contents = f.read()
            return yaml.safe_load(contents)


def _ensure_ip_consistency(url: str, ip: str):
    ip_from_url = re.search(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
        url
    )
    if ip_from_url:
        ip_from_url = ip_from_url.group()
        if ip_from_url != ip:
            msg = (
                'Inconsistency in configuration file! IP address in url',
                f'{ip_from_url} is different from one in ip key {ip}'
            )
            raise ConfigInconsistencyException(' '.join(msg))


__hosts_config = ConfigParser(Path(os.environ['PROJECT_PATH']).joinpath(CONFIG_PATH, 'hosts.yaml'))
__hosts_local_config = ConfigParser(Path(os.environ['PROJECT_PATH']).joinpath(CONFIG_PATH, 'hosts_local.yaml'))
__hosts_config = merge_dicts(__hosts_config, __hosts_local_config)

_ensure_ip_consistency(
    __hosts_config['API_HOSTS'][os.environ['ENV']]['url'],
    __hosts_config['API_HOSTS'][os.environ['ENV']]['ip'],
)

_ensure_ip_consistency(
    __hosts_config['DB_HOSTS'][os.environ['ENV']]['url'],
    __hosts_config['DB_HOSTS'][os.environ['ENV']]['ip'],
)

api_host_config = __hosts_config['API_HOSTS'][os.environ['ENV']]
db_host_config = __hosts_config['DB_HOSTS'][os.environ['ENV']]
ui_host_config = __hosts_config['UI_HOSTS'][os.environ['ENV']]
