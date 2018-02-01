import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./提表需求.csv","a+") as f:
        for suffix in range(0,100):
            sql=str.format("select b.asset_name,b.full_time,b.total_amount,b.annual_rate,b.phase_mode,b.phase_total,b.finish_time,c.mobile,a.investor_uid,a.amount from invest.t_investment_%02d a,product.t_assets b,user.t_user c  where a.asset_id=b.asset_id and b.asset_type=1 and a.investor_uid=c.id and a.state in (2,4,7) and a.create_time >= '2016-11-03 00:00:00' and a.create_time <= '2016-12-31 23:59:59' " % (suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                assetName = list["asset_name"]
                fullTime = list["full_time"]
                totalAmount=list["total_amount"]
                annualRate=list["annual_rate"]
                phaseMode=list["phase_mode"]
                if phaseMode == 1 :
                    phaseMode="日"
                elif phaseMode ==2 :
                    phaseMode="月"
                elif phaseMode ==3 :
                    phaseMode="年"
                phaseTotal=list["phase_total"]
                finishTime=list["finish_time"]
                mobile=list["mobile"]
                investorUid=list["investor_uid"]
                amount=list["amount"]
                print(str.format("%s,%s,%d,%d,%d,%s,%s,%s,%d,%d" % (assetName,fullTime,totalAmount,annualRate,phaseTotal,phaseMode,finishTime,mobile,investorUid,amount)))
                f.write(str.format("%s,%s,%d,%d,%d,%s,%s,%s,%d,%d\n" % (assetName,fullTime,totalAmount,annualRate,phaseTotal,phaseMode,finishTime,mobile,investorUid,amount)))
