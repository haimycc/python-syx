import os
import time
import mysql.connector
from datetime import *
from dateutil.relativedelta import *
import calendar

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("王丽萍的定期理财投资记录.csv", "a+") as f:
        f.write("标的ID,标的名称,投资记录ID,投资金额,投资加利息金额,投标时间\n")
        uid=201609010101757174
        uidSuffix=int(str(uid)[-2:])
        sql="select asset_id,asset_name,investment_id,amount,sum(expect_principal+expect_interest) as amount2 " \
            "from invest.t_investment_payoff_%02d " \
            "where  " \
            "investor_uid= %d and  asset_type = 0 and asset_pool = 1  group by investment_id " % (uidSuffix,uid)
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            assetName=row["asset_name"]
            investId=row["investment_id"]
            amount=row["amount"]
            amount2=row["amount2"]
            investTime=None
            sql="select create_time from invest.t_investments where investment_id = %d " % (investId)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for investRow in investRows:
                investTime=investRow["create_time"]
            f.write("%s,%s,%s,%s,%s,%s\n" % (str(assetId),str(assetName),str(investId),str(amount),str(amount2),investTime))


handler()
