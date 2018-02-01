import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)


def handler():
    count1 = 0
    count2 = 0
    for i in range(100):
        sql = "select count(1) as num from asset.t_asset_flow_%02d where remark='系统扣费';" % (i)
        new_cursor.execute(sql)
        num = new_cursor.fetchall()
        count1 += num[0]['num']
        # print(sql)
    print('系统扣费数量:%d' % (count1))
    for j in range(100):
        sql = "select count(1) as num from asset.t_asset_flow_%02d where remark='用户缴费'" % (j)
        new_cursor.execute(sql)
        num = new_cursor.fetchall()
        count2 += num[0]['num']
        # print(sql)
    print('用户缴费:%d' % (count2))


handler()
