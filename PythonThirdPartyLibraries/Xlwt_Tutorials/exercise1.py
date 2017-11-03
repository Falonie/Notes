import xlwt

expense = [['Rent', 1000], ['Gas', 100], ['Food', 300], ['Gym', 50], ]
with xlwt.Workbook(encoding='ascii') as workbook:
    worksheet = workbook.add_sheet('exercise1')
    row = 0
    col = 0
    for i, j in expense:
        worksheet.write(row, col, i)
        worksheet.write(row, col + 1, j)
    workbook.save('/media/salesmind/Other/PycharmProjects/project_1/Exercise1.xlsx')

workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet('My Worksheet')
worksheet.write(0, 0, label='Row 0, Column 0 Value')
workbook.save('/media/salesmind/Other/PycharmProjects/project_1/Excel_Workbook.xls')