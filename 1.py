import openpyxl

wb = openpyxl.load_workbook('store.xlsx', data_only=True)

#print(wb.sheetnames)

#for sheet in wb:
#	print(sheet.title)

sheet = wb['Products']
#sheet = wb.active

# b2_cell = sheet['B2']
# c2_cell = sheet['c2'] # case insensitive
print(sheet['d2'].value)
sheet['d2'] = 400
print(sheet['d2'].value)

new_product = (11, 'Tablet', 12, 600, 12 * 600)
sheet.append(new_product)


wb.save('store.xlsx')


