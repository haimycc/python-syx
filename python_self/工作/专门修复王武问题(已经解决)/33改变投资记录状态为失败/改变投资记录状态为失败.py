import os
import time
import mysql.connector
from datetime import *
from dateutil.relativedelta import *
import calendar

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updateSql.20170228", "a+") as f:
        assetId=20170228000016223
        assetIdSuffix= int(str(assetId)[-2:])
        sql="select * from product.t_investment_%02d where asset_id=%d " % (assetIdSuffix,assetId)
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            investId=row["investment_id"]
            investIdSuffix=int(str(investId)[-2:])
            financialId=row["financial_plan_id"]
            financialIdSuffix=int(str(financialId)[-2:])
            state=row["state"]
            if state == 2:
                sql1="update product.t_investment_%02d set state =3  where asset_id=%d and investment_id = %d and state = 2 ;\n" % (assetIdSuffix,assetId,investId)
                sql2="update invest.t_investment_%02d set state =3 where asset_id = %d and investment_id = %d and state = 2 ;\n" % (investIdSuffix,assetId,investId)
                sql3="update financial_plan.t_investment_%02d set state =3 where asset_id = %d and investment_id = %d and state =2 ;\n" % (financialIdSuffix,assetId,investId)
                sqls="update invest.t_investments set state =3 where asset_id = %d and investment_id = %d and state =2 ;\n" % (assetId,investId)
                f.write(sql1)
                f.write(sql2)
                f.write(sql3)
                f.write(sqls)
        f.write("update product.t_assets set state=5,full_time='0000-00-00 00:00:00',investor_count=0,raised_amount=0 where asset_id = %d  " % (assetId))




handler()