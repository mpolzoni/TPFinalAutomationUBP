from selenium.webdriver.common.by import By

class AccountPageLocators:
        ACCOUNT_TITLE = (By.CLASS_NAME,'subtext') #'maintext')

class AccountPage:
     def __init__(self, driver):
        self.driver = driver

     def getAccountTitle(self):
        return self.driver.find_element(*AccountPageLocators.ACCOUNT_TITLE)