# -*- coding:utf-8 -*-

import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def getRepayInfo():
    sum=0
    for index in range(0,100):
        sql="select sum(expect_principal) from product.t_repayment_%02d  where state in (0,4) and asset_type=0 and asset_pool in (2,4)  and expect_date >= '2016-12-08 00:00:00'" % (index)
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        for result in results:
            sum+=result["sum(expect_principal)"]
    print(sum/100)


if __name__ == "__main__" :
    getRepayInfo()