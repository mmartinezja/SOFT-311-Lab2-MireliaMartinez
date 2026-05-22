class CartPage:

    def __init__(self, page):

        self.page = page

        self.all_products_button = page.locator(
            '[data-testid="header-menu-all-products"]'
        )

        self.product_card = page.locator(
            '[data-testid="all-products-header"]'
        ).first

        self.add_to_cart_button = page.locator(
            '[data-testid="add-to-cart-button"]'
        )

        self.cart_icon = page.locator(
            '[data-testid="header-cart-icon"]'
        )

        self.cart_drawer = page.locator(
            '[data-testid="cart-drawer"]'
        )

    def go_to_home(self):

        self.page.goto(
            "https://storedemo.testdino.com",
            wait_until="networkidle"
        )

    def click_all_products(self):

        self.all_products_button.click()

    def click_product(self):

        self.product_card.click()

    def click_add_to_cart(self):

        self.add_to_cart_button.click()

    def open_cart(self):

        self.cart_icon.click()

    def is_cart_visible(self):

        return self.cart_drawer.is_visible()