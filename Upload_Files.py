'''
Uploading files
1) open the URL
2) locate the 'upload file' element
3) provide the image/file path in send keys
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//PycharmProjects//POM_UnitTest_Project//drivers//chromedriver.exe")
driver.get("https://fs23.formsite.com/YWss1a/d53vkyctz6/index.html?1612338862282")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #scroll till the end
driver.find_element_by_id("RESULT_FileUpload-6").send_keys("C://Users/ayussriv/Pictures/ayush1.jpg")

#driver.close()