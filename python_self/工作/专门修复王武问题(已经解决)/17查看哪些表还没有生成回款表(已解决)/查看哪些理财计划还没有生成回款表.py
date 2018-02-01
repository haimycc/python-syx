import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getPayoff():
    sql="select asset_id from product.t_assets where asset_type=1 and asset_property & 65536 = 65536 and state = 8 ;"
    new_cursor.execute(sql)
    results = new_cursor.fetchall()
    for result in results:
        assetId=result["asset_id"]
        assetIdSuffix=str(assetId)[-2:]
        tmpSql="select * from specialDB.t_new_financial_plan_payoff where asset_id = %d" % (assetId)
        new_cursor.execute(tmpSql)
        tmpResults=new_cursor.fetchall()
        if len(tmpResults) == 0 :
            print("asset_id is %d " % (assetId))


if __name__ == "__main__" :
    getPayoff()
