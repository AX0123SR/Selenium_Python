from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("C://Users//ayussriv//Downloads//chromedriver_win32 (8)//chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.amazon.in/")

driver.find_element_by_xpath("//*[@id='nav-main']/div[1]").click()
driver.find_element_by_xpath("//div[contains(text(),'Fire TV')]").click()