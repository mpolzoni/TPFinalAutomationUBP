from selenium.webdriver.common.by import By

class HeaderPageLocators:
        SUBCAT_FILTER = (By.CSS_SELECTOR,'ul.categorymenu > li:nth-of-type(5)')
        SUBSUBCAT_FILTER = (By.LINK_TEXT, 'Men')
                            #, '.current > .subcategories > ul:nth-of-type(1) > li:nth-of-type(1) > a')

class HeaderPage:
  def __init__(self, driver):
   self.driver = driver

  def getSubcatFilter(self):
   return self.driver.find_element(*HeaderPageLocators.SUBCAT_FILTER)

  def getSubSubCatFilter(self):
   return self.driver.find_element(*HeaderPageLocators.SUBSUBCAT_FILTER)