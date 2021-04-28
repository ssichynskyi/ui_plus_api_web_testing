from typing import Optional
from framework.utilities.db_connector import db


class TooManyDatabaseEntries(Exception):
    pass


class TooFewDatabaseEntries(Exception):
    pass


class BasicCustomerDAO:

    basic_query = f"SELECT * FROM wp_users WHERE %c;"

    @staticmethod
    def _get(query):
        results = db.execute_sql(query)
        if len(results) > 1:
            msg = f'Too many results. Found {len(results)} entries, 1 expected. SQL: {query}'
            raise TooManyDatabaseEntries(msg)
        elif len(results) == 0:
            msg = f'No entries found, 1 expected. SQL: {query}'
            raise TooFewDatabaseEntries(msg)
        else:
            return results[0]

    def __new__(cls, *args, **kwargs):
        if not (args or kwargs):
            return None
        else:
            return super().__new__(cls)

    def __init__(
            self,
            user_id: Optional[int] = None,
            username: Optional[str] = None,
            email: Optional[str] = None,
            **kwargs
    ):
        kwa = dict()
        if user_id:
            kwa['id'] = user_id
        if username:
            kwa['user_login'] = username
        if email:
            kwa['user_email'] = email
        kwargs.update(kwa)
        params = [f'{k}=\'{str(v)}\'' for k, v in kwargs.items()]
        where_params = ' and '.join(params)
        self.query = self.basic_query.replace('%c', where_params)
        self._dict = self._get(self.query)

    @property
    def username(self):
        return self._dict['user_login']

    @property
    def id(self):
        return self._dict['ID']

    @property
    def email(self):
        return self._dict['user_email']

    @property
    def username(self):
        return self._dict['user_login']

    @property
    def registered(self):
        return self._dict['user_registered']
