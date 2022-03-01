'''
Write data from Excel using Openpyxl
1) Install Openpyxl
2) import Openpyxl
3) Give the path for excel file
4) load the workbook
5) open the active excel sheet
6) Write something in excel using for loop
'''

import openpyxl
path = "C:/Users/ayussriv/Documents/Demo.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1,6):
    for c in range(1,6):
        sheet.cell(row=r,column=c).value="Hello Abizar"

workbook.save(path)