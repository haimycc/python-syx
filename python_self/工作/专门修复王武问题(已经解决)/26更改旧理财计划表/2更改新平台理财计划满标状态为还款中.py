# -*- coding:utf-8 -*-

import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def updateNewFinancialPlan() :
    f=open("./2updateSql","a+")
    sql=" select asset_id,state,business_name,asset_name,match_time from product.t_assets  where asset_type = 1 and asset_property & 65536 !=65536 and state = 6 and match_time != '0000-00-00 00:00:00';"
    new_cursor.execute(sql)
    results = new_cursor.fetchall()
    for result in results:
        assetId=result["asset_id"]
        state=result["state"]
        updateSql1="update product.t_assets set state=%d  where asset_id=%d and state = %d and asset_type = 1 and asset_property & 65536 !=65536 and state = 6  and match_time != '0000-00-00 00:00:00';" % (8,assetId,state)
        print(updateSql1)
        f.write(updateSql1+"\n")
    f.close()



if __name__ == "__main__" :
    updateNewFinancialPlan()
