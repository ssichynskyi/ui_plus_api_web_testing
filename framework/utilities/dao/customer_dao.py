from typing import Optional
from framework.utilities.dao.base_dao import BaseDAO


class BasicCustomerDAO(BaseDAO):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(
            self,
            user_id: Optional[int] = None,
            username: Optional[str] = None,
            email: Optional[str] = None,
            **kwargs
    ):
        """DAO for the user/customer

        Args:
            user_id: ID of the user
            username: user login
            email: user email
            **kwargs: optional search kwargs follow after WHERE in SQL

        """
        kwa = dict()
        if user_id:
            kwa['id'] = user_id
        if username:
            kwa['user_login'] = username
        if email:
            kwa['user_email'] = email
        kwargs.update(kwa)
        super().__init__('wp_users', **kwargs)

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
    def registration_date(self):
        return self._dict['user_registered']
