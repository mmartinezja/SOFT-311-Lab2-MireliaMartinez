import time
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.home_page import HomePage


def test_home():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        page = browser.new_page()

        home = HomePage(page)

        home.go_to_home()

        # Assertion principal
        assert "Store" in home.get_page_title(), (
        "El Home no cargó correctamente"
        )

        print("Home cargado correctamente")

        page.screenshot(path="home_success.png")

        time.sleep(10)
        
        browser.close()

