import pytest

from seleniumbase import BaseCase
from framework.ui.pages.common import MainPage
from framework.ui.elements.common import ProductList


class TestMainPage(BaseCase):
    """Test cases related to login-logout procedures"""

    @pytest.mark.skip
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

    def test_product_list(self):
        page = MainPage(self)
        page.open()
        page.navigation_menu.shop.click()
        product_list = ProductList(self)
        beanie = product_list.get_by_title('Beanie')
        assert beanie.title.text == 'Beanie'
        assert beanie.price.former.text == '€20,00'
        assert beanie.price.actual.text == '€18,00'
        beanie.add_to_cart_button.click()
        print('')
