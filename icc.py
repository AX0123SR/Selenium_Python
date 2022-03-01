import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32 (5)//chromedriver.exe")

driver.get("https://www.icc-cricket.com/")
driver.maximize_window()
time.sleep(2)
'''   Xpath for removing popup   '''
driver.find_element_by_xpath("//button[@class = 'ott-splash-promo__close js-close']").click()

rankings = driver.find_element_by_xpath("//h4[text() = 'Rankings']")
Team = driver.find_element_by_xpath("//h4[text() = 'Rankings']//following::a[2]")
time.sleep(3)
action = ActionChains(driver)
action.move_to_element(rankings).move_to_element(Team).click().perform()

''' Xpath for ODI '''
driver.find_element_by_xpath("//*[text() ='ODI']").click()
time.sleep(3)
''' Xpath for all countries'''
for i in range(1,21):
   countries = str(driver.find_element_by_xpath("//tbody/tr['i']/td[2]").text)
   if countries == "Pakistan":
     print("Matches = ", countries.find_element_by_xpath("//tbody/tr/td[3]").text)
#name = input("Enter the country name = ")
#print(len(countries))
#for country in countries:

''' if country.text == "Pakistan":
         #print("Matches = ", country.find_element_by_xpath("//tbody/tr/td[3]").text)
        #print("Points = ", country.find_element_by_xpath("//tbody/tr/td[4]").text)
        #print("Ranking = ", country.find_element_by_xpath("//tbody/tr/td[5]").text)

        #print(country.find_element_by_xpath("//tbody/tr['country']").text)
'''
driver.close()