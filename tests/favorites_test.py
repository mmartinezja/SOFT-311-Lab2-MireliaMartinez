import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.favorites_page import FavoritesPage
from assertions import assert_with_screenshot


def test_favorites():

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

            # Assertion con screenshot automático
            assert_with_screenshot(
                page,
                condition=page.locator(
                    '[data-testid="all-products-wishlist-button-filled"]'
                ).is_visible(),
                message="El producto no fue agregado a favoritos",
                name="favorites_visible_assert"
            )

            print(
                "Producto agregado a favoritos correctamente"
            )

            page.screenshot(
                path="artifacts/screenshots/favorites_success.png",
                full_page=True
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="artifacts/screenshots/favorites_error.png",
                full_page=True
            )

            print(
                f"Error en favoritos: {error}"
            )

            raise

        finally:

            browser.close()


if __name__ == "__main__":
    test_favorites()