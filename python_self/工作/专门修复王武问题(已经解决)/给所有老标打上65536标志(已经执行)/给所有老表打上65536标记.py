import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def update65536():
    with open("updatesql.20170207", "a+") as f:
        sql="""select asset_id,asset_property,asset_type,asset_pool,create_time from product.t_assets where publish_time <= '2016-11-04'"""
        new_cursor.execute(sql)
        assetrows = new_cursor.fetchall()
        for assetrow in assetrows:
            assetId=assetrow["asset_id"]
            assetIdSuffix=int(str(assetId)[-2:])
            property=assetrow["asset_property"]
            assettype=assetrow["asset_type"]
            assetpool=assetrow["asset_pool"]
            createTime=assetrow["create_time"]
            #给老标打上标记
            f.write("update product.t_assets set asset_property = asset_property | 65536 where asset_id=%d and publish_time <= '2016-11-04' ;\n" %(assetId))
            #给老表的所有投资记录打上标记
            sql="select financial_plan_id,investment_id from product.t_investment_%02d where asset_id=%d " % (assetIdSuffix,assetId)
            new_cursor.execute(sql)
            investrows = new_cursor.fetchall()
            for investrow in investrows:
                investId = investrow["investment_id"]
                investIdSuffix = int(str(investId)[-2:])
                finanId=investrow["financial_plan_id"]
                finanIdSuffix=int(str(finanId)[-2:])
                sql1="update product.t_investment_%02d set asset_property = asset_property | 65536 where asset_id=%d and investment_id=%d ;\n" % (assetIdSuffix,assetId,investId)
                sql2="update invest.t_investment_%02d set asset_property = asset_property | 65536 where asset_id=%d and investment_id=%d ;\n" % (investIdSuffix,assetId,investId)
                sql3="update financial_plan.t_investment_%02d set asset_property = asset_property | 65536 where asset_id=%d and investment_id=%d ;\n" % (finanIdSuffix,assetId,investId)
                sqls="update invest.t_investments set asset_property = asset_property | 65536 where asset_id=%d and investment_id=%d ;\n" % (assetId,investId)
                f.write(sql1)
                f.write(sql2)
                f.write(sql3)
                f.write(sqls)
            print("asset_id is %d" % (assetId))

if __name__ == "__main__":
    update65536()