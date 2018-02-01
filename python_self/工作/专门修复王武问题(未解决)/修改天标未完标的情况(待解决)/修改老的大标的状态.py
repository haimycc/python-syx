import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getAsset():
    with open("updatesql.20170207", "a+") as f:
        sql="select * from product.t_assets where asset_type = 1 and asset_property & 65536 = 65536"
        new_cursor.execute(sql)
        assetRows = new_cursor.fetchall()
        for assetRow in assetRows:
            assetId=assetRow["asset_id"]
            assetSuffix=int(str(assetId)[-2:])
            totalAmount=assetRow["total_amount"]
            sql="select sum(amount) as amount from product.t_investment_%02d where asset_id=%d and asset_type =1 " % (int(str(assetId)[-2:]),assetId)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for investRow in investRows:
                amount=investRow["amount"]
                if totalAmount!=amount:
                    print("错误,标ID是%d" % (assetId))
                    continue

            sql = "select * from product.t_investment_%02d where asset_id=%d and asset_type = 1 " % (int(str(assetId)[-2:]), assetId)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for investRow in investRows:
                investId = investRow["investment_id"]
                investSuffix = int(str(investId)[-2:])
                financialId=investRow["financial_plan_id"]
                financialIdSuffix=int(str(financialId)[-2:])
                sql1 = "update product.t_investment_%02d set asset_state = 10,state = 4,update_time=now()  where asset_id=%d and investment_id=%d  ;\n" % (assetSuffix, assetId, investId)
                sql2 = "update invest.t_investment_%02d set asset_state = 10,state = 4,update_time=now() where asset_id=%d and investment_id=%d  ;\n" % (investSuffix, assetId, investId)
                sql3 = "update financial_plan.t_investment_%02d set asset_state = 10,state = 4,update_time=now() where asset_id=%d and investment_id=%d  ;\n" % (financialIdSuffix,assetId,investId)
                sqls = "update invest.t_investments set asset_state = 10,state = 4,update_time=now() where asset_id=%d and investment_id=%d  ;\n" % (assetId,investId)
                f.write(sql1)
                f.write(sql2)
                f.write(sql3)
                f.write(sqls)
        f.write("update product.t_assets set state=10,update_time=now() where asset_type =1 and asset_property & 65536 = 65536 ;\n")


getAsset()
