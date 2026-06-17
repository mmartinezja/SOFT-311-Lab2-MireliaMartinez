import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.contact_page import ContactUsPage
from utils.screenshot_helper import (
    screenshot_path
)


def test_contact_us_no_message():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=True
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

            contact.fill_subject(
                "Negative Test"
            )

            # Message vacío

            time.sleep(2)

            contact.click_submit()

            time.sleep(3)

            assert page.locator(
                '[data-testid="contact-us-form"]'
            ).is_visible(), (
                "El formulario se envió aunque Message estaba vacío"
            )

            print(
                "Validación negativa correcta: Message requerido"
            )

            page.screenshot(
                path=screenshot_path(
                    "contact_us_no_message_success.png"
                ),
                full_page=True
            )

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "contact_us_no_message_error.png"
                ),
                full_page=True
            )

            print(
                f"Error: {error}"
            )

            raise

        finally:

            browser.close()