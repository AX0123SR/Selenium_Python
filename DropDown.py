from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver= webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

driver.get("https://fs23.formsite.com/YWss1a/d53vkyctz6/index.html?1612338862282")

driver.find_element_by_id("RESULT_TextField-3").send_keys("1234567890")
drop = Select(driver.find_element_by_id("RESULT_RadioButton-4"))  #Select dropdown element

#Select element using select by visible text
#drop.select_by_visible_text("Phone")

#Select element using index
drop.select_by_index(2)

#Select element using value
#drop.select_by_value("Radio-1")

#print the total options in dropdowns
print(len(drop.options))

#print all the options name present in Dropdown
all_options = drop.options
for i in all_options:
    print(i.text)