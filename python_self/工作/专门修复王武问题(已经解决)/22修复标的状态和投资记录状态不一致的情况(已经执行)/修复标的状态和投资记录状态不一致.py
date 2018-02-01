import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getAsset():
    #有标的状态为8,然后投资状态为2
    with open("updatesql.20170207", "a+") as f:
        sql="select distinct asset_id,financial_plan_id,investment_id,asset_state,state,asset_type,asset_pool from invest.t_investments where asset_type =1 and asset_state = 8 and state = 2;"
        new_cursor.execute(sql)
        investRows = new_cursor.fetchall()
        for investRow in investRows:
            assetId=investRow["asset_id"]
            investId=investRow["investment_id"]
            planId=investRow["financial_plan_id"]
            assetIdSuffix=int(str(assetId)[-2:])
            investIdSuffix=int(str(investId)[-2:])
            planIdSuffix=int(str(planId)[-2:])
            assetState=investRow["asset_state"]
            state=investRow["state"]
            assetType=investRow["asset_type"]
            assetPool=investRow["asset_pool"]
            #判断标的状态
            sql="select state from product.t_assets where asset_id = %d " % (assetId)
            new_cursor.execute(sql)
            assetRows = new_cursor.fetchall()
            for assetRow in assetRows:
                assetState = assetRow["state"]
                if assetState != 8:
                    print("错误:asset id is %d,state is %d" % (assetId,assetState))
                    continue
            #查找流水表,没有超标的
            sql="select distinct operation from invest.t_investment_flow_%02d where investment_id = %d and operation in (9) " % (investIdSuffix,investId)
            new_cursor.execute(sql)
            operationRows = new_cursor.fetchall()
            if len(operationRows) == 0 :
                print("错误,投资没有冻结流水,investment id is %d" % (investId))
                continue
            #查找超标流水
            sql="select distinct operation from invest.t_investment_flow_%02d where investment_id = %d and operation in (5) " % (investIdSuffix,investId)
            new_cursor.execute(sql)
            operationRows = new_cursor.fetchall()
            if len(operationRows) != 0 :
                print("错误,投资有解冻流水,investment id is %d,asset_type is %d,asset_pool is %d" % (investId,assetType,assetPool))
                continue
            #都没有问题,那么更新2为4
            sql1="update product.t_investment_%02d set state=4 where asset_id=%d and investment_id=%d and state = 2;\n" % (assetIdSuffix,assetId,investId)
            sql2="update invest.t_investment_%02d set state=4 where asset_id=%d and investment_id=%d and state =2;\n" % (investIdSuffix,assetId,investId)
            sql3="update financial_plan.t_investment_%02d set state=4 where asset_id = %d and investment_id=%d and state=2 ;\n" % (planIdSuffix,assetId,investId)
            sqls="update invest.t_investments set state=4 where asset_id=%d and investment_id=%d and state=2 ;\n" % (assetId,investId)
            f.write(sql1)
            f.write(sql2)
            f.write(sql3)
            f.write(sqls)



if __name__=="__main__":
    getAsset()







