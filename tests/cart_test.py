import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage
from assertions import assert_with_screenshot
from utils.screenshot_helper import (
    screenshot_path
)


def test_cart():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        try:

            cart = CartPage(page)

            cart.go_to_home()

            time.sleep(5)

            cart.click_all_products()

            time.sleep(5)

            cart.click_product()

            time.sleep(5)

            cart.click_add_to_cart()

            time.sleep(5)

            cart.open_cart()

            time.sleep(5)

            # Assertion con screenshot automático
            assert_with_screenshot(
                page,
                condition=cart.is_cart_visible(),
                message="El carrito no se abrió correctamente",
                name="cart_visible_assert"
            )

            print(
                "Producto agregado al carrito correctamente"
            )

            page.screenshot(
                path=screenshot_path(
                    "cart_success.png"
                ),
                full_page=True
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path=screenshot_path(
                    "cart_error.png"
                ),
                full_page=True
            )

            print(
                f"Error en carrito: {error}"
            )

            raise

        finally:

            browser.close()


if __name__ == "__main__":
    test_cart()