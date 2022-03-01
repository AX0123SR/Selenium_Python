'''
Screenshots are necessary as a proof in case of test case failure to send to developers to find the exact issue.
1) Open the uRL
2) Use any of 2 methods - save_Screenshot() or get_screenshot_as_file()
'''
import selenium
from selenium import webdriver
driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32 (1)//chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.maximize_window()
driver.save_screenshot("Homepage.jpg")
#driver.get_screenshot_as_file("Home.png")
print(selenium.__version__)
