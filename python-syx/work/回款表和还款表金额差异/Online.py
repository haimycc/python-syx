# select asset_id,business_name,asset_name FROM t_assets WHERE full_time>20170320 AND state=8;
import mysql.connector

new_conn = mysql.connector.connect(host='192.168.51.145', user='search', password='search@zyxr.com', database='product')
new_cursor = new_conn.cursor(dictionary=True)

def handler(time):
    sql = "select asset_id,business_name,asset_name,full_time FROM product.t_assets WHERE full_time>'%s' AND state=8" % (time)
    new_cursor.execute(sql)
    assetIds = new_cursor.fetchall()
    for assetId in assetIds:
        print(assetId)


handler('2017-03-22 11:00:00')