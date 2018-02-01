import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getSum():
    allnum=0
    for idx in range(0,100):
        sql = "select ifnull(sum(" \
              "loan_principal+loan_interest+loan_add_interest+" \
              "plan_principal+plan_interest+plan_add_interest+" \
              "xrdt_principal+xrdt_interest+xrdt_add_interest),0) as num from invest.t_investment_sum_%02d " % (idx)
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            num=row["num"]
            allnum=allnum+num

    print(allnum)


getSum()