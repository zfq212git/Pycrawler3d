

import xlrd
import xlwt

from openpyxl import load_workbook

def archive_in_excel(file,input1, input2):
	data = xlrd.open_workbook(file)
	sheet1 = data.sheet_by_name(u'sheet1')
	sheet2 = data.sheet_by_name(u'sheet2')
	starting_row_number = int(sheet2.cell(1,0).value)

	

	data_1=load_workbook(file)
	sheet1_1=data_1.get_sheet_by_name(u'sheet1')
	sheet2_1=data_1.get_sheet_by_name(u'sheet2')

	sheet1_1['A1'] = input1
	sheet1_1['A2'] = '=HYPERLINK(input2)'
	sheet2_1['A2'] = starting_row_number+3

	data_1.save(file)


	#sheet1.put_cell (starting_row_number,0, 1,input1,0)
	#sheet1.put_cell (starting_row_number,1, 1, input2,0)

	#sheet2.put_cell(1,0, 2, starting_row_number + 3,0)

	#sheet2.put_cell(1,1,2,999,0)




