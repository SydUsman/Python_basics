import openpyxl

inventory = openpyxl.load_workbook("inventory.xlsx")
product_list = inventory["Sheet1"]
print(product_list.max_row)