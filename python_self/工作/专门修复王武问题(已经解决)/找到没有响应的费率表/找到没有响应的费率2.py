
import os
import mysql.connector
from datetime import datetime, date

idc_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
idc_cursor = idc_conn.cursor(dictionary=True)

def getAllNotRequest():
    #遍历所有费率表
    for suffix in range(0,100):
        print("check product.t_assets_fee_%02d" % (suffix))
        #找到所有transId
        selectSql= "select * from product.t_assets_fee_%02d where operation = 2" % suffix
        idc_cursor.execute(selectSql)
        results = idc_cursor.fetchall()
        for result in results:
            assetId = result["asset_id"]
            transId = result["trans_id"]
            repSql="select * from product.t_assets_fee_%02d where trans_id = %d and operation = 1" % (suffix,transId)
            idc_cursor.execute(repSql)
            represults = idc_cursor.fetchall()
            if len(represults) == 0 :
                print("select * from product.t_assets_fee_%02d where asset_id = %d and trans_id = %d;" % (suffix,assetId,transId))


if __name__ == "__main__" :
    getAllNotRequest()

