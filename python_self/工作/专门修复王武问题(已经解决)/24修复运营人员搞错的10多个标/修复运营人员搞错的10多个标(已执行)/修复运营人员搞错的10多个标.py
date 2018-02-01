import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
from enum import Enum, unique
import math

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

@unique
class repayModeEnum(Enum):
    YCBX=1,#一次性还本付息
    XXHB=2,#先息后本
    DEBX=3,#等额本息
    DEBJ=4,#等额本金
    DEDX=5,#等本等息

assetNames = ["'抵押宝-17011201'",
              "'抵押宝-2017011301'",
              "'抵押宝-17011304'",
              "'抵押宝-17011303'",
              "'抵押宝-17011302'",
              "'抵押宝-17011603'",
              "'抵押宝-17011604'",
              "'抵押宝-17011605'",
              "'抵押宝-17011701'",
              "'抵押宝-17011801'"
              ]

def getAssetIds():
    index=0
    strAssetName=""
    for assetName in assetNames:
        strAssetName=strAssetName+assetName
        index+=1
        if index < len(assetNames):
            strAssetName+=","
    print(strAssetName)
    sql=str.format("select asset_id from product.t_assets where asset_name in (%s) and state = 8 " % (strAssetName))
    new_cursor.execute(sql)
    lists = new_cursor.fetchall()
    assetIds=[]
    for list in lists:
        assetId=list["asset_id"]
        assetIds.append(assetId)
    return sorted(assetIds)


def genRepayInfo():
    with open("./updateRepaySql", "a+") as f:
        with open ("./还款表更新.csv","a+") as f2:
            f2.write("标ID,标名,募集金额(分),期数,原先待还本金,原先待还利息,修复后待还本金,修复后待还利息\n")
            #标ID
            assetIdsList=getAssetIds()
            #找到这个标的所有还款表
            for assetId in assetIdsList:
                # 找到标的的信息
                sql = str.format("select * from product.t_assets where asset_id = %d and state = 8 " % (assetId))
                new_cursor.execute(sql)
                assets = new_cursor.fetchall()
                for asset in assets:
                    amount=asset["total_amount"]
                    phase=asset["phase_total"]
                    annualRate = asset["annual_rate"]
                    sql=str.format("select asset_name,repayment_id,repay_mode,phase,phase_mode,annual_rate,expect_principal,expect_interest,state from product.t_repayments where asset_id=%d and state in (0,4)" % (assetId))
                    new_cursor.execute(sql)
                    repayLists = new_cursor.fetchall()
                    for repay in repayLists:
                        assetName=repay["asset_name"]
                        repayId=repay["repayment_id"]
                        repayMode=repay["repay_mode"]
                        phaseMode=repay["phase_mode"]
                        expectPrincipal=repay["expect_principal"]
                        expectInterest=repay["expect_interest"]
                        state=repay["state"]
                        phasenum=repay["phase"]
                        if repayMode == 3:
                            repayMode=5
                        benjin,lixi=repayWay(amount,repayMode,phase,phaseMode,annualRate)
                        updateSql=str.format("update product.t_repayment_%s set expect_principal= %d,expect_interest=%d,repay_mode=5 where asset_id = %d and repayment_id = %d and state in (0,4) ;\n" % (str(repayId)[-2:],benjin,lixi,assetId,repayId))
                        updateSqls=str.format("update product.t_repayments set expect_principal= %d,expect_interest=%d,repay_mode=5 where asset_id = %d and repayment_id = %d and state in (0,4) ;\n" % (benjin,lixi,assetId,repayId))
                        f.write(updateSql)
                        f.write(updateSqls)
                        f2.write("%d,%s,%d,%d,%d,%d,%d,%d\n" % (assetId,assetName,amount,phasenum,expectPrincipal,expectInterest,benjin,lixi))
                    f.write("update product.t_assets set repay_mode = 5 where asset_id = %d ; \n" % assetId)

#还款人
def repayWay(amount,repayMode,phase,phaseMode,annualRate):
    #等本等息,向上取整
    if repayMode == 5:
        for i in range(1,phase+1):
            #每期本金
            bdCapitalPerPeriod = math.ceil(amount/phase)
            #每期利息
            bdInterestPerPeriod = math.ceil(amount*annualRate/120000)
            return (bdCapitalPerPeriod,bdInterestPerPeriod)
    else:
        print("Error!!!!")



def genPayoffInfo():
    with open("./updatePyaoffSql", "a+") as f:
        with open("./回款表更新.csv","a+") as f2:
            f2.write("标ID,标名,投资人投资金额(分),期数,原先待收本金,原先待收利息,修复后待收本金,修复后待收利息\n")
            # 标ID
            assetIdsList = getAssetIds()
            # 找到这个标的所有投资收益表
            for assetId in assetIdsList:
                # 找到标的的信息
                sql = str.format("select * from product.t_assets where asset_id = %d and state = 8 " % (assetId))
                new_cursor.execute(sql)
                assets = new_cursor.fetchall()
                for asset in assets:
                    assetName=asset["asset_name"]
                    phase=asset["phase_total"]
                    phaseMode=asset["phase_mode"]
                    annualRate = asset["annual_rate"]
                    repayMode=asset["repay_mode"]

                    #找到这个标的所有投资记录
                    sql=str.format("select * from product.t_investment_%s where asset_id = %d and state = 4" % (str(assetId)[-2:],assetId))
                    new_cursor.execute(sql)
                    investLists = new_cursor.fetchall()
                    for invest in investLists:
                        financialId=invest["financial_plan_id"]
                        investId=invest["investment_id"]
                        amount=invest["amount"]
                        #根据投资记录找到所有回款记录
                        sql=str.format("select * from invest.t_investment_payoff_%s where asset_id= %d and investment_id = %d and state = 0  " % (str(investId)[-2:],assetId,investId))
                        new_cursor.execute(sql)
                        payoffs = new_cursor.fetchall()
                        for payoff in payoffs:
                            payoffId=payoff["payoff_id"]
                            expectPrincipal = payoff["expect_principal"]
                            expectInterest = payoff["expect_interest"]
                            state = payoff["state"]
                            phaseNum=payoff["phase"]
                            if repayMode == 3:
                                repayMode = 5
                            benjin,lixi,platform=payoffWay(amount,repayMode,phase,phaseMode,annualRate)
                            updateSql=str.format("update invest.t_investment_payoff_%s set expect_principal= %d,expect_interest=%d,expect_pay_platform=%d  where asset_id = %d and payoff_id = %d ; \n" % (str(payoffId)[-2:],benjin,lixi,platform,assetId,payoffId))
                            f.write(updateSql)
                            f2.write("%d,%s,%d,%d,%d,%d,%d,%d\n" % (assetId,assetName,amount,phaseNum,expectPrincipal,expectInterest,benjin,lixi))
                        #f.write("update product.t_investment_%s set repay_mode=5  where asset_id = %d and investment_id=%d ;\n" % (str(assetId)[-2:],assetId,investId))
                        #f.write("update invest.t_investment_%s set repay_mode=5 where asset_id = %d and investment_id=%d;\n" % (str(investId)[-2:],assetId,investId))
                        #f.write("update financial_plan.t_investment_%02d set repay_mode=5 where asset_id = %d and investment_id=%d;\n" % (int(str(financialId)[-2:]),assetId,investId))
                        #f.write("update invest.t_investments set repay_mode=5 where asset_id = %d ;\n" % (assetId))

#投资人
def payoffWay(amount,repayMode,phase,phaseMode,annualRate):
    #等本等息,向下取整
    if repayMode == 5:
        for i in range(1,phase+1):
            #每期本金
            bdCapitalPerPeriod = math.floor(amount/phase)
            #每期利息
            bdInterestPerPeriod = math.floor(amount*annualRate/120000)
            #真实利息
            bdRealInterestPerPeriod = bdInterestPerPeriod*95/100
            #每期给平台的投资管理费
            bdPlatformPeriod = bdInterestPerPeriod-bdRealInterestPerPeriod

            return (bdCapitalPerPeriod,bdRealInterestPerPeriod,bdPlatformPeriod)
    else:
        print("Error!!!!")



#主程序
if __name__ == "__main__" :
    genRepayInfo()
    genPayoffInfo()







