import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def genSql():
    sql="select * from invest.t_investment_payoffs  where state = 0 and asset_type = 0 and asset_pool = 1 and date(expect_date) < date(now()) "
    new_cursor.execute(sql)
    payoffs = new_cursor.fetchall()
    for payoff in payoffs:
        payoffId=payoff["payoff_id"]
        investId=payoff["investment_id"]
        investIdSuffix=int(str(investId)[-2:])
        #没有找到对应的投资记录
        #sql="select * from invest.t_investment_%02d where investment_id = %d " % (investIdSuffix,investId)
        #new_cursor.execute(sql)
        #invests = new_cursor.fetchall()
        #if len(invests) > 0 :
        #    print("ok")




genSql()
