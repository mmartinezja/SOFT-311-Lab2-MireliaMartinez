import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.favorites_page import FavoritesPage


def run():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            favorites = FavoritesPage(page)

            favorites.go_to_home()

            time.sleep(5)

            favorites.click_all_products()

            time.sleep(5)

            favorites.click_favorite()

            time.sleep(5)

            # Assertion
            assert page.locator(
                '[data-testid="all-products-wishlist-button-filled"]'
            ).is_visible(), (
                "El producto no fue agregado a favoritos"
            )

            print(
                "Producto agregado a favoritos correctamente"
            )

            page.screenshot(
                path="favorites_success.png"
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="favorites_error.png"
            )

            print(
                f"Error en favoritos: {error}"
            )

            raise

        finally:

            browser.close()


if __name__ == "__main__":
    run()