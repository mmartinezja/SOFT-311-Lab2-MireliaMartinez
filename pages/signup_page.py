from playwright.sync_api import Page


class SignUpPage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_signup(self):
        self.page.goto(
            "https://storedemo.testdino.com/signup"
        )

    def fill_first_name(self, first_name):
        self.page.locator(
            '[data-testid="signup-firstname-input"]'
        ).fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator(
            '[data-testid="signup-lastname-input"]'
        ).fill(last_name)

    def fill_email(self, email):
        self.page.locator(
            '[data-testid="signup-email-input"]'
        ).fill(email)

    def fill_password(self, password):
        self.page.locator(
            '[data-testid="signup-password-input"]'
        ).fill(password)

    def click_submit(self):
        self.page.locator(
            '[data-testid="signup-submit-button"]'
        ).click()