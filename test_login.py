from methods import LoginPage, HomePage
import data


def test_login_success(driver):
    login = LoginPage(driver)
    home = HomePage(driver)

    login.open_login_page()
    login.enter_username()
    login.enter_password()
    login.click_login()

    welcome_text = home.get_welcome_message()

    assert data.WELCOME_TEXT in welcome_text
    print("✔ Test completado exitosamente.")
