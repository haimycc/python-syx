import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getSql():
    with open("生产环境回款日历", "a+") as f:
        f.write("标的ID,借款方式,投资人,投资金额,年华利率,加息,借款期限,满标日期,第几期,回款日期,预计本金,预计利息,预计加息,平台管理费\n")
        #找到新手标
        sql="select * from product.t_assets where asset_property & 65536 != 65536 and asset_type = 0 and asset_pool = 1 ;"
        new_cursor.execute(sql)
        assetrows = new_cursor.fetchall()
        for assetRow in assetrows:
            #找到满标放款时间
            assetId=assetRow["asset_id"]
            phaseTotal=assetRow["phase_total"]
            phaseMode=assetRow["phase_mode"]
            fullTime=assetRow["full_time"]
            repayMode=assetRow["repay_mode"]
            annualRate=assetRow["annual_rate"]
            addRate=assetRow["add_rate"]

            if repayMode == 1:
                repayMode="一次性还本付息"
            elif repayMode == 2:
                repayMode="先息后本"
            elif repayMode == 3:
                repayMode ="等额本息"
            elif repayMode == 4:
                repayMode = "等额本金"
            elif repayMode == 5:
                repayMode = "等本等息"

            # 找到该期的回款时间
            mode = ""
            if phaseMode == 1:
                mode = "%d天" % (phaseTotal)
            elif phaseMode == 2:
                mode = "%d月" % (phaseTotal)
            elif phaseMode == 3:
                mode = "%d年" % (phaseTotal)

            #找到每一个投资人的回款详情
            sql="select * from invest.t_investment_payoffs where asset_id=%d order by investor_uid,phase " % (assetId)
            new_cursor.execute(sql)
            investRows = new_cursor.fetchall()
            for investRow in investRows:
                investorUid=investRow["investor_uid"]
                payoffId=investRow["payoff_id"]
                amount=investRow["amount"]
                principal=investRow["expect_principal"]
                interest=investRow["expect_interest"]
                addInterest=investRow["expect_add_interest"]
                platform=investRow["expect_pay_platform"]
                payoffDate=investRow["expect_date"]
                phase=investRow["phase"]

                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (assetId,repayMode,investorUid,amount,str(annualRate),addRate,mode,fullTime,phase,payoffDate,str(principal),str(interest),str(addInterest),str(platform)))


getSql()
