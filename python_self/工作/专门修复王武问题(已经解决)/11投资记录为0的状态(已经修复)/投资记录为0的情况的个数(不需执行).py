import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    sum1=0
    for suffix in range(0,100):
        sql=str.format("select count(1) as count from invest.t_investment_%02d where state in (2,4)  " % (suffix))
        new_cursor.execute(sql)
        lists = new_cursor.fetchall()
        for list in lists:
            count=list["count"]
            sum1+=count
    print(sum1)

    sum2=0
    sql = str.format("select count(1) as count from invest.t_investments where state in (2,4)  ")
    new_cursor.execute(sql)
    lists = new_cursor.fetchall()
    for list in lists:
        count = list["count"]
        sum2 += count
    print(sum2)

    print(sum1-sum2)





