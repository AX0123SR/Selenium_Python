from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32 (6)//chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()

time.sleep(3)
#Close the alert popup by 'OK' button
driver.switch_to_alert().accept()

#Close the alert popup by 'Cancel' button
driver.switch_to_alert().dismiss()
#driver.close()