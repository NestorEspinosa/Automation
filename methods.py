from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import locators
import data



class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Ir a la página del login
    def open_login_page(self):
        self.driver.get(data.URL)

    # Ingresar usuario
    def enter_username(self):
        username_field = self.wait.until(
            EC.presence_of_element_located(locators.USERNAME_INPUT)
        )
        username_field.send_keys(data.USERNAME)

    # Ingresar contraseña
    def enter_password(self):
        password_field = self.driver.find_element(*locators.PASSWORD_INPUT)
        password_field.send_keys(data.PASSWORD)

    # Clic en botón login
    def click_login(self):
        login_btn = self.driver.find_element(*locators.LOGIN_BUTTON)
        login_btn.click()


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Obtener el mensaje de bienvenida
    def get_welcome_message(self):
        message = self.wait.until(
            EC.presence_of_element_located(locators.WELCOME_MESSAGE)
        )
        return message.text
