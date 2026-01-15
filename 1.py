import openpyxl
from openpyxl.styles import *

wb = openpyxl.load_workbook('store.xlsx')
sheet = wb.active

my_cell = sheet['B4']

# print(dir(openpyxl.styles))

font = Font(name="Tahoma", size=16, color=colors.BLUE, bold=True, italic=True)
my_cell.font = font




wb.save('store.xlsx')


