import mysql.connector

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='product')
new_cursor = new_conn.cursor(dictionary=True)

def handler(assetIds):
    split = assetIds.split(',')
    for assetId in split:
        sql = "SELECT * FROM asset.t_asset_fee_%s WHERE unfrozen_node=53 and loan_id=%s "%(assetId[-2:],assetId)
        new_cursor.execute(sql)
        fetchall = new_cursor.fetchall()
        print(fetchall)
        # print(sql)

handler("20170704000174956,"
"20170705000246942,"
"20170720000205171,"
"20170728000141665,"
"20170728000142465,"
"20170728000151430,"
"20170731000037055,"
"20170801000108340,"
"20170802000211396,"
"20170804000210565,"
"24049928810225773")


