from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Amitabh_Bachchan")
driver.maximize_window()

#Scrol down the page to given pixel
#driver.execute_script("window.scrollBy(0,1000)",'')

# Scroll down till the element is visible
id = driver.find_element_by_id("Early_life")
driver.execute_script("arguments[0].scrollIntoView();",id)

#Scroll down till the end
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")