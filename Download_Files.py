'''
Download files from Chrome browser
1) Get the URL - http://demo.automationtesting.in/FileDownload.html
2) Locate the text area, Generate and Download field.
3) Same do with pdf options
4) Delay for 2-3 sec before closing the browser

If want to change download location,
1) import Options class
2) create an object for Options class
3) Using object call method add.experimental_path and pass argument 'prefs' and "variable_name:path_location"
4) In executable path section, add Options object.
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chromeOptions = Options()
#chromeOptions.add_experimental_option("prefs",{"default_download_path":"C://Users/ayussriv/Documents"})
#driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe",chrome_options=chromeOptions)
driver = webdriver.Chrome(executable_path="C://Users//ayussriv//AppData//Local//Programs//Python//Python38-32//chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
# Download text file
driver.find_element_by_id("textbox").send_keys("Hello Ayush, You are doing great job!!")
driver.find_element_by_xpath("//*[@id='createTxt']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()

#Download pdf files
driver.find_element_by_id("pdfbox").send_keys("Hello Ayush, You are doing great job!!")
driver.find_element_by_xpath("//*[@id='createPdf']").click()
driver.find_element_by_xpath("//*[@id='link-to-download']").click()
