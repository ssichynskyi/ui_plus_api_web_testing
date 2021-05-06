from typing import Optional
from framework.utilities.dao.base_dao import BaseDAO


class BasicPostDAO(BaseDAO):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(
            self,
            post_title: Optional[str] = None,
            post_name: Optional[str] = None,
            guid: Optional[str] = None,
            post_id: Optional[int] = None,
            **kwargs
    ):
        """DAO for posts and media items

        Args:
            post_title: the name of the post. For media attachment is equal to post_name
            post_name: the name of the post. For media attachment is equal to post_title
            guid: url to the resource
            **kwargs: optional keyword arguments
        """
        kwa = dict()
        if post_title:
            kwa['post_title'] = post_title
        if post_name:
            kwa['post_name'] = post_name
        if guid:
            kwa['guid'] = guid
        if post_id:
            kwa['ID'] = post_id
        kwargs.update(kwa)
        super().__init__('wp_posts', **kwargs)

    @property
    def title(self):
        return self._dict['post_title']

    @property
    def id(self):
        return self._dict['ID']

    @property
    def name(self):
        return self._dict['post_name']

    @property
    def guid(self):
        return self._dict['guid']

    @property
    def date(self):
        return self._dict['post_date']

    @property
    def date_gmt(self):
        return self._dict['post_date_gmt']

    @property
    def author_id(self):
        return self._dict['author_id']

    @property
    def type(self):
        return self._dict['post_type']

    @property
    def file_type(self):
        return self._dict['post_mime_type']
