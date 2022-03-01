from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C://Users//ayussriv//Downloads//chromedriver//chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")
#to focus on the current open window
print(driver.current_window_handle)

driver.find_element_by_link_text("Click Here").click()
print(driver.title)

#Print to focus all the opening windows
print(driver.window_handles)
print(driver.title)



