from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# start the session
service = ChromeService(executable_path=ChromeDriverManager().install())
options = ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options, service=service)

# login
driver.get("https://idbeauty-staging.idtek.com.vn/")

username = driver.find_element(By.XPATH, "//input[@id='Username']")

#username.send_keys("auto.test")
#username.send_keys(Keys.RETURN)

#driver.close()