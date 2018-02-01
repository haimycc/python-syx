import os
import mysql.connector
from datetime import datetime, date

#new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
#new_cursor = new_conn.cursor(dictionary=True)

def updatePayoffState():
    with open("updatesql.20161219","a+") as f:
        for suffix in range(0,100):
            sql1=str.format("update invest.t_investment_%02d set state=4 where state=7;" % (suffix))
            sql2=str.format("update product.t_investment_%02d set state=4 where state=7;" % (suffix))
            sql3=str.format("update financial_plan.t_investment_%02d set state=4 where state=7;" % (suffix))
            f.write(sql1+"\n")
            f.write(sql2+"\n")
            f.write(sql3+"\n")
        sqls = "update invest.t_investments set state=4 where state=7;"
        f.write(sqls+"\n")

if __name__ == "__main__" :
    updatePayoffState()
