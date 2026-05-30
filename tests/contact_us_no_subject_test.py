import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.contact_page import ContactUsPage
from utils.screenshot_helper import (
    screenshot_path
)


def test_contact_us_no_subject():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            contact = ContactUsPage(page)

            contact.go_to_home()

            time.sleep(3)

            contact.click_contact_us()

            time.sleep(3)

            contact.fill_first_name(
                "Mirelia"
            )

            contact.fill_last_name(
                "Martinez"
            )

            # Subject vacío

            contact.fill_message(
                "Negative test without subject"
            )

            time.sleep(2)

            contact.click_submit()

            time.sleep(3)

            # Validación negativa:
            # seguimos en Contact Us

            assert page.locator(
                '[data-testid="contact-us-form"]'
            ).is_visible(), (
                "El formulario se envió aunque Subject estaba vacío"
            )

            print(
                "Validación negativa correcta: Subject requerido"
            )

            page.screenshot(
                path=screenshot_path(
                    "contact_us_no_subject_success.png"
                ),
                full_page=True
            )

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "contact_us_no_subject_error.png"
                ),
                full_page=True
            )

            print(
                f"Error: {error}"
            )

            raise

        finally:

            browser.close()