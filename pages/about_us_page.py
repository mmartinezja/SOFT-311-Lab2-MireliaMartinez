from playwright.sync_api import Page


class AboutUsPage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_home(self):
        self.page.goto(
            "https://storedemo.testdino.com"
        )

    def click_about_us(self):
        self.page.locator(
            '[data-testid="header-menu-about-us"]'
        ).click()

    def get_heading(self):
        return self.page.locator("h1").text_content()