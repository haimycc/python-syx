import mysql.connector

new_conn = mysql.connector.connect(host='172.27.48.181', user='search', password='search@zyfax.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)


# backup = open('D:\\backupsql.txt', "w")
# f = open('D:\\fixRepayData.txt', "w")

def fun(assetId):
    feeSql = "SELECT * FROM asset.t_asset_fee_{0} WHERE loan_id = {1} and fee_type=2;".format(str(assetId)[-2:],
                                                                                              assetId)
    print(feeSql)
    new_cursor.execute(feeSql)
    feeRows = new_cursor.fetchall()
    update_asset = "update asset.t_asset_fee_{0} set fee_standard=1250,update_time=NOW() WHERE loan_id={1} AND fee_type=2 AND fee_receiver=1 AND fee_standard={2} and fee_type=2;"
    for feeRow in feeRows:
        print(update_asset.format(str(assetId)[-2:], assetId, feeRow["fee_standard"]))
        print(("delete from asset.t_asset_fee_{0} where loan_id = {1} AND fee_type=5 AND fee_standard=4000;").format(str(assetId)[-2:], assetId))

    repaySql = "SELECT * FROM product.t_repayments WHERE asset_id=%d AND state=0;" % (assetId);
    new_cursor.execute(repaySql)
    repayRows = new_cursor.fetchall()
    update_sql = "update product.t_repayments set expect_pay_fee={0},update_time=now() where asset_id={1} and state=0 and expect_pay_fee={2};"
    update_sql2 = "update product.t_repayment_{0} set expect_pay_fee={1},update_time=now() where asset_id={2} and state=0 and expect_pay_fee={3};"
    for repayRow in repayRows:
        fee_off = int(repayRow["amount"] * 0.125 / 100)
        sql_format = update_sql.format(fee_off, assetId, repayRow['expect_pay_fee'])
        sql_format2 = update_sql2.format(str(assetId)[-2:], fee_off, assetId, repayRow['expect_pay_fee'])
        print(sql_format)
        print(sql_format2)

        # backup.close()
        # f.close()

def all_fun(assetIds):
    for assetId in assetIds:
        fun(assetId)

assetIds=[26489067830253798,
          26494885820248322,
          26494826120248038,
          26494937720249172,
          26485808630231381,
          26485779130231231,
          26469529530277499,
          26435786420297324,
          26418013230264021,
          26409841530256895,
          26409347130245573,
          26409373720221687,
          26408411820212951,
          26357742120206684,
          26314385430208658,
          26314515830210336,
          26314454730209405,
          26304012720243409,
          26304126530263028,
          26237859530251423,
          26237810120233664,
          26236438520225666,
          26227639030233593]
all_fun(assetIds)
