# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("javahome-students.xls")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
