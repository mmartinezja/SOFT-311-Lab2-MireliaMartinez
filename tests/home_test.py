import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

# Permite importar módulos desde la raíz del proyecto
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pages.home_page import HomePage
from assertions import assert_with_screenshot
from utils.screenshot_helper import (
    screenshot_path
)


def test_home() -> None:

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        home = HomePage(page)

        # Navegar al Home
        home.go_to_home()

        # Validación principal
        assert_with_screenshot(
            page,
            condition="Store" in home.get_page_title(),
            message=(
                f"Expected page title to contain 'Store' "
                f"but got '{home.get_page_title()}'"
            ),
            name="home_title_assert"
        )

        print("Home cargado correctamente")

        page.wait_for_load_state("networkidle")
        # Screenshot de evidencia exitosa
        page.screenshot(
            path=screenshot_path(
                "home_success.png"
            ),
            full_page=True
        )

        browser.close()


if __name__ == "__main__":
    test_home()