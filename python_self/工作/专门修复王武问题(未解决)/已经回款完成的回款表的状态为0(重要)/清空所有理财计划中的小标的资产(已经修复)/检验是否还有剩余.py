import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def genSql():
    for idx in range(0,100):
        sql="select * from invest.t_investment_payoff_%02d where state = 0 and asset_type = 0 and asset_pool = 2 " % (idx)
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        if len(payoffs) > 0 :
            print(str.format("error"))



genSql()
