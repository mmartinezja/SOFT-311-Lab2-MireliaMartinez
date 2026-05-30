import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.signup_page import SignUpPage


def test_signup_no_password():

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

            # Password vacío

            time.sleep(2)

            signup.click_submit()

            time.sleep(3)

            assert page.locator(
                '[data-testid="signup-submit-button"]'
            ).is_visible(), (
                "El sistema permitió registrarse sin contraseña"
            )

            print(
                "Validación negativa correcta: Password requerido"
            )

            page.screenshot(
                path="signup_no_password_success.png"
            )

        except Exception as error:

            page.screenshot(
                path="signup_no_password_error.png"
            )

            print(
                f"Error: {error}"
            )

            raise

        finally:

            browser.close()