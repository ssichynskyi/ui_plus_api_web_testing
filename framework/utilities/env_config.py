# -*- coding: utf-8 -*-
"""ToDo: rework reading environment params from command line"""
import os
import yaml

from pathlib import Path
from framework.utilities.dict_merger import merge_dicts


CONFIG_PATH = 'config'
"""path to config files folder from project root"""


class ConfigParser:
    """Extracts the data from the configuration file given"""
    def __new__(cls, path):
        with open(path, 'r') as f:
            contents = f.read()
            return yaml.safe_load(contents)


__hosts_config = ConfigParser(Path(os.environ['PROJECT_PATH']).joinpath(CONFIG_PATH, 'hosts.yaml'))
__hosts_local_config = ConfigParser(Path(os.environ['PROJECT_PATH']).joinpath(CONFIG_PATH, 'hosts_local.yaml'))
__hosts_config = merge_dicts(__hosts_config, __hosts_local_config)
api_host_config = __hosts_config['API_HOSTS'][os.environ['ENV']]
db_host_config = __hosts_config['DB_HOSTS'][os.environ['ENV']]
