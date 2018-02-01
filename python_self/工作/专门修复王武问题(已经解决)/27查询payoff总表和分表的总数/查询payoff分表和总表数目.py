import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getNum():
    allNum=0
    for idx in range(0,100):
        sql="select count(1) as num from invest.t_investment_payoff_%02d " % (idx)
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            num=row["num"]
            allNum=allNum+num
    print(allNum)

getNum()