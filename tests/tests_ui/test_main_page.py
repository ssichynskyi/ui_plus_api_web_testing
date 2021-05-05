import pytest

from selenium.common.exceptions import NoSuchElementException
from seleniumbase import BaseCase
from framework.ui.pages.common import MainPage
from framework.ui.elements.common import ProductList, SearchResultList


class TestMainPage(BaseCase):
    """Test cases related to login-logout procedures"""

    @pytest.mark.critical
    @pytest.mark.slow
    def test_main_page_content(self):
        # ToDo add assertions
        page = MainPage(self)
        page.open()
        self.assertEqual("Super website", page.header.site_title.text)
        self.assertEqual("Just another WordPress site", page.header.site_description.text)
        page.header.site_title.click()
        page.navigation_menu.shop.click()
        page.navigation_menu.sample_page.click()
        page.navigation_menu.cart.click()
        page.navigation_menu.home.click()

    @pytest.mark.critical
    @pytest.mark.slow
    def test_product_list_and_cart(self):
        # ToDo: add similar test with random element from DB
        page = MainPage(self)
        page.open()
        page.navigation_menu.shop.click()
        assert page.cart.total_price.text == '€0,00'
        assert page.cart.number_of_items.text == '0 items'
        product_list = ProductList(self)
        beanie = product_list.get_by_title('Beanie')
        assert beanie.title.text == 'Beanie'
        assert beanie.price.former.text == '€20,00'
        assert beanie.price.actual.text == '€18,00'
        self.set_default_timeout(2)
        with self.assertRaises(NoSuchElementException):
            beanie.view_cart_button.text
        self.reset_default_timeout()
        beanie.add_to_cart_button.click()
        # timeout is required because UI element is already
        # available but it takes time to update it
        self.sleep(1)
        assert page.cart.total_price.text == '€18,00'
        assert page.cart.number_of_items.text == '1 item'
        assert beanie.view_cart_button.text == 'View cart'
        beanie.add_to_cart_button.click()
        self.sleep(1)
        assert page.cart.total_price.text == '€36,00'
        assert page.cart.number_of_items.text == '2 items'

    @pytest.mark.major
    @pytest.mark.slow
    def test_global_search(self):
        page = MainPage(self)
        page.open()
        # search with only 1 result
        page.search.search_field.add_text('album')
        page.search.search_field.submit()
        # search with several results
        page.search.search_field.clear()
        page.search.search_field.add_text('beanie')
        page.search.search_field.submit()
        search_results = SearchResultList(self)
        assert search_results.header.text == 'Search Results for: beanie'
        album = search_results.get_by_title('Beanie with Logo')
        assert album.title.text == 'Beanie with Logo'
        description = (
            'Pellentesque habitant morbi tristique senectus et netus et '
            'malesuada fames ac turpis egestas. Vestibulum tortor quam, '
            'feugiat vitae, ultricies eget, tempor sit amet, ante. '
            'Donec eu libero sit amet quam egestas semper. '
            'Aenean ultricies mi vitae est. Mauris placerat eleifend leo.'
        )
        assert album.description.text == description
