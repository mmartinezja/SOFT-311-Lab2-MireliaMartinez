import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.about_us_page import AboutUsPage
from utils.screenshot_helper import (
    screenshot_path
)


def test_about_us():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            about = AboutUsPage(page)

            about.go_to_home()

            time.sleep(3)

            about.click_about_us()

            time.sleep(5)

            # Assertion
            assert page.url != (
                "https://storedemo.testdino.com"
            ), (
                "La página About Us no cargó correctamente"
            )

            print(
                "About Us cargado correctamente"
            )

            page.screenshot(
                path=screenshot_path(
                    "about_us_success.png"
                ),
                full_page=True
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "about_us_error.png"
                ),
                full_page=True
            )

            print(
                f"Error en About Us: {error}"
            )

            raise

        finally:

            browser.close()