# -*- coding:utf-8 -*-

import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


#更改新理财计划的投资记录
def updateNewFinancialPlanInvest() :
    f=open("./4updateSql","a+")
    #找到投资中的理财计划
    sql=" select asset_id,state from product.t_assets  where asset_type = 1 and asset_property & 65536 !=65536 and state = 8;"
    new_cursor.execute(sql)
    results = new_cursor.fetchall()
    for result in results:
        assetId=result["asset_id"]
        assetIdSuffix=str(assetId)[-2:]
        state=result["state"]
        #找到这个理财计划的所有投资记录
        investSqls="select investment_id from product.t_investment_%s where asset_id=%d and asset_type=1 " % (assetIdSuffix,assetId)
        new_cursor.execute(investSqls)
        investIdLists=new_cursor.fetchall()
        for investIdList in investIdLists:
            investId=investIdList["investment_id"]
            investIdSuffix=str(investId)[-2:]
            updateSql1="update product.t_investment_%s inner join product.t_assets a  on " \
                       "product.t_investment_%s.asset_id=a.asset_id " \
                       "set product.t_investment_%s.asset_state=a.state,product.t_investment_%s.full_time=a.full_time "\
                       " where " \
                       "product.t_investment_%s.asset_id = %d and product.t_investment_%s.investment_id = %d and a.state=8 ;" % \
                       (assetIdSuffix,assetIdSuffix,assetIdSuffix,assetIdSuffix,assetIdSuffix,assetId,assetIdSuffix,investId)
            updateSql2="update invest.t_investment_%s inner join product.t_assets a on " \
                       "invest.t_investment_%s.asset_id=a.asset_id " \
                       "set invest.t_investment_%s.asset_state=a.state,invest.t_investment_%s.full_time=a.full_time "\
                       " where " \
                       "invest.t_investment_%s.asset_id = %d and invest.t_investment_%s.investment_id = %d and a.state=8 ;" % \
                       (investIdSuffix,investIdSuffix,investIdSuffix,investIdSuffix,investIdSuffix,assetId,investIdSuffix,investId)
            updateSql3="update invest.t_investments inner join product.t_assets a  on " \
                       "invest.t_investments.asset_id=a.asset_id " \
                       "set invest.t_investments.asset_state=a.state,invest.t_investments.full_time=a.full_time "\
                       " where " \
                       "invest.t_investments.asset_id = %d and invest.t_investments.investment_id = %d and a.state=8 ; " % \
                       (assetId,investId)
            updateSqls="update financial_plan.t_investment_%s inner join product.t_assets a  on " \
                       "financial_plan.t_investment_%s.asset_id=a.asset_id " \
                       "set financial_plan.t_investment_%s.asset_state=a.state,financial_plan.t_investment_%s.full_time=a.full_time "\
                       " where " \
                       "financial_plan.t_investment_%s.asset_id = %d and financial_plan.t_investment_%s.investment_id = %d and a.state=8 ;" % \
                       (assetIdSuffix,assetIdSuffix,assetIdSuffix,assetIdSuffix,assetIdSuffix,assetId,assetIdSuffix,investId)
            print(updateSql1)
            print(updateSql2)
            print(updateSql3)
            print(updateSqls)
            f.write(updateSql1+"\n")
            f.write(updateSql2+"\n")
            f.write(updateSql3+"\n")
            f.write(updateSqls+"\n")
    f.close()


if __name__ == "__main__" :
    updateNewFinancialPlanInvest()
