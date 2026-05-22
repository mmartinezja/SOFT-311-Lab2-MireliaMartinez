import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page_td import LoginPageTD


def run():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        login = LoginPageTD(page)

        login.go_to_login()

        time.sleep(5)

        login.fill_email("mmartinezja@ucenfotec.ac.cr")

        time.sleep(2)

        login.fill_password("Mirelia2021*")

        time.sleep(2)

        login.click_submit()

        time.sleep(5)

        # Assertion
        assert page.locator(
            '[data-testid="header-user-icon"]'
        ).is_visible(), (
            "El usuario no inició sesión correctamente"
        )

        print("Login ejecutado correctamente")

        page.screenshot(path="login_success.png")

        time.sleep(10)

        browser.close()


if __name__ == "__main__":
    run()