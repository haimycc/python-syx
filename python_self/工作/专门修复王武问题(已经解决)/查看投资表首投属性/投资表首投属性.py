import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    sum=0
    for suffix in range(0,100):
        sql=str.format("select investment_id from invest.t_investment_%02d where invest_property = 2 "% (suffix))
        new_cursor.execute(sql)
        lists = new_cursor.fetchall()
        for list in lists:
            investId=list["investment_id"]
            sum=sum+1
    print(sum)
