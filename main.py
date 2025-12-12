from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from methods import LoginPage, HomePage
import data


def main():

    service = Service()
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login = LoginPage(driver)
        home = HomePage(driver)

        # Flujo de prueba
        login.open_login_page()
        login.enter_username()
        login.enter_password()
        login.click_login()

        # Validar mensaje
        welcome_text = home.get_welcome_message()

        assert data.WELCOME_TEXT in welcome_text, \
            f"Texto recibido: {welcome_text}"

        print("✔ Test completado exitosamente.")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
