from datetime import datetime
from framework.utilities.dao.base_dao import BaseDAO


class CustomerDAO(BaseDAO):
    TABLE = 'wp_users'
    ID = 'ID'
    LOGIN = 'user_login'
    EMAIL = 'user_email'
    REG_DATE = 'user_registered'

    def __init__(self, data_dict):
        """Data access object (DAO) for posts/products/pages

        Args:
            data_dict: dict of elements sent by DB where keys = col, values = cells
        """
        super().__init__(data_dict)

    @property
    def username(self) -> str:
        return self._dict[self.LOGIN]

    @property
    def id(self) -> int:
        return self._dict[self.ID]

    @property
    def email(self) -> str:
        return self._dict[self.EMAIL]

    @property
    def registration_date(self) -> datetime:
        return self._dict[self.REG_DATE]
