import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page_td import LoginPageTD
from assertions import assert_with_screenshot


def test_login_valid():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            login = LoginPageTD(page)

            login.go_to_login()

            time.sleep(5)

            login.fill_email(
                "mmartinezja@ucenfotec.ac.cr"
            )

            time.sleep(2)

            login.fill_password(
                "Mirelia2021*"
            )

            time.sleep(2)

            login.click_submit()

            time.sleep(5)

            # Assertion con screenshot automático
            assert_with_screenshot(
                page,
                condition=page.locator(
                    '[data-testid="header-user-icon"]'
                ).is_visible(),
                message="El usuario no inició sesión correctamente",
                name="login_valid_assert"
            )

            print(
                "Login ejecutado correctamente"
            )

            page.screenshot(
                path="artifacts/screenshots/login_success.png",
                full_page=True
            )

            time.sleep(10)

        except Exception as error:

            page.screenshot(
                path="artifacts/screenshots/login_error.png",
                full_page=True
            )

            print(
                f"Error en login: {error}"
            )

            raise

        finally:

            browser.close()


if __name__ == "__main__":
    test_login_valid()