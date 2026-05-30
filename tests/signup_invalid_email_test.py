import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.signup_page import SignUpPage
from utils.screenshot_helper import (
    screenshot_path
)


def test_signup_invalid_email():

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
                "correo_invalido"
            )

            signup.fill_password(
                "Mirelia2021*"
            )

            time.sleep(2)

            signup.click_submit()

            time.sleep(3)

            # Debe permanecer en Sign Up
            assert page.locator(
                '[data-testid="signup-submit-button"]'
            ).is_visible(), (
                "El sistema aceptó un email inválido"
            )

            print(
                "Validación negativa correcta: email inválido"
            )

            page.screenshot(
                path=screenshot_path(
                    "signup_invalid_email_success.png"
                ),
                full_page=True
            )

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "signup_invalid_email_error.png"
                ),
                full_page=True
            )

            print(
                f"Error: {error}"
            )

            raise

        finally:

            browser.close()