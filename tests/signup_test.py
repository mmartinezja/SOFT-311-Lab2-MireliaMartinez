import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.signup_page import SignUpPage


def test_signup():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            signup = SignUpPage(page)

            signup.go_to_signup()

            time.sleep(3)

            signup.fill_first_name(
                "Mirelia"
            )

            signup.fill_last_name(
                "Martinez"
            )

            signup.fill_email(
                f"mirelia{int(time.time())}@test.com"
            )

            signup.fill_password(
                "Mirelia2021*"
            )

            time.sleep(2)

            signup.click_submit()

            time.sleep(5)

            # Validar que fue redirigido al Login
            assert page.locator(
                '[data-testid="login-title"]'
            ).is_visible(), (
                "El usuario no fue redirigido al Login"
            )

            print(
                "Sign Up ejecutado correctamente"
            )

            page.screenshot(
                path="signup_success.png"
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="signup_error.png"
            )

            print(
                f"Error en Sign Up: {error}"
            )

            raise

        finally:

            browser.close()