import openpyxl as openpyxl


def opex():
    wb = openpyxl.load_workbook("../file/问题.xlsx")
    print(wb.sheetnames)
    sheet = wb['Sheet1']

    for row in sheet.rows:
        row_str = ""
        for cell in row:
            cell_str = cell.value
            print(cell_str,end=",")
        print()


def wtex():
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "this is title !"
    sheet.cell(1,1,"哈哈哈哈")
    sheet.cell(1,2,"哈哈哈哈2")
    sheet.cell(1,3,"哈哈哈哈3")
    sheet.cell(2, 1, "张三")
    sheet.cell(2, 2, "李四")
    sheet.cell(2, 3, "玩")
    wb.save(filename="test.xlsx")


if __name__ == '__main__':
    wtex()