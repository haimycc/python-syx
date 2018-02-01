import os
import datetime,time
import dateutil.relativedelta
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.51.145',user='search',password='search@zyxr.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)
if __name__ == "__main__" :
    with open("D:\\productAssetInfo.csv", "a+") as f:
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
            sql=str.format("select a.asset_id,a.asset_name,a.total_amount,b.fee_type,b.fee_node,b.fee_amount from asset.t_asset a, product.t_assets_fee_%02d b where a.asset_id = b.asset_id and b.fee_node = 51 and b.operation = 2 order by b.asset_id,b.fee_type"% (suffix))
            new_cursor.execute(sql)
            lists = new_cursor.fetchall()
            for list in lists:
                assetId = list["asset_id"]
                assetName = list["asset_name"]
                totalAmount = list["total_amount"]
                feeType = list["fee_type"]
                feeNode = list["fee_node"]
                feeAmount = list["fee_amount"]
                feeType = feeMaps.get(feeType,"None")

                f.write(str("%s,%s,%s,%s,%s,%s\n") % (str(assetId),str(assetName),str(totalAmount),str(feeType),str(feeNode),str(feeAmount)))

