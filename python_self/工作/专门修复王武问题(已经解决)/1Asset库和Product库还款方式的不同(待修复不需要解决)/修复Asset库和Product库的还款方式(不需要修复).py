import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :


    with open("修复Asset库和Product库借款方式不一致.sql","a+") as f:
        assetList=["空","信用借款","抵押借款","担保借款","质押借款"]
        productList=["无担保借款","担保借款","抵押借款","信用借款","质押借款"]
        sql="select a.asset_id as aid,a.borrower_borrowway as away,b.borrower_borrowway as bway,b.asset_property," \
            "b.asset_name," \
            "b.borrower_uid," \
            "b.borrower_name " \
            " from " \
            "asset.t_asset a,product.t_assets b " \
            "where " \
            "a.asset_id=b.asset_id " \
            "and " \
            "b.asset_type=0"
        new_cursor.execute(sql)
        assets = new_cursor.fetchall()
        for asset in assets :
            aid=asset["aid"]
            away=asset["away"]
            bway=asset["bway"]
            aName=asset["asset_name"]
            borrowerUid=asset["borrower_uid"]
            borrowerName=asset["borrower_name"]
            property=asset["asset_property"]
            straway=assetList[away]
            strbway=productList[bway]
            if straway != strbway :
                sql=str.format("update product.t_assets set borrower_borrowway = %d  where asset_id = %d and borrower_borrowway= %d " % ())










