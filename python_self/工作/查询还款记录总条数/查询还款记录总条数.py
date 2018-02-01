import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    sql=str.format("select asset_id,phase_total from product.t_assets where state in (8,9) and asset_type = 0 ")
    new_cursor.execute(sql)
    lists = new_cursor.fetchall()
    for list in lists:
        assetId=list["asset_id"]
        phaseTotal=list["phase_total"]
        sql2=str.format("select count(1) as count from product.t_repayment_%s where asset_id = %d " % (str(assetId)[-2:],assetId))
        new_cursor.execute(sql2)
        repayList = new_cursor.fetchall()
        for repay in repayList:
            amountTotal=repay["count"]
            if phaseTotal!=amountTotal:
                if amountTotal == 0 :
                    print("error!!!!!!!!!!!!!!!!!!!!!!!!,asset_id is %d " % (assetId))
                print("product.t_assets:asset id is %d,phaseTotal is %d,product.t_repayments:count is %d" %(assetId,phaseTotal,amountTotal))


