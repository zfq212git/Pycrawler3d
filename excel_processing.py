

import xlrd
import xlwt

from openpyxl import load_workbook

def archive_in_excel(starting_row_number,input1, input2):
	

	print (starting_row_number)

	
	sheet1_1['A'+str(starting_row_number+1)] = input1
	sheet1_1['A'+str(starting_row_number+2)] = input2
	sheet2_1['A2'] = starting_row_number+3

	


	#sheet1.put_cell (starting_row_number,0, 1,input1,0)
	#sheet1.put_cell (starting_row_number,1, 1, input2,0)

	#sheet2.put_cell(1,0, 2, starting_row_number + 3,0)

	#sheet2.put_cell(1,1,2,999,0)




