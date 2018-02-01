import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def genSql():
    platformUid=201611040000002025
    with open("1updatesql.20170224","a+") as f:
        sql="select * from invest.t_investment_payoffs where state = 0 and asset_type = 0 and asset_pool = 2 and investor_uid != %d " % (platformUid)
        new_cursor.execute(sql)
        payoffs = new_cursor.fetchall()
        for payoff in payoffs:
            assetId=payoff["asset_id"]
            assetIdSuffix=int(str(assetId)[-2:])
            payoffId=payoff["payoff_id"]
            payoffIdSuffix=int(str(payoffId)[-2:])
            sql="select * from product.t_assets where asset_id = %d " % (assetId)
            new_cursor.execute(sql)
            assets = new_cursor.fetchall()
            for asset in assets:
                assetType=asset["asset_type"]
                assetPool=asset["asset_pool"]
                if assetType != 0 or assetPool != 2:
                    print(str.format("error:asset id is %d",assetId))
                else:
                    updateSql1="update invest.t_investment_payoff_%02d set state = 3 where asset_id = %d and payoff_id=%d and asset_type = 0 and asset_pool = 2 and state = 0 and investor_uid != %d ;\n " % (payoffIdSuffix,assetId,payoffId,platformUid)
                    updateSqls="update invest.t_investment_payoffs set state = 3 where asset_id = %d and payoff_id=%d and asset_type =0 and asset_pool = 2 and state = 0 and investor_uid != %d ;\n " % (assetId,payoffId,platformUid)
                    f.write(updateSql1)
                    f.write(updateSqls)


genSql()


