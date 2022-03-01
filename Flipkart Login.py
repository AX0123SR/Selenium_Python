from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

#Flipkart site
driver.get("https://www.flipkart.com/")

#Capture the Username
driver.find_element_by_xpath("//span[text()='Login']//following::input[1]").send_keys("7676988989")
time.sleep(2)

#Capture the password
driver.find_element_by_xpath("//span[text()='Login']//following::input[2]").send_keys("sjsjdjshjdh")
time.sleep(2)

#Capture the login button
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
#driver.find_element_by_xpath("//*[@type='submit']//preceding::input[1]").click()

