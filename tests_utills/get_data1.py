import pytest,xlrd,os,requests,json


def get_case_data():
    case_path = 'D:\pytest\pytest_0613\\test_file\\api_case.xls'
    print(case_path)
    book = xlrd.open_workbook(case_path)
    sheet= book.sheet_by_name('Sheet1')
    case = []
    for i in range(0, sheet.nrows ):
        if sheet.row_values(i)[0] == '学生登录' and sheet.row_values(i)[3] == 'YES':
            case.append(sheet.row_values(i))
    return case




pp = get_case_data()
print(pp)