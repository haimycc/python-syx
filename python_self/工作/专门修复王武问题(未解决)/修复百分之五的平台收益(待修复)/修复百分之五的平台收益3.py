import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def updateSql():
    with open("updatesql.20170209.3", "a+") as f:
        for idx in range(0,100):
            sql="select *  from invest.t_investment_%02d " \
                "where " \
                "expect_pay_platform!=actual_pay_platform and " \
                "expect_pay_platform!=0 and actual_pay_platform!=0 " % (idx)
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
                sql="select ifnull(sum(expect_pay_platform),0) as payoff_platform from invest.t_investment_payoffs where investment_id=%d " % (investId)
                new_cursor.execute(sql)
                payoffRows = new_cursor.fetchall()
                for payoffRow in payoffRows:
                    payoffPlatform=payoffRow["payoff_platform"]
                    #if expectPlatform-payoffPlatform>15:
                    #    print("expectPlatform:%d,payoff_platform:%d" % (expectPlatform, payoffPlatform))
                    #if expectPlatform != payoffPlatform:
                    #    print("expectPlatform:%d,payoff_platform:%d" % (expectPlatform,payoffPlatform))
                    sql1 = "update invest.t_investment_%02d set expect_pay_platform=%d  where asset_id=%d and investment_id=%d and expect_pay_platform=%d ;\n" % (
                    investIdSuffix, payoffPlatform, assetId, investId, expectPlatform)
                    sql2 = "update product.t_investment_%02d set expect_pay_platform=%d  where asset_id=%d and investment_id=%d and expect_pay_platform=%d;\n" % (
                    assetIdSuffix, payoffPlatform, assetId, investId, expectPlatform)
                    sql3 = "update financial_plan.t_investment_%02d set expect_pay_platform=%d  where asset_id=%d and investment_id=%d and expect_pay_platform=%d;\n" % (
                    planIdSuffix, payoffPlatform, assetId, investId, expectPlatform)
                    sqls = "update invest.t_investments set expect_pay_platform=%d  where asset_id=%d and investment_id=%d and expect_pay_platform=%d;\n" % (
                    payoffPlatform, assetId, investId, expectPlatform)
                    f.write(sql1)
                    f.write(sql2)
                    f.write(sql3)
                    f.write(sqls)



if __name__ == "__main__":
    updateSql()
