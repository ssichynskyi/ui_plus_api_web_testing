from framework.ui.elements.base import Item, UIElement, HyperLink, TextLabel, EditableTextField
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.actions.key_actions as key_actions


class SiteHeader(Item):
    SITE_TITLE = '#masthead > div.col-full > div.site-branding > h1 > a'
    SITE_DESCR = '#masthead > div.col-full > div.site-branding > p'

    def __init__(self, infra):
        super().__init__(infra)

    @property
    def site_title(self):
        return HyperLink(self.do, self.SITE_TITLE)

    @property
    def site_description(self):
        return TextLabel(self.do, self.SITE_DESCR)


class NavigationMenu(Item):
    LOCATOR = '#site-navigation > div.menu > ul.nav-menu'

    def __init__(self, infra):
        super().__init__(infra)

    @property
    def home(self):
        LOCATOR_EXT = 'li:nth-child(1)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def cart(self):
        LOCATOR_EXT = 'li:nth-child(2)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def checkout(self):
        LOCATOR_EXT = 'li:nth-child(3)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def my_account(self):
        LOCATOR_EXT = 'li:nth-child(4)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def sample_page(self):
        LOCATOR_EXT = 'li:nth-child(5)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def shop(self):
        LOCATOR_EXT = 'li:nth-child(6)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))


class SearchField(EditableTextField):
    LOCATOR = '#woocommerce-product-search-field-0'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)

    def submit(self):
        self.do.submit(self.LOCATOR)
