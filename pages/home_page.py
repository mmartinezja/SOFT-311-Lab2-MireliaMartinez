class HomePage:

    def __init__(self, page):

        self.page = page

    def go_to_home(self):

        self.page.goto(
            "https://storedemo.testdino.com",
            wait_until="domcontentloaded"
        )

    def get_page_title(self):

        return self.page.title()