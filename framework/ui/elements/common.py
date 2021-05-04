from framework.ui.elements.base import (
    Item,
    UIElement,
    HyperLink,
    TextLabel,
    EditableTextField,
    ListOfDynamicElements,
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
    LOCATOR = '#woocommerce-product-search-field-0'

    def __init__(self, infra):
        super().__init__(infra, self.LOCATOR)

    def submit(self):
        """Simulates pressing of the ENTER key"""
        self.do.submit(self.locator)


class ProductImage(UIElement):
    LOCATOR = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > img'

    def __init__(self, infra, locator: str):
        super().__init__(infra, locator)


class ProductTitle(HyperLink):
    LOCATOR = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > h2.woocommerce-loop-product__title'

    def __init__(self, infra, locator: str):
        super().__init__(infra, locator)


class CurrencySymbol(HyperLink):
    LOCATOR = 'span.woocommerce-Price-currencySymbol'

    def __init__(self, infra, external_locator: str):
        super().__init__(infra, ' > '.join((external_locator, self.LOCATOR)))


class Price(HyperLink):
    LOCATOR = 'span > bdi'

    def __init__(self, infra, external_locator: str):
        super().__init__(infra, ' > '.join((external_locator, self.LOCATOR)))

    @property
    def currency(self):
        return CurrencySymbol(self.do, self.locator)


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


class AddToCartButton(ButtonWithText):
    LOCATOR = 'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart'

    def __init__(self, infra, locator: str):
        super().__init__(infra, locator)


class ProductListElement(DynamicListElement):
    LOCATOR = '#main > ul > li'

    def __init__(self, infra):
        super().__init__(infra)
        self.image_locator = ProductImage.LOCATOR
        self.title_locator = ProductTitle.LOCATOR
        self.price_locator = PriceLine.LOCATOR
        self.add_to_cart_button_locator = AddToCartButton.LOCATOR

    @property
    def member_locators(self) -> list:
        return [
            'image_locator',
            'add_to_cart_button_locator',
            'title_locator',
            'price_locator'
        ]

    @property
    def image(self):
        return ProductImage(self.do, self.image_locator)

    @property
    def title(self):
        return ProductTitle(self.do, self.title_locator)

    @property
    def price(self):
        return PriceLine(self.do, self.price_locator)

    @property
    def add_to_cart_button(self):
        return AddToCartButton(self.do, self.add_to_cart_button_locator)


class ProductList(ListOfDynamicElements):

    def __init__(self, infra):
        super().__init__(infra, ProductListElement)

    def get_by_title(self, value):
        return self.get_by_property_value('title.text', value)
