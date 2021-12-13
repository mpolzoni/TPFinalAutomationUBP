from selenium.webdriver.common.by import By

class LoginPageLocators:

    USER_INPUT = (By.ID, 'loginFrm_loginname')
    PASS_INPUT = (By.ID, 'loginFrm_password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[title="Login"]')
    ACCOUNT_TITLE = (By.CLASS_NAME, 'fa fa-user')

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def getUserInput(self):
        return self.driver.find_element(*LoginPageLocators.USER_INPUT)
        print('Completar usuario')

    def getPassInput(self):
        return self.driver.find_element(*LoginPageLocators.PASS_INPUT)
        print('Completar password')

    def getLoginBtn(self):
        return self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
        print('Presiona Botón Login')

    def getAccountTitle(self):
        return self.driver.find_element(*LoginPageLocators.ACCOUNT_TITLE)
        print('Comparo el titulo')