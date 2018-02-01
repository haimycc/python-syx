import os
import mysql.connector
from datetime import datetime, date

new_conn = mysql.connector.connect(host='192.168.50.151',user='search',password='search@zyxr.com', database='invest')
new_cursor = new_conn.cursor(dictionary=True)


def updateAsset():
    aid1=20161221000006606
    sql1=str.format("update product.t_assets set asset_property=asset_property-2 where asset_id=%d" % (aid1))
    investsql=str.format("select investment_id from product.t_investment_06 where asset_id=%d" % (aid1))
    new_cursor.execute(investsql)
    invests = new_cursor.fetchall()
    for invest in invests:
        investId=invest["investment_id"]
        sql2=str.format("update invest.t_investment_%s set asset_property=asset_property-2 where asset_id=%d and investment_id=%d" % (str(investId)[-2:],aid1,investId))
        sql3=str.format("update invest.t_investments set asset_property=asset_property-2 where asset_id=%d and investment_id=%d"% (aid1,investId))
        sql4=str.format("update product.t_investment_%s set asset_property=asset_property-2 where asset_id=%d and investment_id=%d" % (str(aid1)[-2:],aid1,investId))
        sql5=str.format("update financial.t_investment_%s set asset_property=asset_property-2 where asset_id=%d and investment_id=%d")




if __name__ == "__main__" :