# -*- coding:utf-8 -*-

import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def updateOldPlatFromFinancialPlan() :
    f=open("./1updateSql","a+")
    sql="select *  from product.t_assets where asset_type=1 and asset_property & 65536 = 65536 and state in (5,6,7,8,9); "
    new_cursor.execute(sql)
    results = new_cursor.fetchall()
    for list in results:
        assetId=list["asset_id"]
        fullTime=list["full_time"]
        finishTime=list["finish_time"]
        totalAmount=list["total_amount"]
        updateAssetSql="update product.t_assets set state=10 where asset_id=%s and asset_type=1 and asset_property & 65536 = 65536 ;" % (assetId)
        print(updateAssetSql)
        f.write(updateAssetSql+"\n")
        #更新投资记录表
        assetIdsuffix=str(assetId)[-2:]
        investSumSql="select sum(amount) as amount from product.t_investment_%s where asset_id=%s" % (assetIdsuffix,assetId)
        new_cursor.execute(investSumSql)
        sumList=new_cursor.fetchall()
        for sum in sumList:
            investSum=sum["amount"]
            if investSum != None and investSum > totalAmount:
                print("error:investSum>totalAmount,asset id is "+assetId)
        #找到所有投资记录
        investSql="select investment_id from product.t_investment_%s where asset_id = %s " % (assetIdsuffix,assetId)
        new_cursor.execute(investSql)
        investIdLists = new_cursor.fetchall()
        for investIdList in investIdLists:
            investId=investIdList["investment_id"]
            investIdSuffix=str(investId)[-2:]
            updateInvest1="update invest.t_investment_%s set asset_state=10,update_time=now(),full_time='%s',finish_time='%s' where asset_id=%d and investment_id=%d and ( state = 4 or state = 2 or state = 7 ); " % (investIdSuffix,fullTime,finishTime,assetId,investId)
            updateInvest2="update financial_plan.t_investment_%s set asset_state=10,update_time=now(),full_time='%s',finish_time='%s' where asset_id=%d and investment_id=%d and ( state = 4 or state = 2 or state = 7 ); " % (assetIdsuffix,fullTime,finishTime,assetId,investId)
            updateInvest3="update product.t_investment_%s set asset_state=10,update_time=now(),full_time='%s',finish_time='%s' where asset_id=%d and investment_id=%d and ( state = 4 or state = 2 or state = 7 ); " % (assetIdsuffix,fullTime,finishTime,assetId,investId)
            updateInvests="update invest.t_investments set asset_state=10,update_time=now(),full_time='%s',finish_time='%s' where asset_id= %d and investment_id=%d and ( state = 4 or state =2 or state = 7 );" % (fullTime,finishTime,assetId,investId)
            print(updateInvest1)
            print(updateInvest2)
            print(updateInvest3)
            print(updateInvests)
            f.write(updateInvest1+"\n")
            f.write(updateInvest2+"\n")
            f.write(updateInvest3+"\n")
            f.write(updateInvests+"\n")
    f.close()



if __name__ == "__main__" :
    updateOldPlatFromFinancialPlan()