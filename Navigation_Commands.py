from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

driver.get("http://demo.guru99.com/V4/") #First URL
time.sleep(5)
print(driver.title)

driver.get("https://www.pavantestingtools.com/")    #Second URL
time.sleep(5)
print(driver.title)

driver.back()    #First URL
time.sleep(5)
print(driver.title)

driver.forward()   #Second URL
time.sleep(5)
print(driver.title)
