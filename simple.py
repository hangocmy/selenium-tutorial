#from selenium import webdriver
#driver = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe")
#driver.get ("https://vntesters.com/")
#print (driver.title)
#driver.quit()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get ("https://vntesters.com/")
print (driver.title)
#driver.quit()