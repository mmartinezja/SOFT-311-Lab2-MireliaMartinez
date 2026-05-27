class FavoritesPage:

    def __init__(self, page):

        self.page = page

        self.all_products_button = page.locator(
            '[data-testid="header-menu-all-products"]'
        )

        self.favorite_button = page.locator(
            '[data-testid="all-products-wishlist-button"]'
        ).first

    def go_to_home(self):

        self.page.goto(
            "https://storedemo.testdino.com",
            wait_until="networkidle"
        )

    def click_all_products(self):

        self.all_products_button.click()

    def click_favorite(self):

        self.favorite_button.click()