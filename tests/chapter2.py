import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    #create a new Chrome session
    cls.driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
    cls.driver.implicitly_wait(30)
    cls.driver.maximize_window()
    
    #navigate to the application home page
    cls.driver.get("https://business.adobe.com/products/magento/open-source.html")
    cls.driver.title

  def test_search(self):
    #click button search
    self.button_search = self.driver.find_element(By.XPATH, "//*[@daa-ll='Search']").click()

    #get the search textbox
    self.search_field = self.driver.find_element(By.NAME, "q")
    self.search_field.clear()

    #enter search keyword and submit
    self.search_field.send_keys("phone")
    self.search_field.submit()

    #click close popup
    self.clickClose = self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue to United States']").click()

    #get all the anchor elements which have product names displayed
    products = self.driver.find_element(By.XPATH, "//h3[@class='spectrum-Heading spectrum-Heading--subtitle2 ResultsListItem-title']//a")
    #get the number of anchor elements found
    self.assertNotEqual(43, len(products.text))
    
  @classmethod
  def tearDown(cls):
    #close the browser window
    cls.driver.quit()
  
  if __name__ == '__main__':
    unittest.main(verbosity=2)

