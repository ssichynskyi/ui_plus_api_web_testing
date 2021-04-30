import pymysql
from typing import Union, Dict, List, Tuple
from framework.base import LoggingObject
from framework.utilities.credentials_helper import BasicAuthUser, db_user
from framework.utilities.env_config import db_host_config


class DB(LoggingObject):
    def __init__(self, user: BasicAuthUser):
        """Database helper

        Provides connection and query execution wrapper

        Args:
            user: user object

        """
        super().__init__(__name__)
        self._connection_params = {
            'user': user.login,
            'password': user.password,
            'host': db_host_config['url'],
            'port': db_host_config['port'],
            'database': db_host_config['schema'],
            'cursorclass': pymysql.cursors.DictCursor
        }

    def execute_sql(self, sql: str, args: Union[Dict, List, Tuple] = None) -> List[Dict]:
        """Executes given sql with arguments

        Args:
            sql: an SQL query. Placeholder for args shall be
            args: tuple, list or dict to be inserted in sql

        Returns:
            List of Dicts where:
                - list member is row
                - Dict keys: columns names
                - Dict values: row X col value

        """
        connection = pymysql.connect(**self._connection_params)
        with connection:
            with connection.cursor() as cursor:
                self.logger.info(f'Sending SQL query: {sql}')
                cursor.execute(sql, args)
                res = cursor.fetchall()
        return res


db = DB(db_user)
"""data base connector object. Import for manipulations"""
