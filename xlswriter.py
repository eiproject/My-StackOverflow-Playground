import xlsxwriter
from xlsxwriter import workbook

workbook = xlsxwriter.Workbook('test.xlsx')

worksheet_description = workbook.add_worksheet( "description" )

sheetnames = input("Enter (sheets) names: ").split(", ")
for i in sheetnames:    # Loop for each sheet
    worksheet_data = workbook.add_worksheet(i)

    worksheet_data.write('A1', 'Number of table rows')

    data = []
    year = input("Enter years: ").split(", ")
    q = ['q1 ' , 'q2 ', 'q3 ', 'q4 ']
    for x in year:
        for y in q:
            data.append(x + y)
    worksheet_data.write_row(0, 1, data)

    col = input("Numerate columns (enter value): ").split(", ")
    for i in col:
        worksheet_data.write_column(1, 0, col)

workbook.close()