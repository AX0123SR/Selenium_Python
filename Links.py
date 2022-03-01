from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

#driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("http://demo.guru99.com/test/newtours/")
links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links = ", len(links))     #print all the no of links

#print all the link texts
for link in links:
    print(link.text)

#driver.find_element(By.LINK_TEXT,"REGISTER").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG").click()
#driver.quit()