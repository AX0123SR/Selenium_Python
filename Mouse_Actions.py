'''
Move form an elemnt inside to element
1. import ActionChains class
2. open the url
3. Enter the username and password, then submit
4. Locate the elements
5. Create object for ActionChains class
6. using move_to_element, click and perform method
'''


from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32 (5)//chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
usermng = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(usermng).move_to_element(user).click().perform()

#driver.close()