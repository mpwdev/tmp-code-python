import openpyxl

wb = openpyxl.load_workbook('store.xlsx')

#print(wb.sheetnames)

#for sheet in wb:
#	print(sheet.title)

sheet = wb['Products']
#sheet = wb.active

b2_cell = sheet['B2']
c2_cell = sheet['c2'] # case insensitive

print(b2_cell.value, c2_cell.value)

print(sheet.cell(row=4, column=2).value)

print(c2_cell.row, c2_cell.column)

print(sheet['A5'].data_type)
print(sheet['B5'].data_type)
print(sheet['A5'].encoding)

print(sheet['D4'].parent)

print(dir(b2_cell))

print(b2_cell.style, b2_cell._style, c2_cell.coordinate, c2_cell.protection)

