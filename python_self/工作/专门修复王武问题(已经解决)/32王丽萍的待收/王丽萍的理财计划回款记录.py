import os
import time
import mysql.connector
from datetime import *
from dateutil.relativedelta import *
import calendar

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("王丽萍的理财计划回款记录.csv", "a+") as f:
        f.write("标的ID,标的名称,投资记录ID,回款ID,投资金额,回款本金,回款利息,回款时间,是否已回\n")
        uid=201609010101757174
        uidSuffix=int(str(uid)[-2:])
        sql="select *  " \
            "from specialDB.t_new_financial_plan_payoff " \
            "where  " \
            "investor_uid= %d order by investment_id" % (uid)
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            assetName=row["asset_name"]
            investId=row["investment_id"]
            payoffId=row["payoff_id"]
            amount=row["amount"]
            expectPrincipal=row["expect_principal"]
            expectInterest=row["expect_interest"]
            expectDate=row["expect_date"]
            state = row["state"]
            strState="未还"
            if state != 0:
                strState="已还"
            f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (str(assetId),str(assetName),str(investId),str(payoffId),str(amount),str(expectPrincipal),str(expectInterest),str(expectDate),strState))


handler()
