import os
import time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

def getFeeAmount(fee_standard,fee_ispercent):
    if fee_ispercent



#未到product库/预计收费
def getFeeAllExpectBefore(assetId):
    sql=str.format("select * from asset.t_asset_fee_%s where asset_id = %d and fee_node not in (51,52,53,54) " % (str(assetId)[-2:],assetId))


#未到product库/实际收费
def getFeeAllReceiveBefore(assetId):
    sql=str.format("select * from asset.t_asset_fee_%s where asset_id = %d and fee_node not in (51,52,53,54) and fee_state = 1 " % (str(assetId)[-2:],assetId))


#到了product库/预计收费
def getFeeAllExpectAfter(assetId):
    sql=str.format("select * from asset.t_asset_fee_%s where asset_id = %d and fee_node in (51,52,53,54) " % (str(assetId)[-2:],assetId))


# 到了product库/实际收费
def getFeeAllReceiveAfter(assetId):
    sql=str.format("select * from product.t_asset_fee_%s where asset_id = %d and fee_node in (51,52,53,54) " $ (str(assetId)[-2:],assetId))






