from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Here we created an object 'driver' by using webdriver.Chrome
#And provide the path location of ChromeDriver.

driver = webdriver.Firefox(executable_path="C://Users//ayussriv//Downloads//geckodriver-v0.29.0-win32//geckodriver.exe")

driver.get("http://www.demo.guru99.com/V4/")

print(driver.title)
print(driver.current_url)
driver.close()