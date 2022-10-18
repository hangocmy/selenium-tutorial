from selenium import webdriver
from selenium.webdriver.common.by import By
#get the path of chromedriver & create a new Chrome session
driver = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to the application home page
driver.get("https://business.adobe.com/products/magento/open-source.html")

#click button search
button_search = driver.find_element(By.XPATH, "//*[@daa-ll='Search']").click()

#get the search textbox
search_field = driver.find_element(By.NAME, "q")
search_field.clear()

#enter search keyword and submit
search_field.send_keys("phone")
search_field.submit()

#click close popup
clickClose = driver.find_element(By.XPATH, "//a[normalize-space()='Continue to United States']").click()

#get all the anchor elements which have product names displayed
products = driver.find_element(By.XPATH, "//h3[@class='spectrum-Heading spectrum-Heading--subtitle2 ResultsListItem-title']//a")

#get the number of anchor elements found
print(len(products.text))

#close the browser window
driver.quit()
