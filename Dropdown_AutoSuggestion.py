import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32//chromedriver.exe")

driver.get("https://in.search.yahoo.com/?fr2=inr")
driver.find_element_by_id("yschsp").send_keys("aus")
time.sleep(2)

countries = driver.find_element_by_css_selector("li[class='sa-item prog-sugg'] b")
print(len(countries))