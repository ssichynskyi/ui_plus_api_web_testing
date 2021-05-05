from framework.ui.elements.base import (
    Item,
    UIElement,
    HyperLink,
    TextLabel,
    EditableTextField,
    DynamicList,
    ButtonWithText,
    DynamicListElement
)


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

    def __init__(self, infra, locator):
        super().__init__(infra, locator)

    def submit(self):
        """Simulates pressing of the ENTER key"""
        self.do.submit(self.locator)


class SearchProductField(SearchField):
    LOCATOR = '#woocommerce-product-search-field-0'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)


class SearchWidget(UIElement):
    LOCATOR = '#search-2 > form.search-form'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)

    # @property
    # def default_entry(self):
    #     LOCATOR_EXT = 'label > input.search-field'
    #     return TextLabel(self.do, ' > '.join((self.locator, LOCATOR_EXT)))

    @property
    def user_hint(self):
        """Spans when mouse over"""
        LOCATOR_EXT = 'label > span.screen-reader-text'
        return TextLabel(self.do, ' > '.join((self.locator, LOCATOR_EXT)))

    @property
    def search_field(self):
        LOCATOR_EXT = 'label > input.search-field'
        return SearchField(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class CurrencySymbol(HyperLink):
    LOCATOR = 'span.woocommerce-Price-currencySymbol'

    def __init__(self, infra, external_locator: str):
        super().__init__(infra, ' > '.join((external_locator, self.LOCATOR)))


class Price(HyperLink):
    LOCATOR = 'span > bdi'

    def __init__(self, infra, external_locator: str, own_locator: str = None):
        if own_locator is None:
            own_locator = self.LOCATOR
        super().__init__(infra, ' > '.join((external_locator, own_locator)))

    @property
    def currency(self):
        return CurrencySymbol(self.do, self.locator)


class CartContents(UIElement):
    LOCATOR = '#site-header-cart > li > a.cart-contents'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)

    @property
    def total_price(self):
        LOCATOR_EXT = 'span.woocommerce-Price-amount.amount'
        return Price(self.do, self.locator, LOCATOR_EXT)

    @property
    def number_of_items(self):
        LOCATOR_EXT = 'span.count'
        return HyperLink(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class PriceLine(HyperLink):
    LOCATOR = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > span.price'

    def __init__(self, infra, locator: str):
        super().__init__(infra, locator)

    @property
    def former(self):
        """Entry with the previous / strikethrough price of the item"""
        LOCATOR_EXT = 'del'
        return Price(self.do, ' > '.join((self.locator, LOCATOR_EXT)))

    @property
    def actual(self):
        """Entry with the actual price of the item"""
        LOCATOR_EXT = 'ins'
        return Price(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class ProductListElement(DynamicListElement):
    LOCATOR = '#main > ul > li'
    IMAGE = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > img'
    TITLE = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > h2.woocommerce-loop-product__title'
    ADD_TO_CART = 'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart'
    VIEW_CART = 'a.added_to_cart.wc-forward'

    def __init__(self, infra):
        super().__init__(infra)
        self.image_locator = self.IMAGE
        self.title_locator = self.TITLE
        self.price_locator = PriceLine.LOCATOR
        self.add_to_cart_button_locator = self.ADD_TO_CART
        self.view_cart_button_locator = self.VIEW_CART

    @property
    def member_locators(self) -> list:
        return [
            'image_locator',
            'add_to_cart_button_locator',
            'title_locator',
            'price_locator',
            'view_cart_button_locator'
        ]

    @property
    def image(self):
        return UIElement(self.do, self.image_locator)

    @property
    def title(self):
        return HyperLink(self.do, self.title_locator)

    @property
    def price(self):
        return PriceLine(self.do, self.price_locator)

    @property
    def add_to_cart_button(self):
        return ButtonWithText(self.do, self.add_to_cart_button_locator)

    @property
    def view_cart_button(self):
        return ButtonWithText(self.do, self.view_cart_button_locator)


class ProductList(DynamicList):

    def __init__(self, infra):
        super().__init__(infra, ProductListElement)

    def get_by_title(self, value: str) -> ProductListElement:
        return self.get_by_property_value('title.text', value)


class SearchResultListElement(DynamicListElement):
    LOCATOR = '#main > article'
    TITLE = 'header > h2 > a'
    IMAGE = 'div > img'
    DESCRIPTION = 'div > p'

    def __init__(self, infra):
        super().__init__(infra)
        self.title_locator = self.TITLE
        self.image_locator = self.IMAGE
        self.description_locator = self.DESCRIPTION

    @property
    def member_locators(self) -> list:
        return [
            'image_locator',
            'title_locator',
            'description_locator'
        ]

    @property
    def image(self):
        return UIElement(self.do, self.image_locator)

    @property
    def title(self):
        return HyperLink(self.do, self.title_locator)

    @property
    def description(self):
        return TextLabel(self.do, self.description_locator)


class SearchResultList(DynamicList):

    def __init__(self, infra):
        super().__init__(infra, SearchResultListElement)

    @property
    def header(self):
        LOCATOR = '#main > header'
        # 'h1', 'h1 > span'
        return TextLabel(self.do, LOCATOR)

    def get_by_title(self, value: str) -> SearchResultListElement:
        return self.get_by_property_value('title.text', value)
