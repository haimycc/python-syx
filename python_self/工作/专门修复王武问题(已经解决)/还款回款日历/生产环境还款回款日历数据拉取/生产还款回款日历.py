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
        f.write("标的ID,借款期限,满标日期,还款时间,回款日期\n")
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
            #找到每一期还款的时间
            sql="select * from product.t_repayments where asset_id=%d order by phase " % (assetId)
            new_cursor.execute(sql)
            repayrows = new_cursor.fetchall()
            for repayrow in repayrows:
                repayId=repayrow["repayment_id"]
                repayDate=repayrow["expect_date"]
                #找到该期的回款时间
                sql="select distinct expect_date  from invest.t_investment_payoffs where repayment_id= %d " % (repayId)
                new_cursor.execute(sql)
                payoffrows = new_cursor.fetchall()
                for payoffrow in payoffrows:
                    payoffDate = payoffrow["expect_date"]
                    mode=""
                    if phaseMode == 1 :
                        mode="%d天" % (phaseTotal)
                    elif phaseMode == 2:
                        mode="%d月" % (phaseTotal)
                    elif phaseMode == 3:
                        mode="%d年" % (phaseTotal)
                    f.write("%s,%s,%s,%s,%s\n" % (assetId,mode,fullTime,repayDate,payoffDate))


getSql()















