# Definición de la clase HomePage.
# Esta clase representa la página principal (Home)
# siguiendo el patrón Page Object Model (POM).
class HomePage:

    # Constructor de la clase.
    # Se ejecuta automáticamente cuando se crea un objeto HomePage.
    def __init__(self, page):

        # Guarda el objeto page de Playwright
        # para poder utilizarlo en todos los métodos de la clase.
        self.page = page

    # Método encargado de navegar al Home del sistema.
    def go_to_home(self):

        # Abre la URL principal del sitio.
        # wait_until="domcontentloaded" indica que Playwright
        # debe esperar hasta que el DOM esté cargado antes de continuar.
        self.page.goto(
            "https://storedemo.testdino.com",
            wait_until="domcontentloaded"
        )

    # Método que obtiene el título de la página actual.
    def get_page_title(self):

        # Retorna el título de la página web.
        # Ejemplo: "TestDino Demo Store"
        return self.page.title()