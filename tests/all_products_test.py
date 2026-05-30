import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.all_products_page import AllProductsPage


def test_all_products():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            products = AllProductsPage(page)

            products.go_to_home()

            time.sleep(3)

            products.click_all_products()

            time.sleep(5)

            # Assertion
            assert page.locator(
                '[data-testid="all-products-header"]'
            ).count() > 0, (
                "No se encontraron productos en All Products"
            )

            print(
                "All Products cargado correctamente"
            )

            page.screenshot(
                path="all_products_success.png"
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="all_products_error.png"
            )

            print(
                f"Error en All Products: {error}"
            )

            raise

        finally:

            browser.close()