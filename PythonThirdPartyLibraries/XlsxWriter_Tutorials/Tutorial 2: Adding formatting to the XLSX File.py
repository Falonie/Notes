import xlsxwriter

expense = (['Rent', 1000], ['Gas', 100], ['Food', 300], ['Gym', 50],)
with xlsxwriter.Workbook('/media/salesmind/Other/PycharmProjects/project_1/Exercise1.xlsx') as workbook:
    worksheet = workbook.add_worksheet('exercise_sheet')
    bold = workbook.add_format({'bold': True})
    money = workbook.add_format({'num_format': '$#,##0'})
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Cost', bold)
    row = 1;col = 0
    for item, cost in expense:
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost, money)
        row += 1
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 1, '=SUM(B2:B5)', money)