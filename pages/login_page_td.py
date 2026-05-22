class LoginPageTD:

    def __init__(self, page):

        self.page = page

        self.email_input = page.locator(
            '[data-testid="login-email-input"]'
        )

        self.password_input = page.locator(
            '[data-testid="login-password-input"]'
        )

        self.submit_button = page.locator(
            '[data-testid="login-submit-button"]'
        )

    def go_to_login(self):

        self.page.goto(
            "https://storedemo.testdino.com/login",
            wait_until="networkidle"
        )

    def fill_email(self, email):

        self.email_input.fill(email)

    def fill_password(self, password):

        self.password_input.fill(password)

    def click_submit(self):

        self.submit_button.click()