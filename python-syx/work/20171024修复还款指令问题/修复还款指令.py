# -*- coding:utf-8 -*-
#encoding=utf-8
import mysql.connector
import codecs

new_conn = mysql.connector.connect(host='192.168.31.222', user='root', password='123456', database='invest', charset='utf8')

new_cursor = new_conn.cursor(dictionary=True)
file = open("D:\还款指令.txt", "w")
f = codecs.open("D:\还款指令.txt", "w","utf-8")




def hander():
    select_sql = "SELECT asset_name,asset_id FROM  asset.t_asset  WHERE business_type=201706220005812 AND need_call_to_repay=1"
    new_cursor.execute(select_sql)
    resAll = new_cursor.fetchall()
    for res in resAll:
        # print(res)
        update_sql = "update asset.t_asset set need_call_to_repay=0,update_time=now() WHERE business_type=201706220005812  AND need_call_to_repay=1 and asset_id=%s;" % (str(res["asset_id"]))
        print(update_sql)
        f.write(update_sql + "\n")
    file.close()
    f.close()
hander()
