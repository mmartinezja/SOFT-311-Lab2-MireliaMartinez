from playwright.sync_api import Page


class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page

    def go_to_home(self):
        self.page.goto(
            "https://storedemo.testdino.com"
        )

    def click_contact_us(self):
        self.page.locator(
            '[data-testid="header-menu-contact-us"]'
        ).click()

    def fill_first_name(self, first_name):
        self.page.locator(
            '[data-testid="contact-us-first-name-input"]'
        ).fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator(
            '[data-testid="contact-us-last-name-input"]'
        ).fill(last_name)

    def fill_subject(self, subject):
        self.page.locator(
            '[data-testid="contact-us-subject-input"]'
        ).fill(subject)

    def fill_message(self, message):
        self.page.locator(
            '[data-testid="contact-us-message-input"]'
        ).fill(message)

    def click_submit(self):
        self.page.locator(
            '[data-testid="contact-us-submit-button"]'
        ).click()