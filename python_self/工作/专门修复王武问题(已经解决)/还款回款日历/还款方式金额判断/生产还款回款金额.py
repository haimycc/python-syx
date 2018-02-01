import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date
import datetime

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getSql():
    with open("生产环境还款回款日历", "a+") as f:
        f.write("标的ID,募集金额,借款方式,年华利率,借款期限,满标日期,还款时间,回款日期,预计本金,预计利息\n")
        #找到新手标
        sql="select * from product.t_assets where asset_property & 65536 != 65536 and asset_type = 0 and asset_pool = 1 ;"
        new_cursor.execute(sql)
        assetrows = new_cursor.fetchall()
        for assetRow in assetrows:
            #找到满标放款时间
            money=assetRow["total_amount"]
            assetId=assetRow["asset_id"]
            phaseTotal=assetRow["phase_total"]
            phaseMode=assetRow["phase_mode"]
            fullTime=assetRow["full_time"]
            repayMode=assetRow["repay_mode"]
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
            annualRate=assetRow["annual_rate"]

            #找到每一期还款的时间
            sql="select * from product.t_repayments where asset_id=%d order by phase " % (assetId)
            new_cursor.execute(sql)
            repayrows = new_cursor.fetchall()
            for repayrow in repayrows:
                repayId=repayrow["repayment_id"]
                repayDate=repayrow["expect_date"]
                principal=repayrow["expect_principal"]
                interest=repayrow["expect_interest"]
                #找到该期的回款时间
                mode=""
                if phaseMode == 1 :
                    mode="%d天" % (phaseTotal)
                elif phaseMode == 2:
                    mode="%d月" % (phaseTotal)
                elif phaseMode == 3:
                    mode="%d年" % (phaseTotal)
                f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (assetId,str(money),repayMode,str(annualRate),mode,fullTime,repayDate,str(principal),str(interest)))


getSql()
