from playwright.sync_api import Page


class AllProductsPage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_home(self):
        self.page.goto(
            "https://storedemo.testdino.com"
        )

    def click_all_products(self):
        self.page.locator(
            '[data-testid="header-menu-all-products"]'
        ).click()