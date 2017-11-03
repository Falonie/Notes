import xlsxwriter

expense = [['Rent', 1000], ['Gas', 100], ['Food', 300], ['Gym', 50],]
with xlsxwriter.Workbook('/media/salesmind/Other/PycharmProjects/project_1/Exercise1.xlsx') as workbook:
    worksheet = workbook.add_worksheet('exercise_sheet')
    row = 0;col = 0
    for item, cost in expense:
        worksheet.write(row, col,item)
        worksheet.write(row, col + 1, cost)
        row += 1
    worksheet.write(row,0,'Total')
    worksheet.write(row,1,'=SUM(B1:B4)')
# for item,cost in expense:
#     print(item,cost)