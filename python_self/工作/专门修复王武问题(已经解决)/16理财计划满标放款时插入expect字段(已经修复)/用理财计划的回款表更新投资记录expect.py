
import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def findDiff():
    with open(os.path.abspath(os.curdir) + '/updateExpect', 'a+') as f:
        sql="select a.asset_id,a.investment_id,b.expect_interest,b.expect_add_interest,a.create_time  from invest.t_investments a,specialDB.t_new_financial_plan_payoff b where a.asset_id=b.asset_id and a.investment_id=b.investment_id and (a.expect_interest != b.expect_interest or a.expect_add_interest != b.expect_add_interest);"
        new_cursor.execute(sql)
        results = new_cursor.fetchall()
        for result in results:
            assetId=result["asset_id"]
            assetIdSuffix=str(assetId)[-2:]
            investId=result["investment_id"]
            investIdSuffix=str(investId)[-2:]
            expectInterest=result["expect_interest"]
            expectAddInterest=result["expect_add_interest"]
            sql1 = str.format(
                "update invest.t_investment_%s set expect_interest=%d,expect_add_interest=%d  where asset_id = %d and asset_type = 1 and investment_id = %d  ;" %
                (investIdSuffix, expectInterest, expectAddInterest, assetId, investId))
            sql2 = str.format(
                "update product.t_investment_%s set expect_interest=%d,expect_add_interest=%d  where asset_id = %d and asset_type = 1 and investment_id = %d  ;" %
                (assetIdSuffix, expectInterest, expectAddInterest, assetId, investId))
            sql3 = str.format(
                "update financial_plan.t_investment_%s set expect_interest =%d,expect_add_interest=%d where asset_id= %d and asset_type = 1 and investment_id = %d  ;" %
                (assetIdSuffix, expectInterest, expectAddInterest, assetId, investId))
            sqls = str.format(
                "update invest.t_investments set expect_interest=%d,expect_add_interest=%d  where asset_id = %d and asset_type = 1  and investment_id = %d ; " %
                (expectInterest, expectAddInterest, assetId, investId))
            # print(sql1)
            # print(sql2)
            # print(sql3)
            # print(sqls)
            f.write(sql1 + "\n")
            f.write(sql2 + "\n")
            f.write(sql3 + "\n")
            f.write(sqls + "\n")


if __name__ == "__main__" :
    findDiff()


