import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.contact_page import ContactUsPage
from utils.screenshot_helper import (
    screenshot_path
)


def test_contact_us():

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
                "QA Automation Test"
            )

            contact.fill_message(
                "This is an automated test message."
            )

            time.sleep(2)

            contact.click_submit()

            time.sleep(5)

            # Assertion
            assert page.locator(
                '[data-testid="contact-us-form"]'
            ).is_visible(), (
                "El formulario Contact Us no está visible"
            )

            print(
                "Formulario Contact Us completado correctamente"
            )

            page.screenshot(
                path=screenshot_path(
                    "contact_us_success.png"
                ),
                full_page=True
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "contact_us_error.png"
                ),
                full_page=True
            )

            print(
                f"Error en Contact Us: {error}"
            )

            raise

        finally:

            browser.close()