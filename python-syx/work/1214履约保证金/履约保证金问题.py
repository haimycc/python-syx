import os
import datetime, time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

#new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='asset')
#new_cursor = new_conn.cursor(dictionary=True)
new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='invest', charset='utf8')
new_cursor = new_conn.cursor(dictionary=True)

def hander():
    assetSql = "select asset_id,borrower_uid from asset.t_asset where state=2";
    new_cursor.execute(assetSql)
    lists = new_cursor.fetchall()
    for list in lists:
        assetId = list["asset_id"]
        userId = list["borrower_uid"]
        for suffix in range(0, 100):
            sql = str.format(
                "select loan_id from asset.t_asset_fee_%02d where loan_id=%d AND fee_node=3 AND fee_state=0 " % (
                suffix, assetId))
            # print("费用sql=" + sql)
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                accountSql = str.format(
                    "select loan_id from account.t_user_account_flow_%02d where WHERE loan_id=%d AND uid=%d AND bus_type = 23 " % (
                    suffix, assetId, userId))
                print(str.format("履约保证金有问题：userId=%d,assetId=%d" % (userId, assetId)))
                print("update asset.t_asset set state=3,update_time=NOW() WHERE asset_id=%d and borrower_uid=%d  AND state=2;" % (assetId, userId))
                print("update asset.t_asset_fee_%02d set fee_state=1,update_time=NOW() WHERE loan_id=%d AND fee_node=3 AND fee_state=0;" % (suffix,assetId))



hander()
