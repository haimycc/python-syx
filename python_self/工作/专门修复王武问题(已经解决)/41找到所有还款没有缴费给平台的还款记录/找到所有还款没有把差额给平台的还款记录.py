import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)



def handler():
    sql="select asset_id,repayment_id,expect_date from product.t_repayments where state in (2,3) and properties != 6  "
    new_cursor.execute(sql)
    rows = new_cursor.fetchall()
    for row in rows:
        assetId=row["asset_id"]
        repayId=row["repayment_id"]
        expectDate=row["expect_date"]

        sql="select * from account.t_user_account_flow_45 where loan_id = %d and date(create_time)=date('%s') and uid=201607190000004045 and type=2 " % (assetId,expectDate)
        new_cursor.execute(sql)
        counts = new_cursor.fetchall()
        if len(counts) == 0 :
            print("有问题,标ID是%d,expectDate is %s" % (assetId,expectDate))


handler()