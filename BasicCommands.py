from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome Driver
driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32//chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C://Users//ayussriv//Downloads//geckodriver-v0.30.0-win64//geckodriver.exe")
#driver = webdriver.Ie(executable_path="C://Users//ayussriv//Downloads//IEDriverServer_x64_3.9.0//IEDriverServer.exe")
# DemoURL
driver.get("http://demo.guru99.com/V4/")

#Title of page
print(driver.title)

#Url of Page
print(driver.current_url)
# Username
driver.find_element_by_name("uid").send_keys("mngr1336")

# Password
driver.find_element_by_name("password").send_keys("dAnavUq")

# Login Button
driver.find_element_by_name("btnLogin").click()

#Wait for 5 sec
time.sleep(3)

driver.quit()
