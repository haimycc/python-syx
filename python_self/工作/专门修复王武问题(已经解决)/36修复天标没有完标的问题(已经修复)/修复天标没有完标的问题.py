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
    with open("updatesql.20170306.2", "a+") as f:
        sql="select asset_id from product.t_assets where state = 8 and phase_mode = 1 "
        new_cursor.execute(sql)
        rows = new_cursor.fetchall()
        for row in rows:
            assetId=row["asset_id"]
            sql="select repayment_id,phase,state from product.t_repayments where asset_id = %d order by expect_date desc limit 0,1  " % (assetId)
            new_cursor.execute(sql)
            repays = new_cursor.fetchall()
            for repay in repays:
                repayId=repay["repayment_id"]
                phase=repay["phase"]
                state=repay["state"]
                if state == 3 :
                    #检查是否有还款没有完成
                    sql="select repayment_id,state from product.t_repayments where asset_id = %d " % (assetId)
                    new_cursor.execute(sql)
                    repay2s = new_cursor.fetchall()
                    for repay2 in repay2s:
                        state2=repay2["state"]
                        if state2 != 3 :
                            print("error:asset_id is %d " % (assetId))
                            break
                    #所有还款都是ok的,那么
                    sql="select * from invest.t_investments where asset_id = %d and state in (2,4)" % (assetId)
                    new_cursor.execute(sql)
                    invests = new_cursor.fetchall()
                    for invest in invests:
                        assetIdSuffix=int(str(assetId)[-2:])
                        investId=invest["investment_id"]
                        investIdSuffix=int(str(investId)[-2:])
                        financialId=invest["financial_plan_id"]
                        financialIdSuffix=int(str(financialId)[-2:])
                        assetState=invest["asset_state"]
                        sql1="update product.t_investment_%02d set asset_state = 10 where asset_id = %d and investment_id = %d and asset_state = %d and state in (2,4) ;\n" % (assetIdSuffix,assetId,investId,assetState)
                        sql2="update invest.t_investment_%02d set asset_state = 10 where asset_id = %d and investment_id = %d and asset_state = %d and state in (2,4) ;\n" % (investIdSuffix,assetId,investId,assetState)
                        sql3="update financial_plan.t_investment_%02d set asset_state = 10 where asset_id = %d and investment_id = %d and asset_state = %d and state in (2,4) ;\n" % (financialIdSuffix,assetId,investId,assetState)
                        sqls="update invest.t_investments set asset_state = 10 where asset_id = %d and investment_id = %d and asset_state = %d and state in (2,4) ;\n" % (assetId,investId,assetState)
                        f.write(sql1)
                        f.write(sql2)
                        f.write(sql3)
                        f.write(sqls)
                    sqls="update product.t_assets set state = 10 where asset_id = %d and state = 8;\n" % (assetId)
                    f.write(sqls)

handler()












