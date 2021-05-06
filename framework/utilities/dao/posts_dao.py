from datetime import datetime
from framework.utilities.dao.base_dao import BaseDAO


class PostDao(BaseDAO):
    TABLE = 'wp_posts'
    ID = 'ID'
    TITLE = 'post_title'
    NAME = 'post_name'
    GUID = 'guid'
    DATE = 'post_date'
    DATE_GMT = 'post_date_gmt'
    AUTHOR_ID = 'post_author'
    TYPE = 'post_type'
    FILE_TYPE = 'post_mime_type'

    def __init__(self, data_dict):
        """Data access object (DAO) for posts/products/pages

        Args:
            data_dict: dict of elements sent by DB where keys = col, values = cells
        """
        super().__init__(data_dict)

    @property
    def title(self) -> str:
        return self._dict[self.TITLE]

    @property
    def id(self) -> id:
        return self._dict[self.ID]

    @property
    def name(self) -> str:
        return self._dict[self.NAME]

    @property
    def guid(self) -> str:
        return self._dict[self.GUID]

    @property
    def date(self) -> datetime:
        return self._dict[self.DATE]

    @property
    def date_gmt(self) -> datetime:
        return self._dict[self.DATE_GMT]

    @property
    def author_id(self) -> int:
        return self._dict[self.AUTHOR_ID]

    @property
    def type(self) -> str:
        return self._dict[self.TYPE]

    @property
    def file_type(self) -> str:
        return self._dict[self.FILE_TYPE]
