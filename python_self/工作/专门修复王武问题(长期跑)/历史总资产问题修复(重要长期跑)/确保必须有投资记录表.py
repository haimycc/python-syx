import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
from enum import Enum, unique
import math

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getInvests():
    sql="select investment_id from invest.t_investment_payoffs group by investment_id"
    new_cursor.execute(sql)
    payoffRows = new_cursor.fetchall()
    for payoff in payoffRows:
        investId=payoff["investment_id"]
        sql=str.format("select * from invest.t_investment_%02d where investment_id=%d" % (int(str(investId)[-2:]),investId))
        new_cursor.execute(sql)
        investRows = new_cursor.fetchall()
        if len(investRows) == 0 :
            print("错误:找不到投资记录表,investment id is %d" % (investId))
        #else:
        #    print("payoff由投资记录,investment id is %d " % (investId))

getInvests()