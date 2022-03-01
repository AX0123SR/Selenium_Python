from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver= webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

driver.get("https://fs23.formsite.com/YWss1a/d53vkyctz6/index.html?1612338862282")

print("Displayed or not :", driver.find_element(By.ID,"RESULT_TextField-1").is_displayed())
print("Enabled or not :", driver.find_element(By.ID,"RESULT_TextField-1").is_enabled())

#Find no of input boxes in webpage
inputs = driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputs))

driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Gulshan")
driver.find_element(By.ID,"RESULT_TextField-2").send_keys("gulshansingh12@gmail.com")
driver.find_element_by_id("RESULT_TextField-3").send_keys("1234567890")
sleep(2)

# Checkoxes
driver.find_element(By.XPATH,"//label[text()='Executive']").click()
driver.find_element(By.XPATH,"//label[text()='Technology']").click()

drop = driver.find_element_by_id("RESULT_RadioButton-4")
drop.find_element_by_xpath("//*[@id='RESULT_RadioButton-4']/option[3]").click()

