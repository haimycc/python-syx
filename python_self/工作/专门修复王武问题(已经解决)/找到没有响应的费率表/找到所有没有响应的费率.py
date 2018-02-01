
import os
import mysql.connector
from datetime import datetime, date

idc_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='invest')
idc_cursor = idc_conn.cursor(dictionary=True)

def getAllNotRetrun():
    with open(os.path.abspath(os.curdir) + '/noReturn', 'a+') as f:
        #遍历所有费率表
        for suffix in range(0,100):
            print("check product.t_assets_fee_%02d" % (suffix))
            #找到所有transId
            selectSql= "select * from product.t_assets_fee_%02d where operation = 1" % suffix
            idc_cursor.execute(selectSql)
            results = idc_cursor.fetchall()
            for result in results:
                assetId = result["asset_id"]
                assetIdSuffix = str(assetId)[-2:]
                transId = result["trans_id"]
                remark = result["remark"]
                amount = result["fee_amount"]
                repSql="select * from product.t_assets_fee_%02d where trans_id = %d and operation = 2;" % (suffix,transId)
                idc_cursor.execute(repSql)
                represults = idc_cursor.fetchall()
                if len(represults) == 0 :
                    f.write("asset id is "+str(assetId)+","+"trans id is "+str(transId)+",amount is "+str(amount)+",remark is "+remark+"\n")
                    f.write()


if __name__ == "__main__" :
    getAllNotRetrun()

