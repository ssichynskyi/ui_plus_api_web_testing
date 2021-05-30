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
        """Header of the website with title, description, etc.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)

    @property
    def site_title(self) -> HyperLink:
        return HyperLink(self.do, self.SITE_TITLE)

    @property
    def site_description(self) -> TextLabel:
        return TextLabel(self.do, self.SITE_DESCR)


class NavigationMenu(Item):
    LOCATOR = '#site-navigation > div.menu > ul.nav-menu'

    def __init__(self, infra):
        """Navigation menu. Extends Item.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)

    @property
    def home(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(1)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def cart(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(2)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def checkout(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(3)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def my_account(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(4)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def sample_page(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(5)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))

    @property
    def shop(self) -> HyperLink:
        LOCATOR_EXT = 'li:nth-child(6)'
        return HyperLink(self.do, ' > '.join((self.LOCATOR, LOCATOR_EXT)))


class SearchField(EditableTextField):

    def __init__(self, infra, locator):
        """Search field extends Editable Text Field.

        Args:
            infra: Seleniumbase BaseCase object
            locator: own locator

        """
        super().__init__(infra, locator)

    def submit(self):
        """Simulates pressing of the ENTER key"""
        self.do.submit(self.locator)


class SearchProductField(SearchField):
    LOCATOR = '#woocommerce-product-search-field-0'

    def __init__(self, infra):
        """Search product field - shortcut to SearchField with predefined locator.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, self.LOCATOR)


class SearchWidget(UIElement):
    LOCATOR = '#search-2 > form.search-form'

    def __init__(self, infra):
        """Widget that incorporates a search field.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, self.LOCATOR)

    @property
    def user_hint(self) -> TextLabel:
        """Spans when mouse over."""
        LOCATOR_EXT = 'label > span.screen-reader-text'
        return TextLabel(self.do, ' > '.join((self.locator, LOCATOR_EXT)))

    @property
    def search_field(self) -> SearchField:
        LOCATOR_EXT = 'label > input.search-field'
        return SearchField(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class CurrencySymbol(HyperLink):
    LOCATOR = 'span.woocommerce-Price-currencySymbol'

    def __init__(self, infra, external_locator: str):
        super().__init__(infra, ' > '.join((external_locator, self.LOCATOR)))


class Price(HyperLink):
    LOCATOR = 'span > bdi'

    def __init__(self, infra, external_locator: str, own_locator: str = None):
        """Price UI element. Extends Hyperlink with currency field.

        Args:
            infra: Seleniumbase BaseCase object
            external_locator: locator for container of this widget
            own_locator: locator of thi widget
        """
        if own_locator is None:
            own_locator = self.LOCATOR
        super().__init__(infra, ' > '.join((external_locator, own_locator)))

    @property
    def currency(self) -> CurrencySymbol:
        return CurrencySymbol(self.do, self.locator)


class CartContents(UIElement):
    LOCATOR = '#site-header-cart > li > a.cart-contents'

    def __init__(self, infra):
        """Contents of the shopping cart.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, self.LOCATOR)

    @property
    def total_price(self) -> Price:
        LOCATOR_EXT = 'span.woocommerce-Price-amount.amount'
        return Price(self.do, self.locator, LOCATOR_EXT)

    @property
    def number_of_items(self) -> HyperLink:
        LOCATOR_EXT = 'span.count'
        return HyperLink(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class PriceLine(HyperLink):
    LOCATOR = 'a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > span.price'

    def __init__(self, infra, locator: str):
        """Price line which incorporates former and actual price

        Args:
            infra: Seleniumbase BaseCase object
            locator: own locator

        """
        super().__init__(infra, locator)

    @property
    def former(self) -> Price:
        """Entry with the previous / strikethrough price of the item."""
        LOCATOR_EXT = 'del'
        return Price(self.do, ' > '.join((self.locator, LOCATOR_EXT)))

    @property
    def actual(self) -> Price:
        """Entry with the actual price of the item."""
        LOCATOR_EXT = 'ins'
        return Price(self.do, ' > '.join((self.locator, LOCATOR_EXT)))


class BasePost(DynamicListElement):
    LOCATOR = '#main > article'
    TITLE = 'header > h2 > a'
    DESCRIPTION = 'div > p'

    def __init__(self, infra):
        """Basic class for the post widget.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)
        self.title_locator = self.TITLE
        self.description_locator = self.DESCRIPTION

    @property
    def member_locators(self) -> list:
        return [
            'title_locator',
            'description_locator'
        ]

    @property
    def title(self) -> HyperLink:
        return HyperLink(self.do, self.title_locator)

    @property
    def description(self) -> TextLabel:
        return TextLabel(self.do, self.description_locator)


class PostWithImage(BasePost):
    LOCATOR = '#main > article'
    IMAGE = 'div > img'

    def __init__(self, infra):
        """Variance of a post with image. Extends BasePost.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)
        self.image_locator = self.IMAGE

    @property
    def member_locators(self) -> list:
        properties = super().member_locators
        properties.extend(['image_locator'])
        return properties

    @property
    def image(self) -> UIElement:
        return UIElement(self.do, self.image_locator)


class ProductListElement(PostWithImage):
    LOCATOR = '#main > ul > li'
    IMAGE = 'a > img'
    TITLE = 'a > h2.woocommerce-loop-product__title'
    ADD_TO_CART = 'a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart'
    VIEW_CART = 'a.added_to_cart.wc-forward'

    def __init__(self, infra):
        """Element of the list of products. Extends PostWithImage.

        By its nature Woo Commerce implements products as posts.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)
        self.image_locator = self.IMAGE
        self.title_locator = self.TITLE
        self.price_locator = PriceLine.LOCATOR
        self.add_to_cart_button_locator = self.ADD_TO_CART
        self.view_cart_button_locator = self.VIEW_CART

    @property
    def member_locators(self) -> list:
        properties = super().member_locators
        properties.extend([
            'add_to_cart_button_locator',
            'price_locator',
            'view_cart_button_locator'
        ])
        return properties

    @property
    def price(self) -> PriceLine:
        return PriceLine(self.do, self.price_locator)

    @property
    def add_to_cart_button(self) -> ButtonWithText:
        return ButtonWithText(self.do, self.add_to_cart_button_locator)

    @property
    def view_cart_button(self) -> ButtonWithText:
        return ButtonWithText(self.do, self.view_cart_button_locator)


class ProductList(DynamicList):

    def __init__(self, infra):
        """Dynamic list of products. Extends DynamicList.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, ProductListElement)

    def get_by_title(self, value: str) -> ProductListElement:
        """Gets element by its title. Shortcut for parent method.

        Args:
            value: title as a string

        Returns:
            List Element
        """
        return self.get_by_property_value('title.text', value)


class Post(BasePost):
    POSTED_ON = 'header > span.posted-on > a > time'
    POSTED_BY = 'header > span.post-author > a'
    COMMENTS_NUMBER = 'header > span.post-comments > a'

    def __init__(self, infra):
        """Ordinary user's post. Not a product. Extends BasePost.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra)
        self.posted_on_locator = self.POSTED_ON
        self.posted_by_locator = self.POSTED_BY
        self.comments_number_locator = self.COMMENTS_NUMBER

    @property
    def member_locators(self) -> list:
        properties = super().member_locators
        properties.extend([
            'posted_on_locator',
            'posted_by_locator',
            'comments_number_locator'
        ])
        return properties

    @property
    def posted_on(self) -> HyperLink:
        return HyperLink(self.do, self.posted_on_locator)

    @property
    def posted_by(self) -> HyperLink:
        return HyperLink(self.do, self.posted_by_locator)

    @property
    def number_of_comments(self) -> TextLabel:
        return TextLabel(self.do, self.comments_number_locator)


class PostsList(DynamicList):

    def __init__(self, infra):
        """List of ordinary user posts. Not products."""
        super().__init__(infra, Post)


class SearchResultList(DynamicList):

    def __init__(self, infra):
        """List of the results obtained by search. Not product search.

        These lists have differences although both can return products as
        elements of the search result list.

        Args:
            infra: Seleniumbase BaseCase object

        """
        super().__init__(infra, PostWithImage)

    @property
    def header(self) -> TextLabel:
        LOCATOR = '#main > header'
        return TextLabel(self.do, LOCATOR)

    def get_by_title(self, value: str) -> PostWithImage:
        """Gets element by its title. Shortcut for parent method.

        Args:
            value: title as a string

        Returns:
            Element of the list as PostWithImage class object

        """
        return self.get_by_property_value('title.text', value)
