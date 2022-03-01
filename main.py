from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver//chromedriver.exe")
		# set implicit time to 30 seconds
		# navigate to the url
driver.get("https://chercher.tech/python/windows-selenium-python")
		# get the Session id of the Parent
parentGUID = driver.current_window_handle
		# store the element
ele = driver.find_element_by_id("force-new-window")
		# create object for Actions class
act = ActionChains(driver)
		# press the shift key
act.key_down(Keys.SHIFT).click(ele).perform()