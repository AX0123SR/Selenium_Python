'''
Drag and Drop Actions using mouse function
1) import ActionChains
2) get the URL
3) Find the source and target element
4) Create ActionChains object
5) Using object, call function draganddrop(source,target)
'''

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.maximize_window()

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

source_element = driver.find_element_by_xpath("//*[@id='box7']")
target_element = driver.find_element_by_xpath("//*[@id='box107']")

action = ActionChains(driver)

action.drag_and_drop(source_element,target_element).perform()
#driver.close()
