from selenium import webdriver

driver=webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSej9j001F04oWAmMeguphG1znpE7kuP0z-xq5_eOqzCs5vhEw/viewform")

driver.find_element_by_xpath("//div[text() = 'Email address']//following::input[1]").send_keys("comeayush2@gmail.com")
driver.find_element_by_xpath("//div[text() = 'Email address']//following::input[2]").send_keys("Ayush Srivastava")
driver.find_element_by_xpath("//div[text() = 'Email address']//following::input[3]").send_keys("9896233899")
driver.find_element_by_xpath("//div[text() = 'Email address']//following::input[3]").send_keys("comeayush2@gmail.com")
driver.find_element_by_xpath("//*[@id='i27']/div[3]/div").click()
