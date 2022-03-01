from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")

driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfLvjFNtRSB_ElUyu-B5_Qm6PG8daHtRYpNwZ4oOZnQyOp78w/viewform")

driver.find_element_by_xpath("//div[text()='Email address']//following::input[1]").send_keys("comeayush2@gmail.com")
sleep(2)
driver.find_element_by_xpath("//div[text()='Email address']//following::input[2]").send_keys("Ayush Srivastava")
sleep(2)
driver.find_element_by_xpath("//div[text()='Email address']//following::input[3]").send_keys("9896233899")
sleep(2)
driver.find_element_by_xpath("//div[text()='Email address']//following::input[4]").send_keys("Vishal Vishwakarma")
sleep(2)
driver.find_element_by_xpath("//div[text()='Email address']//following::input[5]").send_keys("vvishwakarma497@gmail.com")
sleep(2)
driver.find_element_by_xpath("//div[text()='Email address']//following::input[6]").send_keys("8652544359")
sleep(2)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[3]/div/div/span/span").click()
sleep(2)

