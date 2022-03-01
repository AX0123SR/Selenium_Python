'''
We have to read ad write from an excel sheet.
1)import Excel_Utilies
2)Provide the excel path in a variable
3) for row count, call the getrowcount funtion
4) FOr reading data, do a for loop from row to range(2,row+1)
5) Run the loop from column to column - Username and Password
6) Locate the elements
7) If login success by getting actual title, write data into excel by Pass
8) If login Fails, write data into excel by Fail
9) To check for other test cases, logout and then repeat the same above process.
'''

import Excel_Utilities as xl
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")

path = "C:/Users/ayussriv/Documents/Data_test.xlsx"
row = xl.getRowCount(path,"Sheet1")

for r in range(2,row+1):
    username = xl.ReadData(path,"Sheet1",r,1)
    password = xl.ReadData(path,"Sheet1",r,2)

    driver.find_element_by_id("txtUsername").send_keys(username)
    driver.find_element_by_id("txtPassword").send_keys(password)
    driver.find_element_by_id("btnLogin").click()
    time.sleep(1)
    if(driver.find_element_by_xpath("//*[@id='spanMessage']").text == "Invalid credentials"):

        print("Test Case Failed")
        xl.WriteData(path,"Sheet1",r,3,"fail")

    else:
        print("Test Case Passed")
        xl.WriteData(path,"Sheet1",r,3,"Pass")
        time.sleep(2)
        #driver.find_element_by_xpath("/html/body/div[1]/div[1]/a[2]").click()
        driver.find_element_by_id("welcome").click()
        time.sleep(2)
        driver.find_element_by_link_text("Logout").click()
        time.sleep(2)


driver.quit()