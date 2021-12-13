from selenium.webdriver.common.by import By

class ProductListPageLocators:
        PRODUCT_ITEM = (By.LINK_TEXT,'POUR HOMME EAU DE TOILETTE')

class ProductListPage:
     def __init__(self, driver):
        self.driver = driver

     def getProductItem(self):
        return self.driver.find_element(*ProductListPageLocators.PRODUCT_ITEM)