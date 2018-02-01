import os

import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def delsql():
    uid=1234567890
    with open("./2017-02-24.sql", "a+") as f:
        for idx in range(0,100):
            sql1="delete from financial_plan.t_investment_%02d where investor_uid=%d ;\n" % (idx,uid)
            sql2="delete from invest.t_investment_%02d where investor_uid=%d ; \n" % (idx,uid)
            sql3="delete from product.t_asset_%02d where investor_uid=%d ;\n" % (idx,uid)
            f.write(sql1)
            f.write(sql2)
            f.write(sql3)
        sqls="delete from invest.t_investments where investor_uid=%d ;\n " % (uid)
        f.write(sqls)

delsql()
