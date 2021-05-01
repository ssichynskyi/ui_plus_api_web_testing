from seleniumbase import BaseCase
from framework.ui.pages.common import MainPage


class TestMainPage(BaseCase):
    """Test cases related to login-logout procedures"""

    def test_main_page_content(self):
        page = MainPage(self)
        page.open()
        self.assertEqual("Super website", page.header.site_title.text)
        self.assertEqual("Just another WordPress site", page.header.site_description.text)
        page.header.site_title.click()
        page.navigation_menu.shop.click()
        page.navigation_menu.sample_page.click()
        page.navigation_menu.cart.click()
        page.navigation_menu.home.click()
        page.search_field.add_text('album')
        page.search_field.submit()
