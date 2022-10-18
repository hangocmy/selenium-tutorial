import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SignIn(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    #create a new Chrome session
    cls.driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
    cls.driver.implicitly_wait(30)
    cls.driver.maximize_window()
    
    #navigate to the application home page
    cls.driver.get("https://business.adobe.com/products/magento/open-source.html")

  def test_sign_in(self):
    #click button search
    self.button_sign_in = self.driver.find_element(By.XPATH, "//span[@class='feds-login-text']").click()

  @classmethod
  def tearDown(cls):
    #close the browser window
    cls.driver.quit()
    
  if __name__ == '__main__':
    unittest.main(verbosity=2)

