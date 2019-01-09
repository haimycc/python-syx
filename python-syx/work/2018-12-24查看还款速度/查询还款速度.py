import mysql.connector
import xlrd
from datetime import date, datetime

new_conn = mysql.connector.connect(host='172.27.48.181', user='search', password='search@zyfax.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\湖南中业金服还款速度.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']
    sheet2_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('sheet2')

    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print(rows)
    print(cols)

    # 获取单元格内容
    print(sheet2.cell(1, 0).value.encode('utf-8'))
    print(sheet2.cell_value(1, 0).encode('utf-8'))
    print(sheet2.row(1)[0].value.encode('utf-8'))

    # 获取单元格内容的数据类型
    print(sheet2.cell(1, 0).ctype)


def getOne(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchone()


def getAll(sql, *args):
    new_cursor.execute(sql)
    return new_cursor.fetchall()


def DBclose():
    new_conn.close()


def get_asset_info():
    pass

get_asset_info()
read_excel()
