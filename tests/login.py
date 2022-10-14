from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import allure
import pytest
from assertpy import assert_that

from utils.json_parser import JsonParser

# start the session
service = ChromeService(executable_path=ChromeDriverManager().install())

options = ChromeOptions()
options.add_experimental_option("detach", True) 

driver = webdriver.Chrome(options=options, service=service)

# login
driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")

firstname = driver.find_element(By.NAME, "firstname")
firstname.JsonParser("data.json").read_from_json()["login"]["firstname"]
#firstname.send_keys(Keys.RETURN)

#driver.quit()