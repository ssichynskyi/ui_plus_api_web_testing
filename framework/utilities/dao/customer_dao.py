from typing import Dict, List, Union
from framework.utilities.db_connector import db


class TooManyResultsException(Exception):
    def __init__(self, msg):
        super(TooManyResultsException, self).__init__(msg)


class CustomerDAO:
    def __init__(self):
        self._basic_query = f"SELECT * FROM wp_users WHERE %c=%s;"

    def get_by(self, col_name: str, col_value: str) -> List[Dict]:
        """Get user by column name and value

        Args:
            col_name: name of the column
            col_value: value of the column

        Returns:
            List of Dicts where:
                - list member is row
                - Dict keys: columns names
                - Dict values: row X col value

        """
        query = self._basic_query.replace('%c', col_name)
        return db.execute_sql(query, [col_value])

    def _get_user_unique(self, col_name, value):
        """Same as get_by, but for unique entries only"""
        results = self.get_by(col_name, value)
        if len(results) > 1:
            msg = f'Unexpected output. Found {len(results)} entries, 1 expected'
            raise TooManyResultsException(msg)
        elif len(results) == 0:
            return None
        else:
            return results[0]

    def get_by_username(self, username: str) -> Union[Dict, None]:
        """Get user by username

        Args:
            username: username -> user_nicename (in db)

        Returns:
            User as Dict or None

        Raises:
            TooManyResultsException
        """
        return self._get_user_unique('user_nicename', username)

    def get_by_email(self, email: str) -> Union[Dict, None]:
        """Get user by email

        Args:
            email: email -> user_email (in db)

        Returns:
            User as Dict or None

        Raises:
            TooManyResultsException
        """
        return self._get_user_unique('user_email', email)
