from framework.utilities.db_connector import db
from framework.utilities.dao.exceptions import (
    TooManyDatabaseEntries,
    TooFewDatabaseEntries,
    IncorrectSQLQuery
)


class BaseDAO:

    basic_query = f"SELECT * FROM %t WHERE %c;"

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

    def __init__(self, table: str, **kwargs):
        """Base class for all Data Access Objects (DAO)

        Args:
            **kwargs: optional keyword arguments
        """
        if not isinstance(table, str) or not str:
            msg = f'type: {type(table)}, value: {table}'
            msg = f'Table name must be a meaningful string, given: {msg}'
            raise ValueError(msg)
        params = [f'{k}=\'{str(v)}\'' for k, v in kwargs.items()]
        where_params = ' and '.join(params)
        self.query = self.basic_query.replace('%t', table).replace('%c', where_params)
        if not kwargs:
            msg = f'Result query: {self.query}'
            msg = f' e.g. those given after SQL WHERE statement. {msg}'
            msg = f'SQL query shall contain at least one search criterion {msg}'
            raise IncorrectSQLQuery(msg)
        self._dict = self._get(self.query)
