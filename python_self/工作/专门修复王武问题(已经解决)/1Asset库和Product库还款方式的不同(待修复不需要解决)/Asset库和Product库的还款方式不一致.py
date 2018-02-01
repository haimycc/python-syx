import os
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.50.151', user='search', password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)

if __name__ == "__main__" :
    with open("Asset库和Product库借款方式不一致.csv","a+") as f:
        f.write("标的ID,标的名称,借款人UID,借款人姓名,Asset库借款方式,Product库借款方式,是否是老平台的标\n")
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
            isOld="否"
            if property & 65536 == 65536 :
                isOld="是"
            else:
                isOld="否"
            straway=assetList[away]
            strbway=productList[bway]
            f.write("%s,%s,%s,%s,%s,%s,%s\n" % (str(aid),str(aName),str(borrowerUid),str(borrowerName),str(straway),str(strbway),isOld))




