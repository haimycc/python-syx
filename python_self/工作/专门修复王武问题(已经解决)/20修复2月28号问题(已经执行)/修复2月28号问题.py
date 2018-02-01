import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def selectInvestId():
    with open("updatesql.20170208.back", "a+") as f:
        one29 = datetime.datetime.strptime("2017-01-29 00:00:00", "%Y-%m-%d %H:%M:%S")
        one30 = datetime.datetime.strptime("2017-01-30 00:00:00", "%Y-%m-%d %H:%M:%S")
        one31 = datetime.datetime.strptime("2017-01-31 00:00:00", "%Y-%m-%d %H:%M:%S")
        two1 =  datetime.datetime.strptime("2017-02-01 00:00:00", "%Y-%m-%d %H:%M:%S")
        #找到已经完标的标的
        sql="select asset_id,create_time,bid_time,finish_time,phase_total,phase_mode,state  from product.t_assets where create_time >='2017-01-21' and asset_type = 1 and phase_total = 1 "
        new_cursor.execute(sql)
        assetIdLists = new_cursor.fetchall()
        for assetIdList in assetIdLists:
            #找到标信息
            assetId=assetIdList["asset_id"]
            bidTime=assetIdList["bid_time"]
            finishtime=assetIdList["finish_time"]
            #根据assetId找到所有投资记录
            sql="select financial_plan_id,investment_id from product.t_investment_%s where asset_id = %d " % (str(assetId)[-2:],assetId)
            new_cursor.execute(sql)
            investLists = new_cursor.fetchall()
            for invest in investLists:
                finId=invest["financial_plan_id"]
                investId=invest["investment_id"]
                bidDateTime=datetime.datetime.strptime(str(bidTime), "%Y-%m-%d %H:%M:%S")
                updateSql1=""
                updateSql2=""
                updateSql3=""
                updateSqls=""
                f.write(updateSql1)
                #如果截止时间是29号
                if one29 <= bidDateTime and bidDateTime < one30:
                    updateSql1="update product.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 1 day)  where asset_id = %d and investment_id = %d and finish_time >='2017-02-28' and finish_time < '2017-03-01';\n" % (str(assetId)[-2:],assetId,investId)
                    updateSql2="update financial_plan.t_investment_%02d set finish_time=DATE_ADD(finish_time,interval 1 day)  where asset_id=%d and investment_id= %d and finish_time >='2017-02-28' and finish_time < '2017-03-01';\n" % (int(str(finId)[-2:]),assetId,investId)
                    updateSql3="update invest.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 1 day) where asset_id=%d and investment_id=%d and finish_time >='2017-02-28' and finish_time < '2017-03-01';\n" % (str(investId)[-2:],assetId,investId)
                    updateSqls="update invest.t_investments set finish_time=DATE_ADD(finish_time,interval 1 day) where asset_id=%d and investment_id=%d and finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n " % (assetId,investId)
                # 如果截止时间是30号
                elif one30 <= bidDateTime and bidDateTime < one31:
                    updateSql1="update product.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 2 day)  where asset_id = %d and investment_id = %d and finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (str(assetId)[-2:],assetId,investId)
                    updateSql2="update financial_plan.t_investment_%02d set finish_time=DATE_ADD(finish_time,interval 2 day)  where asset_id=%d and investment_id= %d and finish_time >= '2017-02-28' and finisht_time <'2017-03-01';\n" % (int(str(finId)[-2:]),assetId,investId)
                    updateSql3="update invest.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 2 day) where asset_id=%d and investment_id=%d and finish_time >= '2017-02-28' and finish_time < '2017-03-01' ;\n" % (str(investId)[-2:],assetId,investId)
                    updateSqls="update invest.t_investments set finish_time=DATE_ADD(finish_time,interval 2 day) where asset_id=%d and investment_id=%d and finish_time >= '2017-02-28' and finish_time < '2017-03-01' ;\n" % (assetId,investId)
                # 如果截止时间是31号
                elif one31 <= bidDateTime and bidDateTime < two1:
                    updateSql1="update product.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 3 day)  where asset_id = %d and investment_id = %d and finish_time >= '2017-02-28' and finish_time < '2017-03-01' ;\n" % (str(assetId)[-2:],assetId,investId)
                    updateSql2="update financial_plan.t_investment_%02d set finish_time=DATE_ADD(finish_time,interval 3 day)  where asset_id=%d and investment_id= %d and finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (int(str(finId)[-2:]),assetId,investId)
                    updateSql3="update invest.t_investment_%s set finish_time=DATE_ADD(finish_time,interval 3 day) where asset_id=%d and investment_id=%d and finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (str(investId)[-2:],assetId,investId)
                    updateSqls="update invest.t_investments set finish_time=DATE_ADD(finish_time,interval 3 day) where asset_id=%d and investment_id=%d and finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (assetId,investId)
                 #29号
                f.write(updateSql1)
                f.write(updateSql2)
                f.write(updateSql3)
                f.write(updateSqls)
            #修复标的表
            updateAsset=""
            if one29 <= bidDateTime and bidDateTime < one30:
                updateAsset="update product.t_assets set finish_time=DATE_ADD(finish_time,interval 1 day) where asset_id = %d and  finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (assetId)
            elif one30 <= bidDateTime and bidDateTime < one31:
                updateAsset="update product.t_assets set finish_time=DATE_ADD(finish_time,interval 2 day) where asset_id = %d and  finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (assetId)
            elif one31 <= bidDateTime and bidDateTime < two1:
                updateAsset="update product.t_assets set finish_time=DATE_ADD(finish_time,interval 3 day) where asset_id = %d and  finish_time >= '2017-02-28' and finish_time < '2017-03-01';\n" % (assetId)
            f.write(updateAsset)
            #修复回款表
            updatePayoff=""
            if one29 <= bidDateTime and bidDateTime < one30:
                updatePayoff="update specialDB.t_new_financial_plan_payoff set expect_date=DATE_ADD(expect_date,interval 1 day) where asset_id = %d and expect_date >= '2017-02-28 00:00:00' and expect_date < '2017-03-01 00:00:00' ;\n" % (assetId)
            elif one30 <= bidDateTime and bidDateTime < one31:
                updatePayoff="update specialDB.t_new_financial_plan_payoff set expect_date=DATE_ADD(expect_date,interval 2 day) where asset_id = %d and expect_date >= '2017-02-28 00:00:00' and expect_date < '2017-03-01 00:00:00' ;\n" % (assetId)
            elif one31 <= bidDateTime and bidDateTime < two1:
                updatePayoff="update specialDB.t_new_financial_plan_payoff set expect_date=DATE_ADD(expect_date,interval 3 day) where asset_id = %d and expect_date >= '2017-02-28 00:00:00' and expect_date < '2017-03-01 00:00:00' ;\n" % (assetId)
            f.write(updatePayoff)


if __name__ == "__main__":
    selectInvestId()