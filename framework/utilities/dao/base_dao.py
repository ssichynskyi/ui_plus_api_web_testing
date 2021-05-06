from framework.base import LoggingObject


class BaseDAO(LoggingObject):
    def __init__(self, data_dict: dict):
        """Base class for DAO objects

        Args:
            data_dict: dict of elements sent by DB where keys = col, values = cells

        """
        super().__init__()
        self._dict = data_dict
