import Excel_Utilities as xl
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.get("https://github.com/")
driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()

path = "C:/Users/ayussriv/Documents/Data_test.xlsx"
row = xl.getRowCount(path,"Sheet1")

for r in range(2,row+1):
    username = xl.ReadData(path,"Sheet1",r,1)
    password = xl.ReadData(path,"Sheet1",r,2)

    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_name("commit").click()
    time.sleep(1)
    if(driver.title == "GitHub: Where the world builds software · GitHub"):

        print("Test Case Passed")
        xl.WriteData(path,"Sheet1",r,3,"pass")

    else:
        print("Test Case Failed")
        xl.WriteData(path,"Sheet1",r,3,"Fail")
        time.sleep(1)
        #driver.find_element_by_xpath("/html/body/div[1]/div[1]/a[2]").click()
        driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary").click()
        #time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/form/button").click()
        #time.sleep(1)