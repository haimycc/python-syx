import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime
import xlrd
import xlwt


new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def handler():
    with open("updatesql.20170309", "a+") as f:
        assetId=20170202000001103
        assetIdSuffix=int(str(assetId)[-2:])
        sql="select finish_time from product.t_assets where asset_id = %d " % (assetId)
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            finishTime=row["finish_time"]
            updateSql="update specialDB.t_new_financial_plan_payoff set expect_date='%s' where asset_id = %d ;\n" % (finishTime,assetId)
            f.write(updateSql)

        sql="select investment_id,financial_plan_id from product.t_investment_%02d where asset_id = %d " % (assetIdSuffix,assetId)
        new_cursor.execute(sql)
        rows=new_cursor.fetchall()
        for row in rows:
            investId=row["investment_id"]
            investIdSuffix=int(str(investId)[-2:])
            planId=row["financial_plan_id"]
            planIdSuffix=int(str(planId)[-2:])
            updateSql1="update product.t_investment_%02d set finish_time = '%s' where asset_id = %d and investment_id = %d ;\n" % (assetIdSuffix,finishTime,assetId,investId)
            updateSql2="update invest.t_investment_%02d set finish_time = '%s' where asset_id = %d and investment_id = %d ;\n" % (investIdSuffix,finishTime,assetId,investId)
            updateSql3="update financial_plan.t_investment_%02d set finish_time = '%s' where asset_id = %d and investment_id = %d ;\n" % (planIdSuffix,finishTime,assetId,investId)
            updateSqls="update invest.t_investments set finish_time = '%s' where asset_id = %d and investment_id = %d ;\n" % (finishTime,assetId,investId)
            f.write(updateSql1)
            f.write(updateSql2)
            f.write(updateSql3)
            f.write(updateSqls)


handler()
