from framework.ui.elements.common import SiteHeader, NavigationMenu, SearchField
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
    def search_field(self):
        return SearchField(self.do)
