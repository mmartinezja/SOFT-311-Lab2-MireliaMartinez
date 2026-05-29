import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.login_page_td import LoginPageTD
from assertions import assert_with_screenshot


def test_login_invalid():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            login = LoginPageTD(page)

            login.go_to_login()

            time.sleep(5)

            # Credenciales inválidas
            login.fill_email(
                "invalid@test.com"
            )

            time.sleep(2)

            login.fill_password(
                "wrongpassword"
            )

            time.sleep(2)

            login.click_submit()

            time.sleep(5)

            # Assertion con screenshot automático
            assert_with_screenshot(
                page,
                condition="login" in page.url.lower(),
                message="El login inválido fue aceptado",
                name="login_invalid_assert"
            )

            print(
                "Login inválido validado correctamente"
            )

            page.screenshot(
                path="artifacts/screenshots/login_invalid_success.png",
                full_page=True
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="artifacts/screenshots/login_invalid_error.png",
                full_page=True
            )

            print(
                f"Error en login inválido: {error}"
            )

            raise

        finally:

            browser.close()


if __name__ == "__main__":
    test_login_invalid()