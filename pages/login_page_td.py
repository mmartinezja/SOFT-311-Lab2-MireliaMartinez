# Definición de la clase LoginPageTD.
# Esta clase representa la página de Login del sistema
# utilizando el patrón Page Object Model (POM).
class LoginPageTD:

# Constructor de la clase.
# Se ejecuta automáticamente al crear un objeto LoginPageTD.
    def __init__(self, page):

# Guarda el objeto page de Playwright para poder
# interactuar con la página web desde cualquier método.
        self.page = page

# Localiza el campo de correo electrónico utilizando
# el atributo data-testid definido en la aplicación.
        self.email_input = page.locator(
            '[data-testid="login-email-input"]'
        )

# Localiza el campo de contraseña.
        self.password_input = page.locator(
            '[data-testid="login-password-input"]'
        )

# Localiza el botón de inicio de sesión.
        self.submit_button = page.locator(
            '[data-testid="login-submit-button"]'
        )

# Método encargado de abrir la página de Login.
    def go_to_login(self):

# Navega a la URL de Login.
# wait_until="networkidle" indica que Playwright
# debe esperar hasta que no existan solicitudes
# de red activas antes de continuar.
        self.page.goto(
            "https://storedemo.testdino.com/login",
            wait_until="networkidle"
        )

# Método para ingresar el correo electrónico.
    def fill_email(self, email):

# Escribe el valor recibido en el campo Email.
        self.email_input.fill(email)

# Método para ingresar la contraseña.
    def fill_password(self, password):

    # Escribe el valor recibido en el campo Password.
        self.password_input.fill(password)

# Método para presionar el botón Sign In.
    def click_submit(self):

# Realiza clic sobre el botón de Login.
        self.submit_button.click()