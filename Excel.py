from selenium import webdriver
import openpyxl
path = "C:/Users/ayussriv/Documents/Demo1.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active  # or workbook.get_sheet_by_name("Sheet 1")

driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver//chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
a1 = sheet['A1']
driver.find_element_by_id("txtUsername").send_keys(a1.value)

