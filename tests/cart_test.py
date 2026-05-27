import sys
from pathlib import Path
import time

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from playwright.sync_api import sync_playwright
from pages.cart_page import CartPage


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

            # Assertion
            assert cart.is_cart_visible(), (
                "El carrito no se abrió correctamente"
            )

            print(
                "Producto agregado al carrito correctamente"
            )

            page.screenshot(
                path="cart_success.png"
            )

            time.sleep(5)

        except Exception as error:

            page.screenshot(
                path="cart_error.png"
            )

            print(
                f"Error en carrito: {error}"
            )

            raise

        finally:

            browser.close()

