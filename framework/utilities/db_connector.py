import pymysql
from typing import Union, Dict, List, Tuple
from framework.utilities.credentials_helper import BasicAuthUser
from framework.utilities.env_config import db_host_config


class DB:
    def __init__(self, user: BasicAuthUser):
        """Database helper

        Provides connection and query execution wrapper

        Args:
            user: user object

        """
        self._connection = pymysql.connect(
            user=user.login,
            password=user.password,
            host=db_host_config['url'],
            port=db_host_config['port'],
            database=db_host_config['schema'],
            cursorclass=pymysql.cursors.DictCursor
        )

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
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(sql, args)
                res = cursor.fetchall()
        return res
