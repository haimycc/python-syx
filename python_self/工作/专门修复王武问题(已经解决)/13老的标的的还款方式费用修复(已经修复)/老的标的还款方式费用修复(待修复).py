import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("./updateRepayment.sql", "a+") as f:
        AssetMaps={}
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
                sum=AssetMaps.get(assetId,0)
                sum+=feeAmount
                AssetMaps[assetId]=sum

        for assetId,sum in AssetMaps.items():
            sql1="update product.t_repayment_%s set expect_pay_fee = %d where asset_id = %d and expect_pay_fee = 0 ;\n" % (str(assetId)[-2:],sum,assetId)
            sql2="update product.t_repayments set expect_pay_fee = %d where asset_id = %d and expect_pay_fee = 0 ;\n" % (sum,assetId)
            #print(sql1)
            #print(sql2)
            f.write(sql1)
            f.write(sql2)
            sql3="select asset_id,repayment_id,expect_pay_fee from product.t_repayment_%s where asset_id = %d and expect_pay_fee !=0 and expect_pay_fee != %d " % (str(assetId)[-2:],assetId,sum)
            new_cursor.execute(sql3)
            lists = new_cursor.fetchall()
            for list in lists:
                assetId=list["asset_id"]
                oldfee=list["expect_pay_fee"]
                sql3="update product.t_repayment_%s set expect_pay_fee = %d where asset_id = %d and expect_pay_fee = %d ;\n" % (str(assetId)[-2:],sum,assetId,oldfee)
                sql4="update product.t_repayments set expect_pay_fee = %d where asset_id = %d and expect_pay_fee = %d ; \n" % (sum,assetId,oldfee)
                f.write(sql3)
                f.write(sql4)






