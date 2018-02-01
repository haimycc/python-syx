import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='asset')
new_cursor = new_conn.cursor(dictionary=True)
if __name__ == "__main__" :
    with open("D:\\assetInfo.csv", "a+") as f:
        f.write("标ID,标名称,募资总额(分),费用名称,费用节点,费用金额(分)\n")
        feeMaps={}
        sql = str.format(
            "select *  from asset.t_asset_dict where dict_category = 'fee_type' " )
        new_cursor.execute(sql)
        feeLists = new_cursor.fetchall()
        for fee in feeLists:
            feeKey=fee["dict_key"]
            feeName=fee["dict_value"]
            feeMaps[feeKey]=feeName

        for suffix in range(0,100):
            sql=str.format("select a.asset_id,a.asset_name,a.total_amount,b.fee_type,b.fee_node,b.fee_standard,b.fee_ispercent from asset.t_asset a, asset.t_asset_fee_%02d b where a.asset_id = b.loan_id and b.fee_node = 51  order by b.loan_id,b.fee_type"% (suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                assetId = list["asset_id"]
                assetName = list["asset_name"]
                totalAmount = list["total_amount"]
                feeType = list["fee_type"]
                feeNode = list["fee_node"]
                feeStandard = list["fee_standard"]
                feeIspercent = list["fee_ispercent"]
                feeType = feeMaps.get(feeType,"None")
                totalAmount = totalAmount
                feeAmount = 0
                if feeIspercent == 1:
                    feeAmount = totalAmount * feeStandard // 10000 // 100
                elif feeIspercent == 0:
                    feeAmount = feeStandard // 100
                f.write(str("%s,%s,%s,%s,%s,%s\n") % (str(assetId),str(assetName),str(totalAmount),str(feeType),str(feeNode),str(feeAmount)))

