from selenium.webdriver.common.by import By

class ProductPageLocators:
        PRODUCT_NAME = (By.CLASS_NAME,'bgnone')
        PRO_FLAP_DESC = (By.LINK_TEXT, 'Description')
        PRO_DESC = (By.CSS_SELECTOR, 'div#description > p')

class ProductPage:
     def __init__(self, driver):
        self.driver = driver

     def getProductName(self):
        return self.driver.find_element(*ProductPageLocators.PRODUCT_NAME)

     def getFlapDescription(self):
        return self.driver.find_element(*ProductPageLocators.PRO_FLAP_DESC)

     def getDescription(self):
        return self.driver.find_element(*ProductPageLocators.PRO_DESC)