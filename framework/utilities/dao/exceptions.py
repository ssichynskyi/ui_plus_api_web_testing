"""Database data retrieval errors"""


class TooManyDatabaseEntries(Exception):
    pass


class TooFewDatabaseEntries(Exception):
    pass


class IncorrectSQLQuery(Exception):
    pass
