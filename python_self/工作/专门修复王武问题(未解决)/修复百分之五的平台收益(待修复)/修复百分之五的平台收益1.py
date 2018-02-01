import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def updateSql():
    with open("updatesql.20170207", "a+") as f:
        for idx in range(0,100):
            sql="select * from invest.t_investment_%02d where asset_state = 10 and asset_type = 0 and asset_pool = 1 and expect_pay_platform!=0 and actual_pay_platform!=0 and expect_pay_platform!=actual_pay_platform " % (idx)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for investRow in investRows:
                assetId=investRow["asset_id"]
                assetIdSuffix=int(str(assetId)[-2:])
                investId=investRow["investment_id"]
                investIdSuffix=int(str(investId)[-2:])
                planId=investRow["financial_plan_id"]
                planIdSuffix=int(str(planId)[-2:])
                expectPlatform=investRow["expect_pay_platform"]
                actualPlatform=investRow["actual_pay_platform"]

                if expectPlatform!=actualPlatform :
                    print("investId is %d,expectPlatform is %d,actualPlatform is %d" % (investId,expectPlatform,actualPlatform))
                    sql1="update product.t_investment_%02d set expect_pay_platform=actual_pay_platform where asset_id= %d and investment_id=%d;\n" % (assetIdSuffix,assetId,investId)
                    sql2="update invest.t_investment_%02d set expect_pay_platform=actual_pay_platform where asset_id=%d and investment_id=%d ;\n" % (investIdSuffix,assetId,investId)
                    sql3="update financial_plan.t_investment_%02d set expect_pay_platform=actual_pay_platform where asset_id=%d and investment_id=%d;\n" % (planIdSuffix,assetId,investId)
                    sqls="update invest.t_investments set expect_pay_platform=actual_pay_platform where asset_id=%d and investment_id=%d ;\n" % (assetId,investId)
                    f.write(sql1)
                    f.write(sql2)
                    f.write(sql3)
                    f.write(sqls)

if __name__ == "__main__":
    updateSql()
