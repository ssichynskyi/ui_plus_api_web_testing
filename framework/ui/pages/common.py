from framework.ui.elements.common import (
    SiteHeader, NavigationMenu, SearchWidget, CartContents, SearchProductField, PostsList
)
from framework.ui.pages.base_page import BasePage

from tests.conftest import UI_URL


class MainPage(BasePage):
    URL = UI_URL

    def __init__(self, infra):
        super().__init__(infra)

    @property
    def header(self):
        return SiteHeader(self.do)

    @property
    def navigation_menu(self):
        return NavigationMenu(self.do)

    @property
    def search(self):
        return SearchWidget(self.do)

    @property
    def search_product(self):
        return SearchProductField(self.do)

    @property
    def cart(self):
        return CartContents(self.do)


class HomePage(MainPage):

    def __init__(self, infra):
        super().__init__(infra)

    @property
    def posts(self):
        return PostsList(self.do)
