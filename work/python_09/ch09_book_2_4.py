import openpyxl

work_book = openpyxl.Workbook()

work_sheet = work_book.create_sheet(index=0, title="Python Ch09 Exercise")
work_sheet['B7'] = "Hello python world"

work_book.save(filename="ch09ex.xlsx")